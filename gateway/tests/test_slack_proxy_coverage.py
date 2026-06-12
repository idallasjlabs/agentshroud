# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Coverage tests for SlackAPIProxy — tracker recovery, Slack API call layer,
channel provisioning, and error-branch behavior not exercised by test_slack_proxy.py."""

from __future__ import annotations

import json
import time
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from gateway.proxy.slack_proxy import SlackAPIProxy

_OWNER_UID = "U01J37F6YT0"
_COLLAB_CHANNEL = "C_OTHER"


def _make_proxy(pipeline=None, tracker=None, owner_slack_user_id: str = "") -> SlackAPIProxy:
    """Create a SlackAPIProxy with a fake token and no real secret/file I/O."""
    with patch("gateway.proxy.slack_proxy._read_secret_static", return_value=""):
        proxy = SlackAPIProxy(
            pipeline=pipeline, tracker=tracker, owner_slack_user_id=owner_slack_user_id
        )
    proxy._bot_token = "xoxb-test-token"
    return proxy


# ─── Body parsing error branch (lines 146-147) ───────────────────────────────


class TestBodyParsing:
    @pytest.mark.asyncio
    async def test_malformed_json_body_forwards_with_empty_payload(self):
        """Unparseable JSON body → warning logged, empty payload forwarded (no crash)."""
        pipeline = MagicMock()
        pipeline.process_outbound = AsyncMock()
        proxy = _make_proxy(pipeline=pipeline)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        result = await proxy.proxy_outbound("chat.postMessage", b"{not-json!!!", "application/json")

        # No text fields parsed → nothing to scan, request still forwarded
        assert result == {"ok": True}
        pipeline.process_outbound.assert_not_called()
        sent_payload = proxy._call_slack_api.call_args.args[1]
        assert sent_payload == {}

    @pytest.mark.asyncio
    async def test_unknown_content_type_ignored(self):
        """Bodies with an unrecognized Content-Type are not parsed at all."""
        proxy = _make_proxy()
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        result = await proxy.proxy_outbound("chat.postMessage", b"\x00\x01binary", "text/plain")

        assert result == {"ok": True}
        assert proxy._call_slack_api.call_args.args[1] == {}


# ─── Redaction-count getattr exception swallow (lines 223-224) ───────────────


class _RaisingRedactionResult:
    """Pipeline result whose redaction-count attribute raises on access."""

    blocked = False
    block_reason = ""
    sanitized_message = None

    @property
    def info_filter_redaction_count(self):
        raise RuntimeError("attribute backend offline")

    def __init__(self):
        # sanitized_message left as class attr None
        pass


class TestRedactionCountErrorSwallow:
    @pytest.mark.asyncio
    async def test_redaction_count_access_error_is_non_fatal(self):
        """Non-owner channel: error reading info_filter_redaction_count is swallowed
        and the (otherwise clean) message is still forwarded."""
        pipeline = MagicMock()
        pipeline.process_outbound = AsyncMock(return_value=_RaisingRedactionResult())
        proxy = _make_proxy(pipeline=pipeline, owner_slack_user_id=_OWNER_UID)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        with patch(
            "gateway.proxy.telegram_proxy.TelegramAPIProxy"
            "._contains_high_risk_collaborator_leakage",
            return_value=False,
        ):
            body = json.dumps({"channel": _COLLAB_CHANNEL, "text": "clean"}).encode()
            result = await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        assert result == {"ok": True}
        assert proxy.get_stats()["outbound_blocked"] == 0
        proxy._call_slack_api.assert_called_once()


# ─── Outbound tracker + inbound recovery (lines 260-341) ─────────────────────


class TestOutboundTracking:
    @pytest.mark.asyncio
    async def test_cached_inbound_corr_skips_history_lookup(self):
        """Cached correlation for the channel → no Slack history call; outbound
        is attributed to the cached inbound user ID."""
        tracker = MagicMock()
        proxy = _make_proxy(tracker=tracker)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})
        proxy._last_inbound_corr["C1"] = ("U55:1700000000123", time.time())

        body = json.dumps({"channel": "C1", "text": "bot reply"}).encode()
        result = await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        assert result == {"ok": True}
        # Only the chat.postMessage itself hit the Slack API — no recovery lookup
        assert proxy._call_slack_api.call_count == 1
        tracker.record_activity.assert_called_once()
        kwargs = tracker.record_activity.call_args.kwargs
        assert kwargs["direction"] == "outbound"
        assert kwargs["user_id"] == "U55"  # extracted from cached corr id
        assert kwargs["correlation_id"] == "U55:1700000000123"
        assert kwargs["message_preview"] == "bot reply"
        assert kwargs["source"] == "slack"
        assert kwargs["bot_id"] == "openclaw"

    @pytest.mark.asyncio
    async def test_cached_corr_without_colon_falls_back_to_channel(self):
        """Correlation ID with no ':' separator → outbound attributed to channel id."""
        tracker = MagicMock()
        proxy = _make_proxy(tracker=tracker)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})
        proxy._last_inbound_corr["C9"] = ("opaque-token", time.time())

        body = json.dumps({"channel": "C9", "text": "hi"}).encode()
        await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        kwargs = tracker.record_activity.call_args.kwargs
        assert kwargs["user_id"] == "C9"
        assert kwargs["correlation_id"] == "opaque-token"

    @pytest.mark.asyncio
    async def test_thread_reply_recovers_inbound_via_conversations_replies(self):
        """Thread reply with no cached corr → conversations.replies lookup recovers
        the user's original message; inbound + outbound both recorded."""
        tracker = MagicMock()
        proxy = _make_proxy(tracker=tracker)

        async def fake_api(method, body):
            if method == "chat.postMessage":
                return {"ok": True}
            if method == "conversations.replies":
                assert body["channel"] == "C2"
                assert body["ts"] == "111.222"
                return {
                    "ok": True,
                    "messages": [{"user": "U42", "text": "original question", "ts": "111.222"}],
                }
            raise AssertionError(f"unexpected method {method}")

        proxy._call_slack_api = AsyncMock(side_effect=fake_api)

        body = json.dumps({"channel": "C2", "text": "answer", "thread_ts": "111.222"}).encode()
        result = await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        assert result == {"ok": True}
        assert tracker.record_activity.call_count == 2
        inbound_kwargs = tracker.record_activity.call_args_list[0].kwargs
        outbound_kwargs = tracker.record_activity.call_args_list[1].kwargs
        assert inbound_kwargs["direction"] == "inbound"
        assert inbound_kwargs["user_id"] == "U42"
        assert inbound_kwargs["message_preview"] == "original question"
        assert inbound_kwargs["correlation_id"] == "U42:111222"
        assert outbound_kwargs["direction"] == "outbound"
        assert outbound_kwargs["user_id"] == "U42"
        assert outbound_kwargs["correlation_id"] == "U42:111222"
        # Correlation is cached for subsequent replies in the same channel
        assert proxy._last_inbound_corr["C2"][0] == "U42:111222"

    @pytest.mark.asyncio
    async def test_dm_reply_recovers_inbound_via_conversations_history(self):
        """Non-thread reply → conversations.history lookup; bot and subtype
        messages are skipped when locating the user's message."""
        tracker = MagicMock()
        proxy = _make_proxy(tracker=tracker)

        async def fake_api(method, body):
            if method == "chat.postMessage":
                return {"ok": True}
            if method == "conversations.history":
                assert body == {"channel": "D3", "limit": 5}
                return {
                    "ok": True,
                    "messages": [
                        {"user": "UBOT", "bot_id": "B01", "text": "bot noise", "ts": "5.0"},
                        {"user": "U9", "subtype": "channel_join", "text": "joined", "ts": "4.0"},
                        {"user": "U77", "text": "real user msg", "ts": "3.5"},
                    ],
                }
            raise AssertionError(f"unexpected method {method}")

        proxy._call_slack_api = AsyncMock(side_effect=fake_api)

        body = json.dumps({"channel": "D3", "text": "bot answer"}).encode()
        await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        inbound_kwargs = tracker.record_activity.call_args_list[0].kwargs
        assert inbound_kwargs["user_id"] == "U77"
        assert inbound_kwargs["correlation_id"] == "U77:35"
        outbound_kwargs = tracker.record_activity.call_args_list[1].kwargs
        assert outbound_kwargs["user_id"] == "U77"

    @pytest.mark.asyncio
    async def test_history_error_records_outbound_without_correlation(self):
        """History lookup returns ok=False → no inbound record; outbound still
        logged, attributed to the channel with no correlation id."""
        tracker = MagicMock()
        proxy = _make_proxy(tracker=tracker)

        async def fake_api(method, body):
            if method == "chat.postMessage":
                return {"ok": True}
            return {"ok": False, "error": "channel_not_found"}

        proxy._call_slack_api = AsyncMock(side_effect=fake_api)

        body = json.dumps({"channel": "D4", "text": "reply"}).encode()
        await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        tracker.record_activity.assert_called_once()
        kwargs = tracker.record_activity.call_args.kwargs
        assert kwargs["direction"] == "outbound"
        assert kwargs["user_id"] == "D4"
        assert kwargs["correlation_id"] is None

    @pytest.mark.asyncio
    async def test_recovery_exception_is_non_fatal(self):
        """Exception during inbound recovery → swallowed; outbound still recorded."""
        tracker = MagicMock()
        proxy = _make_proxy(tracker=tracker)

        async def fake_api(method, body):
            if method == "chat.postMessage":
                return {"ok": True}
            raise RuntimeError("slack unreachable")

        proxy._call_slack_api = AsyncMock(side_effect=fake_api)

        body = json.dumps({"channel": "D5", "text": "reply"}).encode()
        result = await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        assert result == {"ok": True}
        tracker.record_activity.assert_called_once()
        assert tracker.record_activity.call_args.kwargs["direction"] == "outbound"

    @pytest.mark.asyncio
    async def test_tracker_exception_does_not_break_response(self):
        """Tracker errors are non-fatal — Slack response still returned to bot."""
        tracker = MagicMock()
        tracker.record_activity.side_effect = RuntimeError("db locked")
        proxy = _make_proxy(tracker=tracker)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True, "ts": "9.9"})
        proxy._last_inbound_corr["C6"] = ("U1:1", time.time())

        body = json.dumps({"channel": "C6", "text": "msg"}).encode()
        result = await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        assert result == {"ok": True, "ts": "9.9"}

    @pytest.mark.asyncio
    async def test_structured_text_serialized_for_preview(self):
        """A dict text payload is JSON-serialized before the 80-char preview."""
        tracker = MagicMock()
        proxy = _make_proxy(tracker=tracker)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})
        proxy._last_inbound_corr["C7"] = ("U2:2", time.time())

        body = json.dumps({"channel": "C7", "text": {"type": "mrkdwn", "text": "hi"}}).encode()
        await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        preview = tracker.record_activity.call_args.kwargs["message_preview"]
        assert preview == json.dumps({"type": "mrkdwn", "text": "hi"})

    @pytest.mark.asyncio
    async def test_missing_channel_or_text_skips_tracking(self):
        """chat.postMessage without channel/text → nothing recorded, no lookups."""
        tracker = MagicMock()
        proxy = _make_proxy(tracker=tracker)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        body = json.dumps({"channel": "C8"}).encode()  # no text
        await proxy.proxy_outbound("chat.postMessage", body, "application/json")

        tracker.record_activity.assert_not_called()
        assert proxy._call_slack_api.call_count == 1

    @pytest.mark.asyncio
    async def test_system_message_not_tracked(self):
        """is_system=True chat.postMessage bypasses the tracker entirely."""
        tracker = MagicMock()
        proxy = _make_proxy(tracker=tracker)
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        body = json.dumps({"channel": "C1", "text": "startup notice"}).encode()
        await proxy.proxy_outbound("chat.postMessage", body, "application/json", is_system=True)

        tracker.record_activity.assert_not_called()


