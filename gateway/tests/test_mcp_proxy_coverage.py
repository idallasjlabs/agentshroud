# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Coverage tests for gateway/proxy/mcp_proxy.py.

Targets the branches not exercised by test_mcp_proxy.py: stdio/HTTP
connections (mocked at the subprocess/aiohttp boundary), connection pool,
egress target extraction, admin-private redaction, approval-queue gating,
tool execution error paths, passthrough execution, and event emission.
"""

from __future__ import annotations

import asyncio
import json
import sys
import types
from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from gateway.proxy.mcp_audit import MCPAuditTrail
from gateway.proxy.mcp_config import (
    MCPProxyConfig,
    MCPServerConfig,
    MCPToolConfig,
    MCPTransport,
    PermissionLevel,
)
from gateway.proxy.mcp_inspector import MCPInspector
from gateway.proxy.mcp_permissions import MCPPermissionManager
from gateway.proxy.mcp_proxy import (
    ConnectionPool,
    HttpSseConnection,
    MCPProxy,
    MCPToolCall,
    MCPToolResult,
    StdioConnection,
)

# ============================================================
# Fixtures / helpers
# ============================================================


def make_config() -> MCPProxyConfig:
    return MCPProxyConfig(
        servers={
            "home": MCPServerConfig(
                name="home",
                transport=MCPTransport.HTTP_SSE,
                url="http://home.local/mcp",
                min_trust_level=0,
                tools={
                    "get_states": MCPToolConfig(
                        name="get_states", permission_level=PermissionLevel.READ
                    ),
                },
            ),
        },
        pii_scan_enabled=True,
        injection_scan_enabled=True,
    )


def make_proxy(**kwargs) -> MCPProxy:
    config = kwargs.pop("config", None) or make_config()
    perm = MCPPermissionManager(config)
    perm.set_trust_level("main-agent", 2)
    return MCPProxy(
        config=config,
        permission_manager=perm,
        inspector=MCPInspector(),
        audit_trail=MCPAuditTrail(),
        **kwargs,
    )


def make_call(**kwargs) -> MCPToolCall:
    defaults = dict(
        id="call-1",
        server_name="home",
        tool_name="get_states",
        parameters={"entity_id": "light.kitchen"},
        agent_id="main-agent",
    )
    defaults.update(kwargs)
    return MCPToolCall(**defaults)


class FakeProcess:
    """Stand-in for asyncio.subprocess.Process — no real child process."""

    def __init__(self, response: dict | None = None, wait_raises: bool = False):
        self.returncode = None
        self.written: list[bytes] = []
        self.stdin = SimpleNamespace(
            write=self.written.append,
            drain=AsyncMock(),
        )
        line = (json.dumps(response or {"jsonrpc": "2.0", "id": 1, "result": "ok"}) + "\n").encode()
        self.stdout = SimpleNamespace(readline=AsyncMock(return_value=line))
        self.terminated = False
        self.killed = False
        self._wait_raises = wait_raises

    def terminate(self):
        self.terminated = True

    def kill(self):
        self.killed = True

    async def wait(self):
        if self._wait_raises:
            raise asyncio.TimeoutError()
        self.returncode = 0
        return 0


class FakeConn:
    """Stand-in connection injected into the proxy's pool."""

    def __init__(self, response=None, raises: Exception | None = None):
        self.response = response
        self.raises = raises
        self.sent: list[tuple[str, dict]] = []
        self.stopped = False

    async def send_request(self, method, params):
        self.sent.append((method, params))
        if self.raises:
            raise self.raises
        return self.response

    async def stop(self):
        self.stopped = True


# ============================================================
# Dataclass defaults
# ============================================================


class TestDataclasses:
    def test_tool_call_generates_id_and_timestamp(self):
        call = MCPToolCall(
            id="", server_name="s", tool_name="t", parameters={}, agent_id="a", timestamp=0.0
        )
        assert call.id  # uuid assigned
        assert call.timestamp > 0

    def test_tool_result_timestamp_default(self):
        result = MCPToolResult(call_id="c", server_name="s", tool_name="t")
        assert result.timestamp > 0


