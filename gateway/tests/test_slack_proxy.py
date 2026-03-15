# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for SlackAPIProxy — inbound event handling and outbound API proxying."""
from __future__ import annotations

import hashlib
import hmac
import json
import time
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from gateway.proxy.slack_proxy import SlackAPIProxy, _SLACK_SIG_VERSION


# ─── Helpers ─────────────────────────────────────────────────────────────────

_TEST_SIGNING_SECRET = "test_slack_signing_secret_abc123"
_OWNER_SLACK_ID = "U_OWNER_001"
_COLLAB_SLACK_ID = "U_COLLAB_001"
_STRANGER_SLACK_ID = "U_STRANGER_999"


def _make_slack_signature(secret: str, timestamp: str, body: bytes) -> str:
    sig_base = f"{_SLACK_SIG_VERSION}:{timestamp}:".encode() + body
    digest = hmac.new(secret.encode(), sig_base, hashlib.sha256).hexdigest()
    return f"{_SLACK_SIG_VERSION}={digest}"


def _make_event_payload(
    user_id: str = _STRANGER_SLACK_ID,
    text: str = "Hello",
    channel: str = "C_GENERAL",
    event_id: str = "Ev_test_001",
    bot_id: str | None = None,
    subtype: str | None = None,
) -> dict:
    event: dict = {
        "type": "message",
        "user": user_id,
        "text": text,
        "channel": channel,
        "ts": "1700000000.000001",
    }
    if bot_id:
        event["bot_id"] = bot_id
    if subtype:
        event["subtype"] = subtype
    return {
        "type": "event_callback",
        "event_id": event_id,
        "event": event,
    }


def _make_proxy(
    owner_id: str = _OWNER_SLACK_ID,
    collab_ids: list[str] | None = None,
    pipeline=None,
) -> SlackAPIProxy:
    """Create a SlackAPIProxy with test credentials and no real I/O."""
    with (
        patch("gateway.proxy.slack_proxy._read_secret_static", return_value=""),
        patch.dict("os.environ", {
            "AGENTSHROUD_SLACK_OWNER_USER_ID": owner_id,
            "AGENTSHROUD_COLLABORATOR_USER_IDS": ",".join(collab_ids or [_COLLAB_SLACK_ID]),
        }),
    ):
        proxy = SlackAPIProxy(pipeline=pipeline)
    proxy._bot_token = "xoxb-test-token"
    proxy._signing_secret = _TEST_SIGNING_SECRET
    return proxy


# ─── Signature Verification ───────────────────────────────────────────────────

class TestVerifySignature:
    def test_valid_signature_passes(self):
        proxy = _make_proxy()
        ts = str(int(time.time()))
        body = b'{"type": "event_callback"}'
        sig = _make_slack_signature(_TEST_SIGNING_SECRET, ts, body)
        assert proxy.verify_signature(ts, body, sig) is True

    def test_invalid_signature_fails(self):
        proxy = _make_proxy()
        ts = str(int(time.time()))
        body = b'{"type": "event_callback"}'
        assert proxy.verify_signature(ts, body, "v0=deadbeef") is False

    def test_timestamp_too_old_fails(self):
        proxy = _make_proxy()
        old_ts = str(int(time.time()) - 400)  # > 5 minutes old
        body = b'{"type": "event_callback"}'
        sig = _make_slack_signature(_TEST_SIGNING_SECRET, old_ts, body)
        assert proxy.verify_signature(old_ts, body, sig) is False

    def test_invalid_timestamp_format_fails(self):
        proxy = _make_proxy()
        sig = _make_slack_signature(_TEST_SIGNING_SECRET, "not_a_number", b"body")
        assert proxy.verify_signature("not_a_number", b"body", sig) is False

    def test_no_signing_secret_allows_all(self):
        proxy = _make_proxy()
        proxy._signing_secret = ""
        assert proxy.verify_signature("12345", b"body", "v0=garbage") is True


# ─── URL Verification ─────────────────────────────────────────────────────────

