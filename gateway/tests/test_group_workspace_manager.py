# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""TDD — SCRUM-67 WS-A: Group workspace manager.

Enforces that a Telegram GROUP acts as a shared team workspace with:
  - Member-gated access: only members (or the system owner) can resolve a
    group's shared workspace/context id.
  - Fail-closed membership checks: unknown group / non-member is DENIED.
  - Cross-group isolation: resolving group A's workspace can never yield group
    B's workspace id, and a member of A cannot access B's workspace.
  - DM isolation: a direct-message context (no group chat id) resolves to a
    distinct per-user namespace, never a group workspace.
  - Memory scoping: reads/writes through the manager are member-gated and land
    in the correct isolated namespace (group vs DM).

These tests are mocked, deterministic, and perform no network / real I/O beyond
tmp_path-backed session storage.
"""

from __future__ import annotations

import pytest

from gateway.security.group_config import TeamsConfig
from gateway.security.group_workspace import (
    GroupAccessDenied,
    GroupWorkspaceManager,
)
from gateway.security.rbac_config import RBACConfig
from gateway.security.session_manager import UserSessionManager
from gateway.security.shared_memory import SharedMemoryManager

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

OWNER_ID = "owner-001"
USER_A = "user-111"
USER_B = "user-222"
STRANGER = "user-999"

GROUP_A_CHAT_ID = "-1001000000001"
GROUP_B_CHAT_ID = "-1001000000002"
GROUP_A_ID = f"group-{GROUP_A_CHAT_ID}"
GROUP_B_ID = f"group-{GROUP_B_CHAT_ID}"

TEAMS_RAW = {
    "groups": {
        GROUP_A_ID: {
            "name": "Team Alpha",
            "members": [USER_A],
            "admin": USER_A,
            "collab_mode": "full_access",
        },
        GROUP_B_ID: {
            "name": "Team Beta",
            "members": [USER_B],
            "admin": USER_B,
            "collab_mode": "full_access",
        },
    },
    "projects": {},
}


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def teams():
    return TeamsConfig(**TEAMS_RAW)


@pytest.fixture
def rbac(teams):
    cfg = RBACConfig(owner_user_id=OWNER_ID, collaborator_user_ids=[USER_A, USER_B])
    cfg.wire_teams_config(teams)
    return cfg


@pytest.fixture
def session_manager(tmp_path):
    return UserSessionManager(base_workspace=tmp_path / "workspace", owner_user_id=OWNER_ID)


@pytest.fixture
def shared_memory(session_manager):
    return SharedMemoryManager(session_manager=session_manager)


@pytest.fixture
def manager(teams, rbac, shared_memory):
    return GroupWorkspaceManager(
        teams_config=teams,
        rbac_config=rbac,
        shared_memory=shared_memory,
    )


# ---------------------------------------------------------------------------
# Class A: members share the group workspace
# ---------------------------------------------------------------------------


class TestMembersShareGroupWorkspace:
    def test_member_can_access_group_workspace(self, manager):
        assert manager.can_access(GROUP_A_CHAT_ID, USER_A) is True

    def test_member_resolves_to_shared_workspace_id(self, manager):
        ws = manager.resolve_workspace(GROUP_A_CHAT_ID, USER_A)
        assert ws.workspace_id == GROUP_A_ID
        assert ws.group_chat_id == GROUP_A_CHAT_ID
        assert ws.is_group is True

    def test_two_members_of_same_group_share_one_workspace_id(self, teams, rbac, shared_memory):
        # Add a second member to group A at runtime.
        teams.groups[GROUP_A_ID].members.append(USER_B)
        mgr = GroupWorkspaceManager(
            teams_config=teams, rbac_config=rbac, shared_memory=shared_memory
        )
        ws_a = mgr.resolve_workspace(GROUP_A_CHAT_ID, USER_A)
        ws_b = mgr.resolve_workspace(GROUP_A_CHAT_ID, USER_B)
        assert ws_a.workspace_id == ws_b.workspace_id == GROUP_A_ID

    def test_system_owner_can_access_any_group(self, manager):
        # Owner is not listed in members but must be allowed (admin oversight).
        assert manager.can_access(GROUP_A_CHAT_ID, OWNER_ID) is True
        ws = manager.resolve_workspace(GROUP_A_CHAT_ID, OWNER_ID)
        assert ws.workspace_id == GROUP_A_ID

    def test_members_share_group_memory(self, manager):
        manager.append_group_memory(GROUP_A_CHAT_ID, USER_A, "Alpha shared note")
        # A second member reads the same content back.
        manager.teams_config.groups[GROUP_A_ID].members.append(USER_B)
        text = manager.read_group_memory(GROUP_A_CHAT_ID, USER_B)
        assert "Alpha shared note" in text


# ---------------------------------------------------------------------------
# Class B: non-member is denied (fail-closed)
# ---------------------------------------------------------------------------


class TestNonMemberDenied:
    def test_stranger_cannot_access(self, manager):
        assert manager.can_access(GROUP_A_CHAT_ID, STRANGER) is False

    def test_stranger_resolve_raises(self, manager):
        with pytest.raises(GroupAccessDenied):
            manager.resolve_workspace(GROUP_A_CHAT_ID, STRANGER)

    def test_unknown_group_denied(self, manager):
        assert manager.can_access("-1009999999999", USER_A) is False
        with pytest.raises(GroupAccessDenied):
            manager.resolve_workspace("-1009999999999", USER_A)

    def test_stranger_cannot_read_group_memory(self, manager):
        manager.append_group_memory(GROUP_A_CHAT_ID, USER_A, "secret")
        with pytest.raises(GroupAccessDenied):
            manager.read_group_memory(GROUP_A_CHAT_ID, STRANGER)

    def test_stranger_cannot_write_group_memory(self, manager):
        with pytest.raises(GroupAccessDenied):
            manager.append_group_memory(GROUP_A_CHAT_ID, STRANGER, "inject")
        # Nothing was written under the group's namespace.
        assert "inject" not in manager.read_group_memory(GROUP_A_CHAT_ID, USER_A)

    def test_no_teams_config_fails_closed(self, shared_memory):
        mgr = GroupWorkspaceManager(
            teams_config=None, rbac_config=None, shared_memory=shared_memory
        )
        assert mgr.can_access(GROUP_A_CHAT_ID, USER_A) is False
        with pytest.raises(GroupAccessDenied):
            mgr.resolve_workspace(GROUP_A_CHAT_ID, USER_A)


# ---------------------------------------------------------------------------
# Class C: group A cannot access group B's workspace
# ---------------------------------------------------------------------------


class TestCrossGroupIsolation:
    def test_member_of_a_denied_group_b(self, manager):
        assert manager.can_access(GROUP_B_CHAT_ID, USER_A) is False
        with pytest.raises(GroupAccessDenied):
            manager.resolve_workspace(GROUP_B_CHAT_ID, USER_A)

    def test_workspace_ids_are_distinct_per_group(self, manager):
        ws_a = manager.resolve_workspace(GROUP_A_CHAT_ID, USER_A)
        ws_b = manager.resolve_workspace(GROUP_B_CHAT_ID, USER_B)
        assert ws_a.workspace_id != ws_b.workspace_id

    def test_group_a_write_invisible_from_group_b(self, manager):
        manager.append_group_memory(GROUP_A_CHAT_ID, USER_A, "Alpha only")
        group_b_text = manager.read_group_memory(GROUP_B_CHAT_ID, USER_B)
        assert "Alpha only" not in group_b_text

    def test_member_of_a_cannot_read_group_b_memory(self, manager):
        manager.append_group_memory(GROUP_B_CHAT_ID, USER_B, "Beta secret")
        with pytest.raises(GroupAccessDenied):
            manager.read_group_memory(GROUP_B_CHAT_ID, USER_A)


# ---------------------------------------------------------------------------
# Class D: DM isolation from group workspaces
# ---------------------------------------------------------------------------


class TestDmIsolation:
    def test_dm_context_resolves_to_user_namespace(self, manager):
        ws = manager.resolve_workspace(group_chat_id=None, user_id=USER_A)
        assert ws.is_group is False
        assert ws.group_chat_id is None
        assert ws.workspace_id == f"dm-{USER_A}"

    def test_dm_workspace_id_differs_from_group(self, manager):
        dm = manager.resolve_workspace(group_chat_id=None, user_id=USER_A)
        grp = manager.resolve_workspace(GROUP_A_CHAT_ID, USER_A)
        assert dm.workspace_id != grp.workspace_id

    def test_dm_write_invisible_from_group(self, manager):
        manager.append_dm_memory(USER_A, "My DM secret")
        group_text = manager.read_group_memory(GROUP_A_CHAT_ID, USER_A)
        assert "My DM secret" not in group_text

    def test_group_write_invisible_from_dm(self, manager):
        manager.append_group_memory(GROUP_A_CHAT_ID, USER_A, "Group note")
        dm_text = manager.read_dm_memory(USER_A)
        assert "Group note" not in dm_text

    def test_dm_context_needs_no_membership(self, manager):
        # A DM from a stranger is a valid DM namespace (their own), never a group.
        assert manager.can_access(group_chat_id=None, user_id=STRANGER) is True
        ws = manager.resolve_workspace(group_chat_id=None, user_id=STRANGER)
        assert ws.workspace_id == f"dm-{STRANGER}"


# ---------------------------------------------------------------------------
# Class E: config gate (default-safe)
# ---------------------------------------------------------------------------


class TestConfigGate:
    def test_disabled_manager_denies_group_resolve(self, teams, rbac, shared_memory):
        mgr = GroupWorkspaceManager(
            teams_config=teams,
            rbac_config=rbac,
            shared_memory=shared_memory,
            enabled=False,
        )
        # Even a genuine member is denied when the feature is disabled (fail-closed).
        assert mgr.can_access(GROUP_A_CHAT_ID, USER_A) is False
        with pytest.raises(GroupAccessDenied):
            mgr.resolve_workspace(GROUP_A_CHAT_ID, USER_A)

    def test_disabled_manager_still_allows_dm(self, teams, rbac, shared_memory):
        mgr = GroupWorkspaceManager(
            teams_config=teams,
            rbac_config=rbac,
            shared_memory=shared_memory,
            enabled=False,
        )
        ws = mgr.resolve_workspace(group_chat_id=None, user_id=USER_A)
        assert ws.workspace_id == f"dm-{USER_A}"

    def test_enabled_default_true(self, manager):
        assert manager.enabled is True


# ---------------------------------------------------------------------------
# Class F: inbound chokepoint wiring (TelegramAPIProxy)
#
# Proves the manager is actually wired into the real inbound path where the
# group-context contextvar is resolved: a non-member / cross-group user is
# isolated from the group workspace, while a member is allowed.
# ---------------------------------------------------------------------------


class TestInboundChokepointWiring:
    @pytest.fixture
    def proxy(self, teams, rbac, monkeypatch):
        from gateway.proxy.telegram_proxy import TelegramAPIProxy

        px = TelegramAPIProxy()
        # Inject test teams/RBAC into the real resolution properties.
        monkeypatch.setattr(type(px), "_teams_config", property(lambda self: teams), raising=True)
        px._rbac = rbac
        # Ensure the feature gate is on.
        monkeypatch.setenv("AGENTSHROUD_GROUP_WORKSPACES_ENABLED", "1")
        return px

    def test_manager_is_wired(self, proxy):
        mgr = proxy._group_workspace_manager()
        assert mgr is not None
        assert mgr.enabled is True

    def test_member_allowed_in_group(self, proxy):
        assert proxy._enforce_group_workspace_access(GROUP_A_CHAT_ID, USER_A) is True

    def test_non_member_blocked_in_group(self, proxy):
        assert proxy._enforce_group_workspace_access(GROUP_A_CHAT_ID, STRANGER) is False

    def test_cross_group_member_blocked(self, proxy):
        # USER_A belongs to group A only — denied in group B.
        assert proxy._enforce_group_workspace_access(GROUP_B_CHAT_ID, USER_A) is False

    def test_owner_allowed_in_any_group(self, proxy):
        assert proxy._enforce_group_workspace_access(GROUP_A_CHAT_ID, OWNER_ID) is True

    def test_non_member_contextvar_isolated_to_none(self, proxy):
        """Simulate the chokepoint: a non-member's active group id is cleared."""
        active_group = GROUP_A_CHAT_ID
        if active_group is not None and not proxy._enforce_group_workspace_access(
            active_group, STRANGER
        ):
            active_group = None
        assert active_group is None

    def test_member_contextvar_preserved(self, proxy):
        active_group = GROUP_A_CHAT_ID
        if active_group is not None and not proxy._enforce_group_workspace_access(
            active_group, USER_A
        ):
            active_group = None
        assert active_group == GROUP_A_CHAT_ID

    def test_disabled_gate_returns_none_manager(self, proxy, monkeypatch):
        monkeypatch.setenv("AGENTSHROUD_GROUP_WORKSPACES_ENABLED", "0")
        assert proxy._group_workspace_manager() is None
        # Disabled → legacy behaviour: enforcement passes through (True).
        assert proxy._enforce_group_workspace_access(GROUP_A_CHAT_ID, STRANGER) is True


