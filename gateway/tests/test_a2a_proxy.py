# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for the A2A (Agent-to-Agent) inbound proxy interceptor (SCRUM-129).

A2AProxy terminates the inbound HTTP connection itself (webhook_receiver.py
pattern — AgentShroud is called directly by the external peer, not "the callee
calls the proxy first" the way MCP tool calls do). It resolves peer identity
from the Authorization: Bearer token (never socket address — independent
mitigation for upstream Hermes gap #80534), parses the JSON-RPC 2.0 envelope,
runs it through A2APolicyEngine, PII-scans Message/Parts content, and forwards
to Hermes's real A2A listener via an injectable client (no real network in
tests — dependency-injected, matching mcp_proxy.py's testable design).
"""

from __future__ import annotations

import pytest

from gateway.proxy.a2a_proxy import A2AProxy, A2AProxyResult
from gateway.security.a2a_policy import A2AMethod, A2APolicyConfig, A2APolicyEngine

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


class _StubForwarder:
    """Records what it was asked to forward; returns a canned response."""

    def __init__(self, response_body: str = '{"result": "ok"}', status: int = 200):
        self.response_body = response_body
        self.status = status
        self.calls: list[dict] = []

    async def forward(self, body: str) -> tuple[int, str]:
        self.calls.append({"body": body})
        return self.status, self.response_body


def _base_policy_engine() -> A2APolicyEngine:
    cfg = A2APolicyConfig.from_dict({"default_action": "deny", "allowed_peers": ["alice"]})
    return A2APolicyEngine(cfg)


@pytest.fixture()
def forwarder() -> _StubForwarder:
    return _StubForwarder()


@pytest.fixture()
def proxy(forwarder: _StubForwarder) -> A2AProxy:
    return A2AProxy(
        policy_engine=_base_policy_engine(),
        peer_tokens={"alice-token": "alice", "bob-token": "bob"},
        forwarder=forwarder,
    )


def _jsonrpc(method: str, params: dict, request_id: str = "1") -> dict:
    return {"jsonrpc": "2.0", "id": request_id, "method": method, "params": params}


# ---------------------------------------------------------------------------
# Peer identity resolution (independent mitigation for gap #80534 — identity
# must come from the Bearer token, never from socket/X-Forwarded-For)
# ---------------------------------------------------------------------------


def test_resolve_peer_id_from_known_bearer_token(proxy: A2AProxy) -> None:
    assert proxy.resolve_peer_id("Bearer alice-token") == "alice"


def test_resolve_peer_id_unknown_token_returns_none(proxy: A2AProxy) -> None:
    assert proxy.resolve_peer_id("Bearer not-a-real-token") is None


def test_resolve_peer_id_missing_header_returns_none(proxy: A2AProxy) -> None:
    assert proxy.resolve_peer_id(None) is None
    assert proxy.resolve_peer_id("") is None


def test_resolve_peer_id_malformed_header_returns_none(proxy: A2AProxy) -> None:
    assert proxy.resolve_peer_id("alice-token") is None  # missing "Bearer " prefix
    assert proxy.resolve_peer_id("Basic dXNlcjpwYXNz") is None


def test_resolve_peer_id_uses_constant_time_comparison(proxy: A2AProxy) -> None:
    """Token comparison must not leak timing information — same guarantee as
    Hermes's own hmac.compare_digest usage. We can't assert timing directly in
    a unit test, so assert the implementation routes through hmac.compare_digest
    rather than a raw `==`/`in` membership check."""
    import inspect

    source = inspect.getsource(proxy.resolve_peer_id)
    assert "compare_digest" in source


# ---------------------------------------------------------------------------
# JSON-RPC envelope parsing
# ---------------------------------------------------------------------------


def test_parse_jsonrpc_extracts_method_and_task_id_from_send_message() -> None:
    body = _jsonrpc(
        "SendMessage",
        {"message": {"taskId": "t-1", "parts": [{"text": "hello"}]}},
    )
    parsed = A2AProxy.parse_jsonrpc_request(body)
    assert parsed.method == A2AMethod.SEND_MESSAGE
    assert parsed.task_id == "t-1"


def test_parse_jsonrpc_extracts_task_id_from_get_task() -> None:
    body = _jsonrpc("GetTask", {"taskId": "t-42"})
    parsed = A2AProxy.parse_jsonrpc_request(body)
    assert parsed.method == A2AMethod.GET_TASK
    assert parsed.task_id == "t-42"


def test_parse_jsonrpc_accepts_legacy_path_style_method_alias() -> None:
    """Pre-1.0 peers send lowercase/path-style method names — Hermes accepts
    both for backward compat; AgentShroud's parser must too, or a legitimate
    older peer gets spuriously denied."""
    body = _jsonrpc("message/send", {"message": {"parts": [{"text": "hi"}]}})
    parsed = A2AProxy.parse_jsonrpc_request(body)
    assert parsed.method == A2AMethod.SEND_MESSAGE


def test_parse_jsonrpc_extracts_callback_url_from_set_push_config() -> None:
    body = _jsonrpc(
        "SetTaskPushNotificationConfig",
        {"taskId": "t-1", "pushNotificationConfig": {"url": "https://example.com/hook"}},
    )
    parsed = A2AProxy.parse_jsonrpc_request(body)
    assert parsed.method == A2AMethod.SET_PUSH_NOTIFICATION_CONFIG
    assert parsed.callback_url == "https://example.com/hook"


def test_parse_jsonrpc_unknown_method_raises_value_error() -> None:
    body = _jsonrpc("SomeMadeUpMethod", {})
    with pytest.raises(ValueError):
        A2AProxy.parse_jsonrpc_request(body)


def test_parse_jsonrpc_missing_method_field_raises_value_error() -> None:
    with pytest.raises(ValueError):
        A2AProxy.parse_jsonrpc_request({"jsonrpc": "2.0", "id": "1", "params": {}})


def test_parse_jsonrpc_non_dict_body_raises_value_error() -> None:
    with pytest.raises(ValueError):
        A2AProxy.parse_jsonrpc_request("not a dict")  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# Message/Parts text extraction for PII scanning
# ---------------------------------------------------------------------------


def test_extract_text_concatenates_text_parts() -> None:
    message = {"parts": [{"text": "hello "}, {"text": "world"}]}
    text, skipped_binary = A2AProxy.extract_text_for_pii_scan(message)
    assert text == "hello world"
    assert skipped_binary is False


def test_extract_text_flags_binary_parts_without_scanning_them() -> None:
    """A file/data Part must not be silently dropped or mis-scanned as text —
    it's flagged so the audit trail never claims PII coverage it doesn't have."""
    message = {
        "parts": [
            {"text": "see attached"},
            {"file": {"bytes": "base64gibberish=="}},
        ]
    }
    text, skipped_binary = A2AProxy.extract_text_for_pii_scan(message)
    assert text == "see attached"
    assert skipped_binary is True


def test_extract_text_empty_message_returns_empty_string() -> None:
    text, skipped_binary = A2AProxy.extract_text_for_pii_scan({})
    assert text == ""
    assert skipped_binary is False


def test_extract_text_handles_missing_parts_key() -> None:
    text, skipped_binary = A2AProxy.extract_text_for_pii_scan({"taskId": "t-1"})
    assert text == ""


# ---------------------------------------------------------------------------
# process_inbound_request(): end-to-end orchestration
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_process_inbound_request_allowed_peer_low_risk_forwards(
    proxy: A2AProxy, forwarder: _StubForwarder
) -> None:
    body = _jsonrpc("GetTask", {"taskId": "t-1"})
    result = await proxy.process_inbound_request(
        raw_body=body, auth_header="Bearer alice-token", source_ip="10.0.0.99"
    )
    assert result.allowed is True
    assert result.blocked is False
    assert result.peer_id == "alice"
    assert len(forwarder.calls) == 1


@pytest.mark.asyncio
async def test_process_inbound_request_missing_auth_is_blocked_and_never_forwarded(
    proxy: A2AProxy, forwarder: _StubForwarder
) -> None:
    body = _jsonrpc("GetTask", {"taskId": "t-1"})
    result = await proxy.process_inbound_request(
        raw_body=body, auth_header=None, source_ip="10.0.0.99"
    )
    assert result.allowed is False
    assert result.blocked is True
    assert "auth" in result.block_reason.lower()
    assert forwarder.calls == []


@pytest.mark.asyncio
async def test_process_inbound_request_unknown_token_is_blocked(
    proxy: A2AProxy, forwarder: _StubForwarder
) -> None:
    body = _jsonrpc("GetTask", {"taskId": "t-1"})
    result = await proxy.process_inbound_request(
        raw_body=body, auth_header="Bearer garbage-token", source_ip="10.0.0.99"
    )
    assert result.blocked is True
    assert forwarder.calls == []


@pytest.mark.asyncio
async def test_process_inbound_request_denied_peer_never_reaches_hermes(
    forwarder: _StubForwarder,
) -> None:
    cfg = A2APolicyConfig.from_dict({"default_action": "deny", "allowed_peers": ["alice"]})
    proxy = A2AProxy(
        policy_engine=A2APolicyEngine(cfg),
        peer_tokens={"eve-token": "eve"},
        forwarder=forwarder,
    )
    body = _jsonrpc("GetTask", {"taskId": "t-1"})
    result = await proxy.process_inbound_request(
        raw_body=body, auth_header="Bearer eve-token", source_ip="10.0.0.99"
    )
    assert result.allowed is False
    assert result.blocked is True
    assert forwarder.calls == []


@pytest.mark.asyncio
async def test_process_inbound_request_task_ownership_violation_blocked(
    proxy: A2AProxy, forwarder: _StubForwarder
) -> None:
    proxy2 = A2AProxy(
        policy_engine=A2APolicyEngine(
            A2APolicyConfig.from_dict({"default_action": "deny", "allowed_peers": ["alice", "bob"]})
        ),
        peer_tokens={"alice-token": "alice", "bob-token": "bob"},
        forwarder=forwarder,
    )
    create_body = _jsonrpc("SendMessage", {"message": {"taskId": "t-1", "parts": []}})
    await proxy2.process_inbound_request(
        raw_body=create_body, auth_header="Bearer alice-token", source_ip="1.1.1.1"
    )
    steal_body = _jsonrpc("GetTask", {"taskId": "t-1"})
    result = await proxy2.process_inbound_request(
        raw_body=steal_body, auth_header="Bearer bob-token", source_ip="2.2.2.2"
    )
    assert result.blocked is True
    assert "task_ownership" in result.block_reason or "does not own" in result.block_reason


@pytest.mark.asyncio
async def test_process_inbound_request_pii_in_message_is_redacted_before_forwarding(
    forwarder: _StubForwarder,
) -> None:
    """A SendMessage containing PII must have it redacted in what's forwarded
    to Hermes — the raw PII-bearing text must never reach the upstream bot."""
    from gateway.security.differential_pii_detector import (
        DifferentialPIIConfig,
        DifferentialPIIDetector,
    )

    detector = DifferentialPIIDetector(DifferentialPIIConfig())
    proxy = A2AProxy(
        policy_engine=_base_policy_engine(),
        peer_tokens={"alice-token": "alice"},
        forwarder=forwarder,
        pii_detector=detector,
    )
    body = _jsonrpc(
        "SendMessage",
        {
            "message": {
                "taskId": "t-1",
                "parts": [{"text": "my SSN is 078-05-1120, call me back"}],
            }
        },
    )
    result = await proxy.process_inbound_request(
        raw_body=body, auth_header="Bearer alice-token", source_ip="1.1.1.1"
    )
    assert result.allowed is True
    forwarded_body = forwarder.calls[0]["body"]
    assert "078-05-1120" not in forwarded_body


@pytest.mark.asyncio
async def test_process_inbound_request_binary_part_is_forwarded_unscanned_and_flagged(
    forwarder: _StubForwarder,
) -> None:
    from gateway.security.differential_pii_detector import (
        DifferentialPIIConfig,
        DifferentialPIIDetector,
    )

    detector = DifferentialPIIDetector(DifferentialPIIConfig())
    proxy = A2AProxy(
        policy_engine=_base_policy_engine(),
        peer_tokens={"alice-token": "alice"},
        forwarder=forwarder,
        pii_detector=detector,
    )
    body = _jsonrpc(
        "SendMessage",
        {"message": {"taskId": "t-1", "parts": [{"file": {"bytes": "Zm9v"}}]}},
    )
    result = await proxy.process_inbound_request(
        raw_body=body, auth_header="Bearer alice-token", source_ip="1.1.1.1"
    )
    assert result.allowed is True
    assert result.pii_scan_skipped_binary is True


@pytest.mark.asyncio
async def test_process_inbound_request_high_risk_method_without_approval_queue_denied(
    forwarder: _StubForwarder,
) -> None:
    proxy = A2AProxy(
        policy_engine=_base_policy_engine(),  # no approval_queue configured
        peer_tokens={"alice-token": "alice"},
        forwarder=forwarder,
    )
    body = _jsonrpc("SendMessage", {"message": {"taskId": "t-1", "parts": []}})
    await proxy.process_inbound_request(
        raw_body=body, auth_header="Bearer alice-token", source_ip="1.1.1.1"
    )
    cancel_body = _jsonrpc("CancelTask", {"taskId": "t-1"})
    result = await proxy.process_inbound_request(
        raw_body=cancel_body, auth_header="Bearer alice-token", source_ip="1.1.1.1"
    )
    assert result.blocked is True
    # Only the earlier (medium-risk, allowed) SendMessage was forwarded — the
    # high-risk CancelTask, denied fail-closed with no approval queue, was not.
    assert len(forwarder.calls) == 1


# ---------------------------------------------------------------------------
# Agent Card discovery — open by spec, but always audited
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_agent_card_discovery_is_never_policy_gated(
    proxy: A2AProxy, forwarder: _StubForwarder
) -> None:
    """GET /.well-known/agent-card.json must pass through with NO auth/peer
    requirement at all — the spec requires open discovery."""
    result = await proxy.process_agent_card_request(source_ip="203.0.113.5")
    assert result.blocked is False
    assert result.allowed is True


@pytest.mark.asyncio
async def test_agent_card_discovery_is_still_audited(
    proxy: A2AProxy, forwarder: _StubForwarder
) -> None:
    result = await proxy.process_agent_card_request(source_ip="203.0.113.5")
    assert result.audit_entry_id != "" or result.matched_rule == "discovery_passthrough"


# ---------------------------------------------------------------------------
# A2AProxyResult
# ---------------------------------------------------------------------------


def test_proxy_result_defaults_are_safe() -> None:
    """A freshly-constructed, un-set result must default to blocked, not
    allowed — a proxy path that forgets to explicitly set the result fails
    closed by construction, not fails open."""
    result = A2AProxyResult()
    assert result.allowed is False
    assert result.blocked is True


# ---------------------------------------------------------------------------
# Remaining edge cases
# ---------------------------------------------------------------------------


def test_resolve_peer_id_whitespace_only_token_returns_none(proxy: A2AProxy) -> None:
    assert proxy.resolve_peer_id("Bearer    ") is None


def test_parse_jsonrpc_tolerates_non_dict_params() -> None:
    body = {"jsonrpc": "2.0", "id": "1", "method": "GetTask", "params": "not-a-dict"}
    parsed = A2AProxy.parse_jsonrpc_request(body)
    assert parsed.params == {}
    assert parsed.task_id is None


def test_extract_text_skips_non_dict_entries_in_parts() -> None:
    message = {"parts": [{"text": "real part"}, "a bare string, not a Part object", 42]}
    text, skipped_binary = A2AProxy.extract_text_for_pii_scan(message)
    assert text == "real part"
    assert skipped_binary is False


@pytest.mark.asyncio
async def test_process_inbound_request_malformed_body_is_blocked(
    proxy: A2AProxy, forwarder: _StubForwarder
) -> None:
    """An unparseable request must be rejected through the same
    process_inbound_request path real traffic uses, not just at the
    parse_jsonrpc_request unit level."""
    result = await proxy.process_inbound_request(
        raw_body={"jsonrpc": "2.0", "id": "1"},  # no 'method' field
        auth_header="Bearer alice-token",
        source_ip="1.1.1.1",
    )
    assert result.blocked is True
    assert "malformed" in result.block_reason
    assert forwarder.calls == []


class _StubAuditStore:
    class _Event:
        def __init__(self, event_id: str):
            self.event_id = event_id

    def __init__(self):
        self.logged: list[dict] = []

    async def log_event(self, event_type, severity, details, source_module, bot_id):
        self.logged.append(
            {
                "event_type": event_type,
                "severity": severity,
                "details": details,
                "source_module": source_module,
                "bot_id": bot_id,
            }
        )
        return self._Event(event_id=f"evt-{len(self.logged)}")


@pytest.mark.asyncio
async def test_process_inbound_request_logs_to_audit_store_when_configured(
    forwarder: _StubForwarder,
) -> None:
    audit_store = _StubAuditStore()
    proxy = A2AProxy(
        policy_engine=_base_policy_engine(),
        peer_tokens={"alice-token": "alice"},
        forwarder=forwarder,
        audit_store=audit_store,
    )
    body = _jsonrpc("GetTask", {"taskId": "t-1"})
    result = await proxy.process_inbound_request(
        raw_body=body, auth_header="Bearer alice-token", source_ip="1.1.1.1"
    )
    assert len(audit_store.logged) == 1
    assert audit_store.logged[0]["details"]["peer_id"] == "alice"
    assert audit_store.logged[0]["bot_id"] == "hermes"
    assert result.audit_entry_id == "evt-1"


@pytest.mark.asyncio
async def test_process_inbound_request_denial_is_also_logged_to_audit_store(
    forwarder: _StubForwarder,
) -> None:
    audit_store = _StubAuditStore()
    proxy = A2AProxy(
        policy_engine=_base_policy_engine(),
        peer_tokens={"alice-token": "alice"},
        forwarder=forwarder,
        audit_store=audit_store,
    )
    result = await proxy.process_inbound_request(
        raw_body=_jsonrpc("GetTask", {"taskId": "t-1"}),
        auth_header=None,
        source_ip="1.1.1.1",
    )
    assert result.blocked is True
    assert len(audit_store.logged) == 1
    assert audit_store.logged[0]["severity"] == "warning"


def test_redact_message_text_clears_all_text_parts_not_just_the_first() -> None:
    """A message with MULTIPLE text parts must not leave a second, unredacted
    text part sitting right next to the redacted first one — the first is
    replaced with the redacted blob, any additional text parts are cleared."""
    from gateway.proxy.a2a_proxy import _redact_message_text

    raw_body = {
        "params": {
            "message": {
                "parts": [
                    {"text": "my SSN is 078-05-1120"},
                    {"text": "078-05-1120 again, in case you missed it"},
                ]
            }
        }
    }
    result = _redact_message_text(raw_body, "[REDACTED]")
    parts = result["params"]["message"]["parts"]
    assert parts[0]["text"] == "[REDACTED]"
    assert parts[1]["text"] == ""
    assert "078-05-1120" not in str(result)
