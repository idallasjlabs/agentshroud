# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Coverage tests for gateway/soc/websocket.py, event_adapter.py and auth.py.

Exercises the realtime SOC plumbing end-to-end at unit scope:
  - SOCWebSocketHandler run loop, keepalive, fan-out and filtering
  - ws_soc_endpoint auth paths (WS token, bearer header, raw password fallback)
  - event_adapter converters incl. all error branches
  - auth token issuance/redemption, config-token resolution, RBAC dependency
"""

from __future__ import annotations

import asyncio
import builtins
import json
import time
import types
from typing import Any, Dict, List, Optional
from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi import HTTPException, WebSocketDisconnect

import gateway.soc.websocket as ws_mod
from gateway.security.rbac import Action, PermissionResult, Resource
from gateway.security.rbac_config import RBACConfig, Role
from gateway.soc import event_adapter
from gateway.soc.auth import (
    SCLCaller,
    _get_config_token,
    _get_rbac_manager,
    _resolve_caller,
    _session_tokens,
    _verify_bearer,
    _verify_session_token,
    _ws_tokens,
    get_caller,
    issue_session_token,
    issue_ws_token,
    redeem_ws_token,
)
from gateway.soc.models import SecurityEvent, Severity, WSEvent, WSEventType
from gateway.soc.websocket import SOCWebSocketHandler, _coerce_to_ws_event, ws_soc_endpoint

_PASSWORD_ENVS = (
    "AGENTSHROUD_GATEWAY_PASSWORD",
    "OPENCLAW_GATEWAY_PASSWORD",
    "GATEWAY_AUTH_TOKEN_FILE",
    "OPENCLAW_GATEWAY_PASSWORD_FILE",
)


@pytest.fixture()
def clean_auth_env(monkeypatch):
    """Remove all gateway-password env vars and clear token stores."""
    for var in _PASSWORD_ENVS:
        monkeypatch.delenv(var, raising=False)
    _ws_tokens.clear()
    _session_tokens.clear()
    yield monkeypatch
    _ws_tokens.clear()
    _session_tokens.clear()


def _block_run_secrets(monkeypatch):
    """Make /run/secrets reads deterministic (raise OSError) on any host."""
    real_open = builtins.open

    def guarded_open(path, *args, **kwargs):
        if isinstance(path, str) and path.startswith("/run/secrets/"):
            raise OSError("blocked in test")
        return real_open(path, *args, **kwargs)

    monkeypatch.setattr(builtins, "open", guarded_open)


# ---------------------------------------------------------------------------
# auth.py — config token resolution
# ---------------------------------------------------------------------------


class TestGetConfigToken:
    def test_explicit_env_wins(self, clean_auth_env):
        clean_auth_env.setenv("AGENTSHROUD_GATEWAY_PASSWORD", "explicit-tok")
        clean_auth_env.setenv("OPENCLAW_GATEWAY_PASSWORD", "legacy-tok")
        assert _get_config_token() == "explicit-tok"

    def test_legacy_env_fallback(self, clean_auth_env):
        clean_auth_env.setenv("OPENCLAW_GATEWAY_PASSWORD", "legacy-tok")
        assert _get_config_token() == "legacy-tok"

    def test_token_file_env(self, clean_auth_env, tmp_path):
        f = tmp_path / "tok.txt"
        f.write_text("file-tok\n")
        clean_auth_env.setenv("GATEWAY_AUTH_TOKEN_FILE", str(f))
        assert _get_config_token() == "file-tok"

    def test_missing_first_file_falls_to_second(self, clean_auth_env, tmp_path):
        clean_auth_env.setenv("GATEWAY_AUTH_TOKEN_FILE", str(tmp_path / "does-not-exist"))
        f2 = tmp_path / "tok2.txt"
        f2.write_text("second-file-tok")
        clean_auth_env.setenv("OPENCLAW_GATEWAY_PASSWORD_FILE", str(f2))
        assert _get_config_token() == "second-file-tok"

    def test_empty_first_file_falls_to_second(self, clean_auth_env, tmp_path):
        empty = tmp_path / "empty.txt"
        empty.write_text("")
        f2 = tmp_path / "tok2.txt"
        f2.write_text("second-tok")
        clean_auth_env.setenv("GATEWAY_AUTH_TOKEN_FILE", str(empty))
        clean_auth_env.setenv("OPENCLAW_GATEWAY_PASSWORD_FILE", str(f2))
        assert _get_config_token() == "second-tok"

    def test_no_sources_returns_empty(self, clean_auth_env):
        _block_run_secrets(clean_auth_env)
        assert _get_config_token() == ""


class TestVerifyBearer:
    def test_match(self):
        assert _verify_bearer("s3cret", "s3cret") is True

    def test_mismatch(self):
        assert _verify_bearer("wrong", "s3cret") is False

    def test_empty_token_or_config(self):
        assert _verify_bearer("", "s3cret") is False
        assert _verify_bearer("s3cret", "") is False


# ---------------------------------------------------------------------------
# auth.py — token stores (pruning branches)
# ---------------------------------------------------------------------------


class TestTokenStorePruning:
    def test_issue_session_token_prunes_expired(self, clean_auth_env):
        _session_tokens["stale"] = ("old-user", time.time() - 99999)
        token = issue_session_token("cfg", "owner-1")
        assert "stale" not in _session_tokens
        assert _verify_session_token(token) == "owner-1"

    def test_issue_ws_token_prunes_expired(self, clean_auth_env):
        _ws_tokens["stale"] = ("old-user", time.time() - 9999)
        token = issue_ws_token("user-9")
        assert "stale" not in _ws_tokens
        assert redeem_ws_token(token) == "user-9"

    def test_redeem_expired_ws_token_returns_none(self, clean_auth_env):
        token = issue_ws_token("user-x")
        uid, _ = _ws_tokens[token]
        _ws_tokens[token] = (uid, time.time() - 10_000)
        assert redeem_ws_token(token) is None


# ---------------------------------------------------------------------------
# auth.py — SCLCaller + RBAC dependency
# ---------------------------------------------------------------------------


class _FakeRBAC:
    """Minimal RBAC stand-in with controllable check_permission results."""

    def __init__(self, allowed: bool, reason: Optional[str] = None, owner: bool = False):
        self._result = PermissionResult(allowed=allowed, reason=reason)
        self.config = types.SimpleNamespace(
            is_owner=lambda uid: owner,
            owner_user_id="8096968754",
        )

    def check_permission(self, user_id, action, resource):
        return self._result


class TestSCLCaller:
    def test_require_allowed_does_not_raise(self):
        caller = SCLCaller("u1", Role.OWNER, _FakeRBAC(allowed=True))
        caller.require(Action.READ, Resource.SYSTEM)  # must not raise

    def test_require_denied_raises_403_with_reason(self):
        caller = SCLCaller("u1", Role.VIEWER, _FakeRBAC(allowed=False, reason="nope"))
        with pytest.raises(HTTPException) as exc:
            caller.require(Action.WRITE, Resource.SYSTEM)
        assert exc.value.status_code == 403
        assert exc.value.detail["code"] == "PERMISSION_DENIED"
        assert exc.value.detail["message"] == "nope"

    def test_require_denied_without_reason_uses_forbidden(self):
        caller = SCLCaller("u1", Role.VIEWER, _FakeRBAC(allowed=False, reason=None))
        with pytest.raises(HTTPException) as exc:
            caller.require(Action.DELETE, Resource.FILES)
        assert exc.value.detail["message"] == "Forbidden"

    def test_is_owner_delegates_to_config(self):
        assert SCLCaller("u1", Role.OWNER, _FakeRBAC(True, owner=True)).is_owner() is True
        assert SCLCaller("u1", Role.VIEWER, _FakeRBAC(True, owner=False)).is_owner() is False

    def test_is_group_admin_without_teams_config(self):
        caller = SCLCaller("u1", Role.OWNER, _FakeRBAC(True))
        assert caller.is_group_admin("g1") is False

    def test_is_group_admin_with_teams_config(self):
        rbac = _FakeRBAC(True)
        rbac.config._teams_config = types.SimpleNamespace(
            is_group_admin=lambda uid, gid: uid == "u1" and gid == "g1"
        )
        caller = SCLCaller("u1", Role.OWNER, rbac)
        assert caller.is_group_admin("g1") is True
        assert caller.is_group_admin("g2") is False

    def test_get_rbac_manager_builds_real_manager(self):
        rbac = _get_rbac_manager()
        result = rbac.check_permission(rbac.config.owner_user_id, Action.READ, Resource.SYSTEM)
        assert result.allowed is True


class TestResolveCaller:
    def test_bearer_header_valid(self, clean_auth_env):
        clean_auth_env.setenv("AGENTSHROUD_GATEWAY_PASSWORD", "cfg-secret")
        caller = _resolve_caller(
            authorization="Bearer cfg-secret", x_soc_token=None, soc_session=None
        )
        assert caller.role == Role.OWNER
        assert caller.user_id == RBACConfig().owner_user_id

    def test_x_soc_token_header_valid(self, clean_auth_env):
        clean_auth_env.setenv("AGENTSHROUD_GATEWAY_PASSWORD", "cfg-secret")
        caller = _resolve_caller(authorization=None, x_soc_token="cfg-secret", soc_session=None)
        assert caller.role == Role.OWNER

    def test_session_cookie_valid(self, clean_auth_env):
        clean_auth_env.setenv("AGENTSHROUD_GATEWAY_PASSWORD", "cfg-secret")
        token = issue_session_token("cfg-secret", "owner-77")
        caller = _resolve_caller(authorization=None, x_soc_token=None, soc_session=token)
        assert caller.user_id == "owner-77"
        assert caller.role == Role.OWNER

    def test_cookie_raw_bearer_fallback(self, clean_auth_env):
        clean_auth_env.setenv("AGENTSHROUD_GATEWAY_PASSWORD", "cfg-secret")
        caller = _resolve_caller(authorization=None, x_soc_token=None, soc_session="cfg-secret")
        assert caller.role == Role.OWNER

    def test_no_credentials_raises_401(self, clean_auth_env):
        _block_run_secrets(clean_auth_env)
        with pytest.raises(HTTPException) as exc:
            _resolve_caller(authorization=None, x_soc_token=None, soc_session=None)
        assert exc.value.status_code == 401
        assert exc.value.headers["WWW-Authenticate"] == "Bearer"

    def test_wrong_bearer_raises_401(self, clean_auth_env):
        clean_auth_env.setenv("AGENTSHROUD_GATEWAY_PASSWORD", "cfg-secret")
        with pytest.raises(HTTPException) as exc:
            _resolve_caller(authorization="Bearer wrong", x_soc_token=None, soc_session=None)
        assert exc.value.status_code == 401

    def test_get_caller_passthrough(self):
        sentinel = SCLCaller("u1", Role.OWNER, _FakeRBAC(True))
        assert get_caller(caller=sentinel) is sentinel


# ---------------------------------------------------------------------------
# event_adapter.py — severity mapping
# ---------------------------------------------------------------------------


class TestMapSeverity:
    @pytest.mark.parametrize(
        "raw,expected",
        [
            ("critical", Severity.CRITICAL),
            ("HIGH", Severity.HIGH),
            ("medium", Severity.MEDIUM),
            ("low", Severity.LOW),
            ("info", Severity.INFO),
            ("warning", Severity.MEDIUM),
            ("warn", Severity.MEDIUM),
            ("error", Severity.HIGH),
            ("bogus", Severity.INFO),
            (None, Severity.INFO),
        ],
    )
    def test_string_mapping(self, raw, expected):
        assert event_adapter._map_severity(raw) == expected

    def test_severity_enum_passthrough(self):
        assert event_adapter._map_severity(Severity.CRITICAL) is Severity.CRITICAL


# ---------------------------------------------------------------------------
# event_adapter.py — converters
# ---------------------------------------------------------------------------


def _audit_entry(**overrides) -> types.SimpleNamespace:
    base: Dict[str, Any] = dict(
        event_type="prompt_blocked",
        severity="high",
        timestamp="2026-06-12T00:00:00+00:00",
        source_module="prompt_guard",
        details={},
        prev_hash="aa",
        entry_hash="bb",
    )
    base.update(overrides)
    return types.SimpleNamespace(**base)


class TestFromAuditChainEntry:
    def test_full_context_summary_from_details(self):
        entry = _audit_entry(
            details={
                "agent_id": "openclaw",
                "user_id": "123",
                "block_reason": "injection detected",
                "action_taken": "blocked",
                "summary": "explicit summary",
            }
        )
        ev = event_adapter.from_audit_chain_entry(entry)
        assert isinstance(ev, SecurityEvent)
        assert ev.summary == "explicit summary"
        assert ev.agent_id == "openclaw"
        assert ev.user_id == "123"
        assert ev.action_taken == "blocked"
        assert ev.severity == Severity.HIGH
        assert ev.chain_hash == "bb"
        assert ev.prev_hash == "aa"

    def test_summary_falls_back_to_block_reason(self):
        entry = _audit_entry(details={"block_reason": "bad prompt"})
        assert event_adapter.from_audit_chain_entry(entry).summary == "bad prompt"

    def test_summary_falls_back_to_message(self):
        entry = _audit_entry(details={"message": "hello msg"})
        assert event_adapter.from_audit_chain_entry(entry).summary == "hello msg"

    def test_summary_from_non_allowed_action(self):
        entry = _audit_entry(details={"action_taken": "sanitized"})
        assert event_adapter.from_audit_chain_entry(entry).summary == "sanitized: prompt_blocked"

    def test_summary_from_agent_id(self):
        entry = _audit_entry(details={"agent_id": "hermes"})
        assert event_adapter.from_audit_chain_entry(entry).summary == "hermes: prompt_blocked"

    def test_summary_falls_back_to_event_type(self):
        entry = _audit_entry(details={})
        assert event_adapter.from_audit_chain_entry(entry).summary == "prompt_blocked"

    def test_missing_timestamp_uses_now(self):
        entry = _audit_entry(timestamp="")
        ev = event_adapter.from_audit_chain_entry(entry)
        assert ev.timestamp  # non-empty ISO fallback

    def test_user_key_fallback(self):
        entry = _audit_entry(details={"user": "456"})
        assert event_adapter.from_audit_chain_entry(entry).user_id == "456"

    def test_conversion_error_path(self):
        class Exploder:
            @property
            def timestamp(self):
                raise ValueError("boom")

        ev = event_adapter.from_audit_chain_entry(Exploder())
        assert ev.event_type == "audit_entry"
        assert ev.summary == "Conversion error"


class TestFromPipelineResult:
    def test_blocked(self):
        result = types.SimpleNamespace(blocked=True, block_reason="bad", sanitized=False)
        ev = event_adapter.from_pipeline_result(result, user_id="42")
        assert ev.event_type == "inbound_blocked"
        assert ev.severity == Severity.HIGH
        assert ev.action_taken == "blocked"
        assert ev.user_id == "42"
        assert ev.summary == "bad"

    def test_sanitized(self):
        result = types.SimpleNamespace(blocked=False, block_reason="", sanitized=True)
        ev = event_adapter.from_pipeline_result(result)
        assert ev.event_type == "inbound_allowed"
        assert ev.severity == Severity.MEDIUM
        assert ev.action_taken == "sanitized"
        assert ev.user_id is None

    def test_allowed(self):
        result = types.SimpleNamespace(blocked=False, block_reason="", sanitized=False)
        ev = event_adapter.from_pipeline_result(result)
        assert ev.severity == Severity.INFO
        assert ev.action_taken == "allowed"
        assert ev.summary == "inbound_allowed"

    def test_conversion_error_path(self):
        class Exploder:
            @property
            def blocked(self):
                raise RuntimeError("boom")

        ev = event_adapter.from_pipeline_result(Exploder())
        assert ev.event_type == "pipeline_result"
        assert ev.summary == "Conversion error"


class TestFromEgressAttempt:
    def test_dict_blocked_with_reason(self):
        ev = event_adapter.from_egress_attempt(
            {"domain": "evil.com", "blocked": True, "reason": "denylist", "agent_id": "a1"}
        )
        assert ev.event_type == "egress_denied"
        assert ev.severity == Severity.HIGH
        assert ev.summary == "Egress to evil.com: blocked (denylist)"
        assert ev.agent_id == "a1"

    def test_dict_allowed_without_reason(self):
        ev = event_adapter.from_egress_attempt({"domain": "ok.com", "blocked": False})
        assert ev.event_type == "egress_allowed"
        assert ev.severity == Severity.INFO
        assert ev.summary == "Egress to ok.com: allowed"

    def test_object_form(self):
        attempt = types.SimpleNamespace(
            domain="api.example.com", blocked=True, reason="quota", agent_id="hermes"
        )
        ev = event_adapter.from_egress_attempt(attempt)
        assert ev.event_type == "egress_denied"
        assert ev.details == {"domain": "api.example.com", "blocked": True, "reason": "quota"}

    def test_conversion_error_path(self):
        class Exploder:
            @property
            def domain(self):
                raise RuntimeError("boom")

        ev = event_adapter.from_egress_attempt(Exploder())
        assert ev.event_type == "egress_attempt"
        assert ev.summary == "Conversion error"


class TestFromAnomalyAlert:
    def test_dict_form(self):
        ev = event_adapter.from_anomaly_alert(
            {"title": "Spike", "severity": "critical", "details": {"count": 9}}
        )
        assert ev.event_type == "anomaly_detected"
        assert ev.severity == Severity.CRITICAL
        assert ev.summary == "Spike"
        assert ev.details == {"count": 9}

    def test_object_form_with_defaults(self):
        alert = types.SimpleNamespace(title=None, severity="medium", details=None)
        ev = event_adapter.from_anomaly_alert(alert)
        assert ev.summary == "Anomaly"
        assert ev.severity == Severity.MEDIUM
        assert ev.details == {}

    def test_conversion_error_path(self):
        class Exploder:
            @property
            def title(self):
                raise RuntimeError("boom")

        ev = event_adapter.from_anomaly_alert(Exploder())
        assert ev.event_type == "anomaly_alert"
        assert ev.summary == "Conversion error"


class TestFromDict:
    def test_full_dict(self):
        ev = event_adapter.from_dict(
            {
                "event_type": "egress_denied",
                "severity": "high",
                "timestamp": "2026-06-12T00:00:00+00:00",
                "source_module": "egress_filter",
                "agent_id": "a1",
                "user_id": 42,
                "action_taken": "blocked",
                "summary": "denied",
                "extra": "kept",
            }
        )
        assert ev.event_type == "egress_denied"
        assert ev.user_id == "42"
        assert ev.details == {"extra": "kept"}

    def test_minimal_dict_uses_fallbacks(self):
        ev = event_adapter.from_dict({"type": "log_event", "message": "hi", "source": "syslog"})
        assert ev.event_type == "log_event"
        assert ev.summary == "hi"
        assert ev.source_module == "syslog"
        assert ev.action_taken == "unknown"

    def test_conversion_error_path(self):
        ev = event_adapter.from_dict(None)  # type: ignore[arg-type]
        assert ev.event_type == "unknown"
        assert ev.summary == "Conversion error"


class TestCollectRecentEvents:
    async def test_none_store_returns_empty(self):
        assert await event_adapter.collect_recent_events(None) == []

    async def test_collects_and_converts(self):
        store = MagicMock()
        store.get_recent_entries = AsyncMock(
            return_value=[_audit_entry(), _audit_entry(severity="info")]
        )
        events = await event_adapter.collect_recent_events(store, limit=5)
        assert len(events) == 2
        assert all(isinstance(e, SecurityEvent) for e in events)
        store.get_recent_entries.assert_awaited_once_with(limit=5)

    async def test_severity_filter_drops_lower(self):
        store = MagicMock()
        store.get_recent_entries = AsyncMock(
            return_value=[
                _audit_entry(severity="info"),
                _audit_entry(severity="critical"),
                _audit_entry(severity="medium"),
            ]
        )
        events = await event_adapter.collect_recent_events(store, severity_filter="high")
        assert len(events) == 1
        assert events[0].severity == Severity.CRITICAL

    async def test_store_error_returns_empty(self):
        store = MagicMock()
        store.get_recent_entries = AsyncMock(side_effect=RuntimeError("db down"))
        assert await event_adapter.collect_recent_events(store) == []


# ---------------------------------------------------------------------------
# websocket.py — _coerce_to_ws_event
# ---------------------------------------------------------------------------


class TestCoerceToWSEventExtra:
    def test_wsevent_passthrough(self):
        ev = WSEvent(type=WSEventType.LOG_EVENT, summary="x")
        assert _coerce_to_ws_event(ev) is ev

    @pytest.mark.parametrize(
        "etype,expected",
        [
            ("egress_allowed", WSEventType.EGRESS_EVENT),
            ("approval_event", WSEventType.APPROVAL_EVENT),
            ("service_event", WSEventType.SERVICE_EVENT),
            ("log_event", WSEventType.LOG_EVENT),
            ("inbound_allowed", WSEventType.SECURITY_EVENT),
            ("anomaly_detected", WSEventType.SECURITY_EVENT),
            ("totally_unknown", WSEventType.SECURITY_EVENT),
        ],
    )
    def test_type_mapping(self, etype, expected):
        ev = _coerce_to_ws_event({"type": etype, "summary": "s"})
        assert ev is not None and ev.type == expected

    def test_event_type_key_fallback(self):
        ev = _coerce_to_ws_event({"event_type": "egress_denied", "summary": "s"})
        assert ev is not None and ev.type == WSEventType.EGRESS_EVENT

    def test_details_excludes_reserved_keys(self):
        ev = _coerce_to_ws_event(
            {
                "type": "log_event",
                "severity": "low",
                "summary": "s",
                "message": "m",
                "timestamp": "2026-06-12T00:00:00+00:00",
                "domain": "x.com",
            }
        )
        assert ev is not None
        assert ev.details == {"domain": "x.com"}
        assert ev.severity == Severity.LOW
        assert ev.source_module == ""

    def test_source_key_fallback(self):
        ev = _coerce_to_ws_event({"type": "log_event", "source": "syslog"})
        assert ev is not None and ev.source_module == "syslog"

    def test_message_fallback_for_summary(self):
        ev = _coerce_to_ws_event({"type": "log_event", "message": "hello"})
        assert ev is not None and ev.summary == "hello"

    def test_unknown_severity_defaults_to_info(self):
        ev = _coerce_to_ws_event({"type": "log_event", "severity": "weird"})
        assert ev is not None and ev.severity == Severity.INFO

    def test_invalid_dict_returns_none(self):
        # timestamp must be str — int triggers pydantic validation error path
        assert _coerce_to_ws_event({"type": "log_event", "timestamp": 12345}) is None


# ---------------------------------------------------------------------------
# websocket.py — SOCWebSocketHandler internals
# ---------------------------------------------------------------------------


class _FakeBus:
    def __init__(self):
        self.cb = None
        self.unsubscribed = False

    async def subscribe(self, cb):
        self.cb = cb

    async def unsubscribe(self, cb):
        self.unsubscribed = True


async def _spin(turns: int = 5):
    for _ in range(turns):
        await asyncio.sleep(0)


class TestSendEventAndKeepalive:
    async def test_send_event_serializes(self):
        ws = MagicMock()
        ws.send_text = AsyncMock()
        handler = SOCWebSocketHandler(ws=ws, user_id="u1")
        await handler._send_event(WSEvent(type=WSEventType.LOG_EVENT, summary="hi"))
        payload = json.loads(ws.send_text.call_args.args[0])
        assert payload["type"] == "log_event"
        assert payload["summary"] == "hi"

    async def test_send_event_swallows_transport_error(self):
        ws = MagicMock()
        ws.send_text = AsyncMock(side_effect=RuntimeError("gone"))
        handler = SOCWebSocketHandler(ws=ws, user_id="u1")
        await handler._send_event(WSEvent(type=WSEventType.LOG_EVENT))  # must not raise

    async def test_keepalive_sends_pings(self, monkeypatch):
        monkeypatch.setattr(ws_mod, "_KEEPALIVE_INTERVAL", 0)
        ws = MagicMock()
        ws.send_text = AsyncMock()
        handler = SOCWebSocketHandler(ws=ws, user_id="u1")
        task = asyncio.create_task(handler._keepalive_loop())
        await _spin(20)
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task
        assert ws.send_text.await_count >= 1
        payload = json.loads(ws.send_text.call_args.args[0])
        assert payload["type"] == "keepalive"
        assert payload["summary"] == "ping"

    async def test_keepalive_breaks_on_construction_error(self, monkeypatch):
        monkeypatch.setattr(ws_mod, "_KEEPALIVE_INTERVAL", 0)

        def boom(*args, **kwargs):
            raise RuntimeError("cannot build event")

        monkeypatch.setattr(ws_mod, "WSEvent", boom)
        ws = MagicMock()
        ws.send_text = AsyncMock()
        handler = SOCWebSocketHandler(ws=ws, user_id="u1")
        # Loop must exit via the break branch, not run forever
        await asyncio.wait_for(handler._keepalive_loop(), timeout=5)
        ws.send_text.assert_not_awaited()


class TestEventFanOut:
    async def test_none_bus_returns_immediately(self):
        handler = SOCWebSocketHandler(ws=MagicMock(), user_id="u1")
        await handler._event_fan_out(None)  # must not hang or raise

    async def test_fan_out_filters_and_forwards(self, monkeypatch):
        ws = MagicMock()
        ws.send_text = AsyncMock()
        handler = SOCWebSocketHandler(ws=ws, user_id="u1")
        handler.subscriptions = {"log_event"}
        bus = _FakeBus()

        task = asyncio.create_task(handler._event_fan_out(bus))
        await _spin()
        assert bus.cb is not None

        await bus.cb(None)  # skipped (None sentinel)
        await bus.cb("garbage")  # skipped (coerce → None)
        await bus.cb({"type": "egress_event", "summary": "filtered"})  # filtered out
        await bus.cb({"type": "log_event", "summary": "delivered"})  # forwarded
        await _spin(10)

        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task
        assert bus.unsubscribed is True
        assert ws.send_text.await_count == 1
        payload = json.loads(ws.send_text.call_args.args[0])
        assert payload["summary"] == "delivered"

    async def test_fan_out_survives_coerce_exception(self, monkeypatch):
        ws = MagicMock()
        ws.send_text = AsyncMock()
        handler = SOCWebSocketHandler(ws=ws, user_id="u1")
        bus = _FakeBus()

        orig = ws_mod._coerce_to_ws_event

        def fragile(raw):
            if isinstance(raw, dict) and raw.get("boom"):
                raise RuntimeError("coerce failure")
            return orig(raw)

        monkeypatch.setattr(ws_mod, "_coerce_to_ws_event", fragile)

        task = asyncio.create_task(handler._event_fan_out(bus))
        await _spin()
        await bus.cb({"boom": True})  # exception logged, loop continues
        await bus.cb({"type": "log_event", "summary": "after-error"})
        await _spin(10)

        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task
        assert ws.send_text.await_count == 1
        assert json.loads(ws.send_text.call_args.args[0])["summary"] == "after-error"


class TestHandlerRun:
    def _handler(self, receive_effects: List[Any]) -> SOCWebSocketHandler:
        ws = MagicMock()
        ws.send_text = AsyncMock()
        ws.receive_text = AsyncMock(side_effect=receive_effects)
        return SOCWebSocketHandler(ws=ws, user_id="u1")

    async def test_initial_subscribe_message_sets_filter(self):
        handler = self._handler(
            [json.dumps({"subscribe": ["log_event", "egress_event"]}), WebSocketDisconnect()]
        )
        await asyncio.wait_for(handler.run(None), timeout=10)
        assert handler.subscriptions == {"log_event", "egress_event"}

    async def test_initial_invalid_json_ignored(self):
        handler = self._handler(["{not-json", WebSocketDisconnect()])
        await asyncio.wait_for(handler.run(None), timeout=10)
        assert handler.subscriptions == set()

    async def test_initial_timeout_subscribes_to_all(self):
        handler = self._handler([asyncio.TimeoutError(), WebSocketDisconnect()])
        await asyncio.wait_for(handler.run(None), timeout=10)
        assert handler.subscriptions == set()

    async def test_command_message_updates_subscription(self):
        handler = self._handler(
            [
                asyncio.TimeoutError(),  # no initial filter
                json.dumps({"subscribe": ["service_event"]}),  # runtime command
                WebSocketDisconnect(),
            ]
        )
        await asyncio.wait_for(handler.run(None), timeout=10)
        assert handler.subscriptions == {"service_event"}

    async def test_command_invalid_json_ignored(self):
        handler = self._handler([asyncio.TimeoutError(), "][bad", WebSocketDisconnect()])
        await asyncio.wait_for(handler.run(None), timeout=10)
        assert handler.subscriptions == set()

    async def test_inner_timeout_continues_loop(self):
        handler = self._handler(
            [
                json.dumps({"subscribe": ["log_event"]}),
                asyncio.TimeoutError(),  # main loop keepalive timeout → continue
                WebSocketDisconnect(),
            ]
        )
        await asyncio.wait_for(handler.run(None), timeout=10)
        assert handler.subscriptions == {"log_event"}


# ---------------------------------------------------------------------------
# websocket.py — ws_soc_endpoint auth paths
# ---------------------------------------------------------------------------


def _make_ws(token: str = "", headers: Optional[Dict[str, str]] = None) -> MagicMock:
    ws = MagicMock()
    ws.query_params = {"token": token} if token else {}
    ws.headers = headers or {}
    ws.close = AsyncMock()
    ws.accept = AsyncMock()
    ws.send_text = AsyncMock()
    ws.receive_text = AsyncMock(side_effect=WebSocketDisconnect())
    return ws


class TestWSSOCEndpoint:
    async def test_unauthorized_closes_4003(self, clean_auth_env):
        _block_run_secrets(clean_auth_env)
        ws = _make_ws()
        await ws_soc_endpoint(ws)
        ws.close.assert_awaited_once_with(code=4003, reason="Unauthorized")
        ws.accept.assert_not_awaited()

    async def test_invalid_token_closes_4003(self, clean_auth_env):
        _block_run_secrets(clean_auth_env)
        ws = _make_ws(token="not-a-real-token")
        await ws_soc_endpoint(ws)
        ws.close.assert_awaited_once_with(code=4003, reason="Unauthorized")

    async def test_valid_ws_token_accepts(self, clean_auth_env):
        token = issue_ws_token("user-555")
        ws = _make_ws(token=token)
        await asyncio.wait_for(ws_soc_endpoint(ws), timeout=10)
        ws.accept.assert_awaited_once()
        ws.close.assert_not_awaited()

    async def test_bearer_header_fallback(self, clean_auth_env):
        token = issue_ws_token("user-556")
        ws = _make_ws(headers={"authorization": f"Bearer {token}"})
        await asyncio.wait_for(ws_soc_endpoint(ws), timeout=10)
        ws.accept.assert_awaited_once()

    async def test_raw_gateway_password_fallback(self, clean_auth_env):
        clean_auth_env.setenv("AGENTSHROUD_GATEWAY_PASSWORD", "gw-pass-x")
        ws = _make_ws(token="gw-pass-x")
        await asyncio.wait_for(ws_soc_endpoint(ws), timeout=10)
        ws.accept.assert_awaited_once()
        ws.close.assert_not_awaited()

    async def test_handler_exception_is_swallowed(self, clean_auth_env, monkeypatch):
        token = issue_ws_token("user-557")
        ws = _make_ws(token=token)
        monkeypatch.setattr(
            ws_mod.SOCWebSocketHandler, "run", AsyncMock(side_effect=RuntimeError("boom"))
        )
        await asyncio.wait_for(ws_soc_endpoint(ws), timeout=10)  # must not raise
        ws.accept.assert_awaited_once()
