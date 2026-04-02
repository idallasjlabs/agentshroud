# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for gateway/security/privacy_policy.py — V9-T2: Privacy policy enforcement."""

from __future__ import annotations

import pytest

from gateway.security.group_config import TeamsConfig
from gateway.security.privacy_policy import (
    PrivacyPolicy,
    PrivacyPolicyEnforcer,
    ServicePolicy,
    ServicePrivacy,
)
from gateway.security.rbac_config import RBACConfig, Role

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

OWNER_ID = "owner-001"
ADMIN_ID = "admin-002"
COLLAB_ID = "collab-003"
GROUP_MEMBER_ID = "ops-member-007"


def _make_rbac(extra_groups: dict = None) -> RBACConfig:
    teams_groups = {
        "ops": {
            "name": "OPS Team",
            "members": [GROUP_MEMBER_ID],
            "admin": GROUP_MEMBER_ID,
            "projects": [],
            "collab_mode": "local_only",
        }
    }
    if extra_groups:
        teams_groups.update(extra_groups)
    teams = TeamsConfig(groups=teams_groups)
    cfg = RBACConfig(owner_user_id=OWNER_ID, collaborator_user_ids=[COLLAB_ID, GROUP_MEMBER_ID])
    cfg.user_roles[ADMIN_ID] = Role.ADMIN
    cfg.wire_teams_config(teams)
    return cfg


@pytest.fixture
def rbac():
    return _make_rbac()


@pytest.fixture
def default_policy():
    return PrivacyPolicy.default()


@pytest.fixture
def enforcer(rbac, default_policy):
    return PrivacyPolicyEnforcer(policy=default_policy, rbac_config=rbac)


# ---------------------------------------------------------------------------
# PrivacyPolicy.from_dict
# ---------------------------------------------------------------------------


class TestPrivacyPolicyParsing:
    def test_default_policy_marks_gmail_private(self, default_policy):
        svc = default_policy.services.get("gmail")
        assert svc is not None
        assert svc.privacy == ServicePrivacy.PRIVATE

    def test_from_dict_overrides_existing(self):
        policy = PrivacyPolicy.from_dict(
            {
                "services": {
                    "gmail": {"privacy": "shared"},
                }
            }
        )
        assert policy.services["gmail"].privacy == ServicePrivacy.SHARED

    def test_from_dict_adds_new_service(self):
        policy = PrivacyPolicy.from_dict(
            {
                "services": {
                    "jira": {"privacy": "shared"},
                    "private_db": {"privacy": "group_only", "allowed_groups": ["ops"]},
                }
            }
        )
        assert policy.services["jira"].privacy == ServicePrivacy.SHARED
        assert policy.services["private_db"].privacy == ServicePrivacy.GROUP_ONLY
        assert policy.services["private_db"].allowed_groups == ["ops"]

    def test_from_dict_unknown_privacy_defaults_to_private(self):
        policy = PrivacyPolicy.from_dict(
            {"services": {"weird_svc": {"privacy": "undefined_value"}}}
        )
        assert policy.services["weird_svc"].privacy == ServicePrivacy.PRIVATE

    def test_extra_redact_patterns_loaded(self):
        policy = PrivacyPolicy.from_dict({"extra_redact_patterns": [r"\bSECRET-\w+\b"]})
        assert len(policy.extra_redact_patterns) == 1


# ---------------------------------------------------------------------------
# Service access control — is_service_allowed
# ---------------------------------------------------------------------------


class TestServiceAccessControl:
    def test_owner_can_access_private_service(self, enforcer):
        assert enforcer.is_service_allowed(OWNER_ID, "gmail")

    def test_collaborator_blocked_from_private_service(self, enforcer):
        assert not enforcer.is_service_allowed(COLLAB_ID, "gmail")

    def test_admin_blocked_from_private_service(self, enforcer):
        assert not enforcer.is_service_allowed(ADMIN_ID, "gmail")

    def test_collaborator_allowed_shared_service(self):
        policy = PrivacyPolicy.from_dict({"services": {"jira": {"privacy": "shared"}}})
        rbac = _make_rbac()
        enforcer = PrivacyPolicyEnforcer(policy=policy, rbac_config=rbac)
        assert enforcer.is_service_allowed(COLLAB_ID, "jira")

    def test_group_member_allowed_group_only_service(self):
        policy = PrivacyPolicy.from_dict(
            {"services": {"monitoring_ops": {"privacy": "group_only", "allowed_groups": ["ops"]}}}
        )
        rbac = _make_rbac()
        enforcer = PrivacyPolicyEnforcer(policy=policy, rbac_config=rbac)
        assert enforcer.is_service_allowed(GROUP_MEMBER_ID, "monitoring_ops")

    def test_non_group_member_blocked_from_group_only_service(self):
        policy = PrivacyPolicy.from_dict(
            {"services": {"monitoring_ops": {"privacy": "group_only", "allowed_groups": ["ops"]}}}
        )
        rbac = _make_rbac()
        enforcer = PrivacyPolicyEnforcer(policy=policy, rbac_config=rbac)
        assert not enforcer.is_service_allowed(COLLAB_ID, "monitoring_ops")

    def test_unknown_service_allowed_by_default(self, enforcer):
        # Services not in policy default to allowed (whitelist, not blacklist approach)
        assert enforcer.is_service_allowed(COLLAB_ID, "some_random_api_not_in_policy")


