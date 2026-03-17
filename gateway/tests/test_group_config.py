# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for group_config.py — V9-4A: TeamsConfig, GroupConfig, ProjectConfig."""

from __future__ import annotations

import pytest
from gateway.security.group_config import (
    GroupConfig,
    ProjectConfig,
    TeamsConfig,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

TEAMS_RAW = {
    "groups": {
        "sort": {
            "name": "SysOps Reliability Team",
            "members": ["8279589982", "8526379012"],
            "admin": "8279589982",
            "projects": ["fleet-alarms"],
            "collab_mode": "project_scoped",
        },
        "gsdea": {
            "name": "Digital Enablement",
            "members": ["8506022825", "8545356403"],
            "admin": "8506022825",
            "projects": ["aws-finops"],
            "collab_mode": "project_scoped",
        },
        "gsde": {
            "name": "Data Engineering",
            "members": ["15712621992", "8633775668"],
            "admin": "15712621992",
            "projects": ["fodl"],
            "collab_mode": "local_only",
        },
    },
    "projects": {
        "fleet-alarms": {
            "name": "Fleet Alarm Standardization",
            "description": "200+ BESS sites",
            "focus_topics": ["alarms", "monitoring", "bess"],
            "allowed_tools": ["read", "write"],
        },
        "aws-finops": {
            "name": "AWS Cost Optimization",
            "description": "40% reduction FY26",
            "focus_topics": ["aws", "cost", "ec2"],
            "allowed_tools": ["read"],
        },
        "fodl": {
            "name": "Fluence Online Data Lakehouse",
            "description": "275TB platform",
            "focus_topics": ["parquet", "athena"],
            "allowed_tools": ["read", "write", "edit"],
        },
    },
}


@pytest.fixture
def teams() -> TeamsConfig:
    return TeamsConfig(**TEAMS_RAW)


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

class TestTeamsConfigParsing:
    def test_parses_groups(self, teams):
        assert len(teams.groups) == 3
        assert "sort" in teams.groups
        assert teams.groups["sort"].name == "SysOps Reliability Team"

    def test_parses_projects(self, teams):
        assert len(teams.projects) == 3
        assert "fleet-alarms" in teams.projects
        assert teams.projects["fleet-alarms"].focus_topics == ["alarms", "monitoring", "bess"]

    def test_empty_teams_parses(self):
        t = TeamsConfig()
        assert t.groups == {}
        assert t.projects == {}


# ---------------------------------------------------------------------------
# Membership queries
# ---------------------------------------------------------------------------

class TestMembershipQueries:
    def test_get_user_groups_member(self, teams):
        groups = teams.get_user_groups("8279589982")
        assert any(g.name == "SysOps Reliability Team" for g in groups)

    def test_get_user_groups_non_member(self, teams):
        groups = teams.get_user_groups("9999999999")
        assert groups == []

    def test_get_user_groups_multi_group(self, teams):
        # Add a user to two groups
        teams.groups["sort"].members.append("8506022825")
        groups = teams.get_user_groups("8506022825")
        group_names = [g.name for g in groups]
        assert "SysOps Reliability Team" in group_names
        assert "Digital Enablement" in group_names

    def test_get_all_member_ids(self, teams):
        ids = teams.get_all_member_ids()
        assert "8279589982" in ids
        assert "8633775668" in ids
        # No duplicates
        assert len(ids) == len(set(ids))


# ---------------------------------------------------------------------------
# Admin checks
# ---------------------------------------------------------------------------

class TestAdminChecks:
    def test_is_group_admin_correct(self, teams):
        assert teams.is_group_admin("8279589982", "sort") is True

    def test_is_group_admin_wrong_user(self, teams):
        assert teams.is_group_admin("8526379012", "sort") is False

    def test_is_group_admin_unknown_group(self, teams):
        assert teams.is_group_admin("8279589982", "nonexistent") is False


# ---------------------------------------------------------------------------
# Project queries
# ---------------------------------------------------------------------------

class TestProjectQueries:
    def test_get_user_projects_member(self, teams):
        projs = teams.get_user_projects("8279589982")
        assert any(p.name == "Fleet Alarm Standardization" for p in projs)

    def test_get_user_projects_non_member(self, teams):
        projs = teams.get_user_projects("9999999999")
        assert projs == []

    def test_no_duplicate_projects(self, teams):
        # User in two groups sharing a project
        teams.groups["gsdea"].projects.append("fleet-alarms")
        teams.groups["gsdea"].members.append("8279589982")
        projs = teams.get_user_projects("8279589982")
        names = [p.name for p in projs]
        assert names.count("Fleet Alarm Standardization") == 1


# ---------------------------------------------------------------------------
# Collab mode resolution
# ---------------------------------------------------------------------------

class TestCollabMode:
    def test_project_scoped_mode(self, teams):
        assert teams.get_user_collab_mode("8279589982") == "project_scoped"

    def test_local_only_mode(self, teams):
        assert teams.get_user_collab_mode("15712621992") == "local_only"

    def test_unknown_user_returns_local_only(self, teams):
        # Unknown users have no groups — default falls back to "local_only"
        assert teams.get_user_collab_mode("9999999999") == "local_only"
