# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""SOC Contributor Manager — wraps RBACConfig + TeamsConfig → ContributorRecord."""
from __future__ import annotations

import logging
from typing import Dict, List, Optional

from .models import ContributorRecord, Platform, UserRole

logger = logging.getLogger("agentshroud.soc.contributors")


def _role_enum(rbac_role_value: str) -> UserRole:
    mapping = {
        "owner": UserRole.OWNER,
        "admin": UserRole.ADMIN,
        "collaborator": UserRole.COLLABORATOR,
        "viewer": UserRole.VIEWER,
    }
    return mapping.get(str(rbac_role_value).lower(), UserRole.VIEWER)


class ContributorManager:
    """Builds ContributorRecord instances from RBACConfig + TeamsConfig."""

    def __init__(self, rbac_config=None, teams_config=None, activity_tracker=None):
        self._rbac = rbac_config
        self._teams = teams_config
        self._tracker = activity_tracker

    def _ensure_rbac(self):
        if self._rbac is None:
            from ..security.rbac_config import RBACConfig
            self._rbac = RBACConfig()
        return self._rbac

    def _ensure_teams(self):
        if self._teams is not None:
            return self._teams
        # Try to get from app_state
        try:
            from ..ingest_api.state import app_state
            cfg = getattr(app_state, "config", None)
            if cfg:
                return getattr(cfg, "teams", None)
        except Exception:
            pass
        return None

    def list_contributors(self) -> List[ContributorRecord]:
        rbac = self._ensure_rbac()
        teams = self._ensure_teams()
        records: List[ContributorRecord] = []
        # Gather activity summary for enrichment
        activity_by_user: Dict[str, dict] = {}
        if self._tracker:
            try:
                summary = self._tracker.get_activity_summary()
                activity_by_user = summary.get("by_user", {})
            except Exception:
                pass

        for uid, role in rbac.user_roles.items():
            records.append(self._build_record(uid, role.value, teams, activity_by_user))
        return records

    def get_contributor(self, user_id: str) -> Optional[ContributorRecord]:
        rbac = self._ensure_rbac()
        teams = self._ensure_teams()
        role = rbac.get_user_role(user_id)
        activity_by_user: Dict[str, dict] = {}
        if self._tracker:
            try:
                summary = self._tracker.get_activity_summary()
                activity_by_user = summary.get("by_user", {})
            except Exception:
                pass
        return self._build_record(user_id, role.value, teams, activity_by_user)

    def _build_record(
        self,
        user_id: str,
        role_value: str,
        teams,
        activity_by_user: Dict[str, dict],
    ) -> ContributorRecord:
        # Groups
        groups: List[str] = []
        projects: List[str] = []
        collab_mode = "local_only"
        if teams:
            try:
                user_groups = teams.get_user_groups(user_id)
                groups = [g.id for g in user_groups]
                user_projects = teams.get_user_projects(user_id)
                projects = [
                    pid
                    for g in user_groups
                    for pid in g.projects
                ]
                collab_mode = teams.get_user_collab_mode(user_id)
            except Exception:
                pass

        # Activity
        activity = activity_by_user.get(user_id, {})
        last_active = None
        total_messages = 0
        display_name = activity.get("username", "")
        if activity:
            ts = activity.get("last_active")
            if ts:
                try:
                    from datetime import datetime, timezone
                    last_active = datetime.fromtimestamp(float(ts), tz=timezone.utc).isoformat()
                except Exception:
                    pass
            total_messages = activity.get("message_count", 0)

        # Lockdown state
        lockdown_level = "normal"
        immunity_active = False
        immunity_expires = None
        try:
            from ..ingest_api.state import app_state
            lockdown = getattr(app_state, "_lockdown", None) or getattr(
                getattr(app_state, "telegram_proxy", None), "_lockdown", None
            )
            if lockdown:
                level = lockdown.get_level(user_id)
                lockdown_level = str(level).lower() if level else "normal"
        except Exception:
            pass

        return ContributorRecord(
            user_id=user_id,
            platform=Platform.TELEGRAM,
            display_name=display_name or user_id,
            role=_role_enum(role_value),
            groups=groups,
            projects=list(set(projects)),
            collab_mode=collab_mode,
            last_active=last_active,
            total_messages=total_messages,
            lockdown_level=lockdown_level,
            immunity_active=immunity_active,
            immunity_expires=immunity_expires,
        )
