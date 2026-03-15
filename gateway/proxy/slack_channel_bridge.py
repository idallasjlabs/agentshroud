# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""
Slack↔Telegram channel bridge.

Translates inbound Slack events into synthetic Telegram update objects queued
for the bot's existing getUpdates polling loop.  No new bot endpoint required.

Outbound routing: when the bot calls sendMessage/editMessageText with a bridge
chat_id, the gateway detects it here and routes the reply to Slack instead of
Telegram.

Chat ID scheme:
  Fake Telegram chat IDs are derived deterministically from the Slack channel ID
  using an MD5 hash offset from _BRIDGE_BASE.  They live in a range well below
  any real Telegram ID (which are positive 32-bit integers or small negatives for
  groups).  Collision with a real Telegram chat_id is astronomically unlikely.

User ID scheme:
  Fake Telegram user IDs are derived from the Slack user ID using the same hash
  approach, offset from _USER_BASE (7 billion+) — above the current Telegram
  user ID range.
"""
from __future__ import annotations

import asyncio
import hashlib
import logging
import os
import time
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger("agentshroud.proxy.slack_bridge")

# Fake chat_id range: large positives above current Telegram user ID space.
# MUST be positive so OpenClaw classifies them as private/direct chats
# (negative IDs are Telegram groups — OpenClaw ignores those without an explicit binding).
# NOTE: for the owner, the REAL Telegram owner ID is used instead of a fake one
# (see enqueue_update) — that is the only way to match OpenClaw's binding.
_BRIDGE_BASE: int = 9_000_000_000
# Fake user_id range: also large positives, distinct from _BRIDGE_BASE range
_USER_BASE: int = 7_000_000_000


@dataclass
class SlackSession:
    """Tracks the Slack context for an active bridge conversation."""

    slack_channel: str
    thread_ts: Optional[str]
    slack_user_id: str
    fake_user_id: int
    fake_chat_id: int


class SlackChannelBridge:
    """Bidirectional Slack↔Telegram translation layer.

    Inbound (Slack → bot):
        enqueue_update() builds a fake Telegram update dict and pushes it onto
        the internal asyncio.Queue.  The Telegram proxy drains this queue when
        the bot polls getUpdates and appends the synthetic updates to the real
        Telegram result list.

    Outbound (bot → Slack):
        is_bridge_chat_id() lets the Telegram proxy detect that a sendMessage
        is destined for Slack.  resolve_chat_id() returns the SlackSession so
        the Telegram proxy can route the reply via the Slack proxy.
    """

    def __init__(
        self,
        telegram_owner_id: Optional[int] = None,
        slack_owner_id: str = "",
    ) -> None:
        """
        Args:
            telegram_owner_id: Real Telegram user ID of the owner (e.g. 8096968754).
                Used as chat_id for owner Slack messages so OpenClaw's binding matches.
                Falls back to AGENTSHROUD_OWNER_USER_ID env var if not supplied.
            slack_owner_id: Slack user ID of the owner (e.g. U0AL7640RHD).
                Falls back to AGENTSHROUD_SLACK_OWNER_USER_ID env var if not supplied.
        """
        self._queue: asyncio.Queue = asyncio.Queue()
        # chat_id → SlackSession (chat_id is real Telegram ID for owner, fake for others)
        self._chat_map: dict[int, SlackSession] = {}
        # slack_channel_id → chat_id (stable per channel)
        self._channel_to_chat_id: dict[str, int] = {}
        self._update_id_counter: int = 900_000_000  # high to avoid collision

        # Real Telegram owner ID — resolved from constructor arg or env var.
        if telegram_owner_id is not None:
            self._telegram_owner_id: Optional[int] = telegram_owner_id
        else:
            _owner_env = str(os.environ.get("AGENTSHROUD_OWNER_USER_ID", "")).strip()
            self._telegram_owner_id = int(_owner_env) if _owner_env.isdigit() else None

        # Slack owner ID — resolved from constructor arg or env var.
        self._slack_owner_id: str = slack_owner_id or str(
            os.environ.get("AGENTSHROUD_SLACK_OWNER_USER_ID", "")
        ).strip()

        # Track which chat_ids have an active Slack session vs Telegram session.
        # When the owner uses Telegram, we clear their Slack session so outbound
        # sendMessage(owner_telegram_id) is NOT intercepted and goes to Telegram.
        self._slack_active: dict[int, bool] = {}

    # ── Helpers ──────────────────────────────────────────────────────────────

    def _fake_chat_id_for(self, channel: str) -> int:
        if channel not in self._channel_to_chat_id:
            h = int(hashlib.md5(channel.encode()).hexdigest()[:8], 16)
            self._channel_to_chat_id[channel] = _BRIDGE_BASE - h
        return self._channel_to_chat_id[channel]

    def _fake_user_id_for(self, slack_user_id: str) -> int:
        h = int(hashlib.md5(slack_user_id.encode()).hexdigest()[:7], 16)
        return _USER_BASE + h

    # ── Inbound ──────────────────────────────────────────────────────────────

    def enqueue_update(
        self,
        user_id: str,
        channel: str,
        thread_ts: Optional[str],
        text: str,
    ) -> None:
        """Build a synthetic Telegram update and queue it for the bot.

        Owner messages use the owner's real Telegram user ID as both chat_id and
        from.id so that OpenClaw's binding (peer.id == telegram_owner_id) matches
        and the message is routed to the main agent.  A fake ID would have no binding
        and be silently discarded.

        Non-owner messages (collaborators when COLLAB_LOCAL_INFO_ONLY=0) use hashed
        fake IDs as before.
        """
        is_owner_msg = bool(
            self._slack_owner_id
            and user_id == self._slack_owner_id
            and self._telegram_owner_id is not None
        )

        if is_owner_msg:
            effective_chat_id = self._telegram_owner_id  # type: ignore[assignment]
            effective_user_id = self._telegram_owner_id  # type: ignore[assignment]
            # Mark Slack as the active platform — outbound sendMessage for this
            # chat_id should be routed to Slack until Telegram clears the session.
            self._slack_active[effective_chat_id] = True
            # Also track stable channel→chat_id for getChat intercept
            self._channel_to_chat_id[channel] = effective_chat_id
        else:
            effective_chat_id = self._fake_chat_id_for(channel)
            effective_user_id = self._fake_user_id_for(user_id)

        session = SlackSession(
            slack_channel=channel,
            thread_ts=thread_ts,
            slack_user_id=user_id,
            fake_user_id=effective_user_id,
            fake_chat_id=effective_chat_id,
        )
        self._chat_map[effective_chat_id] = session

        self._update_id_counter += 1
        update = {
            "update_id": self._update_id_counter,
            "message": {
                "message_id": self._update_id_counter,
                "from": {
                    "id": effective_user_id,
                    "is_bot": False,
                    "first_name": "Slack",
                    "username": user_id.lower().replace("_", ""),
                },
                "chat": {
                    "id": effective_chat_id,
                    "type": "private",
                },
                "date": int(time.time()),
                "text": text,
            },
        }
        self._queue.put_nowait(update)
        logger.info(
            "Slack bridge: queued update for channel=%s user=%s chat_id=%d (owner=%s)",
            channel,
            user_id,
            effective_chat_id,
            is_owner_msg,
        )

    def drain_pending(self) -> list[dict]:
        """Drain all pending synthetic updates (called from getUpdates handler)."""
        updates: list[dict] = []
        while not self._queue.empty():
            try:
                updates.append(self._queue.get_nowait())
            except asyncio.QueueEmpty:
                break
        if updates:
            logger.info("Slack bridge: injecting %d synthetic update(s) into getUpdates", len(updates))
        return updates

    # ── Outbound ─────────────────────────────────────────────────────────────

    def is_bridge_chat_id(self, chat_id: int) -> bool:
        """True when an outbound sendMessage to chat_id should be routed to Slack.

        For the owner's real Telegram chat_id, only intercept when Slack is the
        active platform (i.e., the last message came from Slack, not Telegram).
        """
        if chat_id not in self._chat_map:
            return False
        # If we have platform tracking for this chat_id, honour it
        active = self._slack_active.get(chat_id)
        if active is not None:
            return active
        return True

    def on_telegram_message(self, chat_id: int) -> None:
        """Called when a real Telegram message arrives for chat_id.

        Clears the Slack-active flag so that subsequent outbound sendMessage calls
        for this chat_id are forwarded to Telegram instead of Slack.
        """
        if chat_id in self._slack_active:
            self._slack_active[chat_id] = False
            logger.debug("Slack bridge: chat_id=%d now Telegram-active (Slack routing disabled)", chat_id)

    def resolve_chat_id(self, chat_id: int) -> Optional[SlackSession]:
        return self._chat_map.get(chat_id)

    def is_owner_bridge_chat(self, chat_id: int, rbac) -> bool:
        """Return True when this fake chat_id belongs to an owner-role Slack session.

        Used by the Telegram proxy's _is_owner_chat() so that outbound filtering
        grants full owner-level responses on Slack bridge conversations.
        """
        session = self._chat_map.get(chat_id)
        if session is None:
            return False
        return rbac.is_owner(session.slack_user_id)
