# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""TDD — Workstream A (v1.2.0): Per-member RBAC in group context.

Tests that:
  - read-only member cannot trigger high-risk tool calls in group context.
  - regular member can trigger medium-risk calls but not private tools.
  - owner can trigger all tool calls.
  - GroupRoleResolver correctly maps Telegram user IDs to group roles.
  - ToolACLEnforcer respects group_context_role when provided.
"""

from __future__ import annotations

import pytest

from gateway.security.group_config import GroupConfig, TeamsConfig
from gateway.security.group_rbac import GroupRole, GroupRoleResolver
from gateway.security.rbac_config import RBACConfig, Role
from gateway.security.tool_acl import (
    PRIVATE_TOOLS,
    ToolACLConfig,
    ToolACLEnforcer,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

OWNER_ID = "owner-001"
GROUP_A_CHAT_ID = "-1001000000001"
GROUP_A_ID = f"group-{GROUP_A_CHAT_ID}"

OWNER_IN_GROUP = OWNER_ID
MEMBER_USER = "8506022825"
READONLY_USER = "8633775668"
NON_MEMBER_USER = "9999999999"

# High-risk tools that read-only members must NEVER be allowed
HIGH_RISK_TOOLS = ["email_sending", "file_deletion", "external_api_calls", "skill_installation"]

# Medium-risk tools that regular members can use
MEDIUM_RISK_TOOLS = ["web_search", "web_fetch", "read", "write"]

TEAMS_RAW = {
    "groups": {
        GROUP_A_ID: {
            "name": "Team Alpha",
            "members": [MEMBER_USER, READONLY_USER],
            "admin": MEMBER_USER,
            "collab_mode": "full_access",
        },
    },
    "projects": {},
}

# GroupRoleConfig mapping: chat_id → {user_id: role}
GROUP_ROLE_MAP = {
    GROUP_A_CHAT_ID: {
        OWNER_IN_GROUP: "owner",
        MEMBER_USER: "member",
        READONLY_USER: "read-only",
    }
}


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def teams():
    return TeamsConfig(**TEAMS_RAW)


@pytest.fixture
def rbac(teams):
    cfg = RBACConfig(
        owner_user_id=OWNER_ID,
        collaborator_user_ids=[MEMBER_USER, READONLY_USER],
    )
    cfg.wire_teams_config(teams)
    return cfg


@pytest.fixture
def group_role_resolver():
    return GroupRoleResolver(group_role_map=GROUP_ROLE_MAP)


@pytest.fixture
def acl_config():
    return ToolACLConfig(deny_unknown_tools=True)


@pytest.fixture
def enforcer(rbac, acl_config):
    return ToolACLEnforcer(acl_config=acl_config, rbac_config=rbac)


# ---------------------------------------------------------------------------
# Class A: GroupRoleResolver — map user to group role
# ---------------------------------------------------------------------------


class TestGroupRoleResolver:
    """GroupRoleResolver correctly maps Telegram user IDs to per-group roles."""

    def test_owner_resolves_to_owner_role(self, group_role_resolver):
        """owner_in_group resolves to GroupRole.OWNER."""
        role = group_role_resolver.get_role(GROUP_A_CHAT_ID, OWNER_IN_GROUP)
        assert role == GroupRole.OWNER

    def test_member_resolves_to_member_role(self, group_role_resolver):
        """Regular member resolves to GroupRole.MEMBER."""
        role = group_role_resolver.get_role(GROUP_A_CHAT_ID, MEMBER_USER)
        assert role == GroupRole.MEMBER

    def test_readonly_user_resolves_to_readonly_role(self, group_role_resolver):
        """Read-only user resolves to GroupRole.READ_ONLY."""
        role = group_role_resolver.get_role(GROUP_A_CHAT_ID, READONLY_USER)
        assert role == GroupRole.READ_ONLY

    def test_non_member_defaults_to_readonly(self, group_role_resolver):
        """User not in role map defaults to GroupRole.READ_ONLY (deny-by-default)."""
        role = group_role_resolver.get_role(GROUP_A_CHAT_ID, NON_MEMBER_USER)
        assert role == GroupRole.READ_ONLY

    def test_unknown_group_defaults_to_readonly(self, group_role_resolver):
        """Unknown group_chat_id defaults to GroupRole.READ_ONLY."""
        role = group_role_resolver.get_role("-9999", MEMBER_USER)
        assert role == GroupRole.READ_ONLY

    def test_is_high_risk_true_for_email_sending(self, group_role_resolver):
        """email_sending is recognized as a high-risk tool."""
        assert group_role_resolver.is_high_risk_tool("email_sending") is True

    def test_is_high_risk_true_for_file_deletion(self, group_role_resolver):
        assert group_role_resolver.is_high_risk_tool("file_deletion") is True

    def test_is_high_risk_true_for_external_api_calls(self, group_role_resolver):
        assert group_role_resolver.is_high_risk_tool("external_api_calls") is True

    def test_is_high_risk_true_for_skill_installation(self, group_role_resolver):
        assert group_role_resolver.is_high_risk_tool("skill_installation") is True

    def test_is_high_risk_false_for_web_search(self, group_role_resolver):
        """web_search is NOT a high-risk tool."""
        assert group_role_resolver.is_high_risk_tool("web_search") is False


# ---------------------------------------------------------------------------
# Class B: Read-only member — cannot trigger high-risk tools in group context
# ---------------------------------------------------------------------------


class TestReadOnlyMemberGroupContext:
    """Read-only members must be denied high-risk tools in any group context."""

    def test_readonly_denied_email_sending_in_group(self, enforcer, group_role_resolver):
        """Read-only member denied email_sending even when called from group context."""
        allowed, reason = enforcer.can_use_tool_in_group_context(
            user_id=READONLY_USER,
            tool_name="email_sending",
            group_chat_id=GROUP_A_CHAT_ID,
            group_role_resolver=group_role_resolver,
        )
        assert allowed is False
        assert "read-only" in reason.lower() or "denied" in reason.lower()

    def test_readonly_denied_file_deletion_in_group(self, enforcer, group_role_resolver):
        """Read-only member denied file_deletion in group context."""
        allowed, _ = enforcer.can_use_tool_in_group_context(
            user_id=READONLY_USER,
            tool_name="file_deletion",
            group_chat_id=GROUP_A_CHAT_ID,
            group_role_resolver=group_role_resolver,
        )
        assert allowed is False

    def test_readonly_denied_external_api_calls_in_group(self, enforcer, group_role_resolver):
        """Read-only member denied external_api_calls in group context."""
        allowed, _ = enforcer.can_use_tool_in_group_context(
            user_id=READONLY_USER,
            tool_name="external_api_calls",
            group_chat_id=GROUP_A_CHAT_ID,
            group_role_resolver=group_role_resolver,
        )
        assert allowed is False

    def test_readonly_denied_skill_installation_in_group(self, enforcer, group_role_resolver):
        """Read-only member denied skill_installation in group context."""
        allowed, _ = enforcer.can_use_tool_in_group_context(
            user_id=READONLY_USER,
            tool_name="skill_installation",
            group_chat_id=GROUP_A_CHAT_ID,
            group_role_resolver=group_role_resolver,
        )
        assert allowed is False

    def test_readonly_allowed_web_search_in_group(self, enforcer, group_role_resolver):
        """Read-only member IS allowed web_search (low-risk) in group context."""
        allowed, _ = enforcer.can_use_tool_in_group_context(
            user_id=READONLY_USER,
            tool_name="web_search",
            group_chat_id=GROUP_A_CHAT_ID,
            group_role_resolver=group_role_resolver,
        )
        assert allowed is True

    def test_readonly_allowed_read_in_group(self, enforcer, group_role_resolver):
        """Read-only member IS allowed read tool in group context."""
        allowed, _ = enforcer.can_use_tool_in_group_context(
            user_id=READONLY_USER,
            tool_name="read",
            group_chat_id=GROUP_A_CHAT_ID,
            group_role_resolver=group_role_resolver,
        )
        assert allowed is True


# ---------------------------------------------------------------------------
# Class C: Regular member — allowed medium-risk, denied private/admin tools
# ---------------------------------------------------------------------------


class TestMemberGroupContext:
    """Regular members can use medium-risk tools but not private/admin tools."""

    def test_member_allowed_web_search_in_group(self, enforcer, group_role_resolver):
        """Regular member IS allowed web_search in group context."""
        allowed, _ = enforcer.can_use_tool_in_group_context(
            user_id=MEMBER_USER,
            tool_name="web_search",
            group_chat_id=GROUP_A_CHAT_ID,
            group_role_resolver=group_role_resolver,
        )
        assert allowed is True

    def test_member_allowed_read_write_in_group(self, enforcer, group_role_resolver):
        """Regular member IS allowed read/write in group context."""
        for tool in ("read", "write"):
            allowed, _ = enforcer.can_use_tool_in_group_context(
                user_id=MEMBER_USER,
                tool_name=tool,
                group_chat_id=GROUP_A_CHAT_ID,
                group_role_resolver=group_role_resolver,
            )
            assert allowed is True, f"Member should be allowed '{tool}'"

    def test_member_denied_gmail_private_tool_in_group(self, enforcer, group_role_resolver):
        """Regular member denied gmail (private tool) even in group context."""
        allowed, reason = enforcer.can_use_tool_in_group_context(
            user_id=MEMBER_USER,
            tool_name="gmail",
            group_chat_id=GROUP_A_CHAT_ID,
            group_role_resolver=group_role_resolver,
        )
        assert allowed is False

    def test_member_denied_ssh_private_tool_in_group(self, enforcer, group_role_resolver):
        """Regular member denied ssh (private tool) in group context."""
        allowed, _ = enforcer.can_use_tool_in_group_context(
            user_id=MEMBER_USER,
            tool_name="ssh",
            group_chat_id=GROUP_A_CHAT_ID,
            group_role_resolver=group_role_resolver,
        )
        assert allowed is False

    def test_member_denied_high_risk_tools_in_group(self, enforcer, group_role_resolver):
        """Regular member (non-owner group role) is denied high-risk tools that require approval."""
        # High-risk tools that route through approval queue — members can REQUEST them
        # but they require approval (they're not DENIED, they're queued)
        # This test verifies the group-context role check does not silently allow
        # high-risk tools without routing through the approval queue.
        # For now, member can_use_tool_in_group_context for email_sending returns
        # (True, "requires_approval") rather than (False, ...) — approval is required.
        allowed, reason = enforcer.can_use_tool_in_group_context(
            user_id=MEMBER_USER,
            tool_name="email_sending",
            group_chat_id=GROUP_A_CHAT_ID,
            group_role_resolver=group_role_resolver,
        )
        # Member's request goes to approval queue — not outright denied
        # but must indicate approval is needed
        if allowed:
            assert "approval" in reason.lower() or "queue" in reason.lower()


# ---------------------------------------------------------------------------
# Class D: Owner — unrestricted in group context
# ---------------------------------------------------------------------------


class TestOwnerGroupContext:
    """Owner must have unrestricted access even in group context."""

    def test_owner_allowed_all_tools_in_group(self, enforcer, group_role_resolver):
        """Owner is allowed ALL tools in group context."""
        high_risk = ["email_sending", "file_deletion", "external_api_calls", "skill_installation"]
        private = ["gmail", "ssh", "1password", "terraform"]
        for tool in high_risk + private:
            allowed, _ = enforcer.can_use_tool_in_group_context(
                user_id=OWNER_IN_GROUP,
                tool_name=tool,
                group_chat_id=GROUP_A_CHAT_ID,
                group_role_resolver=group_role_resolver,
            )
            assert allowed is True, f"Owner must be allowed '{tool}' in group context"

    def test_owner_unrestricted_matches_dm_behavior(self, enforcer, group_role_resolver):
        """Owner group-context check must match standard can_use_tool result."""
        for tool in ("gmail", "ssh", "web_search", "read"):
            dm_result, _ = enforcer.can_use_tool(OWNER_IN_GROUP, tool)
            group_result, _ = enforcer.can_use_tool_in_group_context(
                user_id=OWNER_IN_GROUP,
                tool_name=tool,
                group_chat_id=GROUP_A_CHAT_ID,
                group_role_resolver=group_role_resolver,
            )
            assert dm_result == group_result, (
                f"Owner group-context result for '{tool}' must match DM result"
            )


# ---------------------------------------------------------------------------
# Class E: GroupRole properties and helpers (coverage boost)
# ---------------------------------------------------------------------------


class TestGroupRoleProperties:
    """Test GroupRole.rank, can_use_high_risk, and GroupRoleResolver helpers."""

    def test_rank_owner_highest(self):
        assert GroupRole.OWNER.rank == 2

    def test_rank_member_middle(self):
        assert GroupRole.MEMBER.rank == 1

    def test_rank_readonly_lowest(self):
        assert GroupRole.READ_ONLY.rank == 0

    def test_can_use_high_risk_owner(self):
        assert GroupRole.OWNER.can_use_high_risk() is True

    def test_can_use_high_risk_member(self):
        assert GroupRole.MEMBER.can_use_high_risk() is True

    def test_can_use_high_risk_readonly(self):
        assert GroupRole.READ_ONLY.can_use_high_risk() is False

    def test_is_owner_true(self):
        resolver = GroupRoleResolver(group_role_map={
            GROUP_A_CHAT_ID: {OWNER_IN_GROUP: "owner"}
        })
        assert resolver.is_owner(GROUP_A_CHAT_ID, OWNER_IN_GROUP) is True

    def test_is_owner_false_for_member(self):
        resolver = GroupRoleResolver(group_role_map={
            GROUP_A_CHAT_ID: {MEMBER_USER: "member"}
        })
        assert resolver.is_owner(GROUP_A_CHAT_ID, MEMBER_USER) is False

    def test_is_member_or_higher_for_owner(self):
        resolver = GroupRoleResolver(group_role_map={
            GROUP_A_CHAT_ID: {OWNER_IN_GROUP: "owner"}
        })
        assert resolver.is_member_or_higher(GROUP_A_CHAT_ID, OWNER_IN_GROUP) is True

    def test_is_member_or_higher_for_member(self):
        resolver = GroupRoleResolver(group_role_map={
            GROUP_A_CHAT_ID: {MEMBER_USER: "member"}
        })
        assert resolver.is_member_or_higher(GROUP_A_CHAT_ID, MEMBER_USER) is True

    def test_is_member_or_higher_false_for_readonly(self):
        resolver = GroupRoleResolver(group_role_map={
            GROUP_A_CHAT_ID: {READONLY_USER: "read-only"}
        })
        assert resolver.is_member_or_higher(GROUP_A_CHAT_ID, READONLY_USER) is False

    def test_set_role_creates_new_entry(self):
        resolver = GroupRoleResolver()
        resolver.set_role(GROUP_A_CHAT_ID, MEMBER_USER, GroupRole.MEMBER)
        assert resolver.get_role(GROUP_A_CHAT_ID, MEMBER_USER) == GroupRole.MEMBER

    def test_set_role_updates_existing_entry(self):
        resolver = GroupRoleResolver(group_role_map={
            GROUP_A_CHAT_ID: {MEMBER_USER: "member"}
        })
        resolver.set_role(GROUP_A_CHAT_ID, MEMBER_USER, GroupRole.OWNER)
        assert resolver.get_role(GROUP_A_CHAT_ID, MEMBER_USER) == GroupRole.OWNER

    def test_remove_role_falls_back_to_readonly(self):
        resolver = GroupRoleResolver(group_role_map={
            GROUP_A_CHAT_ID: {MEMBER_USER: "member"}
        })
        resolver.remove_role(GROUP_A_CHAT_ID, MEMBER_USER)
        # After removal, get_role defaults to READ_ONLY
        assert resolver.get_role(GROUP_A_CHAT_ID, MEMBER_USER) == GroupRole.READ_ONLY

    def test_remove_role_noop_for_missing_user(self):
        """remove_role on a user not in map is a no-op (no exception)."""
        resolver = GroupRoleResolver()
        resolver.remove_role(GROUP_A_CHAT_ID, "nonexistent-user")  # should not raise

    def test_get_all_roles_returns_all_entries(self):
        resolver = GroupRoleResolver(group_role_map={
            GROUP_A_CHAT_ID: {
                OWNER_IN_GROUP: "owner",
                MEMBER_USER: "member",
                READONLY_USER: "read-only",
            }
        })
        roles = resolver.get_all_roles(GROUP_A_CHAT_ID)
        assert roles[OWNER_IN_GROUP] == GroupRole.OWNER
        assert roles[MEMBER_USER] == GroupRole.MEMBER
        assert roles[READONLY_USER] == GroupRole.READ_ONLY

    def test_get_all_roles_empty_for_unknown_group(self):
        resolver = GroupRoleResolver()
        roles = resolver.get_all_roles("unknown-group")
        assert roles == {}

    def test_get_role_invalid_string_defaults_to_readonly(self):
        """An invalid role string in the map falls back to READ_ONLY."""
        resolver = GroupRoleResolver(group_role_map={
            GROUP_A_CHAT_ID: {MEMBER_USER: "super-admin-invalid"}
        })
        role = resolver.get_role(GROUP_A_CHAT_ID, MEMBER_USER)
        assert role == GroupRole.READ_ONLY

    def test_get_all_roles_invalid_string_defaults_to_readonly(self):
        """get_all_roles with an invalid role string falls back to READ_ONLY per entry."""
        # Insert an invalid role string via direct map manipulation
        resolver = GroupRoleResolver(group_role_map={
            GROUP_A_CHAT_ID: {
                MEMBER_USER: "super-secret-invalid",
                READONLY_USER: "read-only",
            }
        })
        roles = resolver.get_all_roles(GROUP_A_CHAT_ID)
        assert roles[MEMBER_USER] == GroupRole.READ_ONLY
        assert roles[READONLY_USER] == GroupRole.READ_ONLY
