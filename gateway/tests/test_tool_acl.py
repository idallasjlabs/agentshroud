# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for gateway/security/tool_acl.py — V9-T2: Tool-level access control."""

from __future__ import annotations

import pytest

from gateway.security.group_config import TeamsConfig
from gateway.security.rbac_config import RBACConfig, Role
from gateway.security.tool_acl import (
    ADMIN_TOOLS,
    COLLABORATOR_ALLOWED_TOOLS,
    PRIVATE_TOOLS,
    ToolACLConfig,
    ToolACLEnforcer,
)

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
        teams = TeamsConfig(
            **{
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
            }
        )
        rbac = _make_rbac(teams)
        acl_cfg = ToolACLConfig(group_tool_allowlists={"ops": ["monitoring_read"]})
        enforcer = ToolACLEnforcer(acl_config=acl_cfg, rbac_config=rbac)
        allowed, reason = enforcer.can_use_tool(COLLAB_ID, "monitoring_read")
        assert allowed
        assert "group" in reason.lower()

    def test_project_allowed_tools_grant_access(self):
        teams = TeamsConfig(
            **{
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
            }
        )
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


# ── CVE-2026-9367: terminal_tool command injection bypass ────────────────────


class TestCVE2026_9367TerminalToolDenied:
    """terminal_tool must be in PRIVATE_TOOLS and blocked for non-owner principals."""

    def test_terminal_tool_in_private_tools(self):
        assert "terminal_tool" in PRIVATE_TOOLS

    def test_terminal_in_private_tools(self):
        assert "terminal" in PRIVATE_TOOLS

    def test_collaborator_denied_terminal_tool(self, enforcer):
        allowed, reason = enforcer.can_use_tool(COLLAB_ID, "terminal_tool")
        assert not allowed
        assert reason

    def test_owner_allowed_terminal_tool(self, enforcer):
        allowed, _ = enforcer.can_use_tool(OWNER_ID, "terminal_tool")
        assert allowed

    def test_admin_denied_terminal_tool(self, enforcer):
        # terminal_tool is PRIVATE (owner-only), so admin should also be denied
        allowed, _ = enforcer.can_use_tool(ADMIN_ID, "terminal_tool")
        assert not allowed

    def test_viewer_denied_terminal_tool(self, enforcer):
        allowed, _ = enforcer.can_use_tool(VIEWER_ID, "terminal_tool")
        assert not allowed

    def test_terminal_tool_not_in_collab_allowed(self):
        assert "terminal_tool" not in COLLABORATOR_ALLOWED_TOOLS


# ---------------------------------------------------------------------------
# Origin-aware authorization (CVE-derived control, owner directive 2026-09-15)
# ---------------------------------------------------------------------------
class TestOriginAwareAuthorization:
    """AgentShroud-side mitigation for the 'channel skips the check' CVE class.

    Upstream advisories in the OpenClaw registry that all share one shape — a
    request arriving over a side channel is trusted with authority the normal
    path would have checked:

      GHSA-rrxp-5mx8-mvhh (8.8) inbound voice calls could inherit owner tool authorization
      GHSA-58qx-6m8p-wh2j (8.8) Slack group DMs could skip sender allowlists
      GHSA-wwcw-jfpp-gpxw (8.8) native tools could ignore per-chat policy
      GHSA-7cp7-87pj-p32v (8.3) skill dispatch could skip owner-only policy
      GHSA-hpg5-cq3m-phqp (8.3) agent cron tool could reach operator command jobs

    The vendor fix is "upgrade past 2026.8.1", which protects OpenClaw only.
    The durable AgentShroud requirement is different and outlives it: identity
    claimed over an origin that never verified it must not confer owner
    authority, for ANY proxied agent — including a third-party agent that never
    received the vendor's patch.
    """

    def test_owner_over_verified_origin_keeps_full_authority(self, enforcer):
        """The legitimate path must not regress."""
        allowed, _ = enforcer.can_use_tool_from_origin(
            OWNER_ID, "terminal_tool", origin="telegram", origin_verified=True
        )
        assert allowed

    def test_owner_claim_over_unverified_origin_is_refused_elevation(self, enforcer):
        """The core of the CVE class: a side channel claiming to be the owner.

        terminal_tool is owner-private, so refusing elevation must deny it.
        """
        allowed, reason = enforcer.can_use_tool_from_origin(
            OWNER_ID, "terminal_tool", origin="voice_inbound", origin_verified=False
        )
        assert not allowed
        assert "unverified origin" in reason.lower()

    def test_unverified_origin_still_allows_public_tools(self, enforcer):
        """Refusing ELEVATION is not the same as blanket denial — an unverified
        origin still gets the baseline permissions its identity would have."""
        allowed, _ = enforcer.can_use_tool_from_origin(
            OWNER_ID, "web_search", origin="voice_inbound", origin_verified=False
        )
        assert allowed

    def test_non_owner_over_unverified_origin_is_unchanged(self, enforcer):
        """A non-owner gains nothing and loses nothing from origin checking."""
        a1, _ = enforcer.can_use_tool(VIEWER_ID, "terminal_tool")
        a2, _ = enforcer.can_use_tool_from_origin(
            VIEWER_ID, "terminal_tool", origin="voice_inbound", origin_verified=False
        )
        assert a1 == a2 is False

    def test_unknown_origin_defaults_to_unverified(self, enforcer):
        """Fail closed: an origin nobody vouched for is not trusted.

        A caller that forgets to pass origin_verified must not accidentally get
        the permissive branch — that is how this bug class reappears.
        """
        allowed, reason = enforcer.can_use_tool_from_origin(
            OWNER_ID, "terminal_tool", origin="some_new_channel"
        )
        assert not allowed
        assert "unverified origin" in reason.lower()

    def test_denial_is_counted_for_soc_correlation(self, enforcer):
        before = enforcer.get_denial_counts().get(OWNER_ID, 0)
        enforcer.can_use_tool_from_origin(
            OWNER_ID, "terminal_tool", origin="cron", origin_verified=False
        )
        after = enforcer.get_denial_counts().get(OWNER_ID, 0)
        assert after == before + 1

    def test_applies_to_any_agent_not_just_openclaw(self, enforcer):
        """The control is agent-agnostic by construction: it takes an origin and
        an identity, never an agent name. Same refusal regardless of who asks."""
        for agent_origin in ("openclaw_skill", "hermes_cron", "third_party_agent"):
            allowed, _ = enforcer.can_use_tool_from_origin(
                OWNER_ID, "terminal_tool", origin=agent_origin, origin_verified=False
            )
            assert not allowed, f"{agent_origin} was granted owner elevation"
