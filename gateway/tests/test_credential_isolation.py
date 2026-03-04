# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for credential isolation — R-10, R-11, R-12.

Verifies:
- Gateway is the sole credential holder
- Agent container has no secret files or credential env vars
- Transparent credential injection works
- Credential leak detection catches patterns
"""
from __future__ import annotations

import pytest
import os
import re


class TestCredentialInjector:
    """Test the CredentialInjector module."""

    @pytest.fixture
    def injector(self):
        from gateway.security.credential_injector import (
            CredentialInjector,
            CredentialInjectorConfig,
        )
        # Use a temp dir with no secrets (simulating agent container)
        config = CredentialInjectorConfig(secrets_dir="/tmp/nonexistent-secrets")
        return CredentialInjector(config)

    @pytest.fixture
    def injector_with_secrets(self, tmp_path):
        from gateway.security.credential_injector import (
            CredentialInjector,
            CredentialInjectorConfig,
        )
        # Create fake secrets
        (tmp_path / "anthropic_api_key.txt").write_text("sk-ant-test-key-12345")
        (tmp_path / "openai_api_key.txt").write_text("sk-test-openai-key-67890")
        (tmp_path / "anthropic_oauth_token.txt").write_text("test-oauth-token-abc")
        config = CredentialInjectorConfig(secrets_dir=str(tmp_path))
        return CredentialInjector(config)

    def test_inject_anthropic_key(self, injector_with_secrets):
        headers = {}
        injector_with_secrets.inject_headers("api.anthropic.com", headers)
        # Should have injected the OAuth token (last mapping wins for same domain)
        assert "Authorization" in headers or "x-api-key" in headers

    def test_inject_openai_key(self, injector_with_secrets):
        headers = {}
        injector_with_secrets.inject_headers("api.openai.com", headers)
        assert "Authorization" in headers
        assert headers["Authorization"].startswith("Bearer ")

    def test_no_injection_unknown_domain(self, injector_with_secrets):
        headers = {}
        injector_with_secrets.inject_headers("evil.example.com", headers)
        assert len(headers) == 0  # No credentials injected

    def test_no_injection_when_disabled(self, tmp_path):
        from gateway.security.credential_injector import (
            CredentialInjector,
            CredentialInjectorConfig,
        )
        (tmp_path / "anthropic_api_key.txt").write_text("sk-ant-test")
        config = CredentialInjectorConfig(secrets_dir=str(tmp_path), enabled=False)
        injector = CredentialInjector(config)
        headers = {}
        injector.inject_headers("api.anthropic.com", headers)
        assert len(headers) == 0

    def test_no_secrets_loaded_from_empty_dir(self, injector):
        """Agent container should have no secrets."""
        status = injector.get_status()
        assert status["credentials_loaded"] == 0

    def test_has_credential(self, injector_with_secrets):
        assert injector_with_secrets.has_credential("api.openai.com")
        assert not injector_with_secrets.has_credential("evil.example.com")

    def test_status_report(self, injector_with_secrets):
        status = injector_with_secrets.get_status()
        assert status["enabled"] is True
        assert status["credentials_loaded"] > 0
        assert "api.anthropic.com" in status["domains"]


class TestCredentialLeakDetection:
    """Test that credential patterns are detected in outbound content."""

    @pytest.fixture
    def injector(self):
        from gateway.security.credential_injector import (
            CredentialInjector,
            CredentialInjectorConfig,
        )
        config = CredentialInjectorConfig(secrets_dir="/tmp/nonexistent")
        return CredentialInjector(config)

    def test_detect_openai_key(self, injector):
        result = injector.scan_for_credential_leak("Here is my key: sk-proj-abc123def456ghi789jkl012mno345pqr678stu")
        assert result is not None
        assert "API key" in result

    def test_detect_aws_key(self, injector):
        result = injector.scan_for_credential_leak("AWS key: AKIAIOSFODNN7EXAMPLE")
        assert result is not None
        assert "AWS" in result

    def test_detect_github_token(self, injector):
        result = injector.scan_for_credential_leak("Token: ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghij")
        assert result is not None
        assert "GitHub" in result

    def test_detect_google_oauth_secret(self, injector):
        result = injector.scan_for_credential_leak("Secret: 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")
        assert result is not None
        assert "Google" in result

    def test_detect_jwt_token(self, injector):
        result = injector.scan_for_credential_leak(
            "Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.dozjgNryP4J3jVmNHl0w5N_XgL0n3I9PlFUP0THsR8U"
        )
        assert result is not None
        assert "JWT" in result

    def test_detect_1password_token(self, injector):
        result = injector.scan_for_credential_leak("op_1234567890abcdefghijklmnop")
        assert result is not None
        assert "1Password" in result

    def test_clean_content_passes(self, injector):
        result = injector.scan_for_credential_leak("This is a normal message about security best practices.")
        assert result is None

    def test_clean_code_passes(self, injector):
        result = injector.scan_for_credential_leak("def get_api_key(): return os.getenv('KEY')")
        assert result is None

    def test_leak_detection_disabled(self):
        from gateway.security.credential_injector import (
            CredentialInjector,
            CredentialInjectorConfig,
        )
        config = CredentialInjectorConfig(
            secrets_dir="/tmp/nonexistent",
            leak_detection=False,
        )
        injector = CredentialInjector(config)
        result = injector.scan_for_credential_leak("sk-proj-abc123def456ghi789jkl012mno345pqr678stu")
        assert result is None  # Detection disabled


class TestDockerSecretIsolation:
    """Verify Docker Compose configuration isolates secrets correctly."""

    def test_compose_gateway_has_secrets(self):
        """Gateway service should have secrets configured."""
        import yaml
        compose_path = os.path.join(
            os.path.dirname(__file__), "..", "..", "docker", "docker-compose.yml"
        )
        if not os.path.exists(compose_path):
            pytest.skip("docker-compose.yml not found")
        with open(compose_path) as f:
            compose = yaml.safe_load(f)
        gateway = compose.get("services", {}).get("gateway", {})
        assert "secrets" in gateway, "Gateway service must have secrets configured"

    def test_compose_agent_no_gateway_secrets(self):
        """Agent (agentshroud) service should not have credential secrets."""
        import yaml
        compose_path = os.path.join(
            os.path.dirname(__file__), "..", "..", "docker", "docker-compose.yml"
        )
        if not os.path.exists(compose_path):
            pytest.skip("docker-compose.yml not found")
        with open(compose_path) as f:
            compose = yaml.safe_load(f)
        agent = compose.get("services", {}).get("agentshroud", {})
        agent_secrets = agent.get("secrets", [])
        # Agent should not have credential-type secrets
        credential_secrets = [
            "anthropic_api_key", "openai_api_key", "gmail_password",
            "op_service_account_token", "1password_service_account",
        ]
        for secret_name in credential_secrets:
            # Check both string refs and dict refs
            for s in agent_secrets:
                name = s if isinstance(s, str) else s.get("source", "")
                assert name != secret_name, (
                    f"Agent container should NOT have secret '{secret_name}' — "
                    f"credentials must be gateway-only (R-11)"
                )
