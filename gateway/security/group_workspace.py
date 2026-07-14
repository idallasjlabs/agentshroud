# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Group workspace manager — SCRUM-67 WS-A.

Turns a Telegram GROUP into a shared team workspace. A group chat_id maps to a
single canonical workspace/context id (``group-{chat_id}``) that all members of
that group share. Access is member-gated and fail-closed:

  - Only members of the group (or the system owner) can resolve the group's
    workspace or read/write its shared memory.
  - Non-members, unknown groups, and (when the feature is disabled) everyone are
    DENIED with a ``GroupAccessDenied`` exception — never a silent fallthrough.
  - Cross-group isolation is guaranteed by construction: the workspace id is
    derived from the group's own chat_id, so a member of group A can never
    obtain group B's workspace id, and membership is checked per-group.
  - A direct-message (DM) context — ``group_chat_id is None`` — resolves to a
    distinct per-user namespace (``dm-{user_id}``) that is never a group
    workspace, keeping private DMs isolated from every group.

This module reuses the existing group infrastructure rather than rebuilding it:
  - ``gateway.security.group_config.TeamsConfig`` for membership.
  - ``gateway.security.rbac_config.RBACConfig`` for system-owner override.
  - ``gateway.security.shared_memory.SharedMemoryManager`` for the isolated
    per-namespace memory storage (group vs DM).

Wired into the inbound Telegram path (``gateway/proxy/telegram_proxy.py``) at the
point where the active group chat_id contextvar is resolved, so a non-member's
message in a group can never be serviced against that group's shared workspace.

IEC 62443 FR3 (SL3): per-identity access control on every group workspace
resolution. IEC 62443 FR7 (SL2): resource isolation between team workspaces.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:  # pragma: no cover - typing only
    from gateway.security.group_config import TeamsConfig
    from gateway.security.rbac_config import RBACConfig
    from gateway.security.shared_memory import SharedMemoryManager

logger = logging.getLogger("agentshroud.security.group_workspace")

# Sentinel prefixes for the two workspace namespaces.
_GROUP_WORKSPACE_PREFIX = "group-"
_DM_WORKSPACE_PREFIX = "dm-"


class GroupAccessDenied(PermissionError):
    """Raised when a user is not permitted to access a group workspace.

    Subclasses ``PermissionError`` so callers that already treat permission
    failures uniformly (e.g. the inbound guard) catch it naturally.
    """


@dataclass(frozen=True)
class WorkspaceContext:
    """Resolved workspace/context identity for a single inbound message.

    Attributes:
        workspace_id: Canonical, isolated namespace id. ``group-{chat_id}`` for a
            group workspace, ``dm-{user_id}`` for a direct message.
        group_chat_id: The originating group chat_id, or ``None`` for a DM.
        user_id: The requesting Telegram user id.
        is_group: True if this is a shared group workspace, False for a DM.
    """

    workspace_id: str
    group_chat_id: Optional[str]
    user_id: str
    is_group: bool


