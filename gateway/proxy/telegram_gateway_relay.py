# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""
Telegram Gateway Relay — send Telegram messages from API-invoked sessions
via the gateway control plane.

Problem: When Hermes is invoked via the API (not Telegram), the container
cannot send Telegram messages because:
  1. Container lacks DNS for api.telegram.org
  2. Egress proxy blocks CONNECT to Telegram
  3. Bot token is not in container env vars

Solution: Route Telegram sends through the gateway's internal API
(http://gateway:8080/telegram/send), which has access to the bot token
and can reach api.telegram.org directly.

Usage:
    relay = TelegramGatewayRelay()
    await relay.send_message(chat_id="8096968754", text="Status update")
"""

import json
import logging
import os
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger("agentshroud.proxy.telegram_gateway_relay")


@dataclass
class TelegramSendResult:
    """Result of a Telegram send operation via gateway."""

    success: bool
    message_id: Optional[int] = None
    error: Optional[str] = None
    chat_id: Optional[str] = None


class TelegramGatewayRelay:
    """Relay Telegram messages through the gateway control plane.

    This enables containers without direct Telegram access to send
    messages by routing through the gateway's internal API endpoint.
    """

    def __init__(
        self,
        gateway_url: str | None = None,
        auth_token: str | None = None,
    ):
        self.gateway_url = gateway_url or os.environ.get("GATEWAY_BASE_URL", "http://gateway:8080")
        self.auth_token = auth_token or os.environ.get("GATEWAY_AUTH_TOKEN", "")

    def send_message(
        self,
        chat_id: str,
        text: str,
        parse_mode: str = "Markdown",
        bot_name: str | None = None,
    ) -> TelegramSendResult:
        """Send a Telegram message via the gateway relay.

        Args:
            chat_id: Telegram chat ID to send to
            text: Message text
            parse_mode: Telegram parse mode (Markdown, HTML, MarkdownV2)
            bot_name: Optional bot name (defaults to the requesting bot)

        Returns:
            TelegramSendResult with success status and message_id
        """
        if not self.auth_token:
            return TelegramSendResult(
                success=False,
                error="GATEWAY_AUTH_TOKEN not set — cannot relay to gateway",
                chat_id=chat_id,
            )

        url = f"{self.gateway_url}/telegram/send"
        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": parse_mode,
        }
        if bot_name:
            payload["bot_name"] = bot_name

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.auth_token}",
            "X-AgentShroud-System": "1",
        }

        body = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=body, headers=headers, method="POST")

        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode())
                return TelegramSendResult(
                    success=True,
                    message_id=data.get("message_id"),
                    chat_id=chat_id,
                )
        except urllib.error.HTTPError as exc:
            error_body = exc.read().decode("utf-8", errors="replace")
            logger.error("Telegram relay failed: HTTP %d — %s", exc.code, error_body[:200])
            return TelegramSendResult(
                success=False,
                error=f"HTTP {exc.code}: {error_body[:200]}",
                chat_id=chat_id,
            )
        except Exception as exc:
            logger.error("Telegram relay error: %s", exc)
            return TelegramSendResult(
                success=False,
                error=str(exc),
                chat_id=chat_id,
            )

    def send_status_update(
        self,
        chat_id: str,
        title: str,
        body: str,
        bot_name: str | None = None,
    ) -> TelegramSendResult:
        """Send a formatted status update via Telegram.

        Formats the message with a bold title and body text.
        """
        text = f"**{title}**\n\n{body}"
        return self.send_message(
            chat_id=chat_id,
            text=text,
            parse_mode="Markdown",
            bot_name=bot_name,
        )
