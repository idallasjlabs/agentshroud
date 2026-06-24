# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""TDD — Workstream A (v1.2.0): Group memory namespace isolation.

Tests that:
  - Writes to group-A workspace are invisible from group-B workspace.
  - Writes to group-A workspace are invisible from any DM (user) workspace.
  - group-{chat_id} identity is a distinct namespace in SharedMemoryManager.
  - The AgentRegistry accepts group-{chat_id} agent IDs with chat_type metadata.
"""

from __future__ import annotations

import tempfile
from pathlib import Path

import pytest

from gateway.security.agent_isolation import AgentRegistry, ContainerConfig
from gateway.security.group_config import TeamsConfig
from gateway.security.rbac_config import RBACConfig
from gateway.security.session_manager import UserSessionManager
from gateway.security.shared_memory import SharedMemoryManager

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

OWNER_ID = "owner-001"
USER_A = "user-111"
USER_B = "user-222"
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
def tmp_workspace(tmp_path):
    return tmp_path / "workspace"


@pytest.fixture
def session_manager(tmp_workspace):
    return UserSessionManager(base_workspace=tmp_workspace, owner_user_id=OWNER_ID)


@pytest.fixture
def teams():
    return TeamsConfig(**TEAMS_RAW)


@pytest.fixture
def rbac(teams):
    cfg = RBACConfig(
        owner_user_id=OWNER_ID,
        collaborator_user_ids=[USER_A, USER_B],
    )
    cfg.wire_teams_config(teams)
    return cfg


@pytest.fixture
def shared_memory(session_manager):
    return SharedMemoryManager(session_manager=session_manager)


# ---------------------------------------------------------------------------
# Class A: group-{chat_id} memory namespace isolation
# ---------------------------------------------------------------------------


class TestGroupMemoryNamespaceIsolation:
    """Writes in group-A must not be readable from group-B."""

    def test_group_a_write_invisible_from_group_b(self, shared_memory):
        """Content appended to group-A memory must not appear in group-B memory."""
        shared_memory.append_to_group_memory(
            GROUP_A_ID, "Secret Alpha data", author_id=USER_A
        )

        group_b_mem = shared_memory.get_group_memory(GROUP_B_ID)
        assert "Secret Alpha data" not in group_b_mem

    def test_group_b_write_invisible_from_group_a(self, shared_memory):
        """Content appended to group-B must not appear in group-A memory."""
        shared_memory.append_to_group_memory(
            GROUP_B_ID, "Secret Beta data", author_id=USER_B
        )

        group_a_mem = shared_memory.get_group_memory(GROUP_A_ID)
        assert "Secret Beta data" not in group_a_mem

    def test_group_writes_are_independent_namespaces(self, shared_memory):
        """Both groups store separate content with no cross-contamination."""
        shared_memory.append_to_group_memory(GROUP_A_ID, "alpha content", author_id=USER_A)
        shared_memory.append_to_group_memory(GROUP_B_ID, "beta content", author_id=USER_B)

        group_a_mem = shared_memory.get_group_memory(GROUP_A_ID)
        group_b_mem = shared_memory.get_group_memory(GROUP_B_ID)

        assert "alpha content" in group_a_mem
        assert "beta content" not in group_a_mem
        assert "beta content" in group_b_mem
        assert "alpha content" not in group_b_mem

    def test_group_memory_physically_isolated(self, session_manager):
        """group-A and group-B memory files must be in separate directories."""
        gs_a = session_manager.get_or_create_group_session(GROUP_A_ID)
        gs_b = session_manager.get_or_create_group_session(GROUP_B_ID)

        assert gs_a.memory_file != gs_b.memory_file
        assert gs_a.workspace_dir != gs_b.workspace_dir

    def test_group_id_uses_group_prefix_namespace(self, session_manager, tmp_workspace):
        """group-{chat_id} sessions must live under the 'groups' subdirectory."""
        gs = session_manager.get_or_create_group_session(GROUP_A_ID)

        # Must be under base_workspace/groups/{group_id}/
        expected_prefix = tmp_workspace / "groups"
        assert str(gs.memory_file).startswith(str(expected_prefix))


# ---------------------------------------------------------------------------
# Class B: group memory invisible from DM (user) workspaces
# ---------------------------------------------------------------------------


class TestGroupMemoryInvisibleFromDM:
    """Group workspace content must not leak into any user's DM workspace."""

    def test_group_write_invisible_from_user_dm(self, shared_memory):
        """Content written to a group must not appear in any user's private DM memory."""
        shared_memory.append_to_group_memory(
            GROUP_A_ID, "Group private note", author_id=USER_A
        )

        user_a_mem = shared_memory.get_user_memory(USER_A)
        assert "Group private note" not in user_a_mem

    def test_user_dm_write_invisible_from_group(self, shared_memory):
        """Content written to a user DM must not appear in any group memory."""
        shared_memory.append_to_user_memory(USER_A, "My personal DM note")

        group_a_mem = shared_memory.get_group_memory(GROUP_A_ID)
        assert "My personal DM note" not in group_a_mem

    def test_user_dm_write_invisible_from_other_group(self, shared_memory):
        """User DM content must not leak into a group the user is NOT a member of."""
        shared_memory.append_to_user_memory(USER_A, "User A private")

        group_b_mem = shared_memory.get_group_memory(GROUP_B_ID)
        assert "User A private" not in group_b_mem

    def test_merged_memory_separates_group_and_dm(self, shared_memory, rbac):
        """get_merged_memory_for_user returns group section and private section separately."""
        shared_memory.append_to_group_memory(GROUP_A_ID, "Alpha shared note", author_id=USER_A)
        shared_memory.append_to_user_memory(USER_A, "User A private note")

        merged = shared_memory.get_merged_memory_for_user(
            user_id=USER_A, rbac_config=rbac, active_group_id=GROUP_A_ID
        )

        assert "Alpha shared note" in merged
        assert "User A private note" in merged
        # Beta group content must not appear (USER_A not in GROUP_B)
        assert GROUP_B_ID not in merged or "Team Beta" not in merged


