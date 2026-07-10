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
        self._task: asyncio.Task | None = None
        self._stop = asyncio.Event()

    # ------------------------------------------------------------------
    # Parsing
    # ------------------------------------------------------------------

    @staticmethod
    def parse_store(bot: str, path: str) -> list[JobState]:
        """Read one bot's cron store; tolerate absence/corruption."""
        try:
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
        except (OSError, json.JSONDecodeError) as exc:
            logger.debug("cron store %s unreadable (%s) — skipped", path, exc)
            return []

        raw_jobs = data if isinstance(data, list) else data.get("jobs", [])
        jobs: list[JobState] = []
        for raw in raw_jobs:
            if not isinstance(raw, dict) or raw.get("enabled") is False:
                continue
            state = raw.get("state")
            if isinstance(state, dict):  # OpenClaw shape
                status = str(state.get("lastStatus", "")).lower()
                consecutive = int(state.get("consecutiveErrors") or 0)
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
                    job_id=str(raw.get("id", "")),
                    name=str(raw.get("name", "unnamed job")),
                    failing=status in _FAIL_STATUSES,
                    consecutive_errors=consecutive,
                    error=str(error) if error else None,
                    last_run=last_run,
                )
            )
        return jobs

    # ------------------------------------------------------------------
    # Polling
    # ------------------------------------------------------------------

    def check(self) -> None:
        """One poll pass over all stores.  Never raises."""
        for bot, path in self._stores.items():
            try:
                for job in self.parse_store(bot, path):
                    self._evaluate(job)
            except Exception as exc:
                logger.warning("cron monitor pass failed for %s: %s", bot, exc)

    def _evaluate(self, job: JobState) -> None:
        key = (job.bot, job.job_id)
        episode = self._open_episodes.get(key)

        if not job.failing:
            if episode is not None:
                logger.info("cron job recovered: %s/%s", job.bot, job.name)
                del self._open_episodes[key]
            return

        if episode is None:
            # New failure episode.  The episode id is derived from the
            # job's last-run marker so a monitor restart reproduces the
            # same alert id and AlertDispatcher dedups it.
            episode_id = self._episode_id(job)
            self._open_episodes[key] = {"episode": episode_id, "escalated": False}
            self._safe_dispatch(job, "HIGH", episode_id)
        elif job.consecutive_errors >= _CRITICAL_CONSECUTIVE and not episode["escalated"]:
            episode["escalated"] = True
            self._safe_dispatch(job, "CRITICAL", episode["episode"] + "-esc")

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
    def _episode_id(job: JobState) -> str:
        raw = f"cron|{job.bot}|{job.job_id}|{job.last_run or ''}"
        return "cron-" + hashlib.sha256(raw.encode()).hexdigest()[:16]

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def start(self) -> asyncio.Task:
        """Start the poll loop as an asyncio task."""
        self._stop.clear()
        self._task = asyncio.get_running_loop().create_task(self._run())
        return self._task

    async def _run(self) -> None:
        logger.info(
            "CronStateMonitor started: stores=%s interval=%ss",
            list(self._stores),
            self._interval,
        )
        while not self._stop.is_set():
            self.check()
            try:
                await asyncio.wait_for(self._stop.wait(), timeout=self._interval)
            except asyncio.TimeoutError:
                continue

    async def stop(self) -> None:
        self._stop.set()
        if self._task is not None:
            await asyncio.gather(self._task, return_exceptions=True)
