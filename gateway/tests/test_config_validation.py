# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

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

    def test_openclaw_patch_script_recovers_corrupt_json(self):
        """openclaw init patch script must quarantine malformed JSON instead of exiting."""
        script = (REPO_ROOT / "docker" / "config" / "openclaw" / "apply-patches.js").read_text()
        assert "process.exit(1)" not in script
        assert "corrupt-" in script
        assert "moved to" in script

    def test_openclaw_patch_script_removes_legacy_gateway_model_key(self):
        """openclaw init patch script must remove unsupported gateway.model key."""
        script = (REPO_ROOT / "docker" / "config" / "openclaw" / "apply-patches.js").read_text()
        assert "Removed unsupported key gateway.model" in script
        assert "Set internal gateway model" not in script



    def test_openclaw_version_pin_is_consistent_across_bot_images(self):
        """Both bot Dockerfiles must pin the same OpenClaw version."""
        import re

        primary = (REPO_ROOT / "docker" / "Dockerfile.agentshroud").read_text()
        openclaw = (REPO_ROOT / "docker" / "bots" / "openclaw" / "Dockerfile").read_text()

        primary_match = re.search(r"openclaw@([0-9]{4}\.[0-9]+\.[0-9]+)", primary)
        openclaw_match = re.search(r"openclaw@([0-9]{4}\.[0-9]+\.[0-9]+)", openclaw)

        assert primary_match, "Primary bot Dockerfile must pin openclaw@<version>"
        assert openclaw_match, "OpenClaw bot Dockerfile must pin openclaw@<version>"
        assert primary_match.group(1) == openclaw_match.group(1)
        assert primary_match.group(1) == "2026.3.8"
    def test_openclaw_patch_script_sets_control_ui_allowed_origins(self):
        """openclaw init patch script must seed control UI origins for non-loopback bind."""
        script = (REPO_ROOT / "docker" / "config" / "openclaw" / "apply-patches.js").read_text()
        assert "gateway.controlUi.allowedOrigins" in script
        assert "dangerouslyAllowHostHeaderOriginFallback" in script

    def test_openclaw_patch_script_seeds_group_allowlist(self):
        """openclaw init patch script must seed Telegram group allowlist when policy is allowlist."""
        script = (REPO_ROOT / "docker" / "config" / "openclaw" / "apply-patches.js").read_text()
        assert "groupPolicy" in script
        assert "groupAllowFrom" in script
        assert "allowlist" in script

    def test_lifespan_uvicorn_warning_filter_drops_invalid_http_noise(self):
        """Lifespan filter should suppress repeated malformed HTTP warning noise."""
        import logging
        from gateway.ingest_api.lifespan import _DropInvalidHTTPRequestFilter

        filt = _DropInvalidHTTPRequestFilter()
        noisy = logging.LogRecord(
            name="uvicorn.error",
            level=logging.WARNING,
            pathname=__file__,
            lineno=1,
            msg="Invalid HTTP request received.",
            args=(),
            exc_info=None,
        )
        legit = logging.LogRecord(
            name="uvicorn.error",
            level=logging.WARNING,
            pathname=__file__,
            lineno=1,
            msg="Something else happened.",
            args=(),
            exc_info=None,
        )
        assert filt.filter(noisy) is False
        assert filt.filter(legit) is True

    def test_proxy_allowed_network_default_includes_current_subnets(self):
        """Proxy CIDR fallback should include current 10.254 ranges plus legacy compatibility."""
        source = (REPO_ROOT / "gateway" / "ingest_api" / "main.py").read_text()
        assert "10.254.111.0/24" in source
        assert "10.254.112.0/24" in source

    def test_startup_wrapper_defaults_openclaw_bind_to_loopback(self):
        """Startup wrapper should default OpenClaw bind to loopback unless explicitly overridden."""
        script = (REPO_ROOT / "docker" / "scripts" / "start-agentshroud.sh").read_text()
        assert 'OPENCLAW_BIND_MODE="${OPENCLAW_GATEWAY_BIND:-loopback}"' in script
        assert 'openclaw gateway --allow-unconfigured --bind "${OPENCLAW_BIND_MODE}"' in script

    def test_main_compose_sets_openclaw_bind_lan_default(self):
        """Primary compose stack should bind OpenClaw gateway to lan by default for host Control UI access."""
        compose = (REPO_ROOT / "docker" / "docker-compose.yml").read_text()
        assert "OPENCLAW_GATEWAY_BIND=${OPENCLAW_GATEWAY_BIND:-lan}" in compose

    def test_startup_notifications_use_minimal_message_format(self):
        """Startup/shutdown notifications should use minimal, non-identifying text."""
        script = (REPO_ROOT / "docker" / "scripts" / "start-agentshroud.sh").read_text()
        assert '🟡 AgentShroud starting' in script
        assert '🛡️ AgentShroud online' in script
        assert '🟠 AgentShroud starting (readiness delayed)' in script
        assert '🔴 AgentShroud shutting down' in script

    def test_startup_notifications_wait_for_runtime_readiness(self):
        """Startup script should verify Telegram/model readiness before sending online notice."""
        script = (REPO_ROOT / "docker" / "scripts" / "start-agentshroud.sh").read_text()
        assert "_telegram_get_me_ready" in script
        assert "_model_runtime_ready" in script
        assert "/getMe" in script
        assert "/api/tags" in script
        assert "ready=\"no\"" in script
        assert "for _i in $(seq 1 60)" in script

    def test_openclaw_start_script_uses_two_phase_startup_notifications(self):
        """OpenClaw start script should send starting first, then online after readiness checks."""
        script = (REPO_ROOT / "docker" / "bots" / "openclaw" / "start.sh").read_text()
        assert '🟡 AgentShroud starting' in script
        assert '🛡️ AgentShroud online' in script
        assert '🟠 AgentShroud starting (readiness delayed)' in script
        assert "_telegram_get_me_ready" in script
        assert "_model_runtime_ready" in script
        assert "for _i in $(seq 1 60)" in script



    def test_startup_online_notice_sent_only_after_readiness_gate(self):
        """Online notice must appear after readiness probes to avoid premature status signals."""
        script = (REPO_ROOT / "docker" / "scripts" / "start-agentshroud.sh").read_text()
        assert script.index('ready="no"') < script.index('if [ "${ready}" = "yes" ]; then')
        assert script.index('_telegram_get_me_ready') < script.index('if [ "${ready}" = "yes" ]; then')
        assert script.index('_model_runtime_ready') < script.index('if [ "${ready}" = "yes" ]; then')
        assert script.index('🟡 AgentShroud starting') < script.index('🛡️ AgentShroud online')

    def test_openclaw_bot_start_script_online_notice_after_readiness_gate(self):
        """OpenClaw bot wrapper should send online notice only after readiness checks pass."""
        script = (REPO_ROOT / "docker" / "bots" / "openclaw" / "start.sh").read_text()
        assert script.index('ready="no"') < script.index('if [ "${ready}" = "yes" ]; then')
        assert script.index('_telegram_get_me_ready') < script.index('if [ "${ready}" = "yes" ]; then')
        assert script.index('_model_runtime_ready') < script.index('if [ "${ready}" = "yes" ]; then')
        assert script.index('🟡 AgentShroud starting') < script.index('🛡️ AgentShroud online')
    def test_startup_telegram_calls_use_system_header(self):
        """Startup notification Telegram calls should be marked as system-originated."""
        script = (REPO_ROOT / "docker" / "scripts" / "start-agentshroud.sh").read_text()
        bot_script = (REPO_ROOT / "docker" / "bots" / "openclaw" / "start.sh").read_text()
        assert "X-AgentShroud-System: 1" in script
        assert "X-AgentShroud-System: 1" in bot_script
        assert "/getMe" in script
        assert "/getMe" in bot_script

    def test_start_control_center_script_uses_repo_relative_exec(self):
        """Control center launcher should be robust to current working directory."""
        script = (REPO_ROOT / "scripts" / "start-control-center").read_text()
        assert "set -euo pipefail" in script
        assert "REPO_ROOT" in script
        assert "exec python3 src/interfaces/text_control_center.py" in script

    def test_chat_console_script_uses_repo_relative_exec(self):
        """Chat console launcher should be robust to current working directory."""
        script = (REPO_ROOT / "scripts" / "chat-console").read_text()
        assert "set -euo pipefail" in script
        assert "REPO_ROOT" in script
        assert "exec python3 src/interfaces/chat_console.py" in script

    def test_switch_model_script_exists_with_supported_targets(self):
        """Model switch helper should support local and major cloud providers."""
        script = (REPO_ROOT / "scripts" / "switch_model.sh").read_text()
        assert "switch_model.sh <target>" in script
        assert "[model_ref]" in script
        assert "--wait" in script
        assert "local" in script
        assert "gemini" in script
        assert "anthropic" in script
        assert "openai" in script
        assert "CUSTOM_MODEL_REF" in script
        assert "ensure_local_model_available" in script
        assert "docker compose" in script

    def test_switch_model_script_uses_current_target_syntax(self):
        """Operator guidance should use valid switch_model target syntax (no legacy cloud prefix)."""
        script = (REPO_ROOT / "scripts" / "switch_model.sh").read_text()
        assert "scripts/switch_model.sh gemini" in script
        assert "scripts/switch_model.sh cloud gemini" not in script

    def test_openclaw_patch_defaults_to_qwen_local_model(self):
        """OpenClaw patch script should default to local Ollama but keep API adapter configurable."""
        script = (REPO_ROOT / "docker" / "config" / "openclaw" / "apply-patches.js").read_text()
        assert "AGENTSHROUD_MODEL_MODE" in script
        assert "AGENTSHROUD_LOCAL_MODEL_REF" in script
        assert "AGENTSHROUD_CLOUD_MODEL_REF" in script
        assert "ollama/qwen3:14b" in script
        assert "config.models.providers.ollama" in script
        assert "OPENCLAW_OLLAMA_API" in script
        assert "api: OLLAMA_PROVIDER_API" in script
        assert "commands.ownerDisplay" in script
        assert "'hash'" in script
        assert "anthropic/claude-opus-4-6" in script
        assert "agents.defaults.model" in script or "config.agents.defaults.model" in script

    def test_compose_sets_qwen_local_model_overrides(self):
        """Main compose stack should expose a single model-mode switch with local/cloud refs."""
        compose = (REPO_ROOT / "docker" / "docker-compose.yml").read_text()
        assert "AGENTSHROUD_MODEL_MODE=${AGENTSHROUD_MODEL_MODE:-local}" in compose
        assert "AGENTSHROUD_LOCAL_MODEL_REF=${AGENTSHROUD_LOCAL_MODEL_REF:-ollama/qwen3:14b}" in compose
        assert "AGENTSHROUD_CLOUD_MODEL_REF=${AGENTSHROUD_CLOUD_MODEL_REF:-anthropic/claude-opus-4-6}" in compose
        assert "OLLAMA_BASE_URL=${OLLAMA_BASE_URL:-http://gateway:8080/v1}" in compose
        assert "OLLAMA_API_KEY=${OLLAMA_API_KEY:-ollama-local}" in compose

    def test_startup_script_skips_anthropic_when_local_model_selected(self):
        """Bot startup should not load Anthropic secrets when Ollama local model is configured."""
        script = (REPO_ROOT / "docker" / "scripts" / "start-agentshroud.sh").read_text()
        assert '[[ "${OPENCLAW_MAIN_MODEL:-}" == ollama/* ]]' in script
        assert "skipping Claude token load" in script
        assert "skipping Claude op-proxy fetch" in script
        assert "Loaded Google API key" in script

    def test_init_config_skips_anthropic_auth_seed_for_local_model(self):
        """Init config should seed auth profiles for cloud providers and Ollama in local mode."""
        script = (REPO_ROOT / "docker" / "scripts" / "init-openclaw-config.sh").read_text()
        assert "AGENTSHROUD_MODEL_MODE" in script
        assert "provider + ':default'" in script
        assert "version: Number(store.version || 1)" in script
        assert "setApiKey('google'" in script
        assert "setApiKey('openai'" in script
        assert "setApiKey('ollama'" in script
        assert "MODELS_JSON" in script
        assert "rawBaseUrl" in script
        assert "ROOT_AUTH_PROFILES" in script
        assert "ROOT_MODELS_JSON" in script
        assert "Registered Ollama provider/models in models.json" in script


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