# ─── _call_slack_api HTTP layer (lines 347-363) ──────────────────────────────


class TestCallSlackApi:
    @pytest.mark.asyncio
    async def test_success_posts_with_bearer_token(self):
        """Happy path: POSTs to slack.com/api/<method> with injected bot token."""
        proxy = _make_proxy()

        resp = MagicMock()
        resp.json = MagicMock(return_value={"ok": True, "ts": "1.2"})
        client = MagicMock()
        client.post = AsyncMock(return_value=resp)
        cm = MagicMock()
        cm.__aenter__ = AsyncMock(return_value=client)
        cm.__aexit__ = AsyncMock(return_value=False)

        with patch("httpx.AsyncClient", return_value=cm) as client_cls:
            result = await proxy._call_slack_api("chat.postMessage", {"channel": "C1"})

        assert result == {"ok": True, "ts": "1.2"}
        client_cls.assert_called_once_with(timeout=15.0)
        url = client.post.call_args.args[0]
        assert url == "https://slack.com/api/chat.postMessage"
        headers = client.post.call_args.kwargs["headers"]
        assert headers["Authorization"] == "Bearer xoxb-test-token"
        assert client.post.call_args.kwargs["json"] == {"channel": "C1"}

    @pytest.mark.asyncio
    async def test_network_error_returns_synthetic_failure(self):
        """Connection failure → {'ok': False, 'error': <exc>} (no exception leaks)."""
        proxy = _make_proxy()

        client = MagicMock()
        client.post = AsyncMock(side_effect=RuntimeError("connection refused"))
        cm = MagicMock()
        cm.__aenter__ = AsyncMock(return_value=client)
        cm.__aexit__ = AsyncMock(return_value=False)

        with patch("httpx.AsyncClient", return_value=cm):
            result = await proxy._call_slack_api("chat.postMessage", {"channel": "C1"})

        assert result["ok"] is False
        assert "connection refused" in result["error"]


