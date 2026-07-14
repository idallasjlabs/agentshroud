# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for gateway/security/session_manager.py — session isolation and security."""

from __future__ import annotations

from pathlib import Path

import pytest

from gateway.security.session_manager import (
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
# Multi-bot workspace isolation (v1.1.0)
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

        # Write a legacy session_registry.json with a plain user_id key
        registry_path = tmp_path / "session_registry.json"
        legacy_workspace = tmp_path / "users" / "old-user" / "workspace"
        legacy_memory = tmp_path / "users" / "old-user" / "MEMORY.md"
        legacy_workspace.mkdir(parents=True)
        legacy_memory.write_text("# Legacy MEMORY\n")
        registry_path.write_text(
            json.dumps(
                {
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
                }
            )
        )

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


# ---------------------------------------------------------------------------
# Atomic / serialized registry persistence (SCRUM-95)
# ---------------------------------------------------------------------------


class TestAtomicRegistryWrites:
    """Registry writes must be atomic (os.replace) and serialized (lock).

    The session registry lives on a volume shared by multiple bot processes
    (OpenClaw + Hermes).  Non-atomic writes could interleave and corrupt the
    file or drop entries.  These tests pin the durability guarantee.
    """

    def test_save_uses_atomic_replace(self, mgr, monkeypatch):
        """_save_sessions must go through os.replace(tmp, final), never a
        partial in-place write of the destination file."""
        import gateway.security.session_manager as sm

        calls = []
        real_replace = sm.os.replace

        def spy_replace(src, dst):
            calls.append((str(src), str(dst)))
            return real_replace(src, dst)

        monkeypatch.setattr(sm.os, "replace", spy_replace)

        mgr.get_or_create_session("user-atomic")  # triggers a save

        assert calls, "os.replace was never called — write was not atomic"
        # The destination of the atomic rename must be the real registry file,
        # and the source must be a *different* temp file in the same directory.
        src, dst = calls[-1]
        assert dst == str(mgr.session_metadata_file)
        assert src != dst
        assert Path(src).parent == mgr.session_metadata_file.parent

    def test_no_temp_files_left_behind(self, mgr):
        """A successful save leaves only the final registry file, no *.tmp."""
        mgr.get_or_create_session("user-clean")
        leftovers = list(mgr.session_metadata_file.parent.glob("session_registry.json.*"))
        assert leftovers == [], f"temp files left behind: {leftovers}"

    def test_load_tolerates_corrupt_registry(self, tmp_path):
        """A corrupt/partial registry file must not crash construction."""
        registry_path = tmp_path / "session_registry.json"
        registry_path.write_text('{"user-1": {"user_id": "user-1", "workspace')  # truncated JSON

        # Must not raise; manager comes up with an empty session cache.
        mgr2 = UserSessionManager(base_workspace=tmp_path, owner_user_id="owner")
        assert mgr2.sessions == {}

        # And it must still be able to create + persist a fresh session.
        s = mgr2.get_or_create_session("user-1")
        assert s.user_id == "user-1"

    def test_load_tolerates_empty_registry(self, tmp_path):
        """An empty registry file must not crash construction."""
        registry_path = tmp_path / "session_registry.json"
        registry_path.write_text("")
        mgr2 = UserSessionManager(base_workspace=tmp_path, owner_user_id="owner")
        assert mgr2.sessions == {}

    def test_atomic_save_never_leaves_partial_registry_on_crash(self, mgr, monkeypatch):
        """If the write to the temp file fails mid-flight, the existing
        registry on disk must remain intact and readable (not truncated)."""
        import json

        # Seed a valid registry with one persisted session.
        mgr.get_or_create_session("survivor")
        good_bytes = mgr.session_metadata_file.read_bytes()
        good_data = json.loads(good_bytes)
        assert any("survivor" in k for k in good_data)

        # Now make json.dump blow up partway through the *next* save.
        import gateway.security.session_manager as sm

        def boom(*_args, **_kwargs):
            raise OSError("disk full")

        monkeypatch.setattr(sm.json, "dump", boom)

        # This save fails internally (logged, swallowed) — must not corrupt file.
        mgr.get_or_create_session("newcomer")

        # Original registry file is byte-for-byte intact.
        assert mgr.session_metadata_file.read_bytes() == good_bytes
        # No stray temp files from the failed write.
        leftovers = list(mgr.session_metadata_file.parent.glob("session_registry.json.*"))
        assert leftovers == []

    def test_concurrent_saves_do_not_lose_entries(self, mgr):
        """Concurrent add_conversation_message calls (each of which saves) must
        not drop sessions from the on-disk registry."""
        import json
        import threading

        user_ids = [f"user-{i:03d}" for i in range(40)]

        # Pre-create sessions so each thread only mutates + saves.
        for uid in user_ids:
            mgr.get_or_create_session(uid)

        barrier = threading.Barrier(len(user_ids))

        def worker(uid: str):
            barrier.wait()
            mgr.add_conversation_message(uid, "user", f"msg from {uid}")

        threads = [threading.Thread(target=worker, args=(uid,)) for uid in user_ids]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        # The final on-disk registry must parse cleanly and contain every user.
        data = json.loads(mgr.session_metadata_file.read_text())
        keys = set(data.keys())
        for uid in user_ids:
            assert f"{uid}::openclaw" in keys, f"lost registry entry for {uid}"


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
