# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""TDD — Workstream A (v1.2.0): Group approval routing.

Tests that:
  - When an approval is required in a group context, the owner receives the DM.
  - The group chat receives a thread reply notification.
  - GroupApprovalRouter correctly identifies the owner and the originating group.
  - Approvals from DM-context route only to owner DM (no group notification).
"""

from __future__ import annotations

from typing import Any

import pytest

from gateway.approval_queue.group_router import GroupApprovalRouter
from gateway.ingest_api.models import ApprovalRequest

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

OWNER_ID = "8096968754"
GROUP_A_CHAT_ID = "-1001000000001"
GROUP_B_CHAT_ID = "-1001000000002"
GROUP_A_AGENT_ID = f"group-{GROUP_A_CHAT_ID}"
MEMBER_USER_ID = "8506022825"
BOT_TOKEN = "123456789:AAbbCCddEEff-test"

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture
def mock_send_message():
    """Mock async Telegram sendMessage to capture DM and group notifications."""
    sent: list[dict[str, Any]] = []

    async def _send(bot_token: str, chat_id: str, text: str, **kwargs) -> dict:
        sent.append({"bot_token": bot_token, "chat_id": chat_id, "text": text, **kwargs})
        return {"ok": True, "result": {"message_id": len(sent)}}

    return _send, sent


@pytest.fixture
def router(mock_send_message):
    """GroupApprovalRouter wired with a mock Telegram send function."""
    send_fn, _ = mock_send_message
    return GroupApprovalRouter(
        owner_chat_id=OWNER_ID,
        bot_token=BOT_TOKEN,
        send_message_fn=send_fn,
    )


@pytest.fixture
def router_with_sent(mock_send_message):
    """Return (router, sent_list) tuple for assertion convenience."""
    send_fn, sent = mock_send_message
    router = GroupApprovalRouter(
        owner_chat_id=OWNER_ID,
        bot_token=BOT_TOKEN,
        send_message_fn=send_fn,
    )
    return router, sent


# ---------------------------------------------------------------------------
# Class A: Group-context approvals route to owner DM + group thread
# ---------------------------------------------------------------------------


class TestGroupApprovalOwnerDM:
    """Owner must receive a DM when an approval originates from a group chat."""

    @pytest.mark.asyncio
    async def test_owner_receives_dm_for_group_approval(self, router_with_sent):
        """owner_chat_id receives a DM notification for every group-context approval."""
        router, sent = router_with_sent
        request = ApprovalRequest(
            action_type="external_api_calls",
            description="Fetch weather API",
            details={"url": "https://api.weather.example.com"},
            agent_id=GROUP_A_AGENT_ID,
        )

        await router.route_approval(request, group_chat_id=GROUP_A_CHAT_ID)

        owner_messages = [m for m in sent if m["chat_id"] == OWNER_ID]
        assert len(owner_messages) >= 1, "Owner must receive at least one DM notification"

    @pytest.mark.asyncio
    async def test_owner_dm_references_group_chat_id(self, router_with_sent):
        """Owner DM message text must reference the originating group chat_id."""
        router, sent = router_with_sent
        request = ApprovalRequest(
            action_type="email_sending",
            description="Send report email",
            details={"to": "team@example.com"},
            agent_id=GROUP_A_AGENT_ID,
        )

        await router.route_approval(request, group_chat_id=GROUP_A_CHAT_ID)

        owner_dms = [m for m in sent if m["chat_id"] == OWNER_ID]
        assert any(
            GROUP_A_CHAT_ID in m["text"] for m in owner_dms
        ), f"Owner DM must reference the group chat_id {GROUP_A_CHAT_ID}"

    @pytest.mark.asyncio
    async def test_group_chat_receives_thread_reply(self, router_with_sent):
        """The originating group chat must receive a thread-reply notification."""
        router, sent = router_with_sent
        request = ApprovalRequest(
            action_type="file_deletion",
            description="Delete old logs",
            details={"path": "/var/log/old"},
            agent_id=GROUP_A_AGENT_ID,
        )

        await router.route_approval(request, group_chat_id=GROUP_A_CHAT_ID)

        group_messages = [m for m in sent if m["chat_id"] == GROUP_A_CHAT_ID]
        assert len(group_messages) >= 1, "Group chat must receive a notification reply"

    @pytest.mark.asyncio
    async def test_both_owner_dm_and_group_notified(self, router_with_sent):
        """A single group-context approval triggers both owner DM AND group reply."""
        router, sent = router_with_sent
        request = ApprovalRequest(
            action_type="skill_installation",
            description="Install external skill",
            details={"skill": "web-scraper"},
            agent_id=GROUP_A_AGENT_ID,
        )

        await router.route_approval(request, group_chat_id=GROUP_A_CHAT_ID)

        chat_ids_notified = {m["chat_id"] for m in sent}
        assert OWNER_ID in chat_ids_notified, "Owner DM must be included"
        assert GROUP_A_CHAT_ID in chat_ids_notified, "Group chat must be included"

    @pytest.mark.asyncio
    async def test_owner_dm_contains_action_type(self, router_with_sent):
        """Owner DM must describe the action_type that requires approval."""
        router, sent = router_with_sent
        request = ApprovalRequest(
            action_type="external_api_calls",
            description="API call needs approval",
            details={},
            agent_id=GROUP_A_AGENT_ID,
        )

        await router.route_approval(request, group_chat_id=GROUP_A_CHAT_ID)

        owner_dms = [m for m in sent if m["chat_id"] == OWNER_ID]
        assert any(
            "external_api_calls" in m["text"] for m in owner_dms
        ), "Owner DM must describe the action type"


# ---------------------------------------------------------------------------
# Class B: DM-context approvals route only to owner DM (no group)
# ---------------------------------------------------------------------------


class TestDMApprovalOwnerOnly:
    """DM-context approvals must not trigger group notifications."""

    @pytest.mark.asyncio
    async def test_dm_approval_routes_only_to_owner(self, router_with_sent):
        """When group_chat_id is None, only the owner receives a notification."""
        router, sent = router_with_sent
        request = ApprovalRequest(
            action_type="email_sending",
            description="Send DM email",
            details={"to": "owner@example.com"},
            agent_id="collab-8506022825",
        )

        await router.route_approval(request, group_chat_id=None)

        # Only owner should be notified — no group messages
        assert len(sent) == 1, "Exactly one notification for DM-context approval"
        assert sent[0]["chat_id"] == OWNER_ID

    @pytest.mark.asyncio
    async def test_dm_approval_no_group_side_effect(self, router_with_sent):
        """DM approval must not send any message to a group chat ID."""
        router, sent = router_with_sent
        request = ApprovalRequest(
            action_type="file_deletion",
            description="Delete user file",
            details={},
            agent_id="collab-8506022825",
        )

        await router.route_approval(request, group_chat_id=None)

        group_messages = [m for m in sent if str(m["chat_id"]).startswith("-")]
        assert len(group_messages) == 0, "No group chat notifications for DM-context approval"


# ---------------------------------------------------------------------------
# Class C: Router correctly identifies group context from agent_id
# ---------------------------------------------------------------------------


class TestGroupApprovalRouterContextDetection:
    """GroupApprovalRouter must correctly distinguish group vs DM context."""

    def test_is_group_context_true_for_group_agent_id(self):
        """agent_id starting with 'group-' is recognized as group context."""
        router = GroupApprovalRouter(
            owner_chat_id=OWNER_ID,
            bot_token=BOT_TOKEN,
        )
        assert router.is_group_context(GROUP_A_AGENT_ID) is True

    def test_is_group_context_false_for_collab_agent_id(self):
        """agent_id starting with 'collab-' is NOT recognized as group context."""
        router = GroupApprovalRouter(
            owner_chat_id=OWNER_ID,
            bot_token=BOT_TOKEN,
        )
        assert router.is_group_context("collab-8506022825") is False

    def test_is_group_context_false_for_default(self):
        """agent_id='default' is NOT recognized as group context."""
        router = GroupApprovalRouter(
            owner_chat_id=OWNER_ID,
            bot_token=BOT_TOKEN,
        )
        assert router.is_group_context("default") is False

    def test_extract_chat_id_from_group_agent_id(self):
        """Extract the raw chat_id from a group-{chat_id} agent_id."""
        router = GroupApprovalRouter(
            owner_chat_id=OWNER_ID,
            bot_token=BOT_TOKEN,
        )
        chat_id = router.extract_group_chat_id(GROUP_A_AGENT_ID)
        assert chat_id == GROUP_A_CHAT_ID

    def test_extract_chat_id_returns_none_for_non_group(self):
        """extract_group_chat_id returns None for non-group agent IDs."""
        router = GroupApprovalRouter(
            owner_chat_id=OWNER_ID,
            bot_token=BOT_TOKEN,
        )
        assert router.extract_group_chat_id("collab-8506022825") is None
        assert router.extract_group_chat_id("default") is None

    @pytest.mark.asyncio
    async def test_route_approval_auto_detects_group_context(self, router_with_sent):
        """route_approval auto-detects group context when group_chat_id not explicitly passed."""
        router, sent = router_with_sent
        request = ApprovalRequest(
            action_type="email_sending",
            description="Group triggered email",
            details={},
            agent_id=GROUP_A_AGENT_ID,
        )

        # Don't pass group_chat_id — should be auto-detected from agent_id
        await router.route_approval(request)

        chat_ids_notified = {m["chat_id"] for m in sent}
        assert OWNER_ID in chat_ids_notified
        assert GROUP_A_CHAT_ID in chat_ids_notified


# ---------------------------------------------------------------------------
# Class D: Default send stub (coverage for _default_send)
# ---------------------------------------------------------------------------


class TestGroupApprovalRouterDefaultSend:
    """Cover the no-op _default_send stub used when no transport is injected."""

    @pytest.mark.asyncio
    async def test_default_send_stub_returns_ok(self):
        """GroupApprovalRouter._default_send returns {ok: True} without raising."""
        result = await GroupApprovalRouter._default_send(
            bot_token="test-token", chat_id="12345", text="Test message"
        )
        assert result.get("ok") is True

    @pytest.mark.asyncio
    async def test_router_works_without_send_fn(self):
        """Router with no send_message_fn uses the default stub (no network calls)."""
        router = GroupApprovalRouter(
            owner_chat_id=OWNER_ID,
            bot_token=BOT_TOKEN,
            # No send_message_fn — uses _default_send internally
        )
        request = ApprovalRequest(
            action_type="email_sending",
            description="Test with default stub",
            details={},
            agent_id=GROUP_A_AGENT_ID,
        )
        # Should not raise even without a real Telegram transport
        await router.route_approval(request, group_chat_id=GROUP_A_CHAT_ID)
