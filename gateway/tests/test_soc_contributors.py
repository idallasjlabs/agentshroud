# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for gateway/soc/contributors.py — ContributorManager record building.

No dedicated test file previously existed for this module (router tests fully
mock ContributorManager out), so real _build_record() behavior — including
Bug 2 (lockdown_level always "normal" because contributors.py called the
nonexistent ProgressiveLockdown.get_level()) and the new `paused` field — was
untested. Covers both here.
"""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import patch

from gateway.security.progressive_lockdown import ProgressiveLockdown
from gateway.security.rbac_config import Role
from gateway.soc.contributors import ContributorManager


class _FakeRBAC:
    def __init__(self, user_roles):
        self.user_roles = user_roles

    def get_user_role(self, user_id):
        return self.user_roles.get(user_id, Role.VIEWER)


class TestLockdownLevelWiring:
    """Bug 2: contributors.py must call get_status(), not the nonexistent get_level()."""

    def test_build_record_reports_real_lockdown_level(self):
        lockdown = ProgressiveLockdown()
        for _ in range(5):
            lockdown.record_block(user_id="u1", reason="test")

        mgr = ContributorManager(rbac_config=_FakeRBAC({"u1": Role.COLLABORATOR}))
        fake_state = SimpleNamespace(_lockdown=lockdown, telegram_proxy=None)
        with patch("gateway.ingest_api.state.app_state", fake_state):
            rec = mgr.get_contributor("u1")

        assert rec.lockdown_level == "escalated"

    def test_build_record_reports_suspended_level(self):
        lockdown = ProgressiveLockdown()
        for _ in range(10):
            lockdown.record_block(user_id="u9", reason="test")

        mgr = ContributorManager(rbac_config=_FakeRBAC({"u9": Role.COLLABORATOR}))
        fake_state = SimpleNamespace(_lockdown=lockdown, telegram_proxy=None)
        with patch("gateway.ingest_api.state.app_state", fake_state):
            rec = mgr.get_contributor("u9")

        assert rec.lockdown_level == "suspended"

    def test_build_record_defaults_to_normal_when_no_lockdown_state(self):
        lockdown = ProgressiveLockdown()
        mgr = ContributorManager(rbac_config=_FakeRBAC({"u2": Role.COLLABORATOR}))
        fake_state = SimpleNamespace(_lockdown=lockdown, telegram_proxy=None)
        with patch("gateway.ingest_api.state.app_state", fake_state):
            rec = mgr.get_contributor("u2")

        assert rec.lockdown_level == "normal"

    def test_build_record_does_not_crash_if_lockdown_missing(self):
        mgr = ContributorManager(rbac_config=_FakeRBAC({"u3": Role.COLLABORATOR}))
        fake_state = SimpleNamespace(_lockdown=None, telegram_proxy=None)
        with patch("gateway.ingest_api.state.app_state", fake_state):
            rec = mgr.get_contributor("u3")

        assert rec.lockdown_level == "normal"


class TestPausedFieldWiring:
    """paused feature: ContributorRecord.paused reflects the persisted paused set."""

    def test_paused_user_reports_paused_true(self, tmp_path, monkeypatch):
        import gateway.security.rbac_config as rc

        monkeypatch.setattr(
            rc, "_APPROVED_COLLABORATORS_FILE", tmp_path / "approved_collaborators.json"
        )
        rc.pause_collaborator("u4")

        mgr = ContributorManager(rbac_config=_FakeRBAC({"u4": Role.COLLABORATOR}))
        rec = mgr.get_contributor("u4")
        assert rec.paused is True

    def test_non_paused_user_reports_paused_false(self, tmp_path, monkeypatch):
        import gateway.security.rbac_config as rc

        monkeypatch.setattr(
            rc, "_APPROVED_COLLABORATORS_FILE", tmp_path / "approved_collaborators.json"
        )

        mgr = ContributorManager(rbac_config=_FakeRBAC({"u5": Role.COLLABORATOR}))
        rec = mgr.get_contributor("u5")
        assert rec.paused is False

    def test_list_contributors_populates_paused_per_user(self, tmp_path, monkeypatch):
        import gateway.security.rbac_config as rc

        monkeypatch.setattr(
            rc, "_APPROVED_COLLABORATORS_FILE", tmp_path / "approved_collaborators.json"
        )
        rc.pause_collaborator("u6")

        mgr = ContributorManager(
            rbac_config=_FakeRBAC({"u6": Role.COLLABORATOR, "u7": Role.COLLABORATOR})
        )
        records = {r.user_id: r for r in mgr.list_contributors()}
        assert records["u6"].paused is True
        assert records["u7"].paused is False

    def test_paused_is_independent_of_lockdown_level(self, tmp_path, monkeypatch):
        """Constraint check: paused (owner-initiated) and lockdown_level
        (auto-escalation) must not be conflated."""
        import gateway.security.rbac_config as rc

        monkeypatch.setattr(
            rc, "_APPROVED_COLLABORATORS_FILE", tmp_path / "approved_collaborators.json"
        )
        rc.pause_collaborator("u8")

        mgr = ContributorManager(rbac_config=_FakeRBAC({"u8": Role.COLLABORATOR}))
        fake_state = SimpleNamespace(_lockdown=ProgressiveLockdown(), telegram_proxy=None)
        with patch("gateway.ingest_api.state.app_state", fake_state):
            rec = mgr.get_contributor("u8")

        assert rec.paused is True
        assert rec.lockdown_level == "normal"

    def test_load_paused_ids_defaults_to_empty_set_on_error(self):
        """_load_paused_ids must never crash record-building if the persisted
        store is unreadable — degrade to 'nobody paused' instead."""
        with patch(
            "gateway.security.rbac_config.load_paused_collaborator_ids",
            side_effect=OSError("disk error"),
        ):
            assert ContributorManager._load_paused_ids() == set()
