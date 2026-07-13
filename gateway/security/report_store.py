# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Gateway-managed multi-bot report store (SCRUM-79).

Both OpenClaw and Hermes generate reports (competitive intel, security
summaries) into their own container workspaces today, so pipelines get
duplicated and neither bot can consume the other's artifacts through a common
interface.  This is a single gateway-owned store on the shared gateway-data
volume, written and listed through the gateway API.

CONFIDENTIALITY BOUNDARY (be precise — no security theater): the gateway-data
volume is bind-mounted READ-ONLY into both bot containers, so a bot can read
the raw report files directly.  This store is therefore a **shared bulletin
board with NO per-bot read confidentiality** — every bot can see every report.
It is NOT access-controlled storage.  Consequences enforced here:
- ALL free-text fields (content, title, tags) are PII/secret-sanitized on
  write, because everything persisted is visible to every bot (the earlier
  design sanitized only content — a secret in a title would have leaked).
- the API layer's auth gates WRITE and gates reads-via-API, but it is not a
  confidentiality boundary against a compromised bot with raw volume access;
  if per-bot confidentiality is ever required, the store needs its own volume
  not mounted into the bots.

Storage model: one JSON file per report under ``<root>/<id>.json`` holding
metadata + sanitized content.  Restart-durable, no DB.  Bounded: at most
``max_reports`` (oldest pruned) so a spamming bot can't fill the shared volume
that also holds the ledger/audit/session DBs.

Safety posture:
- report ids are server-generated and path-safe; get/delete reject any id
  that isn't a bare 32-hex token, so a crafted id cannot traverse out of root
