# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for gateway/security/shared_memory.py — V9-T1: Group shared memory + isolation."""

from __future__ import annotations

import tempfile
from pathlib import Path

import pytest

from gateway.security.group_config import TeamsConfig
from gateway.security.rbac_config import RBACConfig
from gateway.security.session_manager import UserSessionManager
from gateway.security.shared_memory import SharedMemoryManager

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

OWNER_ID = "owner-001"
USER_A = "8279589982"  # sort group member
USER_B = "8506022825"  # gsdea group member
RANDO = "9999999999"  # not in any group

TEAMS_RAW = {
    "groups": {
        "sort": {
            "name": "SysOps Reliability Team",
            "members": [USER_A],
            "admin": USER_A,
            "projects": ["fleet-alarms"],
            "collab_mode": "project_scoped",
        },
        "gsdea": {
            "name": "Digital Enablement",
            "members": [USER_B],
            "admin": USER_B,
            "projects": ["aws-finops"],
            "collab_mode": "local_only",
        },
    },
    "projects": {
        "fleet-alarms": {
            "name": "Fleet Alarm Standardization",
            "focus_topics": ["alarms", "monitoring", "bess"],
            "allowed_tools": ["read", "write"],
        },
        "aws-finops": {
            "name": "AWS Cost Optimization",
            "focus_topics": ["aws", "cost"],
            "allowed_tools": ["read"],
        },
    },
}


@pytest.fixture
def tmp_workspace(tmp_path):
    return tmp_path / "workspace"


@pytest.fixture
def session_mgr(tmp_workspace):
    return UserSessionManager(base_workspace=tmp_workspace, owner_user_id=OWNER_ID)


@pytest.fixture
def rbac(session_mgr):
    teams = TeamsConfig(**TEAMS_RAW)
    cfg = RBACConfig(owner_user_id=OWNER_ID)
    cfg.wire_teams_config(teams)
    return cfg


@pytest.fixture
def smm(session_mgr):
    return SharedMemoryManager(session_manager=session_mgr)


# ---------------------------------------------------------------------------
# Group memory — read / write
# ---------------------------------------------------------------------------


class TestGroupMemoryReadWrite:
    def test_get_group_memory_empty_initially(self, smm):
        content = smm.get_group_memory("sort")
        # Either empty string or the initialised placeholder
        assert isinstance(content, str)

    def test_append_to_group_memory(self, smm):
        smm.append_to_group_memory("sort", "Test entry", author_id=USER_A)
        content = smm.get_group_memory("sort")
        assert "Test entry" in content
        assert USER_A in content

    def test_multiple_appends_accumulate(self, smm):
        smm.append_to_group_memory("sort", "Entry one", author_id=USER_A)
        smm.append_to_group_memory("sort", "Entry two", author_id=USER_A)
        content = smm.get_group_memory("sort")
        assert "Entry one" in content
        assert "Entry two" in content


# ---------------------------------------------------------------------------
# User private memory
# ---------------------------------------------------------------------------


class TestUserPrivateMemory:
    def test_get_user_memory_returns_string(self, smm):
        content = smm.get_user_memory(USER_A)
        assert isinstance(content, str)

    def test_append_to_user_memory(self, smm):
        smm.append_to_user_memory(USER_A, "My private note")
        content = smm.get_user_memory(USER_A)
        assert "My private note" in content

    def test_user_memory_isolated_between_users(self, smm):
        smm.append_to_user_memory(USER_A, "User A secret")
        smm.append_to_user_memory(USER_B, "User B secret")
        a_mem = smm.get_user_memory(USER_A)
        b_mem = smm.get_user_memory(USER_B)
        assert "User A secret" in a_mem
        assert "User B secret" not in a_mem
        assert "User B secret" in b_mem
        assert "User A secret" not in b_mem


# ---------------------------------------------------------------------------
# Merged memory for user
# ---------------------------------------------------------------------------