class TestHandleEvent:
    @pytest.mark.asyncio
    async def test_non_message_event_skipped(self):
        proxy = _make_proxy()
        payload = {"type": "event_callback", "event_id": "Ev1", "event": {"type": "reaction_added"}}
        result = await proxy.handle_event(payload)
        assert result["status"] == "skipped"

    @pytest.mark.asyncio
    async def test_bot_message_skipped(self):
        proxy = _make_proxy()
        payload = _make_event_payload(bot_id="BSOMEBOT")
        result = await proxy.handle_event(payload)
        assert result["status"] == "skipped"

    @pytest.mark.asyncio
    async def test_message_subtype_skipped(self):
        proxy = _make_proxy()
        payload = _make_event_payload(subtype="message_changed")
        result = await proxy.handle_event(payload)
        assert result["status"] == "skipped"

    @pytest.mark.asyncio
    async def test_duplicate_event_id_skipped(self):
        proxy = _make_proxy()
        proxy._send_slack_message = AsyncMock()
        proxy._forward_to_bot = AsyncMock()
        proxy._rbac.collaborator_user_ids = [_OWNER_SLACK_ID]  # force owner
        payload = _make_event_payload(user_id=_OWNER_SLACK_ID, event_id="Ev_dup")
        # Seed the dedup cache
        proxy._event_dedup["Ev_dup"] = time.time()
        result = await proxy.handle_event(payload)
        assert result["status"] == "skipped"
        assert "duplicate" in result["reason"]


# ─── RBAC Enforcement ─────────────────────────────────────────────────────────

class TestRBACEnforcement:
    @pytest.mark.asyncio
    async def test_stranger_queues_access_request(self):
        proxy = _make_proxy()
        proxy._send_slack_message = AsyncMock()
        proxy._notify_owner = AsyncMock()
        proxy._forward_to_bot = AsyncMock()

        payload = _make_event_payload(user_id=_STRANGER_SLACK_ID)
        result = await proxy.handle_event(payload)

        assert result["status"] == "blocked"
        assert _STRANGER_SLACK_ID in proxy._pending_access_requests
        proxy._notify_owner.assert_called_once()

    @pytest.mark.asyncio
    async def test_stranger_rate_limited(self):
        proxy = _make_proxy()
        proxy._send_slack_message = AsyncMock()
        proxy._notify_owner = AsyncMock()
        # Exhaust the rate limit
        for _ in range(10):
            proxy._stranger_rate_limiter.check(_STRANGER_SLACK_ID)

        payload = _make_event_payload(user_id=_STRANGER_SLACK_ID)
        result = await proxy.handle_event(payload)

        assert result["status"] == "blocked"
        assert result["reason"] == "stranger rate limit"

    @pytest.mark.asyncio
    async def test_collaborator_receives_disclosure_on_first_message(self):
        proxy = _make_proxy(collab_ids=[_COLLAB_SLACK_ID])
        proxy._send_slack_message = AsyncMock()
        proxy._forward_to_bot = AsyncMock()

        payload = _make_event_payload(user_id=_COLLAB_SLACK_ID)
        await proxy.handle_event(payload)

        # First call should be the disclosure notice
        first_call_text = proxy._send_slack_message.call_args_list[0][0][1]
        assert "AgentShroud Notice" in first_call_text
        assert _COLLAB_SLACK_ID in proxy._disclosure_sent

    @pytest.mark.asyncio
    async def test_collaborator_no_duplicate_disclosure(self):
        proxy = _make_proxy(collab_ids=[_COLLAB_SLACK_ID])
        proxy._send_slack_message = AsyncMock()
        proxy._forward_to_bot = AsyncMock()
        proxy._disclosure_sent.add(_COLLAB_SLACK_ID)  # already sent

        payload = _make_event_payload(user_id=_COLLAB_SLACK_ID)
        await proxy.handle_event(payload)

        # No disclosure call on second message
        texts = [c[0][1] for c in proxy._send_slack_message.call_args_list]
        assert not any("AgentShroud Notice" in t for t in texts)

    @pytest.mark.asyncio
    async def test_owner_message_forwarded_without_rate_limit(self):
        proxy = _make_proxy(owner_id=_OWNER_SLACK_ID)
        proxy._send_slack_message = AsyncMock()
        proxy._forward_to_bot = AsyncMock()

        payload = _make_event_payload(user_id=_OWNER_SLACK_ID)
        result = await proxy.handle_event(payload)

        assert result["status"] in ("forwarded", "handled_locally")
        proxy._forward_to_bot.assert_called_once()

    @pytest.mark.asyncio
    async def test_collaborator_blocked_command_denied(self):
        proxy = _make_proxy(collab_ids=[_COLLAB_SLACK_ID])
        proxy._send_slack_message = AsyncMock()
        proxy._forward_to_bot = AsyncMock()
        proxy._disclosure_sent.add(_COLLAB_SLACK_ID)

        payload = _make_event_payload(user_id=_COLLAB_SLACK_ID, text="/approve someuser")
        result = await proxy.handle_event(payload)

        assert result["status"] == "blocked"
        proxy._forward_to_bot.assert_not_called()


# ─── Pipeline Integration ─────────────────────────────────────────────────────

