# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for gateway/security/delegation.py — V9-T1: Owner-away privilege delegation."""

from __future__ import annotations

import time

import pytest

from gateway.security.delegation import (
    Delegation,
    DelegationError,
    DelegationManager,
    DelegationPrivilege,
)

OWNER = "owner-001"
USER_A = "user-a-001"
USER_B = "user-b-002"
RANDO = "rando-999"


@pytest.fixture
def mgr() -> DelegationManager:
    """In-memory delegation manager (no disk I/O)."""
    return DelegationManager(owner_user_id=OWNER, persist=False)


# ---------------------------------------------------------------------------
# Basic delegation lifecycle
# ---------------------------------------------------------------------------


class TestDelegateBasic:
    def test_create_egress_delegation(self, mgr):
        d = mgr.delegate(OWNER, USER_A, DelegationPrivilege.EGRESS_APPROVAL, duration_hours=2)
        assert d.delegated_by == OWNER
        assert d.delegated_to == USER_A
        assert d.privilege == DelegationPrivilege.EGRESS_APPROVAL.value
        assert d.is_active

    def test_create_user_management_delegation(self, mgr):
        d = mgr.delegate(OWNER, USER_A, DelegationPrivilege.USER_MANAGEMENT, duration_hours=4)
        assert d.privilege == DelegationPrivilege.USER_MANAGEMENT.value
        assert d.is_active

    def test_delegation_has_unique_id(self, mgr):
        d1 = mgr.delegate(OWNER, USER_A, DelegationPrivilege.EGRESS_APPROVAL, 1)
        d2 = mgr.delegate(OWNER, USER_B, DelegationPrivilege.EGRESS_APPROVAL, 1)
        assert d1.id != d2.id

    def test_delegation_expires_correctly(self, mgr):
        d = mgr.delegate(OWNER, USER_A, DelegationPrivilege.EGRESS_APPROVAL, duration_hours=1)
        # Artificially expire it
        d.expires_at = time.time() - 1
        assert not d.is_active


# ---------------------------------------------------------------------------
# is_delegated
# ---------------------------------------------------------------------------


class TestIsDelegated:
    def test_is_delegated_returns_true_for_active(self, mgr):
        mgr.delegate(OWNER, USER_A, DelegationPrivilege.EGRESS_APPROVAL, 2)
        assert mgr.is_delegated(USER_A, DelegationPrivilege.EGRESS_APPROVAL)

    def test_is_delegated_returns_false_for_other_user(self, mgr):
        mgr.delegate(OWNER, USER_A, DelegationPrivilege.EGRESS_APPROVAL, 2)
        assert not mgr.is_delegated(USER_B, DelegationPrivilege.EGRESS_APPROVAL)

    def test_is_delegated_returns_false_for_other_privilege(self, mgr):
        mgr.delegate(OWNER, USER_A, DelegationPrivilege.EGRESS_APPROVAL, 2)
        assert not mgr.is_delegated(USER_A, DelegationPrivilege.USER_MANAGEMENT)

    def test_is_delegated_returns_false_after_expiry(self, mgr):
        d = mgr.delegate(OWNER, USER_A, DelegationPrivilege.EGRESS_APPROVAL, 1)
        d.expires_at = time.time() - 1
        assert not mgr.is_delegated(USER_A, DelegationPrivilege.EGRESS_APPROVAL)


# ---------------------------------------------------------------------------
# Revoke
# ---------------------------------------------------------------------------


class TestRevoke:
    def test_revoke_removes_delegation(self, mgr):
        mgr.delegate(OWNER, USER_A, DelegationPrivilege.EGRESS_APPROVAL, 2)
        result = mgr.revoke(OWNER, USER_A, DelegationPrivilege.EGRESS_APPROVAL)
        assert result is True
        assert not mgr.is_delegated(USER_A, DelegationPrivilege.EGRESS_APPROVAL)

    def test_revoke_returns_false_when_nothing_to_revoke(self, mgr):
        result = mgr.revoke(OWNER, USER_A, DelegationPrivilege.EGRESS_APPROVAL)
        assert result is False

    def test_revoke_all_for_user(self, mgr):
        mgr.delegate(OWNER, USER_A, DelegationPrivilege.EGRESS_APPROVAL, 2)
        mgr.delegate(OWNER, USER_A, DelegationPrivilege.USER_MANAGEMENT, 2)
        count = mgr.revoke_all_for_user(OWNER, USER_A)
        assert count == 2
        assert not mgr.is_delegated(USER_A, DelegationPrivilege.EGRESS_APPROVAL)
        assert not mgr.is_delegated(USER_A, DelegationPrivilege.USER_MANAGEMENT)


