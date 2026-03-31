# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for gateway/security/tool_acl.py — V9-T2: Tool-level access control."""
from __future__ import annotations

import pytest

from gateway.security.tool_acl import (
    ADMIN_TOOLS,
    COLLABORATOR_ALLOWED_TOOLS,
    PRIVATE_TOOLS,
    ToolACLConfig,
    ToolACLEnforcer,
)
from gateway.security.rbac_config import RBACConfig, Role
from gateway.security.group_config import TeamsConfig


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

OWNER_ID = "owner-001"
ADMIN_ID = "admin-002"
COLLAB_ID = "collab-003"
VIEWER_ID = "viewer-004"


def _make_rbac(teams: TeamsConfig = None) -> RBACConfig:
    cfg = RBACConfig(
        owner_user_id=OWNER_ID,
        collaborator_user_ids=[COLLAB_ID],
    )
    cfg.user_roles[ADMIN_ID] = Role.ADMIN
    cfg.user_roles[VIEWER_ID] = Role.VIEWER
    if teams:
        cfg.wire_teams_config(teams)
    return cfg


@pytest.fixture
def rbac():
    return _make_rbac()


@pytest.fixture
def enforcer(rbac):
    return ToolACLEnforcer(acl_config=ToolACLConfig(), rbac_config=rbac)


# ---------------------------------------------------------------------------
# Owner: unrestricted
# ---------------------------------------------------------------------------

class TestOwnerAccess:
    def test_owner_can_use_private_tool(self, enforcer):
        allowed, reason = enforcer.can_use_tool(OWNER_ID, "gmail")
        assert allowed
        assert "owner" in reason

    def test_owner_can_use_admin_tool(self, enforcer):
        allowed, _ = enforcer.can_use_tool(OWNER_ID, "rbac_manage")
        assert allowed

    def test_owner_can_use_any_unknown_tool(self, enforcer):
        allowed, _ = enforcer.can_use_tool(OWNER_ID, "some_exotic_tool_xyz")
        assert allowed

    def test_owner_denied_tools_is_empty(self, enforcer):
        assert enforcer.get_denied_tools(OWNER_ID) == []


# ---------------------------------------------------------------------------
# Admin: admin tools + collaborator tools, not private
# ---------------------------------------------------------------------------

class TestAdminAccess:
    def test_admin_blocked_from_private_tool(self, enforcer):
        allowed, reason = enforcer.can_use_tool(ADMIN_ID, "gmail")
        assert not allowed
        assert "owner-private" in reason

    def test_admin_can_use_admin_tool(self, enforcer):
        allowed, _ = enforcer.can_use_tool(ADMIN_ID, "rbac_manage")
        assert allowed

    def test_admin_can_use_collaborator_tool(self, enforcer):
        allowed, _ = enforcer.can_use_tool(ADMIN_ID, "web_search")
        assert allowed

    def test_admin_denied_tools_contains_private(self, enforcer):
        denied = enforcer.get_denied_tools(ADMIN_ID)
        assert "gmail" in denied
        assert "1password" in denied


# ---------------------------------------------------------------------------
# Collaborator: only allowed subset
# ---------------------------------------------------------------------------

class TestCollaboratorAccess:
    def test_collaborator_blocked_from_private_tool(self, enforcer):
        for tool in ["gmail", "icloud", "home_assistant", "banking"]:
            allowed, reason = enforcer.can_use_tool(COLLAB_ID, tool)
            assert not allowed, f"Expected {tool} to be blocked for collaborator"

    def test_collaborator_blocked_from_admin_tool(self, enforcer):
        allowed, reason = enforcer.can_use_tool(COLLAB_ID, "rbac_manage")
        assert not allowed
        assert "admin" in reason

    def test_collaborator_can_use_allowed_tool(self, enforcer):
        for tool in ["read", "write", "web_search", "search"]:
            allowed, _ = enforcer.can_use_tool(COLLAB_ID, tool)
            assert allowed, f"Expected {tool} to be allowed for collaborator"

    def test_collaborator_denied_unknown_by_default(self, enforcer):
        allowed, reason = enforcer.can_use_tool(COLLAB_ID, "super_secret_tool_xyz")
        assert not allowed
        assert "deny_unknown_tools" in reason

    def test_collaborator_denied_tools_includes_admin_and_private(self, enforcer):
        denied = enforcer.get_denied_tools(COLLAB_ID)
        assert "gmail" in denied
        assert "rbac_manage" in denied

    def test_collaborator_allowed_tools_does_not_include_private(self, enforcer):
        allowed = enforcer.get_allowed_tools(COLLAB_ID)
        assert "gmail" not in allowed
        assert "home_assistant" not in allowed


# ---------------------------------------------------------------------------
# Viewer: same as collaborator (no tool use)
# ---------------------------------------------------------------------------

class TestViewerAccess:
    def test_viewer_blocked_from_private_tool(self, enforcer):
        allowed, _ = enforcer.can_use_tool(VIEWER_ID, "icloud")
        assert not allowed

    def test_viewer_blocked_from_admin_tool(self, enforcer):
        allowed, _ = enforcer.can_use_tool(VIEWER_ID, "audit_export")
        assert not allowed


# ---------------------------------------------------------------------------
# Group tool allowlist override
# ---------------------------------------------------------------------------