# ---------------------------------------------------------------------------
# Class G: defensive guards (owner override edge cases, memory-less manager)
# ---------------------------------------------------------------------------


class TestDefensiveGuards:
    def test_no_rbac_owner_check_is_false(self, teams, shared_memory):
        # teams present but rbac_config=None → _is_owner short-circuits to False,
        # and a genuine member is still resolvable via membership.
        mgr = GroupWorkspaceManager(
            teams_config=teams, rbac_config=None, shared_memory=shared_memory
        )
        assert mgr._is_owner(OWNER_ID) is False
        assert mgr.can_access(GROUP_A_CHAT_ID, USER_A) is True
        # A non-member with no owner override is denied.
        assert mgr.can_access(GROUP_A_CHAT_ID, STRANGER) is False

    def test_rbac_without_is_owner_callable(self, teams, shared_memory):
        class _BadRBAC:
            is_owner = "not-callable"

        mgr = GroupWorkspaceManager(
            teams_config=teams, rbac_config=_BadRBAC(), shared_memory=shared_memory
        )
        assert mgr._is_owner(OWNER_ID) is False

    def test_memory_helpers_require_shared_memory(self, teams, rbac):
        mgr = GroupWorkspaceManager(teams_config=teams, rbac_config=rbac, shared_memory=None)
        with pytest.raises(RuntimeError):
            mgr.read_group_memory(GROUP_A_CHAT_ID, USER_A)

    def test_group_keyed_by_raw_chat_id(self, rbac, shared_memory):
        # A TeamsConfig where the group is keyed by the raw chat_id (no prefix)
        # is still resolvable via the raw-key fallback.
        raw_teams = TeamsConfig(
            **{
                "groups": {
                    GROUP_A_CHAT_ID: {
                        "name": "Raw Keyed",
                        "members": [USER_A],
                        "admin": USER_A,
                        "collab_mode": "full_access",
                    }
                },
                "projects": {},
            }
        )
        mgr = GroupWorkspaceManager(
            teams_config=raw_teams, rbac_config=rbac, shared_memory=shared_memory
        )
        assert mgr.can_access(GROUP_A_CHAT_ID, USER_A) is True
