# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for Egress Firewall Telegram inline button notifications."""

import json
from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock, patch

import pytest

from gateway.proxy.telegram_egress_notify import EgressTelegramNotifier


class TestEgressTelegramNotify:
    """Test Telegram egress notification system."""

    @pytest.fixture
    def notifier(self):
        return EgressTelegramNotifier(bot_token="test_token", owner_chat_id="123456789")

    @pytest.mark.asyncio
    async def test_notify_pending_success(self, notifier):
        """Test successful notification sending."""
        with patch.object(notifier, "_async_send") as mock_send:
            mock_send.return_value = {"ok": True, "result": {"message_id": 42}}

            result = await notifier.notify_pending(
                request_id="abc123",
                domain="example.com",
                port=443,
                risk_level="medium",
                agent_id="bot-1",
                tool_name="web_fetch",
            )

            assert result is True
            mock_send.assert_called_once()
            call_args = mock_send.call_args
            assert call_args[0][0] == "sendMessage"
            payload = call_args[0][1]
            assert payload["chat_id"] == "123456789"
            assert "example.com:443" in payload["text"]
            assert "reply_markup" in payload
            assert "abc123" in notifier.pending_requests

    @pytest.mark.asyncio
    async def test_notify_pending_failure(self, notifier):
        """Test notification handles API failure gracefully."""
        with patch.object(notifier, "_async_send", side_effect=Exception("Network error")):
            result = await notifier.notify_pending(
                request_id="fail123",
                domain="evil.com",
                port=80,
                risk_level="high",
                agent_id="bot-1",
                tool_name="exec",
            )
            assert result is False

    @pytest.mark.asyncio
    async def test_handle_callback_approve_permanent(self, notifier):
        """Test handling permanent (allow_always) approval callback."""
        notifier.pending_requests["req1"] = {
            "domain": "api.example.com",
            "port": 443,
            "risk_level": "low",
            "agent_id": "bot",
            "tool_name": "web_fetch",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        result = await notifier.handle_callback("egress_allow_always_req1")
        assert result["status"] == "ok"
        assert result["action"] == "allow_always"
        assert result["duration"] == "always"
        assert result["expires_at"] is None
        assert result["domain"] == "api.example.com"
        assert "req1" not in notifier.pending_requests

    @pytest.mark.asyncio
    async def test_handle_callback_approve_1h(self, notifier):
        """Test handling 1-hour time-limited approval callback."""
        notifier.pending_requests["req2"] = {
            "domain": "cdn.example.com",
            "port": 443,
            "risk_level": "medium",
            "agent_id": "bot",
            "tool_name": "web_search",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        result = await notifier.handle_callback("egress_allow_1h_req2")
        assert result["status"] == "ok"
        assert result["action"] == "allow_1h"
        assert result["duration"] == "1h"
        assert result["expires_at"] is not None  # should be ~1h from now

    @pytest.mark.asyncio
    async def test_handle_callback_approve_4h(self, notifier):
        """Test handling 4-hour time-limited approval callback."""
        notifier.pending_requests["req4h"] = {
            "domain": "cdn.example.com",
            "port": 443,
            "risk_level": "low",
            "agent_id": "bot",
            "tool_name": "web_fetch",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        result = await notifier.handle_callback("egress_allow_4h_req4h")
        assert result["status"] == "ok"
        assert result["action"] == "allow_4h"
        assert result["duration"] == "4h"
        assert result["expires_at"] is not None

    @pytest.mark.asyncio
    async def test_handle_callback_deny(self, notifier):
        """Test handling deny callback."""
        notifier.pending_requests["req3"] = {
            "domain": "evil.com",
            "port": 80,
            "risk_level": "high",
            "agent_id": "bot",
            "tool_name": "exec",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        result = await notifier.handle_callback("egress_deny_req3")
        assert result["status"] == "ok"
        assert result["action"] == "deny"
        assert "req3" not in notifier.pending_requests

    @pytest.mark.asyncio
    async def test_handle_callback_invalid_format(self, notifier):
        """Test handling invalid callback data."""
        result = await notifier.handle_callback("garbage_data")
        assert result["status"] == "error"
        assert result["reason"] == "invalid_format"

    @pytest.mark.asyncio
    async def test_handle_callback_request_not_found(self, notifier):
        """Test callback for non-existent request."""
        result = await notifier.handle_callback("egress_deny_nonexistent")
        assert result["status"] == "error"
        assert result["reason"] == "request_not_found"

    def test_cleanup_expired_requests(self, notifier):
        """Test cleanup removes expired pending requests."""
        old_time = (datetime.now(timezone.utc) - timedelta(seconds=600)).isoformat()
        new_time = datetime.now(timezone.utc).isoformat()

        notifier.pending_requests["old1"] = {
            "domain": "old.com",
            "port": 80,
            "risk_level": "low",
            "agent_id": "bot",
            "tool_name": "test",
            "timestamp": old_time,
        }
        notifier.pending_requests["new1"] = {
            "domain": "new.com",
            "port": 443,
            "risk_level": "low",
            "agent_id": "bot",
            "tool_name": "test",
            "timestamp": new_time,
        }

        removed = notifier.cleanup_expired(max_age_seconds=300)
        assert removed == 1
        assert "old1" not in notifier.pending_requests
        assert "new1" in notifier.pending_requests

    @pytest.mark.asyncio
    async def test_answer_callback_success(self, notifier):
        """Test answering callback query."""
        with patch.object(notifier, "_async_send") as mock_send:
            mock_send.return_value = {"ok": True}
            result = await notifier.answer_callback("cb123", "Approved!")
            assert result is True
            mock_send.assert_called_once_with(
                "answerCallbackQuery",
                {
                    "callback_query_id": "cb123",
                    "text": "Approved!",
                    "show_alert": False,
                },
            )

    @pytest.mark.asyncio
    async def test_answer_callback_error(self, notifier):
        """Test answer_callback handles errors."""
        with patch.object(notifier, "_async_send", side_effect=Exception("fail")):
            result = await notifier.answer_callback("cb123", "text")
            assert result is False

    def test_get_pending_count(self, notifier):
        """Test pending count."""
        assert notifier.get_pending_count() == 0
        notifier.pending_requests["r1"] = {"domain": "test.com"}
        assert notifier.get_pending_count() == 1

    def test_risk_emoji_mapping(self, notifier):
        """Test risk level emoji display."""
        from gateway.proxy.telegram_egress_notify import RISK_EMOJI

        assert RISK_EMOJI["low"] == "🟢"
        assert RISK_EMOJI["medium"] == "🟡"
        assert RISK_EMOJI["high"] == "🔴"
        assert RISK_EMOJI["unknown"] == "⚪"

    @pytest.mark.asyncio
    async def test_handle_callback_returns_agent_id(self, notifier):
        """handle_callback must include agent_id so the proxy can notify the originating collaborator."""
        notifier.pending_requests["rid-collab"] = {
            "domain": "example.com",
            "port": 443,
            "risk_level": "yellow",
            "agent_id": "telegram_web_fetch:9876543210",
            "tool_name": "web_fetch",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        result = await notifier.handle_callback("egress_allow_always_rid-collab")
        assert result["status"] == "ok"
        assert result.get("agent_id") == "telegram_web_fetch:9876543210"

    @pytest.mark.asyncio
    async def test_handle_callback_allow_always_returns_agent_id(self, notifier):
        """Permanent approval also includes agent_id in result."""
        notifier.pending_requests["rid-perm"] = {
            "domain": "api.safe.com",
            "port": 443,
            "risk_level": "low",
            "agent_id": "telegram_web_fetch:1111111111",
            "tool_name": "web_fetch",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        result = await notifier.handle_callback("egress_allow_always_rid-perm")
        assert result["status"] == "ok"
        assert result.get("agent_id") == "telegram_web_fetch:1111111111"

    @pytest.mark.asyncio
    async def test_handle_callback_deny_returns_agent_id(self, notifier):
        """Denial result also includes agent_id so collaborator can be notified."""
        notifier.pending_requests["rid-deny"] = {
            "domain": "evil.com",
            "port": 80,
            "risk_level": "high",
            "agent_id": "telegram_web_fetch:2222222222",
            "tool_name": "exec",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        result = await notifier.handle_callback("egress_deny_rid-deny")
        assert result["status"] == "ok"
        assert result.get("agent_id") == "telegram_web_fetch:2222222222"

    @pytest.mark.asyncio
    async def test_handle_callback_missing_agent_id_safe(self, notifier):
        """Missing agent_id in stored request returns empty string, not a crash."""
        notifier.pending_requests["rid-noagent"] = {
            "domain": "example.com",
            "port": 443,
            "risk_level": "low",
            "tool_name": "web_fetch",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        result = await notifier.handle_callback("egress_allow_always_rid-noagent")
        assert result["status"] == "ok"
        assert result.get("agent_id", "") == ""

    def test_notification_recipients_owner_only_by_default(self, notifier):
        """Collaborators are never added to notification_recipients — only owner gets egress buttons."""
        # Notifier is initialized with just owner_chat_id="123456789" (see fixture)
        assert notifier.notification_recipients == ["123456789"]
        assert len(notifier.notification_recipients) == 1
