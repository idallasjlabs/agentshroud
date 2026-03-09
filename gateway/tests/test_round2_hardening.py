"""Tests for Round 2 hardening — 9 fixes."""
import os
import sys
import pytest
from unittest.mock import patch, MagicMock

# ── Fix 1: resource_guard fail-closed ────────────────────────────────────

class TestResourceGuardFailClosed:
    """Verify resource check methods return False (deny) on exception."""

    def test_check_cpu_limit_returns_false_on_exception(self):
        from gateway.security.resource_guard import ResourceGuard
        guard = ResourceGuard()
        guard.start_request_tracking("test-agent")
        # Patch psutil.Process to raise
        with patch("gateway.security.resource_guard.psutil.Process", side_effect=RuntimeError("boom")):
            result = guard.check_cpu_limit("test-agent")
        assert result is False, "check_cpu_limit must deny on exception"

    def test_check_memory_limit_returns_false_on_exception(self):
        from gateway.security.resource_guard import ResourceGuard
        guard = ResourceGuard()
        guard.start_request_tracking("test-agent")
        with patch("gateway.security.resource_guard.psutil.Process", side_effect=RuntimeError("boom")):
            result = guard.check_memory_limit("test-agent")
        assert result is False, "check_memory_limit must deny on exception"

    def test_check_disk_write_limit_returns_false_on_exception(self):
        from gateway.security.resource_guard import ResourceGuard
        guard = ResourceGuard()
        guard.start_request_tracking("test-agent")
        # Patch _get_disk_io_stats to raise
        with patch.object(guard, "_get_disk_io_stats", side_effect=RuntimeError("boom")):
            result = guard.check_disk_write_limit("test-agent")
        assert result is False, "check_disk_write_limit must deny on exception"


# ── Fix 2: file_sandbox default enforce ──────────────────────────────────

class TestFileSandboxDefaultEnforce:
    def test_default_mode_is_enforce(self):
        from gateway.security.file_sandbox import FileSandboxConfig
        cfg = FileSandboxConfig()
        assert cfg.mode == "enforce", f"Expected enforce, got {cfg.mode}"


# ── Fix 3: git_guard default enforce ─────────────────────────────────────

class TestGitGuardDefaultEnforce:
    def test_default_mode_is_enforce(self):
        from gateway.security.git_guard import GitGuard
        guard = GitGuard()
        assert guard.mode == "enforce", f"Expected enforce, got {guard.mode}"

    def test_scan_repository_default_enforce(self):
        from gateway.security.git_guard import scan_repository
        import tempfile, inspect
        # Check the default parameter value
        sig = inspect.signature(scan_repository)
        default = sig.parameters["mode"].default
        assert default == "enforce", f"Expected enforce, got {default}"


# ── Fix 4: egress_config from_environment() default enforce ──────────────

class TestEgressConfigDefaultEnforce:
    def test_from_environment_defaults_to_enforce(self):
        from gateway.security.egress_config import EgressFilterConfig
        # Clear env vars so defaults apply
        env = {k: v for k, v in os.environ.items() 
               if k not in ("AGENTSHROUD_MODE", "AGENTSHROUD_EGRESS_MODE")}
        with patch.dict(os.environ, env, clear=True):
            cfg = EgressFilterConfig.from_environment()
        assert cfg.mode == "enforce", f"Expected enforce, got {cfg.mode}"


# ── Fix 5: env_guard fail-open on parse exceptions ───────────────────────
# Text that fails shlex.split() cannot be a shell command; allow it through.
# Natural language with unmatched quotes (e.g. "What is AgentShroud?") must
# not be blocked by env_guard.

class TestEnvGuardFailOpen:
    def test_unparseable_text_is_allowed(self):
        from gateway.security.env_guard import EnvironmentGuard
        guard = EnvironmentGuard()
        # shlex.split raises on unterminated quotes — natural language, not a command
        result = guard.check_command_execution('echo "unterminated', "test-agent")
        assert result is True, "Unparseable text is not a shell command — must allow"

    def test_natural_language_question_is_allowed(self):
        from gateway.security.env_guard import EnvironmentGuard
        guard = EnvironmentGuard()
        result = guard.check_command_execution('What is AgentShroud?" — get an overview...', "test-agent")
        assert result is True, "Natural language questions must pass env_guard"


# ── Fix 6: DRY owner chat ID ────────────────────────────────────────────

class TestDRYOwnerChatID:
    def test_no_hardcoded_owner_id_in_lifespan(self):
        import gateway.ingest_api.lifespan as mod
        source = open(mod.__file__).read()
        # The string "8096968754" should NOT appear as a hardcoded value
        # (it may appear in comments, but not in admin_chat_id= or owner_chat_id=)
        import re
        hardcoded = re.findall(r'(?:admin_chat_id|owner_chat_id)\s*=\s*"8096968754"', source)
        assert len(hardcoded) == 0, f"Found hardcoded owner ID: {hardcoded}"


# ── Fix 7: LLM proxy endpoints (v0.9.0: proxy enabled, not 501) ──────────

class TestLLMProxyEndpoints:
    def test_v1_endpoint_is_defined(self):
        """The /v1/{path} endpoint must exist (enabled in v0.9.0)."""
        import gateway.ingest_api.main as mod
        source = open(mod.__file__).read()
        # v0.9.0 enables the LLM proxy — endpoint delegates to llm_proxy.proxy_messages
        assert "/v1/{path:path}" in source, "LLM proxy endpoint must be defined"
        assert "proxy_messages" in source, "LLM proxy must call proxy_messages"

    def test_llm_stats_endpoint_is_defined(self):
        """The /llm-proxy/stats endpoint must exist."""
        import gateway.ingest_api.main as mod
        source = open(mod.__file__).read()
        assert "llm_proxy_stats" in source, "LLM proxy stats endpoint must be defined"


# ── Fix 8: KeyVault dead code removed ───────────────────────────────────

class TestKeyVaultRemoved:
    def test_keyvault_not_instantiated(self):
        import gateway.ingest_api.lifespan as mod
        source = open(mod.__file__).read()
        assert "KeyVault(KeyVaultConfig())" not in source, "KeyVault should be removed"
        assert "KeyVault removed" in source or "key_vault" not in source.split("KeyVault removed")[0].split("# KeyVault")[-1]


# ── Fix 9: _notify_user_blocked reason sanitization ─────────────────────

class TestNotifyUserBlockedSanitization:
    def test_sanitize_reason_strips_module_paths(self):
        from gateway.proxy.telegram_proxy import TelegramAPIProxy
        reason = "Blocked by gateway.security.prompt_guard.PromptGuard: injection score 0.95"
        sanitized = TelegramAPIProxy._sanitize_reason(reason)
        assert "gateway.security.prompt_guard" not in sanitized
        assert "[internal]" in sanitized

    def test_sanitize_reason_strips_file_paths(self):
        from gateway.proxy.telegram_proxy import TelegramAPIProxy
        reason = "Error in /app/gateway/security/rbac.py line 42"
        sanitized = TelegramAPIProxy._sanitize_reason(reason)
        assert "/app/gateway/security/rbac.py" not in sanitized

    def test_sanitize_reason_preserves_simple_text(self):
        from gateway.proxy.telegram_proxy import TelegramAPIProxy
        reason = "RBAC: unauthorized user"
        sanitized = TelegramAPIProxy._sanitize_reason(reason)
        assert "RBAC" in sanitized
        assert "unauthorized" in sanitized
