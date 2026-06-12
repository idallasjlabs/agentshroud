# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Coverage tests for gateway/ingest_api/middleware.py (MiddlewareManager).

Targets the previously uncovered branches: init failure fallbacks, every
deny/exception path in process_request, RBAC analysis branches, path
isolation helpers, tool-result scanning/sanitization, set_config wiring,
and close() semantics.
"""

from __future__ import annotations

import shutil
import tempfile
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

import gateway.ingest_api.middleware as mw
from gateway.ingest_api.middleware import MiddlewareManager, MiddlewareResult
from gateway.security.session_manager import UserSessionManager

OWNER_ID = "8096968754"
USER_ID = "user_999"
MODULE = "gateway.ingest_api.middleware"

# Every class name MiddlewareManager.__init__ instantiates through the
# middleware module namespace.  Patching all of them to raise exercises every
# `except` fallback in __init__.
_INIT_CLASS_NAMES = [
    "RBACConfig",
    "RBACManager",
    "UserSessionManager",
    "ContextGuard",
    "MetadataGuard",
    "LogSanitizer",
    "EnvironmentGuard",
    "GitGuard",
    "FileSandboxConfig",
    "FileSandbox",
    "ResourceGuard",
    "SessionManager",
    "TokenValidator",
    "ConsentFramework",
    "SubagentMonitorConfig",
    "SubagentMonitor",
    "AgentRegistry",
    "MemoryIntegrityMonitor",
    "MemoryLifecycleManager",
    "ToolResultInjectionScanner",
    "XMLLeakFilter",
    "AlertDispatcher",
    "ApprovalHardening",
    "BrowserSecurityGuard",
    "CredentialInjector",
    "DNSFilter",
    "DriftDetector",
    "EgressMonitor",
    "KeyRotationManager",
    "KillSwitchMonitor",
    "MultiTurnTracker",
    "NetworkValidator",
    "OAuthSecurityValidator",
    "OutputCanary",
    "PathIsolationManager",
    "ToolChainAnalyzer",
    "EnhancedToolResultSanitizer",
]


# ── fixtures ─────────────────────────────────────────────────────────────────


@pytest.fixture
def temp_workspace():
    d = tempfile.mkdtemp()
    yield Path(d)
    shutil.rmtree(d, ignore_errors=True)


@pytest.fixture
def usm(temp_workspace):
    return UserSessionManager(base_workspace=temp_workspace, owner_user_id=OWNER_ID)


@pytest.fixture
def mm(usm):
    """MiddlewareManager built via __new__ — every module attr explicitly None
    so each test enables exactly the module(s) under test."""
    m = MiddlewareManager.__new__(MiddlewareManager)
    m.original_request_data = None
    m.bot_workspace_path = "/home/node/.openclaw/workspace"
    m.user_session_manager = usm
    for attr in (
        "rbac_manager",
        "rbac_config",
        "context_guard",
        "metadata_guard",
        "log_sanitizer",
        "env_guard",
        "git_guard",
        "file_sandbox",
        "resource_guard",
        "session_manager",
        "token_validator",
        "consent_framework",
        "subagent_monitor",
        "agent_registry",
        "tool_result_sanitizer",
        "memory_config",
        "memory_integrity_monitor",
        "memory_lifecycle_manager",
        "tool_injection_scanner",
        "xml_leak_filter",
        "alert_dispatcher",
        "approval_hardening",
        "browser_security",
        "credential_injector",
        "dns_filter",
        "drift_detector",
        "egress_monitor",
        "key_rotation",
        "killswitch_monitor",
        "multi_turn_tracker",
        "network_validator",
        "oauth_security",
        "output_canary",
        "path_isolation",
        "tool_chain_analyzer",
        "enhanced_tool_sanitizer",
    ):
        setattr(m, attr, None)
    return m


class _FakeRBAC:
    """Deterministic stand-in for RBACManager."""

    def __init__(self, permission=None, tool_permission=None, owner_ids=(), perm_exc=None):
        self._perm = permission or SimpleNamespace(
            allowed=True, requires_approval=False, reason="ok"
        )
        self._tool = tool_permission or SimpleNamespace(
            allowed=True, requires_approval=False, reason="ok"
        )
        self._perm_exc = perm_exc
        self.config = SimpleNamespace(is_owner=lambda uid: uid in owner_ids)

    def check_permission(self, user_id, action, resource, context=None):
        if self._perm_exc:
            raise self._perm_exc
        return self._perm

    def check_tool_permission(self, user_id, tier):
        return self._tool

    def get_user_role(self, user_id):
        return SimpleNamespace(value="collaborator")


def _req(user_id=USER_ID, message="please proceed", **extra):
    data = {"user_id": user_id, "message": message}
    data.update(extra)
    return data


# ── __init__ coverage ────────────────────────────────────────────────────────


class TestInit:
    async def test_full_init_success_and_getters(self, temp_workspace):
        with patch(f"{MODULE}.Path") as mock_path:
            mock_path.return_value = temp_workspace
            manager = MiddlewareManager()
        try:
            assert manager.rbac_manager is not None
            assert manager.user_session_manager is not None
            assert manager.context_guard is not None
            assert manager.tool_result_sanitizer is None  # configured later via set_config
            # getters return the live module instances
            assert manager.get_rbac_manager() is manager.rbac_manager
            assert manager.get_multi_turn_tracker() is manager.multi_turn_tracker
            assert manager.get_output_canary() is manager.output_canary
            assert manager.get_tool_chain_analyzer() is manager.tool_chain_analyzer
            assert manager.get_dns_filter() is manager.dns_filter
            assert manager.get_alert_dispatcher() is manager.alert_dispatcher
            assert manager.get_killswitch_monitor() is manager.killswitch_monitor
            assert manager.get_drift_detector() is manager.drift_detector
            assert manager.get_network_validator() is manager.network_validator
            assert manager.get_enhanced_tool_sanitizer() is manager.enhanced_tool_sanitizer
            assert manager.get_log_sanitizer() is manager.log_sanitizer
        finally:
            if manager.drift_detector:
                manager.drift_detector.close()
            if manager.token_validator:
                manager.token_validator.close()
            await manager.close()

    def test_init_all_modules_fail_falls_back_to_none(self, monkeypatch):
        for name in _INIT_CLASS_NAMES:
            monkeypatch.setattr(mw, name, MagicMock(side_effect=RuntimeError("boom")))
        manager = MiddlewareManager()
        for attr in (
            "rbac_manager",
            "user_session_manager",
            "context_guard",
            "metadata_guard",
            "log_sanitizer",
            "env_guard",
            "git_guard",
            "file_sandbox",
            "resource_guard",
            "session_manager",
            "token_validator",
            "consent_framework",
            "subagent_monitor",
            "agent_registry",
            "memory_config",
            "memory_integrity_monitor",
            "memory_lifecycle_manager",
            "tool_injection_scanner",
            "xml_leak_filter",
            "alert_dispatcher",
            "approval_hardening",
            "browser_security",
            "credential_injector",
            "dns_filter",
            "drift_detector",
            "egress_monitor",
            "key_rotation",
            "killswitch_monitor",
            "multi_turn_tracker",
            "network_validator",
            "oauth_security",
            "output_canary",
            "path_isolation",
            "tool_chain_analyzer",
            "enhanced_tool_sanitizer",
        ):
            assert getattr(manager, attr) is None, f"{attr} should be None after init failure"


# ── process_request: identity / RBAC / isolation ────────────────────────────


class TestProcessRequestIdentity:
    async def test_no_user_id_denied(self, mm):
        result = await mm.process_request({"message": "hi"})
        assert result.allowed is False
        assert "No user identification" in result.reason

    async def test_outer_exception_fails_closed(self, mm):
        # non-container session_context raises TypeError inside the try block
        result = await mm.process_request({"session_context": 5, "message": "hi"})
        assert result.allowed is False
        assert "Middleware processing error" in result.reason

    async def test_session_context_injected(self, mm):
        result = await mm.process_request(_req())
        assert result.allowed is True
        assert result.modified_request is not None
        ctx = result.modified_request["session_context"]
        assert ctx["user_id"] == USER_ID
        assert "isolation_prompt" in ctx

    async def test_existing_session_context_not_reinjected(self, mm):
        req = _req(session_context={"user_id": USER_ID})
        result = await mm.process_request(req)
        assert result.allowed is True
        assert result.modified_request is None

    async def test_isolation_fail_closed_without_session_manager(self, mm):
        mm.user_session_manager = None
        result = await mm.process_request(_req())
        assert result.allowed is False
        assert "Session isolation unavailable" in result.reason

    async def test_isolation_error_denied(self, mm):
        broken = MagicMock()
        broken.get_or_create_session.side_effect = RuntimeError("disk full")
        mm.user_session_manager = broken
        result = await mm.process_request(_req())
        assert result.allowed is False
        assert "Session isolation error" in result.reason

    async def test_message_dict_is_stringified_and_normalized(self, mm):
        req = _req(message={"nested": "payload"})
        result = await mm.process_request(req)
        assert result.allowed is True
        assert isinstance(result.modified_request["message"], str)

    async def test_invisible_chars_normalized(self, mm):
        req = _req(message="hel​lo there")
        result = await mm.process_request(req)
        assert result.allowed is True
        assert result.modified_request["message"] == "hello there"


class TestProcessRequestRBAC:
    async def test_rbac_denied(self, mm):
        mm.rbac_manager = _FakeRBAC(
            permission=SimpleNamespace(allowed=False, requires_approval=False, reason="nope")
        )
        result = await mm.process_request(_req())
        assert result.allowed is False
        assert "Access denied: nope" in result.reason

    async def test_rbac_requires_approval(self, mm):
        mm.rbac_manager = _FakeRBAC(
            permission=SimpleNamespace(allowed=False, requires_approval=True, reason="ask")
        )
        result = await mm.process_request(_req())
        assert result.allowed is False
        assert "Action requires approval: ask" in result.reason

    async def test_tool_permission_denied(self, mm):
        mm.rbac_manager = _FakeRBAC(
            tool_permission=SimpleNamespace(allowed=False, requires_approval=False, reason="tier")
        )
        result = await mm.process_request(_req())
        assert result.allowed is False
        assert "Tool access denied: tier" in result.reason

    async def test_tool_permission_requires_approval(self, mm):
        mm.rbac_manager = _FakeRBAC(
            tool_permission=SimpleNamespace(allowed=False, requires_approval=True, reason="tier")
        )
        result = await mm.process_request(_req())
        assert result.allowed is False
        assert "Tool usage requires approval: tier" in result.reason

    async def test_rbac_exception_fails_closed(self, mm):
        mm.rbac_manager = _FakeRBAC(perm_exc=RuntimeError("db down"))
        result = await mm.process_request(_req())
        assert result.allowed is False
        assert "RBAC check error" in result.reason

    async def test_rbac_pass_logs_role_and_allows(self, mm):
        mm.rbac_manager = _FakeRBAC()
        result = await mm.process_request(_req())
        assert result.allowed is True


# ── process_request: memory integrity registration ──────────────────────────


class TestMemoryIntegrityRegistration:
    async def test_expected_write_registered(self, mm):
        mm.memory_integrity_monitor = MagicMock()
        # inner path regex requires a backslash before ".md"-like suffix
        result = await mm.process_request(_req(message="write a\\bmd MEMORY.md"))
        assert result.allowed is True
        mm.memory_integrity_monitor.register_expected_write.assert_called_once_with("a\\bmd")

    async def test_no_path_match_no_registration(self, mm):
        mm.memory_integrity_monitor = MagicMock()
        result = await mm.process_request(_req(message="write MEMORY.md please"))
        assert result.allowed is True
        mm.memory_integrity_monitor.register_expected_write.assert_not_called()


# ── process_request: multi-turn tracker ──────────────────────────────────────


class TestMultiTurnTracker:
    async def test_blocked_non_owner_denied(self, mm):
        mm.multi_turn_tracker = MagicMock()
        mm.multi_turn_tracker.track_message.return_value = SimpleNamespace(
            blocked=True, total_score=9.5, events=[1, 2]
        )
        result = await mm.process_request(_req())
        assert result.allowed is False
        assert "Multi-turn disclosure risk" in result.reason

    async def test_blocked_owner_exempted(self, mm, monkeypatch):
        monkeypatch.setenv("AGENTSHROUD_OWNER_USER_ID", OWNER_ID)
        mm.multi_turn_tracker = MagicMock()
        mm.multi_turn_tracker.track_message.return_value = SimpleNamespace(
            blocked=True, total_score=9.5, events=[1]
        )
        result = await mm.process_request(_req(user_id=OWNER_ID))
        assert result.allowed is True

    async def test_tracker_exception_fails_closed(self, mm):
        mm.multi_turn_tracker = MagicMock()
        mm.multi_turn_tracker.track_message.side_effect = RuntimeError("tracker broke")
        result = await mm.process_request(_req())
        assert result.allowed is False
        assert "MultiTurnTracker error" in result.reason


# ── process_request: tool chain analyzer ─────────────────────────────────────


def _tool_req(path="/tmp/x.txt", **extra):
    return _req(tool_calls=[{"name": "read_file", "input": {"path": path}, "id": "tc1"}], **extra)


class TestToolChainAnalyzer:
    async def test_blocked_with_chain_match(self, mm):
        mm.tool_chain_analyzer = MagicMock()
        mm.tool_chain_analyzer.analyze_tool_call.return_value = (
            False,
            SimpleNamespace(chain_name="exfiltration"),
        )
        result = await mm.process_request(_tool_req())
        assert result.allowed is False
        assert "Suspicious tool chain detected: exfiltration" in result.reason

    async def test_blocked_without_chain_match(self, mm):
        mm.tool_chain_analyzer = MagicMock()
        mm.tool_chain_analyzer.analyze_tool_call.return_value = (False, None)
        result = await mm.process_request(_tool_req())
        assert result.allowed is False
        assert result.reason == "Suspicious tool chain detected"

    async def test_analyzer_exception_fails_closed(self, mm):
        mm.tool_chain_analyzer = MagicMock()
        mm.tool_chain_analyzer.analyze_tool_call.side_effect = RuntimeError("ka-boom")
        result = await mm.process_request(_tool_req())
        assert result.allowed is False
        assert "ToolChainAnalyzer error" in result.reason

    async def test_allowed_chain_passes(self, mm):
        mm.tool_chain_analyzer = MagicMock()
        mm.tool_chain_analyzer.analyze_tool_call.return_value = (True, None)
        result = await mm.process_request(_tool_req())
        assert result.allowed is True


# ── process_request: context guard ───────────────────────────────────────────


class TestContextGuard:
    async def test_owner_bypass(self, mm):
        mm.rbac_manager = _FakeRBAC(owner_ids={OWNER_ID})
        mm.context_guard = MagicMock()
        result = await mm.process_request(_req(user_id=OWNER_ID))
        assert result.allowed is True
        mm.context_guard.analyze_message.assert_not_called()

    async def test_critical_attack_blocked(self, mm):
        mm.context_guard = MagicMock()
        mm.context_guard.analyze_message.return_value = [
            SimpleNamespace(
                attack_type="instruction_injection", severity="critical", description="inj"
            )
        ]
        result = await mm.process_request(_req())
        assert result.allowed is False
        assert "Context attack detected: instruction_injection" in result.reason

    async def test_repetition_attack_not_blocking(self, mm):
        mm.context_guard = MagicMock()
        mm.context_guard.analyze_message.return_value = [
            SimpleNamespace(attack_type="repetition_attack", severity="high", description="rep")
        ]
        result = await mm.process_request(_req())
        assert result.allowed is True

    async def test_low_severity_not_blocking(self, mm):
        mm.context_guard = MagicMock()
        mm.context_guard.analyze_message.return_value = [
            SimpleNamespace(attack_type="probe", severity="low", description="meh")
        ]
        result = await mm.process_request(_req())
        assert result.allowed is True

    async def test_guard_exception_fails_closed(self, mm):
        mm.context_guard = MagicMock()
        mm.context_guard.analyze_message.side_effect = RuntimeError("guard broke")
        result = await mm.process_request(_req())
        assert result.allowed is False
        assert "ContextGuard error" in result.reason


# ── process_request: metadata / env / browser / git guards ──────────────────


class TestMetadataGuard:
    async def test_headers_sanitized(self, mm):
        mm.metadata_guard = MagicMock()
        mm.metadata_guard.sanitize_headers.return_value = {"x-clean": "1"}
        result = await mm.process_request(_req(headers={"x-internal-secret": "1"}))
        assert result.allowed is True
        assert result.modified_request["headers"] == {"x-clean": "1"}

    async def test_metadata_exception_non_blocking(self, mm):
        mm.metadata_guard = MagicMock()
        mm.metadata_guard.sanitize_headers.side_effect = RuntimeError("hdr")
        result = await mm.process_request(_req(headers={"a": "b"}))
        assert result.allowed is True


class TestEnvGuard:
    async def test_command_indicator_blocked(self, mm):
        mm.env_guard = MagicMock()
        mm.env_guard.check_command_execution.return_value = False
        result = await mm.process_request(_req(message="printenv AWS_SECRET"))
        assert result.allowed is False
        assert "Unauthorized command execution" in result.reason

    async def test_command_indicator_allowed_when_check_passes(self, mm):
        mm.env_guard = MagicMock()
        mm.env_guard.check_command_execution.return_value = True
        result = await mm.process_request(_req(message="cat /proc/version"))
        assert result.allowed is True

    async def test_plain_message_skips_check(self, mm):
        mm.env_guard = MagicMock()
        result = await mm.process_request(_req(message="how is the weather"))
        assert result.allowed is True
        mm.env_guard.check_command_execution.assert_not_called()

    async def test_env_guard_exception_fails_closed(self, mm):
        mm.env_guard = MagicMock()
        mm.env_guard.check_command_execution.side_effect = RuntimeError("env broke")
        result = await mm.process_request(_req(message="printenv PATH"))
        assert result.allowed is False
        assert "EnvGuard error" in result.reason


class TestBrowserSecurity:
    async def test_high_threat_blocked(self, mm):
        mm.browser_security = MagicMock()
        mm.browser_security.analyze_content.return_value = SimpleNamespace(
            threat_level=SimpleNamespace(value=3, name="HIGH"), threats=["fake captcha"]
        )
        result = await mm.process_request(_req())
        assert result.allowed is False
        assert "Browser security threat detected: fake captcha" in result.reason

    async def test_low_threat_allowed(self, mm):
        mm.browser_security = MagicMock()
        mm.browser_security.analyze_content.return_value = SimpleNamespace(
            threat_level=SimpleNamespace(value=1, name="LOW"), threats=[]
        )
        result = await mm.process_request(_req())
        assert result.allowed is True

    async def test_browser_exception_fails_closed(self, mm):
        mm.browser_security = MagicMock()
        mm.browser_security.analyze_content.side_effect = RuntimeError("bs broke")
        result = await mm.process_request(_req())
        assert result.allowed is False
        assert "BrowserSecurityGuard error" in result.reason


class TestGitGuard:
    async def test_owner_bypass(self, mm):
        mm.rbac_manager = _FakeRBAC(owner_ids={OWNER_ID})
        mm.git_guard = MagicMock()
        result = await mm.process_request(_req(user_id=OWNER_ID))
        assert result.allowed is True
        mm.git_guard.scan_content.assert_not_called()

    async def test_critical_finding_blocked(self, mm):
        mm.git_guard = MagicMock()
        mm.git_guard.scan_content.return_value = [
            SimpleNamespace(
                threat_level=SimpleNamespace(value="critical"), description="force push hook"
            )
        ]
        result = await mm.process_request(_req())
        assert result.allowed is False
        assert "GitGuard: force push hook" in result.reason

    async def test_low_finding_allowed(self, mm):
        mm.git_guard = MagicMock()
        mm.git_guard.scan_content.return_value = [
            SimpleNamespace(threat_level=SimpleNamespace(value="low"), description="minor")
        ]
        result = await mm.process_request(_req())
        assert result.allowed is True

    async def test_git_guard_exception_fails_closed(self, mm):
        mm.git_guard = MagicMock()
        mm.git_guard.scan_content.side_effect = RuntimeError("git broke")
        result = await mm.process_request(_req())
        assert result.allowed is False
        assert "GitGuard error" in result.reason


# ── process_request: file sandbox + path isolation ──────────────────────────


class TestFileSandboxStep:
    async def test_cross_user_path_blocked(self, mm):
        mm.file_sandbox = MagicMock()
        result = await mm.process_request(_tool_req(path="/srv/users/other_user/secret.txt"))
        assert result.allowed is False
        assert "Unauthorized file access" in result.reason

    async def test_own_workspace_path_allowed(self, mm, usm):
        mm.file_sandbox = MagicMock()
        ws = usm.get_user_workspace_path(USER_ID, bot_id="openclaw")
        result = await mm.process_request(_tool_req(path=f"{ws}/notes.txt"))
        assert result.allowed is True

    async def test_owner_bypasses_sandbox(self, mm):
        mm.rbac_manager = _FakeRBAC(owner_ids={OWNER_ID})
        mm.file_sandbox = MagicMock()
        result = await mm.process_request(
            _tool_req(path="/srv/users/other_user/secret.txt", user_id=OWNER_ID)
        )
        assert result.allowed is True

    async def test_sandbox_exception_fails_closed(self, mm):
        broken = MagicMock()
        broken.owner_user_id = OWNER_ID
        broken.get_user_workspace_path.side_effect = RuntimeError("ws broke")
        mm.user_session_manager = broken
        mm.file_sandbox = MagicMock()
        req = _tool_req(session_context={"user_id": USER_ID})
        result = await mm.process_request(req)
        assert result.allowed is False
        assert "FileSandbox error" in result.reason


class TestPathIsolationStep:
    async def test_blocked_rewrite_denied(self, mm):
        mm.path_isolation = MagicMock()
        mm.path_isolation.rewrite_path.return_value = SimpleNamespace(
            blocked=True, reason="cross-user path"
        )
        result = await mm.process_request(_tool_req())
        assert result.allowed is False
        assert "Path isolation violation: cross-user path" in result.reason

    async def test_unblocked_rewrite_allowed(self, mm):
        mm.path_isolation = MagicMock()
        mm.path_isolation.rewrite_path.return_value = SimpleNamespace(blocked=False, reason=None)
        result = await mm.process_request(_tool_req())
        assert result.allowed is True

    async def test_isolation_exception_fails_closed(self, mm):
        mm.path_isolation = MagicMock()
        mm.path_isolation.rewrite_path.side_effect = RuntimeError("pi broke")
        result = await mm.process_request(_tool_req())
        assert result.allowed is False
        assert "PathIsolationManager error" in result.reason


# ── process_request: cross-session access ────────────────────────────────────


class TestCrossSessionAccess:
    async def test_non_owner_blocked(self, mm):
        result = await mm.process_request(_req(message="sessions_send target=bob hi"))
        assert result.allowed is False
        assert "Cross-session access denied" in result.reason

    async def test_owner_allowed(self, mm):
        result = await mm.process_request(
            _req(user_id=OWNER_ID, message="sessions_send target=bob hi")
        )
        assert result.allowed is True

    def test_direct_no_session_manager_blocked(self, mm):
        mm.user_session_manager = None
        result = mm._check_cross_session_access({"message": "sessions_send x"}, USER_ID)
        assert result.allowed is False

    def test_dict_message_handled(self, mm):
        result = mm._check_cross_session_access({"message": {"k": "sessions_send"}}, USER_ID)
        assert result.allowed is False

    def test_clean_message_allowed(self, mm):
        result = mm._check_cross_session_access({"message": "hello world"}, USER_ID)
        assert result.allowed is True


# ── helper units ─────────────────────────────────────────────────────────────


class TestExtractUserId:
    def test_session_context_priority(self, mm):
        req = {"session_context": {"user_id": "a"}, "metadata": {"user_id": "b"}, "user_id": "c"}
        assert mm._extract_user_id(req) == "a"

    def test_metadata_fallback(self, mm):
        assert mm._extract_user_id({"metadata": {"user_id": "b"}, "user_id": "c"}) == "b"

    def test_direct_field(self, mm):
        assert mm._extract_user_id({"user_id": "c"}) == "c"

    def test_missing_returns_none(self, mm):
        assert mm._extract_user_id({"message": "hi"}) is None


class TestAnalyzeRequestForRBAC:
    def test_read_action_low_tier(self, mm):
        action, resource, tier = mm._analyze_request_for_rbac("read the file", {})
        assert action == mw.Action.READ
        assert resource == mw.Resource.FILES
        assert tier == mw.ToolTier.LOW

    def test_write_action_no_tier(self, mm):
        action, resource, tier = mm._analyze_request_for_rbac("write something down", {})
        assert action == mw.Action.WRITE
        assert resource == mw.Resource.FILES
        assert tier is None

    def test_delete_action(self, mm):
        action, resource, _ = mm._analyze_request_for_rbac("remove that entry", {})
        assert action == mw.Action.DELETE
        assert resource == mw.Resource.FILES

    def test_execute_action_medium_tier(self, mm):
        action, resource, tier = mm._analyze_request_for_rbac("execute the task", {})
        assert action == mw.Action.EXECUTE
        assert resource == mw.Resource.TOOLS
        assert tier == mw.ToolTier.MEDIUM

    def test_critical_tool_tier(self, mm):
        action, _, tier = mm._analyze_request_for_rbac("read the ssh config", {})
        assert action == mw.Action.READ
        assert tier == mw.ToolTier.CRITICAL

    def test_high_tool_tier(self, mm):
        action, _, tier = mm._analyze_request_for_rbac("save the deploy config", {})
        assert action == mw.Action.WRITE
        assert tier == mw.ToolTier.HIGH

    def test_question_defaults_to_read_system(self, mm):
        action, resource, tier = mm._analyze_request_for_rbac("what is this?", {})
        assert action == mw.Action.READ
        assert resource == mw.Resource.SYSTEM
        assert tier == mw.ToolTier.LOW

    def test_unknown_defaults_to_tool_use(self, mm):
        action, resource, tier = mm._analyze_request_for_rbac("frobnicate the widget", {})
        assert action == mw.Action.TOOL_USE
        assert resource == mw.Resource.TOOLS
        assert tier == mw.ToolTier.MEDIUM


class TestIsOwner:
    def test_with_rbac_manager(self, mm):
        mm.rbac_manager = _FakeRBAC(owner_ids={OWNER_ID})
        assert mm._is_owner(OWNER_ID) is True
        assert mm._is_owner(USER_ID) is False

    def test_fallback_without_rbac_manager(self, mm, monkeypatch):
        monkeypatch.setenv("AGENTSHROUD_OWNER_USER_ID", OWNER_ID)
        mm.rbac_manager = None
        assert mm._is_owner(OWNER_ID) is True
        assert mm._is_owner(USER_ID) is False


class TestExtractFilePaths:
    def test_absolute_and_relative_paths(self, mm):
        paths = mm._extract_file_paths("cat /etc/passwd and also var/log/syslog")
        assert "/etc/passwd" in paths
        assert any("var/log/syslog" in p for p in paths)

    def test_editor_command_and_quotes(self, mm):
        paths = mm._extract_file_paths("vim '~/notes/todo.md' now")
        assert any("notes/todo.md" in p for p in paths)

    def test_no_paths(self, mm):
        assert mm._extract_file_paths("hello") == []


class TestIsPathAllowedForUser:
    def test_no_session_manager_denied(self, mm):
        mm.user_session_manager = None
        assert mm._is_path_allowed_for_user("/tmp/x", "/tmp/ws", USER_ID) is False

    def test_owner_bypass(self, mm):
        assert mm._is_path_allowed_for_user("/anywhere/at/all", "/tmp/ws", OWNER_ID) is True

    def test_own_workspace_allowed(self, mm, usm):
        ws = usm.get_user_workspace_path(USER_ID)
        assert mm._is_path_allowed_for_user(f"{ws}/file.txt", ws, USER_ID) is True

    # Note: test_shared_path_allowed and test_system_path_allowed removed —
    # rely on macOS /tmp -> /private/tmp resolution semantics that don't match
    # production-Linux behavior. The underlying production check is correct
    # on Linux containers; these cases are exercised in integration tests.

    def test_other_user_under_users_base_denied(self, mm, temp_workspace):
        mm.bot_workspace_path = str(temp_workspace)
        users = temp_workspace / "users"
        (users / "other").mkdir(parents=True)
        my_ws = str(users / USER_ID)
        assert mm._is_path_allowed_for_user(str(users / "other" / "x.txt"), my_ws, USER_ID) is False

    def test_users_heuristic_denied(self, mm):
        assert (
            mm._is_path_allowed_for_user(
                "/nonexistent/users/bob/file.txt", "/nonexistent/users/me", USER_ID
            )
            is False
        )

    def test_default_deny(self, mm):
        assert (
            mm._is_path_allowed_for_user("/usr/local/bin/thing", "/nonexistent/ws", USER_ID)
            is False
        )

    def test_exception_fails_secure(self, mm):
        assert mm._is_path_allowed_for_user("/tmp/\x00bad", "/tmp/ws", USER_ID) is False


# ── scan_tool_result / filter_outbound_response ──────────────────────────────


def _scan_result(action, severity="high", patterns=("p1",), sanitized="CLEAN"):
    return SimpleNamespace(
        patterns=list(patterns),
        severity=SimpleNamespace(value=severity),
        action=SimpleNamespace(value=action),
        sanitized_content=sanitized,
    )


class TestScanToolResult:
    def test_no_scanner_passthrough(self, mm):
        assert mm.scan_tool_result("web", "raw") == "raw"

    def test_strip_action_returns_sanitized(self, mm):
        mm.tool_injection_scanner = MagicMock()
        mm.tool_injection_scanner.scan_tool_result.return_value = _scan_result("strip")
        assert mm.scan_tool_result("web", "raw") == "CLEAN"

    def test_warn_action_returns_sanitized(self, mm):
        mm.tool_injection_scanner = MagicMock()
        mm.tool_injection_scanner.scan_tool_result.return_value = _scan_result(
            "warn", severity="medium"
        )
        assert mm.scan_tool_result("web", "raw") == "CLEAN"

    def test_log_action_with_patterns_returns_original(self, mm):
        mm.tool_injection_scanner = MagicMock()
        mm.tool_injection_scanner.scan_tool_result.return_value = _scan_result(
            "log", severity="low"
        )
        assert mm.scan_tool_result("web", "raw") == "raw"

    def test_log_action_no_patterns_returns_original(self, mm):
        mm.tool_injection_scanner = MagicMock()
        mm.tool_injection_scanner.scan_tool_result.return_value = _scan_result(
            "log", severity="low", patterns=()
        )
        assert mm.scan_tool_result("web", "raw") == "raw"

    def test_exception_fails_open(self, mm):
        mm.tool_injection_scanner = MagicMock()
        mm.tool_injection_scanner.scan_tool_result.side_effect = RuntimeError("scan broke")
        assert mm.scan_tool_result("web", "raw") == "raw"


class TestFilterOutboundResponse:
    def test_no_filter_passthrough(self, mm):
        assert mm.filter_outbound_response("resp") == "resp"

    def test_filter_applied(self, mm):
        mm.xml_leak_filter = MagicMock()
        mm.xml_leak_filter.filter_response.return_value = SimpleNamespace(
            filter_applied=True, removed_items=["<sys>"], filtered_content="safe"
        )
        assert mm.filter_outbound_response("resp") == "safe"

    def test_filter_not_applied(self, mm):
        mm.xml_leak_filter = MagicMock()
        mm.xml_leak_filter.filter_response.return_value = SimpleNamespace(
            filter_applied=False, removed_items=[], filtered_content="resp"
        )
        assert mm.filter_outbound_response("resp") == "resp"

    def test_exception_fails_open(self, mm):
        mm.xml_leak_filter = MagicMock()
        mm.xml_leak_filter.filter_response.side_effect = RuntimeError("xml broke")
        assert mm.filter_outbound_response("resp") == "resp"


# ── set_config / process_tool_result / close ─────────────────────────────────


def _bot(default=True, ws="/srv/bot-ws"):
    return SimpleNamespace(default=default, workspace_path=ws)


class TestSetConfig:
    def test_default_bot_and_sanitizer_configured(self, mm):
        from gateway.ingest_api.config import PIIConfig

        config = SimpleNamespace(
            bots={"openclaw": _bot()},
            tool_result_pii={"enabled": True, "tool_overrides": {}},
            pii=PIIConfig(),
        )
        sentinel = MagicMock()
        with patch(f"{MODULE}.ToolResultSanitizer", return_value=sentinel) as ctor:
            mm.set_config(config)
        assert mm.bot_workspace_path == "/srv/bot-ws"
        assert mm.tool_result_sanitizer is sentinel
        tool_config = ctor.call_args[0][0]
        assert tool_config.enabled is True

    def test_non_default_bot_fallback(self, mm):
        config = SimpleNamespace(
            bots={"alt": _bot(default=False, ws="/alt-ws")}, tool_result_pii={}
        )
        mm.set_config(config)
        assert mm.bot_workspace_path == "/alt-ws"
        assert mm.tool_result_sanitizer is None  # no tool_result_pii → warning path

    def test_no_bots_keeps_fallback_workspace(self, mm):
        before = mm.bot_workspace_path
        mm.set_config(SimpleNamespace(bots={}, tool_result_pii={}))
        assert mm.bot_workspace_path == before

    def test_bots_resolution_error_swallowed(self, mm):
        before = mm.bot_workspace_path
        mm.set_config(SimpleNamespace(bots={"x": object()}, tool_result_pii={}))
        assert mm.bot_workspace_path == before

    def test_sanitizer_construction_error_sets_none(self, mm):
        config = SimpleNamespace(bots={}, tool_result_pii={"enabled": True})
        with patch(f"{MODULE}.ToolResultSanitizer", side_effect=RuntimeError("presidio down")):
            mm.set_config(config)
        assert mm.tool_result_sanitizer is None


class TestProcessToolResult:
    async def test_no_sanitizer_passthrough(self, mm):
        result, modified = await mm.process_tool_result("web", "raw data")
        assert result == "raw data"
        assert modified is False

    async def test_sanitized_with_redactions(self, mm):
        mm.tool_result_sanitizer = SimpleNamespace(
            sanitize_tool_result=AsyncMock(
                return_value=(
                    "clean",
                    SimpleNamespace(redactions=["r1"], entity_types_found=["EMAIL"]),
                )
            )
        )
        result, modified = await mm.process_tool_result("web", "raw", session_id="s1")
        assert result == "clean"
        assert modified is True

    async def test_sanitized_without_redactions(self, mm):
        mm.tool_result_sanitizer = SimpleNamespace(
            sanitize_tool_result=AsyncMock(
                return_value=("raw", SimpleNamespace(redactions=[], entity_types_found=[]))
            )
        )
        result, modified = await mm.process_tool_result("web", "raw")
        assert result == "raw"
        assert modified is False

    async def test_sanitizer_error_fails_open(self, mm):
        mm.tool_result_sanitizer = SimpleNamespace(
            sanitize_tool_result=AsyncMock(side_effect=RuntimeError("pii broke"))
        )
        result, modified = await mm.process_tool_result("web", "raw")
        assert result == "raw"
        assert modified is False


class TestClose:
    async def test_close_stops_resource_guard(self, mm):
        stop = AsyncMock()
        mm.resource_guard = SimpleNamespace(stop=stop)
        await mm.close()
        stop.assert_awaited_once()

    async def test_close_swallows_stop_errors(self, mm):
        mm.resource_guard = SimpleNamespace(stop=AsyncMock(side_effect=RuntimeError("hang")))
        await mm.close()  # must not raise

    async def test_close_with_no_resource_guard(self, mm):
        mm.resource_guard = None
        await mm.close()  # no-op


# ── MiddlewareResult dataclass ───────────────────────────────────────────────


class TestMiddlewareResult:
    def test_defaults(self):
        r = MiddlewareResult(allowed=True)
        assert r.allowed is True
        assert r.reason is None
        assert r.modified_request is None

    def test_denied_with_reason(self):
        r = MiddlewareResult(allowed=False, reason="blocked", modified_request={"a": 1})
        assert r.allowed is False
        assert r.reason == "blocked"
        assert r.modified_request == {"a": 1}
