# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Cron job failure monitor (SCRUM-61 part 2).

Detection half of cron/job failure alerting.  Polls the bots' persisted cron
job stores (mounted read-only into the gateway container — no bot-code
changes) and dispatches through AlertDispatcher when a job transitions into
failure, so the owner hears about a dead cron within one poll interval
instead of at the next weekly review.

Supported store schemas (normalized in :meth:`parse_store`):

- OpenClaw ``jobs.json``: ``{"jobs": [{id, name, enabled,
  state: {lastStatus, consecutiveErrors, ...}}]}`` (top-level list also
  accepted)
- Hermes ``jobs.json``: ``{"jobs": [{id, name, enabled, last_status,
  last_error, ...}]}``

Alerting policy:

- ok→fail transition (or first sight of a failing job) → HIGH alert, once
  per failure episode
- ``consecutiveErrors`` reaching :data:`_CRITICAL_CONSECUTIVE` while an
  episode is open → one CRITICAL escalation
- recovery (fail→ok) closes the episode; a later failure re-alerts
- alert ids are stable per (bot, job, episode) so AlertDispatcher's 24 h
  dedup absorbs monitor restarts without re-pinging the owner
- unreadable/corrupt stores are tolerated silently at DEBUG — a missing
  volume mount must not crash the gateway
