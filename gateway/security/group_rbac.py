# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Group-context RBAC — per-member role resolution for Telegram group workspaces.

Maps Telegram user IDs to per-group roles (owner / member / read-only) and
provides a high-risk tool classification list used to block read-only members
from triggering actions that route through the approval queue.

Architecture:
  GroupRoleResolver wraps a dict mapping:
    {group_chat_id: {user_id: role_string}}

  This mapping is populated at runtime from agentshroud.yaml `groups:` entries
  where each group can optionally carry a `roles:` sub-section. If no roles
  entry is present for a user, they default to GroupRole.READ_ONLY (deny-safe).

IEC 62443 FR3 (SL3): per-identity access control on every tool call in group context.
"""

from __future__ import annotations

import logging
from enum import Enum
from typing import Dict, Optional

logger = logging.getLogger("agentshroud.security.group_rbac")

# ---------------------------------------------------------------------------
# High-risk tools that require approval and are restricted to member+ roles.
# Read-only members receive an outright deny (not a queue entry).
# ---------------------------------------------------------------------------

_HIGH_RISK_TOOLS: frozenset[str] = frozenset(
    {
        # Approval-queue gated (from CLAUDE.md §7 hard constraint #7)
        "email_sending",
        "file_deletion",
        "external_api_calls",
        "skill_installation",
        # Additional high-risk categories
        "code_execution",
        "database_write",
        "cloud_deploy",
        "webhook_send",
        "data_export",
    }
)


class GroupRole(str, Enum):
    """Per-group roles for Telegram group workspace members.

    Hierarchy (highest to lowest):
      OWNER > MEMBER > READ_ONLY
    """

    OWNER = "owner"
    MEMBER = "member"
    READ_ONLY = "read-only"

    @property
    def rank(self) -> int:
        """Numeric rank for comparison — higher is more privileged."""
        return {"owner": 2, "member": 1, "read-only": 0}[self.value]

    def can_use_high_risk(self) -> bool:
        """Return True if this role is permitted to REQUEST high-risk tools.

        OWNER: unrestricted.
        MEMBER: can request (routed to approval queue).
        READ_ONLY: denied outright — no queue entry created.
        """
        return self in (GroupRole.OWNER, GroupRole.MEMBER)


class GroupRoleResolver:
    """Resolve per-group roles for Telegram group workspace members.

    Args:
        group_role_map: Dict mapping
            {group_chat_id: {user_id: role_string}}
            where role_string is one of "owner", "member", "read-only".
    """

    def __init__(self, group_role_map: Optional[Dict[str, Dict[str, str]]] = None):
        # group_chat_id (str) → {user_id (str) → role_string (str)}
        self._map: Dict[str, Dict[str, str]] = group_role_map or {}

    # ------------------------------------------------------------------
    # Role resolution
    # ------------------------------------------------------------------

    def get_role(self, group_chat_id: str, user_id: str) -> GroupRole:
        """Return the GroupRole for user_id in group_chat_id.

        Returns GroupRole.READ_ONLY if the group or user is unknown (deny-safe).
        """
        group_roles = self._map.get(str(group_chat_id), {})
        role_str = group_roles.get(str(user_id), GroupRole.READ_ONLY.value)
        try:
            return GroupRole(role_str)
        except ValueError:
            logger.warning(
                "Unknown group role '%s' for user=%s group=%s — defaulting to read-only",
                role_str,
                user_id,
                group_chat_id,
            )
            return GroupRole.READ_ONLY

    def is_owner(self, group_chat_id: str, user_id: str) -> bool:
        """Return True if user_id is the owner in group_chat_id."""
        return self.get_role(group_chat_id, user_id) == GroupRole.OWNER

    def is_member_or_higher(self, group_chat_id: str, user_id: str) -> bool:
        """Return True if user_id is at least a member (member or owner)."""
        return self.get_role(group_chat_id, user_id).rank >= GroupRole.MEMBER.rank

    # ------------------------------------------------------------------
    # Tool risk classification
    # ------------------------------------------------------------------

    @staticmethod
    def is_high_risk_tool(tool_name: str) -> bool:
        """Return True if the tool is classified as high-risk.

        High-risk tools require owner/member role to request (read-only denied).
        """
        return tool_name.lower().strip() in _HIGH_RISK_TOOLS

    # ------------------------------------------------------------------
    # Runtime map management
    # ------------------------------------------------------------------

    def set_role(self, group_chat_id: str, user_id: str, role: GroupRole) -> None:
        """Set or update the role for a user in a specific group."""
        gid = str(group_chat_id)
        uid = str(user_id)
        if gid not in self._map:
            self._map[gid] = {}
        self._map[gid][uid] = role.value
        logger.info(
            "GroupRoleResolver: set role %s for user=%s group=%s", role.value, uid, gid
        )

    def remove_role(self, group_chat_id: str, user_id: str) -> None:
        """Remove a user's role entry from a group (falls back to READ_ONLY)."""
        gid = str(group_chat_id)
        uid = str(user_id)
        if gid in self._map and uid in self._map[gid]:
            del self._map[gid][uid]
            logger.info("GroupRoleResolver: removed role for user=%s group=%s", uid, gid)

    def get_all_roles(self, group_chat_id: str) -> Dict[str, GroupRole]:
        """Return all user→role mappings for a group."""
        group_roles = self._map.get(str(group_chat_id), {})
        result: Dict[str, GroupRole] = {}
        for uid, role_str in group_roles.items():
            try:
                result[uid] = GroupRole(role_str)
            except ValueError:
                result[uid] = GroupRole.READ_ONLY
        return result