class TestMergedMemory:
    def test_user_sees_own_private_memory(self, smm, rbac):
        smm.append_to_user_memory(USER_A, "My private note A")
        merged = smm.get_merged_memory_for_user(USER_A, rbac)
        assert "My private note A" in merged

    def test_user_sees_their_group_memory(self, smm, rbac):
        smm.append_to_group_memory("sort", "SORT group info", author_id=USER_A)
        merged = smm.get_merged_memory_for_user(USER_A, rbac)
        assert "SORT group info" in merged

    def test_user_does_not_see_other_group_memory(self, smm, rbac):
        smm.append_to_group_memory("gsdea", "GSDEA secret", author_id=USER_B)
        merged = smm.get_merged_memory_for_user(USER_A, rbac)
        assert "GSDEA secret" not in merged

    def test_owner_sees_all_groups(self, smm, rbac):
        smm.append_to_group_memory("sort", "SORT info", author_id=USER_A)
        smm.append_to_group_memory("gsdea", "GSDEA info", author_id=USER_B)
        merged = smm.get_merged_memory_for_user(OWNER_ID, rbac)
        assert "SORT info" in merged
        assert "GSDEA info" in merged

    def test_unknown_user_sees_only_private_memory(self, smm, rbac):
        smm.append_to_user_memory(RANDO, "Rando private")
        smm.append_to_group_memory("sort", "Group secret", author_id=USER_A)
        merged = smm.get_merged_memory_for_user(RANDO, rbac)
        assert "Rando private" in merged
        assert "Group secret" not in merged

    def test_active_group_appears_first(self, smm, rbac):
        # USER_A is only in sort, so active_group_id is sort — verify it appears
        smm.append_to_group_memory("sort", "SORT first", author_id=USER_A)
        merged = smm.get_merged_memory_for_user(USER_A, rbac, active_group_id="sort")
        assert "SORT first" in merged


# ---------------------------------------------------------------------------
# Private content detection and filtering
# ---------------------------------------------------------------------------


class TestPrivateContentDetection:
    def test_detects_api_key_pattern(self):
        assert SharedMemoryManager.contains_private_content("api_key: example-key-000")

    def test_detects_bearer_token(self):
        assert SharedMemoryManager.contains_private_content("Authorization: Bearer eyJhbGci")

    def test_detects_private_section_header(self):
        text = "## Admin Credentials\npassword=super_secret"
        assert SharedMemoryManager.contains_private_content(text)

    def test_clean_text_not_flagged(self):
        text = "Meeting notes: discussed alarm standardization for BESS sites."
        assert not SharedMemoryManager.contains_private_content(text)

    def test_strip_private_content_redacts_api_key(self):
        raw = "api_key: sk-example-not-real\nSafe content here."
        stripped = SharedMemoryManager._strip_private_content(raw)
        assert "sk-example-not-real" not in stripped
        assert "[REDACTED]" in stripped
        assert "Safe content here" in stripped

    def test_strip_private_section(self):
        raw = "## Overview\nPublic info.\n## Admin\nPassword: secret123\n## Summary\nAll done."
        stripped = SharedMemoryManager._strip_private_content(raw)
        assert "Public info" in stripped
        assert "secret123" not in stripped
        assert "All done" in stripped

    def test_collaborator_gets_filtered_group_memory(self, smm, rbac):
        # Write private-looking content into group memory
        smm.append_to_group_memory("sort", "api_key: sk-super-secret-key", author_id=OWNER_ID)
        merged = smm.get_merged_memory_for_user(USER_A, rbac)
        # Collaborator should not see the raw key
        assert "sk-super-secret-key" not in merged

    def test_owner_gets_unfiltered_group_memory(self, smm, rbac):
        smm.append_to_group_memory("sort", "api_key: sk-super-secret-key", author_id=OWNER_ID)
        merged = smm.get_merged_memory_for_user(OWNER_ID, rbac)
        # Owner gets unfiltered
        assert "sk-super-secret-key" in merged


# ---------------------------------------------------------------------------
# Topic-scoped memory
# ---------------------------------------------------------------------------


class TestTopicScopedMemory:
    def test_topic_scoped_returns_matching_group(self, smm, rbac):
        smm.append_to_group_memory("sort", "Fleet alarm data", author_id=USER_A)
        # "alarms" is a focus topic for fleet-alarms project in sort group
        result = smm.get_topic_scoped_memory(
            USER_A, rbac, query_text="check the alarms for site-42"
        )
        assert "Fleet alarm data" in result

    def test_topic_scoped_excludes_non_matching_project_scoped_group(self, smm, rbac):
        # USER_A is in sort (project_scoped), ask about AWS cost (not a sort topic)
        smm.append_to_group_memory("sort", "SORT info", author_id=USER_A)
        result = smm.get_topic_scoped_memory(USER_A, rbac, query_text="optimize AWS cost spend")
        # sort group's focus topics don't match AWS cost — should be excluded
        assert "SORT info" not in result

    def test_topic_scoped_includes_local_only_group(self, smm, rbac):
        # USER_B is in gsdea (local_only) — local_only groups are always included
        smm.append_to_group_memory("gsdea", "GSDEA note", author_id=USER_B)
        result = smm.get_topic_scoped_memory(USER_B, rbac, query_text="anything unrelated")
        assert "GSDEA note" in result
