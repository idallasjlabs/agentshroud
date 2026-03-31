# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for gateway/security/session_manager.py — session isolation and security."""
from __future__ import annotations

import tempfile
from pathlib import Path

import pytest
from gateway.security.session_manager import (
    ConversationMessage,
    UserSession,
    UserSessionManager,
)


@pytest.fixture
def mgr(tmp_path):
    """Create a UserSessionManager with a temp base workspace and an owner."""
    return UserSessionManager(base_workspace=tmp_path, owner_user_id="owner123")


# ---------------------------------------------------------------------------
# Session creation & isolation
# ---------------------------------------------------------------------------

class TestSessionIsolation:
    def test_sessions_are_isolated(self, mgr):
        s1 = mgr.get_or_create_session("user-1")
        s2 = mgr.get_or_create_session("user-2")
        assert s1.user_id != s2.user_id
        assert s1.workspace_dir != s2.workspace_dir
        assert s1.memory_file != s2.memory_file
        # Paths should not be prefixes of each other
        assert not str(s1.workspace_dir).startswith(str(s2.workspace_dir))

    def test_get_or_create_returns_same_session(self, mgr):
        s1 = mgr.get_or_create_session("user-x")
        s2 = mgr.get_or_create_session("user-x")
        assert s1.user_id == s2.user_id
        assert s1.workspace_dir == s2.workspace_dir

    def test_workspace_directory_created(self, mgr):
        s = mgr.get_or_create_session("user-a")
        assert s.workspace_dir.exists()
        assert s.workspace_dir.is_dir()

    def test_memory_file_created(self, mgr):
        s = mgr.get_or_create_session("user-a")
        assert s.memory_file.exists()

    def test_default_trust_level_is_untrusted(self, mgr):
        s = mgr.get_or_create_session("new-user")
        assert s.trust_level == "UNTRUSTED"


# ---------------------------------------------------------------------------
# Access control
# ---------------------------------------------------------------------------

class TestAccessControl:
    def test_owner_can_view_all_sessions(self, mgr):
        mgr.get_or_create_session("user-1")
        mgr.get_or_create_session("user-2")
        visible = mgr.list_sessions_for_user("owner123")
        assert "user-1" in visible
        assert "user-2" in visible

    def test_non_owner_cannot_view_other_sessions(self, mgr):
        mgr.get_or_create_session("user-1")
        mgr.get_or_create_session("user-2")
        visible = mgr.list_sessions_for_user("user-1")
        assert "user-1" in visible
        assert "user-2" not in visible

    def test_non_owner_empty_when_no_session(self, mgr):
        visible = mgr.list_sessions_for_user("stranger")
        assert visible == []

    def test_owner_can_access_any_session(self, mgr):
        mgr.get_or_create_session("user-1")
        assert mgr.can_user_access_session("owner123", "user-1")

    def test_user_can_access_own_session(self, mgr):
        assert mgr.can_user_access_session("user-1", "user-1")

    def test_user_cannot_access_other_session(self, mgr):
        assert not mgr.can_user_access_session("user-1", "user-2")


# ---------------------------------------------------------------------------
# Input validation / path traversal
# ---------------------------------------------------------------------------

class TestInputValidation:
    def test_path_traversal_rejected(self, mgr):
        with pytest.raises(ValueError):
            mgr.get_or_create_session("../etc/passwd")

    def test_empty_user_id_rejected(self, mgr):
        with pytest.raises(ValueError):
            mgr.get_or_create_session("")

    def test_long_user_id_rejected(self, mgr):
        with pytest.raises(ValueError):
            mgr.get_or_create_session("a" * 65)

    def test_special_chars_rejected(self, mgr):
        with pytest.raises(ValueError):
            mgr.get_or_create_session("user;rm -rf /")


# ---------------------------------------------------------------------------
# Conversation history
# ---------------------------------------------------------------------------

class TestConversationHistory:
    def test_add_message(self, mgr):
        mgr.get_or_create_session("user-1")
        mgr.add_conversation_message("user-1", "user", "Hello!")
        s = mgr.get_or_create_session("user-1")
        assert len(s.conversation_history) == 1
        assert s.conversation_history[0].content == "Hello!"
        assert s.conversation_history[0].role == "user"

    def test_conversation_history_limit(self, mgr):
        """History should be capped at 1000 messages."""
        mgr.get_or_create_session("user-1")
        for i in range(1010):
            mgr.add_conversation_message("user-1", "user", f"msg-{i}")
        s = mgr.get_or_create_session("user-1")
        assert len(s.conversation_history) <= 1000


# ---------------------------------------------------------------------------
# Trust level updates
# ---------------------------------------------------------------------------

class TestTrustLevel:
    def test_update_trust_level(self, mgr):
        mgr.get_or_create_session("user-1")
        mgr.update_user_trust_level("user-1", "TRUSTED")
        s = mgr.get_or_create_session("user-1")
        assert s.trust_level == "TRUSTED"


# ---------------------------------------------------------------------------
# Session context & prompt injection
# ---------------------------------------------------------------------------

class TestSessionContext:
    def test_get_session_context_contains_user_id(self, mgr):
        mgr.get_or_create_session("user-1")
        ctx = mgr.get_session_context("user-1")
        assert ctx["user_id"] == "user-1"

    def test_prompt_addition_mentions_isolation(self, mgr):
        mgr.get_or_create_session("user-1")
        prompt = mgr.get_session_prompt_addition("user-1")
        assert "isolat" in prompt.lower() or "cannot access" in prompt.lower()


# ---------------------------------------------------------------------------
# Serialization roundtrip
# ---------------------------------------------------------------------------

class TestSerialization:
    def test_session_to_dict_and_back(self):
        s = UserSession(
            user_id="u1",
            workspace_dir=Path("/tmp/ws"),
            memory_file=Path("/tmp/mem.md"),
            trust_level="TRUSTED",
            created_at="2026-01-01T00:00:00+00:00",
        )
        d = s.to_dict()
        s2 = UserSession.from_dict(d)
        assert s2.user_id == "u1"
        assert s2.trust_level == "TRUSTED"


# ── C16: System Prompt Re-anchoring tests ─────────────────────────────────────

class TestSystemPromptReanchoring:
    def test_reanchor_prepends_preamble(self, mgr):
        """Re-anchoring prepends a security notice to the system prompt."""
        session = mgr.get_or_create_session("u_reanchor")
        original = "You are a helpful assistant."
        result = mgr.reanchor_system_prompt(session, original)
        assert result.endswith(original)
        assert result != original  # preamble was added

    def test_reanchor_contains_security_notice(self, mgr):
        """Preamble contains a security notice keyword."""
        session = mgr.get_or_create_session("u_notice")
        prompt = "SYSTEM: Do everything."
        result = mgr.reanchor_system_prompt(session, prompt)
        assert "[SECURITY" in result

    def test_reanchor_preserves_original_content(self, mgr):
        """Original system prompt content is always preserved in the output."""
        session = mgr.get_or_create_session("u_preserve")
        prompt = "Be concise and accurate."
        result = mgr.reanchor_system_prompt(session, prompt)
        assert prompt in result