class GroupWorkspaceManager:
    """Resolve and access-control shared group workspaces.

    Args:
        teams_config: TeamsConfig carrying group membership. If ``None``, every
            group access fails closed (DMs still resolve to their own namespace).
        rbac_config: Optional RBACConfig used to grant the system owner access to
            any group for oversight. ``None`` disables the owner override.
        shared_memory: Optional SharedMemoryManager used to read/write the
            isolated per-namespace memory. Required for the memory helpers.
        enabled: Feature gate. When ``False`` the manager fails closed on all
            group resolutions (default-safe rollout); DM resolution is
            unaffected because a DM is not a shared group workspace.
    """

    def __init__(
        self,
        teams_config: Optional["TeamsConfig"],
        rbac_config: Optional["RBACConfig"] = None,
        shared_memory: Optional["SharedMemoryManager"] = None,
        enabled: bool = True,
    ) -> None:
        self.teams_config = teams_config
        self.rbac_config = rbac_config
        self._memory = shared_memory
        self.enabled = bool(enabled)

    # ------------------------------------------------------------------
    # Namespace id helpers
    # ------------------------------------------------------------------

    @staticmethod
    def group_workspace_id(group_chat_id: str) -> str:
        """Canonical workspace id for a group chat_id: ``group-{chat_id}``."""
        return f"{_GROUP_WORKSPACE_PREFIX}{group_chat_id}"

    @staticmethod
    def dm_workspace_id(user_id: str) -> str:
        """Canonical workspace id for a direct-message context: ``dm-{user_id}``."""
        return f"{_DM_WORKSPACE_PREFIX}{user_id}"

    # ------------------------------------------------------------------
    # Membership resolution
    # ------------------------------------------------------------------

    def _is_owner(self, user_id: str) -> bool:
        """Return True if user_id is the system owner (oversight override)."""
        if self.rbac_config is None:
            return False
        is_owner = getattr(self.rbac_config, "is_owner", None)
        if not callable(is_owner):
            return False
        try:
            return bool(is_owner(user_id))
        except Exception:  # pragma: no cover - defensive; RBAC never raises here
            return False

    def can_access(self, group_chat_id: Optional[str], user_id: str) -> bool:
        """Return True if user_id may access the workspace for ``group_chat_id``.

        A DM context (``group_chat_id is None``) is always accessible by its own
        user — it is that user's private namespace, not a shared group workspace.

        For a group context, access requires (fail-closed):
          - the feature is enabled, AND
          - a TeamsConfig is present with a matching group, AND
          - the user is a member of that group OR is the system owner.
        """
        # DM context: a user always owns their own DM namespace.
        if group_chat_id is None:
            return True

        if not self.enabled:
            logger.debug(
                "GroupWorkspace DENIED (feature disabled): user=%s group=%s",
                user_id,
                group_chat_id,
            )
            return False

        if self.teams_config is None:
            logger.debug(
                "GroupWorkspace DENIED (no teams config): user=%s group=%s",
                user_id,
                group_chat_id,
            )
            return False

        # System owner may access any group for oversight.
        if self._is_owner(user_id):
            return True

        group = self.teams_config.groups.get(self.group_workspace_id(group_chat_id))
        if group is None:
            # Fall back to a raw-key lookup in case a group is keyed by chat_id.
            group = self.teams_config.groups.get(str(group_chat_id))
        if group is None:
            logger.warning(
                "GroupWorkspace DENIED (unknown group): user=%s group=%s",
                user_id,
                group_chat_id,
            )
            return False

        allowed = group.is_member(user_id)
        if not allowed:
            logger.warning(
                "GroupWorkspace DENIED (non-member): user=%s group=%s",
                user_id,
                group_chat_id,
            )
        return allowed

    def resolve_workspace(self, group_chat_id: Optional[str], user_id: str) -> WorkspaceContext:
        """Resolve the workspace/context for an inbound message, fail-closed.

        Returns:
            WorkspaceContext with the canonical, isolated workspace id.

        Raises:
            GroupAccessDenied: if this is a group context and the user is not a
                member (or the feature is disabled / group unknown / no config).
        """
        if group_chat_id is None:
            return WorkspaceContext(
                workspace_id=self.dm_workspace_id(user_id),
                group_chat_id=None,
                user_id=str(user_id),
                is_group=False,
            )

        if not self.can_access(group_chat_id, user_id):
            raise GroupAccessDenied(
                f"user '{user_id}' is not permitted to access group workspace " f"'{group_chat_id}'"
            )

        return WorkspaceContext(
            workspace_id=self.group_workspace_id(group_chat_id),
            group_chat_id=str(group_chat_id),
            user_id=str(user_id),
            is_group=True,
        )

    # ------------------------------------------------------------------
    # Member-gated memory access (isolated per namespace)
    # ------------------------------------------------------------------

    def _require_memory(self) -> "SharedMemoryManager":
        if self._memory is None:
            raise RuntimeError(
                "GroupWorkspaceManager has no SharedMemoryManager wired; "
                "memory operations are unavailable"
            )
        return self._memory

    def read_group_memory(self, group_chat_id: str, user_id: str) -> str:
        """Read a group's shared memory, gated by member access (fail-closed)."""
        ws = self.resolve_workspace(group_chat_id, user_id)
        return self._require_memory().get_group_memory(ws.workspace_id)

    def append_group_memory(self, group_chat_id: str, user_id: str, content: str) -> None:
        """Append to a group's shared memory, gated by member access (fail-closed)."""
        ws = self.resolve_workspace(group_chat_id, user_id)
        self._require_memory().append_to_group_memory(
            ws.workspace_id, content, author_id=str(user_id)
        )

    def read_dm_memory(self, user_id: str, bot_id: str = "openclaw") -> str:
        """Read a user's private DM memory (isolated from every group)."""
        return self._require_memory().get_user_memory(user_id, bot_id=bot_id)

    def append_dm_memory(self, user_id: str, content: str, bot_id: str = "openclaw") -> None:
        """Append to a user's private DM memory (isolated from every group)."""
        self._require_memory().append_to_user_memory(user_id, content, bot_id=bot_id)
