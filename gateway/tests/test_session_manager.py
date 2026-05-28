# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
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
        # list_sessions_for_user now returns "user_id::bot_id" keys
        assert any("user-1" in k for k in visible)
        assert any("user-2" in k for k in visible)

    def test_non_owner_cannot_view_other_sessions(self, mgr):
        mgr.get_or_create_session("user-1")
        mgr.get_or_create_session("user-2")
        visible = mgr.list_sessions_for_user("user-1")
        # user-1 sees their own session key(s) but not user-2's
        assert any("user-1" in k for k in visible)
        assert not any("user-2" in k for k in visible)

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


# ---------------------------------------------------------------------------
# Multi-bot workspace isolation (v1.4.0)
# ---------------------------------------------------------------------------


class TestMultiBotIsolation:
    """Verify that different bots get independent workspaces per user."""

    def test_different_bots_get_different_workspace_dirs(self, mgr):
        """openclaw and hermes sessions for the same user must not share a directory."""
        s_oc = mgr.get_or_create_session("user-1", bot_id="openclaw")
        s_hm = mgr.get_or_create_session("user-1", bot_id="hermes")
        assert s_oc.workspace_dir != s_hm.workspace_dir
        assert not str(s_oc.workspace_dir).startswith(str(s_hm.workspace_dir))

    def test_different_bots_get_different_memory_files(self, mgr):
        s_oc = mgr.get_or_create_session("user-1", bot_id="openclaw")
        s_hm = mgr.get_or_create_session("user-1", bot_id="hermes")
        assert s_oc.memory_file != s_hm.memory_file

    def test_same_bot_same_user_returns_same_session(self, mgr):
        s1 = mgr.get_or_create_session("user-1", bot_id="openclaw")
        s2 = mgr.get_or_create_session("user-1", bot_id="openclaw")
        assert s1.workspace_dir == s2.workspace_dir

    def test_session_bot_id_stored_correctly(self, mgr):
        s = mgr.get_or_create_session("user-1", bot_id="hermes")
        assert s.bot_id == "hermes"

    def test_default_bot_id_is_openclaw(self, mgr):
        s = mgr.get_or_create_session("user-1")
        assert s.bot_id == "openclaw"

    def test_workspace_paths_under_bot_namespace(self, mgr, tmp_path):
        s = mgr.get_or_create_session("user-1", bot_id="openclaw")
        # Expect: base/users/user-1/bots/openclaw/workspace
        assert "bots" in str(s.workspace_dir)
        assert "openclaw" in str(s.workspace_dir)

    def test_invalid_bot_id_rejected(self, mgr):
        with pytest.raises(ValueError):
            mgr.get_or_create_session("user-1", bot_id="../evil")

    def test_long_bot_id_rejected(self, mgr):
        with pytest.raises(ValueError):
            mgr.get_or_create_session("user-1", bot_id="b" * 33)

    def test_conversation_histories_are_bot_scoped(self, mgr):
        mgr.get_or_create_session("user-1", bot_id="openclaw")
        mgr.get_or_create_session("user-1", bot_id="hermes")
        mgr.add_conversation_message("user-1", "user", "hello via openclaw", bot_id="openclaw")
        mgr.add_conversation_message("user-1", "user", "hello via hermes", bot_id="hermes")

        s_oc = mgr.get_or_create_session("user-1", bot_id="openclaw")
        s_hm = mgr.get_or_create_session("user-1", bot_id="hermes")
        assert len(s_oc.conversation_history) == 1
        assert len(s_hm.conversation_history) == 1
        assert s_oc.conversation_history[0].content == "hello via openclaw"
        assert s_hm.conversation_history[0].content == "hello via hermes"

    def test_session_context_includes_bot_id(self, mgr):
        ctx = mgr.get_session_context("user-1", bot_id="hermes")
        assert ctx["bot_id"] == "hermes"

    def test_session_registry_uses_compound_key(self, mgr):
        mgr.get_or_create_session("user-1", bot_id="openclaw")
        mgr.get_or_create_session("user-1", bot_id="hermes")
        assert "user-1::openclaw" in mgr.sessions
        assert "user-1::hermes" in mgr.sessions

    def test_legacy_session_promoted_on_load(self, tmp_path):
        """Existing plain user_id keys (no separator) are promoted to user::openclaw."""
        import json
        from pathlib import Path

        # Write a legacy session_registry.json with a plain user_id key
        registry_path = tmp_path / "session_registry.json"
        legacy_workspace = tmp_path / "users" / "old-user" / "workspace"
        legacy_memory = tmp_path / "users" / "old-user" / "MEMORY.md"
        legacy_workspace.mkdir(parents=True)
        legacy_memory.write_text("# Legacy MEMORY\n")
        registry_path.write_text(json.dumps({
            "old-user": {
                "user_id": "old-user",
                "workspace_dir": str(legacy_workspace),
                "memory_file": str(legacy_memory),
                "conversation_history": [],
                "trust_level": "UNTRUSTED",
                "created_at": None,
                "last_active": None,
                "metadata": {},
            }
        }))

        mgr2 = UserSessionManager(base_workspace=tmp_path, owner_user_id="owner")
        # Legacy key must be promoted to compound form
        assert "old-user::openclaw" in mgr2.sessions
        assert "old-user" not in mgr2.sessions

    def test_lazy_migration_copies_legacy_memory(self, tmp_path):
        """If legacy users/{uid}/MEMORY.md exists, first openclaw session copies it."""
        legacy_memory = tmp_path / "users" / "migrated-user" / "MEMORY.md"
        legacy_memory.parent.mkdir(parents=True)
        legacy_memory.write_text("# Old memory content\n")

        mgr2 = UserSessionManager(base_workspace=tmp_path, owner_user_id="owner")
        s = mgr2.get_or_create_session("migrated-user", bot_id="openclaw")
        assert s.memory_file.exists()
        assert "Old memory content" in s.memory_file.read_text()


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
