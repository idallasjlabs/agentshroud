# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Group Shared Memory Manager (v0.9.0 Tranche 1)

Provides a high-level API for group shared memory + private memory isolation:

  - Each group has a shared MEMORY.md visible to all group members.
  - Each user retains a private MEMORY.md invisible to other users.
  - Owner sees everything; collaborators see only their own + their groups'.
  - Private-content patterns (admin credentials, API keys, etc.) are
    stripped before shared memory is served to non-owner users.

Architecture:
  SharedMemoryManager wraps UserSessionManager for storage.
  group workspaces live at:  <base>/groups/<group_id>/MEMORY.md
  user workspaces live at:   <base>/users/<user_id>/MEMORY.md
"""
from __future__ import annotations

import logging
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from gateway.security.session_manager import UserSessionManager
    from gateway.security.rbac_config import RBACConfig

logger = logging.getLogger("agentshroud.security.shared_memory")

# ---------------------------------------------------------------------------
# Private content patterns — stripped from shared/group memory before
# serving to non-owner collaborators.
# ---------------------------------------------------------------------------
_PRIVATE_PATTERNS: List[re.Pattern] = [
    # key/secret/token assignment — stays on one line to avoid bleeding into next
    re.compile(r"(?i)(api[_\s-]?key|secret|password|token|credential)[ \t]*[:=][ \t]*\S+"),
    re.compile(r"(?i)bearer\s+[A-Za-z0-9\-._~+/]+=*"),
    re.compile(r"(?i)sk-[A-Za-z0-9]{20,}"),         # OpenAI-style keys
    re.compile(r"(?i)[0-9]{10}:[A-Za-z0-9\-_]{35}"), # Telegram bot token shape
    re.compile(r"(?i)-----BEGIN [A-Z ]+-----[\s\S]+?-----END [A-Z ]+-----"),  # PEM blocks
    re.compile(r"\b[A-Z0-9]{20}\b"),                 # AWS access key shape (20-char uppercase)
]

_PRIVATE_SECTION_HEADER = re.compile(
    r"^#{1,3}\s*(admin|private|owner|credentials?|secrets?|keys?)\b",
    re.IGNORECASE | re.MULTILINE,
)


class SharedMemoryManager:
    """High-level shared-memory API wrapping UserSessionManager storage."""

    def __init__(self, session_manager: "UserSessionManager"):
        self._sm = session_manager

    # ------------------------------------------------------------------
    # Group memory
    # ------------------------------------------------------------------

    def get_group_memory(self, group_id: str) -> str:
        """Read raw group shared memory. Returns empty string if not yet created."""
        try:
            gs = self._sm.get_or_create_group_session(group_id)
            if gs.memory_file.exists():
                return gs.memory_file.read_text(encoding="utf-8", errors="replace")
        except Exception as exc:
            logger.warning("Could not read group memory for %s: %s", group_id, exc)
        return ""

    def append_to_group_memory(self, group_id: str, content: str, author_id: str) -> None:
        """Append a timestamped entry to the group shared memory file."""
        try:
            gs = self._sm.get_or_create_group_session(group_id)
            ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
            entry = f"\n---\n**[{ts}] {author_id}:**\n{content.strip()}\n"
            with open(gs.memory_file, "a", encoding="utf-8") as fh:
                fh.write(entry)
            logger.debug("Appended to group memory: group=%s author=%s bytes=%d", group_id, author_id, len(entry))
        except Exception as exc:
            logger.warning("Could not append to group memory for %s: %s", group_id, exc)

    # ------------------------------------------------------------------
    # User private memory
    # ------------------------------------------------------------------

    def get_user_memory(self, user_id: str) -> str:
        """Read raw private memory for a user."""
        try:
            sess = self._sm.get_or_create_session(user_id)
            if sess.memory_file.exists():
                return sess.memory_file.read_text(encoding="utf-8", errors="replace")
        except Exception as exc:
            logger.warning("Could not read user memory for %s: %s", user_id, exc)
        return ""

    def append_to_user_memory(self, user_id: str, content: str) -> None:
        """Append content to user's private memory file."""
        try:
            sess = self._sm.get_or_create_session(user_id)
            ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
            entry = f"\n---\n**[{ts}]**\n{content.strip()}\n"
            with open(sess.memory_file, "a", encoding="utf-8") as fh:
                fh.write(entry)
        except Exception as exc:
            logger.warning("Could not append to user memory for %s: %s", user_id, exc)

    # ------------------------------------------------------------------
    # Merged memory context for prompt injection
    # ------------------------------------------------------------------

    def get_merged_memory_for_user(
        self,
        user_id: str,
        rbac_config: "RBACConfig",
        active_group_id: Optional[str] = None,
    ) -> str:
        """Build merged memory context for bot prompt injection.

        Includes:
          1. User's own private memory (unfiltered).
          2. Shared memory of all groups the user belongs to (private-stripped).
             If active_group_id is set, that group's memory appears first.

        Owner receives unfiltered content; non-owners get private-stripped shared memory.

        Args:
            user_id: The requesting user.
            rbac_config: Used to determine group membership and owner status.
            active_group_id: Optional hint — prioritise this group's memory.

        Returns:
            Multi-section string suitable for prepending to bot system context.
        """
        is_owner = getattr(rbac_config, "is_owner", lambda _: False)(user_id)
        parts: List[str] = []

        # 1. User's private memory (always first, always unfiltered)
        private_mem = self.get_user_memory(user_id)
        if private_mem.strip():
            parts.append(f"[YOUR PRIVATE MEMORY]\n{private_mem}")

        # 2. Resolve accessible groups
        teams = getattr(rbac_config, "teams_config", None)
        if teams is None:
            return "\n\n---\n\n".join(parts) if parts else ""

        accessible_groups = []
        for gid, group in teams.groups.items():
            if is_owner or user_id in group.members:
                accessible_groups.append((gid, group))

        # Prioritise active_group_id
        if active_group_id:
            accessible_groups.sort(
                key=lambda item: (0 if item[0] == active_group_id else 1)
            )

        # 3. Append each group's shared memory
        for gid, group in accessible_groups:
            raw = self.get_group_memory(gid)
            if not raw.strip():
                continue
            filtered = raw if is_owner else self._strip_private_content(raw)
            if filtered.strip():
                parts.append(f"[GROUP MEMORY — {group.name}]\n{filtered}")

        return "\n\n---\n\n".join(parts) if parts else ""

    # ------------------------------------------------------------------
    # Topic-scoped context (multi-group resolution for project-scoped groups)
    # ------------------------------------------------------------------

    def get_topic_scoped_memory(
        self,
        user_id: str,
        rbac_config: "RBACConfig",
        query_text: str,
    ) -> str:
        """Return memory from groups whose focus_topics match the query text.

        For project_scoped groups, only return memory relevant to the query.
        Falls back to full merged memory if no topic match or no projects configured.
        """
        teams = getattr(rbac_config, "teams_config", None)
        if teams is None:
            return self.get_merged_memory_for_user(user_id, rbac_config)

        is_owner = getattr(rbac_config, "is_owner", lambda _: False)(user_id)
        parts: List[str] = []

        # Private memory always included
        private_mem = self.get_user_memory(user_id)
        if private_mem.strip():
            parts.append(f"[YOUR PRIVATE MEMORY]\n{private_mem}")

        for gid, group in teams.groups.items():
            if not (is_owner or user_id in group.members):
                continue

            # For project_scoped groups, check topic relevance
            if group.collab_mode == "project_scoped":
                project_matches = any(
                    teams.projects[pid].matches_topic(query_text)
                    for pid in group.projects
                    if pid in teams.projects
                )
                if not project_matches:
                    continue

            raw = self.get_group_memory(gid)
            if not raw.strip():
                continue
            filtered = raw if is_owner else self._strip_private_content(raw)
            if filtered.strip():
                parts.append(f"[GROUP MEMORY — {group.name}]\n{filtered}")

        return "\n\n---\n\n".join(parts) if parts else ""

    # ------------------------------------------------------------------
    # Private content detection / filtering
    # ------------------------------------------------------------------

    @staticmethod
    def contains_private_content(text: str) -> bool:
        """Return True if text contains patterns matching private/sensitive content."""
        if _PRIVATE_SECTION_HEADER.search(text):
            return True
        return any(p.search(text) for p in _PRIVATE_PATTERNS)

    @staticmethod
    def _strip_private_content(text: str) -> str:
        """Remove private-looking content from shared memory before serving
        to non-owner users.

        Strategy:
          1. Remove entire sections whose headers match private keywords.
          2. Redact inline pattern matches.
        """
        # Step 1: Remove private sections (header + content until next header)
        lines = text.splitlines(keepends=True)
        result_lines: List[str] = []
        skipping = False
        for line in lines:
            if _PRIVATE_SECTION_HEADER.match(line):
                skipping = True
                result_lines.append("[REDACTED — private section]\n")
                continue
            if skipping and re.match(r"^#{1,3}\s+\S", line):
                skipping = False  # next section, stop skipping
            if not skipping:
                result_lines.append(line)

        redacted = "".join(result_lines)

        # Step 2: Redact inline patterns
        for pattern in _PRIVATE_PATTERNS:
            redacted = pattern.sub("[REDACTED]", redacted)

        return redacted
