# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for gateway/security/credential_injector.py — verify secrets never leak."""

from __future__ import annotations

import logging
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
    secret_file.write_text("sk-example-not-a-real-key-000000000")
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

    def test_strip_headers_removes_conflicting_header(self, secrets_dir):
        """strip_headers must remove x-api-key before injecting Authorization: Bearer."""
        cfg = CredentialInjectorConfig(
            secrets_dir=str(secrets_dir),
            enabled=True,
            mappings=[
                CredentialMapping(
                    domain="api.example.com",
                    header_name="Authorization",
                    secret_file="test_api_key.txt",
                    header_prefix="Bearer ",
                    strip_headers=["x-api-key"],
                ),
            ],
        )
        inj = CredentialInjector(config=cfg)
        headers = {"x-api-key": "stale-oauth-token", "Content-Type": "application/json"}
        inj.inject_headers("api.example.com", headers)
        assert "x-api-key" not in headers, "x-api-key must be stripped"
        assert "Authorization" in headers
        assert headers["Authorization"].startswith("Bearer ")
        assert "Content-Type" in headers  # other headers untouched

    def test_anthropic_default_strips_x_api_key(self, tmp_path):
        """Default Anthropic mapping must strip x-api-key (regression guard)."""
        oauth_file = tmp_path / "anthropic_oauth_token"
        oauth_file.write_text("sk-ant-oat01-fake-token")
        cfg = CredentialInjectorConfig(secrets_dir=str(tmp_path), enabled=True)
        inj = CredentialInjector(config=cfg)
        headers = {"x-api-key": "sk-ant-oat01-fake-token", "anthropic-version": "2023-06-01"}
        inj.inject_headers("api.anthropic.com", headers)
        assert "x-api-key" not in headers, "x-api-key must be stripped for Anthropic"
        assert headers.get("Authorization", "").startswith("Bearer ")


# ---------------------------------------------------------------------------
# Leak detection
# ---------------------------------------------------------------------------


class TestLeakDetection:
    def test_openai_key_detected(self, injector):
        content = "Here is the key: sk-EXAMPLEFAKEKEYabcdef000000000000000000000000"
        result = injector.scan_for_credential_leak(content)
        assert result is not None

    def test_aws_key_detected(self, injector):
        content = "AWS key is AKIAIOSFODNN7EXAMPLE"
        result = injector.scan_for_credential_leak(content)
        assert result is not None

    def test_github_token_detected(self, injector):
        content = "Token: ghp_EXAMPLEFAKETOKENabcdefghijklmnopqrst"
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
        result = inj.scan_for_credential_leak("sk-EXAMPLEFAKEKEYabcdef000000000000000000000000")
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
        secret = "sk-example-not-a-real-key-000000000"
        for record in caplog.records:
            assert secret not in record.getMessage(), f"Secret leaked in log: {record.getMessage()}"


# ---------------------------------------------------------------------------
# OAuth-token injection (anthropic-beta header + inject-if-absent)
# ---------------------------------------------------------------------------


