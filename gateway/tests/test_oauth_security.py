# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for oauth_security module - MCP OAuth proxy security.
TDD: Written before implementation.
"""

from __future__ import annotations

import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from security.oauth_security import (
    ConfusedDeputyError,
    OAuthError,
    OAuthRequest,
    OAuthSecurityValidator,
    PKCEViolation,
    RedirectMismatch,
)


@pytest.fixture
def validator():
    return OAuthSecurityValidator(
        allowed_redirect_uris=["https://app.example.com/callback"], require_pkce=True
    )


class TestClientValidation:
    def test_unique_client_id_accepted(self, validator):
        req = OAuthRequest(
            client_id="client-abc-123",
            redirect_uri="https://app.example.com/callback",
            state="random-state",
            code_challenge="challenge",
            code_challenge_method="S256",
        )
        assert validator.validate_request(req)

    def test_static_shared_client_id_rejected(self, validator):
        validator.register_known_shared_ids(["public-client", "default"])
        req = OAuthRequest(
            client_id="public-client",
            redirect_uri="https://app.example.com/callback",
            state="s",
            code_challenge="c",
            code_challenge_method="S256",
        )
        with pytest.raises(ConfusedDeputyError):
            validator.validate_request(req)

    def test_empty_client_id_rejected(self, validator):
        req = OAuthRequest(
            client_id="",
            redirect_uri="https://app.example.com/callback",
            state="s",
            code_challenge="c",
            code_challenge_method="S256",
        )
        with pytest.raises(OAuthError):
            validator.validate_request(req)


class TestStateValidation:
    def test_valid_state_accepted(self, validator):
        req = OAuthRequest(
            client_id="c1",
            redirect_uri="https://app.example.com/callback",
            state="abc123xyz",
            code_challenge="ch",
            code_challenge_method="S256",
        )
        assert validator.validate_request(req)

    def test_empty_state_rejected(self, validator):
        req = OAuthRequest(
            client_id="c1",
            redirect_uri="https://app.example.com/callback",
            state="",
            code_challenge="ch",
            code_challenge_method="S256",
        )
        with pytest.raises(OAuthError):
            validator.validate_request(req)

    def test_short_state_rejected(self, validator):
        req = OAuthRequest(
            client_id="c1",
            redirect_uri="https://app.example.com/callback",
            state="ab",
            code_challenge="ch",
            code_challenge_method="S256",
        )
        with pytest.raises(OAuthError):
            validator.validate_request(req)

    def test_state_replay_detected(self, validator):
        req = OAuthRequest(
            client_id="c1",
            redirect_uri="https://app.example.com/callback",
            state="unique-state-1234",
            code_challenge="ch",
            code_challenge_method="S256",
        )
        validator.validate_request(req)
        validator.record_state_used("unique-state-1234")
        with pytest.raises(OAuthError, match="replay"):
            validator.check_state_reuse("unique-state-1234")


class TestPKCE:
    def test_pkce_required_missing_challenge(self, validator):
        req = OAuthRequest(
            client_id="c1",
            redirect_uri="https://app.example.com/callback",
            state="valid-state",
            code_challenge=None,
            code_challenge_method=None,
        )
        with pytest.raises(PKCEViolation):
            validator.validate_request(req)

    def test_pkce_s256_accepted(self, validator):
        req = OAuthRequest(
            client_id="c1",
            redirect_uri="https://app.example.com/callback",
            state="valid-state",
            code_challenge="abcdef",
            code_challenge_method="S256",
        )
        assert validator.validate_request(req)

    def test_pkce_plain_rejected_when_s256_required(self, validator):
        validator.require_s256 = True
        req = OAuthRequest(
            client_id="c1",
            redirect_uri="https://app.example.com/callback",
            state="valid-state",
            code_challenge="abcdef",
            code_challenge_method="plain",
        )
        with pytest.raises(PKCEViolation):
            validator.validate_request(req)

    def test_pkce_verifier_validation(self, validator):
        import base64
        import hashlib

        verifier = "dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk"
        expected = (
            base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest())
            .rstrip(b"=")
            .decode()
        )
        assert validator.verify_pkce(verifier, expected, "S256")


class TestRedirectURI:
    def test_exact_match_accepted(self, validator):
        assert validator.validate_redirect_uri("https://app.example.com/callback")

    def test_different_uri_rejected(self, validator):
        with pytest.raises(RedirectMismatch):
            validator.validate_redirect_uri("https://evil.com/callback")

    def test_path_traversal_rejected(self, validator):
        with pytest.raises(RedirectMismatch):
            validator.validate_redirect_uri("https://app.example.com/callback/../admin")

    def test_http_rejected(self, validator):
        v = OAuthSecurityValidator(
            allowed_redirect_uris=["http://localhost/cb"], require_pkce=False
        )
        # localhost http is ok
        assert v.validate_redirect_uri("http://localhost/cb")
        # but non-localhost http is not
        with pytest.raises(RedirectMismatch):
            v.validate_redirect_uri("http://evil.com/cb")


class TestConsentCookieBinding:
    def test_create_consent_cookie(self, validator):
        cookie = validator.create_consent_cookie("client-1", ["read", "write"], "user-123")
        assert cookie
        assert len(cookie) > 20

    def test_validate_consent_cookie(self, validator):
        cookie = validator.create_consent_cookie("client-1", ["read"], "user-1")
        assert validator.validate_consent_cookie(cookie, "client-1", ["read"], "user-1")

    def test_cookie_wrong_client_fails(self, validator):
        cookie = validator.create_consent_cookie("client-1", ["read"], "user-1")
        assert not validator.validate_consent_cookie(cookie, "client-2", ["read"], "user-1")

    def test_cookie_wrong_scope_fails(self, validator):
        cookie = validator.create_consent_cookie("client-1", ["read"], "user-1")
        assert not validator.validate_consent_cookie(cookie, "client-1", ["write"], "user-1")

    def test_cookie_tamper_detected(self, validator):
        cookie = validator.create_consent_cookie("client-1", ["read"], "user-1")
        tampered = cookie[:-4] + "XXXX"
        assert not validator.validate_consent_cookie(tampered, "client-1", ["read"], "user-1")
