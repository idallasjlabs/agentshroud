# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""
Egress Firewall Telegram Inline Button Notifications.

Sends inline keyboard approve/deny buttons to the owner via Telegram
when an unknown domain is encountered by the egress firewall.
Uses urllib (stdlib) to avoid aiohttp dependency.
"""

import asyncio
import json
import logging
import urllib.request
import urllib.parse
from datetime import datetime, timezone, timedelta
from typing import Optional

logger = logging.getLogger("agentshroud.proxy.telegram_egress_notify")

RISK_EMOJI = {"low": "🟢", "medium": "🟡", "high": "🔴", "unknown": "⚪"}


class EgressTelegramNotifier:
    """Sends Telegram inline keyboard notifications for egress approval.

    Supports multiple notification recipients (e.g. owner + backup admin).
    Approval buttons are time-limited: 1h, 4h, 24h, or permanent.
    """

    # Approval durations: button label → seconds (None = permanent)
    APPROVAL_DURATIONS: dict[str, Optional[int]] = {
        "1h": 3600,
        "4h": 14400,
        "24h": 86400,
        "always": None,
    }

    def __init__(self, bot_token: str, owner_chat_id: str,
                 notification_recipients: Optional[list[str]] = None,
                 base_url: str = "https://api.telegram.org",
                 timeout_seconds: int = 30):
        self.bot_token = bot_token
        self.owner_chat_id = owner_chat_id
        # All chat IDs that receive egress approval notifications.
        # Always includes owner_chat_id; additional admins can be added.
        self.notification_recipients: list[str] = list(
            {owner_chat_id, *(notification_recipients or [])}
        )
        self.base_url = base_url
        self.timeout_seconds = timeout_seconds
        self.pending_requests: dict[str, dict] = {}

    def _api_url(self, method: str) -> str:
        return f"{self.base_url}/bot{self.bot_token}/{method}"

    def _send_request(self, method: str, payload: dict) -> dict:
        """Send a request to Telegram Bot API (sync, run in executor)."""
        url = self._api_url(method)
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url, data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode("utf-8"))

    async def _async_send(self, method: str, payload: dict) -> dict:
        """Async wrapper around sync Telegram API call."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._send_request, method, payload)

    async def notify_pending(self, request_id: str, domain: str, port: int,
                             risk_level: str, agent_id: str, tool_name: str) -> bool:
        """Send Telegram message with time-limited approve/deny buttons.

        Buttons: Allow 1h | Allow 4h | Allow 24h | Allow Forever | Deny
        Notification is sent to all configured recipients (owner + any additional admins).
        Returns True if at least one recipient received the message.
        """
        emoji = RISK_EMOJI.get(risk_level, "⚪")
        text = (
            f"🌐 *Egress Request*\n\n"
            f"Domain: `{domain}:{port}`\n"
            f"Risk: {emoji} {risk_level.title()}\n"
            f"Tool: `{tool_name}`\n"
            f"Agent: `{agent_id}`\n"
            f"ID: `{request_id[:8]}`"
        )

        keyboard = {
            "inline_keyboard": [
                [
                    {"text": "✅ 1h", "callback_data": f"egress_allow_1h_{request_id}"},
                    {"text": "✅ 4h", "callback_data": f"egress_allow_4h_{request_id}"},
                    {"text": "✅ 24h", "callback_data": f"egress_allow_24h_{request_id}"},
                    {"text": "✅ Forever", "callback_data": f"egress_allow_always_{request_id}"},
                ],
                [
                    {"text": "❌ Deny", "callback_data": f"egress_deny_{request_id}"},
                ],
            ]
        }

        self.pending_requests[request_id] = {
            "domain": domain,
            "port": port,
            "risk_level": risk_level,
            "agent_id": agent_id,
            "tool_name": tool_name,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        any_ok = False
        for chat_id in self.notification_recipients:
            payload = {
                "chat_id": chat_id,
                "text": text,
                "parse_mode": "Markdown",
                "reply_markup": keyboard,
            }
            try:
                result = await self._async_send("sendMessage", payload)
                if result.get("ok", False):
                    any_ok = True
            except Exception as e:
                logger.error(f"Failed to send egress notification to {chat_id}: {e}")
        return any_ok

    async def handle_callback(self, callback_data: str) -> dict:
        """Process inline button callback. Returns action result.

        Actions: allow_1h, allow_4h, allow_24h, allow_always, deny
        Result includes expires_at (ISO8601) for time-limited approvals, None for permanent.
        """
        # Parse: egress_allow_{duration}_{id} or egress_deny_{id}
        # Map prefix → (action_name, duration_key)
        # action_name is returned directly in the result for downstream use.
        _ALLOW_DURATIONS = {
            "egress_allow_1h_": ("allow_1h", "1h"),
            "egress_allow_4h_": ("allow_4h", "4h"),
            "egress_allow_24h_": ("allow_24h", "24h"),
            "egress_allow_always_": ("allow_always", "always"),
        }

        action = None
        duration_key = None
        request_id = None

        for prefix, (act, dur) in _ALLOW_DURATIONS.items():
            if callback_data.startswith(prefix):
                action = act
                duration_key = dur
                request_id = callback_data[len(prefix):]
                break

        if action is None:
            if callback_data.startswith("egress_deny_"):
                action = "deny"
                duration_key = None
                request_id = callback_data[len("egress_deny_"):]
            else:
                return {"status": "error", "reason": "invalid_format"}

        if not request_id or request_id not in self.pending_requests:
            return {"status": "error", "reason": "request_not_found"}

        request_info = self.pending_requests.pop(request_id)

        # Compute expiry for time-limited approvals
        expires_at = None
        if duration_key and duration_key != "always":
            seconds = self.APPROVAL_DURATIONS.get(duration_key)
            if seconds:
                expires_at = (datetime.now(timezone.utc) + timedelta(seconds=seconds)).isoformat()

        return {
            "status": "ok",
            "action": action,
            "duration": duration_key,
            "request_id": request_id,
            "domain": request_info["domain"],
            "port": request_info["port"],
            "expires_at": expires_at,
            "agent_id": request_info.get("agent_id", ""),
        }

    async def answer_callback(self, callback_query_id: str, text: str) -> bool:
        """Send answerCallbackQuery to dismiss the button loading state."""
        try:
            result = await self._async_send("answerCallbackQuery", {
                "callback_query_id": callback_query_id,
                "text": text,
                "show_alert": False,
            })
            return result.get("ok", False)
        except Exception as e:
            logger.error(f"Failed to answer callback: {e}")
            return False

    async def edit_decision_message(
        self, chat_id, message_id: int, decision_text: str
    ) -> bool:
        """Replace the inline keyboard approval message with a decision record.

        Removes the buttons and shows the outcome so it's visible in chat history.
        """
        try:
            result = await self._async_send("editMessageText", {
                "chat_id": chat_id,
                "message_id": message_id,
                "text": decision_text,
                "parse_mode": "Markdown",
            })
            return result.get("ok", False)
        except Exception as e:
            logger.error(f"Failed to edit egress decision message: {e}")
            return False

    def cleanup_expired(self, max_age_seconds: int = 300) -> int:
        """Remove pending requests older than max_age_seconds. Returns count removed."""
        now = datetime.now(timezone.utc)
        expired = []
        for rid, info in self.pending_requests.items():
            ts = datetime.fromisoformat(info["timestamp"])
            if (now - ts).total_seconds() > max_age_seconds:
                expired.append(rid)
        for rid in expired:
            del self.pending_requests[rid]
        return len(expired)

    def get_pending_count(self) -> int:
        return len(self.pending_requests)
