# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Gateway-managed multi-bot report store (SCRUM-79).

Both OpenClaw and Hermes generate reports (competitive intel, security
summaries) into their own container workspaces today, so neither can read the
other's artifacts and pipelines get duplicated.  This is a single gateway-owned
store on the shared gateway-data volume: bots write through the gateway API and
read each other's reports through it, with access mediated centrally (RBAC /
ToolACL at the API layer) instead of raw cross-container filesystem access.

Storage model: one JSON file per report under ``<root>/<id>.json`` holding both
metadata and content.  Simple, restart-durable, and trivially auditable — no
database dependency.  The store is the persistence + safety layer; the API
(``gateway/ingest_api``) is the access-control layer.

Safety posture (this is a security product):
- report ids are server-generated and path-safe; ``get``/``delete`` reject any
  id that isn't a bare token, so a crafted id cannot traverse out of the root
- content is PII-sanitized on write via an injected sanitizer (presidio in
  production) — reports are read by multiple bots, so secrets/PII must not
  persist in the shared store
- content size is capped; bot/title fields are length-bounded
- corrupt files never break ``list`` (one bad report can't hide the rest)
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
import re
import uuid
from datetime import datetime, timezone
from typing import Any, Callable

logger = logging.getLogger("agentshroud.security.report_store")

_ID_RE = re.compile(r"^[a-f0-9]{32}$")  # server-generated ids only
_DEFAULT_MAX_CONTENT_BYTES = 2 * 1024 * 1024  # 2 MB per report
_BOT_MAX = 64
_TITLE_MAX = 256


class ReportStore:
    """Filesystem-backed report store on the shared gateway-data volume."""

    def __init__(
        self,
        root: str,
        sanitize_fn: Callable[[str], str] | None = None,
        max_content_bytes: int = _DEFAULT_MAX_CONTENT_BYTES,
    ) -> None:
        self._root = root
        self._sanitize = sanitize_fn
        self._max_content_bytes = max_content_bytes
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
        """Persist a report; return its server-generated id.

        Raises ValueError if the content exceeds the size cap (before
        sanitization, to bound work).
        """
        raw = content if isinstance(content, str) else str(content)
        if len(raw.encode("utf-8")) > self._max_content_bytes:
            raise ValueError(f"report content exceeds {self._max_content_bytes} bytes")
        if self._sanitize is not None:
            raw = str(self._sanitize(raw))
        return self._persist(bot, title, raw, tags)

    async def save_async(
        self,
        bot: str,
        title: str,
        content: str,
        tags: list[str] | None = None,
    ) -> str:
        """Async save — awaits an async sanitizer (presidio) if injected.

        The API layer runs under asyncio and the production sanitizer is
        async; sync ``save`` stays for callers with a sync/no sanitizer.
        """
        import inspect

        raw = content if isinstance(content, str) else str(content)
        if len(raw.encode("utf-8")) > self._max_content_bytes:
            raise ValueError(f"report content exceeds {self._max_content_bytes} bytes")
        if self._sanitize is not None:
            result = self._sanitize(raw)
            raw = str(await result) if inspect.isawaitable(result) else str(result)
        return self._persist(bot, title, raw, tags)

    def _persist(self, bot: str, title: str, raw: str, tags: list[str] | None) -> str:
        report_id = uuid.uuid4().hex  # 32 hex chars — matches _ID_RE
        record = {
            "id": report_id,
            "bot": str(bot)[:_BOT_MAX],
            "title": str(title)[:_TITLE_MAX],
            "tags": [str(t)[:64] for t in (tags or [])][:32],
            "content": raw,
            "content_sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
            "created": datetime.now(timezone.utc).isoformat(),
        }
        path = self._path(report_id)
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(record, fh)
        os.replace(tmp, path)  # atomic publish
        logger.info(
            "report stored: id=%s bot=%s title=%s", report_id, record["bot"], record["title"]
        )
        return report_id

    # ------------------------------------------------------------------
    # Read
    # ------------------------------------------------------------------

    def get(self, report_id: str) -> dict[str, Any] | None:
        """Return the full report record, or None if missing/invalid id."""
        if not self._valid_id(report_id):
            return None
        path = self._path(report_id)
        try:
            with open(path, encoding="utf-8") as fh:
                return json.load(fh)
        except (OSError, json.JSONDecodeError):
            return None

    def list(self, bot: str | None = None) -> list[dict[str, Any]]:
        """Return metadata (no content) for all reports, newest first."""
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
        """Remove a report; return True if it existed."""
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
        # report_id is validated by _valid_id before this is called on any
        # caller-supplied value; join stays inside root by construction.
        return os.path.join(self._root, f"{report_id}.json")
