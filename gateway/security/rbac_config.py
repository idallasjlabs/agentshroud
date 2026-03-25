# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
RBAC Configuration - Role-Based Access Control Configuration
Defines user roles and access control policies for AgentShroud.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from enum import Enum
import os


class Role(str, Enum):
    """User roles in AgentShroud RBAC system."""
    OWNER = "owner"
    ADMIN = "admin"
    COLLABORATOR = "collaborator"
    VIEWER = "viewer"


class ToolTier(str, Enum):
    """Tool security tiers for RBAC permissions."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


@dataclass
class RBACConfig:
    """Configuration for Role-Based Access Control."""
    # User to role mapping
    user_roles: Dict[str, Role] = field(default_factory=dict)
    
    # Default role for unknown users
    default_role: Role = Role.VIEWER
    
    # Owner user ID (has full access)
    owner_user_id: str = "8096968754"
    
    # Pre-configured collaborators
    collaborator_user_ids: List[str] = field(default_factory=lambda: [
        "8506022825",
        "8545356403",
        "15712621992",
        "8279589982",
        "8526379012",
        "7614658040",
        "8633775668"
    ])
    
    def __post_init__(self):
        """Initialize user roles based on configuration."""
        owner_override = str(os.environ.get("AGENTSHROUD_OWNER_USER_ID", "")).strip()
        if owner_override:
            self.owner_user_id = owner_override

        # Slack owner: same person on a different platform. Slack IDs are alphanumeric
        # (e.g. U0ABC123DEF) — naturally disjoint from Telegram numeric IDs, no collision risk.
        slack_owner = str(os.environ.get("AGENTSHROUD_SLACK_OWNER_USER_ID", "")).strip()
        if slack_owner:
            self.user_roles[slack_owner] = Role.OWNER

        collaborators_override = str(
            os.environ.get("AGENTSHROUD_COLLABORATOR_USER_IDS", "")
        ).strip()
        if collaborators_override:
            parsed = [
                token.strip()
                for token in collaborators_override.split(",")
                if token.strip()
            ]
            self.collaborator_user_ids = parsed

        # Ensure owner never appears as collaborator.
        self.collaborator_user_ids = [
            uid for uid in self.collaborator_user_ids if str(uid) != str(self.owner_user_id)
        ]

        # Merge dynamically approved collaborators from persistent store (inline Approve button).
        for _uid in load_persisted_collaborators():
            if _uid not in self.collaborator_user_ids and str(_uid) != str(self.owner_user_id):
                self.collaborator_user_ids.append(_uid)

        # Set owner role
        if self.owner_user_id:
            self.user_roles[self.owner_user_id] = Role.OWNER
        
        # Set collaborator roles
        for user_id in self.collaborator_user_ids:
            if user_id not in self.user_roles:  # Don't override owner
                self.user_roles[user_id] = Role.COLLABORATOR
    
    def get_user_role(self, user_id: str) -> Role:
        """Get role for a user ID."""
        return self.user_roles.get(user_id, self.default_role)
    
    def set_user_role(self, user_id: str, role: Role) -> None:
        """Set role for a user ID (owner-only operation)."""
        self.user_roles[user_id] = role
    
    def get_users_by_role(self, role: Role) -> List[str]:
        """Get all users with a specific role."""
        return [user_id for user_id, user_role in self.user_roles.items() if user_role == role]
    
    def is_owner(self, user_id: str) -> bool:
        """Check if user is the owner (any platform)."""
        return user_id == self.owner_user_id or self.user_roles.get(user_id) == Role.OWNER
    
    def is_admin_or_higher(self, user_id: str) -> bool:
        """Check if user has admin privileges or higher."""
        role = self.get_user_role(user_id)
        return role in [Role.OWNER, Role.ADMIN]
    
    def is_collaborator_or_higher(self, user_id: str) -> bool:
        """Check if user has collaborator privileges or higher."""
        role = self.get_user_role(user_id)
        return role in [Role.OWNER, Role.ADMIN, Role.COLLABORATOR]


# ---------------------------------------------------------------------------
# Group management — named collections of users with optional platform scope.
# Auto-groups (telegram, slack, everyone) are derived from RBACConfig at runtime
# and never persisted. Custom groups are persisted to groups.json.
# ---------------------------------------------------------------------------

@dataclass
class Group:
    """A named group of users."""
    id: str
    name: str
    members: List[str] = field(default_factory=list)
    platform: Optional[str] = None          # 'telegram', 'slack', or None for cross-platform
    telegram_chat_id: Optional[int] = None  # Linked Telegram group/supergroup chat ID
    slack_channel_id: Optional[str] = None  # Provisioned Slack channel ID (C...)


_AUTO_GROUP_IDS = frozenset({"telegram", "slack", "everyone"})


@dataclass
class GroupRegistry:
    """Manages user groups including auto-groups and custom groups."""
    groups: Dict[str, Group] = field(default_factory=dict)

    def init_auto_groups(self, rbac: "RBACConfig") -> None:
        """Derive and reset auto-groups from current RBAC user list, then load custom groups."""
        all_users = list(rbac.user_roles.keys())
        # Telegram: numeric user IDs (may be prefixed with - for supergroups, but user IDs are positive)
        telegram_users = [uid for uid in all_users if uid.lstrip("-").isdigit()]
        # Slack: alphanumeric IDs starting with U (e.g. U0AL7640RHD)
        slack_users = [uid for uid in all_users if uid.startswith("U") and len(uid) >= 8 and uid[1:].isalnum()]

        self.groups["telegram"] = Group(
            id="telegram", name="Telegram Users",
            members=telegram_users, platform="telegram",
        )
        self.groups["slack"] = Group(
            id="slack", name="Slack Users",
            members=slack_users, platform="slack",
        )
        self.groups["everyone"] = Group(
            id="everyone", name="Everyone",
            members=all_users, platform=None,
        )
        # Layer custom groups on top without overwriting auto-groups
        for group in _load_persisted_groups():
            if group.id not in _AUTO_GROUP_IDS:
                self.groups[group.id] = group

    def get_group(self, group_id: str) -> Optional[Group]:
        """Return group by ID, or None."""
        return self.groups.get(group_id)

    def list_groups(self) -> List[Group]:
        """Return all groups."""
        return list(self.groups.values())

    def create_group(self, group_id: str, name: str,
                     members: Optional[List[str]] = None,
                     platform: Optional[str] = None) -> Group:
        """Create or replace a custom group and persist it."""
        if group_id in _AUTO_GROUP_IDS:
            raise ValueError(f"Cannot create group with reserved id: {group_id!r}")
        group = Group(id=group_id, name=name, members=list(members or []), platform=platform)
        self.groups[group_id] = group
        _persist_groups(self.groups)
        return group

    def delete_group(self, group_id: str) -> bool:
        """Delete a custom group. Returns True if deleted, False if not found."""
        if group_id in _AUTO_GROUP_IDS:
            raise ValueError(f"Cannot delete auto-group: {group_id!r}")
        if group_id in self.groups:
            del self.groups[group_id]
            _persist_groups(self.groups)
            return True
        return False

    def add_member(self, group_id: str, user_id: str) -> None:
        """Add a user to a group (auto-groups are updated in-memory only)."""
        if group_id not in self.groups:
            raise KeyError(f"Group not found: {group_id!r}")
        if user_id not in self.groups[group_id].members:
            self.groups[group_id].members.append(user_id)
        if group_id not in _AUTO_GROUP_IDS:
            _persist_groups(self.groups)

    def remove_member(self, group_id: str, user_id: str) -> None:
        """Remove a user from a group (auto-groups are updated in-memory only)."""
        if group_id not in self.groups:
            raise KeyError(f"Group not found: {group_id!r}")
        self.groups[group_id].members = [
            m for m in self.groups[group_id].members if m != user_id
        ]
        if group_id not in _AUTO_GROUP_IDS:
            _persist_groups(self.groups)

    def is_member(self, group_id: str, user_id: str) -> bool:
        """Return True if user_id is in the group."""
        group = self.groups.get(group_id)
        return group is not None and user_id in group.members


# ---------------------------------------------------------------------------
# Group persistence — only custom (non-auto) groups are written to disk.
# ---------------------------------------------------------------------------

_GROUPS_FILE_PATH = Path(
    os.environ.get("AGENTSHROUD_DATA_DIR", "/app/data")
) / "groups.json"
_groups_persist_logger = logging.getLogger("agentshroud.security.rbac_config")


def _load_persisted_groups() -> List[Group]:
    """Read custom groups from disk."""
    try:
        if _GROUPS_FILE_PATH.exists():
            data = json.loads(_GROUPS_FILE_PATH.read_text(encoding="utf-8"))
            return [
                Group(
                    id=g["id"],
                    name=g.get("name", g["id"]),
                    members=g.get("members", []),
                    platform=g.get("platform"),
                    telegram_chat_id=g.get("telegram_chat_id"),
                    slack_channel_id=g.get("slack_channel_id"),
                )
                for g in data.get("groups", [])
                if g.get("id") and g["id"] not in _AUTO_GROUP_IDS
            ]
    except Exception as exc:
        _groups_persist_logger.warning("Could not read groups.json: %s", exc)
    return []


def _persist_groups(groups: Dict[str, Group]) -> None:
    """Write only custom groups to disk (auto-groups are derived at runtime)."""
    custom = [g for g in groups.values() if g.id not in _AUTO_GROUP_IDS]
    try:
        _GROUPS_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "groups": [
                {
                    "id": g.id,
                    "name": g.name,
                    "members": g.members,
                    "platform": g.platform,
                    "telegram_chat_id": g.telegram_chat_id,
                    "slack_channel_id": g.slack_channel_id,
                }
                for g in custom
            ]
        }
        _GROUPS_FILE_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")
    except Exception as exc:
        _groups_persist_logger.warning("Could not persist groups: %s", exc)


# ---------------------------------------------------------------------------
# Collaborator persistence — approvals made via inline buttons persist across
# gateway restarts. Written to /app/data/approved_collaborators.json on the
# shared data volume.
# ---------------------------------------------------------------------------
import fcntl
import json
import logging
from pathlib import Path

_collab_persist_logger = logging.getLogger("agentshroud.security.rbac_config")
_APPROVED_COLLABORATORS_FILE = Path(
    os.environ.get("AGENTSHROUD_DATA_DIR", "/app/data")
) / "approved_collaborators.json"


def load_persisted_collaborators() -> list[str]:
    """Read dynamically approved collaborator IDs from disk."""
    try:
        if _APPROVED_COLLABORATORS_FILE.exists():
            data = json.loads(_APPROVED_COLLABORATORS_FILE.read_text(encoding="utf-8"))
            return [str(uid) for uid in data.get("collaborators", [])]
    except Exception as exc:
        _collab_persist_logger.warning("Could not read approved_collaborators.json: %s", exc)
    return []


def persist_approved_collaborator(uid: str) -> None:
    """Append a collaborator UID to the persistent store (idempotent, file-locked)."""
    try:
        _APPROVED_COLLABORATORS_FILE.parent.mkdir(parents=True, exist_ok=True)
    except OSError as _mkdir_exc:
        _collab_persist_logger.warning("Could not create collaborator persist dir: %s", _mkdir_exc)
        return
    lock_path = _APPROVED_COLLABORATORS_FILE.with_suffix(".lock")
    try:
        with open(lock_path, "w") as lock_fh:
            fcntl.flock(lock_fh, fcntl.LOCK_EX)
            try:
                existing = load_persisted_collaborators()
                if uid in existing:
                    return
                existing.append(uid)
                _APPROVED_COLLABORATORS_FILE.write_text(
                    json.dumps({"collaborators": existing}, indent=2), encoding="utf-8"
                )
                _collab_persist_logger.info("Persisted approved collaborator: %s", uid)
            finally:
                fcntl.flock(lock_fh, fcntl.LOCK_UN)
    except Exception as exc:
        _collab_persist_logger.warning("Could not persist approved collaborator %s: %s", uid, exc)