# ─── Group channel provisioning (lines 446-464) ──────────────────────────────


class TestProvisionGroupChannel:
    @pytest.mark.asyncio
    async def test_no_token_returns_none(self):
        proxy = _make_proxy()
        proxy._bot_token = ""
        proxy._call_slack_api = AsyncMock()

        assert await proxy.provision_group_channel("g1", "Team Alpha") is None
        proxy._call_slack_api.assert_not_called()

    @pytest.mark.asyncio
    async def test_success_returns_channel_id_with_sanitized_name(self):
        """Channel name is lowercased, spaces/underscores → hyphens, symbols dropped."""
        proxy = _make_proxy()
        proxy._call_slack_api = AsyncMock(return_value={"ok": True, "channel": {"id": "C_NEW"}})

        channel_id = await proxy.provision_group_channel("g1", "Team Alpha_Beta! #7")

        assert channel_id == "C_NEW"
        method, body = proxy._call_slack_api.call_args.args
        assert method == "conversations.create"
        assert body["name"] == "group-team-alpha-beta-7"
        assert body["is_private"] is False

    @pytest.mark.asyncio
    async def test_name_truncated_to_80_chars(self):
        proxy = _make_proxy()
        proxy._call_slack_api = AsyncMock(return_value={"ok": True, "channel": {"id": "C_L"}})

        await proxy.provision_group_channel("g2", "x" * 200)

        body = proxy._call_slack_api.call_args.args[1]
        assert body["name"] == "group-" + "x" * 80

    @pytest.mark.asyncio
    async def test_slack_error_returns_none(self):
        proxy = _make_proxy()
        proxy._call_slack_api = AsyncMock(return_value={"ok": False, "error": "name_taken"})

        assert await proxy.provision_group_channel("g1", "Team Alpha") is None


