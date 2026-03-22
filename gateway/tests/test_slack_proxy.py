# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for SlackAPIProxy — outbound Slack API proxying through SecurityPipeline."""
from __future__ import annotations

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from gateway.proxy.slack_proxy import SlackAPIProxy


# ─── Helpers ─────────────────────────────────────────────────────────────────

def _make_proxy(pipeline=None, owner_slack_user_id: str = "") -> SlackAPIProxy:
    """Create a SlackAPIProxy with test credentials and no real I/O."""
    with patch("gateway.proxy.slack_proxy._read_secret_static", return_value=""):
        proxy = SlackAPIProxy(pipeline=pipeline, owner_slack_user_id=owner_slack_user_id)
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


# ─── Owner vs Collaborator Channel Filtering ─────────────────────────────────

_OWNER_UID = "U01J37F6YT0"
_COLLAB_CHANNEL = "C_OTHER_CHANNEL"


class TestOwnerChannelFiltering:
    """P0 security: Slack outbound must differentiate owner vs collaborator channels."""

    def test_is_owner_channel_matches_owner_uid(self):
        proxy = _make_proxy(owner_slack_user_id=_OWNER_UID)
        assert proxy._is_owner_channel(_OWNER_UID) is True

    def test_is_owner_channel_no_match_for_other(self):
        proxy = _make_proxy(owner_slack_user_id=_OWNER_UID)
        assert proxy._is_owner_channel(_COLLAB_CHANNEL) is False

    def test_is_owner_channel_empty_owner_uid_always_false(self):
        # Patch env var to ensure no fallthrough when explicit empty string passed
        with patch.dict("os.environ", {"AGENTSHROUD_SLACK_OWNER_USER_ID": ""}):
            proxy = _make_proxy(owner_slack_user_id="")
        assert proxy._is_owner_channel(_OWNER_UID) is False

    @pytest.mark.asyncio
    async def test_owner_channel_uses_full_trust(self):
        """Owner channel: pipeline called with user_trust_level=FULL, message forwarded."""
        pipeline = MagicMock()
        result = MagicMock()
        result.blocked = False
        result.sanitized_message = None
        pipeline.process_outbound = AsyncMock(return_value=result)

        proxy = _make_proxy(pipeline=pipeline, owner_slack_user_id=_OWNER_UID)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        body = json.dumps({"channel": _OWNER_UID, "text": "owner reply"}).encode()
        resp = await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        assert resp == {"ok": True}
        call_kwargs = pipeline.process_outbound.call_args
        assert call_kwargs.kwargs.get("user_trust_level") == "FULL" or \
               (call_kwargs.args and False)  # kwargs form

    @pytest.mark.asyncio
    async def test_non_owner_high_risk_leakage_blocked_before_pipeline(self):
        """Non-owner channel: high-risk leakage detected before pipeline → blocked."""
        pipeline = MagicMock()
        pipeline.process_outbound = AsyncMock()

        proxy = _make_proxy(pipeline=pipeline, owner_slack_user_id=_OWNER_UID)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        with patch(
            "gateway.proxy.telegram_proxy.TelegramAPIProxy._contains_high_risk_collaborator_leakage",
            return_value=True,
        ):
            body = json.dumps({"channel": _COLLAB_CHANNEL, "text": "contains 192.168.7.25"}).encode()
            resp = await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        assert resp["ok"] is False
        assert resp["error"] == "content_policy_violation"
        pipeline.process_outbound.assert_not_called()
        proxy._call_slack_api.assert_not_called()
        assert proxy.get_stats()["outbound_blocked"] == 1

    @pytest.mark.asyncio
    async def test_non_owner_tailscale_hostname_blocked(self):
        """Non-owner channel: Tailscale hostname triggers leakage pre-check → blocked."""
        pipeline = MagicMock()
        pipeline.process_outbound = AsyncMock()

        proxy = _make_proxy(pipeline=pipeline, owner_slack_user_id=_OWNER_UID)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        with patch(
            "gateway.proxy.telegram_proxy.TelegramAPIProxy._contains_high_risk_collaborator_leakage",
            return_value=True,
        ):
            body = json.dumps({"channel": _COLLAB_CHANNEL, "text": "raspberrypi.tail240ea8.ts.net"}).encode()
            resp = await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        assert resp["ok"] is False
        assert resp["error"] == "content_policy_violation"
        pipeline.process_outbound.assert_not_called()

    @pytest.mark.asyncio
    async def test_non_owner_pipeline_exception_fail_closed(self):
        """Non-owner channel: pipeline exception → blocked (fail-closed)."""
        pipeline = MagicMock()
        pipeline.process_outbound = AsyncMock(side_effect=RuntimeError("pipeline fault"))

        proxy = _make_proxy(pipeline=pipeline, owner_slack_user_id=_OWNER_UID)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        with patch(
            "gateway.proxy.telegram_proxy.TelegramAPIProxy._contains_high_risk_collaborator_leakage",
            return_value=False,
        ):
            body = json.dumps({"channel": _COLLAB_CHANNEL, "text": "safe text"}).encode()
            resp = await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        assert resp["ok"] is False
        assert resp["error"] == "content_policy_violation"
        proxy._call_slack_api.assert_not_called()

    @pytest.mark.asyncio
    async def test_owner_pipeline_exception_fail_open(self):
        """Owner channel: pipeline exception → logged but message still forwarded."""
        pipeline = MagicMock()
        pipeline.process_outbound = AsyncMock(side_effect=RuntimeError("pipeline fault"))

        proxy = _make_proxy(pipeline=pipeline, owner_slack_user_id=_OWNER_UID)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        body = json.dumps({"channel": _OWNER_UID, "text": "owner message"}).encode()
        resp = await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        # Owner: exception is logged but message proceeds to Slack
        assert resp == {"ok": True}
        proxy._call_slack_api.assert_called_once()

    @pytest.mark.asyncio
    async def test_non_owner_info_filter_redaction_blocks(self):
        """Non-owner channel: pipeline passes but info_filter_redaction_count > 0 → blocked."""
        pipeline = MagicMock()
        result = MagicMock()
        result.blocked = False
        result.sanitized_message = "[PRIVATE_IP]"
        result.info_filter_redaction_count = 1
        pipeline.process_outbound = AsyncMock(return_value=result)

        proxy = _make_proxy(pipeline=pipeline, owner_slack_user_id=_OWNER_UID)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        with patch(
            "gateway.proxy.telegram_proxy.TelegramAPIProxy._contains_high_risk_collaborator_leakage",
            return_value=False,
        ):
            body = json.dumps({"channel": _COLLAB_CHANNEL, "text": "192.168.7.25"}).encode()
            resp = await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        assert resp["ok"] is False
        assert resp["error"] == "content_policy_violation"
        proxy._call_slack_api.assert_not_called()

    @pytest.mark.asyncio
    async def test_non_owner_clean_message_passes(self):
        """Non-owner channel: clean message with no leakage passes through."""
        pipeline = MagicMock()
        result = MagicMock()
        result.blocked = False
        result.sanitized_message = None
        result.info_filter_redaction_count = 0
        pipeline.process_outbound = AsyncMock(return_value=result)

        proxy = _make_proxy(pipeline=pipeline, owner_slack_user_id=_OWNER_UID)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        with patch(
            "gateway.proxy.telegram_proxy.TelegramAPIProxy._contains_high_risk_collaborator_leakage",
            return_value=False,
        ):
            body = json.dumps({"channel": _COLLAB_CHANNEL, "text": "Hello, here is your answer."}).encode()
            resp = await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        assert resp == {"ok": True}
        proxy._call_slack_api.assert_called_once()


