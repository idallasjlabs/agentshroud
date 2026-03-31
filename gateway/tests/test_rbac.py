# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
RBAC Tests - Role-Based Access Control Tests
Tests for the AgentShroud RBAC implementation.
"""

from __future__ import annotations
import pytest
from unittest.mock import Mock, patch
from dataclasses import dataclass
from typing import Dict, Any

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from gateway.security.rbac import RBACManager, Action, Resource, ToolTier, PermissionResult
from gateway.security.rbac_config import RBACConfig, Role


class TestRBACConfig:
    """Test RBAC configuration."""
    
    def test_default_config_initialization(self):
        """Test default RBAC configuration initialization."""
        config = RBACConfig()
        
        # Check owner role assignment
        assert config.get_user_role("8096968754") == Role.OWNER
        assert config.is_owner("8096968754")
        
        # Check collaborator role assignments
        collaborators = ["8506022825", "8545356403", "15712621992", "8279589982", "8526379012"]
        for user_id in collaborators:
            assert config.get_user_role(user_id) == Role.COLLABORATOR
            assert config.is_collaborator_or_higher(user_id)
        
        # Check default role for unknown users
        assert config.get_user_role("unknown_user") == Role.VIEWER
    
    def test_role_hierarchy_checks(self):
        """Test role hierarchy helper methods."""
        config = RBACConfig()
        
        owner_id = "8096968754"
        collaborator_id = "8506022825"
        unknown_id = "unknown_user"
        
        # Owner checks
        assert config.is_owner(owner_id)
        assert config.is_admin_or_higher(owner_id)
        assert config.is_collaborator_or_higher(owner_id)
        
        # Collaborator checks
        assert not config.is_owner(collaborator_id)
        assert not config.is_admin_or_higher(collaborator_id)
        assert config.is_collaborator_or_higher(collaborator_id)
        
        # Viewer (unknown) checks
        assert not config.is_owner(unknown_id)
        assert not config.is_admin_or_higher(unknown_id)
        assert not config.is_collaborator_or_higher(unknown_id)
    
    def test_role_assignment(self):
        """Test dynamic role assignment."""
        config = RBACConfig()
        
        # Set a new user as admin
        config.set_user_role("new_admin", Role.ADMIN)
        assert config.get_user_role("new_admin") == Role.ADMIN
        assert config.is_admin_or_higher("new_admin")
        
        # Change an existing user's role
        collaborator_id = "8506022825"
        config.set_user_role(collaborator_id, Role.ADMIN)
        assert config.get_user_role(collaborator_id) == Role.ADMIN
    
    def test_get_users_by_role(self):
        """Test getting users by role."""
        config = RBACConfig()
        
        owners = config.get_users_by_role(Role.OWNER)
        assert "8096968754" in owners
        # Owner list may include additional platform IDs (e.g. Slack user ID)
        # alongside the primary Telegram owner ID — allow ≥ 1.
        assert len(owners) >= 1
        
        collaborators = config.get_users_by_role(Role.COLLABORATOR)
        expected_collaborators = ["8506022825", "8545356403", "15712621992", "8279589982", "8526379012"]
        for user_id in expected_collaborators:
            assert user_id in collaborators

    def test_owner_and_collaborators_can_be_overridden_from_env(self):
        """Env overrides should drive runtime owner/collaborator identity."""
        with patch.dict(
            os.environ,
            {
                "AGENTSHROUD_OWNER_USER_ID": "7614658040",
                "AGENTSHROUD_COLLABORATOR_USER_IDS": "8506022825, 8545356403,7614658040",
            },
            clear=False,
        ):
            config = RBACConfig()

        assert config.owner_user_id == "7614658040"
        assert config.get_user_role("7614658040") == Role.OWNER
        # Owner should be excluded from collaborator list even if included in env.
        assert "7614658040" not in config.collaborator_user_ids
        assert config.get_user_role("8506022825") == Role.COLLABORATOR


class TestRBACManager:
    """Test RBAC manager functionality."""
    
    def setup_method(self):
        """Set up test environment."""
        self.config = RBACConfig()
        self.rbac_manager = RBACManager(self.config)
        
        # Test user IDs
        self.owner_id = "8096968754"
        self.collaborator_id = "8506022825"
        self.viewer_id = "unknown_user"
        
        # Create an admin user for testing
        self.admin_id = "test_admin"
        self.config.set_user_role(self.admin_id, Role.ADMIN)
    
    def test_permission_matrix_viewer(self):
        """Test viewer role permissions."""
        viewer_id = self.viewer_id
        
        # Viewer should only have read access to files and sessions
        assert self.rbac_manager.check_permission(viewer_id, Action.READ, Resource.FILES).allowed
        assert self.rbac_manager.check_permission(viewer_id, Action.READ, Resource.SESSIONS).allowed
        
        # Viewer should not have write access
        assert not self.rbac_manager.check_permission(viewer_id, Action.WRITE, Resource.FILES).allowed
        assert not self.rbac_manager.check_permission(viewer_id, Action.TOOL_USE, Resource.TOOLS).allowed
        
        # Viewer should not have admin actions
        assert not self.rbac_manager.check_permission(viewer_id, Action.MANAGE, Resource.USERS).allowed
        assert not self.rbac_manager.check_permission(viewer_id, Action.SET_ROLE, Resource.USERS).allowed
    
    def test_permission_matrix_collaborator(self):
        """Test collaborator role permissions."""
        collaborator_id = self.collaborator_id
        
        # Collaborator should have read/write for files and tool usage
        assert self.rbac_manager.check_permission(collaborator_id, Action.READ, Resource.FILES).allowed
        assert self.rbac_manager.check_permission(collaborator_id, Action.WRITE, Resource.FILES).allowed
        assert self.rbac_manager.check_permission(collaborator_id, Action.TOOL_USE, Resource.TOOLS).allowed
        
        # Collaborator should not have admin actions
        assert not self.rbac_manager.check_permission(collaborator_id, Action.MANAGE, Resource.USERS).allowed
        assert not self.rbac_manager.check_permission(collaborator_id, Action.SET_ROLE, Resource.USERS).allowed
        assert not self.rbac_manager.check_permission(collaborator_id, Action.CONFIGURE, Resource.SYSTEM).allowed
    
    def test_permission_matrix_admin(self):
        """Test admin role permissions."""
        admin_id = self.admin_id
        
        # Admin should have most permissions
        assert self.rbac_manager.check_permission(admin_id, Action.READ, Resource.FILES).allowed
        assert self.rbac_manager.check_permission(admin_id, Action.WRITE, Resource.FILES).allowed
        assert self.rbac_manager.check_permission(admin_id, Action.MANAGE, Resource.USERS).allowed
        assert self.rbac_manager.check_permission(admin_id, Action.CONFIGURE, Resource.SYSTEM).allowed
        assert self.rbac_manager.check_permission(admin_id, Action.APPROVE, Resource.APPROVALS).allowed
        
        # Admin should not be able to set roles (owner-only)
        assert not self.rbac_manager.check_permission(admin_id, Action.SET_ROLE, Resource.USERS).allowed
    
    def test_permission_matrix_owner(self):
        """Test owner role permissions."""
        owner_id = self.owner_id
        
        # Owner should have all permissions
        assert self.rbac_manager.check_permission(owner_id, Action.READ, Resource.FILES).allowed
        assert self.rbac_manager.check_permission(owner_id, Action.WRITE, Resource.FILES).allowed
        assert self.rbac_manager.check_permission(owner_id, Action.MANAGE, Resource.USERS).allowed
        assert self.rbac_manager.check_permission(owner_id, Action.CONFIGURE, Resource.SYSTEM).allowed
        assert self.rbac_manager.check_permission(owner_id, Action.SET_ROLE, Resource.USERS).allowed
        assert self.rbac_manager.check_permission(owner_id, Action.DELETE, Resource.SESSIONS).allowed
    
    def test_tool_tier_permissions(self):
        """Test tool tier access permissions."""
        # Viewer - no tool access
        assert not self.rbac_manager.check_tool_permission(self.viewer_id, ToolTier.LOW).allowed
        assert not self.rbac_manager.check_tool_permission(self.viewer_id, ToolTier.MEDIUM).allowed
        
        # Collaborator - low and medium tools
        assert self.rbac_manager.check_tool_permission(self.collaborator_id, ToolTier.LOW).allowed
        assert self.rbac_manager.check_tool_permission(self.collaborator_id, ToolTier.MEDIUM).allowed
        assert not self.rbac_manager.check_tool_permission(self.collaborator_id, ToolTier.HIGH).allowed
        assert not self.rbac_manager.check_tool_permission(self.collaborator_id, ToolTier.CRITICAL).allowed
        
        # Admin - low, medium, high tools (critical requires approval)
        assert self.rbac_manager.check_tool_permission(self.admin_id, ToolTier.LOW).allowed
        assert self.rbac_manager.check_tool_permission(self.admin_id, ToolTier.MEDIUM).allowed
        assert self.rbac_manager.check_tool_permission(self.admin_id, ToolTier.HIGH).allowed
        
        # Admin should require approval for critical tools
        critical_result = self.rbac_manager.check_tool_permission(self.admin_id, ToolTier.CRITICAL)
        assert not critical_result.allowed
        assert critical_result.requires_approval
        
        # Owner - all tools
        assert self.rbac_manager.check_tool_permission(self.owner_id, ToolTier.LOW).allowed
        assert self.rbac_manager.check_tool_permission(self.owner_id, ToolTier.MEDIUM).allowed
        assert self.rbac_manager.check_tool_permission(self.owner_id, ToolTier.HIGH).allowed
        assert self.rbac_manager.check_tool_permission(self.owner_id, ToolTier.CRITICAL).allowed
    
    def test_set_user_role(self):
        """Test setting user roles."""
        # Only owner should be able to set roles
        target_user = "test_target_user"
        
        # Owner setting role should work
        result = self.rbac_manager.set_user_role(self.owner_id, target_user, Role.ADMIN)
        assert result.allowed
        assert self.rbac_manager.get_user_role(target_user) == Role.ADMIN
        
        # Admin trying to set role should fail
        result = self.rbac_manager.set_user_role(self.admin_id, target_user, Role.COLLABORATOR)
        assert not result.allowed
        assert not result.allowed  # Admin cannot set roles
        
        # Cannot change owner role
        result = self.rbac_manager.set_user_role(self.owner_id, self.owner_id, Role.ADMIN)
        assert not result.allowed
        assert "Cannot change owner role" in result.reason
    
    def test_user_permissions_summary(self):
        """Test getting user permissions summary."""
        summary = self.rbac_manager.get_user_permissions_summary(self.collaborator_id)
        
        assert summary["user_id"] == self.collaborator_id
        assert summary["role"] == "collaborator"
        assert "read" in summary["permissions"]
        assert "write" in summary["permissions"]
        assert "tool_use" in summary["permissions"]
        assert "low" in summary["allowed_tool_tiers"]
        assert "medium" in summary["allowed_tool_tiers"]
        assert not summary["is_owner"]
        assert not summary["is_admin_or_higher"]
        assert summary["is_collaborator_or_higher"]
    
    def test_user_management_hierarchy(self):
        """Test user management hierarchy."""
        # Owner can manage everyone except other owners
        assert self.rbac_manager.can_user_manage_user(self.owner_id, self.admin_id)
        assert self.rbac_manager.can_user_manage_user(self.owner_id, self.collaborator_id)
        assert self.rbac_manager.can_user_manage_user(self.owner_id, self.viewer_id)
        assert not self.rbac_manager.can_user_manage_user(self.owner_id, self.owner_id)
        
        # Admin can manage collaborators and viewers
        assert self.rbac_manager.can_user_manage_user(self.admin_id, self.collaborator_id)
        assert self.rbac_manager.can_user_manage_user(self.admin_id, self.viewer_id)
        assert not self.rbac_manager.can_user_manage_user(self.admin_id, self.owner_id)
        assert not self.rbac_manager.can_user_manage_user(self.admin_id, self.admin_id)
        
        # Collaborators cannot manage anyone
        assert not self.rbac_manager.can_user_manage_user(self.collaborator_id, self.viewer_id)
        assert not self.rbac_manager.can_user_manage_user(self.collaborator_id, self.admin_id)
    
    def test_list_users_and_roles(self):
        """Test listing users and roles."""
        # Admin should be able to list users
        result = self.rbac_manager.list_users_and_roles(self.admin_id)
        assert result.allowed
        
        # Collaborator should not be able to list users
        result = self.rbac_manager.list_users_and_roles(self.collaborator_id)
        assert not result.allowed
        
        # Viewer should not be able to list users
        result = self.rbac_manager.list_users_and_roles(self.viewer_id)
        assert not result.allowed
    
    def test_role_hierarchy_levels(self):
        """Test role hierarchy levels."""
        hierarchy = self.rbac_manager.get_role_hierarchy()
        
        assert hierarchy["viewer"] < hierarchy["collaborator"]
        assert hierarchy["collaborator"] < hierarchy["admin"]
        assert hierarchy["admin"] < hierarchy["owner"]


class TestRBACIntegration:
    """Test RBAC integration with middleware."""
    
    def setup_method(self):
        """Set up test environment."""
        from gateway.ingest_api.middleware import MiddlewareManager
        self.middleware = MiddlewareManager()
        
        # Test users
        self.owner_id = "8096968754"
        self.collaborator_id = "8506022825"
        self.viewer_id = "unknown_user"
    
    def test_rbac_initialization_in_middleware(self):
        """Test that RBAC is properly initialized in middleware."""
        assert self.middleware.rbac_manager is not None
        assert self.middleware.rbac_config is not None
        
        # Check that RBAC manager can get user roles
        assert self.middleware.rbac_manager.get_user_role(self.owner_id) == Role.OWNER
        assert self.middleware.rbac_manager.get_user_role(self.collaborator_id) == Role.COLLABORATOR
        assert self.middleware.rbac_manager.get_user_role(self.viewer_id) == Role.VIEWER
    
    @pytest.mark.asyncio
    async def test_rbac_blocks_unauthorized_access(self):
        """Test that RBAC blocks unauthorized access attempts."""
        # Viewer trying to use tools
        request_data = {
            "user_id": self.viewer_id,
            "message": "execute some command",
            "session_context": {"user_id": self.viewer_id}
        }
        
        result = await self.middleware.process_request(request_data)
        assert not result.allowed
        assert "access denied" in result.reason.lower() or "denied" in result.reason.lower()
    
    @pytest.mark.asyncio
    async def test_rbac_allows_authorized_access(self):
        """Test that RBAC allows authorized access."""
        # Collaborator reading files
        request_data = {
            "user_id": self.collaborator_id,
            "message": "read some file",
            "session_context": {"user_id": self.collaborator_id}
        }
        
        result = await self.middleware.process_request(request_data)
        # Note: This may fail due to other middleware checks, but RBAC should pass
        # We're mainly testing that RBAC doesn't block legitimate requests
        if not result.allowed and "rbac" in result.reason.lower():
            pytest.fail("RBAC incorrectly blocked authorized request")
    
    @pytest.mark.asyncio
    async def test_rbac_handles_missing_user_id(self):
        """Test RBAC handling when user ID is missing."""
        request_data = {
            "message": "some request without user id"
        }
        
        result = await self.middleware.process_request(request_data)
        assert not result.allowed
        assert "no user identification" in result.reason.lower()


class TestRBACErrorHandling:
    """Test RBAC error handling and edge cases."""
    
    def test_invalid_user_id(self):
        """Test handling of invalid user IDs."""
        rbac_manager = RBACManager()
        
        # None user_id
        result = rbac_manager.check_permission(None, Action.READ, Resource.FILES)
        assert not result.allowed
        
        # Empty user_id
        result = rbac_manager.check_permission("", Action.READ, Resource.FILES)
        assert not result.allowed
    
    def test_invalid_action_resource_combinations(self):
        """Test handling of invalid action/resource combinations."""
        rbac_manager = RBACManager()
        owner_id = "8096968754"
        
        # These should still work due to the permission matrix design
        result = rbac_manager.check_permission(owner_id, Action.READ, Resource.FILES)
        assert result.allowed
    
    def test_rbac_manager_without_config(self):
        """Test RBAC manager initialization without explicit config."""
        rbac_manager = RBACManager()
        
        # Should use default config
        assert rbac_manager.config is not None
        assert rbac_manager.config.owner_user_id == "8096968754"
    
    def test_permission_check_with_context(self):
        """Test permission checks with additional context."""
        rbac_manager = RBACManager()
        admin_id = "test_admin"
        rbac_manager.config.set_user_role(admin_id, Role.ADMIN)
        
        # Admin trying to use critical tools with context
        context = {"tool_tier": ToolTier.CRITICAL}
        result = rbac_manager.check_permission(admin_id, Action.TOOL_USE, Resource.TOOLS, context)
        assert not result.allowed
        assert result.requires_approval


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


# ── GroupRegistry tests ───────────────────────────────────────────────────────

from gateway.security.rbac_config import Group, GroupRegistry, RBACConfig


class TestGroupRegistry:
    """Tests for GroupRegistry auto-groups and custom group management."""

    def _make_rbac(self) -> RBACConfig:
        rbac = RBACConfig.__new__(RBACConfig)
        rbac.owner_user_id = "8096968754"
        rbac.collaborator_user_ids = ["8506022825", "8545356403"]
        rbac.default_role = None
        from gateway.security.rbac_config import Role
        rbac.user_roles = {
            "8096968754": Role.OWNER,
            "8506022825": Role.COLLABORATOR,
            "8545356403": Role.COLLABORATOR,
            "U0AL7640RHD": Role.OWNER,  # Slack owner
        }
        return rbac

    def test_auto_groups_created(self):
        registry = GroupRegistry()
        registry.init_auto_groups(self._make_rbac())
        assert "telegram" in registry.groups
        assert "slack" in registry.groups
        assert "everyone" in registry.groups

    def test_telegram_group_contains_numeric_ids(self):
        registry = GroupRegistry()
        registry.init_auto_groups(self._make_rbac())
        tg = registry.get_group("telegram")
        assert tg is not None
        assert "8096968754" in tg.members
        assert "8506022825" in tg.members
        assert "U0AL7640RHD" not in tg.members

    def test_slack_group_contains_slack_ids(self):
        registry = GroupRegistry()
        registry.init_auto_groups(self._make_rbac())
        slack = registry.get_group("slack")
        assert slack is not None
        assert "U0AL7640RHD" in slack.members
        assert "8096968754" not in slack.members

    def test_everyone_group_contains_all_users(self):
        registry = GroupRegistry()
        registry.init_auto_groups(self._make_rbac())
        everyone = registry.get_group("everyone")
        assert everyone is not None
        for uid in ["8096968754", "8506022825", "U0AL7640RHD"]:
            assert uid in everyone.members

    def test_create_custom_group(self, tmp_path, monkeypatch):
        import gateway.security.rbac_config as rc
        monkeypatch.setattr(rc, "_GROUPS_FILE_PATH", tmp_path / "groups.json")
        registry = GroupRegistry()
        registry.init_auto_groups(self._make_rbac())
        g = registry.create_group("project-alpha", "Project Alpha", members=["8506022825"])
        assert g.id == "project-alpha"
        assert "8506022825" in g.members
        assert "project-alpha" in registry.groups

    def test_delete_custom_group(self, tmp_path, monkeypatch):
        import gateway.security.rbac_config as rc
        monkeypatch.setattr(rc, "_GROUPS_FILE_PATH", tmp_path / "groups.json")
        registry = GroupRegistry()
        registry.init_auto_groups(self._make_rbac())
        registry.create_group("temp-group", "Temp")
        assert registry.delete_group("temp-group") is True
        assert "temp-group" not in registry.groups

    def test_cannot_delete_auto_group(self):
        registry = GroupRegistry()
        registry.init_auto_groups(self._make_rbac())
        with pytest.raises(ValueError, match="auto-group"):
            registry.delete_group("telegram")

    def test_cannot_create_reserved_group_id(self):
        registry = GroupRegistry()
        registry.init_auto_groups(self._make_rbac())
        with pytest.raises(ValueError, match="reserved"):
            registry.create_group("everyone", "My Everyone")

    def test_add_remove_member(self, tmp_path, monkeypatch):
        import gateway.security.rbac_config as rc
        monkeypatch.setattr(rc, "_GROUPS_FILE_PATH", tmp_path / "groups.json")
        registry = GroupRegistry()
        registry.init_auto_groups(self._make_rbac())
        registry.create_group("team-a", "Team A")
        registry.add_member("team-a", "8506022825")
        assert registry.is_member("team-a", "8506022825")
        registry.remove_member("team-a", "8506022825")
        assert not registry.is_member("team-a", "8506022825")

    def test_is_member_unknown_group_returns_false(self):
        registry = GroupRegistry()
        registry.init_auto_groups(self._make_rbac())
        assert registry.is_member("nonexistent", "8506022825") is False