# ─── Channel membership management (lines 468-485, 489-506) ──────────────────


class TestInviteChannelMember:
    @pytest.mark.asyncio
    async def test_no_token_returns_false(self):
        proxy = _make_proxy()
        proxy._bot_token = ""
        proxy._call_slack_api = AsyncMock()

        assert await proxy.invite_channel_member("C1", "U1") is False
        proxy._call_slack_api.assert_not_called()

    @pytest.mark.asyncio
    async def test_missing_args_return_false(self):
        proxy = _make_proxy()
        proxy._call_slack_api = AsyncMock()

        assert await proxy.invite_channel_member("", "U1") is False
        assert await proxy.invite_channel_member("C1", "") is False
        proxy._call_slack_api.assert_not_called()

    @pytest.mark.asyncio
    async def test_success_returns_true(self):
        proxy = _make_proxy()
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        assert await proxy.invite_channel_member("C1", "U1") is True
        method, body = proxy._call_slack_api.call_args.args
        assert method == "conversations.invite"
        assert body == {"channel": "C1", "users": "U1"}

    @pytest.mark.asyncio
    async def test_already_in_channel_is_idempotent_true(self):
        proxy = _make_proxy()
        proxy._call_slack_api = AsyncMock(return_value={"ok": False, "error": "already_in_channel"})

        assert await proxy.invite_channel_member("C1", "U1") is True

    @pytest.mark.asyncio
    async def test_other_error_returns_false(self):
        proxy = _make_proxy()
        proxy._call_slack_api = AsyncMock(return_value={"ok": False, "error": "cant_invite"})

        assert await proxy.invite_channel_member("C1", "U1") is False


