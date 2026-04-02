# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Shared collaborator response templates for Telegram and Slack proxies.

Centralises all user-facing message strings and formatters so they stay
consistent across channels without duplication.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..security.group_config import GroupConfig, ProjectConfig, TeamsConfig


# ---------------------------------------------------------------------------
# Status / info templates
# ---------------------------------------------------------------------------

COLLAB_UNAVAILABLE = "I'm not available right now. Please try again shortly."

COLLAB_OUTSIDE_SCOPE = (
    "That request falls outside the current project scope. "
    "I can only assist with topics related to your assigned project. "
    "Contact the workspace owner if you need broader access."
)

COLLAB_NO_GROUPS = (
    "You are not assigned to any team groups. "
    "Contact the workspace owner to be added to a group."
)

COLLAB_NO_PROJECTS = (
    "No projects are currently active for your groups. "
    "Contact the workspace owner to assign a project."
)


# ---------------------------------------------------------------------------
# Group/project formatters
# ---------------------------------------------------------------------------


def format_groups_list(user_id: str, teams: "TeamsConfig") -> str:
    """Format a user's group memberships for display."""
    groups = teams.get_user_groups(user_id)
    if not groups:
        return COLLAB_NO_GROUPS

    lines = ["Your team groups:"]
    for g in groups:
        admin_note = " (you are admin)" if g.is_admin(user_id) else ""
        project_names = []
        for pid in g.projects:
            proj = teams.projects.get(pid)
            if proj:
                project_names.append(proj.name)
        proj_text = ", ".join(project_names) if project_names else "none"
        lines.append(
            f"  \u2022 {g.name} [{g.id}]{admin_note}\n"
            f"    Mode: {g.collab_mode} | Projects: {proj_text}"
        )
    return "\n".join(lines)


def format_group_info(group: "GroupConfig", teams: "TeamsConfig", user_id: str) -> str:
    """Format detailed info for a single group."""
    project_names = []
    for pid in group.projects:
        proj = teams.projects.get(pid)
        if proj:
            project_names.append(f"{proj.name} ({pid})")

    lines = [
        f"Group: {group.name} [{group.id}]",
        f"Mode: {group.collab_mode}",
        f"Members: {len(group.members)}",
        f"Admin: {group.admin or 'none'}",
        f"Projects: {', '.join(project_names) or 'none'}",
    ]
    return "\n".join(lines)


def format_projects_list(user_id: str, teams: "TeamsConfig") -> str:
    """Format a user's accessible projects for display."""
    projects = teams.get_user_projects(user_id)
    if not projects:
        return COLLAB_NO_PROJECTS

    lines = ["Your accessible projects:"]
    for p in projects:
        topic_preview = ", ".join(p.focus_topics[:5])
        lines.append(f"  \u2022 {p.name}\n" f"    Topics: {topic_preview}")
    return "\n".join(lines)


def format_addtogroup_success(user_id: str, group_id: str) -> str:
    return f"User {user_id} added to group '{group_id}'."


def format_rmfromgroup_success(user_id: str, group_id: str) -> str:
    return f"User {user_id} removed from group '{group_id}'."


def format_setmode_success(target: str, mode: str) -> str:
    return f"Collab mode for '{target}' set to '{mode}'."


def format_unknown_group(group_id: str) -> str:
    return f"Unknown group: '{group_id}'. Use /groups to see available groups."


def format_not_member(user_id: str, group_id: str) -> str:
    return f"User {user_id} is not a member of group '{group_id}'."


def format_already_member(user_id: str, group_id: str) -> str:
    return f"User {user_id} is already a member of group '{group_id}'."


def format_no_permission(action: str) -> str:
    return f"You do not have permission to {action}."


# ---------------------------------------------------------------------------
# Project context injection string (prepended to bot context)
# ---------------------------------------------------------------------------


def build_project_context_injection(group_name: str, project: "ProjectConfig") -> str:
    """Build the system-prompt injection for project_scoped mode."""
    topics = ", ".join(project.focus_topics) if project.focus_topics else "general"
    tools = ", ".join(project.allowed_tools) if project.allowed_tools else "read, write"
    return (
        f"[PROJECT CONTEXT] You are assisting a member of {group_name} "
        f"on project {project.name}.\n"
        f"Focus: {topics}. Allowed tools: {tools}.\n"
        f"Only assist with queries related to the above. "
        f"For out-of-scope requests, respond: "
        f'"This falls outside the current project scope."'
    )