# ============================================================
# StdioConnection
# ============================================================


class TestStdioConnection:
    async def test_start_send_and_stop(self, monkeypatch):
        cfg = MCPServerConfig(
            name="fs",
            transport=MCPTransport.STDIO,
            command="node",
            args=["server.js"],
            env={"FOO": "BAR"},
            timeout_seconds=3,
        )
        proc = FakeProcess(response={"jsonrpc": "2.0", "id": 1, "result": {"pong": True}})
        captured = {}

        async def fake_exec(cmd, *args, **kwargs):
            captured["cmd"] = cmd
            captured["args"] = args
            captured["env"] = kwargs.get("env")
            return proc

        monkeypatch.setattr(asyncio, "create_subprocess_exec", fake_exec)
        conn = StdioConnection(cfg)
        assert conn.is_running is False

        response = await conn.send_request("tools/call", {"name": "read_file"})
        assert response["result"] == {"pong": True}
        assert captured["cmd"] == "node"
        assert captured["args"] == ("server.js",)
        assert captured["env"]["FOO"] == "BAR"  # merged env passed through
        # Request was framed as newline-delimited JSON-RPC with incrementing id
        sent = json.loads(proc.written[0].decode())
        assert sent["method"] == "tools/call"
        assert sent["id"] == 1
        assert conn.is_running is True

        # start() is idempotent while the process is alive
        await conn.start()
        assert conn.process is proc

        await conn.stop()
        assert proc.terminated is True
        assert conn.process is None
        assert conn.is_running is False

        # stop() on an already-stopped connection is a no-op
        await conn.stop()

    async def test_start_without_env_passes_none(self, monkeypatch):
        cfg = MCPServerConfig(name="fs", transport=MCPTransport.STDIO, command="cmd")
        proc = FakeProcess()
        captured = {}

        async def fake_exec(cmd, *args, **kwargs):
            captured["env"] = kwargs.get("env")
            return proc

        monkeypatch.setattr(asyncio, "create_subprocess_exec", fake_exec)
        conn = StdioConnection(cfg)
        await conn.start()
        assert captured["env"] is None
        assert conn.is_running is True
        proc.returncode = 1  # simulate dead process
        assert conn.is_running is False

    async def test_stop_kills_on_wait_timeout(self, monkeypatch):
        cfg = MCPServerConfig(name="fs", transport=MCPTransport.STDIO, command="cmd")
        proc = FakeProcess(wait_raises=True)

        async def fake_exec(*args, **kwargs):
            return proc

        monkeypatch.setattr(asyncio, "create_subprocess_exec", fake_exec)
        conn = StdioConnection(cfg)
        await conn.start()
        await conn.stop()
        assert proc.terminated is True
        assert proc.killed is True
        assert conn.process is None


# ============================================================
# HttpSseConnection
# ============================================================


class TestHttpSseConnection:
    def _fake_aiohttp(self, payload):
        sessions = []

        class FakeResp:
            async def json(self):
                return payload

            async def __aenter__(self):
                return self

            async def __aexit__(self, *exc):
                return False

        class FakeSession:
            def __init__(self):
                self.posts = []
                self.closed = False
                sessions.append(self)

            def post(self, url, json=None, timeout=None):
                self.posts.append({"url": url, "json": json, "timeout": timeout})
                return FakeResp()

            async def close(self):
                self.closed = True

        mod = types.ModuleType("aiohttp")
        mod.ClientSession = FakeSession
        mod.ClientTimeout = lambda total=None: {"total": total}
        return mod, sessions

    async def test_send_request_and_session_reuse(self, monkeypatch):
        mod, sessions = self._fake_aiohttp({"jsonrpc": "2.0", "id": 1, "result": "pong"})
        monkeypatch.setitem(sys.modules, "aiohttp", mod)
        cfg = MCPServerConfig(
            name="ha", transport=MCPTransport.HTTP_SSE, url="http://ha.local/mcp", timeout_seconds=7
        )
        conn = HttpSseConnection(cfg)
        resp = await conn.send_request("tools/call", {"name": "x"})
        assert resp["result"] == "pong"
        resp2 = await conn.send_request("tools/list", {})
        assert resp2["result"] == "pong"
        assert len(sessions) == 1  # session reused across requests
        assert sessions[0].posts[0]["url"] == "http://ha.local/mcp"
        assert sessions[0].posts[0]["json"]["method"] == "tools/call"
        assert sessions[0].posts[0]["timeout"] == {"total": 7}

        await conn.stop()
        assert sessions[0].closed is True
        assert conn._session is None
        # stop() with no session is a no-op
        await conn.stop()

    async def test_missing_aiohttp_raises_runtime_error(self, monkeypatch):
        monkeypatch.setitem(sys.modules, "aiohttp", None)  # forces ImportError
        conn = HttpSseConnection(
            MCPServerConfig(name="ha", transport=MCPTransport.HTTP_SSE, url="http://ha.local")
        )
        with pytest.raises(RuntimeError, match="aiohttp required"):
            await conn.send_request("tools/call", {})