# ---------------------------------------------------------------------------
# Class C: AgentRegistry accepts group-{chat_id} identities
# ---------------------------------------------------------------------------


class TestAgentRegistryGroupIdentity:
    """AgentRegistry must accept group-{chat_id} agent IDs with chat_type metadata."""

    def test_register_group_agent_identity(self):
        """Register a group-{chat_id} identity in AgentRegistry."""
        registry = AgentRegistry()
        cfg = ContainerConfig(
            agent_id=GROUP_A_ID,
            container_name="agentshroud-group-alpha",
            network="agentshroud-internal",
            volume="group-alpha-config",
        )
        registry.register(cfg)

        assert GROUP_A_ID in registry.list_agents()
        retrieved = registry.get(GROUP_A_ID)
        assert retrieved.agent_id == GROUP_A_ID

    def test_register_group_agent_with_chat_type_supergroup(self):
        """Register a supergroup-type agent identity."""
        registry = AgentRegistry()
        cfg = ContainerConfig(
            agent_id="group--1001000000003",
            container_name="agentshroud-group-super",
            network="agentshroud-internal",
            volume="group-super-config",
            env_vars={"chat_type": "supergroup", "chat_id": "-1001000000003"},
        )
        registry.register(cfg)

        retrieved = registry.get("group--1001000000003")
        assert retrieved is not None
        assert retrieved.env_vars.get("chat_type") == "supergroup"

    def test_group_and_collab_identities_coexist(self):
        """group-{chat_id} and collab-{uid} identities can coexist in the same registry."""
        registry = AgentRegistry()
        group_cfg = ContainerConfig(
            agent_id=GROUP_A_ID,
            container_name="agentshroud-group-alpha",
            network="agentshroud-internal",
            volume="group-alpha-config",
        )
        collab_cfg = ContainerConfig(
            agent_id="collab-8506022825",
            container_name="agentshroud-collab-brett",
            network="agentshroud-internal",
            volume="collab-brett-config",
        )
        registry.register(group_cfg)
        registry.register(collab_cfg)

        agents = registry.list_agents()
        assert GROUP_A_ID in agents
        assert "collab-8506022825" in agents

    def test_group_agents_are_isolatable(self):
        """Two group identities should each have distinct volumes."""
        registry = AgentRegistry()
        registry.register(
            ContainerConfig(
                agent_id=GROUP_A_ID,
                container_name="agentshroud-group-alpha",
                network="agentshroud-internal",
                volume="group-alpha-vol",
            )
        )
        registry.register(
            ContainerConfig(
                agent_id=GROUP_B_ID,
                container_name="agentshroud-group-beta",
                network="agentshroud-internal",
                volume="group-beta-vol",
            )
        )

        cfg_a = registry.get(GROUP_A_ID)
        cfg_b = registry.get(GROUP_B_ID)
        assert cfg_a.volume != cfg_b.volume
