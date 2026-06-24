# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Group-aware Approval Router (v1.2.0 Workstream A).

When an approval request originates from a Telegram group workspace, this
router:
  1. Sends a DM to the owner (owner_chat_id) with the action details and
     the originating group chat_id.
  2. Sends a thread-reply notification to the originating group chat so
     group members can see that an approval request was submitted.

For DM-context approvals (group_chat_id is None), only the owner DM is sent.

Architecture:
  GroupApprovalRouter is injected into EnhancedApprovalQueue at construction
  time. The queue calls route_approval() after every submit() call when the
  request comes from a group context agent_id (prefixed with "group-").

IEC 62443 FR6 (SL3): tamper-evident audit trail for every approval event.
"""

from __future__ import annotations

import logging
from typing import Any, Awaitable, Callable, Optional

from gateway.ingest_api.models import ApprovalRequest

logger = logging.getLogger("agentshroud.approval_queue.group_router")

# Sentinel prefix that identifies group-context agent IDs.
_GROUP_AGENT_PREFIX = "group-"

# Default async send_message stub when no Telegram transport is provided.
# Real production code injects the TelegramAPIProxy._send helper.
_NOOP_SEND: Callable[..., Awaitable[dict[str, Any]]] = None  # type: ignore[assignment]


class GroupApprovalRouter:
    """Routes approval notifications to owner DM and (optionally) group thread.

    Args:
        owner_chat_id: Telegram chat_id of the owner who must receive every DM.
        bot_token: Bot token used to call the Telegram sendMessage API.
        send_message_fn: Async callable with signature
            ``async (bot_token, chat_id, text, **kwargs) -> dict``.
            Defaults to a no-op stub if not provided (safe for unit testing
            without network access).
    """

    def __init__(
        self,
        owner_chat_id: str,
        bot_token: str = "",
        send_message_fn: Optional[Callable[..., Awaitable[dict[str, Any]]]] = None,
    ):
        self.owner_chat_id = str(owner_chat_id)
        self.bot_token = bot_token
        self._send = send_message_fn or self._default_send

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    async def route_approval(
        self,
        request: ApprovalRequest,
        group_chat_id: Optional[str] = None,
    ) -> None:
        """Route an approval notification to the appropriate recipients.

        Routing logic:
          - If group_chat_id is None AND agent_id is a group agent:
            auto-detect group_chat_id from agent_id.
          - If group_chat_id is known: send DM to owner + reply in group.
          - If no group context: send DM to owner only.

        Args:
            request: The ApprovalRequest being routed.
            group_chat_id: The Telegram chat_id of the originating group, or
                None if not yet determined (auto-detected from agent_id).
        """
        # Auto-detect group_chat_id from agent_id when not explicitly provided.
        if group_chat_id is None:
            group_chat_id = self.extract_group_chat_id(request.agent_id)

        owner_text = self._build_owner_dm_text(request, group_chat_id)
        await self._send(self.bot_token, self.owner_chat_id, owner_text)
        logger.info(
            "GroupApprovalRouter: DM sent to owner=%s action=%s agent=%s",
            self.owner_chat_id,
            request.action_type,
            request.agent_id,
        )

        if group_chat_id:
            group_text = self._build_group_reply_text(request)
            await self._send(self.bot_token, group_chat_id, group_text)
            logger.info(
                "GroupApprovalRouter: group reply sent to chat_id=%s action=%s",
                group_chat_id,
                request.action_type,
            )

    # ------------------------------------------------------------------
    # Context detection helpers
    # ------------------------------------------------------------------

    def is_group_context(self, agent_id: str) -> bool:
        """Return True if agent_id represents a Telegram group workspace."""
        return str(agent_id).startswith(_GROUP_AGENT_PREFIX)

    def extract_group_chat_id(self, agent_id: str) -> Optional[str]:
        """Extract the raw chat_id from a group-{chat_id} agent_id.

        Returns None if the agent_id is not a group agent.
        """
        if not self.is_group_context(agent_id):
            return None
        return agent_id[len(_GROUP_AGENT_PREFIX):]

    # ------------------------------------------------------------------
    # Message builders
    # ------------------------------------------------------------------

    def _build_owner_dm_text(
        self, request: ApprovalRequest, group_chat_id: Optional[str]
    ) -> str:
        """Build the owner DM notification text."""
        if group_chat_id:
            origin = f"Group chat {group_chat_id}"
        else:
            origin = f"Agent {request.agent_id}"

        return (
            f"🛡️ AgentShroud Approval Request\n\n"
            f"Action: {request.action_type}\n"
            f"From: {origin}\n"
            f"Description: {request.description}\n\n"
            f"Reply /approve or /deny to this request."
        )

    def _build_group_reply_text(self, request: ApprovalRequest) -> str:
        """Build the group thread reply notification text."""
        return (
            f"🛡️ Approval request submitted for: {request.action_type}\n"
            f"{request.description}\n\n"
            "The owner has been notified and will review this request."
        )

    # ------------------------------------------------------------------
    # Default stub send (no-op for unit tests without network)
    # ------------------------------------------------------------------

    @staticmethod
    async def _default_send(
        bot_token: str, chat_id: str, text: str, **kwargs: Any
    ) -> dict[str, Any]:
        """No-op send stub — used when no transport is injected."""
        logger.debug(
            "GroupApprovalRouter._default_send: bot=%s chat_id=%s text_len=%d",
            bot_token[:10] if bot_token else "",
            chat_id,
            len(text),
        )
        return {"ok": True, "result": {}}
