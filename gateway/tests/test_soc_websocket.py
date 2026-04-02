# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for gateway/soc/websocket.py — SOCWebSocketHandler unit tests."""

from __future__ import annotations

import asyncio
import json
from unittest.mock import MagicMock

import pytest

from gateway.soc.models import WSEventType
from gateway.soc.websocket import SOCWebSocketHandler, _coerce_to_ws_event


class TestSOCWebSocketHandlerImport:
    def test_import(self):
        assert SOCWebSocketHandler is not None

    def test_instantiate(self):
        mock_ws = MagicMock()
        handler = SOCWebSocketHandler(ws=mock_ws, user_id="test-user")
        assert handler.user_id == "test-user"
        assert handler.subscriptions == set()


class TestSubscriptionFilter:
    """Test event filtering via the subscriptions set (mirrors _event_fan_out logic)."""

    def _make_handler(self, subs=None) -> SOCWebSocketHandler:
        mock_ws = MagicMock()
        handler = SOCWebSocketHandler(ws=mock_ws, user_id="u1")
        if subs is not None:
            handler.subscriptions = set(subs)
        return handler

    def _matches(self, handler: SOCWebSocketHandler, event_dict: dict) -> bool:
        """Replicate the filter logic from _event_fan_out."""
        ev = _coerce_to_ws_event(event_dict)
        if ev is None:
            return False
        return not handler.subscriptions or ev.type.value in handler.subscriptions

    def test_no_subscription_accepts_security_event(self):
        h = self._make_handler()
        assert self._matches(h, {"type": "security_event", "summary": "x"}) is True

    def test_no_subscription_accepts_log_event(self):
        h = self._make_handler()
        assert self._matches(h, {"type": "log_event", "summary": "x"}) is True

    def test_subscription_filters_correctly(self):
        h = self._make_handler(subs=["security_event"])
        assert self._matches(h, {"type": "security_event", "summary": "x"}) is True
        assert self._matches(h, {"type": "log_event", "summary": "x"}) is False

    def test_multi_subscription(self):
        h = self._make_handler(subs=["security_event", "egress_event"])
        assert self._matches(h, {"type": "security_event", "summary": "x"}) is True
        assert self._matches(h, {"type": "egress_event", "summary": "x"}) is True
        assert self._matches(h, {"type": "log_event", "summary": "x"}) is False


class TestCoerceToWSEvent:
    def test_security_event(self):
        ev = _coerce_to_ws_event({"type": "security_event", "summary": "test"})
        assert ev is not None
        assert ev.type == WSEventType.SECURITY_EVENT

    def test_legacy_inbound_blocked(self):
        ev = _coerce_to_ws_event({"type": "inbound_blocked", "summary": "blocked"})
        assert ev is not None
        assert ev.type == WSEventType.SECURITY_EVENT

    def test_egress_denied(self):
        ev = _coerce_to_ws_event({"type": "egress_denied", "summary": "denied"})
        assert ev is not None
        assert ev.type == WSEventType.EGRESS_EVENT

    def test_returns_none_on_bad_input(self):
        assert _coerce_to_ws_event(None) is None
        assert _coerce_to_ws_event("not-a-dict") is None

    def test_preserves_severity(self):
        ev = _coerce_to_ws_event({"type": "security_event", "severity": "critical", "summary": "x"})
        from gateway.soc.models import Severity

        assert ev.severity == Severity.CRITICAL