# ============================================================
# ConnectionPool
# ============================================================


class TestConnectionPool:
    def test_get_or_create_by_transport_and_caching(self):
        pool = ConnectionPool()
        stdio_cfg = MCPServerConfig(name="fs", transport=MCPTransport.STDIO, command="cmd")
        http_cfg = MCPServerConfig(name="ha", transport=MCPTransport.HTTP_SSE, url="http://x")

        c1 = pool.get_or_create("fs", stdio_cfg)
        assert isinstance(c1, StdioConnection)
        c2 = pool.get_or_create("ha", http_cfg)
        assert isinstance(c2, HttpSseConnection)
        assert pool.get_or_create("fs", stdio_cfg) is c1  # cached

        pool.remove("fs")
        assert pool.get_or_create("fs", stdio_cfg) is not c1
        pool.remove("nonexistent")  # no error

    async def test_stop_all_clears_pool(self):
        pool = ConnectionPool()
        conn = FakeConn()
        pool._connections["fake"] = conn
        await pool.stop_all()
        assert conn.stopped is True
        assert pool._connections == {}


# ============================================================
# Egress target extraction
# ============================================================


class TestExtractEgressTargets:
    def test_direct_urls_dedup_and_lists(self):
        params = {
            "urls": ["https://a.example.com/x", "https://a.example.com/x"],
            "nested": {"link": "http://b.example.com/y"},
            "count": 3,
        }
        targets = MCPProxy._extract_egress_targets(params)
        assert targets == ["https://a.example.com/x", "http://b.example.com/y"]

    def test_bare_host_in_destination_field(self):
        targets = MCPProxy._extract_egress_targets({"url": "api.example.com:8443"})
        assert targets == ["https://api.example.com:8443/"]

    def test_bare_host_in_non_destination_field_ignored(self):
        assert MCPProxy._extract_egress_targets({"note": "api.example.com"}) == []

    def test_invalid_url_without_netloc_ignored(self):
        assert MCPProxy._extract_egress_targets({"url": "https://"}) == []

    def test_list_inherits_parent_key(self):
        targets = MCPProxy._extract_egress_targets({"host": ["one.example.com"]})
        assert targets == ["https://one.example.com/"]

    def test_non_matching_text_in_destination_field(self):
        assert MCPProxy._extract_egress_targets({"url": "not a host"}) == []


# ============================================================
# Admin-private data sanitization
# ============================================================


class TestSanitizeAdminPrivateData:
    def test_owner_bypasses_redaction(self):
        proxy = make_proxy()
        proxy.permissions._owner_user_id = "owner-1"
        proxy.permissions._private_data_patterns = [r"secret-code-\d+"]
        value, redacted, count = proxy._sanitize_admin_private_data("secret-code-1", "owner-1")
        assert value == "secret-code-1"
        assert redacted is False
        assert count == 0

    def test_no_patterns_returns_unchanged(self):
        proxy = make_proxy()
        proxy.permissions._private_data_patterns = []
        value, redacted, count = proxy._sanitize_admin_private_data("anything", "stranger")
        assert value == "anything"
        assert redacted is False
        assert count == 0

    def test_redacts_nested_dict_list_tuple(self):
        proxy = make_proxy()
        proxy.permissions._private_data_patterns = [r"secret-code-\d+"]
        payload = {
            "a": ["secret-code-1", ("secret-code-2", 5)],
            "b": {"c": "clean text"},
            "n": 42,
        }
        value, redacted, count = proxy._sanitize_admin_private_data(payload, "stranger")
        assert redacted is True
        assert count == 2
        assert value["a"][0] == "<ADMIN_PRIVATE_DATA>"
        assert value["a"][1] == ("<ADMIN_PRIVATE_DATA>", 5)
        assert value["b"]["c"] == "clean text"
        assert value["n"] == 42


