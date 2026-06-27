# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for gateway/proxy/anthropic_openai_translator.py and
gateway/proxy/anthropic_openai_sse_translator.py."""

from __future__ import annotations

import asyncio
import json
from typing import AsyncIterator

import pytest

from gateway.proxy.anthropic_openai_sse_translator import translate_openai_sse_to_anthropic
from gateway.proxy.anthropic_openai_translator import (
    anthropic_to_openai_request,
    openai_to_anthropic_response,
)

# ---------------------------------------------------------------------------
# anthropic_to_openai_request
# ---------------------------------------------------------------------------


def test_translator_basic_text_message():
    body = {
        "model": "claude-opus-4-6",
        "system": "You are concise.",
        "messages": [{"role": "user", "content": "hello"}],
        "max_tokens": 50,
    }
    result = anthropic_to_openai_request(body, "qwen3:14b")
    assert result["model"] == "qwen3:14b"
    assert result["max_tokens"] == 50
    msgs = result["messages"]
    assert msgs[0] == {"role": "system", "content": "You are concise."}
    assert msgs[1] == {"role": "user", "content": "hello"}


def test_translator_system_block_list():
    body = {
        "model": "claude-opus-4-6",
        "system": [{"type": "text", "text": "Part A"}, {"type": "text", "text": "Part B"}],
        "messages": [{"role": "user", "content": "hi"}],
    }
    result = anthropic_to_openai_request(body, "qwen3:14b")
    system_msg = result["messages"][0]
    assert system_msg["role"] == "system"
    assert "Part A" in system_msg["content"]
    assert "Part B" in system_msg["content"]


def test_translator_tool_use_blocks():
    body = {
        "model": "claude-opus-4-6",
        "messages": [
            {
                "role": "assistant",
                "content": [
                    {"type": "text", "text": "I'll call the tool."},
                    {
                        "type": "tool_use",
                        "id": "toolu_abc",
                        "name": "get_weather",
                        "input": {"city": "NY"},
                    },
                ],
            }
        ],
    }
    result = anthropic_to_openai_request(body, "qwen3:14b")
    asst_msg = result["messages"][0]
    assert asst_msg["role"] == "assistant"
    assert asst_msg.get("tool_calls") is not None
    tc = asst_msg["tool_calls"][0]
    assert tc["type"] == "function"
    assert tc["function"]["name"] == "get_weather"
    assert json.loads(tc["function"]["arguments"])["city"] == "NY"
    assert asst_msg.get("content") == "I'll call the tool."


def test_translator_tool_result_becomes_tool_role_message():
    body = {
        "model": "claude-opus-4-6",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "tool_result",
                        "tool_use_id": "toolu_abc",
                        "content": "72°F and sunny",
                    }
                ],
            }
        ],
    }
    result = anthropic_to_openai_request(body, "qwen3:14b")
    msgs = result["messages"]
    tool_msg = next(m for m in msgs if m["role"] == "tool")
    assert tool_msg["tool_call_id"] == "toolu_abc"
    assert tool_msg["content"] == "72°F and sunny"


def test_translator_anthropic_tool_definitions():
    body = {
        "model": "claude-opus-4-6",
        "messages": [{"role": "user", "content": "check weather"}],
        "tools": [
            {
                "name": "get_weather",
                "description": "Get the weather",
                "input_schema": {
                    "type": "object",
                    "properties": {"city": {"type": "string"}},
                    "required": ["city"],
                },
            }
        ],
    }
    result = anthropic_to_openai_request(body, "qwen3:14b")
    assert "tools" in result
    fn = result["tools"][0]
    assert fn["type"] == "function"
    assert fn["function"]["name"] == "get_weather"
    assert "city" in fn["function"]["parameters"]["properties"]


def test_translator_no_system_prompt():
    body = {
        "model": "claude-opus-4-6",
        "messages": [{"role": "user", "content": "ping"}],
    }
    result = anthropic_to_openai_request(body, "qwen3:14b")
    assert result["messages"][0]["role"] == "user"  # no system prepended


# ---------------------------------------------------------------------------
# openai_to_anthropic_response
# ---------------------------------------------------------------------------


def test_translator_openai_to_anthropic_basic():
    openai_resp = {
        "id": "chatcmpl-abc",
        "choices": [
            {
                "index": 0,
                "message": {"role": "assistant", "content": "Hello!"},
                "finish_reason": "stop",
            }
        ],
        "usage": {"prompt_tokens": 10, "completion_tokens": 5},
    }
    result = openai_to_anthropic_response(openai_resp, "claude-opus-4-6")
    assert result["type"] == "message"
    assert result["role"] == "assistant"
    assert result["model"] == "claude-opus-4-6"
    assert result["stop_reason"] == "end_turn"
    assert result["content"][0]["type"] == "text"
    assert result["content"][0]["text"] == "Hello!"
    assert result["usage"]["input_tokens"] == 10
    assert result["usage"]["output_tokens"] == 5


def test_translator_preserves_original_model():
    openai_resp = {
        "choices": [{"message": {"role": "assistant", "content": "hi"}, "finish_reason": "stop"}],
        "usage": {},
    }
    result = openai_to_anthropic_response(openai_resp, "claude-opus-4-6")
    assert result["model"] == "claude-opus-4-6"


def test_translator_tool_calls_to_tool_use():
    openai_resp = {
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": None,
                    "tool_calls": [
                        {
                            "id": "call_xyz",
                            "type": "function",
                            "function": {
                                "name": "get_weather",
                                "arguments": '{"city": "NY"}',
                            },
                        }
                    ],
                },
                "finish_reason": "tool_calls",
            }
        ],
        "usage": {"prompt_tokens": 20, "completion_tokens": 15},
    }
    result = openai_to_anthropic_response(openai_resp, "claude-opus-4-6")
    assert result["stop_reason"] == "tool_use"
    tool_block = result["content"][0]
    assert tool_block["type"] == "tool_use"
    assert tool_block["id"] == "call_xyz"
    assert tool_block["name"] == "get_weather"
    assert tool_block["input"]["city"] == "NY"


def test_translator_max_tokens_finish_reason():
    openai_resp = {
        "choices": [{"message": {"content": "..."}, "finish_reason": "length"}],
        "usage": {},
    }
    result = openai_to_anthropic_response(openai_resp, "claude-opus-4-6")
    assert result["stop_reason"] == "max_tokens"


# ---------------------------------------------------------------------------
# translate_openai_sse_to_anthropic (streaming)
# ---------------------------------------------------------------------------


async def _collect_sse(chunks: list[bytes]) -> list[dict]:
    """Feed raw SSE bytes into the translator and collect Anthropic events."""

    async def source() -> AsyncIterator[bytes]:
        for chunk in chunks:
            yield chunk

    events = []
    async for raw in translate_openai_sse_to_anthropic(source(), "claude-opus-4-6"):
        for line in raw.decode().split("\n"):
            if line.startswith("data: "):
                try:
                    events.append(json.loads(line[6:]))
                except json.JSONDecodeError:
                    pass
    return events


def test_sse_translator_basic_text_stream():
    chunks = [
        b'data: {"choices":[{"delta":{"content":"Hello"},"finish_reason":null}]}\n',
        b'data: {"choices":[{"delta":{"content":" world"},"finish_reason":"stop"}]}\n',
        b"data: [DONE]\n",
    ]
    events = asyncio.run(_collect_sse(chunks))
    event_types = [e.get("type") for e in events]
    assert "message_start" in event_types
    assert "content_block_start" in event_types
    assert "content_block_delta" in event_types
    assert "content_block_stop" in event_types
    assert "message_delta" in event_types
    assert "message_stop" in event_types

    deltas = [e for e in events if e.get("type") == "content_block_delta"]
    combined_text = "".join(d["delta"]["text"] for d in deltas)
    assert combined_text == "Hello world"


def test_sse_translator_model_preserved_in_message_start():
    chunks = [
        b'data: {"choices":[{"delta":{"content":"hi"},"finish_reason":"stop"}]}\n',
        b"data: [DONE]\n",
    ]
    events = asyncio.run(_collect_sse(chunks))
    start = next(e for e in events if e.get("type") == "message_start")
    assert start["message"]["model"] == "claude-opus-4-6"


def test_sse_translator_stop_reason_propagated():
    chunks = [
        b'data: {"choices":[{"delta":{"content":"x"},"finish_reason":"length"}]}\n',
        b"data: [DONE]\n",
    ]
    events = asyncio.run(_collect_sse(chunks))
    delta_evt = next(e for e in events if e.get("type") == "message_delta")
    assert delta_evt["delta"]["stop_reason"] == "max_tokens"


def test_sse_translator_empty_stream_emits_full_sequence():
    chunks = [b"data: [DONE]\n"]
    events = asyncio.run(_collect_sse(chunks))
    event_types = {e.get("type") for e in events}
    assert "message_start" in event_types
    assert "message_stop" in event_types


# ---------------------------------------------------------------------------
# openai_to_anthropic_response — empty-content guard (regression: IndexError)
# ---------------------------------------------------------------------------


def test_translator_null_content_no_tool_calls_yields_nonempty_content():
    """Failover reply with null content and no tool_calls must not return content:[]."""
    openai_resp = {
        "choices": [{"message": {"role": "assistant", "content": None}, "finish_reason": "stop"}],
        "usage": {},
    }
    result = openai_to_anthropic_response(openai_resp, "claude-opus-4-7")
    assert len(result["content"]) >= 1
    assert result["content"][0]["type"] == "text"


def test_translator_empty_string_content_yields_nonempty_content():
    """Failover reply with empty-string content must not return content:[]."""
    openai_resp = {
        "choices": [{"message": {"role": "assistant", "content": ""}, "finish_reason": "stop"}],
        "usage": {},
    }
    result = openai_to_anthropic_response(openai_resp, "claude-opus-4-7")
    assert len(result["content"]) >= 1


def test_translator_empty_choices_yields_nonempty_content():
    """Failover reply with choices:[] (e.g. rate-limit stub) must not return content:[]."""
    openai_resp = {"choices": [], "usage": {}}
    result = openai_to_anthropic_response(openai_resp, "claude-opus-4-7")
    assert len(result["content"]) >= 1
    assert result["content"][0]["type"] == "text"


# ---------------------------------------------------------------------------
# SSE translator — tool-call-only index offset (regression: gap at index 0)
# ---------------------------------------------------------------------------


def test_sse_translator_tool_call_only_starts_at_index_0():
    """Tool-call-only SSE stream must produce tool_use at index 0 (no text gap)."""
    chunks = [
        b'data: {"choices":[{"delta":{"tool_calls":[{"index":0,"id":"call_1","type":"function","function":{"name":"get_weather","arguments":""}}]},"finish_reason":null}]}\n',
        b'data: {"choices":[{"delta":{"tool_calls":[{"index":0,"function":{"arguments":"{\\"city\\":\\"NY\\"}"}}]},"finish_reason":"tool_calls"}]}\n',
        b"data: [DONE]\n",
    ]
    events = asyncio.run(_collect_sse(chunks))
    starts = [e for e in events if e.get("type") == "content_block_start"]
    tool_start = next((e for e in starts if e.get("content_block", {}).get("type") == "tool_use"), None)
    assert tool_start is not None, "no tool_use content_block_start found"
    assert tool_start["index"] == 0, f"tool_use should start at index 0, got {tool_start['index']}"
