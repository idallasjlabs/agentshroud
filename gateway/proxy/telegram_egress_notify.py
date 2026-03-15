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
    """Sends Telegram inline keyboard notifications for egress approval."""

    def __init__(self, bot_token: str, owner_chat_id: str,
                 base_url: str = "https://api.telegram.org",
                 timeout_seconds: int = 30):
        self.bot_token = bot_token
        self.owner_chat_id = owner_chat_id
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
        """Send Telegram message with inline approve/deny buttons.

        Returns True if message was sent successfully.
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
            "inline_keyboard": [[
                {"text": "✅ Allow Always", "callback_data": f"egress_allow_always_{request_id}"},
                {"text": "✅ Allow Once", "callback_data": f"egress_allow_once_{request_id}"},
                {"text": "❌ Deny", "callback_data": f"egress_deny_{request_id}"},
            ]]
        }

        payload = {
            "chat_id": self.owner_chat_id,
            "text": text,
            "parse_mode": "Markdown",
            "reply_markup": keyboard,
        }

        self.pending_requests[request_id] = {
            "domain": domain,
            "port": port,
            "risk_level": risk_level,
            "agent_id": agent_id,
            "tool_name": tool_name,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        try:
            result = await self._async_send("sendMessage", payload)
            return result.get("ok", False)
        except Exception as e:
            logger.error(f"Failed to send egress notification: {e}")
            return False

    async def handle_callback(self, callback_data: str) -> dict:
        """Process inline button callback. Returns action result."""
        parts = callback_data.split("_", 3)
        if len(parts) < 3 or parts[0] != "egress":
            return {"status": "error", "reason": "invalid_format"}

        # Parse: egress_allow_always_{id}, egress_allow_once_{id}, egress_deny_{id}
        if callback_data.startswith("egress_allow_always_"):
            action = "allow_always"
            request_id = callback_data[len("egress_allow_always_"):]
        elif callback_data.startswith("egress_allow_once_"):
            action = "allow_once"
            request_id = callback_data[len("egress_allow_once_"):]
        elif callback_data.startswith("egress_deny_"):
            action = "deny"
            request_id = callback_data[len("egress_deny_"):]
        else:
            return {"status": "error", "reason": "invalid_format"}

        if request_id not in self.pending_requests:
            return {"status": "error", "reason": "request_not_found"}

        request_info = self.pending_requests.pop(request_id)
        return {
            "status": "ok",
            "action": action,
            "request_id": request_id,
            "domain": request_info["domain"],
            "port": request_info["port"],
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
