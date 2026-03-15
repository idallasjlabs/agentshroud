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
from typing import Dict, Set, List, Optional
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
        "7614658040"
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