class TestKickChannelMember:
    @pytest.mark.asyncio
    async def test_no_token_returns_false(self):
        proxy = _make_proxy()
        proxy._bot_token = ""
        proxy._call_slack_api = AsyncMock()

        assert await proxy.kick_channel_member("C1", "U1") is False
        proxy._call_slack_api.assert_not_called()

    @pytest.mark.asyncio
    async def test_missing_args_return_false(self):
        proxy = _make_proxy()
        proxy._call_slack_api = AsyncMock()

        assert await proxy.kick_channel_member("", "U1") is False
        assert await proxy.kick_channel_member("C1", "") is False
        proxy._call_slack_api.assert_not_called()

    @pytest.mark.asyncio
    async def test_success_returns_true(self):
        proxy = _make_proxy()
        proxy._call_slack_api = AsyncMock(return_value={"ok": True})

        assert await proxy.kick_channel_member("C1", "U1") is True
        method, body = proxy._call_slack_api.call_args.args
        assert method == "conversations.kick"
        assert body == {"channel": "C1", "user": "U1"}

    @pytest.mark.asyncio
    async def test_not_in_channel_is_idempotent_true(self):
        proxy = _make_proxy()
        proxy._call_slack_api = AsyncMock(return_value={"ok": False, "error": "not_in_channel"})

        assert await proxy.kick_channel_member("C1", "U1") is True

    @pytest.mark.asyncio
    async def test_cant_kick_self_is_idempotent_true(self):
        proxy = _make_proxy()
        proxy._call_slack_api = AsyncMock(return_value={"ok": False, "error": "cant_kick_self"})

        assert await proxy.kick_channel_member("C1", "U1") is True

    @pytest.mark.asyncio
    async def test_other_error_returns_false(self):
        proxy = _make_proxy()
        proxy._call_slack_api = AsyncMock(return_value={"ok": False, "error": "restricted_action"})

        assert await proxy.kick_channel_member("C1", "U1") is False