# ============================================================
# Privacy event emission
# ============================================================


class TestEmitPrivacyEvent:
    async def test_emits_event_to_bus(self):
        proxy = make_proxy()
        bus = SimpleNamespace(emit=AsyncMock())
        proxy.set_event_bus(bus)
        await proxy._emit_privacy_event("privacy_data_redacted", "summary", {"k": "v"}, "info")
        assert bus.emit.await_count == 1
        event = bus.emit.await_args.args[0]
        assert event.type == "privacy_data_redacted"
        assert event.severity == "info"
        assert event.details == {"k": "v"}

    async def test_emit_swallows_bus_errors(self):
        proxy = make_proxy()
        bus = SimpleNamespace(emit=AsyncMock(side_effect=RuntimeError("bus down")))
        proxy.set_event_bus(bus)
        # Must not raise — best-effort telemetry
        await proxy._emit_privacy_event("privacy_data_redacted", "s", {})


# ============================================================
# Approval queue gating
# ============================================================


class FakeApprovalQueue:
    def __init__(self, requires_wait=True, approved=True, item=None):
        self.requires_wait = requires_wait
        self.approved = approved
        self.item = item
        self.submissions = []

    async def submit_tool_request(self, tool_name, parameters, agent_id):
        self.submissions.append((tool_name, agent_id))
        return "req-1", self.requires_wait

    async def wait_for_decision(self, request_id):
        return self.approved

    async def get_item(self, request_id):
        return self.item


class TestApprovalQueue:
    async def test_no_queue_allows_by_default(self):
        proxy = make_proxy()
        ok, reason = await proxy.check_approval_required(make_call())
        assert ok is True
        assert reason is None

    async def test_tool_not_requiring_approval_allowed(self):
        queue = FakeApprovalQueue(requires_wait=False)
        proxy = make_proxy(approval_queue=queue)
        ok, reason = await proxy.check_approval_required(make_call())
        assert ok is True
        assert reason is None
        assert queue.submissions == [("get_states", "main-agent")]

    async def test_approved_decision_allows(self):
        proxy = make_proxy(approval_queue=FakeApprovalQueue(requires_wait=True, approved=True))
        ok, reason = await proxy.check_approval_required(make_call())
        assert ok is True
        assert reason is None

    async def test_denied_decision_blocks_with_item_status(self):
        item = SimpleNamespace(status="expired")
        proxy = make_proxy(
            approval_queue=FakeApprovalQueue(requires_wait=True, approved=False, item=item)
        )
        ok, reason = await proxy.check_approval_required(make_call())
        assert ok is False
        assert "expired" in reason
        assert "get_states" in reason

    async def test_denied_decision_with_missing_item_defaults_denied(self):
        proxy = make_proxy(
            approval_queue=FakeApprovalQueue(requires_wait=True, approved=False, item=None)
        )
        ok, reason = await proxy.check_approval_required(make_call())
        assert ok is False
        assert "denied" in reason

    async def test_process_tool_call_blocks_on_denial(self):
        proxy = make_proxy(
            approval_queue=FakeApprovalQueue(requires_wait=True, approved=False, item=None)
        )
        result = await proxy.process_tool_call(make_call())
        assert result.blocked is True
        assert result.allowed is False
        assert "denied" in result.block_reason
        assert result.audit_entry_id
        assert proxy._stats["blocked"] == 1


# ============================================================
# Egress filter integration in process_tool_call
# ============================================================