class TestPipelineIntegration:
    @pytest.mark.asyncio
    async def test_pipeline_blocked_message_not_forwarded(self):
        pipeline = MagicMock()
        pipeline_result = MagicMock()
        pipeline_result.blocked = True
        pipeline_result.block_reason = "injection_detected"
        pipeline_result.sanitized_message = None
        pipeline.process_inbound = AsyncMock(return_value=pipeline_result)

        proxy = _make_proxy(owner_id=_OWNER_SLACK_ID, pipeline=pipeline)
        proxy._send_slack_message = AsyncMock()
        proxy._forward_to_bot = AsyncMock()

        payload = _make_event_payload(user_id=_OWNER_SLACK_ID)
        result = await proxy.handle_event(payload)

        assert result["status"] == "blocked"
        proxy._forward_to_bot.assert_not_called()

    @pytest.mark.asyncio
    async def test_pipeline_pass_message_forwarded_with_sanitized_text(self):
        pipeline = MagicMock()
        pipeline_result = MagicMock()
        pipeline_result.blocked = False
        pipeline_result.sanitized_message = "clean text"
        pipeline.process_inbound = AsyncMock(return_value=pipeline_result)

        proxy = _make_proxy(owner_id=_OWNER_SLACK_ID, pipeline=pipeline)
        proxy._send_slack_message = AsyncMock()
        proxy._forward_to_bot = AsyncMock()

        payload = _make_event_payload(user_id=_OWNER_SLACK_ID, text="raw text")
        await proxy.handle_event(payload)

        call_payload = proxy._forward_to_bot.call_args[0][0]
        assert call_payload["text"] == "clean text"
        assert call_payload["source"] == "slack"


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


# ─── Local Commands ───────────────────────────────────────────────────────────

class TestLocalCommands:
    @pytest.mark.asyncio
    async def test_status_command(self):
        proxy = _make_proxy(owner_id=_OWNER_SLACK_ID)
        proxy._send_slack_message = AsyncMock()

        handled = await proxy._handle_local_command("/status", _OWNER_SLACK_ID, "C123", "", True)
        assert handled is True
        sent_text = proxy._send_slack_message.call_args[0][1]
        assert "AgentShroud Status" in sent_text

    @pytest.mark.asyncio
    async def test_whoami_command(self):
        proxy = _make_proxy(owner_id=_OWNER_SLACK_ID)
        proxy._send_slack_message = AsyncMock()

        handled = await proxy._handle_local_command("/whoami", _OWNER_SLACK_ID, "C123", "", True)
        assert handled is True
        sent_text = proxy._send_slack_message.call_args[0][1]
        assert "owner" in sent_text

    @pytest.mark.asyncio
    async def test_approve_command_grants_collaborator(self):
        proxy = _make_proxy(owner_id=_OWNER_SLACK_ID)
        proxy._send_slack_message = AsyncMock()
        proxy._pending_access_requests[_STRANGER_SLACK_ID] = time.time()

        handled = await proxy._handle_local_command(
            f"/approve {_STRANGER_SLACK_ID}", _OWNER_SLACK_ID, "C123", "", True
        )
        assert handled is True
        assert _STRANGER_SLACK_ID not in proxy._pending_access_requests
        assert _STRANGER_SLACK_ID in proxy._runtime_collaborators

    @pytest.mark.asyncio
    async def test_deny_command_rejects_requester(self):
        proxy = _make_proxy(owner_id=_OWNER_SLACK_ID)
        proxy._send_slack_message = AsyncMock()
        proxy._pending_access_requests[_STRANGER_SLACK_ID] = time.time()

        handled = await proxy._handle_local_command(
            f"/deny {_STRANGER_SLACK_ID}", _OWNER_SLACK_ID, "C123", "", True
        )
        assert handled is True
        assert _STRANGER_SLACK_ID not in proxy._pending_access_requests
        assert _STRANGER_SLACK_ID in proxy._runtime_revoked

    @pytest.mark.asyncio
    async def test_revoke_command_revokes_collaborator(self):
        proxy = _make_proxy(owner_id=_OWNER_SLACK_ID, collab_ids=[_COLLAB_SLACK_ID])
        proxy._send_slack_message = AsyncMock()

        handled = await proxy._handle_local_command(
            f"/revoke {_COLLAB_SLACK_ID}", _OWNER_SLACK_ID, "C123", "", True
        )
        assert handled is True
        assert _COLLAB_SLACK_ID in proxy._runtime_revoked

    @pytest.mark.asyncio
    async def test_owner_only_command_rejected_for_collaborator(self):
        proxy = _make_proxy()
        proxy._send_slack_message = AsyncMock()

        handled = await proxy._handle_local_command(
            f"/approve {_STRANGER_SLACK_ID}", _COLLAB_SLACK_ID, "C123", "", False
        )
        assert handled is False  # Caller blocks the command, not this method


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
