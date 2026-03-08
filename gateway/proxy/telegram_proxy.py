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
import os
import time
import urllib.request
import urllib.error
import ssl
from typing import Any, Optional

logger = logging.getLogger("agentshroud.proxy.telegram_api")

TELEGRAM_API_BASE = "https://api.telegram.org"

# Slash-commands that are forbidden for collaborators (owner-only capabilities)
_COLLABORATOR_BLOCKED_COMMANDS = {
    "/skill", "/1password", "/op", "/exec", "/run", "/cron",
    "/ssh", "/admin", "/config", "/secret", "/key", "/token",
    "/memory", "/reset", "/kill", "/restart", "/update",
}

_DISCLOSURE_MESSAGE = (
    "\U0001f6e1\ufe0f *AgentShroud Notice*\n\n"
    "This conversation is logged and may be reviewed as part of the AgentShroud\u2122 "
    "project\\. By continuing, you acknowledge this\\. Questions? Reach out to Isaiah directly\\.\n\n"
    "_Bot commands like /skill aren't available in collaborator mode\\. "
    "I'm the collaborator\\-facing assistant with read\\-only access \u2014 I can discuss "
    "AgentShroud's features, security concepts, and provide technical advice, but I don't "
    "have access to the full command set\\._"
)


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
        self._bot_token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
        self._ssl_context = ssl.create_default_context()

        # Track which collaborator user IDs have already received the disclosure notice
        # this session. Persisted in-memory only — resets on gateway restart (acceptable).
        self._disclosure_sent: set[str] = set()

        # Cache RBAC config to avoid re-instantiating on every message
        try:
            from gateway.security.rbac_config import RBACConfig
            self._rbac = RBACConfig()
        except Exception:
            self._rbac = None

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
        """Filter outbound bot messages through the full security pipeline.
        
        Order: XML blocks -> Credentials -> PII sanitizer -> Outbound pipeline
        """
        try:
            if content_type and "json" in content_type:
                data = json.loads(body)
                text = data.get("text", "")
                if text and self.sanitizer:
                    # Step 1: XML leak filter
                    filtered, was_filtered = self.sanitizer.filter_xml_blocks(text)
                    if was_filtered:
                        data["text"] = filtered
                        self._stats["outbound_filtered"] += 1
                        logger.info("Outbound message: XML blocks stripped")

                    # Step 2: Credential blocking
                    blocked, was_blocked = await self.sanitizer.block_credentials(
                        data["text"], "telegram"
                    )
                    if was_blocked:
                        data["text"] = blocked
                        self._stats["outbound_filtered"] += 1
                        logger.warning("Outbound message: credentials blocked")

                    # Step 3: PII sanitization (PHONE_NUMBER, SSN, CREDIT_CARD, EMAIL)
                    sanitize_result = await self.sanitizer.sanitize(data["text"])
                    if sanitize_result.redactions:
                        data["text"] = sanitize_result.sanitized_content
                        self._stats["outbound_filtered"] += 1
                        logger.warning(
                            "Outbound message: PII redacted (%d entities: %s)",
                            len(sanitize_result.redactions),
                            sanitize_result.entity_types_found,
                        )

                # Step 4: Full outbound pipeline (OutboundInfoFilter, OutputCanary, etc.)
                if text and self.pipeline:
                    try:
                        chat_id = str(data.get("chat_id", ""))
                        pipeline_result = await self.pipeline.process_outbound(
                            data.get("text", text),
                            agent_id="telegram",
                            source="telegram_outbound",
                            user_trust_level=self._get_trust_level(chat_id),
                        )
                        if pipeline_result.blocked:
                            logger.warning(
                                "Outbound message BLOCKED by pipeline: %s",
                                pipeline_result.block_reason,
                            )
                            data["text"] = (
                                "🛡️ This response was blocked by the "
                                "security pipeline. Please contact the administrator."
                            )
                            self._stats["messages_blocked"] += 1
                        elif pipeline_result.sanitized_message != data.get("text", text):
                            data["text"] = pipeline_result.sanitized_message
                            self._stats["outbound_filtered"] += 1
                            logger.info("Outbound message: pipeline filtered")
                    except Exception as e:
                        logger.error("Outbound pipeline error: %s", e)
                        # Fail-closed for non-owner
                        owner_id = self._rbac.owner_user_id if self._rbac else None
                        chat_id = str(data.get("chat_id", ""))
                        if chat_id != owner_id:
                            data["text"] = (
                                "🛡️ Response held — security pipeline "
                                "error. Please try again."
                            )
                            self._stats["messages_blocked"] += 1

                return json.dumps(data).encode()
        except Exception as e:
            logger.error(f"Outbound filter error: {e}")
        return body

    def _get_trust_level(self, chat_id: str) -> str:
        """Determine trust level for a chat ID."""
        if not self._rbac:
            return "UNTRUSTED"
        if chat_id == self._rbac.owner_user_id:
            return "FULL"
        return "UNTRUSTED"

    async def _filter_inbound_updates(self, response_data: dict) -> dict:
        """Scan inbound messages from getUpdates for security threats."""
        updates = response_data.get("result", [])
        filtered_updates = []

        for update in updates:
            # Handle inline button callbacks for egress approve/deny
            callback_query = update.get("callback_query")
            if callback_query:
                cb_data = callback_query.get("data", "")
                if cb_data.startswith("egress_"):
                    try:
                        from gateway.ingest_api.state import app_state as _app_state
                        _notifier = getattr(_app_state, "egress_notifier", None)
                        if _notifier:
                            result = await _notifier.handle_callback(cb_data)
                            await _notifier.answer_callback(
                                callback_query.get("id", ""),
                                f"Egress {result.get('action', 'processed')}",
                            )
                            logger.info("Egress callback handled: %s", result)
                    except Exception as _ce:
                        logger.error("Egress callback error (non-fatal): %s", _ce)
                # Drop callback_query updates — they are not bot messages
                continue

            message = update.get("message", {}) or update.get("edited_message", {})
            if not message:
                filtered_updates.append(update)
                continue

            text = message.get("text", "") or message.get("caption", "")
            user_id = str(message.get("from", {}).get("id", "unknown"))
            chat_id = message.get("chat", {}).get("id")

            if not text:
                filtered_updates.append(update)
                continue

            self._stats["messages_scanned"] += 1

            # ── Role resolution ───────────────────────────────────────────────
            is_owner = self._rbac.is_owner(user_id) if self._rbac else False
            is_collaborator = (
                self._rbac and
                not is_owner and
                user_id in {str(uid) for uid in (self._rbac.collaborator_user_ids or [])}
            )

            # ── Gateway-level collaborator activity tracking ──────────────────
            # This is the authoritative tracking point — all messages (including
            # long-polling) flow through here. webhook_receiver only handles
            # push-mode webhooks which are not used in this deployment.
            if is_collaborator:
                try:
                    from gateway.ingest_api.state import app_state as _app_state
                    _tracker = getattr(_app_state, "collaborator_tracker", None)
                    if _tracker:
                        sender = message.get("from", {})
                        _username = sender.get("first_name") or (
                            f"@{sender['username']}" if sender.get("username") else "unknown"
                        )
                        _tracker.record_activity(
                            user_id=user_id,
                            username=_username,
                            message_preview=text[:80],
                            source="telegram",
                        )
                except Exception as _te:
                    logger.debug("Collaborator tracker error (non-fatal): %s", _te)

            # ── Disclosure notice — send once per session per collaborator ─────
            if is_collaborator and chat_id and user_id not in self._disclosure_sent:
                await self._send_disclosure(chat_id)
                self._disclosure_sent.add(user_id)

            # ── Collaborator command blocking ─────────────────────────────────
            # Block owner-only slash commands before they reach the bot.
            if is_collaborator and chat_id:
                cmd = text.strip().split()[0].lower() if text.strip() else ""
                # Strip bot @mention suffix (e.g. /skill@agentshroud_bot → /skill)
                cmd_base = cmd.split("@")[0]
                if cmd_base in _COLLABORATOR_BLOCKED_COMMANDS:
                    self._stats["messages_blocked"] += 1
                    logger.info(
                        "Collaborator %s attempted blocked command %r — rejecting",
                        user_id, cmd_base,
                    )
                    await self._notify_collaborator_command_blocked(chat_id, cmd_base)
                    # Drop the update — do not forward to bot
                    continue

            # ── Middleware pipeline (RBAC, context guard, multi-turn, etc.) ───
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
                        if is_owner:
                            # Owner messages are logged but never blocked by middleware
                            logger.info(
                                "Middleware would block owner message (%s) — allowing: %s",
                                user_id, result.reason,
                            )
                        else:
                            logger.warning(
                                "Telegram message from %s blocked by middleware: %s",
                                user_id, result.reason,
                            )
                            self._stats["messages_blocked"] += 1
                            if chat_id:
                                await self._notify_user_blocked(chat_id, result.reason)
                            if "message" in update:
                                update["message"]["text"] = f"[BLOCKED BY AGENTSHROUD: {result.reason}]"
                            elif "edited_message" in update:
                                update["edited_message"]["text"] = f"[BLOCKED BY AGENTSHROUD: {result.reason}]"
                            filtered_updates.append(update)
                            continue
                except Exception as e:
                    logger.error(f"Middleware error for telegram message: {e}")

            # ── Inbound security pipeline (PromptGuard, EncodingDetector, TrustManager) ──
            if self.pipeline and text:
                try:
                    pipeline_result = await self.pipeline.process_inbound(
                        message=text,
                        agent_id="telegram",
                        source="telegram",
                        metadata={
                            "webhook_source": "telegram",
                            "user_id": user_id,
                        },
                    )
                    if pipeline_result.blocked:
                        if is_owner:
                            logger.info(
                                "Pipeline would block owner message (%s) — allowing: %s",
                                user_id, pipeline_result.block_reason,
                            )
                        else:
                            logger.warning(
                                "Telegram message from %s blocked by pipeline: %s",
                                user_id, pipeline_result.block_reason,
                            )
                            self._stats["messages_blocked"] += 1
                            if chat_id:
                                await self._notify_user_blocked(chat_id, pipeline_result.block_reason)
                            if "message" in update:
                                update["message"]["text"] = f"[BLOCKED BY AGENTSHROUD: {pipeline_result.block_reason}]"
                            elif "edited_message" in update:
                                update["edited_message"]["text"] = f"[BLOCKED BY AGENTSHROUD: {pipeline_result.block_reason}]"
                            filtered_updates.append(update)
                            continue
                    # Use the sanitized version from the pipeline going forward
                    if pipeline_result.sanitized_message != text:
                        if "message" in update:
                            update["message"]["text"] = pipeline_result.sanitized_message
                        elif "edited_message" in update:
                            update["edited_message"]["text"] = pipeline_result.sanitized_message
                        text = pipeline_result.sanitized_message
                except Exception as e:
                    logger.error("Inbound pipeline error for telegram message: %s", e)
                    if not is_owner:
                        # Fail closed for non-owner messages
                        self._stats["messages_blocked"] += 1
                        if chat_id:
                            await self._notify_user_blocked(chat_id, "Security pipeline error")
                        if "message" in update:
                            update["message"]["text"] = "[BLOCKED BY AGENTSHROUD: pipeline error]"
                        elif "edited_message" in update:
                            update["edited_message"]["text"] = "[BLOCKED BY AGENTSHROUD: pipeline error]"
                        filtered_updates.append(update)
                        continue

            # ── PII sanitization ──────────────────────────────────────────────
            if self.sanitizer and text:
                try:
                    sanitize_result = await self.sanitizer.sanitize(text)
                    if sanitize_result.entity_types_found:
                        self._stats["messages_sanitized"] += 1
                        logger.info(
                            "Telegram message from %s: PII redacted: %s",
                            user_id, sanitize_result.entity_types_found,
                        )
                        if "message" in update:
                            update["message"]["text"] = sanitize_result.sanitized_content
                            update["message"]["_agentshroud_pii_redacted"] = True
                            update["message"]["_agentshroud_redactions"] = list(sanitize_result.entity_types_found)
                        elif "edited_message" in update:
                            update["edited_message"]["text"] = sanitize_result.sanitized_content
                            update["edited_message"]["_agentshroud_pii_redacted"] = True
                except Exception as e:
                    logger.error(f"PII sanitization error for telegram message: {e}")

            filtered_updates.append(update)

        response_data["result"] = filtered_updates
        return response_data

    async def _send_disclosure(self, chat_id: int) -> None:
        """Send the one-time collaborator disclosure notice."""
        try:
            if self._bot_token:
                url = f"{TELEGRAM_API_BASE}/bot{self._bot_token}/sendMessage"
                payload = {
                    "chat_id": chat_id,
                    "text": _DISCLOSURE_MESSAGE,
                    "parse_mode": "MarkdownV2",
                }
                req = urllib.request.Request(
                    url,
                    data=json.dumps(payload).encode(),
                    headers={"Content-Type": "application/json"},
                )
                loop = asyncio.get_event_loop()
                await loop.run_in_executor(
                    None,
                    lambda: urllib.request.urlopen(req, timeout=5, context=self._ssl_context),
                )
                logger.info("Sent collaborator disclosure to chat %s", chat_id)
        except Exception as e:
            logger.warning("Failed to send disclosure to chat %s: %s", chat_id, e)

    async def _notify_collaborator_command_blocked(self, chat_id: int, command: str) -> None:
        """Notify a collaborator that a privileged command is not available."""
        try:
            if self._bot_token:
                msg = (
                    f"\U0001f512 `{command}` is not available in collaborator mode\\.\n\n"
                    "Privileged commands \\(1Password, exec, SSH, skills\\) are restricted "
                    "to the workspace owner\\. I can still help you with questions about "
                    "AgentShroud, security concepts, and technical advice\\."
                )
                url = f"{TELEGRAM_API_BASE}/bot{self._bot_token}/sendMessage"
                req = urllib.request.Request(
                    url,
                    data=json.dumps({"chat_id": chat_id, "text": msg, "parse_mode": "MarkdownV2"}).encode(),
                    headers={"Content-Type": "application/json"},
                )
                loop = asyncio.get_event_loop()
                await loop.run_in_executor(
                    None,
                    lambda: urllib.request.urlopen(req, timeout=5, context=self._ssl_context),
                )
        except Exception as e:
            logger.warning("Failed to send command-blocked notice to chat %s: %s", chat_id, e)


    @staticmethod
    def _sanitize_reason(reason: str) -> str:
        """Strip internal module names, file paths, and class references from reason text."""
        sanitized = reason
        # Remove Python module paths (e.g. gateway.security.foo_bar)
        sanitized = re.sub(r'[a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*){2,}', '[internal]', sanitized)
        # Remove file paths (e.g. /app/gateway/... or /home/...)
        sanitized = re.sub(r'/[a-zA-Z0-9_./-]{3,}\.(?:py|yaml|yml|json|toml|cfg)', '[path]', sanitized)
        # Remove class::method references
        sanitized = re.sub(r'[A-Z][a-zA-Z0-9]+::[a-zA-Z_]\w+', '[internal]', sanitized)
        # Remove traceback-style references  
        sanitized = re.sub(r'File "[^"]+",\s*line \d+', '[internal]', sanitized)
        # Collapse multiple [internal] markers
        sanitized = re.sub(r'(\[internal\]\s*)+', '[internal] ', sanitized).strip()
        return sanitized

    async def _notify_user_blocked(self, chat_id: int, reason: str):
        """Send a user-friendly notification when a message is blocked."""
        try:
            friendly_reasons = {
                "gitguard": "Your message contained patterns resembling code or script injection.",
                "promptguard": "Your message was flagged as a potential prompt injection attempt.",
                "prompt injection": "Your message was flagged as a potential prompt injection attempt.",
                "browsersecurity": "Your message contained a potentially unsafe browser payload.",
                "rbac": "You don\'t have permission to perform this action.",
                "contextguard": "Your message was flagged for context manipulation.",
                "filesandbox": "Your message referenced a restricted file path.",
            }
            user_msg = "Your message was blocked by a security filter."
            reason_lower = reason.lower()
            for key, friendly in friendly_reasons.items():
                if key in reason_lower:
                    user_msg = friendly
                    break

            notice = (
                "\u26a0\ufe0f *Message Blocked*\n\n"
                f"{user_msg}\n\n"
                f"_Reason: {self._sanitize_reason(reason)}_\n\n"
                "If this is an error, contact the system owner."
            )
            if self._bot_token:
                url = f"https://api.telegram.org/bot{self._bot_token}/sendMessage"
                req = urllib.request.Request(
                    url,
                    data=json.dumps({"chat_id": chat_id, "text": notice, "parse_mode": "Markdown"}).encode(),
                    headers={"Content-Type": "application/json"},
                )
                loop = asyncio.get_event_loop()
                await loop.run_in_executor(
                    None,
                    lambda: urllib.request.urlopen(req, timeout=5, context=self._ssl_context),
                )
                logger.info(f"Sent block notification to chat {chat_id}")
        except Exception as e:
            logger.error(f"Failed to send block notification to {chat_id}: {e}")

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
