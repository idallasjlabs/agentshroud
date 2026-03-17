# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
RBAC Manager - Role-Based Access Control Core
Implements role-based access control for AgentShroud operations.
"""

from __future__ import annotations
import logging
from dataclasses import dataclass
from typing import Dict, Set, List, Optional, Any
from enum import Enum

from .rbac_config import RBACConfig, Role, ToolTier

logger = logging.getLogger(__name__)


@dataclass
class PermissionResult:
    """Result of permission check."""
    allowed: bool
    reason: Optional[str] = None
    requires_approval: bool = False
    denied_action: Optional[str] = None


class Action(str, Enum):
    """Actions that can be performed in the system."""
    READ = "read"
    WRITE = "write"
    EXECUTE = "execute"
    MANAGE = "manage"
    CONFIGURE = "configure"
    DELETE = "delete"
    TOOL_USE = "tool_use"
    APPROVE = "approve"
    SET_ROLE = "set_role"
    INVITE = "invite"


class Resource(str, Enum):
    """Resources that can be accessed in the system."""
    FILES = "files"
    TOOLS = "tools"
    SYSTEM = "system"
    USERS = "users"
    SESSIONS = "sessions"
    APPROVALS = "approvals"
    CONFIGURATION = "configuration"
    GROUPS = "groups"


class RBACManager:
    """Role-Based Access Control Manager."""
    
    def __init__(self, config: Optional[RBACConfig] = None):
        """Initialize RBAC manager with configuration."""
        self.config = config or RBACConfig()
        
        # Define permission matrix: Role -> {Action -> {Resource -> allowed}}
        self._permission_matrix = self._build_permission_matrix()
        
        # Define tool tier permissions: Role -> allowed tool tiers
        self._tool_permissions = self._build_tool_permissions()
        
        logger.info(f"RBAC Manager initialized with {len(self.config.user_roles)} configured users")
    
    def _build_permission_matrix(self) -> Dict[Role, Dict[Action, Set[Resource]]]:
        """Build the permission matrix for all roles."""
        matrix = {}
        
        # VIEWER role - read-only access
        matrix[Role.VIEWER] = {
            Action.READ: {Resource.FILES, Resource.SESSIONS},
        }
        
        # COLLABORATOR role - can interact and use limited tools
        matrix[Role.COLLABORATOR] = {
            Action.READ: {Resource.FILES, Resource.SESSIONS, Resource.TOOLS, Resource.SYSTEM, Resource.GROUPS},
            Action.WRITE: {Resource.FILES},
            Action.EXECUTE: {Resource.TOOLS},
            Action.TOOL_USE: {Resource.TOOLS},
        }
        
        # ADMIN role - can manage and configure, use all except critical tools
        matrix[Role.ADMIN] = {
            Action.READ: {Resource.FILES, Resource.SESSIONS, Resource.TOOLS, Resource.USERS, Resource.SYSTEM, Resource.GROUPS},
            Action.WRITE: {Resource.FILES, Resource.SYSTEM},
            Action.EXECUTE: {Resource.TOOLS, Resource.SYSTEM},
            Action.MANAGE: {Resource.USERS, Resource.SESSIONS, Resource.TOOLS, Resource.GROUPS},
            Action.CONFIGURE: {Resource.SYSTEM, Resource.TOOLS},
            Action.DELETE: {Resource.FILES},
            Action.TOOL_USE: {Resource.TOOLS},
            Action.APPROVE: {Resource.APPROVALS},
            Action.INVITE: {Resource.GROUPS},
        }

        # OWNER role - full access to everything
        matrix[Role.OWNER] = {
            Action.READ: {Resource.FILES, Resource.SESSIONS, Resource.TOOLS, Resource.USERS, Resource.SYSTEM, Resource.CONFIGURATION, Resource.APPROVALS, Resource.GROUPS},
            Action.WRITE: {Resource.FILES, Resource.SYSTEM, Resource.CONFIGURATION, Resource.GROUPS},
            Action.EXECUTE: {Resource.TOOLS, Resource.SYSTEM},
            Action.MANAGE: {Resource.USERS, Resource.SESSIONS, Resource.TOOLS, Resource.SYSTEM, Resource.GROUPS},
            Action.CONFIGURE: {Resource.SYSTEM, Resource.TOOLS, Resource.CONFIGURATION},
            Action.DELETE: {Resource.FILES, Resource.USERS, Resource.SESSIONS},
            Action.TOOL_USE: {Resource.TOOLS},
            Action.APPROVE: {Resource.APPROVALS},
            Action.SET_ROLE: {Resource.USERS},
            Action.INVITE: {Resource.GROUPS},
        }
        
        return matrix
    
    def _build_tool_permissions(self) -> Dict[Role, Set[ToolTier]]:
        """Build tool tier permissions for each role."""
        return {
            Role.VIEWER: set(),  # No tool usage
            Role.COLLABORATOR: {ToolTier.LOW, ToolTier.MEDIUM},
            Role.ADMIN: {ToolTier.LOW, ToolTier.MEDIUM, ToolTier.HIGH},  # Critical requires approval
            Role.OWNER: {ToolTier.LOW, ToolTier.MEDIUM, ToolTier.HIGH, ToolTier.CRITICAL},
        }
    
    def check_permission(self, user_id: str, action: Action, resource: Resource, 
                        context: Optional[Dict[str, Any]] = None) -> PermissionResult:
        """Check if a user has permission to perform an action on a resource."""
        if not user_id or not isinstance(user_id, str) or not user_id.strip():
            return PermissionResult(allowed=False, reason="Invalid user ID")
        try:
            role = self.get_user_role(user_id)
            
            # Check if action is allowed for this role on this resource
            role_permissions = self._permission_matrix.get(role, {})
            allowed_resources = role_permissions.get(action, set())
            
            if resource not in allowed_resources:
                return PermissionResult(
                    allowed=False,
                    reason=f"Role {role.value} does not have {action.value} permission for {resource.value}",
                    denied_action=action.value
                )
            
            # Special case: Admin using critical tools requires approval
            if (role == Role.ADMIN and action == Action.TOOL_USE and 
                context and context.get("tool_tier") == ToolTier.CRITICAL):
                return PermissionResult(
                    allowed=False,
                    reason="Critical tools require owner approval for admin users",
                    requires_approval=True,
                    denied_action=action.value
                )
            
            return PermissionResult(allowed=True)
            
        except Exception as e:
            logger.error(f"Error checking permission for user {user_id}: {e}")
            return PermissionResult(
                allowed=False,
                reason=f"Permission check error: {str(e)}"
            )
    
    def check_tool_permission(self, user_id: str, tool_tier: ToolTier) -> PermissionResult:
        """Check if a user can use tools of a specific tier."""
        try:
            role = self.get_user_role(user_id)
            allowed_tiers = self._tool_permissions.get(role, set())
            
            if tool_tier not in allowed_tiers:
                # Special case: Admin can request approval for critical tools
                if role == Role.ADMIN and tool_tier == ToolTier.CRITICAL:
                    return PermissionResult(
                        allowed=False,
                        reason=f"Critical tools require approval for admin users",
                        requires_approval=True,
                        denied_action="tool_use"
                    )
                
                return PermissionResult(
                    allowed=False,
                    reason=f"Role {role.value} cannot use {tool_tier.value} tier tools",
                    denied_action="tool_use"
                )
            
            return PermissionResult(allowed=True)
            
        except Exception as e:
            logger.error(f"Error checking tool permission for user {user_id}: {e}")
            return PermissionResult(
                allowed=False,
                reason=f"Tool permission check error: {str(e)}"
            )
    
    def get_user_role(self, user_id: str) -> Role:
        """Get the role for a user."""
        return self.config.get_user_role(user_id)
    
    def set_user_role(self, admin_user_id: str, target_user_id: str, role: Role) -> PermissionResult:
        """Set a user's role (owner-only operation)."""
        # Check if admin has permission to set roles
        permission = self.check_permission(admin_user_id, Action.SET_ROLE, Resource.USERS)
        if not permission.allowed:
            return permission
        
        try:
            # Additional check: only owner can set roles
            if not self.config.is_owner(admin_user_id):
                return PermissionResult(
                    allowed=False,
                    reason="Only the owner can modify user roles"
                )
            
            # Don't allow changing owner role
            if self.config.is_owner(target_user_id):
                return PermissionResult(
                    allowed=False,
                    reason="Cannot change owner role"
                )
            
            old_role = self.config.get_user_role(target_user_id)
            self.config.set_user_role(target_user_id, role)
            
            logger.info(f"User {admin_user_id} changed role for user {target_user_id}: {old_role.value} -> {role.value}")
            
            return PermissionResult(allowed=True)
            
        except Exception as e:
            logger.error(f"Error setting user role: {e}")
            return PermissionResult(
                allowed=False,
                reason=f"Role setting error: {str(e)}"
            )
    
    def get_user_permissions_summary(self, user_id: str) -> Dict[str, Any]:
        """Get a summary of permissions for a user."""
        role = self.get_user_role(user_id)
        role_permissions = self._permission_matrix.get(role, {})
        tool_permissions = self._tool_permissions.get(role, set())
        
        # Convert to serializable format
        permissions = {}
        for action, resources in role_permissions.items():
            permissions[action.value] = [resource.value for resource in resources]
        
        return {
            "user_id": user_id,
            "role": role.value,
            "permissions": permissions,
            "allowed_tool_tiers": [tier.value for tier in tool_permissions],
            "is_owner": self.config.is_owner(user_id),
            "is_admin_or_higher": self.config.is_admin_or_higher(user_id),
            "is_collaborator_or_higher": self.config.is_collaborator_or_higher(user_id)
        }
    
    def list_users_and_roles(self, requesting_user_id: str) -> PermissionResult:
        """List all users and their roles (admin+ only)."""
        # Check if user can read user information
        permission = self.check_permission(requesting_user_id, Action.READ, Resource.USERS)
        if not permission.allowed:
            return permission
        
        try:
            users_info = []
            for user_id, role in self.config.user_roles.items():
                users_info.append({
                    "user_id": user_id,
                    "role": role.value,
                    "is_owner": self.config.is_owner(user_id)
                })
            
            return PermissionResult(
                allowed=True, 
                reason="success", 
            )
            
        except Exception as e:
            logger.error(f"Error listing users and roles: {e}")
            return PermissionResult(
                allowed=False,
                reason=f"Error listing users: {str(e)}"
            )
    
    def get_role_hierarchy(self) -> Dict[str, int]:
        """Get role hierarchy levels (higher number = more privileges)."""
        return {
            Role.VIEWER.value: 1,
            Role.COLLABORATOR.value: 2,
            Role.ADMIN.value: 3,
            Role.OWNER.value: 4
        }
    
    def can_user_manage_user(self, manager_user_id: str, target_user_id: str) -> bool:
        """Check if one user can manage another user."""
        manager_role = self.get_user_role(manager_user_id)
        target_role = self.get_user_role(target_user_id)
        
        hierarchy = self.get_role_hierarchy()
        
        # Owner can manage everyone except other owners
        if manager_role == Role.OWNER and target_role != Role.OWNER:
            return True
        
        # Admin can manage collaborators and viewers
        if manager_role == Role.ADMIN and target_role in [Role.COLLABORATOR, Role.VIEWER]:
            return True

        return False

    def check_group_permission(
        self, user_id: str, group_id: str, action: Action
    ) -> PermissionResult:
        """Check if a user can perform an action on a group.

        Permission matrix:
          OWNER    — full MANAGE + INVITE on all groups
          ADMIN    — MANAGE + INVITE on all groups
          group admin — MANAGE + INVITE on their own group
          group member — READ on their own group
          other   — denied
        """
        try:
            role = self.get_user_role(user_id)
            # Owner and admin can do anything to any group
            if role in (Role.OWNER, Role.ADMIN):
                return PermissionResult(allowed=True)

            # For collaborators, check group membership / admin status via TeamsConfig
            teams = getattr(self.config, "teams_config", None)
            if teams is None:
                return PermissionResult(
                    allowed=False,
                    reason="No teams config available",
                )

            is_member = user_id in teams.get_user_groups_by_id(group_id)
            is_admin = teams.is_group_admin(user_id, group_id)

            if action == Action.READ and is_member:
                return PermissionResult(allowed=True)
            if action in (Action.MANAGE, Action.INVITE) and is_admin:
                return PermissionResult(allowed=True)

            return PermissionResult(
                allowed=False,
                reason=f"User {user_id} lacks {action.value} permission on group {group_id}",
                denied_action=action.value,
            )
        except Exception as exc:
            logger.error("Error checking group permission for %s on %s: %s", user_id, group_id, exc)
            return PermissionResult(allowed=False, reason=str(exc))
