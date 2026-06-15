# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""
Anthropic Messages API ↔ Ollama OpenAI-compat translator.

Pure functions — no I/O, no side effects. Used by the LLM failover orchestrator
to transparently re-route Anthropic-format requests to a local Ollama instance
when cloud quota is exhausted.

Supports: text, tool_use/tool_result, image (vision passthrough).
Streaming is handled by the companion anthropic_openai_sse_translator module.
"""

from __future__ import annotations

import json
import logging
import random
import string
import time

logger = logging.getLogger("agentshroud.proxy.anthropic_openai_translator")

_FINISH_REASON_TO_STOP_REASON: dict[str, str] = {
    "stop": "end_turn",
    "length": "max_tokens",
    "tool_calls": "tool_use",
    "content_filter": "stop_sequence",
}


def _random_msg_id() -> str:
    chars = string.ascii_lowercase + string.digits
    return "msg_local_" + "".join(random.choices(chars, k=8))


# ---------------------------------------------------------------------------
# Request: Anthropic → OpenAI
# ---------------------------------------------------------------------------


def _anthropic_content_to_openai(content: str | list) -> str | list:
    """Convert an Anthropic message content field to OpenAI format."""
    if isinstance(content, str):
        return content

    openai_parts: list = []
    for block in content:
        if not isinstance(block, dict):
            continue
        btype = block.get("type", "")
        if btype == "text":
            openai_parts.append({"type": "text", "text": block.get("text", "")})
        elif btype == "image":
            # Pass image_url blocks through; Ollama OpenAI-compat supports them
            # for vision models. Unsupported models will ignore or 400, but we
            # should not silently drop the block.
            src = block.get("source", {})
            if src.get("type") == "base64":
                url = f"data:{src.get('media_type','image/png')};base64,{src.get('data','')}"
                openai_parts.append({"type": "image_url", "image_url": {"url": url}})
            elif src.get("type") == "url":
                openai_parts.append({"type": "image_url", "image_url": {"url": src.get("url", "")}})
            else:
                logger.warning(
                    "anthropic_to_openai: unsupported image source type %s — skipping",
                    src.get("type"),
                )
        elif btype == "tool_use":
            # Accumulated as a separate tool_call on the assistant message — handled
            # at the message level, not the content-part level.
            pass
        elif btype == "tool_result":
            # tool_result blocks convert to role="tool" messages — handled by the
            # caller at the messages loop level.
            pass
        else:
            # Unknown block type — log a warning, skip gracefully.
            logger.warning("anthropic_to_openai: unknown content block type %s — skipping", btype)

    # If only text parts remain and there's exactly one, return as plain string
    # so OpenAI-compat APIs that don't support multi-part content still work.
    if all(p.get("type") == "text" for p in openai_parts):
        combined = "".join(p.get("text", "") for p in openai_parts)
        return combined or ""

    return openai_parts or ""


def _anthropic_system_to_openai(system: str | list | None) -> str:
    """Flatten Anthropic system prompt (string or content-block list) to plain text."""
    if system is None:
        return ""
    if isinstance(system, str):
        return system
    # List of content blocks — concatenate text blocks
    parts = []
    for block in system:
        if isinstance(block, dict) and block.get("type") == "text":
            parts.append(block.get("text", ""))
    return "\n".join(parts)


def anthropic_to_openai_request(body: dict, target_model: str) -> dict:
    """Translate an Anthropic Messages request body to OpenAI chat completions format.

    Returns a new dict suitable for posting to an Ollama OpenAI-compat endpoint
    at /v1/chat/completions.
    """
    messages: list = []

    # System prompt → first OpenAI message
    system_text = _anthropic_system_to_openai(body.get("system"))
    if system_text:
        messages.append({"role": "system", "content": system_text})

    # Anthropic messages → OpenAI messages
    for msg in body.get("messages", []):
        role = msg.get("role", "user")
        content = msg.get("content", "")

        if role == "assistant":
            # Check for tool_use blocks — these become tool_calls on the assistant turn
            content_list = content if isinstance(content, list) else []
            tool_calls = []
            text_parts = []

            for block in content_list:
                if not isinstance(block, dict):
                    continue
                if block.get("type") == "tool_use":
                    tool_calls.append(
                        {
                            "id": block.get("id", f"call_{_random_msg_id()}"),
                            "type": "function",
                            "function": {
                                "name": block.get("name", ""),
                                "arguments": json.dumps(block.get("input", {})),
                            },
                        }
                    )
                elif block.get("type") == "text":
                    text_parts.append(block.get("text", ""))

            oai_msg: dict = {"role": "assistant"}
            if text_parts:
                oai_msg["content"] = "\n".join(text_parts)
            else:
                oai_msg["content"] = None
            if tool_calls:
                oai_msg["tool_calls"] = tool_calls
            messages.append(oai_msg)

        elif role == "user":
            # Check for tool_result blocks — these become separate tool-role messages
            content_list = content if isinstance(content, list) else []
            has_tool_result = any(
                isinstance(b, dict) and b.get("type") == "tool_result" for b in content_list
            )

            if has_tool_result:
                for block in content_list:
                    if not isinstance(block, dict):
                        continue
                    if block.get("type") == "tool_result":
                        tool_content = block.get("content", "")
                        if isinstance(tool_content, list):
                            # Flatten content blocks to plain text
                            tool_content = "".join(
                                b.get("text", "")
                                for b in tool_content
                                if isinstance(b, dict) and b.get("type") == "text"
                            )
                        messages.append(
                            {
                                "role": "tool",
                                "tool_call_id": block.get("tool_use_id", ""),
                                "content": tool_content or "",
                            }
                        )
            else:
                oai_content = _anthropic_content_to_openai(content)
                messages.append({"role": "user", "content": oai_content})
        else:
            # Unexpected role — pass through as-is
            messages.append({"role": role, "content": _anthropic_content_to_openai(content)})

    openai_req: dict = {
        "model": target_model,
        "messages": messages,
    }

    # Forward optional fields
    for field in ("max_tokens", "temperature", "top_p", "stop", "stream", "n"):
        if field in body:
            openai_req[field] = body[field]

    # Tools: Anthropic tool definitions → OpenAI function definitions
    if "tools" in body and body["tools"]:
        openai_req["tools"] = [
            {
                "type": "function",
                "function": {
                    "name": t.get("name", ""),
                    "description": t.get("description", ""),
                    "parameters": t.get("input_schema", {}),
                },
            }
            for t in body["tools"]
            if isinstance(t, dict)
        ]

    # tool_choice: Anthropic "auto"/"any"/{type:"tool",name:N} → OpenAI "auto"/"required"/{type:"function",function:{name:N}}
    tc = body.get("tool_choice")
    if tc:
        if isinstance(tc, str):
            openai_req["tool_choice"] = "auto" if tc == "auto" else "required"
        elif isinstance(tc, dict) and tc.get("type") == "tool":
            openai_req["tool_choice"] = {
                "type": "function",
                "function": {"name": tc.get("name", "")},
            }
        else:
            openai_req["tool_choice"] = "auto"

    return openai_req


# ---------------------------------------------------------------------------
# Request: OpenAI → Anthropic  (hermes v0.16.0 sends /chat/completions for Claude)
# ---------------------------------------------------------------------------


def openai_to_anthropic_request(body: dict, target_model: str | None = None) -> dict:
    """Translate an OpenAI /v1/chat/completions request body to Anthropic /v1/messages.

    Minimal coverage for hermes v0.16.0 cron jobs (text-only, no tools, no
    streaming SSE — buffered responses only).  Strips the OpenAI "system"
    role messages out of the messages array and puts the joined text in
    Anthropic's top-level `system` field.
    """
    out: dict = {
        "model": target_model or body.get("model", ""),
        "max_tokens": body.get("max_tokens", 1024),
    }
    if "temperature" in body:
        out["temperature"] = body["temperature"]
    if "top_p" in body:
        out["top_p"] = body["top_p"]
    if "stop" in body and body["stop"]:
        out["stop_sequences"] = (
            [body["stop"]] if isinstance(body["stop"], str) else list(body["stop"])
        )
    system_parts: list[str] = []
    messages: list[dict] = []
    for m in body.get("messages", []) or []:
        role = m.get("role")
        content = m.get("content", "")
        if role == "system":
            if isinstance(content, str):
                system_parts.append(content)
            elif isinstance(content, list):
                for c in content:
                    if isinstance(c, dict) and c.get("type") == "text":
                        system_parts.append(c.get("text", ""))
            continue
        if role not in ("user", "assistant"):
            continue
        if isinstance(content, list):
            messages.append({"role": role, "content": content})
        else:
            messages.append({"role": role, "content": str(content)})
    if system_parts:
        out["system"] = "\n\n".join(p for p in system_parts if p)
    out["messages"] = messages
    return out


# ---------------------------------------------------------------------------
# Response: Anthropic → OpenAI  (hermes's OpenAI client expects this shape)
# ---------------------------------------------------------------------------


def anthropic_to_openai_response(
    anthropic_resp: dict, original_model: str | None = None
) -> dict:
    """Anthropic /v1/messages response → OpenAI /v1/chat/completions envelope."""
    content_blocks = anthropic_resp.get("content", []) or []
    text_parts = [
        b.get("text", "")
        for b in content_blocks
        if isinstance(b, dict) and b.get("type") == "text"
    ]
    tool_calls = [
        {
            "id": b.get("id") or f"call_{_random_msg_id()}",
            "type": "function",
            "function": {
                "name": b.get("name", ""),
                "arguments": json.dumps(b.get("input", {})),
            },
        }
        for b in content_blocks
        if isinstance(b, dict) and b.get("type") == "tool_use"
    ]
    message: dict = {"role": "assistant", "content": "\n".join(text_parts)}
    if tool_calls:
        message["tool_calls"] = tool_calls
    usage = anthropic_resp.get("usage", {}) or {}
    stop_map = {
        "end_turn": "stop",
        "max_tokens": "length",
        "stop_sequence": "stop",
        "tool_use": "tool_calls",
    }
    return {
        "id": anthropic_resp.get("id") or f"chatcmpl_{_random_msg_id()}",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": original_model or anthropic_resp.get("model", ""),
        "choices": [
            {
                "index": 0,
                "message": message,
                "finish_reason": stop_map.get(anthropic_resp.get("stop_reason") or "", "stop"),
            }
        ],
        "usage": {
            "prompt_tokens": usage.get("input_tokens", 0),
            "completion_tokens": usage.get("output_tokens", 0),
            "total_tokens": usage.get("input_tokens", 0) + usage.get("output_tokens", 0),
        },
    }


# ---------------------------------------------------------------------------
# Response: OpenAI → Anthropic
# ---------------------------------------------------------------------------


def openai_to_anthropic_response(openai_resp: dict, original_model: str) -> dict:
    """Translate an Ollama OpenAI-compat response to Anthropic Messages API format.

    The returned dict will be accepted by any client that speaks the Anthropic
    Messages API, making the failover transparent.
    """
    choice = {}
    choices = openai_resp.get("choices", [])
    if choices:
        choice = choices[0]

    message = choice.get("message", {})
    text = message.get("content") or ""
    finish_reason = choice.get("finish_reason", "stop")
    stop_reason = _FINISH_REASON_TO_STOP_REASON.get(finish_reason, "end_turn")

    # Build Anthropic content blocks
    content_blocks: list = []
    if text:
        content_blocks.append({"type": "text", "text": text})

    # tool_calls → Anthropic tool_use blocks
    for tc in message.get("tool_calls") or []:
        fn = tc.get("function", {})
        try:
            fn_input = json.loads(fn.get("arguments", "{}"))
        except (json.JSONDecodeError, TypeError):
            fn_input = {}
        content_blocks.append(
            {
                "type": "tool_use",
                "id": tc.get("id", f"toolu_{_random_msg_id()}"),
                "name": fn.get("name", ""),
                "input": fn_input,
            }
        )

    # Usage
    usage_raw = openai_resp.get("usage", {})
    usage = {
        "input_tokens": usage_raw.get("prompt_tokens", 0),
        "output_tokens": usage_raw.get("completion_tokens", 0),
    }

    return {
        "id": openai_resp.get("id") or _random_msg_id(),
        "type": "message",
        "role": "assistant",
        "content": content_blocks,
        "model": original_model,
        "stop_reason": stop_reason,
        "stop_sequence": None,
        "usage": usage,
    }