# ---------------------------------------------------------------------------
# Access control
# ---------------------------------------------------------------------------


class TestAccessControl:
    def test_non_owner_cannot_delegate(self, mgr):
        with pytest.raises(DelegationError, match="owner"):
            mgr.delegate(RANDO, USER_A, DelegationPrivilege.EGRESS_APPROVAL, 1)

    def test_non_owner_cannot_revoke(self, mgr):
        mgr.delegate(OWNER, USER_A, DelegationPrivilege.EGRESS_APPROVAL, 1)
        with pytest.raises(DelegationError, match="owner"):
            mgr.revoke(RANDO, USER_A, DelegationPrivilege.EGRESS_APPROVAL)

    def test_owner_cannot_self_delegate(self, mgr):
        with pytest.raises(DelegationError, match="themselves"):
            mgr.delegate(OWNER, OWNER, DelegationPrivilege.EGRESS_APPROVAL, 1)

    def test_duration_zero_rejected(self, mgr):
        with pytest.raises(DelegationError):
            mgr.delegate(OWNER, USER_A, DelegationPrivilege.EGRESS_APPROVAL, 0)

    def test_duration_over_max_rejected(self, mgr):
        with pytest.raises(DelegationError):
            mgr.delegate(OWNER, USER_A, DelegationPrivilege.EGRESS_APPROVAL, 999)


# ---------------------------------------------------------------------------
# Re-delegation (idempotent override)
# ---------------------------------------------------------------------------


class TestRedelegation:
    def test_redelegate_replaces_existing(self, mgr):
        d1 = mgr.delegate(OWNER, USER_A, DelegationPrivilege.EGRESS_APPROVAL, 1)
        d2 = mgr.delegate(OWNER, USER_A, DelegationPrivilege.EGRESS_APPROVAL, 4)
        # Old delegation ID should be gone; new one present
        assert mgr.is_delegated(USER_A, DelegationPrivilege.EGRESS_APPROVAL)
        active = mgr.get_active_delegations()
        ids = [d.id for d in active]
        assert d1.id not in ids
        assert d2.id in ids


# ---------------------------------------------------------------------------
# List and cleanup
# ---------------------------------------------------------------------------


class TestListAndCleanup:
    def test_get_active_delegations_excludes_expired(self, mgr):
        mgr.delegate(OWNER, USER_A, DelegationPrivilege.EGRESS_APPROVAL, 1)
        d_expired = mgr.delegate(OWNER, USER_B, DelegationPrivilege.USER_MANAGEMENT, 1)
        d_expired.expires_at = time.time() - 1
        active = mgr.get_active_delegations()
        user_ids = [d.delegated_to for d in active]
        assert USER_A in user_ids
        assert USER_B not in user_ids

    def test_cleanup_expired_removes_and_returns_count(self, mgr):
        d = mgr.delegate(OWNER, USER_A, DelegationPrivilege.EGRESS_APPROVAL, 1)
        d.expires_at = time.time() - 1
        count = mgr.cleanup_expired()
        assert count == 1
        assert len(mgr.get_active_delegations()) == 0

    def test_get_delegations_for_user(self, mgr):
        mgr.delegate(OWNER, USER_A, DelegationPrivilege.EGRESS_APPROVAL, 1)
        mgr.delegate(OWNER, USER_A, DelegationPrivilege.USER_MANAGEMENT, 2)
        mgr.delegate(OWNER, USER_B, DelegationPrivilege.EGRESS_APPROVAL, 1)
        user_a_delegs = mgr.get_delegations_for_user(USER_A)
        assert len(user_a_delegs) == 2
        assert all(d.delegated_to == USER_A for d in user_a_delegs)

    def test_no_active_delegations_initially(self, mgr):
        assert mgr.get_active_delegations() == []


# ---------------------------------------------------------------------------
# Serialization round-trip
# ---------------------------------------------------------------------------


class TestSerialization:
    def test_delegation_to_dict_and_back(self, mgr):
        d = mgr.delegate(OWNER, USER_A, DelegationPrivilege.EGRESS_APPROVAL, 3)
        d_dict = d.to_dict()
        d2 = Delegation.from_dict(d_dict)
        assert d2.id == d.id
        assert d2.delegated_to == USER_A
        assert d2.privilege == DelegationPrivilege.EGRESS_APPROVAL.value
        assert abs(d2.expires_at - d.expires_at) < 0.01