"""

from __future__ import annotations

import asyncio
import hashlib
import json
import logging
import os
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Callable

logger = logging.getLogger("agentshroud.security.cron_state_monitor")

_FAIL_STATUSES = {"error", "fail", "failed"}
_CRITICAL_CONSECUTIVE = 3
_STORE_MAX_BYTES = 5 * 1024 * 1024  # a jobs.json beyond 5 MB is abuse, not config
_MAX_NEW_EPISODES_PER_PASS = 5  # per bot; excess folds into ONE aggregate alert
_DEFAULT_INTERVAL_SECONDS = float(os.environ.get("AGENTSHROUD_CRON_MONITOR_INTERVAL", "60"))


@dataclass
class JobState:
    """Normalized view of one bot cron job."""

    bot: str
    job_id: str
    name: str
    failing: bool
    consecutive_errors: int
    error: str | None
    last_run: str | None


class CronStateMonitor:
    """Poll bot cron stores; dispatch AlertDispatcher alerts on failures."""

    def __init__(
        self,
        stores: dict[str, str],
        dispatch_fn: Callable[[dict], dict],
        interval_seconds: float = _DEFAULT_INTERVAL_SECONDS,
    ) -> None:
        self._stores = dict(stores)
        self._dispatch = dispatch_fn
        self._interval = interval_seconds
        # (bot, job_id) → {"episode": str, "escalated": bool} for OPEN
        # failure episodes; absence means the job was last seen healthy.
        self._open_episodes: dict[tuple[str, str], dict[str, Any]] = {}
        # Per-key episode sequence: incremented on recovery so re-failures
        # get fresh alert ids.  In-memory only — a gateway restart during an
        # OPEN episode reproduces seq 0 and dedups (desired); the pathological
        # recover+refail entirely within a restart window may dedup once
        # (documented trade-off).
        self._episode_seq: dict[tuple[str, str], int] = {}
        self._task: asyncio.Task | None = None
        self._stop = asyncio.Event()

    # ------------------------------------------------------------------
    # Parsing
    # ------------------------------------------------------------------

    @staticmethod
    def parse_store(bot: str, path: str) -> list[JobState]:
        """Read one bot's cron store; tolerate absence/corruption."""
        try:
            if os.stat(path).st_size > _STORE_MAX_BYTES:
                logger.warning(
                    "cron store %s exceeds %d bytes — skipped (possible abuse)",
                    path,
                    _STORE_MAX_BYTES,
                )
                return []
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
        except (OSError, json.JSONDecodeError) as exc:
            logger.debug("cron store %s unreadable (%s) — skipped", path, exc)
            return []

        raw_jobs = data if isinstance(data, list) else data.get("jobs", [])
        if not isinstance(raw_jobs, list):
            return []
        jobs: list[JobState] = []
        for raw in raw_jobs:
            if not isinstance(raw, dict) or raw.get("enabled") is False:
                continue
            # The store is BOT-CONTROLLED input: one crafted job must never
            # blind the rest of the store (review finding — a ValueError
            # from int() used to discard the whole pass).
            try:
                state = raw.get("state")
                if isinstance(state, dict):  # OpenClaw shape
                    status = str(state.get("lastStatus", "")).lower()
                    try:
                        consecutive = int(state.get("consecutiveErrors") or 0)
                    except (TypeError, ValueError):
                        consecutive = 0
                    error = None
                    last_run = str(state.get("lastRunAtMs") or "") or None
                else:  # Hermes shape (flat fields)
                    status = str(raw.get("last_status", "")).lower()
                    consecutive = 1 if status in _FAIL_STATUSES else 0
                    error = raw.get("last_error")
                    last_run = raw.get("last_run_at")
                jobs.append(
                    JobState(
                        bot=bot,
                        job_id=str(raw.get("id", ""))[:128],
                        name=str(raw.get("name", "unnamed job"))[:120],
                        failing=status in _FAIL_STATUSES,
                        consecutive_errors=max(0, consecutive),
                        error=str(error)[:300] if error else None,
                        last_run=str(last_run)[:64] if last_run else None,
                    )
                )
            except Exception as exc:
                logger.debug("cron store %s: malformed job skipped (%s)", path, exc)
        return jobs

    # ------------------------------------------------------------------
    # Polling
    # ------------------------------------------------------------------

    def check(self) -> None:
        """One poll pass over all stores.  Never raises."""
        for bot, path in self._stores.items():
            try:
                new_this_pass = 0
                overflow: list[JobState] = []
                for job in self.parse_store(bot, path):
                    new_this_pass += self._evaluate(job, new_this_pass, overflow)
                if overflow:
                    self._dispatch_aggregate(bot, overflow)
            except Exception as exc:
                logger.warning("cron monitor pass failed for %s: %s", bot, exc)

    def _evaluate(self, job: JobState, new_this_pass: int, overflow: list[JobState]) -> int:
        """Evaluate one job.  Returns 1 if a NEW episode was alerted.

        Flood guard (review finding): a compromised bot can fabricate
        thousands of unique failing job ids; unlimited per-job HIGH alerts
        would exhaust AlertDispatcher's shared 10/h budget and starve OTHER
        security modules' critical alerts.  Beyond
        _MAX_NEW_EPISODES_PER_PASS new episodes per bot per pass, jobs are
        folded into a single aggregate alert.
        """
        key = (job.bot, job.job_id)
        episode = self._open_episodes.get(key)

        if not job.failing:
            if episode is not None:
                logger.info("cron job recovered: %s/%s", job.bot, job.name)
                # Bump the per-key episode sequence so the NEXT failure gets
                # a fresh alert id — AlertDispatcher's 24 h id-dedup must not
                # swallow the re-alert when last_run never advanced (review
                # finding; the old id was derived from last_run alone).
                self._episode_seq[key] = self._episode_seq.get(key, 0) + 1
                del self._open_episodes[key]
            return 0

        if episode is None:
            if new_this_pass >= _MAX_NEW_EPISODES_PER_PASS:
                overflow.append(job)
                # Still open the episode (silently) so the aggregate isn't
                # re-sent every pass for the same jobs.
                self._open_episodes[key] = {
                    "episode": self._episode_id(job, self._episode_seq.get(key, 0)),
                    "escalated": False,
                    "observed_failures": max(1, job.consecutive_errors),
                    "last_run_seen": job.last_run,
                }
                return 1
            episode_id = self._episode_id(job, self._episode_seq.get(key, 0))
            self._open_episodes[key] = {
                "episode": episode_id,
                "escalated": False,
                "observed_failures": max(1, job.consecutive_errors),
                "last_run_seen": job.last_run,
            }
            self._safe_dispatch(job, "HIGH", episode_id)
            return 1

        # Open episode: count OBSERVED failing runs ourselves (last_run
        # advancing while still failing = a new failed run).  Hermes's store
        # has no consecutiveErrors counter, so escalation must not depend on
        # the store's counter alone (review finding — CRITICAL was
        # unreachable for Hermes).
        if job.last_run != episode.get("last_run_seen"):
            episode["last_run_seen"] = job.last_run
            episode["observed_failures"] = episode.get("observed_failures", 1) + 1
        effective = max(job.consecutive_errors, episode.get("observed_failures", 1))
        if effective >= _CRITICAL_CONSECUTIVE and not episode["escalated"]:
            episode["escalated"] = True
            self._safe_dispatch(job, "CRITICAL", episode["episode"] + "-esc")
        return 0

    def _dispatch_aggregate(self, bot: str, jobs: list[JobState]) -> None:
        names = ", ".join(j.name for j in jobs[:10])
        alert = {
            "id": "cron-aggregate-"
            + hashlib.sha256(
                f"{bot}|{'|'.join(sorted(j.job_id for j in jobs))}".encode()
            ).hexdigest()[:16],
            "severity": "HIGH",
            "tool": "cron-scheduler",
            "message": (
                f"{len(jobs)} additional cron jobs failing on {bot} "
                f"(flood guard active): {names}"
            ),
            "details": {"bot": bot, "job_count": len(jobs)},
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        try:
            self._dispatch(alert)
        except Exception as exc:
            logger.warning("cron aggregate alert dispatch failed: %s", exc)

    def _safe_dispatch(self, job: JobState, severity: str, alert_id: str) -> None:
        message = (
            f"Cron job '{job.name}' ({job.bot}) is failing"
            f" — {job.consecutive_errors} consecutive error(s)."
        )
        if job.error:
            message += f" Last error: {job.error[:300]}"
        alert = {
            "id": alert_id,
            "severity": severity,
            "tool": "cron-scheduler",
            "message": message,
            "details": {
                "bot": job.bot,
                "job_id": job.job_id,
                "job_name": job.name,
                "consecutive_errors": job.consecutive_errors,
                "last_run": job.last_run,
            },
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        try:
            result = self._dispatch(alert)
            logger.info(
                "cron failure alert dispatched (%s): %s/%s → %s",
                severity,
                job.bot,
                job.name,
                result,
            )
        except Exception as exc:
            logger.warning("cron failure alert dispatch failed: %s", exc)

    @staticmethod
    def _episode_id(job: JobState, seq: int) -> str:
        raw = f"cron|{job.bot}|{job.job_id}|{job.last_run or ''}|{seq}"
        return "cron-" + hashlib.sha256(raw.encode()).hexdigest()[:16]

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def start(self) -> asyncio.Task:
        """Start the poll loop as an asyncio task (idempotent)."""
        if self._task is not None and not self._task.done():
            return self._task
        self._stop.clear()
        self._task = asyncio.get_running_loop().create_task(self._run())
        return self._task

    async def _run(self) -> None:
        logger.info(
            "CronStateMonitor started: stores=%s interval=%ss",
            list(self._stores),
            self._interval,
        )
        loop = asyncio.get_running_loop()
        while not self._stop.is_set():
            # File I/O + JSON parse off the event loop — a bot-controlled
            # store must not be able to stall gateway proxy traffic.
            await loop.run_in_executor(None, self.check)
            try:
                await asyncio.wait_for(self._stop.wait(), timeout=self._interval)
            except asyncio.TimeoutError:
                continue

    async def stop(self) -> None:
        self._stop.set()
        if self._task is not None:
            await asyncio.gather(self._task, return_exceptions=True)
