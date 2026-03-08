# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for gateway/security/credential_injector.py — verify secrets never leak."""
from __future__ import annotations

import logging
import tempfile
from pathlib import Path

import pytest
from gateway.security.credential_injector import (
    CredentialInjector,
    CredentialInjectorConfig,
    CredentialMapping,
)


@pytest.fixture
def secrets_dir(tmp_path):
    """Create a temp secrets directory with a test credential."""
    secret_file = tmp_path / "test_api_key.txt"
    secret_file.write_text("sk-test-secret-key-12345678901234567890")
    return tmp_path


@pytest.fixture
def injector(secrets_dir):
    """CredentialInjector with a custom mapping pointing at the temp secrets."""
    cfg = CredentialInjectorConfig(
        secrets_dir=str(secrets_dir),
        enabled=True,
        leak_detection=True,
        mappings=[
            CredentialMapping(
                domain="api.example.com",
                header_name="Authorization",
                secret_file="test_api_key.txt",
                header_prefix="Bearer ",
            ),
        ],
    )
    return CredentialInjector(config=cfg)


# ---------------------------------------------------------------------------
# Header injection
# ---------------------------------------------------------------------------

class TestCredentialInjection:
    def test_credential_injected_into_request(self, injector):
        headers: dict[str, str] = {}
        injector.inject_headers("api.example.com", headers)
        assert "Authorization" in headers
        assert headers["Authorization"].startswith("Bearer ")

    def test_credential_not_injected_for_unknown_domain(self, injector):
        headers: dict[str, str] = {}
        injector.inject_headers("unknown.example.com", headers)
        assert "Authorization" not in headers

    def test_has_credential_true_for_loaded(self, injector):
        assert injector.has_credential("api.example.com")

    def test_has_credential_false_for_missing(self, injector):
        assert not injector.has_credential("nonexistent.example.com")

    def test_injection_disabled(self, secrets_dir):
        cfg = CredentialInjectorConfig(
            secrets_dir=str(secrets_dir),
            enabled=False,
            mappings=[
                CredentialMapping(
                    domain="api.example.com",
                    header_name="Authorization",
                    secret_file="test_api_key.txt",
                    header_prefix="Bearer ",
                ),
            ],
        )
        inj = CredentialInjector(config=cfg)
        headers: dict[str, str] = {}
        inj.inject_headers("api.example.com", headers)
        assert "Authorization" not in headers


# ---------------------------------------------------------------------------
# Leak detection
# ---------------------------------------------------------------------------

class TestLeakDetection:
    def test_openai_key_detected(self, injector):
        content = "Here is the key: sk-abcdefghijklmnopqrstuvwxyz1234"
        result = injector.scan_for_credential_leak(content)
        assert result is not None

    def test_aws_key_detected(self, injector):
        content = "AWS key is AKIAIOSFODNN7EXAMPLE"
        result = injector.scan_for_credential_leak(content)
        assert result is not None

    def test_github_token_detected(self, injector):
        content = "Token: ghp_ABCDEFghijklmnopqrstuvwxyz0123456789"
        result = injector.scan_for_credential_leak(content)
        assert result is not None

    def test_clean_content_passes(self, injector):
        content = "The weather in NYC is 72°F and sunny."
        result = injector.scan_for_credential_leak(content)
        assert result is None

    def test_leak_detection_disabled(self, secrets_dir):
        cfg = CredentialInjectorConfig(
            secrets_dir=str(secrets_dir),
            leak_detection=False,
        )
        inj = CredentialInjector(config=cfg)
        result = inj.scan_for_credential_leak("sk-abcdefghijklmnopqrstuvwxyz1234")
        assert result is None

    def test_jwt_detected(self, injector):
        # Minimal JWT-like string
        content = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.something"
        result = injector.scan_for_credential_leak(content)
        assert result is not None

    def test_slack_token_detected(self, injector):
        content = "xoxb-1234567890-abcdefghij"
        result = injector.scan_for_credential_leak(content)
        assert result is not None


# ---------------------------------------------------------------------------
# Status endpoint
# ---------------------------------------------------------------------------

class TestStatus:
    def test_get_status_structure(self, injector):
        status = injector.get_status()
        assert "enabled" in status
        assert "leak_detection" in status
        assert "domains_configured" in status
        assert "credentials_loaded" in status
        assert isinstance(status["domains"], dict)

    def test_credential_never_in_logs(self, injector, caplog):
        """Verify that raw credential values never appear in log output."""
        with caplog.at_level(logging.DEBUG):
            headers: dict[str, str] = {}
            injector.inject_headers("api.example.com", headers)
        # The actual secret value should NOT appear in any log record
        secret = "sk-test-secret-key-12345678901234567890"
        for record in caplog.records:
            assert secret not in record.getMessage(), (
                f"Secret leaked in log: {record.getMessage()}"
            )