# ---------------------------------------------------------------------------
# Audit / alert flags
# ---------------------------------------------------------------------------


class TestAuditAndAlert:
    def test_should_audit_private_service(self, enforcer):
        assert enforcer.should_audit(COLLAB_ID, "gmail")

    def test_should_not_audit_unknown_service(self, enforcer):
        assert not enforcer.should_audit(COLLAB_ID, "some_unknown_svc")

    def test_should_alert_non_owner(self, enforcer):
        assert enforcer.should_alert(COLLAB_ID, "gmail")

    def test_should_not_alert_owner(self, enforcer):
        assert not enforcer.should_alert(OWNER_ID, "gmail")

    def test_audit_disabled_globally(self, rbac):
        policy = PrivacyPolicy.from_dict({"audit_access_attempts": False})
        enforcer = PrivacyPolicyEnforcer(policy=policy, rbac_config=rbac)
        assert not enforcer.should_audit(COLLAB_ID, "gmail")


# ---------------------------------------------------------------------------
# Response filtering
# ---------------------------------------------------------------------------


class TestResponseFiltering:
    def test_owner_response_not_filtered(self, enforcer):
        raw = "From: admin@example.com\nTo: boss@example.com\nSubject: quarterly report"
        filtered, was_modified = enforcer.filter_response(raw, OWNER_ID)
        assert filtered == raw
        assert not was_modified

    def test_collaborator_email_content_redacted(self, enforcer):
        raw = "From: admin@example.com — the report is ready"
        filtered, was_modified = enforcer.filter_response(raw, COLLAB_ID)
        assert was_modified
        assert "admin@example.com" not in filtered
        assert "[CONTENT BLOCKED" in filtered

    def test_collaborator_api_key_redacted(self, enforcer):
        # Format matches pattern: keyword[:=]value on same line
        raw = "token=sk-abcdefghij1234567890 — use for auth"
        filtered, was_modified = enforcer.filter_response(raw, COLLAB_ID)
        assert was_modified
        assert "sk-abcdefghij1234567890" not in filtered

    def test_clean_response_not_modified(self, enforcer):
        raw = "The BESS fleet alarm threshold has been updated to 95%."
        filtered, was_modified = enforcer.filter_response(raw, COLLAB_ID)
        assert not was_modified
        assert filtered == raw

    def test_extra_pattern_redacted(self, rbac):
        policy = PrivacyPolicy.from_dict({"extra_redact_patterns": [r"\bCONFIDENTIAL-\w+\b"]})
        enforcer = PrivacyPolicyEnforcer(policy=policy, rbac_config=rbac)
        raw = "Project code: CONFIDENTIAL-X99 is approved."
        filtered, was_modified = enforcer.filter_response(raw, COLLAB_ID)
        assert was_modified
        assert "CONFIDENTIAL-X99" not in filtered

    def test_invalid_extra_pattern_does_not_crash(self, rbac):
        policy = PrivacyPolicy.from_dict(
            {"extra_redact_patterns": [r"[invalid(pattern"]}  # malformed regex
        )
        enforcer = PrivacyPolicyEnforcer(policy=policy, rbac_config=rbac)
        raw = "Some safe response"
        filtered, _ = enforcer.filter_response(raw, COLLAB_ID)
        assert filtered == raw  # no crash, returns unchanged

    def test_contains_private_data_detects_email(self, enforcer):
        assert enforcer.contains_private_data("From: user@example.com Subject: hello")

    def test_contains_private_data_clean_text(self, enforcer):
        assert not enforcer.contains_private_data("Normal conversation about monitoring.")