class TestEgressFilterPaths:
    async def test_sync_egress_filter_deny_blocks(self):
        deny_filter = SimpleNamespace(
            check=lambda agent_id, target: SimpleNamespace(
                action="deny", details="domain on blocklist", rule=""
            )
        )
        proxy = make_proxy(egress_filter=deny_filter)
        call = make_call(parameters={"url": "https://evil.example.com/x"})
        result = await proxy.process_tool_call(call)
        assert result.blocked is True
        assert "Egress blocked" in result.block_reason
        assert "evil.example.com" in result.block_reason
        assert "domain on blocklist" in result.block_reason

    async def test_async_egress_filter_deny_uses_rule_as_reason(self):
        async def check_async(agent_id, destination, tool_name):
            return SimpleNamespace(action=SimpleNamespace(value="deny"), details="", rule="rule-7")

        proxy = make_proxy(egress_filter=SimpleNamespace(check_async=check_async))
        result = await proxy.process_tool_call(
            make_call(parameters={"url": "https://blocked.example.com/"})
        )
        assert result.blocked is True
        assert "rule-7" in result.block_reason

    async def test_egress_filter_allow_passes_through(self):
        allow_filter = SimpleNamespace(
            check=lambda agent_id, target: SimpleNamespace(action="allow", details="", rule="")
        )
        proxy = make_proxy(egress_filter=allow_filter)
        result = await proxy.process_tool_call(
            make_call(parameters={"url": "https://ok.example.com/"})
        )
        assert result.allowed is True
        assert result.blocked is False


# ============================================================
# Tool execution paths (_execute_tool_call via process_tool_call)
# ============================================================


class TestExecuteToolCall:
    async def test_unknown_server_returns_error_result(self):
        proxy = make_proxy()
        result = await proxy._execute_tool_call(make_call(server_name="ghost"))
        assert result.is_error is True
        assert "Unknown server: ghost" in result.error_message

    async def test_successful_execution_with_result_inspection(self):
        proxy = make_proxy()
        conn = FakeConn(response={"result": {"text": "all systems nominal"}})
        proxy.pool._connections["home"] = conn
        result = await proxy.process_tool_call(make_call(), execute=True)
        assert result.allowed is True
        assert result.tool_result is not None
        assert result.tool_result.is_error is False
        assert result.tool_result.content == {"text": "all systems nominal"}
        assert result.sanitized_result == {"text": "all systems nominal"}
        method, params = conn.sent[0]
        assert method == "tools/call"
        assert params["name"] == "get_states"
        assert params["arguments"] == {"entity_id": "light.kitchen"}
        # result was logged to the audit trail
        assert len(proxy.audit) == 2  # call + result entries

    async def test_execution_redacts_admin_private_content(self):
        proxy = make_proxy()
        proxy.permissions._private_data_patterns = [r"secret-code-\d+"]
        bus = SimpleNamespace(emit=AsyncMock())
        proxy.set_event_bus(bus)
        conn = FakeConn(response={"result": {"text": "the code is secret-code-42"}})
        proxy.pool._connections["home"] = conn
        result = await proxy.process_tool_call(make_call(), execute=True)
        assert result.sanitized_result == {"text": "the code is <ADMIN_PRIVATE_DATA>"}
        events = proxy.permissions.get_private_redaction_events()
        assert events and events[-1]["agent_id"] == "main-agent"
        assert bus.emit.await_count == 1
        assert bus.emit.await_args.args[0].type == "privacy_data_redacted"

    async def test_execution_with_none_content_skips_result_inspection(self):
        proxy = make_proxy()
        proxy.pool._connections["home"] = FakeConn(response={"result": None})
        result = await proxy.process_tool_call(make_call(), execute=True)
        assert result.allowed is True
        assert result.tool_result.content is None
        assert result.sanitized_result is None

    async def test_server_error_response(self):
        proxy = make_proxy()
        proxy.pool._connections["home"] = FakeConn(response={"error": {"message": "tool exploded"}})
        result = await proxy._execute_tool_call(make_call())
        assert result.is_error is True
        assert result.error_message == "tool exploded"

    async def test_server_error_response_without_message(self):
        proxy = make_proxy()
        proxy.pool._connections["home"] = FakeConn(response={"error": {"code": -32000}})
        result = await proxy._execute_tool_call(make_call())
        assert result.is_error is True
        assert "-32000" in result.error_message

    async def test_timeout_error(self):
        proxy = make_proxy()
        proxy.pool._connections["home"] = FakeConn(raises=asyncio.TimeoutError())
        result = await proxy._execute_tool_call(make_call())
        assert result.is_error is True
        assert "Timeout after" in result.error_message
        assert proxy._stats["errors"] == 1

    async def test_generic_exception(self):
        proxy = make_proxy()
        proxy.pool._connections["home"] = FakeConn(raises=ConnectionResetError("conn reset"))
        result = await proxy._execute_tool_call(make_call())
        assert result.is_error is True
        assert "conn reset" in result.error_message
        assert proxy._stats["errors"] == 1

    async def test_sanitized_params_preferred_over_originals(self):
        proxy = make_proxy()
        conn = FakeConn(response={"result": "ok"})
        proxy.pool._connections["home"] = conn
        await proxy._execute_tool_call(make_call(), sanitized_params={"entity_id": "[REDACTED]"})
        assert conn.sent[0][1]["arguments"] == {"entity_id": "[REDACTED]"}


