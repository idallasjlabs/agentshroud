# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Gateway-level collaborator activity tracker.

Logs every non-owner message from configured collaborator IDs to a JSONL file
on the shared gateway-data volume. Provides summary and recent-activity queries
for the /collaborators API endpoint and management dashboard.
"""

from __future__ import annotations

import json
import logging
import os
import time
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional

logger = logging.getLogger("agentshroud.security.collaborator_tracker")

_PREVIEW_MAX = 80


class CollaboratorActivityTracker:
    """Tracks collaborator messages at the gateway level.

    Records every inbound message from a known collaborator user ID into a
    newline-delimited JSON log. The owner's messages are never logged here.

    Args:
        log_path: Absolute path to the .jsonl activity log file.
        owner_user_id: Telegram user ID of the workspace owner — excluded from tracking.
        collaborator_ids: List of Telegram user IDs that are tracked as collaborators.
    """

    def __init__(
        self,
        log_path: Path,
        owner_user_id: str,
        collaborator_ids: list[str],
        contributor_log_dir: Optional[Path] = None,
    ) -> None:
        self.log_path = log_path
        self.owner_user_id = str(owner_user_id)
        self.collaborator_ids: set[str] = {str(uid) for uid in (collaborator_ids or [])}
        self.track_unknown_non_owner = (
            str(os.environ.get("AGENTSHROUD_TRACK_ALL_NON_OWNER_ACTIVITY", "true")).strip().lower()
            not in ("0", "false", "no", "off")
        )
        self.contributor_log_dir = contributor_log_dir or Path(
            os.environ.get(
                "AGENTSHROUD_CONTRIBUTOR_LOG_DIR",
                "/data/bot-workspace/memory/contributors",
            )
        )
        configured_dirs = str(
            os.environ.get(
                "AGENTSHROUD_CONTRIBUTOR_LOG_DIRS",
                "/app/data/contributors",
            )
        )
        self.contributor_log_dirs: list[Path] = []
        for raw_dir in configured_dirs.split(","):
            candidate = Path(raw_dir.strip())
            if not raw_dir.strip():
                continue
            if candidate not in self.contributor_log_dirs:
                self.contributor_log_dirs.append(candidate)
        if self.contributor_log_dir not in self.contributor_log_dirs:
            self.contributor_log_dirs.append(self.contributor_log_dir)
        self._active_contributor_log_dirs: list[Path] = []

        # Ensure parent directory exists
        try:
            self.log_path.parent.mkdir(parents=True, exist_ok=True)
        except OSError as exc:
            logger.warning("CollaboratorActivityTracker: cannot create log dir: %s", exc)
        for log_dir in self.contributor_log_dirs:
            try:
                log_dir.mkdir(parents=True, exist_ok=True)
                self._active_contributor_log_dirs.append(log_dir)
            except OSError as exc:
                logger.info(
                    "CollaboratorActivityTracker: contributor dir unavailable (%s): %s",
                    log_dir,
                    exc,
                )
        if not self._active_contributor_log_dirs:
            logger.warning(
                "CollaboratorActivityTracker: no contributor log dirs writable; configured=%s",
                [str(p) for p in self.contributor_log_dirs],
            )

    def record_activity(
        self,
        user_id: str,
        username: str,
        message_preview: str,
        source: str,
    ) -> None:
        """Append one activity entry if user_id is a tracked collaborator.

        The owner is never logged. Unknown users are silently skipped.

        Args:
            user_id: Telegram user ID string.
            username: Display name (first_name or @username).
            message_preview: Raw message text, truncated to 80 chars for privacy.
            source: Ingress channel (e.g. "telegram").
        """
        uid = str(user_id)
        if uid == self.owner_user_id:
            return
        if uid not in self.collaborator_ids and self.track_unknown_non_owner:
            self.collaborator_ids.add(uid)
        if uid not in self.collaborator_ids:
            return

        normalized_preview = self._normalize_preview(message_preview)
        entry = {
            "timestamp": time.time(),
            "user_id": uid,
            "username": self._normalize_username(username),
            "message_preview": normalized_preview[:_PREVIEW_MAX],
            "source": source,
        }
        try:
            with self.log_path.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps(entry) + "\n")
        except OSError as exc:
            logger.warning("CollaboratorActivityTracker: write failed: %s", exc)
        self._append_contributor_log(entry)

    def _append_contributor_log(self, entry: dict) -> None:
        """Mirror activity into workspace contributor logs used by daily digests."""
        try:
            ts = float(entry.get("timestamp", time.time()))
            dt = datetime.fromtimestamp(ts, tz=timezone.utc)
            date_str = dt.strftime("%Y-%m-%d")
            uid = str(entry.get("user_id", "unknown"))
            safe_uid = "".join(ch for ch in uid if ch.isalnum() or ch in ("-", "_")) or "unknown"
            line = (
                f"- {dt.isoformat()} | {entry.get('username', 'unknown')} ({uid}) "
                f"| {entry.get('source', 'unknown')} | {entry.get('message_preview', '')}\n"
            )
            wrote = False
            for log_dir in self._active_contributor_log_dirs:
                try:
                    file_path = log_dir / f"{date_str}-{safe_uid}.md"
                    with file_path.open("a", encoding="utf-8") as fh:
                        fh.write(line)
                    wrote = True
                except OSError as exc:
                    logger.info(
                        "CollaboratorActivityTracker: contributor log write skipped (%s): %s",
                        log_dir,
                        exc,
                    )
            if not wrote:
                logger.warning("CollaboratorActivityTracker: contributor log write failed for all dirs")
        except OSError as exc:
            logger.warning("CollaboratorActivityTracker: contributor log write failed: %s", exc)

    @staticmethod
    def _normalize_preview(text: str) -> str:
        """Normalize previews to single-line safe text for JSONL + markdown mirrors."""
        value = str(text or "")
        # Collapse multiline/control characters to prevent malformed contributor logs.
        value = value.replace("\r", " ").replace("\n", " ").replace("\t", " ")
        value = " ".join(value.split())
        return value

    @staticmethod
    def _normalize_username(username: str) -> str:
        """Normalize username for safe contributor-log tokenization."""
        value = str(username or "unknown")
        value = value.replace("\r", " ").replace("\n", " ").replace("\t", " ")
        value = " ".join(value.split()) or "unknown"
        # Contributor logs use pipe + "(uid)" delimiters; keep username token stable.
        value = value.replace("|", "/").replace("(", "[").replace(")", "]")
        return value

    def get_activity(self, since: float = 0, limit: int = 100) -> list[dict]:
        """Return recent activity entries in chronological order.

        Args:
            since: Unix timestamp — only return entries after this time.
            limit: Maximum number of entries to return (most recent first).

        Returns:
            List of activity dicts, newest first.
        """
        if not self.log_path.exists():
            return []

        entries: list[dict] = []
        try:
            with self.log_path.open("r", encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                        if entry.get("timestamp", 0) > since:
                            entries.append(entry)
                    except json.JSONDecodeError:
                        continue
        except OSError as exc:
            logger.warning("CollaboratorActivityTracker: read failed: %s", exc)
            return []

        # Newest first, capped to limit
        entries.sort(key=lambda e: e.get("timestamp", 0), reverse=True)
        return entries[:limit]

    def get_activity_summary(self) -> dict:
        """Return aggregated statistics over all recorded activity.

        Returns:
            Dict with keys: total_messages, unique_users, last_activity, by_user.
        """
        if not self.log_path.exists():
            return {
                "total_messages": 0,
                "unique_users": 0,
                "last_activity": None,
                "by_user": {},
            }

        total = 0
        last_ts: Optional[float] = None
        by_user: dict[str, dict] = {}

        try:
            with self.log_path.open("r", encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue

                    total += 1
                    uid = entry.get("user_id", "unknown")
                    ts = entry.get("timestamp", 0)

                    if last_ts is None or ts > last_ts:
                        last_ts = ts

                    if uid not in by_user:
                        by_user[uid] = {
                            "username": entry.get("username", "unknown"),
                            "message_count": 0,
                            "last_active": ts,
                        }
                    by_user[uid]["message_count"] += 1
                    if ts > by_user[uid]["last_active"]:
                        by_user[uid]["last_active"] = ts
                        by_user[uid]["username"] = entry.get("username", by_user[uid]["username"])
        except OSError as exc:
            logger.warning("CollaboratorActivityTracker: summary read failed: %s", exc)

        return {
            "total_messages": total,
            "unique_users": len(by_user),
            "last_activity": last_ts,
            "by_user": by_user,
        }
