# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for SlackAPIProxy — outbound Slack API proxying through SecurityPipeline."""
from __future__ import annotations

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from gateway.proxy.slack_proxy import SlackAPIProxy


# ─── Helpers ─────────────────────────────────────────────────────────────────

def _make_proxy(pipeline=None) -> SlackAPIProxy:
    """Create a SlackAPIProxy with test credentials and no real I/O."""
    with patch("gateway.proxy.slack_proxy._read_secret_static", return_value=""):
        proxy = SlackAPIProxy(pipeline=pipeline)
    proxy._bot_token = "xoxb-test-token"
    return proxy


# ─── Outbound Proxy ───────────────────────────────────────────────────────────

class TestProxyOutbound:
    @pytest.mark.asyncio
    async def test_chat_postmessage_content_scanned(self):
        pipeline = MagicMock()
        pipeline_result = MagicMock()
        pipeline_result.blocked = False
        pipeline_result.sanitized_message = "safe text"
        pipeline.process_outbound = AsyncMock(return_value=pipeline_result)

        proxy = _make_proxy(pipeline=pipeline)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        body = json.dumps({"channel": "C123", "text": "bot response"}).encode()
        result = await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        pipeline.process_outbound.assert_called_once()
        proxy._call_slack_api.assert_called_once()
        assert result == {"ok": True}

    @pytest.mark.asyncio
    async def test_outbound_blocked_returns_error(self):
        pipeline = MagicMock()
        pipeline_result = MagicMock()
        pipeline_result.blocked = True
        pipeline_result.block_reason = "credential_leak"
        pipeline.process_outbound = AsyncMock(return_value=pipeline_result)

        proxy = _make_proxy(pipeline=pipeline)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        body = json.dumps({"channel": "C123", "text": "secret_key=abc123"}).encode()
        result = await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        assert result["ok"] is False
        assert result["error"] == "content_policy_violation"
        proxy._call_slack_api.assert_not_called()

    @pytest.mark.asyncio
    async def test_non_message_method_not_scanned(self):
        pipeline = MagicMock()
        pipeline.process_outbound = AsyncMock()

        proxy = _make_proxy(pipeline=pipeline)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        body = json.dumps({"channel": "C123", "timestamp": "1234"}).encode()
        result = await proxy.proxy_outbound("reactions.add", body, "application/json")

        pipeline.process_outbound.assert_not_called()
        proxy._call_slack_api.assert_called_once()

    @pytest.mark.asyncio
    async def test_system_notification_skips_pipeline(self):
        pipeline = MagicMock()
        pipeline.process_outbound = AsyncMock()

        proxy = _make_proxy(pipeline=pipeline)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        body = json.dumps({"channel": "C123", "text": "AgentShroud online"}).encode()
        result = await proxy.proxy_outbound("chat.postMessage", body, "application/json", is_system=True)

        pipeline.process_outbound.assert_not_called()
        assert result == {"ok": True}

    @pytest.mark.asyncio
    async def test_no_bot_token_returns_error(self):
        proxy = _make_proxy()
        proxy._bot_token = ""

        body = json.dumps({"channel": "C123", "text": "hello"}).encode()
        result = await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        assert result["ok"] is False
        assert result["error"] == "not_configured"

    @pytest.mark.asyncio
    async def test_chat_update_content_scanned(self):
        pipeline = MagicMock()
        pipeline_result = MagicMock()
        pipeline_result.blocked = False
        pipeline_result.sanitized_message = None
        pipeline.process_outbound = AsyncMock(return_value=pipeline_result)

        proxy = _make_proxy(pipeline=pipeline)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        body = json.dumps({"channel": "C123", "ts": "123.456", "text": "updated"}).encode()
        await proxy.proxy_outbound("chat.update", body, "application/json")

        pipeline.process_outbound.assert_called_once()

    @pytest.mark.asyncio
    async def test_sanitized_text_replaces_original(self):
        pipeline = MagicMock()
        pipeline_result = MagicMock()
        pipeline_result.blocked = False
        pipeline_result.sanitized_message = "sanitized output"
        pipeline.process_outbound = AsyncMock(return_value=pipeline_result)

        proxy = _make_proxy(pipeline=pipeline)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        body = json.dumps({"channel": "C123", "text": "raw output"}).encode()
        await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        call_body = proxy._call_slack_api.call_args[0][1]
        assert call_body["text"] == "sanitized output"

    @pytest.mark.asyncio
    async def test_urlencoded_body_parsed(self):
        pipeline = MagicMock()
        pipeline_result = MagicMock()
        pipeline_result.blocked = False
        pipeline_result.sanitized_message = None
        pipeline.process_outbound = AsyncMock(return_value=pipeline_result)

        proxy = _make_proxy(pipeline=pipeline)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        body = b"channel=C123&text=hello+world"
        await proxy.proxy_outbound("chat.postMessage", body, "application/x-www-form-urlencoded")

        pipeline.process_outbound.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_stats_returns_counters(self):
        proxy = _make_proxy()
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        body = json.dumps({"channel": "C123", "text": "hi"}).encode()
        await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        stats = proxy.get_stats()
        assert stats["outbound_forwarded"] == 1
        assert stats["outbound_blocked"] == 0


# ─── WebhookReceiver Slack extraction ────────────────────────────────────────

class TestWebhookReceiverSlackExtraction:
    def test_extract_user_id_slack(self):
        from gateway.proxy.webhook_receiver import WebhookReceiver
        payload = {"event": {"type": "message", "user": "U_ABC123", "text": "hi"}}
        uid = WebhookReceiver._extract_user_id(payload, "slack")
        assert uid == "U_ABC123"

    def test_extract_username_slack(self):
        from gateway.proxy.webhook_receiver import WebhookReceiver
        payload = {"event": {"type": "message", "user": "U_ABC123", "username": "bob"}}
        name = WebhookReceiver._extract_username(payload, "slack")
        assert name == "bob"

    def test_extract_username_slack_fallback_to_user_id(self):
        from gateway.proxy.webhook_receiver import WebhookReceiver
        payload = {"event": {"type": "message", "user": "U_ABC123"}}
        name = WebhookReceiver._extract_username(payload, "slack")
        assert name == "U_ABC123"

    def test_extract_user_id_slack_missing_event(self):
        from gateway.proxy.webhook_receiver import WebhookReceiver
        payload = {"type": "event_callback"}  # no event key
        uid = WebhookReceiver._extract_user_id(payload, "slack")
        assert uid is None

    def test_extract_user_id_telegram_unchanged(self):
        from gateway.proxy.webhook_receiver import WebhookReceiver
        payload = {"message": {"from": {"id": 12345}, "text": "hello"}}
        uid = WebhookReceiver._extract_user_id(payload, "telegram")
        assert uid == "12345"
