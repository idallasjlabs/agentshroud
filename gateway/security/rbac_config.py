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
from typing import TYPE_CHECKING, Dict, Set, List, Optional
from enum import Enum
import os

if TYPE_CHECKING:
    from .group_config import TeamsConfig


class Role(str, Enum):
    """User roles in AgentShroud RBAC system.

    Hierarchy (highest to lowest):
      OWNER > ADMIN > OPERATOR > COLLABORATOR > VIEWER

    OPERATOR: Trusted collaborator with group management and egress-approval
    capability when explicitly delegated by the owner. Sits between admin and
    collaborator — can be granted time-bounded owner-delegated privileges.
    """
    OWNER = "owner"
    ADMIN = "admin"
    OPERATOR = "operator"      # v0.9.0: granular role between admin and collaborator
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

    # Group admin mapping — {group_id: admin_user_id}. Populated from TeamsConfig.
    group_admin_ids: Dict[str, str] = field(default_factory=dict)

    # TeamsConfig reference (set by lifespan after config load, not in __post_init__)
    teams_config: Optional["TeamsConfig"] = field(default=None, repr=False)
    
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
    
    def wire_teams_config(self, teams: "TeamsConfig") -> None:
        """Merge group membership and admin IDs from TeamsConfig into RBAC.

        Called from lifespan.py after both configs are loaded.
        Idempotent — safe to call multiple times.
        """
        self.teams_config = teams
        # Build group_admin_ids map
        for group_id, group in teams.groups.items():
            if group.admin:
                self.group_admin_ids[group_id] = group.admin
        # Auto-merge all group member IDs as collaborators
        for uid in teams.get_all_member_ids():
            if uid not in self.collaborator_user_ids and str(uid) != str(self.owner_user_id):
                self.collaborator_user_ids.append(uid)
            if uid not in self.user_roles and str(uid) != str(self.owner_user_id):
                self.user_roles[uid] = Role.COLLABORATOR

    def get_user_groups_by_id(self, group_id: str) -> List[str]:
        """Return member IDs of a group, or empty list if no teams config."""
        if self.teams_config is None:
            return []
        group = self.teams_config.groups.get(group_id)
        return list(group.members) if group else []

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

    def is_operator_or_higher(self, user_id: str) -> bool:
        """Check if user has operator privileges or higher (admin, operator, owner)."""
        role = self.get_user_role(user_id)
        return role in [Role.OWNER, Role.ADMIN, Role.OPERATOR]

    def is_collaborator_or_higher(self, user_id: str) -> bool:
        """Check if user has collaborator privileges or higher."""
        role = self.get_user_role(user_id)
        return role in [Role.OWNER, Role.ADMIN, Role.OPERATOR, Role.COLLABORATOR]


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
    lock_path = _APPROVED_COLLABORATORS_FILE.with_suffix(".lock")
    try:
        _APPROVED_COLLABORATORS_FILE.parent.mkdir(parents=True, exist_ok=True)
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
