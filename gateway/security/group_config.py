# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Group and Project configuration models for v0.9.0 Team Collaboration.

Defines TeamsConfig, GroupConfig, and ProjectConfig Pydantic models.
Provides membership queries, admin checks, and group-override persistence.
"""
from __future__ import annotations

import fcntl
import json
import logging
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, field_validator

logger = logging.getLogger("agentshroud.security.group_config")

_DATA_DIR = Path(os.environ.get("AGENTSHROUD_DATA_DIR", "/app/data"))
_GROUP_OVERRIDES_FILE = _DATA_DIR / "group_overrides.json"


# ---------------------------------------------------------------------------
# Pydantic models
# ---------------------------------------------------------------------------

class ProjectConfig(BaseModel):
    """A project defines a scoped focus area for a team."""

    name: str
    description: str = ""
    focus_topics: List[str] = Field(default_factory=list)
    allowed_tools: List[str] = Field(default_factory=lambda: ["read", "write"])

    @field_validator("focus_topics", mode="before")
    @classmethod
    def normalise_topics(cls, v):
        if isinstance(v, list):
            return [str(t).lower().strip() for t in v if t]
        return v

    def matches_topic(self, text: str) -> bool:
        """Return True if any focus_topic appears in the text (case-insensitive)."""
        ltext = text.lower()
        return any(topic in ltext for topic in self.focus_topics)


class GroupConfig(BaseModel):
    """A team group with members, admin, projects, and collab mode."""

    id: str = ""  # Populated by TeamsConfig.model_post_init
    name: str
    members: List[str] = Field(default_factory=list)
    admin: Optional[str] = None
    projects: List[str] = Field(default_factory=list)
    collab_mode: str = "local_only"  # local_only | project_scoped | full_access
    tool_tier_max: str = "medium"
    # V9-4: Per-group response prefix hook — operators can set a brief context
    # string (e.g. "Team: Ops") that is prepended to collaborator-safe responses
    # for members of this group.  None means no prefix (default behaviour).
    safe_response_prefix: Optional[str] = None

    @field_validator("members", mode="before")
    @classmethod
    def coerce_members(cls, v):
        if isinstance(v, list):
            return [str(m) for m in v]
        return v

    @field_validator("collab_mode")
    @classmethod
    def validate_mode(cls, v):
        valid = {"local_only", "project_scoped", "full_access"}
        if v not in valid:
            raise ValueError(f"collab_mode must be one of {valid}, got: {v!r}")
        return v

    def is_member(self, user_id: str) -> bool:
        return str(user_id) in [str(m) for m in self.members]

    def is_admin(self, user_id: str) -> bool:
        return self.admin is not None and str(user_id) == str(self.admin)


class TeamsConfig(BaseModel):
    """Top-level teams configuration parsed from agentshroud.yaml `teams:` section."""

    groups: Dict[str, GroupConfig] = Field(default_factory=dict)
    projects: Dict[str, ProjectConfig] = Field(default_factory=dict)

    def model_post_init(self, __context) -> None:
        # Back-fill group ids from dict key
        for gid, gcfg in self.groups.items():
            if not gcfg.id:
                gcfg.id = gid
        # Apply persisted group overrides (runtime member additions)
        _apply_persisted_overrides(self)

    # ------------------------------------------------------------------
    # Membership queries
    # ------------------------------------------------------------------

    def get_user_groups(self, user_id: str) -> List[GroupConfig]:
        """Return all groups the user belongs to."""
        uid = str(user_id)
        return [g for g in self.groups.values() if g.is_member(uid)]

    def get_user_projects(self, user_id: str) -> List[ProjectConfig]:
        """Return all projects accessible to the user via group membership."""
        project_ids: set[str] = set()
        for group in self.get_user_groups(user_id):
            project_ids.update(group.projects)
        return [self.projects[pid] for pid in project_ids if pid in self.projects]

    def is_group_admin(self, user_id: str, group_id: str) -> bool:
        group = self.groups.get(group_id)
        if group is None:
            return False
        return group.is_admin(user_id)

    def get_all_member_ids(self) -> List[str]:
        """Return deduplicated list of all user IDs across all groups."""
        seen: set[str] = set()
        result: List[str] = []
        for group in self.groups.values():
            for uid in group.members:
                if uid not in seen:
                    seen.add(uid)
                    result.append(uid)
        return result

    def get_group_admin_ids(self) -> Dict[str, str]:
        """Return mapping of group_id → admin_user_id for all groups that have an admin."""
        return {gid: g.admin for gid, g in self.groups.items() if g.admin}

    def get_active_project_for_user(self, user_id: str) -> Optional[ProjectConfig]:
        """Return the first project accessible to a user (primary project)."""
        projects = self.get_user_projects(user_id)
        return projects[0] if projects else None

    def get_group_safe_response_prefix(self, user_id: str) -> Optional[str]:
        """Return the safe_response_prefix for the first group that the user belongs to
        which has one set.  Returns None if no group defines a prefix (V9-4 hook)."""
        for group in self.groups.values():
            if group.is_member(user_id) and group.safe_response_prefix:
                return group.safe_response_prefix
        return None

    def get_user_collab_mode(self, user_id: str) -> str:
        """Return the most-permissive collab_mode across all user's groups.

        Ordering: full_access > project_scoped > local_only.
        """
        mode_rank = {"local_only": 0, "project_scoped": 1, "full_access": 2}
        groups = self.get_user_groups(user_id)
        if not groups:
            return "local_only"
        best = max(groups, key=lambda g: mode_rank.get(g.collab_mode, 0))
        return best.collab_mode


# ---------------------------------------------------------------------------
# Group-override persistence
# Runtime member additions via /addtogroup are stored here and merged into
# TeamsConfig at startup (or immediately in the same process).
# ---------------------------------------------------------------------------

def _apply_persisted_overrides(teams: TeamsConfig) -> None:
    """Merge group_overrides.json additions into the in-memory TeamsConfig."""
    try:
        if not _GROUP_OVERRIDES_FILE.exists():
            return
        data = json.loads(_GROUP_OVERRIDES_FILE.read_text(encoding="utf-8"))
        for group_id, ops in data.items():
            # Runtime deletions take priority
            if ops.get("_deleted"):
                teams.groups.pop(group_id, None)
                continue
            # Runtime group creations (groups not in static yaml)
            if ops.get("_created") and group_id not in teams.groups:
                try:
                    new_group = GroupConfig(
                        id=group_id,
                        name=ops.get("name", group_id),
                        members=ops.get("members", []),
                        admin=ops.get("admin") or None,
                        collab_mode=ops.get("collab_mode", "local_only"),
                    )
                    teams.groups[group_id] = new_group
                except Exception as e:
                    logger.warning("Could not recreate group '%s' from overrides: %s", group_id, e)
            group = teams.groups.get(group_id)
            if group is None:
                logger.info("group_overrides: unknown group '%s' skipped", group_id)
                continue
            for uid in ops.get("add_members", []):
                if uid not in group.members:
                    group.members.append(uid)
            for uid in ops.get("remove_members", []):
                if uid in group.members:
                    group.members.remove(uid)
            if ops.get("collab_mode"):
                group.collab_mode = ops["collab_mode"]
    except Exception as exc:
        logger.warning("Could not apply group overrides: %s", exc)


def _load_overrides() -> dict:
    try:
        if _GROUP_OVERRIDES_FILE.exists():
            return json.loads(_GROUP_OVERRIDES_FILE.read_text(encoding="utf-8"))
    except Exception:
        pass
    return {}


def _save_overrides(data: dict) -> None:
    _GROUP_OVERRIDES_FILE.parent.mkdir(parents=True, exist_ok=True)
    lock_path = _GROUP_OVERRIDES_FILE.with_suffix(".lock")
    try:
        with open(lock_path, "w") as lf:
            fcntl.flock(lf, fcntl.LOCK_EX)
            try:
                _GROUP_OVERRIDES_FILE.write_text(
                    json.dumps(data, indent=2), encoding="utf-8"
                )
            finally:
                fcntl.flock(lf, fcntl.LOCK_UN)
    except Exception as exc:
        logger.warning("Could not write group overrides: %s", exc)


def persist_group_member_add(group_id: str, user_id: str) -> None:
    """Persist a runtime group membership addition."""
    data = _load_overrides()
    group_data = data.setdefault(group_id, {"add_members": [], "remove_members": []})
    removes = group_data.setdefault("remove_members", [])
    if user_id in removes:
        removes.remove(user_id)
    adds = group_data.setdefault("add_members", [])
    if user_id not in adds:
        adds.append(user_id)
    _save_overrides(data)
    logger.info("Persisted group member add: %s → %s", user_id, group_id)


def persist_group_member_remove(group_id: str, user_id: str) -> None:
    """Persist a runtime group membership removal."""
    data = _load_overrides()
    group_data = data.setdefault(group_id, {"add_members": [], "remove_members": []})
    adds = group_data.setdefault("add_members", [])
    if user_id in adds:
        adds.remove(user_id)
    removes = group_data.setdefault("remove_members", [])
    if user_id not in removes:
        removes.append(user_id)
    _save_overrides(data)
    logger.info("Persisted group member remove: %s from %s", user_id, group_id)


def persist_group_collab_mode(group_id: str, mode: str) -> None:
    """Persist a runtime collab mode change for a group."""
    data = _load_overrides()
    data.setdefault(group_id, {})["collab_mode"] = mode
    _save_overrides(data)
    logger.info("Persisted group collab_mode: %s → %s", group_id, mode)


def persist_group_create(
    group_id: str,
    name: str,
    collab_mode: str,
    members: List[str],
    admin: Optional[str],
) -> None:
    """Persist a runtime group creation so it survives container restarts."""
    data = _load_overrides()
    data[group_id] = {
        "_created": True,
        "name": name,
        "collab_mode": collab_mode,
        "members": members or [],
        "admin": admin,
        "add_members": [],
        "remove_members": [],
    }
    _save_overrides(data)
    logger.info("Persisted group create: %s (%s)", group_id, name)


def persist_group_delete(group_id: str) -> None:
    """Persist a runtime group deletion so it survives container restarts."""
    data = _load_overrides()
    data[group_id] = {"_deleted": True}
    _save_overrides(data)
    logger.info("Persisted group delete: %s", group_id)