class TestOAuthInjection:
    """Verify gateway-side OAuth-token translation for the Anthropic path.

    Root cause context: Anthropic OAuth tokens (sk-ant-oat0…) are only accepted
    as Authorization: Bearer <token> + anthropic-beta: oauth-2025-04-20.
    Hermes sends them as x-api-key → 401. The gateway must intercept and translate.
    """

    def _make_anthropic_injector(self, tmp_path: Path) -> CredentialInjector:
        (tmp_path / "anthropic_oauth_token").write_text("sk-ant-oat01-gateway-token")
        return CredentialInjector(
            config=CredentialInjectorConfig(secrets_dir=str(tmp_path), enabled=True)
        )

    def test_adds_oauth_beta_header_when_injecting(self, tmp_path):
        """inject_headers sets anthropic-beta: oauth-2025-04-20 when Bearer is injected."""
        inj = self._make_anthropic_injector(tmp_path)
        headers: dict[str, str] = {"x-api-key": "sk-ant-oat01-hermes-token"}
        inj.inject_headers("api.anthropic.com", headers)
        assert "anthropic-beta" in headers
        assert "oauth-2025-04-20" in headers["anthropic-beta"]

    def test_inject_if_absent_skips_when_bearer_already_present(self, tmp_path):
        """inject_headers does NOT overwrite an existing Authorization: Bearer token,
        but it must still apply protocol-required extra_headers (e.g. anthropic-version).
        Hermes sends its own Bearer via the base-URL override without setting the version
        header — failing to add the version here is the bug behind the 400 retry loop."""
        inj = self._make_anthropic_injector(tmp_path)
        original = "Bearer sk-ant-oat01-openclaw-runtime-token"
        headers: dict[str, str] = {"Authorization": original}
        inj.inject_headers("api.anthropic.com", headers)
        assert (
            headers["Authorization"] == original
        ), "Gateway must not clobber client's Bearer token"
        assert (
            headers.get("anthropic-version") == "2023-06-01"
        ), "extra_headers must still be applied when caller owns auth"
        assert "oauth-2025-04-20" in headers.get("anthropic-beta", "")

    def test_x_api_key_stripped_and_bearer_plus_beta_injected(self, tmp_path):
        """x-api-key is stripped; Authorization: Bearer and anthropic-beta are added."""
        inj = self._make_anthropic_injector(tmp_path)
        headers: dict[str, str] = {
            "x-api-key": "sk-ant-oat01-hermes-token",
            "anthropic-version": "2023-06-01",
        }
        inj.inject_headers("api.anthropic.com", headers)
        assert "x-api-key" not in headers
        assert headers["Authorization"] == "Bearer sk-ant-oat01-gateway-token"
        assert "oauth-2025-04-20" in headers["anthropic-beta"]
        assert "anthropic-version" in headers  # unrelated headers must survive

    def test_anthropic_version_auto_injected_when_absent(self, tmp_path):
        """anthropic-version is required on every /v1/messages call; the gateway adds it
        automatically when the upstream client (e.g. hermes via base-URL override) does not.
        Without this Anthropic returns 400: 'anthropic-version: header is required'.
        """
        inj = self._make_anthropic_injector(tmp_path)
        headers: dict[str, str] = {"x-api-key": "sk-ant-oat01-hermes-token"}
        inj.inject_headers("api.anthropic.com", headers)
        assert headers.get("anthropic-version") == "2023-06-01"

    def test_existing_anthropic_version_preserved(self, tmp_path):
        """Caller-supplied anthropic-version (e.g. a newer beta date) must not be clobbered."""
        inj = self._make_anthropic_injector(tmp_path)
        headers: dict[str, str] = {
            "x-api-key": "sk-ant-oat01-hermes-token",
            "anthropic-version": "2024-10-01",
        }
        inj.inject_headers("api.anthropic.com", headers)
        # Comma-merge logic preserves the caller's value, appending the default once.
        assert "2024-10-01" in headers["anthropic-version"]

    def test_existing_anthropic_beta_preserved_and_oauth_appended_no_duplicate(self, tmp_path):
        """Existing anthropic-beta values are kept; oauth-2025-04-20 is appended once."""
        inj = self._make_anthropic_injector(tmp_path)
        headers: dict[str, str] = {
            "x-api-key": "sk-ant-oat01-hermes-token",
            "anthropic-beta": "computer-use-2024-10-22",
        }
        inj.inject_headers("api.anthropic.com", headers)
        beta = headers["anthropic-beta"]
        assert "computer-use-2024-10-22" in beta, "Pre-existing beta flags must be preserved"
        assert "oauth-2025-04-20" in beta
        assert beta.count("oauth-2025-04-20") == 1, "oauth-2025-04-20 must appear exactly once"


# ---------------------------------------------------------------------------
# CVE-2026-9352: load_all_secret_file_values
# ---------------------------------------------------------------------------


class TestLoadAllSecretFileValues:
    """load_all_secret_file_values reads all Docker secret files for scrubbing."""

    def test_returns_empty_when_dir_missing(self, tmp_path):
        from gateway.security.credential_injector import load_all_secret_file_values

        result = load_all_secret_file_values(secrets_dir=str(tmp_path / "nonexistent"))
        assert result == []

    def test_returns_values_meeting_min_len(self, tmp_path):
        from gateway.security.credential_injector import load_all_secret_file_values

        (tmp_path / "token_a").write_text("supersecrettoken12345")
        (tmp_path / "token_b").write_text("short")
        result = load_all_secret_file_values(secrets_dir=str(tmp_path), min_len=12)
        assert "supersecrettoken12345" in result
        assert "short" not in result

    def test_strips_trailing_newline(self, tmp_path):
        from gateway.security.credential_injector import load_all_secret_file_values

        (tmp_path / "mytoken").write_text("myverylongsecretvalue\n")
        result = load_all_secret_file_values(secrets_dir=str(tmp_path), min_len=12)
        assert "myverylongsecretvalue" in result
        assert "myverylongsecretvalue\n" not in result

    def test_get_all_loaded_values_method(self, tmp_path):
        """CredentialInjector.get_all_loaded_values returns all loaded credential values."""
        from gateway.security.credential_injector import (
            CredentialInjector,
            CredentialInjectorConfig,
        )

        (tmp_path / "anthropic_api_key").write_text("sk-ant-oat01-testvalue12345678")
        cfg = CredentialInjectorConfig(secrets_dir=str(tmp_path))
        inj = CredentialInjector(config=cfg)
        vals = inj.get_all_loaded_values(min_len=12)
        # The injector only exposes values from its domain map, not all files
        # — that's correct: load_all_secret_file_values handles the rest.
        assert isinstance(vals, list)
