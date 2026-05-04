# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""
LLM API Reverse Proxy — intercepts all OpenClaw ↔ (Anthropic/OpenAI/Google) traffic.

Sits between OpenClaw and the LLM APIs, enabling:
- Inbound: User messages in the prompt are scanned (PII redaction, injection defense)
- Outbound: LLM responses are filtered (credential blocking, XML stripping, canary detection)
- Audit: Every API call is logged to the security ledger
"""

from __future__ import annotations

import asyncio
import json
import logging
import os
import re
import ssl
import time
import urllib.error
import urllib.request
from collections.abc import AsyncIterator
from typing import Any

logger = logging.getLogger("agentshroud.proxy.llm_api")

ANTHROPIC_API_BASE = "https://api.anthropic.com"
OPENAI_API_BASE = "https://api.openai.com"
GOOGLE_API_BASE = "https://generativelanguage.googleapis.com"
OLLAMA_API_BASE = "http://host.docker.internal:11434"
LMSTUDIO_API_BASE = os.environ.get("LMSTUDIO_API_BASE", "http://host.docker.internal:1234")
MLXLM_API_BASE = os.environ.get("MLXLM_API_BASE", "http://host.docker.internal:8234")
MAIN_MODEL = os.environ.get("AGENTSHROUD_LOCAL_MODEL", "qwen2.5-coder:7b")
MODEL_MODE = os.environ.get("AGENTSHROUD_MODEL_MODE", "local").lower()

# Maps model name prefixes to specific backend base URLs.
# Checked before the generic Ollama fallback — only needed for models that do NOT
# run under Ollama (e.g. mlx_lm or LM Studio on a different port).
# Models not listed here fall through to OLLAMA_API_BASE automatically.
LOCAL_MODEL_ROUTES: dict[str, str] = {
    "mlx-community/deepseek-r1": MLXLM_API_BASE,  # mlx-lm full-ID: DeepSeek-R1-0528-Qwen3-8B-4bit
    "deepseek-r1": MLXLM_API_BASE,  # Reasoning — mlx_lm on :8234 (no tool calling)
    "qwen3": LMSTUDIO_API_BASE,  # Qwen3 family — LM Studio on :1234
    "qwen2.5-coder": LMSTUDIO_API_BASE,  # Coding — LM Studio on :1234
    "gemma": LMSTUDIO_API_BASE,  # Gemma family — LM Studio on :1234
}

# Qwen3 models generate <think> blocks by default which can consume thousands of
# tokens before producing a user-visible response, causing timeouts on complex
# prompts.  Prefixing /no_think to the first system message suppresses thinking —
# the model produces an empty <think></think> and goes straight to the answer.
# Models whose name prefix appears in this set get the injection.
_QWEN3_THINK_SUPPRESS_PREFIXES = ("qwen3",)

# Models that SHOULD think (reasoning models) are excluded.
_REASONING_MODEL_PREFIXES = ("deepseek-r1", "mlx-community/deepseek-r1")


def _inject_no_think(request_data: dict, model_name: str) -> bool:
    """Prepend /no_think to the first system message for Qwen3 non-reasoning models.

    Returns True if the request was modified.
    """
    model_lower = model_name.lower()
    # Only apply to Qwen3 models
    if not any(model_lower.startswith(p) for p in _QWEN3_THINK_SUPPRESS_PREFIXES):
        return False
    # Skip reasoning models
    if any(model_lower.startswith(p) for p in _REASONING_MODEL_PREFIXES):
        return False

    messages = request_data.get("messages")
    if not messages or not isinstance(messages, list):
        return False

    # Find the first system message and prepend /no_think
    for msg in messages:
        if isinstance(msg, dict) and msg.get("role") == "system":
            content = msg.get("content", "")
            if isinstance(content, str) and not content.startswith("/no_think"):
                msg["content"] = "/no_think\n" + content
                return True
            return False  # Already has /no_think

    # No system message — inject one at the start
    messages.insert(0, {"role": "system", "content": "/no_think"})
    return True


class LLMProxy:
    """Proxies LLM API calls (Anthropic, OpenAI, Google) through the security pipeline."""

    def __init__(
        self, pipeline=None, middleware_manager=None, sanitizer=None, tool_acl_enforcer=None
    ):
        self.pipeline = pipeline
        self.middleware_manager = middleware_manager
        self.sanitizer = sanitizer
        self.tool_acl_enforcer = tool_acl_enforcer
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
        """Proxy an LLM API request.

        Returns (status_code, response_headers, response_body).
        Automatically detects provider (Anthropic, OpenAI, Google) based on path or headers.
        """
        self._stats["total_requests"] += 1

        # Determine provider
        is_openai = "/v1/chat/completions" in path or "/v1/completions" in path
        is_google = "/v1beta" in path or "google" in path.lower()
        is_ollama_native = "/api/" in path

        request_data = None
        if body:
            try:
                request_data = json.loads(body)
            except (json.JSONDecodeError, UnicodeDecodeError):
                pass

        # Detect local model (Ollama, LM Studio, or mlx_lm)
        model_name = request_data.get("model", "") if request_data else ""
        local_keywords = [
            "qwen",
            "llama",
            "mistral",
            "deepseek",
            "phi",
            "ollama",
            "lmstudio",
            "mlxlm",
        ]

        # INTERCEPT: If the system tries to use Claude Opus, force it to use the configured local model
        if MODEL_MODE not in ("cloud",) and "claude-opus" in model_name.lower():
            logger.info(f"LLMProxy: Intercepted internal Claude Opus request, forcing {MAIN_MODEL}")
            if request_data:
                request_data["model"] = MAIN_MODEL
                body = json.dumps(request_data).encode()
            model_name = MAIN_MODEL

        is_ollama = (
            is_ollama_native
            or any(k in model_name.lower() for k in local_keywords)
            or model_name.startswith("ollama/")
            or model_name.startswith("lmstudio/")
        )

        # Normalize provider-prefixed model references (ollama/, lmstudio/) to bare model names.
        # OpenClaw may emit model IDs like "ollama/qwen2.5-coder:7b" or "lmstudio/qwen3.5-27b",
        # but all local OpenAI-compatible APIs expect bare model names.
        model_lower = model_name.lower()
        for prefix in ("ollama/", "lmstudio/"):
            if model_lower.startswith(prefix):
                request_data["model"] = model_name.split("/", 1)[1]
                model_name = request_data["model"]
                model_lower = model_name.lower()
                break

        # Suppress Qwen3 thinking for non-reasoning models (prevents timeouts)
        if request_data and is_ollama:
            if _inject_no_think(request_data, model_lower):
                body = json.dumps(request_data).encode()

        # === INBOUND SCANNING: Scan user messages ===
        if request_data:
            await self._scan_request_data(request_data, user_id)
            body = json.dumps(request_data).encode()

        # Determine provider base URL.
        # LOCAL_MODEL_ROUTES maps model name prefixes to specific backends (LM Studio / mlx_lm).
        # Falls back to Ollama for all other local keywords.
        base_url = ANTHROPIC_API_BASE
        if is_ollama:
            base_url = OLLAMA_API_BASE
            for prefix, route_url in LOCAL_MODEL_ROUTES.items():
                if model_lower.startswith(prefix):
                    base_url = route_url
                    break
        elif is_openai:
            base_url = OPENAI_API_BASE
        elif is_google:
            base_url = GOOGLE_API_BASE

        url = f"{base_url}{path}"

        # Check if streaming
        is_streaming = request_data and request_data.get("stream", False)

        try:
            status, resp_headers, resp_body = await self._forward_request(url, body, headers)
        except TimeoutError as e:
            logger.error(f"LLM proxy timeout: {e}")
            fallback_body = self._build_timeout_fallback_response(
                is_openai=is_openai,
                is_google=is_google,
                is_ollama=is_ollama,
                model_name=model_name or (request_data or {}).get("model", ""),
            )
            return 200, {"content-type": "application/json"}, fallback_body
        except Exception as e:
            logger.error(f"LLM proxy error: {e}")
            error_resp = json.dumps(
                {
                    "type": "error",
                    "error": {"type": "api_error", "message": f"Gateway proxy error: {e}"},
                }
            ).encode()
            return 502, {"content-type": "application/json"}, error_resp

        # === OUTBOUND FILTERING ===
        if not is_streaming and status == 200 and resp_body:
            resp_body = await self._filter_outbound(resp_body)
            # Tool ACL: gate tool_use blocks in Anthropic responses
            if self.tool_acl_enforcer and user_id != "unknown":
                resp_body = self._enforce_tool_acl(resp_body, user_id)
        elif is_streaming and status == 200 and resp_body:
            # Streaming responses are fully buffered by urllib before delivery
            resp_body = await self._filter_outbound_streaming(resp_body, user_id=user_id)

        return status, resp_headers, resp_body

    async def proxy_messages_streaming(
        self,
        path: str,
        body: bytes,
        headers: dict[str, str],
        user_id: str = "unknown",
    ) -> AsyncIterator[bytes]:
        """Proxy a streaming LLM API request, yielding SSE chunks as they arrive.

        Used when the client sends stream:true.  Bypasses the buffering in
        _forward_request so OpenClaw's 60-second HTTP fetch timeout is not
        triggered while waiting for the first response byte from a slow model.
        """
        import httpx

        self._stats["total_requests"] += 1

        request_data = None
        if body:
            try:
                request_data = json.loads(body)
            except (json.JSONDecodeError, UnicodeDecodeError):
                pass

        # Determine target URL (same routing logic as proxy_messages)
        model_name = (request_data or {}).get("model", "")
        is_openai = "/v1/chat/completions" in path or "/v1/completions" in path
        is_google = "/v1beta" in path or "google" in path.lower()
        model_lower = model_name.lower()
        local_keywords = [
            "qwen",
            "llama",
            "mistral",
            "deepseek",
            "phi",
            "ollama",
            "lmstudio",
            "mlxlm",
        ]
        is_ollama = (
            any(k in model_lower for k in local_keywords)
            or model_lower.startswith("ollama/")
            or model_lower.startswith("lmstudio/")
        )

        # Suppress Qwen3 thinking for non-reasoning models (prevents timeouts)
        if request_data and is_ollama:
            _inject_no_think(request_data, model_lower)

        # Inbound scanning (same as proxy_messages)
        if request_data:
            await self._scan_request_data(request_data, user_id)
            body = json.dumps(request_data).encode()

        base_url = ANTHROPIC_API_BASE
        if is_ollama:
            base_url = OLLAMA_API_BASE
            for prefix, route_url in LOCAL_MODEL_ROUTES.items():
                if model_lower.startswith(prefix):
                    base_url = route_url
                    break
        elif is_openai:
            base_url = OPENAI_API_BASE
        elif is_google:
            base_url = GOOGLE_API_BASE

        url = f"{base_url}{path}"

        forward_headers: dict[str, str] = {}
        allowed_headers = (
            "authorization",
            "x-api-key",
            "anthropic-version",
            "anthropic-beta",
            "content-type",
            "accept",
            "user-agent",
            "x-goog-api-key",
        )
        for key, value in headers.items():
            if key.lower() in allowed_headers:
                forward_headers[key] = value

        async def _stream() -> AsyncIterator[bytes]:
            try:
                async with httpx.AsyncClient(
                    verify=True, timeout=httpx.Timeout(5.0, read=600.0)
                ) as client:
                    async with client.stream(
                        "POST", url, content=body, headers=forward_headers
                    ) as response:
                        async for chunk in response.aiter_bytes():
                            if chunk:
                                yield chunk
            except Exception as e:
                logger.error("LLM proxy streaming error: %s", e)
                err = json.dumps(
                    {"type": "error", "error": {"type": "api_error", "message": str(e)}}
                )
                yield f"data: {err}\n\n".encode()

        return _stream()

    async def _scan_request_data(self, request_data: dict, user_id: str):
        """Scan request data for PII and injection across different provider formats."""
        # Anthropic/OpenAI format
        if "messages" in request_data:
            messages = request_data["messages"]
            for i, msg in enumerate(messages):
                if msg.get("role") == "user":
                    content = msg.get("content", "")
                    if isinstance(content, str):
                        messages[i]["content"] = await self._scan_inbound(content, user_id=user_id)
                    elif isinstance(content, list):
                        for part in content:
                            if isinstance(part, dict) and part.get("type") == "text":
                                part["text"] = await self._scan_inbound(
                                    part["text"], user_id=user_id
                                )

        # Google Gemini format
        if "contents" in request_data:
            for content in request_data["contents"]:
                if content.get("role") == "user":
                    for part in content.get("parts", []):
                        if "text" in part:
                            part["text"] = await self._scan_inbound(part["text"], user_id=user_id)

        # Ollama Native Chat/Generate format
        if "prompt" in request_data and isinstance(request_data["prompt"], str):
            request_data["prompt"] = await self._scan_inbound(
                request_data["prompt"], user_id=user_id
            )

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
                    logger.info(
                        f"LLM proxy: PII redacted from user message: {result.entity_types_found}"
                    )
                    text = result.sanitized_content
            except Exception as e:
                logger.error(f"LLM proxy PII scan error: {e}")

        # Middleware checks (injection detection, context guard, etc.).
        # Some model-provider calls do not carry end-user identity headers.
        # Avoid enforcing RBAC/context middleware on "unknown" synthetic IDs.
        if self.middleware_manager and user_id != "unknown":
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

            # Anthropic/OpenAI response formats differ
            modified = False

            # Anthropic
            if "content" in data and isinstance(data["content"], list):
                for i, block in enumerate(data["content"]):
                    if block.get("type") == "text":
                        text = block.get("text", "")
                        filtered, was_f = await self._apply_filters(text)
                        if was_f:
                            data["content"][i]["text"] = filtered
                            modified = True

            # OpenAI
            if "choices" in data and isinstance(data["choices"], list):
                for i, choice in enumerate(data["choices"]):
                    if "message" in choice:
                        msg = choice["message"]
                        # Handle reasoning_content (LM Studio separateReasoningContentInAPI).
                        # When present, content has the final answer and reasoning_content
                        # has the thinking. If content is empty, fall back to reasoning_content.
                        reasoning = msg.pop("reasoning_content", None)
                        if reasoning and isinstance(reasoning, str):
                            if not msg.get("content"):
                                msg["content"] = reasoning
                            data["choices"][i]["message"] = msg
                            modified = True
                        # Strip <think>...</think> blocks from inline content (Qwen3 without
                        # separateReasoningContentInAPI sends thinking as <think> tags).
                        if isinstance(msg.get("content"), str) and "<think>" in msg["content"]:
                            cleaned = re.sub(r"<think>[\s\S]*?</think>\s*", "", msg["content"]).strip()
                            if cleaned != msg["content"]:
                                msg["content"] = cleaned
                                data["choices"][i]["message"] = msg
                                modified = True
                        if "content" in msg and msg["content"]:
                            text = msg["content"]
                            filtered, was_f = await self._apply_filters(text)
                            if was_f:
                                data["choices"][i]["message"]["content"] = filtered
                                modified = True

            if modified:
                return json.dumps(data).encode()
        except Exception as e:
            logger.error(f"LLM proxy outbound filter error: {e}")

        return resp_body

    def _enforce_tool_acl(self, resp_body: bytes, user_id: str) -> bytes:
        """Scan Anthropic tool_use blocks; replace denied tools with a text error block.

        Only acts on non-streaming Anthropic-format responses (content list with
        tool_use blocks). Silently passes through non-Anthropic or malformed responses.
        """
        try:
            data = json.loads(resp_body)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return resp_body

        content = data.get("content")
        if not isinstance(content, list):
            return resp_body

        modified = False
        new_content = []
        for block in content:
            if not isinstance(block, dict) or block.get("type") != "tool_use":
                new_content.append(block)
                continue

            tool_name = block.get("name", "")
            allowed, reason = self.tool_acl_enforcer.can_use_tool(user_id, tool_name)
            if allowed:
                new_content.append(block)
            else:
                logger.warning(
                    "LLMProxy ToolACL: blocked tool_use for user=%s tool=%s reason=%s",
                    user_id,
                    tool_name,
                    reason,
                )
                # Replace denied tool_use with an informational text block
                new_content.append(
                    {
                        "type": "text",
                        "text": f"[AgentShroud] Tool '{tool_name}' is not permitted for your role. {reason}",
                    }
                )
                modified = True

        if not modified:
            return resp_body

        data["content"] = new_content
        return json.dumps(data).encode()

    @staticmethod
    def _build_timeout_fallback_response(
        *,
        is_openai: bool,
        is_google: bool,
        is_ollama: bool,
        model_name: str,
    ) -> bytes:
        """Build provider-compatible timeout fallback message to avoid silent Telegram failures."""
        fallback_text = (
            "⏳ Model response timed out before completion. "
            "Please retry in 10–20 seconds. "
            "If this repeats, switch model profile with scripts/switch_model.sh "
            "(for example: openai or local llama3.1:8b)."
        )
        now = int(time.time())

        if is_google:
            return json.dumps(
                {
                    "candidates": [
                        {
                            "content": {"parts": [{"text": fallback_text}], "role": "model"},
                            "finishReason": "STOP",
                            "index": 0,
                        }
                    ]
                }
            ).encode()

        if is_openai or is_ollama:
            return json.dumps(
                {
                    "id": f"chatcmpl-agentshroud-timeout-{now}",
                    "object": "chat.completion",
                    "created": now,
                    "model": model_name or "agentshroud-timeout-fallback",
                    "choices": [
                        {
                            "index": 0,
                            "message": {"role": "assistant", "content": fallback_text},
                            "finish_reason": "stop",
                        }
                    ],
                }
            ).encode()

        # Anthropic-compatible fallback
        return json.dumps(
            {
                "id": f"msg_agentshroud_timeout_{now}",
                "type": "message",
                "role": "assistant",
                "model": model_name or "agentshroud-timeout-fallback",
                "content": [{"type": "text", "text": fallback_text}],
                "stop_reason": "end_turn",
                "stop_sequence": None,
                "usage": {"input_tokens": 0, "output_tokens": 0},
            }
        ).encode()

    async def _apply_filters(self, text: str) -> tuple[str, bool]:
        """Apply XML and credential filters to text."""
        if not text or not self.sanitizer:
            return text, False

        modified = False
        # XML leak filter
        filtered, was_filtered = self.sanitizer.filter_xml_blocks(text)
        if was_filtered:
            text = filtered
            modified = True
            self._stats["responses_filtered"] += 1

        # Credential blocking
        blocked, was_blocked = await self.sanitizer.block_credentials(text, "telegram")
        if was_blocked:
            text = blocked
            modified = True
            self._stats["responses_filtered"] += 1

        return text, modified

    async def _filter_outbound_streaming(self, resp_body: bytes, user_id: str = "unknown") -> bytes:
        """Filter buffered SSE-like streaming responses for XML/credential leaks."""
        del user_id  # reserved for per-user telemetry in future revisions

        try:
            text = resp_body.decode("utf-8")
        except UnicodeDecodeError:
            return resp_body

        if "data:" not in text:
            return resp_body

        modified_any = False
        out_lines: list[str] = []

        for line in text.splitlines(keepends=False):
            if not line.startswith("data:"):
                out_lines.append(line)
                continue

            payload = line[5:].lstrip()
            if payload == "[DONE]":
                out_lines.append(line)
                continue

            try:
                event = json.loads(payload)
            except json.JSONDecodeError:
                out_lines.append(line)
                continue

            modified_event = await self._filter_streaming_event(event)
            if modified_event is not event:
                modified_any = True
            out_lines.append(f"data: {json.dumps(modified_event, separators=(',', ':'))}")

        if not modified_any:
            return resp_body

        self._stats["streaming_responses_scanned"] += 1
        return ("\n".join(out_lines) + "\n").encode("utf-8")

    async def _filter_streaming_event(self, event: dict[str, Any]) -> dict[str, Any]:
        """Apply outbound text filters to known streaming response formats."""
        modified = False
        event_copy = dict(event)

        # OpenAI-style: choices[].delta.content / choices[].message.content
        choices = event_copy.get("choices")
        if isinstance(choices, list):
            new_choices = []
            for choice in choices:
                if not isinstance(choice, dict):
                    new_choices.append(choice)
                    continue

                new_choice = dict(choice)
                delta = new_choice.get("delta")
                if isinstance(delta, dict):
                    # Handle reasoning_content: move to content if content is empty
                    reasoning = delta.pop("reasoning_content", None)
                    if reasoning and isinstance(reasoning, str):
                        delta = dict(delta)
                        if not delta.get("content"):
                            delta["content"] = reasoning
                        new_choice["delta"] = delta
                        modified = True
                    # Strip <think> tags from streaming content
                    if isinstance(delta.get("content"), str) and "<think>" in delta["content"]:
                        cleaned = re.sub(r"<think>[\s\S]*?</think>\s*", "", delta["content"])
                        if cleaned != delta["content"]:
                            delta = dict(delta)
                            delta["content"] = cleaned
                            new_choice["delta"] = delta
                            modified = True
                    if isinstance(delta.get("content"), str) and delta["content"]:
                        filtered, changed = await self._apply_filters(delta["content"])
                        if changed:
                            delta = dict(delta)
                            delta["content"] = filtered
                            new_choice["delta"] = delta
                            modified = True

                message = new_choice.get("message")
                if isinstance(message, dict):
                    reasoning = message.pop("reasoning_content", None)
                    if reasoning and isinstance(reasoning, str):
                        message = dict(message)
                        if not message.get("content"):
                            message["content"] = reasoning
                        new_choice["message"] = message
                        modified = True
                    if isinstance(message.get("content"), str):
                        filtered, changed = await self._apply_filters(message["content"])
                        if changed:
                            message = dict(message)
                            message["content"] = filtered
                            new_choice["message"] = message
                        modified = True

                new_choices.append(new_choice)
            event_copy["choices"] = new_choices

        # Anthropic-like event chunks: content[].text
        content_blocks = event_copy.get("content")
        if isinstance(content_blocks, list):
            new_blocks = []
            for block in content_blocks:
                if not isinstance(block, dict):
                    new_blocks.append(block)
                    continue
                new_block = dict(block)
                if new_block.get("type") == "text" and isinstance(new_block.get("text"), str):
                    filtered, changed = await self._apply_filters(new_block["text"])
                    if changed:
                        new_block["text"] = filtered
                        modified = True
                new_blocks.append(new_block)
            event_copy["content"] = new_blocks

        if modified:
            self._stats["streaming_responses_redacted"] += 1
            return event_copy
        return event

    async def _forward_request(
        self, url: str, body: bytes, headers: dict[str, str]
    ) -> tuple[int, dict, bytes]:
        """Forward request to the real LLM API provider.

        Retries up to 3 times on transient API errors (429, 529, 503) with
        exponential backoff + jitter. Respects Retry-After header when present.
        """
        import random

        forward_headers = {}
        allowed_headers = (
            "authorization",
            "x-api-key",
            "anthropic-version",
            "anthropic-beta",
            "content-type",
            "accept",
            "user-agent",
            "x-goog-api-key",
        )
        for key, value in headers.items():
            if key.lower() in allowed_headers:
                forward_headers[key] = value

        _RETRYABLE = {429, 503, 529}  # 529 = Anthropic "overloaded"
        _MAX_RETRIES = 3
        loop = asyncio.get_event_loop()

        for _attempt in range(_MAX_RETRIES + 1):
            req = urllib.request.Request(url, data=body, headers=forward_headers)
            try:
                response = await loop.run_in_executor(
                    None,
                    lambda: urllib.request.urlopen(req, timeout=600, context=self._ssl_context),
                )
                resp_body = response.read()
                resp_headers = dict(response.headers)
                return response.status, resp_headers, resp_body
            except urllib.error.HTTPError as e:
                resp_body = e.read()
                resp_headers = dict(e.headers)
                if e.code not in _RETRYABLE or _attempt >= _MAX_RETRIES:
                    return e.code, resp_headers, resp_body
                # Respect Retry-After header (Anthropic 429 includes it)
                retry_after_str = resp_headers.get("retry-after") or resp_headers.get(
                    "Retry-After", ""
                )
                try:
                    wait = max(float(retry_after_str), 1.0)
                except (ValueError, TypeError):
                    # Exponential backoff: 2s, 4s, 8s + jitter
                    wait = (2 ** (_attempt + 1)) + random.uniform(0, 1)
                logger.warning(
                    "LLM API returned %s (attempt %d/%d) — retrying in %.1fs",
                    e.code,
                    _attempt + 1,
                    _MAX_RETRIES,
                    wait,
                )
                await asyncio.sleep(wait)
