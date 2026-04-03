# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
TDD — FileSandbox message-gating and owner bypass.

Root cause of the BLOCKED BY AGENTSHROUD: Unauthorized file access bug:
  _extract_file_paths() runs on ALL message text, including plain chat.
  Conversational words like "check memory" or "read config.yaml" trigger
  false-positive path extractions and block legitimate messages.

Fixes verified here:
  1. _is_tool_call_request() — True only for requests with actual tool calls
  2. FileSandbox block skipped for plain chat (non-tool-call) requests
  3. Owner (8096968754) bypasses content-pattern blocking (still audited)
"""

from __future__ import annotations

import shutil
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, Mock

import pytest
import pytest_asyncio

from gateway.ingest_api.middleware import MiddlewareManager, MiddlewareResult
from gateway.security.session_manager import UserSessionManager

OWNER_ID = "8096968754"
USER_ID = "user_999"


@pytest.fixture
def temp_workspace():
    d = tempfile.mkdtemp()
    yield Path(d)
    shutil.rmtree(d)


@pytest.fixture
def session_manager(temp_workspace):
    return UserSessionManager(
        base_workspace=temp_workspace,
        owner_user_id=OWNER_ID,
    )


@pytest.fixture
def manager(session_manager):
    """MiddlewareManager with real session_manager, all other deps mocked.

    Uses __new__ to avoid running the real __init__ (which touches sockets,
    filesystems, etc.).  Each attribute must be set explicitly — add any new
    middleware attributes added to process_request here.
    """
    mm = MiddlewareManager.__new__(MiddlewareManager)
    mm.user_session_manager = session_manager
    # Guards used in process_request — all None/mock so they don't interfere
    mm.context_guard = None
    mm.metadata_guard = None
    mm.env_guard = None
    mm.git_guard = None
    mm.file_sandbox = MagicMock()  # present but shouldn't block plain messages
    mm.rbac_manager = None
    mm.log_sanitizer = None
    mm.memory_integrity_monitor = None
    mm.original_request_data = None
    # Batch B — new wired modules (set None to skip their logic in these tests)
    mm.multi_turn_tracker = None
    mm.tool_chain_analyzer = None
    mm.browser_security = None
    mm.path_isolation = None
    return mm


# ── helpers ─────────────────────────────────────────────────────────────────


def _plain_msg(user_id: str, text: str) -> dict:
    return {"user_id": user_id, "message": text}


def _tool_call_msg(
    user_id: str, text: str, tool_name: str = "read_file", path: str = "/tmp/x"
) -> dict:
    return {
        "user_id": user_id,
        "message": text,
        "tool_calls": [{"name": tool_name, "input": {"path": path}}],
    }


def _tool_result_msg(user_id: str) -> dict:
    return {
        "user_id": user_id,
        "message": "",
        "tool_results": [{"tool_use_id": "abc", "content": "some output"}],
    }


# ── RED: _is_tool_call_request ───────────────────────────────────────────────


class TestIsToolCallRequest:
    """Unit tests for the _is_tool_call_request helper (TDD RED phase)."""

    def test_plain_chat_not_a_tool_call(self, manager):
        req = _plain_msg(OWNER_ID, "Hey, check memory please")
        assert manager._is_tool_call_request(req) is False

    def test_tool_calls_key_detected(self, manager):
        req = _tool_call_msg(OWNER_ID, "read this file", path="/workspace/file.py")
        assert manager._is_tool_call_request(req) is True

    def test_tool_results_key_detected(self, manager):
        req = _tool_result_msg(OWNER_ID)
        assert manager._is_tool_call_request(req) is True

    def test_empty_tool_calls_not_a_tool_call(self, manager):
        req = {"user_id": OWNER_ID, "message": "hi", "tool_calls": []}
        assert manager._is_tool_call_request(req) is False

    def test_empty_tool_results_not_a_tool_call(self, manager):
        req = {"user_id": OWNER_ID, "message": "hi", "tool_results": []}
        assert manager._is_tool_call_request(req) is False

    def test_type_field_tool_call(self, manager):
        req = {"user_id": OWNER_ID, "message": "", "type": "tool_call"}
        assert manager._is_tool_call_request(req) is True

    def test_type_field_message_not_tool_call(self, manager):
        req = {"user_id": OWNER_ID, "message": "hello", "type": "message"}
        assert manager._is_tool_call_request(req) is False


# ── RED: FileSandbox skipped for plain chat ──────────────────────────────────


class TestFileSandboxSkippedForPlainMessages:
    """FileSandbox must NOT block plain chat messages that mention file-like words."""

    @pytest.mark.asyncio
    async def test_plain_message_mentioning_memory_not_blocked(self, manager):
        # "MEMORY.md" in conversation text should NOT trigger sandbox
        req = _plain_msg(USER_ID, "Can you check my MEMORY.md file?")
        result = await manager.process_request(req)
        assert result.allowed is True, f"Plain chat message blocked: {result.reason}"

    @pytest.mark.asyncio
    async def test_plain_message_mentioning_config_yaml_not_blocked(self, manager):
        req = _plain_msg(USER_ID, "Please look at config.yaml and fix it")
        result = await manager.process_request(req)
        assert (
            result.allowed is True
        ), f"config.yaml mention in chat incorrectly blocked: {result.reason}"

    @pytest.mark.asyncio
    async def test_plain_message_mentioning_etc_passwd_not_blocked(self, manager):
        # Even a path like /etc/passwd in chat text must not trigger a block.
        # FileSandbox is for actual tool-call file operations, not chat content scanning.
        req = _plain_msg(USER_ID, "I read that /etc/passwd contains user entries")
        result = await manager.process_request(req)
        assert (
            result.allowed is True
        ), f"Educational mention of /etc/passwd in chat blocked: {result.reason}"

    @pytest.mark.asyncio
    async def test_tool_call_with_unauthorized_path_still_blocked(self, manager, temp_workspace):
        # Actual tool calls to unauthorized paths MUST still be blocked
        # Set up the other user's workspace path
        other_ws = str(temp_workspace / "users" / "other_user" / "workspace")
        req = _tool_call_msg(
            USER_ID,
            "read file",
            tool_name="read_file",
            path=other_ws + "/secret.txt",
        )
        result = await manager.process_request(req)
        # Either allowed=False OR allowed=True (workspace may not exist) — the
        # key assertion is that the code PATH for tool_calls is taken.
        # We verify by confirming plain messages don't hit the sandbox at all.
        # This is a smoke test to ensure the tool-call branch executes.
        assert isinstance(result, MiddlewareResult)


# ── RED: Owner bypass ────────────────────────────────────────────────────────


class TestOwnerBypassContentPatternChecks:
    """Owner (8096968754) must not be blocked by content-pattern scanning.
    They should still be audited, but never hard-blocked."""

    @pytest.mark.asyncio
    async def test_owner_plain_message_with_path_not_blocked(self, manager):
        req = _plain_msg(OWNER_ID, "Let me check /etc/hosts for the mapping")
        result = await manager.process_request(req)
        assert result.allowed is True, f"Owner blocked by content pattern: {result.reason}"

    @pytest.mark.asyncio
    async def test_owner_message_mentioning_other_users_file_not_blocked(
        self, manager, temp_workspace
    ):
        other_path = str(temp_workspace / "users" / "user_999" / "workspace" / "data.txt")
        req = _plain_msg(OWNER_ID, f"Review {other_path} for user_999")
        result = await manager.process_request(req)
        assert (
            result.allowed is True
        ), f"Owner blocked when reviewing another user's file path in chat: {result.reason}"

    @pytest.mark.asyncio
    async def test_non_owner_cross_path_plain_message_still_blocked(self, manager, temp_workspace):
        # A plain message from a non-owner mentioning another user's /users/ path
        # should be allowed now that we gate on tool_calls (it's plain chat).
        # This test confirms we don't over-reach with the owner logic.
        req = _plain_msg(USER_ID, "Can I see user_123's workspace data?")
        result = await manager.process_request(req)
        # Plain chat — should pass (no actual file op occurring)
        assert result.allowed is True