- content size capped (default matches the gateway's 1 MB request-body limit)
- report count bounded (oldest-pruned) — no unbounded disk growth
- corrupt files never break list()
"""

from __future__ import annotations

import hashlib
import inspect
import json
import logging
import os
import re
import uuid
from datetime import datetime, timezone
from typing import Any, Awaitable, Callable

logger = logging.getLogger("agentshroud.security.report_store")

_ID_RE = re.compile(r"^[a-f0-9]{32}$")  # server-generated ids only
# Matches the gateway's 1 MB request-body middleware — a larger store cap would
# be dead code (the body limit rejects first), so keep them consistent.
_DEFAULT_MAX_CONTENT_BYTES = 1 * 1024 * 1024
_DEFAULT_MAX_REPORTS = 5000
_BOT_MAX = 64
_TITLE_MAX = 256
_TAG_MAX = 64
_MAX_TAGS = 32


class ReportStore:
    """Filesystem-backed shared report store on the gateway-data volume."""

    def __init__(
        self,
        root: str,
        sanitize_fn: Callable[[str], str | Awaitable[str]] | None = None,
        max_content_bytes: int = _DEFAULT_MAX_CONTENT_BYTES,
        max_reports: int = _DEFAULT_MAX_REPORTS,
    ) -> None:
        self._root = root
        self._sanitize = sanitize_fn
        self._max_content_bytes = max_content_bytes
        self._max_reports = max_reports
        os.makedirs(self._root, exist_ok=True)

    # ------------------------------------------------------------------
    # Write
    # ------------------------------------------------------------------

    def save(
        self,
        bot: str,
        title: str,
        content: str,
        tags: list[str] | None = None,
    ) -> str:
        """Persist a report (sync sanitizer path); return its id.

        Sanitizes ALL free-text fields — everything persisted is visible to
        every bot, so nothing free-text may bypass redaction.
        """
        raw = self._check_size(content)
        clean = self._sanitize_sync
        return self._persist(bot, clean(title), clean(raw), [clean(t) for t in (tags or [])])

    async def save_async(
        self,
        bot: str,
        title: str,
        content: str,
        tags: list[str] | None = None,
    ) -> str:
        """Persist a report awaiting an async sanitizer (presidio) if injected.

        Sanitizes ALL free-text fields (content, title, tags).
        """
        raw = self._check_size(content)
        title_c = await self._sanitize_async(title)
        content_c = await self._sanitize_async(raw)
        tags_c = [await self._sanitize_async(t) for t in (tags or [])]
        return self._persist(bot, title_c, content_c, tags_c)

    # ------------------------------------------------------------------

    def _check_size(self, content: object) -> str:
        raw = content if isinstance(content, str) else str(content)
        if len(raw.encode("utf-8")) > self._max_content_bytes:
            raise ValueError(f"report content exceeds {self._max_content_bytes} bytes")
        return raw

    def _sanitize_sync(self, text: str) -> str:
        if self._sanitize is None:
            return text
        result = self._sanitize(text)
        if inspect.isawaitable(result):  # sync path can't await — refuse loudly
            raise RuntimeError("async sanitizer requires save_async(), not save()")
        return str(result)

    async def _sanitize_async(self, text: str) -> str:
        if self._sanitize is None:
            return text
        result = self._sanitize(text)
        return str(await result) if inspect.isawaitable(result) else str(result)

    def _persist(self, bot: str, title: str, content: str, tags: list[str]) -> str:
        report_id = uuid.uuid4().hex  # 32 hex chars — matches _ID_RE
        record = {
            "id": report_id,
            "bot": str(bot)[:_BOT_MAX],
            "title": str(title)[:_TITLE_MAX],
            "tags": [str(t)[:_TAG_MAX] for t in tags][:_MAX_TAGS],
            "content": content,
            "content_sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
            "created": datetime.now(timezone.utc).isoformat(),
        }
        path = self._path(report_id)
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(record, fh)
        os.replace(tmp, path)  # atomic publish
        logger.info(
            "report stored: id=%s bot=%s title=%s",
            report_id,
            record["bot"],
            record["title"],
        )
        self._enforce_count_cap()
        return report_id

    def _enforce_count_cap(self) -> None:
        """Prune oldest reports so the shared volume can't be filled."""
        metas = self.list()  # newest-first, metadata only
        if len(metas) <= self._max_reports:
            return
        for stale in metas[self._max_reports :]:
            rid = stale.get("id")
            if isinstance(rid, str):
                self.delete(rid)
        logger.warning(
            "report store at cap (%d) — pruned %d oldest",
            self._max_reports,
            len(metas) - self._max_reports,
        )

    # ------------------------------------------------------------------
    # Read
    # ------------------------------------------------------------------

    def get(self, report_id: str) -> dict[str, Any] | None:
        if not self._valid_id(report_id):
            return None
        try:
            with open(self._path(report_id), encoding="utf-8") as fh:
                return json.load(fh)
        except (OSError, json.JSONDecodeError):
            return None

    def list(self, bot: str | None = None) -> list[dict[str, Any]]:
        """Metadata (no content) for all reports, newest first.

        O(n) file reads per call; n is bounded by max_reports, so this stays
        cheap for the shared-bulletin-board use case.
        """
        items: list[dict[str, Any]] = []
        try:
            names = os.listdir(self._root)
        except OSError:
            return []
        for name in names:
            if not name.endswith(".json") or name.endswith(".tmp"):
                continue
            rid = name[:-5]
            if not self._valid_id(rid):
                continue
            rec = self.get(rid)
            if rec is None:
                continue
            if bot is not None and rec.get("bot") != bot:
                continue
            items.append({k: v for k, v in rec.items() if k != "content"})
        items.sort(key=lambda r: r.get("created", ""), reverse=True)
        return items

    def delete(self, report_id: str) -> bool:
        if not self._valid_id(report_id):
            return False
        try:
            os.remove(self._path(report_id))
            return True
        except OSError:
            return False

    # ------------------------------------------------------------------

    @staticmethod
    def _valid_id(report_id: object) -> bool:
        return isinstance(report_id, str) and bool(_ID_RE.match(report_id))

    def _path(self, report_id: str) -> str:
        # report_id is validated by _valid_id before this is reached on any
        # caller-supplied value; join stays inside root by construction.
        return os.path.join(self._root, f"{report_id}.json")
