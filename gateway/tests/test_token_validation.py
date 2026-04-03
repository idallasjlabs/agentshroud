# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for token_validation module.
TDD: Written before implementation.
"""

from __future__ import annotations

import base64
import json
import os
import sys
import time

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from security.token_validation import (
    AudienceMismatch,
    IssuerMismatch,
    ScopeViolation,
    TokenError,
    TokenExpiredError,
    TokenValidationResult,
    TokenValidator,
)


def _make_token(payload: dict) -> str:
    """Create a simple base64-encoded JSON token for testing."""
    header = base64.urlsafe_b64encode(json.dumps({"alg": "none"}).encode()).rstrip(b"=").decode()
    body = base64.urlsafe_b64encode(json.dumps(payload).encode()).rstrip(b"=").decode()
    return f"{header}.{body}.fakesig"


@pytest.fixture
def validator():
    return TokenValidator(
        expected_audience="https://api.agentshroud.com",
        expected_issuer="https://auth.agentshroud.com",
        audit_log_path=":memory:",
    )


class TestAudienceValidation:
    def test_correct_audience_accepted(self, validator):
        token = _make_token(
            {
                "aud": "https://api.agentshroud.com",
                "iss": "https://auth.agentshroud.com",
                "exp": time.time() + 3600,
                "scope": "read",
            }
        )
        result = validator.validate(token)
        assert result.valid

    def test_wrong_audience_rejected(self, validator):
        token = _make_token(
            {
                "aud": "https://other-api.com",
                "iss": "https://auth.agentshroud.com",
                "exp": time.time() + 3600,
                "scope": "read",
            }
        )
        with pytest.raises(AudienceMismatch):
            validator.validate(token)

    def test_missing_audience_rejected(self, validator):
        token = _make_token(
            {"iss": "https://auth.agentshroud.com", "exp": time.time() + 3600, "scope": "read"}
        )
        with pytest.raises(AudienceMismatch):
            validator.validate(token)

    def test_array_audience_accepted(self, validator):
        token = _make_token(
            {
                "aud": ["https://api.agentshroud.com", "https://other.com"],
                "iss": "https://auth.agentshroud.com",
                "exp": time.time() + 3600,
                "scope": "read",
            }
        )
        result = validator.validate(token)
        assert result.valid


class TestIssuerValidation:
    def test_wrong_issuer_rejected(self, validator):
        token = _make_token(
            {
                "aud": "https://api.agentshroud.com",
                "iss": "https://evil-auth.com",
                "exp": time.time() + 3600,
                "scope": "read",
            }
        )
        with pytest.raises(IssuerMismatch):
            validator.validate(token)

    def test_missing_issuer_rejected(self, validator):
        token = _make_token(
            {"aud": "https://api.agentshroud.com", "exp": time.time() + 3600, "scope": "read"}
        )
        with pytest.raises(IssuerMismatch):
            validator.validate(token)


class TestScopeEnforcement:
    def test_requested_scope_within_granted(self, validator):
        token = _make_token(
            {
                "aud": "https://api.agentshroud.com",
                "iss": "https://auth.agentshroud.com",
                "exp": time.time() + 3600,
                "scope": "read write",
            }
        )
        result = validator.validate(token, required_scopes=["read"])
        assert result.valid

    def test_requested_scope_exceeds_granted(self, validator):
        token = _make_token(
            {
                "aud": "https://api.agentshroud.com",
                "iss": "https://auth.agentshroud.com",
                "exp": time.time() + 3600,
                "scope": "read",
            }
        )
        with pytest.raises(ScopeViolation):
            validator.validate(token, required_scopes=["read", "admin"])

    def test_empty_scope_accepted_when_none_required(self, validator):
        token = _make_token(
            {
                "aud": "https://api.agentshroud.com",
                "iss": "https://auth.agentshroud.com",
                "exp": time.time() + 3600,
                "scope": "",
            }
        )
        result = validator.validate(token)
        assert result.valid

    def test_no_scope_claim_rejected_when_required(self, validator):
        token = _make_token(
            {
                "aud": "https://api.agentshroud.com",
                "iss": "https://auth.agentshroud.com",
                "exp": time.time() + 3600,
            }
        )
        with pytest.raises(ScopeViolation):
            validator.validate(token, required_scopes=["read"])


class TestTokenExpiry:
    def test_expired_token_rejected(self, validator):
        token = _make_token(
            {
                "aud": "https://api.agentshroud.com",
                "iss": "https://auth.agentshroud.com",
                "exp": time.time() - 100,
                "scope": "read",
            }
        )
        with pytest.raises(TokenExpiredError):
            validator.validate(token)

    def test_missing_exp_rejected(self, validator):
        token = _make_token(
            {
                "aud": "https://api.agentshroud.com",
                "iss": "https://auth.agentshroud.com",
                "scope": "read",
            }
        )
        with pytest.raises(TokenError):
            validator.validate(token)

    def test_future_token_accepted(self, validator):
        token = _make_token(
            {
                "aud": "https://api.agentshroud.com",
                "iss": "https://auth.agentshroud.com",
                "exp": time.time() + 7200,
                "scope": "read",
            }
        )
        result = validator.validate(token)
        assert result.valid


class TestAuditLogging:
    def test_successful_validation_logged(self, validator):
        token = _make_token(
            {
                "aud": "https://api.agentshroud.com",
                "iss": "https://auth.agentshroud.com",
                "exp": time.time() + 3600,
                "scope": "read",
            }
        )
        validator.validate(token)
        logs = validator.get_audit_log()
        assert len(logs) == 1
        assert logs[0]["decision"] == "approved"

    def test_failed_validation_logged(self, validator):
        token = _make_token(
            {
                "aud": "https://wrong.com",
                "iss": "https://auth.agentshroud.com",
                "exp": time.time() + 3600,
                "scope": "read",
            }
        )
        with pytest.raises(AudienceMismatch):
            validator.validate(token)
        logs = validator.get_audit_log()
        assert len(logs) == 1
        assert logs[0]["decision"] == "rejected"

    def test_multiple_validations_logged(self, validator):
        for i in range(5):
            token = _make_token(
                {
                    "aud": "https://api.agentshroud.com",
                    "iss": "https://auth.agentshroud.com",
                    "exp": time.time() + 3600,
                    "scope": "read",
                }
            )
            validator.validate(token)
        logs = validator.get_audit_log()
        assert len(logs) == 5


class TestMalformedTokens:
    def test_not_a_jwt_rejected(self, validator):
        with pytest.raises(TokenError):
            validator.validate("not-a-token")

    def test_empty_token_rejected(self, validator):
        with pytest.raises(TokenError):
            validator.validate("")

    def test_corrupted_payload_rejected(self, validator):
        with pytest.raises(TokenError):
            validator.validate("header.!!!invalid-base64!!!.sig")
