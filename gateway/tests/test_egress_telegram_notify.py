# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.

import pytest
from unittest.mock import AsyncMock, patch, MagicMock
import json
from datetime import datetime, timedelta
from gateway.proxy.telegram_egress_notify import EgressTelegramNotifier


class TestEgressTelegramNotify:
    """Test Telegram egress notification system."""

    @pytest.fixture
    def notifier(self):
        """Create notifier instance for testing."""
        return EgressTelegramNotifier(
            bot_token="test_token",
            owner_chat_id="123456789"
        )

    @pytest.mark.asyncio
    async def test_notify_pending_success(self, notifier):
        """Test successful notification sending."""
        with patch("aiohttp.ClientSession.post") as mock_post:
            # Setup mock response
            mock_response = AsyncMock()
            mock_response.status = 200
            mock_post.return_value.__aenter__.return_value = mock_response
            
            await notifier.notify_pending(
                request_id="test123",
                domain="example.com",
                port=443,
                risk_level="unknown",
                agent_id="agent001",
                tool_name="web_fetch"
            )
            
            # Verify request was stored
            assert "test123" in notifier.pending_requests
            request_info = notifier.pending_requests["test123"]
            assert request_info["domain"] == "example.com"
            assert request_info["port"] == 443
            assert request_info["risk_level"] == "unknown"
            assert request_info["agent_id"] == "agent001"
            assert request_info["tool_name"] == "web_fetch"
            
            # Verify HTTP request was made
            mock_post.assert_called_once()

    @pytest.mark.asyncio
    async def test_handle_callback_approve_permanent(self, notifier):
        """Test handling permanent approval callback."""
        # Setup pending request
        notifier.pending_requests["test123"] = {
            "domain": "example.com",
            "port": 443,
            "risk_level": "unknown",
            "agent_id": "agent001",
            "tool_name": "web_fetch",
            "timestamp": datetime.utcnow().isoformat()
        }
        
        with patch.object(notifier, "_answer_callback") as mock_answer:
            result = await notifier.handle_callback(
                callback_data="approve_permanent_test123",
                callback_query_id="callback123"
            )
            
            # Verify decision
            assert result is not None
            assert result["action"] == "allow"
            assert result["permanent"] is True
            assert result["domain"] == "example.com"
            assert result["port"] == 443
            assert result["request_id"] == "test123"
            
            # Verify callback was answered
            mock_answer.assert_called_once()
            
            # Verify request was cleaned up
            assert "test123" not in notifier.pending_requests

    @pytest.mark.asyncio
    async def test_handle_callback_approve_once(self, notifier):
        """Test handling one-time approval callback."""
        # Setup pending request
        notifier.pending_requests["test123"] = {
            "domain": "example.com",
            "port": 443,
            "risk_level": "unknown",
            "agent_id": "agent001",
            "tool_name": "web_fetch",
            "timestamp": datetime.utcnow().isoformat()
        }
        
        with patch.object(notifier, "_answer_callback") as mock_answer:
            result = await notifier.handle_callback(
                callback_data="approve_once_test123",
                callback_query_id="callback123"
            )
            
            # Verify decision
            assert result is not None
            assert result["action"] == "allow"
            assert result["permanent"] is False
            assert result["domain"] == "example.com"
            assert result["port"] == 443
            assert result["request_id"] == "test123"

    @pytest.mark.asyncio
    async def test_handle_callback_deny(self, notifier):
        """Test handling denial callback."""
        # Setup pending request
        notifier.pending_requests["test123"] = {
            "domain": "example.com",
            "port": 443,
            "risk_level": "unknown",
            "agent_id": "agent001",
            "tool_name": "web_fetch",
            "timestamp": datetime.utcnow().isoformat()
        }
        
        with patch.object(notifier, "_answer_callback") as mock_answer:
            result = await notifier.handle_callback(
                callback_data="deny_test123",
                callback_query_id="callback123"
            )
            
            # Verify decision
            assert result is not None
            assert result["action"] == "deny"
            assert result["domain"] == "example.com"
            assert result["port"] == 443
            assert result["request_id"] == "test123"

    @pytest.mark.asyncio
    async def test_handle_callback_invalid_format(self, notifier):
        """Test handling invalid callback data format."""
        with patch.object(notifier, "_answer_callback") as mock_answer:
            result = await notifier.handle_callback(
                callback_data="invalid_format",
                callback_query_id="callback123"
            )
            
            assert result is None

    @pytest.mark.asyncio
    async def test_handle_callback_request_not_found(self, notifier):
        """Test handling callback for non-existent request."""
        with patch.object(notifier, "_answer_callback") as mock_answer:
            result = await notifier.handle_callback(
                callback_data="approve_permanent_nonexistent",
                callback_query_id="callback123"
            )
            
            assert result is None
            mock_answer.assert_called_once_with("callback123", "❌ Request expired or not found")

    def test_get_pending_count(self, notifier):
        """Test getting pending request count."""
        assert notifier.get_pending_count() == 0
        
        notifier.pending_requests["test1"] = {"domain": "example.com"}
        notifier.pending_requests["test2"] = {"domain": "test.com"}
        
        assert notifier.get_pending_count() == 2

    def test_cleanup_expired_requests(self, notifier):
        """Test cleanup of expired pending requests."""
        now = datetime.utcnow()
        old_time = now - timedelta(hours=1)
        recent_time = now - timedelta(minutes=5)
        
        # Add requests with different timestamps
        notifier.pending_requests["old_request"] = {
            "domain": "example.com",
            "timestamp": old_time.isoformat()
        }
        notifier.pending_requests["recent_request"] = {
            "domain": "test.com",
            "timestamp": recent_time.isoformat()
        }
        
        # Clean up requests older than 30 minutes
        notifier.cleanup_expired_requests(max_age_minutes=30)
        
        # Old request should be removed, recent should remain
        assert "old_request" not in notifier.pending_requests
        assert "recent_request" in notifier.pending_requests

    @pytest.mark.asyncio
    async def test_answer_callback_success(self, notifier):
        """Test successful callback answer."""
        with patch("aiohttp.ClientSession.post") as mock_post:
            mock_response = AsyncMock()
            mock_response.status = 200
            mock_post.return_value.__aenter__.return_value = mock_response
            
            await notifier._answer_callback("callback123", "Test message")
            
            mock_post.assert_called_once()

    @pytest.mark.asyncio
    async def test_answer_callback_error(self, notifier):
        """Test callback answer error handling."""
        with patch("aiohttp.ClientSession.post") as mock_post:
            mock_response = AsyncMock()
            mock_response.status = 400
            mock_response.text = AsyncMock(return_value="Error message")
            mock_post.return_value.__aenter__.return_value = mock_response
            
            # Should not raise exception
            await notifier._answer_callback("callback123", "Test message")
