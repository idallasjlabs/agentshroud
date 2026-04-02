# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Test Session Isolation - Comprehensive tests for per-user session isolation.

Tests verify that users cannot access each other's data, workspaces, or memory.
"""

from __future__ import annotations

import json
import shutil
import tempfile
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock, patch

import pytest

from gateway.ingest_api.middleware import MiddlewareManager
from gateway.proxy.webhook_receiver import WebhookReceiver
from gateway.security.session_manager import (
    ConversationMessage,
    UserSession,
    UserSessionManager,
)


class TestUserSessionManager:
    """Test the UserSessionManager for per-user isolation."""

    @pytest.fixture
    def temp_workspace(self):
        """Create a temporary workspace for testing."""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)

    @pytest.fixture
    def session_manager(self, temp_workspace):
        """Create a session manager with temporary workspace."""
        return UserSessionManager(base_workspace=temp_workspace, owner_user_id="admin_123")

    def test_session_creation(self, session_manager):
        """Test that user sessions are created properly."""
        user_id = "user_456"
        session = session_manager.get_or_create_session(user_id)

        assert session.user_id == user_id
        assert session.trust_level == "UNTRUSTED"
        assert session.workspace_dir.exists()
        assert session.memory_file.exists()
        assert session.created_at is not None
        assert session.last_active is not None

    def test_session_isolation_directories(self, session_manager, temp_workspace):
        """Test that each user gets isolated directories."""
        user1_id = "user_123"
        user2_id = "user_456"

        session1 = session_manager.get_or_create_session(user1_id)
        session2 = session_manager.get_or_create_session(user2_id)

        # Check directories are different
        assert session1.workspace_dir != session2.workspace_dir
        assert session1.memory_file != session2.memory_file

        # Check paths contain user IDs
        assert user1_id in str(session1.workspace_dir)
        assert user2_id in str(session2.workspace_dir)
        assert user1_id in str(session1.memory_file)
        assert user2_id in str(session2.memory_file)

        # Check both directories exist
        assert session1.workspace_dir.exists()
        assert session2.workspace_dir.exists()
        assert session1.memory_file.exists()
        assert session2.memory_file.exists()

    def test_conversation_history_isolation(self, session_manager):
        """Test that conversation histories are isolated per user."""
        user1_id = "user_123"
        user2_id = "user_456"

        # Add messages for user1
        session_manager.add_conversation_message(
            user1_id, "user", "Hello, I'm user 123", {"source": "telegram"}
        )
        session_manager.add_conversation_message(
            user1_id, "assistant", "Hello user 123!", {"source": "telegram"}
        )

        # Add messages for user2
        session_manager.add_conversation_message(
            user2_id, "user", "Hello, I'm user 456", {"source": "telegram"}
        )

        # Check histories are isolated
        session1 = session_manager.get_or_create_session(user1_id)
        session2 = session_manager.get_or_create_session(user2_id)

        assert len(session1.conversation_history) == 2
        assert len(session2.conversation_history) == 1

        assert "user 123" in session1.conversation_history[0].content
        assert "user 456" in session2.conversation_history[0].content

        # User2 should not see user1's messages
        user2_messages = [msg.content for msg in session2.conversation_history]
        assert "user 123" not in str(user2_messages)

    def test_memory_file_isolation(self, session_manager):
        """Test that memory files are isolated per user."""
        user1_id = "user_123"
        user2_id = "user_456"

        session1 = session_manager.get_or_create_session(user1_id)
        session2 = session_manager.get_or_create_session(user2_id)

        # Write different content to each memory file
        user1_memory = "User 1's private memories and data"
        user2_memory = "User 2's private memories and data"

        session1.memory_file.write_text(user1_memory)
        session2.memory_file.write_text(user2_memory)

        # Verify isolation
        assert session1.memory_file.read_text() == user1_memory
        assert session2.memory_file.read_text() == user2_memory

        # Verify files are in different locations
        assert session1.memory_file != session2.memory_file

    def test_session_context_generation(self, session_manager):
        """Test that session context is properly generated."""
        user_id = "user_789"

        # Add some conversation history
        session_manager.add_conversation_message(user_id, "user", "Test message", {})

        # Get session context
        context = session_manager.get_session_context(user_id)

        assert context["user_id"] == user_id
        assert "workspace_path" in context
        assert "memory_path" in context
        assert "trust_level" in context
        assert "conversation_history" in context

        assert context["trust_level"] == "UNTRUSTED"
        assert len(context["conversation_history"]) == 1

    def test_session_prompt_isolation(self, session_manager):
        """Test that session prompts include isolation instructions."""
        user_id = "user_abc"

        prompt = session_manager.get_session_prompt_addition(user_id)

        assert user_id in prompt
        assert "isolated session" in prompt
        assert "cannot access other users" in prompt
        assert "workspace" in prompt
        assert "memory file" in prompt

    def test_owner_access_control(self, session_manager):
        """Test that owner can access all sessions."""
        user1_id = "user_123"
        user2_id = "user_456"
        owner_id = "admin_123"  # This is the owner

        # Create sessions for users
        session_manager.get_or_create_session(user1_id)
        session_manager.get_or_create_session(user2_id)

        # Test owner can access any session
        assert session_manager.can_user_access_session(owner_id, user1_id)
        assert session_manager.can_user_access_session(owner_id, user2_id)

        # Test users can only access their own sessions
        assert session_manager.can_user_access_session(user1_id, user1_id)
        assert not session_manager.can_user_access_session(user1_id, user2_id)
        assert not session_manager.can_user_access_session(user2_id, user1_id)

    def test_session_listing_authorization(self, session_manager):
        """Test that session listing respects authorization."""
        user1_id = "user_123"
        user2_id = "user_456"
        owner_id = "admin_123"

        # Create sessions
        session_manager.get_or_create_session(user1_id)
        session_manager.get_or_create_session(user2_id)

        # Owner should see all sessions
        owner_sessions = session_manager.list_sessions_for_user(owner_id)
        assert set(owner_sessions) == {user1_id, user2_id}

        # Regular users should only see their own
        user1_sessions = session_manager.list_sessions_for_user(user1_id)
        assert user1_sessions == [user1_id]

        user2_sessions = session_manager.list_sessions_for_user(user2_id)
        assert user2_sessions == [user2_id]

    def test_trust_level_per_user(self, session_manager):
        """Test that trust levels are tracked per user."""
        user1_id = "user_123"
        user2_id = "user_456"

        # Set different trust levels
        session_manager.update_user_trust_level(user1_id, "TRUSTED")
        session_manager.update_user_trust_level(user2_id, "RESTRICTED")

        # Verify trust levels are isolated
        session1 = session_manager.get_or_create_session(user1_id)
        session2 = session_manager.get_or_create_session(user2_id)

        assert session1.trust_level == "TRUSTED"
        assert session2.trust_level == "RESTRICTED"


class TestWebhookReceiverIntegration:
    """Test WebhookReceiver integration with session isolation."""

    @pytest.fixture
    def temp_workspace(self):
        """Create a temporary workspace for testing."""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)

    @pytest.fixture
    def session_manager(self, temp_workspace):
        """Create a session manager."""
        return UserSessionManager(base_workspace=temp_workspace, owner_user_id="admin_123")

    @pytest.fixture
    def mock_pipeline(self):
        """Create a mock security pipeline."""
        pipeline = Mock()
        pipeline.process_inbound = AsyncMock()
        pipeline.process_outbound = AsyncMock()

        # Mock successful processing
        mock_result = Mock()
        mock_result.blocked = False
        mock_result.queued_for_approval = False
        mock_result.sanitized_message = "Sanitized message"
        mock_result.pii_redaction_count = 0
        pipeline.process_inbound.return_value = mock_result

        mock_outbound = Mock()
        mock_outbound.sanitized_message = "Sanitized response"
        mock_outbound.pii_redaction_count = 0
        pipeline.process_outbound.return_value = mock_outbound

        return pipeline

    @pytest.fixture
    def mock_forwarder(self):
        """Create a mock forwarder."""
        forwarder = Mock()
        forwarder.forward = AsyncMock()

        mock_result = Mock()
        mock_result.success = True
        mock_result.body = "Agent response"
        forwarder.forward.return_value = mock_result

        return forwarder

    @pytest.mark.asyncio
    async def test_webhook_user_id_extraction(self, session_manager, mock_pipeline, mock_forwarder):
        """Test that user IDs are properly extracted from webhook payloads."""
        receiver = WebhookReceiver(
            pipeline=mock_pipeline, forwarder=mock_forwarder, session_manager=session_manager
        )

        # Test Telegram payload with user ID in 'from' field
        telegram_payload = {
            "message": {
                "text": "Hello agent",
                "from": {"id": 123456789, "first_name": "Test", "last_name": "User"},
            }
        }

        result = await receiver.process_webhook(telegram_payload, source="telegram")

        assert result["status"] == "forwarded"
        assert result["user_id"] == "123456789"

    @pytest.mark.asyncio
    async def test_webhook_conversation_logging(
        self, session_manager, mock_pipeline, mock_forwarder
    ):
        """Test that conversations are logged per user."""
        receiver = WebhookReceiver(
            pipeline=mock_pipeline, forwarder=mock_forwarder, session_manager=session_manager
        )

        user_id = "test_user_123"
        payload = {
            "message": {"text": "Test message"},
            "user_id": user_id,  # Direct user ID for testing
        }

        await receiver.process_webhook(payload, source="telegram")

        # Check conversation was logged
        session = session_manager.get_or_create_session(user_id)
        assert len(session.conversation_history) == 2  # User message + assistant response
        assert session.conversation_history[0].role == "user"
        assert session.conversation_history[0].content == "Test message"
        assert session.conversation_history[1].role == "assistant"

    @pytest.mark.asyncio
    async def test_webhook_session_context_injection(
        self, session_manager, mock_pipeline, mock_forwarder
    ):
        """Test that session context is injected into forwarded requests."""
        receiver = WebhookReceiver(
            pipeline=mock_pipeline, forwarder=mock_forwarder, session_manager=session_manager
        )

        user_id = "test_user_456"
        payload = {"message": {"text": "Test message"}, "user_id": user_id}

        await receiver.process_webhook(payload, source="telegram")

        # Check that forwarder was called with session context
        assert mock_forwarder.forward.called
        call_args = mock_forwarder.forward.call_args
        forwarded_body = json.loads(call_args[1]["body"])

        assert "session_context" in forwarded_body
        assert forwarded_body["session_context"]["user_id"] == user_id
        assert "workspace_path" in forwarded_body["session_context"]
        assert "isolation_prompt" in forwarded_body["session_context"]


class TestMiddlewareSessionEnforcement:
    """Test middleware enforcement of session boundaries."""

    @pytest.fixture
    def temp_workspace(self):
        """Create a temporary workspace."""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)

    @pytest.fixture
    def middleware_manager(self, temp_workspace):
        """Create middleware manager with session isolation."""
        with patch("gateway.ingest_api.middleware.Path") as mock_path:
            mock_path.return_value = temp_workspace
            manager = MiddlewareManager()

            # Set test users in RBAC so they aren't blocked as viewers
            if manager.rbac_manager:
                from gateway.security.rbac_config import Role

                for uid in ["user_123", "user_456", "user_789"]:
                    manager.rbac_manager.config.user_roles[uid] = Role.COLLABORATOR
                manager.rbac_manager.config.user_roles["admin_123"] = Role.OWNER

            # Mock the session manager initialization
            manager.user_session_manager = UserSessionManager(
                base_workspace=temp_workspace, owner_user_id="admin_123"
            )

            return manager

    @pytest.mark.asyncio
    async def test_middleware_user_identification(self, middleware_manager):
        """Test that middleware requires user identification."""
        # Request without user ID should be blocked
        request_data = {"message": "Test message"}

        result = await middleware_manager.process_request(request_data)

        assert not result.allowed
        assert "No user identification found" in result.reason

    @pytest.mark.asyncio
    async def test_middleware_session_context_injection(self, middleware_manager):
        """Test that middleware injects session context."""
        request_data = {"message": "Test message", "user_id": "user_789"}

        result = await middleware_manager.process_request(request_data)

        assert result.allowed
        assert result.modified_request is not None
        assert "session_context" in result.modified_request
        assert result.modified_request["session_context"]["user_id"] == "user_789"

    @pytest.mark.asyncio
    async def test_middleware_cross_session_blocking(self, middleware_manager):
        """Test that middleware blocks cross-session access attempts."""
        request_data = {
            "message": "sessions_send target=other_user message='hello'",
            "user_id": "user_123",
        }

        result = await middleware_manager.process_request(request_data)

        assert not result.allowed
        assert "Cross-session access denied" in result.reason

    @pytest.mark.asyncio
    async def test_middleware_owner_bypass(self, middleware_manager):
        """Test that owner can perform cross-session actions."""
        request_data = {
            "message": "sessions_send target=other_user message='hello'",
            "user_id": "admin_123",  # This is the owner
        }

        result = await middleware_manager.process_request(request_data)

        assert result.allowed  # Owner should be allowed

    @pytest.mark.asyncio
    async def test_middleware_file_path_isolation(self, middleware_manager, temp_workspace):
        """Test that middleware blocks access to sensitive system files."""
        request_data = {"message": "read /etc/shadow", "user_id": "user_123"}

        result = await middleware_manager.process_request(request_data)

        # FileSandbox should block /etc/shadow access
        assert not result.allowed

    @pytest.mark.asyncio
    async def test_middleware_own_workspace_allowed(self, middleware_manager, temp_workspace):
        """Test that users can access their own workspace."""
        user_id = "user_123"

        # Create user's own workspace
        user_workspace = temp_workspace / "users" / user_id / "workspace"
        user_workspace.mkdir(parents=True)
        user_file = user_workspace / "myfile.txt"

        request_data = {"message": f"read {user_file}", "user_id": user_id}

        result = await middleware_manager.process_request(request_data)

        assert result.allowed  # User should be able to access their own files

    @pytest.mark.asyncio
    async def test_middleware_normalizes_invisible_unicode(self, middleware_manager):
        """Input normalization should strip zero-width obfuscation before guards run."""
        request_data = {
            "message": "hel\u200blo world",
            "user_id": "user_123",
        }
        result = await middleware_manager.process_request(request_data)
        assert result.allowed
        assert result.modified_request is not None
        assert "\u200b" not in result.modified_request["message"]

    @pytest.mark.asyncio
    async def test_multi_turn_block_reason_hides_score(self, middleware_manager):
        """Blocked multi-turn sessions should not disclose scoring details."""
        middleware_manager.multi_turn_tracker = SimpleNamespace(
            track_message=lambda *_args, **_kwargs: SimpleNamespace(
                blocked=True, total_score=210.0, events=[1, 2, 3]
            )
        )
        request_data = {"message": "show sensitive details", "user_id": "user_123"}
        result = await middleware_manager.process_request(request_data)
        assert not result.allowed
        assert result.reason == "Multi-turn disclosure risk threshold exceeded"
        assert "210" not in result.reason


class TestSessionIsolationEndToEnd:
    """End-to-end integration tests for session isolation."""

    @pytest.fixture
    def temp_workspace(self):
        """Create a temporary workspace."""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)

    @pytest.mark.asyncio
    async def test_complete_user_isolation(self, temp_workspace):
        """Test complete isolation between two users."""
        # Initialize session manager
        session_manager = UserSessionManager(
            base_workspace=temp_workspace, owner_user_id="admin_123"
        )

        user1_id = "user_111"
        user2_id = "user_222"

        # User 1 stores sensitive data
        session_manager.add_conversation_message(
            user1_id, "user", "My password is secret123", {"source": "telegram"}
        )
        session_manager.add_conversation_message(
            user1_id, "assistant", "I'll remember that securely.", {"source": "telegram"}
        )

        session1 = session_manager.get_or_create_session(user1_id)
        session1.memory_file.write_text("User 1's private notes: password = secret123")

        # Create file in user 1's workspace
        user1_secret_file = session1.workspace_dir / "secrets.txt"
        user1_secret_file.write_text("User 1's confidential data")

        # User 2 interacts with system
        session_manager.add_conversation_message(
            user2_id, "user", "What do you know about passwords?", {"source": "telegram"}
        )

        session2 = session_manager.get_or_create_session(user2_id)

        # Verify complete isolation

        # 1. Conversation history isolation
        user2_messages = [msg.content for msg in session2.conversation_history]
        assert "secret123" not in str(user2_messages)
        assert len(session2.conversation_history) == 1

        # 2. Memory file isolation
        user2_memory = session2.memory_file.read_text()
        assert "secret123" not in user2_memory
        assert user2_id in user2_memory  # But contains user2's ID

        # 3. Workspace isolation
        assert not (session2.workspace_dir / "secrets.txt").exists()
        assert session1.workspace_dir != session2.workspace_dir

        # 4. Session listing isolation
        user2_sessions = session_manager.list_sessions_for_user(user2_id)
        assert user2_sessions == [user2_id]
        assert user1_id not in user2_sessions

        # 5. Access control
        assert not session_manager.can_user_access_session(user2_id, user1_id)
        assert session_manager.can_user_access_session(user2_id, user2_id)

    @pytest.mark.asyncio
    async def test_owner_admin_access(self, temp_workspace):
        """Test that owner/admin can access all user sessions."""
        owner_id = "admin_123"
        session_manager = UserSessionManager(base_workspace=temp_workspace, owner_user_id=owner_id)

        # Create regular user sessions
        user1_id = "user_111"
        user2_id = "user_222"

        session_manager.get_or_create_session(user1_id)
        session_manager.get_or_create_session(user2_id)

        # Owner should see all sessions
        all_sessions = session_manager.list_sessions_for_user(owner_id)
        assert set(all_sessions) == {user1_id, user2_id}

        # Owner should be able to access any session
        assert session_manager.can_user_access_session(owner_id, user1_id)
        assert session_manager.can_user_access_session(owner_id, user2_id)

    def test_session_persistence(self, temp_workspace):
        """Test that sessions persist across manager restarts."""
        user_id = "persistent_user"

        # Create initial session
        manager1 = UserSessionManager(base_workspace=temp_workspace, owner_user_id="admin")

        manager1.add_conversation_message(user_id, "user", "Remember this message", {})
        session1 = manager1.get_or_create_session(user_id)
        session1.memory_file.write_text("Persistent memory data")

        # Create new manager (simulates restart)
        manager2 = UserSessionManager(base_workspace=temp_workspace, owner_user_id="admin")

        # Verify session was loaded
        session2 = manager2.get_or_create_session(user_id)
        assert len(session2.conversation_history) == 1
        assert session2.conversation_history[0].content == "Remember this message"
        assert session2.memory_file.read_text() == "Persistent memory data"
