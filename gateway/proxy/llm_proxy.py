# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""
LLM API Reverse Proxy — intercepts all OpenClaw ↔ Anthropic traffic.

Sits between OpenClaw and the Anthropic API, enabling:
- Inbound: User messages in the prompt are scanned (PII redaction, injection defense)
- Outbound: LLM responses are filtered (credential blocking, XML stripping, canary detection)
- Audit: Every API call is logged to the security ledger

OpenClaw connects to http://gateway:8080/v1/messages instead of https://api.anthropic.com/v1/messages
via ANTHROPIC_BASE_URL env var.
"""
from __future__ import annotations

import asyncio
import json
import logging
import ssl
import time
import urllib.request
import urllib.error
from typing import Any, Optional

logger = logging.getLogger("agentshroud.proxy.llm_api")

ANTHROPIC_API_BASE = "https://api.anthropic.com"


class LLMProxy:
    """Proxies Anthropic API calls through the security pipeline."""

    def __init__(self, pipeline=None, middleware_manager=None, sanitizer=None):
        self.pipeline = pipeline
        self.middleware_manager = middleware_manager
        self.sanitizer = sanitizer
        self._ssl_context = ssl.create_default_context()
        self._stats = {
            "total_requests": 0,
            "messages_scanned": 0,
            "pii_redacted": 0,
            "injections_blocked": 0,
            "responses_filtered": 0,
            "streaming_responses_scanned": 0,
            "streaming_responses_blocked": 0,
            "streaming_responses_redacted": 0,
        }

    def get_stats(self) -> dict:
        return dict(self._stats)

    async def proxy_messages(
        self,
        path: str,
        body: bytes,
        headers: dict[str, str],
        user_id: str = "unknown",
    ) -> tuple[int, dict, bytes]:
        """Proxy a /v1/messages (or any /v1/*) request to Anthropic.
        
        Returns (status_code, response_headers, response_body).
        For /v1/messages: scans user messages for PII and injection.
        For streaming: passes through (content filtering on non-stream responses).
        """
        self._stats["total_requests"] += 1

        # Parse the request body for /v1/messages
        is_messages = "/messages" in path
        request_data = None
        if is_messages and body:
            try:
                request_data = json.loads(body)
            except (json.JSONDecodeError, UnicodeDecodeError):
                pass

        # === INBOUND SCANNING: Scan user messages ===
        if request_data and "messages" in request_data:
            messages = request_data["messages"]
            for i, msg in enumerate(messages):
                if msg.get("role") != "user":
                    continue
                
                content = msg.get("content", "")
                if isinstance(content, list):
                    # Multi-part content (text + images)
                    for part in content:
                        if isinstance(part, dict) and part.get("type") == "text":
                            part["text"] = await self._scan_inbound(part["text"], user_id=user_id)
                elif isinstance(content, str):
                    messages[i]["content"] = await self._scan_inbound(content, user_id=user_id)

            request_data["messages"] = messages
            body = json.dumps(request_data).encode()

        # === FORWARD TO ANTHROPIC ===
        url = f"{ANTHROPIC_API_BASE}{path}"
        
        # Check if streaming
        is_streaming = request_data and request_data.get("stream", False)
        
        try:
            status, resp_headers, resp_body = await self._forward_to_anthropic(
                url, body, headers
            )
        except Exception as e:
            logger.error(f"LLM proxy error: {e}")
            error_resp = json.dumps({
                "type": "error",
                "error": {"type": "api_error", "message": f"Gateway proxy error: {e}"}
            }).encode()
            return 502, {"content-type": "application/json"}, error_resp

        # === OUTBOUND FILTERING ===
        if not is_streaming and status == 200 and resp_body:
            resp_body = await self._filter_outbound(resp_body)
        elif is_streaming and status == 200 and resp_body:
            # Streaming responses are fully buffered by urllib before delivery,
            # so we CAN inspect the complete SSE stream here.
            resp_body = await self._filter_outbound_streaming(resp_body, user_id=user_id)

        return status, resp_headers, resp_body

    async def _scan_inbound(self, text: str, user_id: str = "unknown") -> str:
        """Scan inbound user message text for PII and injection."""
        if not text:
            return text

        self._stats["messages_scanned"] += 1

        # PII Redaction
        if self.sanitizer:
            try:
                result = await self.sanitizer.sanitize(text)
                if result.entity_types_found:
                    self._stats["pii_redacted"] += 1
                    logger.info(f"LLM proxy: PII redacted from user message: {result.entity_types_found}")
                    text = result.sanitized_content
            except Exception as e:
                logger.error(f"LLM proxy PII scan error: {e}")

        # Middleware checks (injection detection, context guard, etc.)
        if self.middleware_manager:
            try:
                request_data = {
                    "message": text,
                    "content_type": "text",
                    "source": "llm_proxy",
                    "headers": {},
                    "user_id": user_id,
                }
                result = await self.middleware_manager.process_request(request_data, "llm_proxy")
                if not result.allowed:
                    self._stats["injections_blocked"] += 1
                    logger.warning(f"LLM proxy: message blocked by middleware: {result.reason}")
                    return f"[MESSAGE BLOCKED BY AGENTSHROUD: {result.reason}]"
            except Exception as e:
                logger.error(f"LLM proxy middleware error: {e}")

        return text

    async def _filter_outbound(self, resp_body: bytes) -> bytes:
        """Filter outbound LLM response for credential leaks and XML."""
        try:
            data = json.loads(resp_body)
            content = data.get("content", [])
            modified = False

            for i, block in enumerate(content):
                if block.get("type") != "text":
                    continue
                text = block.get("text", "")
                if not text:
                    continue

                # XML leak filter
                if self.sanitizer:
                    filtered, was_filtered = self.sanitizer.filter_xml_blocks(text)
                    if was_filtered:
                        content[i]["text"] = filtered
                        modified = True
                        self._stats["responses_filtered"] += 1
                        logger.info("LLM proxy: XML blocks stripped from response")

                    # Credential blocking
                    blocked, was_blocked = await self.sanitizer.block_credentials(
                        content[i]["text"], "telegram"
                    )
                    if was_blocked:
                        content[i]["text"] = blocked
                        modified = True
                        self._stats["responses_filtered"] += 1
                        logger.warning("LLM proxy: credentials blocked in response")

            if modified:
                data["content"] = content
                return json.dumps(data).encode()
        except Exception as e:
            logger.error(f"LLM proxy outbound filter error: {e}")

        return resp_body

    async def _filter_outbound_streaming(
        self, resp_body: bytes, user_id: str = "unknown"
    ) -> bytes:
        """Inspect a fully-buffered Anthropic SSE stream through the security pipeline.

        urllib.request reads the complete SSE body before we return it, so we can
        scan the accumulated text and either block or sanitize it before delivery.

        BLOCK: the entire resp_body is replaced with a synthetic SSE error stream.
        REDACT: text deltas are consolidated into a single sanitized delta event.
        """
        self._stats["streaming_responses_scanned"] += 1

        accumulated = self._extract_sse_text(resp_body)
        if not accumulated:
            return resp_body

        try:
            if self.pipeline:
                result = await self.pipeline.process_outbound(
                    response=accumulated,
                    agent_id="default",
                    metadata={"user_id": user_id, "source": "llm_proxy_stream"},
                )
                if result.blocked:
                    self._stats["streaming_responses_blocked"] += 1
                    logger.critical(
                        "LLM proxy: streaming response BLOCKED (user=%s, reason=%s)",
                        user_id,
                        result.block_reason,
                    )
                    return self._build_blocked_sse(result.block_reason)

                if result.sanitized_message != accumulated:
                    self._stats["streaming_responses_redacted"] += 1
                    logger.info(
                        "LLM proxy: streaming response sanitized (pii=%d, info=%d, encodings=%s)",
                        result.pii_redaction_count,
                        result.info_filter_redaction_count,
                        result.encoding_detections,
                    )
                    return self._rebuild_sse(resp_body, result.sanitized_message)
            elif self.sanitizer:
                # Fallback when no full pipeline: basic XML + credential filter
                resp_body = await self._filter_outbound(resp_body)
        except Exception as exc:
            logger.error("LLM proxy streaming filter error: %s", exc)

        return resp_body

    def _extract_sse_text(self, resp_body: bytes) -> str:
        """Accumulate all text_delta content from an Anthropic SSE stream."""
        parts: list[str] = []
        for line in resp_body.decode("utf-8", errors="replace").splitlines():
            if not line.startswith("data: "):
                continue
            try:
                data = json.loads(line[6:])
                if data.get("type") == "content_block_delta":
                    delta = data.get("delta", {})
                    if delta.get("type") == "text_delta":
                        parts.append(delta.get("text", ""))
            except (json.JSONDecodeError, KeyError):
                continue
        return "".join(parts)

    def _build_blocked_sse(self, reason: str) -> bytes:
        """Synthesize a minimal SSE stream that delivers a block notification."""
        blocked_text = f"[AGENTSHROUD SECURITY: Response blocked — {reason}]"
        events = [
            'event: message_start\n'
            'data: {"type":"message_start","message":{"id":"blocked","type":"message",'
            '"role":"assistant","content":[],"stop_reason":null,"stop_sequence":null,'
            '"usage":{"input_tokens":0,"output_tokens":0}}}\n',
            'event: content_block_start\n'
            'data: {"type":"content_block_start","index":0,'
            '"content_block":{"type":"text","text":""}}\n',
            f'event: content_block_delta\n'
            f'data: {json.dumps({"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":blocked_text}})}\n',
            'event: content_block_stop\n'
            'data: {"type":"content_block_stop","index":0}\n',
            'event: message_delta\n'
            'data: {"type":"message_delta","delta":{"stop_reason":"end_turn","stop_sequence":null},'
            '"usage":{"output_tokens":1}}\n',
            'event: message_stop\n'
            'data: {"type":"message_stop"}\n',
        ]
        return ("\n".join(events) + "\n").encode("utf-8")

    def _rebuild_sse(self, original: bytes, sanitized_text: str) -> bytes:
        """Rebuild SSE stream replacing all text deltas with a single sanitized delta.

        Keeps all non-text-delta events intact (message_start, content_block_start/stop,
        message_delta, message_stop) so the bot's streaming client gets valid SSE.
        The sanitized text is injected as the first text_delta; subsequent ones are dropped.
        """
        lines = original.decode("utf-8", errors="replace").splitlines()
        output: list[str] = []
        text_injected = False

        for line in lines:
            if not line.startswith("data: "):
                output.append(line)
                continue
            try:
                data = json.loads(line[6:])
                if data.get("type") == "content_block_delta":
                    delta = data.get("delta", {})
                    if delta.get("type") == "text_delta":
                        if not text_injected:
                            data["delta"]["text"] = sanitized_text
                            output.append(f"data: {json.dumps(data)}")
                            text_injected = True
                        # Subsequent text_deltas consumed into the single replacement
                        continue
            except (json.JSONDecodeError, KeyError):
                pass
            output.append(line)

        return "\n".join(output).encode("utf-8")

    async def _forward_to_anthropic(
        self, url: str, body: bytes, headers: dict[str, str]
    ) -> tuple[int, dict, bytes]:
        """Forward request to real Anthropic API."""
        # Filter headers — pass through auth and content type
        forward_headers = {}
        for key, value in headers.items():
            lower = key.lower()
            if lower in (
                "authorization", "x-api-key", "anthropic-version",
                "anthropic-beta", "content-type", "accept",
            ):
                forward_headers[key] = value

        req = urllib.request.Request(url, data=body, headers=forward_headers)

        loop = asyncio.get_event_loop()
        try:
            response = await loop.run_in_executor(
                None,
                lambda: urllib.request.urlopen(req, timeout=120, context=self._ssl_context),
            )
            resp_body = response.read()
            resp_headers = dict(response.headers)
            return response.status, resp_headers, resp_body
        except urllib.error.HTTPError as e:
            resp_body = e.read()
            return e.code, dict(e.headers), resp_body
