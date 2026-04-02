# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for gateway/proxy/collaborator_responses.py — response template formatters."""

from __future__ import annotations

import pytest

from gateway.proxy.collaborator_responses import (
    COLLAB_NO_GROUPS,
    COLLAB_NO_PROJECTS,
    COLLAB_OUTSIDE_SCOPE,
    COLLAB_UNAVAILABLE,
    build_project_context_injection,
    format_addtogroup_success,
    format_already_member,
    format_group_info,
    format_groups_list,
    format_no_permission,
    format_not_member,
    format_projects_list,
    format_rmfromgroup_success,
    format_setmode_success,
    format_unknown_group,
)
from gateway.security.group_config import GroupConfig, ProjectConfig, TeamsConfig


@pytest.fixture
def teams():
    return TeamsConfig(
        groups={
            "sort": GroupConfig(
                name="SysOps Reliability Team",
                members=["8279589982", "8526379012"],
                admin="8279589982",
                projects=["fleet-alarms"],
                collab_mode="project_scoped",
            )
        },
        projects={
            "fleet-alarms": ProjectConfig(
                name="Fleet Alarm Standardization",
                focus_topics=["alarms", "bess"],
                allowed_tools=["read"],
            )
        },
    )


@pytest.fixture
def project():
    return ProjectConfig(
        name="Fleet Alarm Standardization",
        description="200+ BESS sites",
        focus_topics=["alarms", "bess"],
        allowed_tools=["read", "write"],
    )


class TestConstantMessages:
    def test_collab_unavailable_not_empty(self):
        assert COLLAB_UNAVAILABLE
        assert len(COLLAB_UNAVAILABLE) > 0

    def test_collab_outside_scope_not_empty(self):
        assert COLLAB_OUTSIDE_SCOPE

    def test_no_groups_not_empty(self):
        assert COLLAB_NO_GROUPS

    def test_no_projects_not_empty(self):
        assert COLLAB_NO_PROJECTS


class TestFormatGroupsList:
    def test_member_sees_group(self, teams):
        result = format_groups_list("8279589982", teams)
        assert "SysOps Reliability Team" in result
        assert "sort" in result

    def test_no_groups_for_unknown_user(self, teams):
        result = format_groups_list("9999999999", teams)
        assert COLLAB_NO_GROUPS in result


class TestFormatGroupInfo:
    def test_shows_admin(self, teams):
        result = format_group_info(teams.groups["sort"], teams, "8279589982")
        assert "8279589982" in result
        assert "project_scoped" in result

    def test_shows_projects(self, teams):
        result = format_group_info(teams.groups["sort"], teams, "8279589982")
        assert "fleet-alarms" in result


class TestFormatProjectsList:
    def test_member_sees_project(self, teams):
        result = format_projects_list("8279589982", teams)
        assert "Fleet Alarm Standardization" in result

    def test_no_projects_for_unknown_user(self, teams):
        result = format_projects_list("9999999999", teams)
        assert COLLAB_NO_PROJECTS in result


class TestMutationFormatters:
    def test_addtogroup_success(self):
        result = format_addtogroup_success("8633775668", "gsde")
        assert "8633775668" in result
        assert "gsde" in result

    def test_rmfromgroup_success(self):
        result = format_rmfromgroup_success("8633775668", "gsde")
        assert "8633775668" in result

    def test_setmode_success_group(self):
        result = format_setmode_success("sort", "project_scoped")
        assert "project_scoped" in result
        assert "sort" in result

    def test_setmode_success_user(self):
        result = format_setmode_success("8279589982", "full_access")
        assert "full_access" in result


class TestErrorFormatters:
    def test_unknown_group(self):
        result = format_unknown_group("nonexistent")
        assert "nonexistent" in result

    def test_not_member(self):
        result = format_not_member("uid-123", "secret-group")
        assert "secret-group" in result

    def test_already_member(self):
        result = format_already_member("uid-123", "group-x")
        assert "uid-123" in result

    def test_no_permission(self):
        result = format_no_permission("manage")
        assert "manage" in result


class TestBuildProjectContextInjection:
    def test_contains_group_and_project(self, project):
        result = build_project_context_injection("SORT", project)
        assert "SORT" in result
        assert "Fleet Alarm Standardization" in result
        assert "alarms" in result

    def test_contains_allowed_tools(self, project):
        result = build_project_context_injection("SORT", project)
        assert "read" in result
