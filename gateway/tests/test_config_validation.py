# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Configuration Validation Tests — example configs and validation."""

from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent.parent


def _parse_env_file(path: Path) -> dict[str, str]:
    """Parse a .env file into a dict (ignoring comments and blanks)."""
    config = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            key, _, value = line.partition("=")
            config[key.strip()] = value.strip()
    return config


class TestParanoidConfig:
    """paranoid.env should enable ALL security features."""

    @pytest.fixture
    def config(self):
        path = REPO_ROOT / "examples" / "paranoid.env"
        if not path.exists():
            pytest.skip("paranoid.env not found")
        return _parse_env_file(path)

    def test_has_auth_token_placeholder(self, config):
        assert "GATEWAY_AUTH_TOKEN" in config

    def test_pii_enabled(self, config):
        assert config.get("PII_REDACTION", "").lower() == "true"

    def test_pii_engine_presidio(self, config):
        assert config.get("PII_ENGINE") == "presidio"

    def test_approval_queue_enabled(self, config):
        assert config.get("APPROVAL_QUEUE", "").lower() == "true"

    def test_prompt_guard_enabled(self, config):
        assert config.get("PROMPT_GUARD_ENABLED", "").lower() == "true"

    def test_egress_filter_enabled(self, config):
        assert config.get("EGRESS_FILTER_ENABLED", "").lower() == "true"

    def test_trust_manager_enabled(self, config):
        assert config.get("TRUST_MANAGER_ENABLED", "").lower() == "true"

    def test_drift_detector_enabled(self, config):
        assert config.get("DRIFT_DETECTOR_ENABLED", "").lower() == "true"

    def test_encrypted_store_enabled(self, config):
        assert config.get("ENCRYPTED_STORE_ENABLED", "").lower() == "true"

    def test_kill_switch_enabled(self, config):
        assert config.get("KILL_SWITCH_ENABLED", "").lower() == "true"

    def test_container_hardening(self, config):
        assert config.get("READ_ONLY_ROOTFS", "").lower() == "true"
        assert config.get("NO_NEW_PRIVILEGES", "").lower() == "true"

    def test_rootless(self, config):
        assert config.get("ROOTLESS", "").lower() == "true"

    def test_has_memory_limit(self, config):
        assert "MEMORY_LIMIT" in config

    def test_has_seccomp_profile(self, config):
        assert "SECCOMP_PROFILE" in config

    def test_telemetry_disabled(self, config):
        assert config.get("TELEMETRY_DISABLED", "").lower() == "true"

    def test_ssh_requires_approval(self, config):
        assert config.get("SSH_REQUIRE_APPROVAL", "").lower() == "true"

    def test_extensive_approval_actions(self, config):
        actions = config.get("REQUIRE_APPROVAL_FOR", "")
        assert "email_sending" in actions
        assert "file_deletion" in actions

    def test_long_retention(self, config):
        days = int(config.get("LEDGER_RETENTION_DAYS", "0"))
        assert days >= 365


class TestMinimalConfig:
    """minimal.env should have reasonable defaults."""

    @pytest.fixture
    def config(self):
        path = REPO_ROOT / "examples" / "minimal.env"
        if not path.exists():
            pytest.skip("minimal.env not found")
        return _parse_env_file(path)

    def test_has_auth_token(self, config):
        assert "GATEWAY_AUTH_TOKEN" in config

    def test_has_gateway_bind(self, config):
        assert config.get("GATEWAY_BIND") == "127.0.0.1"

    def test_has_gateway_port(self, config):
        assert "GATEWAY_PORT" in config

    def test_has_log_level(self, config):
        assert "LOG_LEVEL" in config


class TestRecommendedConfig:
    """recommended.env should balance security and usability."""

    @pytest.fixture
    def config(self):
        path = REPO_ROOT / "examples" / "recommended.env"
        if not path.exists():
            pytest.skip("recommended.env not found")
        return _parse_env_file(path)

    def test_pii_enabled(self, config):
        assert config.get("PII_REDACTION", "").lower() == "true"

    def test_approval_queue_enabled(self, config):
        assert config.get("APPROVAL_QUEUE", "").lower() == "true"

    def test_kill_switch_enabled(self, config):
        assert config.get("KILL_SWITCH_ENABLED", "").lower() == "true"

    def test_tailscale_enabled(self, config):
        assert config.get("TAILSCALE", "").lower() == "true"

    def test_ssh_requires_approval(self, config):
        assert config.get("SSH_REQUIRE_APPROVAL", "").lower() == "true"


class TestConfigValidation:
    """GatewayConfig validation behavior."""

    def test_invalid_router_url_rejected(self):
        from gateway.ingest_api.config import RouterConfig

        with pytest.raises(Exception):
            RouterConfig(default_url="ftp://evil.com")

    def test_router_url_must_be_localhost_or_openclaw(self):
        from gateway.ingest_api.config import RouterConfig

        with pytest.raises(Exception):
            RouterConfig(default_url="http://attacker.com:8080")

    def test_valid_router_url_accepted(self):
        from gateway.ingest_api.config import RouterConfig

        config = RouterConfig(default_url="http://localhost:8080")
        assert config.default_url == "http://localhost:8080"

    def test_invalid_target_url_rejected(self):
        from gateway.ingest_api.config import RouterConfig

        with pytest.raises(Exception):
            RouterConfig(targets={"evil": "http://evil.com:1234"})

    def test_empty_content_rejected(self):
        from gateway.ingest_api.models import ForwardRequest

        with pytest.raises(Exception):
            ForwardRequest(content="   ", source="api")

    def test_invalid_source_rejected(self):
        from gateway.ingest_api.models import ForwardRequest

        with pytest.raises(Exception):
            ForwardRequest(content="hello", source="invalid_source")

    def test_valid_forward_request(self):
        from gateway.ingest_api.models import ForwardRequest

        req = ForwardRequest(content="hello", source="api")
        assert req.source == "api"


class TestAllExampleConfigsExist:
    """Verify all referenced example configs exist."""

    EXPECTED_FILES = [
        "examples/minimal.env",
        "examples/recommended.env",
        "examples/paranoid.env",
        "examples/docker-compose.minimal.yml",
        "examples/docker-compose.production.yml",
    ]

    @pytest.mark.parametrize("filepath", EXPECTED_FILES)
    def test_file_exists(self, filepath):
        path = REPO_ROOT / filepath
        assert path.exists(), f"Expected example file not found: {filepath}"
