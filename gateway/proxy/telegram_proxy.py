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
import ipaddress
import json
import logging
import re
import os
import time
import uuid
import urllib.request
import urllib.error
import urllib.parse
import ssl
from typing import Any, Optional
from urllib.parse import urlparse

from gateway.security.input_normalizer import normalize_input, strip_markdown_exfil

logger = logging.getLogger("agentshroud.proxy.telegram_api")

TELEGRAM_API_BASE = "https://api.telegram.org"
_SUPPRESS_OUTBOUND_TOKEN = "__AGENTSHROUD_SUPPRESS_OUTBOUND__"

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
        self._max_outbound_chars = int(os.environ.get("AGENTSHROUD_MAX_OUTBOUND_CHARS", "3800"))
        self._block_cascade_seconds = float(os.environ.get("AGENTSHROUD_BLOCK_CASCADE_SECONDS", "4.0"))
        self._recent_outbound_blocks_until: dict[str, float] = {}
        self._system_notice_cooldown_seconds = float(
            os.environ.get("AGENTSHROUD_SYSTEM_NOTICE_COOLDOWN_SECONDS", "120.0")
        )
        self._recent_system_notice_until: dict[tuple[str, str], float] = {}
        self._web_fetch_approval_cooldown_seconds = float(
            os.environ.get("AGENTSHROUD_WEB_FETCH_APPROVAL_COOLDOWN_SECONDS", "20.0")
        )
        self._recent_web_fetch_approval_until: dict[tuple[str, str], float] = {}
        self._no_reply_notice_cooldown_seconds = float(
            os.environ.get("AGENTSHROUD_NO_REPLY_NOTICE_COOLDOWN_SECONDS", "15.0")
        )
        self._recent_no_reply_notice_until: dict[str, float] = {}

        # Track which collaborator user IDs have already received the disclosure notice
        # this session. Persisted in-memory only — resets on gateway restart (acceptable).
        self._disclosure_sent: set[str] = set()

        # Cache RBAC config to avoid re-instantiating on every message
        try:
            from gateway.security.rbac_config import RBACConfig
            self._rbac = RBACConfig()
        except Exception:
            self._rbac = None

        # Per-user collaborator rate limiter: 200 messages per hour
        from gateway.ingest_api.auth import RateLimiter
        self._collaborator_rate_limiter = RateLimiter(max_requests=200, window_seconds=3600)

    def _is_owner_chat(self, chat_id: str) -> bool:
        """Return True when chat_id belongs to the configured owner."""
        if not self._rbac:
            return False
        return str(chat_id) == str(getattr(self._rbac, "owner_user_id", ""))

    def _set_outbound_block_cascade(self, chat_id: str) -> None:
        """Set short per-chat block window to prevent fragment leak-through."""
        if chat_id:
            self._recent_outbound_blocks_until[chat_id] = time.time() + self._block_cascade_seconds

    def get_stats(self) -> dict:
        return dict(self._stats)

    @staticmethod
    def _sanitize_reason(reason: str) -> str:
        """Strip internal paths and module names from block reasons before user display."""
        # Remove Python module paths (gateway.security.module_name patterns)
        sanitized = re.sub(r'gateway\.[a-z_.]+', '[internal]', reason)
        # Remove absolute file paths (/app/..., /home/..., /usr/...)
        sanitized = re.sub(r'/[a-z][a-zA-Z0-9/_.-]+\.py(?:\s+line\s+\d+)?', '', sanitized)
        return sanitized.strip()

    @staticmethod
    def _strip_json_fence(text: str) -> str:
        """Strip optional markdown json fences around model output."""
        candidate = normalize_input(text or "").strip()
        if candidate.startswith("```"):
            candidate = re.sub(r"^```(?:json)?\s*", "", candidate, flags=re.IGNORECASE)
            candidate = re.sub(r"\s*```$", "", candidate)
        return candidate.strip()

    @classmethod
    def _parse_tool_call_json(cls, text: str) -> Optional[dict[str, Any]]:
        """Parse leaked model tool-call JSON blobs (e.g. {'name': 'NO_REPLY', ...})."""
        candidate = cls._strip_json_fence(text)
        if not candidate.startswith("{") or not candidate.endswith("}"):
            return None
        try:
            parsed = json.loads(candidate)
        except Exception:
            return None
        if not isinstance(parsed, dict):
            return None
        name = parsed.get("name")
        arguments = parsed.get("arguments")
        if isinstance(name, str) and isinstance(arguments, (dict, list, str, int, float, bool, type(None))):
            return parsed
        return None

    @classmethod
    def _extract_embedded_tool_call_json(
        cls, text: str
    ) -> Optional[tuple[dict[str, Any], int, int]]:
        """Find first embedded tool-call JSON object inside arbitrary text."""
        source = text or ""
        decoder = json.JSONDecoder()
        i = 0
        while i < len(source):
            start = source.find("{", i)
            if start < 0:
                return None
            try:
                parsed, end = decoder.raw_decode(source, start)
            except Exception:
                i = start + 1
                continue
            if isinstance(parsed, dict):
                name = parsed.get("name")
                if isinstance(name, str) and "arguments" in parsed:
                    return parsed, start, end
            i = end if end > start else start + 1
        return None

    @staticmethod
    def _extract_first_egress_target(text: str) -> Optional[str]:
        """Extract first outbound web target (URL or bare domain) for egress preflight."""
        if not text:
            return None
        url_match = re.search(r"https?://[^\s<>()\"']+", text, flags=re.IGNORECASE)
        if url_match:
            url = url_match.group(0).rstrip(".,;:!?)]}>'\"")
            return url or None

        # Support bare domains like "weather.com/today" so collaborator requests
        # still trigger interactive egress approval before model/tool execution.
        domain_match = re.search(
            r"(?<!@)\b(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}(?![a-z0-9_-])(?:/[^\s<>()\"']*)?",
            text,
            flags=re.IGNORECASE,
        )
        if not domain_match:
            return None
        candidate = domain_match.group(0).rstrip(".,;:!?)]}>'\"")
        if not candidate:
            return None
        return f"https://{candidate}"

    @staticmethod
    def _is_valid_domain_name(domain: str) -> bool:
        """Validate normalized domain labels to avoid malformed allowlist entries."""
        raw = (domain or "").strip().lower()
        if not raw:
            return False
        if ".." in raw:
            return False
        labels = raw.split(".")
        if len(labels) < 2:
            return False
        for label in labels:
            if not label:
                return False
            if len(label) > 63:
                return False
            if label.startswith("-") or label.endswith("-"):
                return False
            if not re.fullmatch(r"[a-z0-9-]+", label):
                return False
        return True

    @staticmethod
    def _resolve_text_field(data: dict[str, Any]) -> tuple[str, str]:
        """Return (field_name, text_value) for Telegram-style outbound payloads."""
        for key in ("text", "draft", "message", "content", "caption"):
            value = data.get(key)
            if isinstance(value, str):
                return key, value
        return "text", ""

    async def proxy_request(
        self,
        bot_token: str,
        method: str,
        body: Optional[bytes] = None,
        content_type: Optional[str] = None,
        is_system: bool = False,
        path_prefix: str = "",
    ) -> dict:
        """Proxy a single Telegram API request.

        For getUpdates responses: scan each message through security pipeline.
        For sendMessage requests: scan outbound content.
        is_system=True skips outbound filtering for system/admin notifications
        (startup, shutdown) that are not LLM-generated output.
        path_prefix: set to "file/" for Telegram file download requests so the
        upstream URL is constructed as https://api.telegram.org/file/bot<token>/<path>.
        """
        self._stats["total_requests"] += 1
        url = f"{TELEGRAM_API_BASE}/{path_prefix}bot{bot_token}/{method}"

        # === OUTBOUND FILTERING (bot → Telegram) ===
        # For sendMessage, editMessageText, etc. — scan the bot's outgoing text.
        # Skip for system notifications (X-AgentShroud-System: 1) — these are
        # shell-script admin messages, not LLM output, so content filtering is not needed.
        #
        # Draft methods are suppressed to prevent transient raw tool-call JSON flicker in
        # Telegram clients before final message sanitization.
        if not is_system and method in ("sendMessageDraft", "editMessageDraft"):
            return {"ok": True, "result": {"suppressed": True, "method": method}}
        if method in ("sendMessage", "editMessageText") and body:
            if self._suppress_duplicate_system_notice(body, content_type):
                return {"ok": True, "result": {"suppressed": True, "method": method}}

        if not is_system and method in (
            "sendMessage",
            "editMessageText",
            "sendPhoto",
            "sendDocument",
            "copyMessage",
            "forwardMessage",
        ) and body:
            body = await self._filter_outbound(body, content_type)
            if self._is_suppressed_outbound_payload(body, content_type):
                return {"ok": True, "result": {"suppressed": True, "method": method}}

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
            ct = (content_type or "").lower()
            if "multipart" in ct:
                # For multipart/form-data (sendPhoto, sendDocument with caption):
                # apply XML leak filter using latin-1 for lossless binary round-trip.
                # latin-1 is bijective over 0x00-0xFF so binary image parts are
                # preserved byte-for-byte while XML patterns in text fields are stripped.
                if self.sanitizer:
                    body_str = body.decode("latin-1")
                    filtered, was_filtered = self.sanitizer.filter_xml_blocks(body_str)
                    if was_filtered:
                        body = filtered.encode("latin-1")
                        self._stats["outbound_filtered"] += 1
                        logger.info("Outbound multipart: XML blocks stripped")
                return body
            elif "json" in ct or (not ct and body.lstrip().startswith(b"{")):
                data = json.loads(body)
                text_key, text = self._resolve_text_field(data)
                chat_id = str(data.get("chat_id", ""))
                is_owner_chat = self._is_owner_chat(chat_id)

                # Guardrail: never leak raw tool-call JSON blobs to Telegram users.
                parsed_tool_call = self._parse_tool_call_json(text) if isinstance(text, str) else None
                embedded_tool_call = (
                    self._extract_embedded_tool_call_json(text) if isinstance(text, str) else None
                )
                if parsed_tool_call is None and embedded_tool_call is not None:
                    parsed_tool_call, emb_start, emb_end = embedded_tool_call
                    leading = text[:emb_start].strip()
                    trailing = text[emb_end:].strip()
                    cleaned = " ".join(part for part in (leading, trailing) if part).strip()
                    if cleaned:
                        tool_name = str(parsed_tool_call.get("name", "")).strip()
                        tool_args = parsed_tool_call.get("arguments") if isinstance(parsed_tool_call.get("arguments"), dict) else {}
                        if tool_name == "web_fetch":
                            approval_queued = await self._trigger_web_fetch_approval(chat_id, tool_args)
                            if approval_queued:
                                cleaned = (
                                    f"{cleaned}\n\n"
                                    "🌐 Web access request detected. Approval request queued for this destination."
                                ).strip()
                        data[text_key] = cleaned
                        self._stats["outbound_filtered"] += 1
                        return json.dumps(data).encode()
                if parsed_tool_call is not None:
                    tool_name = str(parsed_tool_call.get("name", "")).strip()
                    tool_args = parsed_tool_call.get("arguments") if isinstance(parsed_tool_call.get("arguments"), dict) else {}
                    self._stats["outbound_filtered"] += 1
                    if tool_name.upper() == "NO_REPLY":
                        now = time.time()
                        blocked_until = self._recent_no_reply_notice_until.get(chat_id, 0.0) if chat_id else 0.0
                        if chat_id and blocked_until > now:
                            data[text_key] = _SUPPRESS_OUTBOUND_TOKEN
                        else:
                            data[text_key] = "⏳ Agent is still processing a previous request. Please wait 10–20 seconds and retry."
                            if chat_id:
                                self._recent_no_reply_notice_until[chat_id] = (
                                    now + self._no_reply_notice_cooldown_seconds
                                )
                    elif tool_name == "sessions_spawn" and str(tool_args.get("agentId", "")) == "acp.healthcheck":
                        data[text_key] = "✅ Healthcheck started. I’ll reply with status once complete."
                    elif tool_name == "web_fetch":
                        approval_queued = await self._trigger_web_fetch_approval(chat_id, tool_args)
                        approval_note = (
                            " Approval request queued for this destination."
                            if approval_queued else
                            ""
                        )
                        data[text_key] = (
                            "🌐 Web fetch requested, but this model returned raw tool JSON instead of executing it. "
                            "Switch to a tool-capable model (e.g., scripts/switch_model.sh gemini or local qwen3:14b once pulled)."
                            + approval_note
                        )
                    elif tool_name in {"sessions_spawn", "sessions_send", "subagents"}:
                        data[text_key] = "✅ Request accepted and queued."
                    else:
                        self._quarantine_outbound_block(
                            chat_id=chat_id,
                            text=text or "",
                            reason=f"Raw tool-call JSON leaked to outbound text (tool={tool_name or 'unknown'})",
                            source="telegram_outbound_toolcall_json",
                        )
                        data[text_key] = "[AgentShroud: internal tool-call output suppressed]"
                    return json.dumps(data).encode()

                if isinstance(text, str) and "session file locked" in text.lower():
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = "⏳ Agent is still processing a previous request. Please wait 10–20 seconds and retry."
                    return json.dumps(data).encode()
                if isinstance(text, str) and "does not support tools" in text.lower():
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = "⚠️ Current local model does not support tool calls. Use scripts/switch_model.sh local qwen3:14b (or a tools-capable model)."
                    return json.dumps(data).encode()
                if isinstance(text, str) and "ollama requires authentication" in text.lower():
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = (
                        "⚠️ Ollama provider is not configured in this session. Set OLLAMA_API_KEY=ollama-local and restart, "
                        "or run scripts/switch_model.sh cloud gemini."
                    )
                    return json.dumps(data).encode()
                if isinstance(text, str) and "unknown model:" in text.lower():
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = (
                        "⚠️ Selected model is not registered. Use scripts/switch_model.sh to pick a configured model "
                        "(local qwen3:14b or cloud gemini/openai)."
                    )
                    return json.dumps(data).encode()

                if text:
                    normalized_text = normalize_input(text)
                    scrubbed_text = strip_markdown_exfil(normalized_text)
                    if scrubbed_text != text:
                        data["text"] = scrubbed_text
                        text = scrubbed_text
                        self._stats["outbound_filtered"] += 1

                # Prevent Telegram HTML parse errors caused by redaction placeholders
                # like <EMAIL_ADDRESS> / <PHONE_NUMBER> in sanitized output.
                parse_mode = str(data.get("parse_mode", "")).upper()
                if parse_mode == "HTML" and isinstance(data.get(text_key), str):
                    if re.search(r"<[A-Z][A-Z0-9_]{1,64}>", data[text_key]):
                        data.pop("parse_mode", None)
                        self._stats["outbound_filtered"] += 1

                if chat_id:
                    blocked_until = self._recent_outbound_blocks_until.get(chat_id, 0.0)
                    if blocked_until > time.time() and not is_owner_chat:
                        self._quarantine_outbound_block(
                            chat_id=chat_id,
                            text=text or "",
                            reason="Outbound block cascade active",
                            source="telegram_outbound_cascade",
                        )
                        data["text"] = "[AgentShroud: outbound content blocked by security policy]"
                        self._stats["outbound_filtered"] += 1
                        return json.dumps(data).encode()

                if (
                    text
                    and chat_id
                    and not is_owner_chat
                    and len(text) > self._max_outbound_chars
                ):
                    self._quarantine_outbound_block(
                        chat_id=chat_id,
                        text=text or "",
                        reason=f"Outbound text exceeds max length ({len(text)} chars)",
                        source="telegram_outbound_overlength",
                    )
                    data["text"] = "[AgentShroud: outbound content blocked by security policy]"
                    self._stats["outbound_filtered"] += 1
                    self._set_outbound_block_cascade(chat_id)
                    logger.warning(
                        "Outbound over-length message blocked for chat %s (%d chars)",
                        chat_id,
                        len(text),
                    )
                    return json.dumps(data).encode()

                if text and self.pipeline:
                    pipeline_result = await self.pipeline.process_outbound(
                        response=text,
                        source="telegram",
                        user_trust_level="FULL" if is_owner_chat else "UNTRUSTED",
                        metadata={"chat_id": chat_id},
                    )
                    if pipeline_result.blocked:
                        self._quarantine_outbound_block(
                            chat_id=chat_id,
                            text=text or "",
                            reason=pipeline_result.block_reason or "Pipeline blocked outbound response",
                            source="telegram_outbound_pipeline_block",
                        )
                        data["text"] = "[AgentShroud: outbound content blocked by security policy]"
                        self._stats["outbound_filtered"] += 1
                        self._set_outbound_block_cascade(chat_id)
                        logger.warning(
                            "Outbound message blocked by pipeline: %s", pipeline_result.block_reason
                        )
                    elif (
                        chat_id
                        and not is_owner_chat
                        and getattr(pipeline_result, "info_filter_redaction_count", 0) > 0
                    ):
                        self._quarantine_outbound_block(
                            chat_id=chat_id,
                            text=text or "",
                            reason=(
                                "Outbound info filter redacted protected content "
                                f"({getattr(pipeline_result, 'info_filter_redaction_count', 0)} redactions)"
                            ),
                            source="telegram_outbound_info_filter_block",
                        )
                        data["text"] = "[AgentShroud: outbound content blocked by security policy]"
                        self._stats["outbound_filtered"] += 1
                        self._set_outbound_block_cascade(chat_id)
                        logger.warning(
                            "Outbound message blocked after info-filter redactions "
                            "(chat=%s redactions=%s)",
                            chat_id,
                            getattr(pipeline_result, "info_filter_redaction_count", 0),
                        )
                    elif pipeline_result.sanitized_message != text:
                        data["text"] = pipeline_result.sanitized_message
                        self._stats["outbound_filtered"] += 1
                    return json.dumps(data).encode()
                elif text and self.sanitizer:
                    # Fallback: direct sanitizer calls when pipeline is unavailable
                    # 1. PII sanitization (phone numbers, SSNs, emails, etc.)
                    pii_result = await self.sanitizer.sanitize(data["text"])
                    if pii_result.entity_types_found:
                        data["text"] = pii_result.sanitized_content
                        self._stats["outbound_filtered"] += 1
                        logger.info("Outbound message: PII redacted: %s", pii_result.entity_types_found)
                    # 2. XML leak filter
                    filtered, was_filtered = self.sanitizer.filter_xml_blocks(data["text"])
                    if was_filtered:
                        data["text"] = filtered
                        self._stats["outbound_filtered"] += 1
                        logger.info("Outbound message: XML blocks stripped")
                    # 3. Credential blocking
                    blocked, was_blocked = await self.sanitizer.block_credentials(
                        data["text"], "telegram"
                    )
                    if was_blocked:
                        self._quarantine_outbound_block(
                            chat_id=chat_id,
                            text=text or "",
                            reason="Credential blocking triggered",
                            source="telegram_outbound_credential_block",
                        )
                        data["text"] = blocked
                        self._stats["outbound_filtered"] += 1
                        logger.warning("Outbound message: credentials blocked")
                    return json.dumps(data).encode()
            elif "x-www-form-urlencoded" in ct or (
                not ct
                and b"chat_id=" in body
                and any(
                    marker in body
                    for marker in (
                        b"text=",
                        b"draft=",
                        b"message=",
                        b"content=",
                        b"caption=",
                    )
                )
            ):
                # Telegram draft/edit calls may arrive as urlencoded form payloads.
                # Filter these the same way as JSON payloads to prevent transient leaks.
                parsed = urllib.parse.parse_qsl(
                    body.decode("utf-8", errors="replace"),
                    keep_blank_values=True,
                )
                data = dict(parsed)
                text_key, text = self._resolve_text_field(data)
                chat_id = str(data.get("chat_id", ""))

                parsed_tool_call = self._parse_tool_call_json(text) if isinstance(text, str) else None
                embedded_tool_call = (
                    self._extract_embedded_tool_call_json(text) if isinstance(text, str) else None
                )
                if parsed_tool_call is None and embedded_tool_call is not None:
                    parsed_tool_call, emb_start, emb_end = embedded_tool_call
                    leading = text[:emb_start].strip()
                    trailing = text[emb_end:].strip()
                    cleaned = " ".join(part for part in (leading, trailing) if part).strip()
                    if cleaned:
                        tool_name = str(parsed_tool_call.get("name", "")).strip()
                        tool_args = parsed_tool_call.get("arguments") if isinstance(parsed_tool_call.get("arguments"), dict) else {}
                        if tool_name == "web_fetch":
                            approval_queued = await self._trigger_web_fetch_approval(chat_id, tool_args)
                            if approval_queued:
                                cleaned = (
                                    f"{cleaned}\n\n"
                                    "🌐 Web access request detected. Approval request queued for this destination."
                                ).strip()
                        data[text_key] = cleaned
                        self._stats["outbound_filtered"] += 1
                        return urllib.parse.urlencode(data).encode()
                if parsed_tool_call is not None:
                    tool_name = str(parsed_tool_call.get("name", "")).strip()
                    tool_args = parsed_tool_call.get("arguments") if isinstance(parsed_tool_call.get("arguments"), dict) else {}
                    self._stats["outbound_filtered"] += 1
                    if tool_name.upper() == "NO_REPLY":
                        now = time.time()
                        blocked_until = self._recent_no_reply_notice_until.get(chat_id, 0.0) if chat_id else 0.0
                        if chat_id and blocked_until > now:
                            data[text_key] = _SUPPRESS_OUTBOUND_TOKEN
                        else:
                            data[text_key] = "⏳ Agent is still processing a previous request. Please wait 10–20 seconds and retry."
                            if chat_id:
                                self._recent_no_reply_notice_until[chat_id] = (
                                    now + self._no_reply_notice_cooldown_seconds
                                )
                    elif tool_name == "sessions_spawn" and str(tool_args.get("agentId", "")) == "acp.healthcheck":
                        data[text_key] = "✅ Healthcheck started. I’ll reply with status once complete."
                    elif tool_name == "web_fetch":
                        approval_queued = await self._trigger_web_fetch_approval(chat_id, tool_args)
                        approval_note = (
                            " Approval request queued for this destination."
                            if approval_queued else
                            ""
                        )
                        data[text_key] = (
                            "🌐 Web fetch requested, but this model returned raw tool JSON instead of executing it. "
                            "Switch to a tool-capable model (e.g., scripts/switch_model.sh gemini or local qwen3:14b once pulled)."
                            + approval_note
                        )
                    elif tool_name in {"sessions_spawn", "sessions_send", "subagents"}:
                        data[text_key] = "✅ Request accepted and queued."
                    else:
                        data[text_key] = "[AgentShroud: internal tool-call output suppressed]"
                    return urllib.parse.urlencode(data).encode()

                if isinstance(text, str) and "session file locked" in text.lower():
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = "⏳ Agent is still processing a previous request. Please wait 10–20 seconds and retry."
                    return urllib.parse.urlencode(data).encode()
                if isinstance(text, str) and "does not support tools" in text.lower():
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = "⚠️ Current local model does not support tool calls. Use scripts/switch_model.sh local qwen3:14b (or a tools-capable model)."
                    return urllib.parse.urlencode(data).encode()
                if isinstance(text, str) and "ollama requires authentication" in text.lower():
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = (
                        "⚠️ Ollama provider is not configured in this session. Set OLLAMA_API_KEY=ollama-local and restart, "
                        "or run scripts/switch_model.sh cloud gemini."
                    )
                    return urllib.parse.urlencode(data).encode()
                if isinstance(text, str) and "unknown model:" in text.lower():
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = (
                        "⚠️ Selected model is not registered. Use scripts/switch_model.sh to pick a configured model "
                        "(local qwen3:14b or cloud gemini/openai)."
                    )
                    return urllib.parse.urlencode(data).encode()
        except Exception as e:
            logger.error(f"Outbound filter error: {e}")
            # Fail-closed: if pipeline crashes, block non-owner outbound messages.
            # Determine if the destination is the owner by inspecting chat_id.
            try:
                data = json.loads(body)
                chat_id = str(data.get("chat_id", ""))
                owner_id = str(self._rbac.owner_user_id) if self._rbac else ""
                if owner_id and chat_id != owner_id:
                    self._quarantine_outbound_block(
                        chat_id=chat_id,
                        text=str(data.get("text", "")),
                        reason="Security pipeline error (fail-closed)",
                        source="telegram_outbound_fail_closed",
                    )
                    data["text"] = "[AgentShroud: security pipeline error — response blocked]"
                    return json.dumps(data).encode()
            except Exception:
                pass
        return body

    async def _trigger_web_fetch_approval(self, chat_id: str, tool_args: dict[str, Any]) -> bool:
        """Queue an interactive egress approval when raw web_fetch JSON leaks."""
        url = str((tool_args or {}).get("url", "")).strip().strip("'\"<>[]{}()")
        if not url:
            return False
        parsed = urlparse(url if "://" in url else f"https://{url}")
        raw_domain = (parsed.hostname or "").strip().lower()
        if ".." in raw_domain:
            return False
        domain = raw_domain.strip(".")
        if not domain:
            return False
        # Reject malformed hosts instead of silently rewriting them into a
        # potentially different allowlist destination.
        if re.search(r"[^a-z0-9.-]", domain):
            return False
        if not domain:
            return False
        if "." not in domain:
            return False
        if not self._is_valid_domain_name(domain):
            return False
        if domain in {"localhost", "local", "localdomain"}:
            return False
        try:
            # Never queue collaborator egress approvals for literal IP targets.
            # IP-based egress (esp. private/link-local) should remain blocked by
            # network policy rather than entering allowlist workflows.
            ipaddress.ip_address(domain)
            return False
        except ValueError:
            pass
        approval_key = ((chat_id or "unknown"), domain)
        now = time.time()
        blocked_until = self._recent_web_fetch_approval_until.get(approval_key, 0.0)
        if blocked_until > now:
            return False
        try:
            from gateway.ingest_api.state import app_state as _app_state
            _egress_filter = getattr(_app_state, "egress_filter", None)
            if _egress_filter is None or not hasattr(_egress_filter, "check_async"):
                return False
            _port = parsed.port or (443 if parsed.scheme != "http" else 80)
            _agent_id = f"telegram_web_fetch:{chat_id}" if chat_id else "telegram_web_fetch"
            asyncio.create_task(
                _egress_filter.check_async(
                    agent_id=_agent_id,
                    destination=f"{parsed.scheme or 'https'}://{domain}",
                    port=_port,
                    tool_name="web_fetch",
                )
            )
            self._recent_web_fetch_approval_until[approval_key] = (
                now + self._web_fetch_approval_cooldown_seconds
            )
            return True
        except Exception:
            return False

    def _suppress_duplicate_system_notice(self, body: bytes, content_type: Optional[str]) -> bool:
        """Suppress repeated startup/shutdown system notices in short windows."""
        def _canonical_notice(raw: str) -> str:
            text = (raw or "").strip()
            # Normalize emoji-variation and punctuation drift so duplicate startup
            # notices are suppressed even when renderers alter glyph variants.
            lowered = re.sub(r"[\ufe0f\u200d]", "", text).lower()
            lowered = re.sub(r"\s+", " ", lowered).strip()
            if "agentshroud" in lowered and "online" in lowered:
                return "agentshroud_online"
            if "agentshroud" in lowered and "shutting down" in lowered:
                return "agentshroud_shutting_down"
            return ""

        try:
            ct = (content_type or "").lower()
            payload: dict[str, Any] = {}
            if "json" in ct or (not ct and body.lstrip().startswith(b"{")):
                payload = json.loads(body)
            elif "x-www-form-urlencoded" in ct or (not ct and b"=" in body):
                payload = dict(
                    urllib.parse.parse_qsl(
                        body.decode("utf-8", errors="replace"), keep_blank_values=True
                    )
                )
            chat_id = str(payload.get("chat_id", "")).strip()
            _, text = self._resolve_text_field(payload)
            canonical_notice = _canonical_notice(text or "")
            if not chat_id or not canonical_notice:
                return False
            key = (chat_id, canonical_notice)
            now = time.time()
            blocked_until = self._recent_system_notice_until.get(key, 0.0)
            if blocked_until > now:
                logger.info(
                    "Suppressing duplicate system notice for chat %s: %s",
                    chat_id,
                    canonical_notice,
                )
                return True
            self._recent_system_notice_until[key] = now + self._system_notice_cooldown_seconds
        except Exception:
            return False
        return False

    @staticmethod
    def _is_suppressed_outbound_payload(body: bytes, content_type: Optional[str]) -> bool:
        """True when filtered payload should be dropped instead of forwarded."""
        try:
            ct = (content_type or "").lower()
            if "json" in ct or (not ct and body.lstrip().startswith(b"{")):
                data = json.loads(body)
                for key in ("text", "draft", "message", "content", "caption"):
                    value = data.get(key)
                    if isinstance(value, str) and value.strip() == _SUPPRESS_OUTBOUND_TOKEN:
                        return True
                return False
            if "x-www-form-urlencoded" in ct or (not ct and b"=" in body):
                data = dict(
                    urllib.parse.parse_qsl(
                        body.decode("utf-8", errors="replace"), keep_blank_values=True
                    )
                )
                for key in ("text", "draft", "message", "content", "caption"):
                    value = data.get(key)
                    if isinstance(value, str) and value.strip() == _SUPPRESS_OUTBOUND_TOKEN:
                        return True
        except Exception:
            return False
        return False

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
                            if not isinstance(result, dict):
                                result = {
                                    "status": "error",
                                    "reason": str(result),
                                    "action": "ignored",
                                }
                            _queue = getattr(_app_state, "egress_approval_queue", None)
                            if _queue and result.get("status") == "ok":
                                from gateway.security.egress_approval import ApprovalMode
                                rid = result.get("request_id", "")
                                action = result.get("action", "")
                                if action == "allow_always":
                                    await _queue.approve(rid, ApprovalMode.PERMANENT)
                                elif action == "allow_once":
                                    await _queue.approve(rid, ApprovalMode.ONCE)
                                elif action == "deny":
                                    await _queue.deny(rid, ApprovalMode.ONCE)
                            await _notifier.answer_callback(
                                callback_query.get("id", ""),
                                f"Egress {result.get('action', 'processed')}",
                            )
                            logger.info(
                                "Egress callback handled: %s",
                                json.dumps(result, sort_keys=True),
                            )
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

            # Normalize transport text before any guard checks so downstream
            # detectors see de-obfuscated content (zero-width, encoded entities, etc.).
            normalized_text = normalize_input(text)
            if normalized_text != text:
                if "message" in update:
                    update["message"]["text"] = normalized_text
                elif "edited_message" in update:
                    update["edited_message"]["text"] = normalized_text
                text = normalized_text

            self._stats["messages_scanned"] += 1

            # ── Role resolution ───────────────────────────────────────────────
            is_owner = self._rbac.is_owner(user_id) if self._rbac else False
            is_collaborator = (
                self._rbac and
                not is_owner and
                user_id in {str(uid) for uid in (self._rbac.collaborator_user_ids or [])}
            )

            # ── Egress preflight from user intent ────────────────────────────
            # If a non-owner message includes an explicit URL, proactively queue
            # interactive egress approval for that destination. This preserves
            # "little snitch" UX even when the model fails before tool execution.
            if not is_owner:
                try:
                    requested_url = self._extract_first_egress_target(text)
                    if requested_url:
                        await self._trigger_web_fetch_approval(
                            str(chat_id or ""),
                            {"url": requested_url},
                        )
                except Exception as _pf:
                    logger.debug("Egress preflight approval error (non-fatal): %s", _pf)

            # ── Gateway-level collaborator/non-owner activity tracking ────────
            # This is the authoritative tracking point — all messages (including
            # long-polling) flow through here. webhook_receiver only handles
            # push-mode webhooks which are not used in this deployment.
            # Track all non-owner users; tracker policy decides whether unknown
            # users are auto-enrolled (track_unknown_non_owner).
            if not is_owner:
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

            # ── Session unlock for blocked disclosure tracker on /start ───────
            if is_collaborator and text.strip().lower().startswith("/start"):
                try:
                    from gateway.ingest_api.state import app_state as _app_state
                    _tracker = getattr(_app_state, "multi_turn_tracker", None)
                    if _tracker and _tracker.reset_session(user_id, owner_override=True):
                        logger.info("Reset MultiTurnTracker session for collaborator %s via /start", user_id)
                except Exception as _re:
                    logger.debug("MultiTurnTracker reset error (non-fatal): %s", _re)

            # ── Collaborator rate limiting (200 msgs/hour) ────────────────────
            if is_collaborator and not self._collaborator_rate_limiter.check(user_id):
                self._stats["messages_blocked"] += 1
                logger.warning(
                    "Collaborator %s exceeded rate limit (200/hr) — dropping message",
                    user_id,
                )
                self._quarantine_blocked_message(
                    user_id=user_id,
                    chat_id=chat_id,
                    text=text,
                    reason="Rate limit exceeded",
                    source="telegram_rate_limit",
                )
                if chat_id:
                    await self._send_rate_limit_notice(chat_id)
                continue

            # ── Collaborator command blocking ─────────────────────────────────
            # Block owner-only slash commands before they reach the bot.
            if is_collaborator and chat_id:
                cmd = text.strip().split()[0].lower() if text.strip() else ""
                # Strip bot @mention suffix (e.g. /skill@agentshroud_bot → /skill)
                cmd_base = cmd.split("@")[0]
                if cmd_base in _COLLABORATOR_BLOCKED_COMMANDS:
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason=f"Blocked command: {cmd_base}",
                        source="telegram_command_block",
                    )
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
                            self._quarantine_blocked_message(
                                user_id=user_id,
                                chat_id=chat_id,
                                text=text,
                                reason=result.reason or "Middleware blocked message",
                                source="telegram_middleware_block",
                            )
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

            # ── Security pipeline (prompt injection, PII, heuristic, audit) ──
            # ContextGuard already ran via middleware_manager; skip_context_guard=True avoids double-check.
            if self.pipeline and text:
                try:
                    pipeline_result = await self.pipeline.process_inbound(
                        message=text,
                        source="telegram",
                        metadata={"user_id": user_id, "chat_id": chat_id},
                        skip_context_guard=True,
                    )
                    if pipeline_result.blocked:
                        if is_owner:
                            logger.info(
                                "Pipeline would block owner message (%s) — allowing; reason: %s",
                                user_id, pipeline_result.block_reason,
                            )
                        else:
                            self._stats["messages_blocked"] += 1
                            logger.warning(
                                "Pipeline blocked Telegram message from %s: %s",
                                user_id, pipeline_result.block_reason,
                            )
                            self._quarantine_blocked_message(
                                user_id=user_id,
                                chat_id=chat_id,
                                text=text,
                                reason=pipeline_result.block_reason or "Pipeline blocked message",
                                source="telegram_pipeline_block",
                            )
                            if chat_id:
                                await self._notify_user_blocked(chat_id, pipeline_result.block_reason)
                            blocked_text = f"[BLOCKED BY AGENTSHROUD: {pipeline_result.block_reason}]"
                            if "message" in update:
                                update["message"]["text"] = blocked_text
                            elif "edited_message" in update:
                                update["edited_message"]["text"] = blocked_text
                            filtered_updates.append(update)
                            continue
                    # Apply sanitized text from pipeline (PII redactions, etc.)
                    sanitized_text = pipeline_result.sanitized_message
                    if sanitized_text != text:
                        self._stats["messages_sanitized"] += 1
                        if "message" in update:
                            update["message"]["text"] = sanitized_text
                            update["message"]["_agentshroud_pii_redacted"] = True
                            update["message"]["_agentshroud_redactions"] = pipeline_result.pii_redactions
                        elif "edited_message" in update:
                            update["edited_message"]["text"] = sanitized_text
                            update["edited_message"]["_agentshroud_pii_redacted"] = True
                except Exception as exc:
                    logger.error("Pipeline error for Telegram message from %s: %s", user_id, exc)
                    if not is_owner:
                        # Fail-closed: replace message text with block notice, keep in updates list
                        self._stats["messages_blocked"] += 1
                        if chat_id:
                            await self._notify_user_blocked(chat_id, "Security pipeline error")
                        blocked_text = "[BLOCKED BY AGENTSHROUD: Security pipeline error]"
                        if "message" in update:
                            update["message"]["text"] = blocked_text
                        elif "edited_message" in update:
                            update["edited_message"]["text"] = blocked_text
                        filtered_updates.append(update)
                        continue
                    logger.warning("Pipeline error on owner message — allowing through")
            elif self.sanitizer and text:
                # Fallback: direct PII sanitization when pipeline is unavailable
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

    def _quarantine_blocked_message(
        self,
        user_id: str,
        chat_id: Optional[int],
        text: str,
        reason: str,
        source: str,
    ) -> None:
        """Persist blocked inbound messages for admin review."""
        try:
            from gateway.ingest_api.state import app_state as _app_state
            store = getattr(_app_state, "blocked_message_quarantine", None)
            if store is None:
                store = []
                setattr(_app_state, "blocked_message_quarantine", store)
            store.append(
                {
                    "message_id": str(uuid.uuid4()),
                    "timestamp": time.time(),
                    "user_id": str(user_id),
                    "chat_id": str(chat_id) if chat_id is not None else "",
                    "text": text,
                    "reason": reason,
                    "source": source,
                    "status": "pending",
                    "released_at": None,
                    "released_by": None,
                    "review_note": "",
                }
            )
            if len(store) > 5000:
                del store[: len(store) - 5000]
            self._emit_quarantine_event(
                event_type="quarantine_inbound_blocked",
                summary="Inbound message quarantined",
                details={
                    "user_id": str(user_id),
                    "chat_id": str(chat_id) if chat_id is not None else "",
                    "reason": reason,
                    "source": source,
                },
            )
        except Exception as exc:
            logger.debug("Failed to quarantine blocked message: %s", exc)

    def _quarantine_outbound_block(
        self,
        chat_id: str,
        text: str,
        reason: str,
        source: str,
    ) -> None:
        """Persist blocked outbound messages for admin review."""
        try:
            from gateway.ingest_api.state import app_state as _app_state
            store = getattr(_app_state, "blocked_outbound_quarantine", None)
            if store is None:
                store = []
                setattr(_app_state, "blocked_outbound_quarantine", store)
            store.append(
                {
                    "message_id": str(uuid.uuid4()),
                    "timestamp": time.time(),
                    "chat_id": str(chat_id),
                    "text": text,
                    "reason": reason,
                    "source": source,
                    "status": "pending",
                    "released_at": None,
                    "released_by": None,
                    "review_note": "",
                }
            )
            if len(store) > 5000:
                del store[: len(store) - 5000]
            self._emit_quarantine_event(
                event_type="quarantine_outbound_blocked",
                summary="Outbound message quarantined",
                details={
                    "chat_id": str(chat_id),
                    "reason": reason,
                    "source": source,
                },
            )
        except Exception as exc:
            logger.debug("Failed to quarantine blocked outbound message: %s", exc)

    def _emit_quarantine_event(self, event_type: str, summary: str, details: dict) -> None:
        """Best-effort async event emission for quarantine actions."""
        try:
            from gateway.ingest_api.state import app_state as _app_state
            bus = getattr(_app_state, "event_bus", None)
            if not bus:
                return
            from gateway.ingest_api.event_bus import make_event
            loop = asyncio.get_running_loop()
            loop.create_task(
                bus.emit(
                    make_event(
                        event_type,
                        summary,
                        details,
                        severity="warning",
                    )
                )
            )
        except Exception:
            # No running loop or unavailable event bus: skip quietly.
            return

    async def _send_rate_limit_notice(self, chat_id: int) -> None:
        """Notify a collaborator they have exceeded the hourly rate limit."""
        try:
            if self._bot_token:
                msg = (
                    "\U0001f6ab You have reached the collaborator message limit "
                    "\\(200 messages/hour\\)\\. Please try again later\\."
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
            logger.warning("Failed to send rate limit notice to chat %s: %s", chat_id, e)

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
                "\u26a0\ufe0f Message Blocked\n\n"
                f"{user_msg}\n\n"
                f"Reason: {self._sanitize_reason(reason)}\n\n"
                "If this is an error, contact the system owner."
            )
            if self._bot_token:
                url = f"https://api.telegram.org/bot{self._bot_token}/sendMessage"
                req = urllib.request.Request(
                    url,
                    data=json.dumps({"chat_id": chat_id, "text": notice}).encode(),
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
        try:
            response = await loop.run_in_executor(
                None,
                lambda: urllib.request.urlopen(req, timeout=60, context=self._ssl_context),
            )
            response_body = response.read()
            return json.loads(response_body)
        except urllib.error.HTTPError as exc:
            # Telegram uses HTTP 4xx/5xx with JSON bodies for expected API failures
            # (e.g., malformed Markdown, invalid chat ID). Treat as handled response.
            raw = b""
            try:
                raw = exc.read() if hasattr(exc, "read") else b""
            except Exception:
                raw = b""

            parsed: dict[str, Any]
            if raw:
                try:
                    loaded = json.loads(raw.decode("utf-8", errors="replace"))
                    if isinstance(loaded, dict):
                        parsed = loaded
                    else:
                        parsed = {}
                except Exception:
                    parsed = {}
            else:
                parsed = {}

            if "ok" not in parsed:
                parsed["ok"] = False
            parsed.setdefault("error_code", getattr(exc, "code", 502))
            parsed.setdefault("description", getattr(exc, "reason", str(exc)))

            logger.info(
                "Telegram API returned HTTP %s (%s)",
                parsed.get("error_code"),
                parsed.get("description"),
            )
            return parsed