class TestGroupToolAllowlist:
    def test_group_allowlist_grants_extra_tool(self):
        teams = TeamsConfig(**{
            "groups": {
                "ops": {
                    "name": "Ops Team",
                    "members": [COLLAB_ID],
                    "projects": ["monitoring"],
                    "collab_mode": "project_scoped",
                },
            },
            "projects": {
                "monitoring": {
                    "name": "Monitoring",
                    "focus_topics": ["monitoring"],
                    "allowed_tools": ["monitoring_read", "grafana_query"],
                },
            },
        })
        rbac = _make_rbac(teams)
        acl_cfg = ToolACLConfig(group_tool_allowlists={"ops": ["monitoring_read"]})
        enforcer = ToolACLEnforcer(acl_config=acl_cfg, rbac_config=rbac)
        allowed, reason = enforcer.can_use_tool(COLLAB_ID, "monitoring_read")
        assert allowed
        assert "group" in reason.lower()

    def test_project_allowed_tools_grant_access(self):
        teams = TeamsConfig(**{
            "groups": {
                "data": {
                    "name": "Data Team",
                    "members": [COLLAB_ID],
                    "projects": ["lakehouse"],
                    "collab_mode": "project_scoped",
                },
            },
            "projects": {
                "lakehouse": {
                    "name": "Lakehouse",
                    "focus_topics": ["parquet"],
                    "allowed_tools": ["athena_query", "s3_read"],
                },
            },
        })
        rbac = _make_rbac(teams)
        enforcer = ToolACLEnforcer(acl_config=ToolACLConfig(), rbac_config=rbac)
        # athena_query is in project allowed_tools → granted via group
        allowed, _ = enforcer.can_use_tool(COLLAB_ID, "athena_query")
        assert allowed


# ---------------------------------------------------------------------------
# No RBAC config (defaults to viewer)
# ---------------------------------------------------------------------------

class TestNoRBACConfig:
    def test_no_rbac_defaults_to_viewer(self):
        enforcer = ToolACLEnforcer()
        allowed, _ = enforcer.can_use_tool("anyone", "gmail")
        assert not allowed

    def test_no_rbac_allows_read(self):
        enforcer = ToolACLEnforcer(acl_config=ToolACLConfig(deny_unknown_tools=False))
        allowed, _ = enforcer.can_use_tool("anyone", "read")
        assert allowed


# ---------------------------------------------------------------------------
# deny_unknown_tools=False mode
# ---------------------------------------------------------------------------

class TestDenyUnknownFalse:
    def test_collaborator_can_use_unknown_tool_when_not_denied(self, rbac):
        cfg = ToolACLConfig(deny_unknown_tools=False)
        enforcer = ToolACLEnforcer(acl_config=cfg, rbac_config=rbac)
        allowed, _ = enforcer.can_use_tool(COLLAB_ID, "some_new_tool")
        assert allowed

    def test_private_tool_still_blocked_even_when_deny_unknown_false(self, rbac):
        cfg = ToolACLConfig(deny_unknown_tools=False)
        enforcer = ToolACLEnforcer(acl_config=cfg, rbac_config=rbac)
        allowed, _ = enforcer.can_use_tool(COLLAB_ID, "gmail")
        assert not allowed


# ---------------------------------------------------------------------------
# Classification sets sanity checks
# ---------------------------------------------------------------------------

class TestClassificationSets:
    def test_private_and_admin_do_not_overlap_with_collab_allowed(self):
        overlap_private = PRIVATE_TOOLS & COLLABORATOR_ALLOWED_TOOLS
        assert not overlap_private, f"Private tools leaked into collab allowlist: {overlap_private}"
        overlap_admin = ADMIN_TOOLS & COLLABORATOR_ALLOWED_TOOLS
        assert not overlap_admin, f"Admin tools leaked into collab allowlist: {overlap_admin}"

    def test_private_and_admin_do_not_overlap(self):
        overlap = PRIVATE_TOOLS & ADMIN_TOOLS
        assert not overlap, f"Private/admin tool sets overlap: {overlap}"


# ── C35: Per-Tool Rate Limiting tests ────────────────────────────────────────

class TestToolRateLimiting:
    @pytest.fixture
    def enforcer(self):
        return ToolACLEnforcer()

    def test_under_threshold_passes(self, enforcer):
        """Calls within limits should pass."""
        for _ in range(4):
            assert enforcer.check_tool_rate_limit("user1", "execute_command")

    def test_per_minute_limit_exceeded_blocks(self, enforcer):
        """Exceeding per-minute limit should return False."""
        # execute_command limit is 5/min
        for _ in range(5):
            enforcer.check_tool_rate_limit("user2", "execute_command")
        # 6th call should be blocked
        assert not enforcer.check_tool_rate_limit("user2", "execute_command")

    def test_per_user_isolation(self, enforcer):
        """Rate limits are tracked independently per user."""
        # Exhaust user3's limit
        for _ in range(5):
            enforcer.check_tool_rate_limit("user3", "execute_command")
        enforcer.check_tool_rate_limit("user3", "execute_command")  # blocked
        # user4 should still be allowed
        assert enforcer.check_tool_rate_limit("user4", "execute_command")

    def test_unlisted_tool_always_passes(self, enforcer):
        """Tools not in the rate-limit map should always pass."""
        for _ in range(100):
            assert enforcer.check_tool_rate_limit("user5", "web_search")