# ============================================================
# Passthrough mode
# ============================================================


class TestPassthrough:
    async def test_passthrough_with_execute(self):
        proxy = MCPProxy(config=make_config(), passthrough=True)
        proxy.pool._connections["home"] = FakeConn(response={"result": {"ok": True}})
        result = await proxy.process_tool_call(make_call(), execute=True)
        assert result.passthrough is True
        assert result.allowed is True
        assert result.tool_result.content == {"ok": True}
        assert len(proxy.audit) == 2  # call + result logged even in passthrough

    async def test_passthrough_process_tool_result(self):
        proxy = MCPProxy(config=make_config(), passthrough=True)
        tool_result = MCPToolResult(
            call_id="c1", server_name="home", tool_name="get_states", content={"raw": "data"}
        )
        result = await proxy.process_tool_result(tool_result, agent_id="main-agent")
        assert result.passthrough is True
        assert result.allowed is True
        assert result.sanitized_result == {"raw": "data"}
        assert len(proxy.audit) == 1


# ============================================================
# process_tool_result (non-passthrough) + stats + shutdown
# ============================================================


class TestResultProcessingAndLifecycle:
    async def test_process_tool_result_redacts_private_data(self):
        proxy = make_proxy()
        proxy.permissions._private_data_patterns = [r"secret-code-\d+"]
        tool_result = MCPToolResult(
            call_id="c1",
            server_name="home",
            tool_name="get_states",
            content={"text": "secret-code-7"},
        )
        result = await proxy.process_tool_result(tool_result, agent_id="stranger")
        assert result.allowed is True  # results are never blocked, only redacted
        assert result.sanitized_result == {"text": "<ADMIN_PRIVATE_DATA>"}

    async def test_process_tool_result_handles_none_content(self):
        proxy = make_proxy()
        tool_result = MCPToolResult(
            call_id="c2",
            server_name="home",
            tool_name="get_states",
            is_error=True,
            error_message="boom",
        )
        result = await proxy.process_tool_result(tool_result, agent_id="main-agent")
        assert result.allowed is True
        assert len(proxy.audit) == 1

    def test_get_stats_zero_and_after_calls(self):
        proxy = make_proxy()
        stats = proxy.get_stats()
        assert stats["avg_processing_time_ms"] == 0
        assert stats["total_calls"] == 0
        assert stats["audit_chain_valid"] is True
        assert stats["passthrough_mode"] is False

    async def test_get_stats_after_allowed_call(self):
        proxy = make_proxy()
        await proxy.process_tool_call(make_call())
        stats = proxy.get_stats()
        assert stats["total_calls"] == 1
        assert stats["allowed"] == 1
        assert stats["audit_entries"] == 1

    async def test_shutdown_stops_all_connections(self):
        proxy = make_proxy()
        conn = FakeConn()
        proxy.pool._connections["home"] = conn
        await proxy.shutdown()
        assert conn.stopped is True
        assert proxy.pool._connections == {}
