# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
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
        path = REPO_ROOT / "docker" / "config" / "openclaw" / "apply-patches.js"
        if not path.exists():
            pytest.skip("apply-patches.js not available in this environment")
        script = path.read_text()
        assert "process.exit(1)" not in script
        assert "corrupt-" in script
        assert "moved to" in script

    def test_openclaw_patch_script_removes_legacy_gateway_model_key(self):
        """openclaw init patch script must remove unsupported gateway.model key."""
        path = REPO_ROOT / "docker" / "config" / "openclaw" / "apply-patches.js"
        if not path.exists():
            pytest.skip("apply-patches.js not available in this environment")
        script = path.read_text()
        assert "Removed unsupported key gateway.model" in script
        assert "Set internal gateway model" not in script

    def test_openclaw_version_pin_is_consistent_across_bot_images(self):
        """Both bot Dockerfiles must pin OpenClaw to the same value
        (either both a specific version or both @latest)."""
        import re

        primary_path = REPO_ROOT / "docker" / "Dockerfile.agentshroud"
        openclaw_path = REPO_ROOT / "docker" / "bots" / "openclaw" / "Dockerfile"
        if not primary_path.exists() or not openclaw_path.exists():
            pytest.skip("Bot Dockerfiles not available in this environment")
        primary = primary_path.read_text()
        openclaw = openclaw_path.read_text()

        # Accept either a pinned version (YYYY.MM.NN) or the literal "latest".
        pat = re.compile(r"openclaw@([0-9]{4}\.[0-9]+\.[0-9]+|latest)")
        primary_match = pat.search(primary)
        openclaw_match = pat.search(openclaw)

        assert primary_match, "Primary bot Dockerfile must pin openclaw@<version|latest>"
        assert openclaw_match, "OpenClaw bot Dockerfile must pin openclaw@<version|latest>"
        assert primary_match.group(1) == openclaw_match.group(1), (
            f"OpenClaw pin drift: primary={primary_match.group(1)} "
            f"openclaw={openclaw_match.group(1)}"
        )

    def test_openclaw_patch_script_sets_control_ui_allowed_origins(self):
        """openclaw init patch script must seed control UI origins for non-loopback bind."""
        path = REPO_ROOT / "docker" / "config" / "openclaw" / "apply-patches.js"
        if not path.exists():
            pytest.skip("apply-patches.js not available in this environment")
        script = path.read_text()
        assert "gateway.controlUi.allowedOrigins" in script
        assert "dangerouslyAllowHostHeaderOriginFallback" in script

    def test_openclaw_patch_script_seeds_group_allowlist(self):
        """openclaw init patch script must seed Telegram group allowlist when policy is allowlist."""
        path = REPO_ROOT / "docker" / "config" / "openclaw" / "apply-patches.js"
        if not path.exists():
            pytest.skip("apply-patches.js not available in this environment")
        script = path.read_text()
        assert "groupPolicy" in script
        assert "groupAllowFrom" in script
        assert "allowlist" in script

    def test_openclaw_patch_script_uses_multi_group_allowlist_var(self):
        """apply-patches.js must reference AGENTSHROUD_GROUP_CHAT_IDS (multi-group).

        Regression: SCRUM-45 — legacy single-ID var only supported one group. The new
        var is comma-separated and supports an allowlist of arbitrary groups.
        """
        path = REPO_ROOT / "docker" / "config" / "openclaw" / "apply-patches.js"
        if not path.exists():
            pytest.skip("apply-patches.js not available in this environment")
        script = path.read_text()
        assert "AGENTSHROUD_GROUP_CHAT_IDS" in script, (
            "Multi-group allowlist env var must be referenced in apply-patches.js"
        )
        # Script must split on comma to support multiple IDs
        assert "split" in script, "Script must split comma-separated chat IDs"
        # Legacy single-ID var must still be accepted for backward compat
        assert "AGENTSHROUD_GROUP_CHAT_ID" in script, (
            "Legacy single-ID var must be kept for backward compat"
        )

    def test_openclaw_patch_script_emits_per_chat_group_agents(self):
        """apply-patches.js must create per-chat group-{chatId} agents for the approval router.

        gateway/approval_queue/group_router.py expects agent ids of the form "group-{chat_id}"
        so it can extract the numeric chat id. The old static "group-project" id broke this.
        """
        path = REPO_ROOT / "docker" / "config" / "openclaw" / "apply-patches.js"
        if not path.exists():
            pytest.skip("apply-patches.js not available in this environment")
        script = path.read_text()
        # Script must build dynamic "group-{chatId}" agent ids
        assert "group-${" in script or "`group-${" in script, (
            "Script must emit per-chat group-{chatId} agent IDs for approval router compat"
        )
        # Script must remove stale bindings when chat IDs leave the allowlist
        assert "stale" in script.lower(), (
            "Script must clean up stale group bindings on config volume restart"
        )

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

    def test_lifespan_op_prewarm_guarded_against_pytest(self):
        """The 1Password prewarm thread must never spawn real op subprocesses under pytest."""
        source = (REPO_ROOT / "gateway" / "ingest_api" / "lifespan.py").read_text()
        guard_pos = source.index('"PYTEST_CURRENT_TEST" not in os.environ')
        thread_pos = source.index("threading.Thread(target=_prewarm_op")
        assert guard_pos < thread_pos, "pytest guard must gate the op prewarm thread"

    def test_startup_wrapper_defaults_openclaw_bind_to_loopback(self):
        """Startup wrapper should default OpenClaw bind to loopback unless explicitly overridden."""
        path = REPO_ROOT / "docker" / "scripts" / "start-agentshroud.sh"
        if not path.exists():
            pytest.skip("start-agentshroud.sh not available in this environment")
        script = path.read_text()
        assert 'OPENCLAW_BIND_MODE="${OPENCLAW_GATEWAY_BIND:-loopback}"' in script
        # The invocation was updated to pass --stack-size via node directly (ARM64 stack overflow fix).
        # Assert the bind flag is passed regardless of the exact invocation form.
        assert '--bind "${OPENCLAW_BIND_MODE}"' in script

    def test_main_compose_sets_openclaw_bind_lan_default(self):
        """Primary compose stack should bind OpenClaw gateway to lan by default for host Control UI access."""
        compose = (REPO_ROOT / "docker" / "docker-compose.yml").read_text()
        assert "OPENCLAW_GATEWAY_BIND=${OPENCLAW_GATEWAY_BIND:-lan}" in compose

    def test_startup_notifications_use_minimal_message_format(self):
        """Startup/shutdown notifications should use minimal, non-identifying text."""
        path = REPO_ROOT / "docker" / "scripts" / "start-agentshroud.sh"
        if not path.exists():
            pytest.skip("start-agentshroud.sh not available in this environment")
        script = path.read_text()
        assert "🟡 OpenClaw starting" in script
        assert "🛡️ OpenClaw online" in script
        assert "🟠 OpenClaw starting (readiness delayed)" in script
        assert "🔴 OpenClaw shutting down" in script

    def test_startup_notifications_wait_for_runtime_readiness(self):
        """Startup script should verify Telegram/model readiness before sending online notice."""
        path = REPO_ROOT / "docker" / "scripts" / "start-agentshroud.sh"
        if not path.exists():
            pytest.skip("start-agentshroud.sh not available in this environment")
        script = path.read_text()
        assert "_telegram_get_me_ready" in script
        assert "_model_runtime_ready" in script
        assert "/getMe" in script
        assert "/api/tags" in script
        assert 'ready="no"' in script
        assert "for _i in $(seq 1 60)" in script

    def test_startup_online_notice_sent_only_after_readiness_gate(self):
        """Online notice must appear after readiness probes to avoid premature status signals."""
        path = REPO_ROOT / "docker" / "scripts" / "start-agentshroud.sh"
        if not path.exists():
            pytest.skip("start-agentshroud.sh not available in this environment")
        script = path.read_text()
        assert script.index('ready="no"') < script.index('if [ "${ready}" = "yes" ]; then')
        assert script.index("_telegram_get_me_ready") < script.index(
            'if [ "${ready}" = "yes" ]; then'
        )
        assert script.index("_model_runtime_ready") < script.index(
            'if [ "${ready}" = "yes" ]; then'
        )
        assert script.index("🟡 OpenClaw starting") < script.index("🛡️ OpenClaw online")

    def test_startup_telegram_calls_use_system_header(self):
        """Startup notification Telegram calls should be marked as system-originated."""
        script_path = REPO_ROOT / "docker" / "scripts" / "start-agentshroud.sh"
        if not script_path.exists():
            pytest.skip("startup scripts not available in this environment")
        script = script_path.read_text()
        assert "X-AgentShroud-System: 1" in script
        assert "/getMe" in script

    def test_hermes_startup_telegram_calls_use_system_header(self):
        """Hermes startup notifications must use X-AgentShroud-System: 1 (bypasses content filter)."""
        hermes_path = REPO_ROOT / "docker" / "bots" / "hermes" / "start.sh"
        if not hermes_path.exists():
            pytest.skip("hermes/start.sh not available in this environment")
        script = hermes_path.read_text()
        assert "X-AgentShroud-System: 1" in script, "Hermes startup must set system-message header"
        assert "/getMe" in script, "Hermes startup must poll getMe readiness"
        assert "🟡 Hermes starting" in script, "Must send starting notification"
        assert "🛡️ Hermes online" in script, "Must send online notification"
        assert "🔴 Hermes shutting down" in script, "Must send shutdown notification"
        assert "🟠 Hermes starting (readiness delayed)" in script, "Must handle delayed readiness"
        assert (
            "TRAP" not in script or "trap" in script
        ), "Must set TERM/INT trap for shutdown notification"
        assert (
            "hermes gateway run &" in script
        ), "Must run hermes in background (not exec) to enable trap"
        assert "wait" in script, "Must wait on background hermes PID"
        assert (
            "_STARTUP_NOTICE_STAMP" in script
        ), "Must use cooldown stamp to suppress duplicate notifications"

    def test_hermes_dockerfile_installs_xxd(self):
        """Hermes Dockerfile must install xxd — terminal_tool hex dumps fail without it."""
        import re

        path = REPO_ROOT / "docker" / "bots" / "hermes" / "Dockerfile"
        if not path.exists():
            pytest.skip("hermes Dockerfile not available in this environment")
        dockerfile = path.read_text()
        install_block = re.search(r"apt-get install\b.*?(?=&&)", dockerfile, re.S)
        assert install_block, "Hermes Dockerfile must have an apt-get install block"
        assert re.search(
            r"\bxxd\b", install_block.group(0)
        ), "Hermes Dockerfile must install xxd (upstream image lacks it; tool exec errors)"

    def test_hermes_openai_api_key_wired_via_secret(self):
        """Hermes must receive OPENAI_API_KEY from the shared openai_api_key Docker secret.

        Hermes routes all OpenAI calls through the gateway (OPENAI_BASE_URL),
        but its client rebuild logs 'missing OPENAI_API_KEY' warnings unless
        the env var is present. The injector script and compose must agree.
        """
        import yaml

        secrets_path = REPO_ROOT / "docker" / "bots" / "hermes" / "agentshroud-secrets.sh"
        compose_path = REPO_ROOT / "docker" / "docker-compose.yml"
        if not secrets_path.exists() or not compose_path.exists():
            pytest.skip("hermes secrets script or compose file not available")

        script = secrets_path.read_text()
        assert "inject OPENAI_API_KEY" in script, "Injector must export OPENAI_API_KEY"
        assert (
            "/run/secrets/openai_api_key" in script
        ), "Injector must read the openai_api_key Docker secret"

        compose = yaml.safe_load(compose_path.read_text())
        hermes_secrets = compose["services"]["hermes"].get("secrets", [])
        assert (
            "openai_api_key" in hermes_secrets
        ), "hermes service must mount the openai_api_key secret"
        assert "openai_api_key" in compose.get(
            "secrets", {}
        ), "compose must define the openai_api_key secret"

    def test_hermes_dashboard_insecure_optin_is_loopback_bounded(self):
        """HERMES_DASHBOARD_INSECURE may only be enabled with a loopback-only host publish.

        hermes-agent v0.15.1+ fails closed on non-loopback dashboard binds without an
        OAuth provider. We opt in to the pre-gate behaviour, which is only acceptable
        while the host port publish stays 127.0.0.1-bound and the service stays on the
        internal isolated network.
        """
        import yaml

        compose_path = REPO_ROOT / "docker" / "docker-compose.yml"
        if not compose_path.exists():
            pytest.skip("compose file not available in this environment")

        compose = yaml.safe_load(compose_path.read_text())
        hermes = compose["services"]["hermes"]
        env = hermes.get("environment", {})
        if str(env.get("HERMES_DASHBOARD_INSECURE", "")) not in ("1", "true"):
            pytest.skip("HERMES_DASHBOARD_INSECURE not enabled — nothing to bound")

        # 9119 reaches the host via the gateway's TCP forwarder publish, not hermes
        # itself (hermes sits on the internal isolated network and publishes nothing).
        gateway_ports = compose["services"]["gateway"].get("ports", [])
        dash_ports = [p for p in gateway_ports if ":9119" in str(p)]
        assert dash_ports, "dashboard port 9119 must be published via the gateway forwarder"
        for port in dash_ports:
            assert str(port).startswith(
                "127.0.0.1:"
            ), f"insecure dashboard requires loopback-only publish, got: {port}"
        networks = hermes.get("networks", [])
        net_names = networks if isinstance(networks, list) else list(networks)
        assert net_names and all(
            "isolated" in n for n in net_names
        ), f"insecure dashboard requires isolated-only networks, got: {net_names}"

    def test_patch_slack_sdk_pong_patch_is_idempotent(self):
        """patch-slack-sdk.sh must stay quiet when the pong patch is already applied.

        The script runs at image build AND every boot; without the
        already-patched guard it logs 'pattern not found' noise on every start.
        """
        path = REPO_ROOT / "docker" / "scripts" / "patch-slack-sdk.sh"
        if not path.exists():
            pytest.skip("patch-slack-sdk.sh not available in this environment")
        script = path.read_text()
        # Already-patched detection must come before the pattern-absent fallback.
        # Match the console.log markers specifically — bare substrings also appear
        # in the script's explanatory comment, which precedes both code branches.
        assert "pong timeout already patched" in script
        assert script.index("pong timeout already patched") < script.index(
            "pattern not found — skipped"
        )
        # Pattern-absent case must continue (informational skip), never fail the boot.
        assert "skipped, continuing" in script
        assert "exit 1" not in script

    def test_start_control_center_script_uses_repo_relative_exec(self):
        """Control center launcher should be robust to current working directory."""
        path = REPO_ROOT / "scripts" / "start-control-center"
        if not path.exists():
            pytest.skip("start-control-center not available in this environment")
        script = path.read_text()
        assert "set -euo pipefail" in script
        assert "REPO_ROOT" in script
        assert "exec python3 src/interfaces/text_control_center.py" in script

    def test_chat_console_script_uses_repo_relative_exec(self):
        """Chat console launcher should be robust to current working directory."""
        path = REPO_ROOT / "scripts" / "chat-console"
        if not path.exists():
            pytest.skip("chat-console not available in this environment")
        script = path.read_text()
        assert "set -euo pipefail" in script
        assert "REPO_ROOT" in script
        assert "exec python3 src/interfaces/chat_console.py" in script

    def test_switch_model_script_exists_with_supported_targets(self):
        """Model switch helper should support local and major cloud providers."""
        path = REPO_ROOT / "scripts" / "switch_model.sh"
        if not path.exists():
            pytest.skip("switch_model.sh not available in this environment")
        script = path.read_text()
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
        path = REPO_ROOT / "scripts" / "switch_model.sh"
        if not path.exists():
            pytest.skip("switch_model.sh not available in this environment")
        script = path.read_text()
        assert "scripts/switch_model.sh gemini" in script
        assert "scripts/switch_model.sh cloud gemini" not in script

    def test_openclaw_patch_defaults_to_qwen_local_model(self):
        """OpenClaw patch script should default to local Ollama but keep API adapter configurable."""
        path = REPO_ROOT / "docker" / "config" / "openclaw" / "apply-patches.js"
        if not path.exists():
            pytest.skip("apply-patches.js not available in this environment")
        script = path.read_text()
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
        assert "AGENTSHROUD_MODEL_MODE=${AGENTSHROUD_MODEL_MODE:-cloud}" in compose
        assert (
            "AGENTSHROUD_LOCAL_MODEL_REF=${AGENTSHROUD_LOCAL_MODEL_REF:-ollama/qwen3:14b}"
            in compose
        )
        assert (
            "AGENTSHROUD_CLOUD_MODEL_REF=${AGENTSHROUD_CLOUD_MODEL_REF:-anthropic/claude-opus-4-6}"
            in compose
        )
        assert "OLLAMA_BASE_URL=${OLLAMA_BASE_URL:-http://gateway:8080/v1}" in compose
        assert "OLLAMA_API_KEY=${OLLAMA_API_KEY:-ollama-local}" in compose

    def test_startup_script_skips_anthropic_when_local_model_selected(self):
        """Bot startup should not load Anthropic secrets when Ollama local model is configured."""
        path = REPO_ROOT / "docker" / "scripts" / "start-agentshroud.sh"
        if not path.exists():
            pytest.skip("start-agentshroud.sh not available in this environment")
        script = path.read_text()
        assert '[[ "${OPENCLAW_MAIN_MODEL:-}" == ollama/* ]]' in script
        assert "skipping Claude token load" in script
        assert "skipping Claude op-proxy fetch" in script
        assert "Loaded Google API key" in script

    def test_init_config_skips_anthropic_auth_seed_for_local_model(self):
        """Init config should seed auth profiles for cloud providers and Ollama in local mode."""
        path = REPO_ROOT / "docker" / "scripts" / "init-openclaw-config.sh"
        if not path.exists():
            pytest.skip("init-openclaw-config.sh not available in this environment")
        script = path.read_text()
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


    def test_hermes_soul_documents_ssh_hosts(self):
        """Hermes SOUL.md must document all three lab hosts and the gateway /ssh/exec recipe.

        This test guards the persona template against silent drift — SOUL.md seeding is
        one-shot (init-config.sh:44-45), so a template regression would only surface after
        a volume reset.
        """
        path = REPO_ROOT / "docker" / "config" / "hermes" / "SOUL.md"
        if not path.exists():
            pytest.skip("hermes SOUL.md not available in this environment")
        soul = path.read_text()
        # All three lab hosts by canonical name (gateway resolves; raw IPs must not be sole ref)
        assert "marvin" in soul, "SOUL.md must document marvin host"
        assert "trillian" in soul, "SOUL.md must document trillian host"
        assert "raspberrypi" in soul, "SOUL.md must document raspberrypi host"
        # SSH user
        assert "agentshroud-bot" in soul, "SOUL.md must specify agentshroud-bot SSH user"
        # Gateway REST recipe (both the endpoint and the auth header pattern)
        assert "http://gateway:8080/ssh/exec" in soul, "SOUL.md must include /ssh/exec endpoint"
        assert "Authorization: Bearer" in soul, "SOUL.md must include bearer-auth header"
        # Proxy-bypass flag — required because HTTP_PROXY=gateway:8181 is set in the container
        assert "--noproxy gateway" in soul, "SOUL.md must include --noproxy gateway flag"

    def test_hermes_soul_has_no_refuse_directive(self):
        """Hermes SOUL.md must instruct the agent never to issue a blanket 'cannot connect' refusal.

        The directive must be honest (attempt + report real error), not silencing — the bot
        must not fabricate success or hide genuine failures.
        """
        path = REPO_ROOT / "docker" / "config" / "hermes" / "SOUL.md"
        if not path.exists():
            pytest.skip("hermes SOUL.md not available in this environment")
        soul = path.read_text()
        assert "cannot connect" in soul, "SOUL.md must contain the no-refuse directive text"
        assert "Never reply" in soul or "never reply" in soul, (
            "SOUL.md must explicitly instruct the agent never to give a blanket refusal"
        )

    def test_openclaw_soul_has_no_refuse_directive(self):
        """OpenClaw SOUL.md must carry the same 'never blanket-refuse cannot connect' directive.

        Both bot personas must be consistent so neither emits a canned refusal when SSH is
        attempted against a known-configured host.
        """
        path = REPO_ROOT / "docker" / "config" / "openclaw" / "workspace" / "SOUL.md"
        if not path.exists():
            pytest.skip("openclaw SOUL.md not available in this environment")
        soul = path.read_text()
        assert "cannot connect" in soul, "OpenClaw SOUL.md must contain the no-refuse directive"
        assert "Never reply" in soul or "never reply" in soul, (
            "OpenClaw SOUL.md must explicitly instruct the agent never to give a blanket refusal"
        )


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
