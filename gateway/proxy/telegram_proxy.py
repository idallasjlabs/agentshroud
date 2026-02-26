# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
"""
Telegram API Reverse Proxy — intercepts all bot ↔ Telegram traffic.

The gateway acts as a man-in-the-middle for Telegram Bot API calls:
- Inbound: Messages from users are scanned (PII detection, injection defense)
- Outbound: Bot responses are filtered (credential blocking, XML stripping)

The bot connects to http://gateway:8080/telegram-api/bot<token>/<method>
instead of https://api.telegram.org/bot<token>/<method>.
"""
from __future__ import annotations

import asyncio
import json
import logging
import re
import time
import urllib.request
import urllib.error
import ssl
from typing import Any, Optional

logger = logging.getLogger("agentshroud.proxy.telegram_api")

TELEGRAM_API_BASE = "https://api.telegram.org"


class TelegramAPIProxy:
    """Proxies Telegram Bot API calls through the security pipeline."""

    def __init__(self, pipeline=None, middleware_manager=None, sanitizer=None):
        self.pipeline = pipeline
        self.middleware_manager = middleware_manager
        self.sanitizer = sanitizer
        self._stats = {
            "total_requests": 0,
            "messages_scanned": 0,
            "messages_sanitized": 0,
            "messages_blocked": 0,
            "outbound_filtered": 0,
        }
        self._ssl_context = ssl.create_default_context()

    def get_stats(self) -> dict:
        return dict(self._stats)

    async def proxy_request(
        self,
        bot_token: str,
        method: str,
        body: Optional[bytes] = None,
        content_type: Optional[str] = None,
    ) -> dict:
        """Proxy a single Telegram API request.
        
        For getUpdates responses: scan each message through security pipeline.
        For sendMessage requests: scan outbound content.
        """
        self._stats["total_requests"] += 1
        url = f"{TELEGRAM_API_BASE}/bot{bot_token}/{method}"

        # === OUTBOUND FILTERING (bot → Telegram) ===
        # For sendMessage, editMessageText, etc. — scan the bot's outgoing text
        if method in ("sendMessage", "editMessageText", "sendPhoto", "sendDocument",
                       "copyMessage", "forwardMessage") and body:
            body = await self._filter_outbound(body, content_type)

        # Forward to real Telegram API
        try:
            response_data = await self._forward_to_telegram(url, body, content_type)
        except Exception as e:
            logger.error(f"Telegram API proxy error for {method}: {e}")
            return {"ok": False, "error_code": 502, "description": str(e)}

        # === INBOUND FILTERING (Telegram → bot) ===
        # For getUpdates: scan each message in the response
        if method == "getUpdates" and response_data.get("ok"):
            response_data = await self._filter_inbound_updates(response_data)

        return response_data

    async def _filter_outbound(self, body: bytes, content_type: Optional[str]) -> bytes:
        """Filter outbound bot messages (sendMessage, etc.)."""
        try:
            if content_type and "json" in content_type:
                data = json.loads(body)
                text = data.get("text", "")
                if text and self.sanitizer:
                    # XML leak filter
                    filtered, was_filtered = self.sanitizer.filter_xml_blocks(text)
                    if was_filtered:
                        data["text"] = filtered
                        self._stats["outbound_filtered"] += 1
                        logger.info("Outbound message: XML blocks stripped")

                    # Credential blocking
                    blocked, was_blocked = await self.sanitizer.block_credentials(
                        data["text"], "telegram"
                    )
                    if was_blocked:
                        data["text"] = blocked
                        self._stats["outbound_filtered"] += 1
                        logger.warning("Outbound message: credentials blocked")

                    return json.dumps(data).encode()
        except Exception as e:
            logger.error(f"Outbound filter error: {e}")
        return body

    async def _filter_inbound_updates(self, response_data: dict) -> dict:
        """Scan inbound messages from getUpdates for security threats."""
        updates = response_data.get("result", [])
        filtered_updates = []

        for update in updates:
            message = update.get("message", {}) or update.get("edited_message", {})
            if not message:
                filtered_updates.append(update)
                continue

            text = message.get("text", "") or message.get("caption", "")
            user_id = str(message.get("from", {}).get("id", "unknown"))

            if not text:
                filtered_updates.append(update)
                continue

            self._stats["messages_scanned"] += 1

            # Run through middleware (RBAC, context guard, multi-turn tracking, etc.)
            if self.middleware_manager:
                try:
                    request_data = {
                        "message": text,
                        "content_type": "text",
                        "source": "telegram",
                        "headers": {},
                        "user_id": user_id,
                    }
                    result = await self.middleware_manager.process_request(
                        request_data, f"telegram_{user_id}"
                    )
                    if not result.allowed:
                        logger.warning(
                            f"Telegram message from {user_id} blocked by middleware: {result.reason}"
                        )
                        self._stats["messages_blocked"] += 1
                        # Replace message text with block notice
                        if "message" in update:
                            update["message"]["text"] = f"[BLOCKED BY AGENTSHROUD: {result.reason}]"
                        elif "edited_message" in update:
                            update["edited_message"]["text"] = f"[BLOCKED BY AGENTSHROUD: {result.reason}]"
                        filtered_updates.append(update)
                        continue
                except Exception as e:
                    logger.error(f"Middleware error for telegram message: {e}")

            # PII sanitization on inbound messages
            if self.sanitizer and text:
                try:
                    result = await self.sanitizer.sanitize(text)
                    if result.entity_types_found:
                        self._stats["messages_sanitized"] += 1
                        logger.info(
                            f"Telegram message from {user_id}: PII detected and redacted: "
                            f"{result.entity_types_found}"
                        )
                        # Replace text with sanitized version
                        if "message" in update:
                            update["message"]["text"] = result.sanitized_content
                            update["message"]["_agentshroud_pii_redacted"] = True
                            update["message"]["_agentshroud_redactions"] = list(result.entity_types_found)
                        elif "edited_message" in update:
                            update["edited_message"]["text"] = result.sanitized_content
                            update["edited_message"]["_agentshroud_pii_redacted"] = True
                except Exception as e:
                    logger.error(f"PII sanitization error for telegram message: {e}")

            filtered_updates.append(update)

        response_data["result"] = filtered_updates
        return response_data

    async def _forward_to_telegram(
        self, url: str, body: Optional[bytes], content_type: Optional[str]
    ) -> dict:
        """Forward request to real Telegram API and return parsed response."""
        headers = {}
        if content_type:
            headers["Content-Type"] = content_type

        req = urllib.request.Request(url, data=body, headers=headers)

        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda: urllib.request.urlopen(req, timeout=60, context=self._ssl_context),
        )
        response_body = response.read()
        return json.loads(response_body)
