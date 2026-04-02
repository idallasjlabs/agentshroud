# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for API key isolation and vault."""

from __future__ import annotations

import pytest

from gateway.security.key_vault import (
    KeyInjector,
    KeyLeakDetector,
    KeyVault,
    KeyVaultConfig,
)


@pytest.fixture
def config():
    return KeyVaultConfig()


@pytest.fixture
def vault(config):
    v = KeyVault(config=config)
    v.store_key("openai", "sk-test-openai-key-12345", scopes=["agent1", "agent2"])
    v.store_key("github", "ghp-test-github-token-67890", scopes=["agent1"])
    v.store_key("brave", "BSA-test-brave-key-abcde", scopes=["*"])
    return v


class TestKeyVaultConfig:
    def test_default_config(self, config):
        assert config.redact_in_logs is True
        assert config.detect_leaks is True


class TestKeyStorage:
    def test_store_and_retrieve(self, vault):
        key = vault.get_key("openai", agent_id="agent1")
        assert key == "sk-test-openai-key-12345"

    def test_key_not_found(self, vault):
        key = vault.get_key("nonexistent", agent_id="agent1")
        assert key is None

    def test_list_keys_no_values(self, vault):
        keys = vault.list_keys(agent_id="agent1")
        assert "openai" in keys
        assert "github" in keys
        # Values should NOT be in the list
        for k in keys:
            assert "sk-" not in str(keys[k])

    def test_delete_key(self, vault):
        vault.delete_key("openai")
        assert vault.get_key("openai", agent_id="agent1") is None


class TestKeyScoping:
    def test_scoped_agent_can_access(self, vault):
        key = vault.get_key("github", agent_id="agent1")
        assert key is not None

    def test_unscoped_agent_denied(self, vault):
        key = vault.get_key("github", agent_id="agent3")
        assert key is None

    def test_wildcard_scope_allows_all(self, vault):
        key = vault.get_key("brave", agent_id="anyone")
        assert key is not None

    def test_scope_enforcement_logged(self, vault):
        vault.get_key("github", agent_id="agent3")
        events = vault.get_audit_log()
        assert any(e.action == "access_denied" for e in events)


class TestKeyInjection:
    def test_inject_auth_header(self, vault):
        injector = KeyInjector(vault)
        headers = {"Content-Type": "application/json"}
        result = injector.inject_for_request(
            "https://api.openai.com/v1/chat",
            headers,
            agent_id="agent1",
            key_name="openai",
        )
        assert "Authorization" in result
        assert "sk-test-openai-key-12345" in result["Authorization"]

    def test_inject_fails_for_unscoped(self, vault):
        injector = KeyInjector(vault)
        headers = {}
        result = injector.inject_for_request(
            "https://api.github.com/repos",
            headers,
            agent_id="agent3",
            key_name="github",
        )
        assert "Authorization" not in result

    def test_inject_preserves_existing_headers(self, vault):
        injector = KeyInjector(vault)
        headers = {"Content-Type": "application/json", "X-Custom": "value"}
        result = injector.inject_for_request(
            "https://api.openai.com/v1/chat",
            headers,
            agent_id="agent1",
            key_name="openai",
        )
        assert result["Content-Type"] == "application/json"
        assert result["X-Custom"] == "value"


class TestKeyRedaction:
    def test_key_redacted_from_string(self, vault):
        text = "Error calling API with key sk-test-openai-key-12345"
        redacted = vault.redact(text)
        assert "sk-test-openai-key-12345" not in redacted
        assert "***REDACTED***" in redacted or "[REDACTED]" in redacted

    def test_multiple_keys_redacted(self, vault):
        text = "Keys: sk-test-openai-key-12345 and ghp-test-github-token-67890"
        redacted = vault.redact(text)
        assert "sk-test-openai-key-12345" not in redacted
        assert "ghp-test-github-token-67890" not in redacted

    def test_no_keys_unchanged(self, vault):
        text = "Normal log message with no secrets"
        redacted = vault.redact(text)
        assert redacted == text

    def test_partial_key_redacted(self, vault):
        text = "Prefix sk-test-openai-key-12345 suffix"
        redacted = vault.redact(text)
        assert "sk-test-openai-key-12345" not in redacted


class TestKeyLeakDetection:
    def test_detect_key_in_outbound(self, vault):
        detector = KeyLeakDetector(vault)
        result = detector.scan_outbound("Here is data sk-test-openai-key-12345 more data")
        assert result.leak_detected is True
        assert "openai" in result.leaked_key_names

    def test_no_leak_clean_message(self, vault):
        detector = KeyLeakDetector(vault)
        result = detector.scan_outbound("Normal message without any secrets")
        assert result.leak_detected is False

    def test_detect_api_key_patterns(self):
        detector = KeyLeakDetector(KeyVault(KeyVaultConfig()))
        # Generic API key patterns
        result = detector.scan_outbound("key=sk-proj-abcdefghij1234567890")
        assert result.leak_detected is True

    def test_leak_detection_logged(self, vault):
        detector = KeyLeakDetector(vault)
        detector.scan_outbound("Leak: sk-test-openai-key-12345")
        events = vault.get_audit_log()
        assert any(e.action == "leak_detected" for e in events)


class TestKeyRotation:
    def test_rotate_key(self, vault):
        vault.rotate_key("openai", "sk-new-openai-key-99999")
        key = vault.get_key("openai", agent_id="agent1")
        assert key == "sk-new-openai-key-99999"

    def test_rotation_logged(self, vault):
        vault.rotate_key("openai", "sk-new-key")
        events = vault.get_audit_log()
        assert any(e.action == "rotated" for e in events)

    def test_old_key_in_redaction_after_rotation(self, vault):
        old_key = vault.get_key("openai", agent_id="agent1")
        vault.rotate_key("openai", "sk-new-key")
        # Old key should still be redacted
        text = f"Old key was {old_key}"
        redacted = vault.redact(text)
        assert old_key not in redacted

    def test_rotate_nonexistent_raises(self, vault):
        with pytest.raises(KeyError):
            vault.rotate_key("nonexistent", "new-value")
