# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""
OpenAI-compat SSE stream → Anthropic SSE stream translator.

Consumes an async iterator of raw bytes from an Ollama /v1/chat/completions
streaming response and re-emits Anthropic-format SSE events so the receiving
client (OpenClaw / any Anthropic SDK consumer) never knows it's talking to a
local model during cloud quota failover.

Anthropic SSE event sequence emitted:
  message_start
  content_block_start  (index 0, type "text")
  content_block_delta* (type "text_delta" per OpenAI delta chunk)
  content_block_stop   (index 0)
  message_delta        (stop_reason, usage)
  message_stop

Tool-call streaming is also handled:
  content_block_start  (index N, type "tool_use")
  content_block_delta* (type "input_json_delta" per arguments chunk)
  content_block_stop   (index N)
"""

from __future__ import annotations

import json
import logging
import random
import string
from collections.abc import AsyncIterator

logger = logging.getLogger("agentshroud.proxy.anthropic_openai_sse_translator")


def _random_msg_id() -> str:
    chars = string.ascii_lowercase + string.digits
    return "msg_local_" + "".join(random.choices(chars, k=8))


def _sse(event: str, data: dict) -> bytes:
    return f"event: {event}\ndata: {json.dumps(data)}\n\n".encode()


_FINISH_REASON_TO_STOP_REASON = {
    "stop": "end_turn",
    "length": "max_tokens",
    "tool_calls": "tool_use",
    "content_filter": "stop_sequence",
}


async def translate_openai_sse_to_anthropic(
    source: AsyncIterator[bytes],
    original_model: str,
) -> AsyncIterator[bytes]:
    """Translate an OpenAI-compat SSE byte stream to Anthropic SSE byte events.

    Yields Anthropic-format SSE bytes. All yields are complete SSE blocks
    (event + data + double-newline) that can be forwarded byte-for-byte to the
    client.
    """
    msg_id = _random_msg_id()
    # Track state for multi-chunk assembly
    text_started = False
    tool_call_blocks: dict[int, dict] = {}  # oai_index → {id, name, args_buf}
    output_token_count = 0
    finish_reason: str | None = None

    # Emit message_start
    yield _sse(
        "message_start",
        {
            "type": "message_start",
            "message": {
                "id": msg_id,
                "type": "message",
                "role": "assistant",
                "model": original_model,
                "content": [],
                "stop_reason": None,
                "stop_sequence": None,
                "usage": {"input_tokens": 0, "output_tokens": 0},
            },
        },
    )

    # Anthropic clients expect a ping to follow message_start
    yield b'event: ping\ndata: {"type":"ping"}\n\n'

    buf = b""

    async for chunk in source:
        buf += chunk
        while b"\n" in buf:
            line, buf = buf.split(b"\n", 1)
            line = line.rstrip(b"\r")
            if not line.startswith(b"data: "):
                continue
            payload = line[6:]
            if payload.strip() == b"[DONE]":
                continue
            try:
                event = json.loads(payload)
            except json.JSONDecodeError:
                logger.debug("translate_openai_sse: could not parse payload: %s", payload[:100])
                continue

            choices = event.get("choices", [])
            usage_update = event.get("usage")

            for choice in choices:
                delta = choice.get("delta", {})
                text_delta = delta.get("content")
                fr = choice.get("finish_reason")
                if fr:
                    finish_reason = fr

                # ---- text delta ----
                if text_delta is not None and text_delta != "":
                    if not text_started:
                        text_started = True
                        yield _sse(
                            "content_block_start",
                            {
                                "type": "content_block_start",
                                "index": 0,
                                "content_block": {"type": "text", "text": ""},
                            },
                        )
                    yield _sse(
                        "content_block_delta",
                        {
                            "type": "content_block_delta",
                            "index": 0,
                            "delta": {"type": "text_delta", "text": text_delta},
                        },
                    )

                # ---- tool_calls deltas ----
                for tc_delta in delta.get("tool_calls") or []:
                    idx = tc_delta.get("index", 0)
                    # Anthropic content block index: text gets 0, each tool gets idx+1
                    anthr_idx = idx + 1

                    if idx not in tool_call_blocks:
                        # Start of a new tool_use block
                        tool_call_blocks[idx] = {
                            "id": tc_delta.get("id", f"toolu_{_random_msg_id()}"),
                            "name": (tc_delta.get("function") or {}).get("name", ""),
                            "args_buf": "",
                        }
                        yield _sse(
                            "content_block_start",
                            {
                                "type": "content_block_start",
                                "index": anthr_idx,
                                "content_block": {
                                    "type": "tool_use",
                                    "id": tool_call_blocks[idx]["id"],
                                    "name": tool_call_blocks[idx]["name"],
                                    "input": {},
                                },
                            },
                        )
                    else:
                        # Name can arrive in later chunks too
                        fn = tc_delta.get("function") or {}
                        if fn.get("name"):
                            tool_call_blocks[idx]["name"] += fn["name"]

                    # arguments chunk
                    args_chunk = (tc_delta.get("function") or {}).get("arguments", "")
                    if args_chunk:
                        tool_call_blocks[idx]["args_buf"] += args_chunk
                        yield _sse(
                            "content_block_delta",
                            {
                                "type": "content_block_delta",
                                "index": anthr_idx,
                                "delta": {"type": "input_json_delta", "partial_json": args_chunk},
                            },
                        )

            if usage_update:
                output_token_count = usage_update.get("completion_tokens", output_token_count)

    # Close text block
    if text_started:
        yield _sse("content_block_stop", {"type": "content_block_stop", "index": 0})

    # Close tool_use blocks
    for idx in sorted(tool_call_blocks.keys()):
        anthr_idx = idx + 1
        yield _sse("content_block_stop", {"type": "content_block_stop", "index": anthr_idx})

    stop_reason = _FINISH_REASON_TO_STOP_REASON.get(finish_reason or "stop", "end_turn")

    yield _sse(
        "message_delta",
        {
            "type": "message_delta",
            "delta": {"stop_reason": stop_reason, "stop_sequence": None},
            "usage": {"output_tokens": output_token_count},
        },
    )

    yield _sse("message_stop", {"type": "message_stop"})