# ─── Socket Mode Relay (apps.connections.open interception) ───────────────────

class TestSocketModeRelay:
    @pytest.mark.asyncio
    async def test_connections_open_rewrites_url(self):
        """apps.connections.open: real WSS URL is stored and relay URL returned."""
        proxy = _make_proxy()
        real_wss = "wss://wss-primary.slack.com/link?ticket=abc123&app_id=A01"
        proxy._call_slack_api = AsyncMock(
            return_value={"ok": True, "url": real_wss}
        )

        body = json.dumps({"token": "xapp-test"}).encode()
        resp = await proxy.proxy_outbound("apps.connections.open", body, "application/json")

        assert resp["ok"] is True
        relay_url = resp["url"]
        assert relay_url.startswith("ws://")
        assert "/slack-ws-relay?t=" in relay_url

        # Token maps to the real URL
        token = relay_url.split("t=")[1]
        assert proxy._relay_tokens.get(token) == real_wss

    @pytest.mark.asyncio
    async def test_connections_open_slack_error_passthrough(self):
        """apps.connections.open: Slack error response returned unchanged."""
        proxy = _make_proxy()
        proxy._call_slack_api = AsyncMock(
            return_value={"ok": False, "error": "invalid_auth"}
        )

        body = json.dumps({"token": "xapp-bad"}).encode()
        resp = await proxy.proxy_outbound("apps.connections.open", body, "application/json")

        assert resp == {"ok": False, "error": "invalid_auth"}
        assert not proxy._relay_tokens  # No token stored on error

    @pytest.mark.asyncio
    async def test_connections_open_missing_url_passthrough(self):
        """apps.connections.open: response without url field returned unchanged."""
        proxy = _make_proxy()
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        body = json.dumps({"token": "xapp-test"}).encode()
        resp = await proxy.proxy_outbound("apps.connections.open", body, "application/json")

        assert resp == {"ok": True}
        assert not proxy._relay_tokens

    @pytest.mark.asyncio
    async def test_connections_open_skips_content_pipeline(self):
        """apps.connections.open: pipeline is NOT invoked (not a message method)."""
        pipeline = MagicMock()
        pipeline.process_outbound = AsyncMock()
        proxy = _make_proxy(pipeline=pipeline)
        proxy._call_slack_api = AsyncMock(
            return_value={"ok": True, "url": "wss://slack.com/link?ticket=x"}
        )

        body = json.dumps({"token": "xapp-test"}).encode()
        await proxy.proxy_outbound("apps.connections.open", body, "application/json")

        pipeline.process_outbound.assert_not_called()

    def test_consume_relay_token_one_time(self):
        """consume_relay_token returns the URL once then None."""
        proxy = _make_proxy()
        proxy._relay_tokens["tok1"] = "wss://slack.com/link?ticket=x"

        assert proxy.consume_relay_token("tok1") == "wss://slack.com/link?ticket=x"
        assert proxy.consume_relay_token("tok1") is None  # consumed

    def test_consume_relay_token_unknown(self):
        """consume_relay_token returns None for unknown tokens."""
        proxy = _make_proxy()
        assert proxy.consume_relay_token("nonexistent") is None

    @pytest.mark.asyncio
    async def test_each_reconnect_issues_unique_token(self):
        """Each call to apps.connections.open issues a distinct relay token."""
        proxy = _make_proxy()
        proxy._call_slack_api = AsyncMock(
            return_value={"ok": True, "url": "wss://wss-primary.slack.com/link?ticket=t1"}
        )

        body = json.dumps({"token": "xapp-test"}).encode()
        resp1 = await proxy.proxy_outbound("apps.connections.open", body, "application/json")
        resp2 = await proxy.proxy_outbound("apps.connections.open", body, "application/json")

        token1 = resp1["url"].split("t=")[1]
        token2 = resp2["url"].split("t=")[1]
        assert token1 != token2
