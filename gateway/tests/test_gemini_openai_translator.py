# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for gateway/proxy/gemini_openai_translator.py."""

from __future__ import annotations

from gateway.proxy.gemini_openai_translator import (
    gemini_failover_unsupported_reason,
    gemini_to_openai_request,
    openai_to_gemini_response,
)

# ---------------------------------------------------------------------------
# gemini_to_openai_request
# ---------------------------------------------------------------------------


def test_gemini_basic_text_request():
    body = {
        "systemInstruction": {"parts": [{"text": "You are concise."}]},
        "contents": [{"role": "user", "parts": [{"text": "hello"}]}],
        "generationConfig": {"maxOutputTokens": 50, "temperature": 0.2},
    }
    result = gemini_to_openai_request(body, "qwen3:14b")
    assert result["model"] == "qwen3:14b"
    assert result["max_tokens"] == 50
    assert result["temperature"] == 0.2
    msgs = result["messages"]
    assert msgs[0] == {"role": "system", "content": "You are concise."}
    assert msgs[1] == {"role": "user", "content": "hello"}


def test_gemini_multi_part_contents_joined():
    body = {
        "contents": [
            {"role": "user", "parts": [{"text": "part one"}, {"text": "part two"}]},
        ],
    }
    result = gemini_to_openai_request(body, "qwen3:14b")
    assert result["messages"] == [{"role": "user", "content": "part one\npart two"}]


def test_gemini_missing_system_instruction_omits_system_message():
    body = {"contents": [{"role": "user", "parts": [{"text": "hi"}]}]}
    result = gemini_to_openai_request(body, "qwen3:14b")
    assert all(m["role"] != "system" for m in result["messages"])
    assert result["messages"][0] == {"role": "user", "content": "hi"}


def test_gemini_role_mapping_model_to_assistant():
    body = {
        "contents": [
            {"role": "user", "parts": [{"text": "q1"}]},
            {"role": "model", "parts": [{"text": "a1"}]},
            {"role": "user", "parts": [{"text": "q2"}]},
        ],
    }
    result = gemini_to_openai_request(body, "qwen3:14b")
    roles = [m["role"] for m in result["messages"]]
    assert roles == ["user", "assistant", "user"]
    assert result["messages"][1]["content"] == "a1"


def test_gemini_missing_role_defaults_to_user():
    body = {"contents": [{"parts": [{"text": "no role here"}]}]}
    result = gemini_to_openai_request(body, "qwen3:14b")
    assert result["messages"] == [{"role": "user", "content": "no role here"}]


def test_gemini_system_instruction_snake_case_and_string():
    snake = {"system_instruction": {"parts": [{"text": "sys"}]}, "contents": []}
    assert gemini_to_openai_request(snake, "m")["messages"][0]["content"] == "sys"

    as_string = {"systemInstruction": "plain sys", "contents": []}
    assert gemini_to_openai_request(as_string, "m")["messages"][0]["content"] == "plain sys"


def test_gemini_generation_config_top_p_and_stop_sequences():
    body = {
        "contents": [{"role": "user", "parts": [{"text": "hi"}]}],
        "generationConfig": {"topP": 0.9, "stopSequences": ["END"]},
    }
    result = gemini_to_openai_request(body, "m")
    assert result["top_p"] == 0.9
    assert result["stop"] == ["END"]


def test_gemini_non_text_parts_skipped():
    body = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"inlineData": {"mimeType": "image/png", "data": "AAAA"}},
                    {"text": "describe"},
                ],
            }
        ],
    }
    result = gemini_to_openai_request(body, "m")
    assert result["messages"] == [{"role": "user", "content": "describe"}]


# ---------------------------------------------------------------------------
# openai_to_gemini_response
# ---------------------------------------------------------------------------


def test_openai_response_to_gemini_candidates():
    openai_resp = {
        "id": "chatcmpl-1",
        "model": "qwen3:14b",
        "choices": [
            {
                "index": 0,
                "message": {"role": "assistant", "content": "Hello from local!"},
                "finish_reason": "stop",
            }
        ],
        "usage": {"prompt_tokens": 10, "completion_tokens": 5},
    }
    result = openai_to_gemini_response(openai_resp)
    cand = result["candidates"][0]
    assert cand["content"]["parts"] == [{"text": "Hello from local!"}]
    assert cand["content"]["role"] == "model"
    assert cand["finishReason"] == "STOP"
    assert cand["index"] == 0
    usage = result["usageMetadata"]
    assert usage["promptTokenCount"] == 10
    assert usage["candidatesTokenCount"] == 5
    assert usage["totalTokenCount"] == 15
    assert result["modelVersion"] == "qwen3:14b"


def test_openai_response_length_maps_to_max_tokens():
    openai_resp = {
        "choices": [
            {"message": {"role": "assistant", "content": "trunc"}, "finish_reason": "length"}
        ]
    }
    result = openai_to_gemini_response(openai_resp)
    assert result["candidates"][0]["finishReason"] == "MAX_TOKENS"


def test_openai_response_empty_choices_yields_empty_text():
    result = openai_to_gemini_response({"choices": []})
    assert result["candidates"][0]["content"]["parts"] == [{"text": ""}]
    assert result["candidates"][0]["finishReason"] == "STOP"
    assert result["usageMetadata"]["totalTokenCount"] == 0


# ---------------------------------------------------------------------------
# gemini_failover_unsupported_reason
# ---------------------------------------------------------------------------


def test_unsupported_reason_none_for_plain_text():
    body = {"contents": [{"role": "user", "parts": [{"text": "hi"}]}]}
    path = "/v1beta/models/gemini-2.0-flash:generateContent"
    assert gemini_failover_unsupported_reason(body, path) is None


def test_unsupported_reason_streaming_path():
    body = {"contents": [{"role": "user", "parts": [{"text": "hi"}]}]}
    path = "/v1beta/models/gemini-2.0-flash:streamGenerateContent?alt=sse"
    assert gemini_failover_unsupported_reason(body, path) is not None


def test_unsupported_reason_tools_in_body():
    body = {
        "contents": [{"role": "user", "parts": [{"text": "hi"}]}],
        "tools": [{"functionDeclarations": [{"name": "get_weather"}]}],
    }
    path = "/v1beta/models/gemini-2.0-flash:generateContent"
    assert gemini_failover_unsupported_reason(body, path) is not None


def test_unsupported_reason_function_call_parts():
    body = {
        "contents": [
            {"role": "model", "parts": [{"functionCall": {"name": "f", "args": {}}}]},
        ],
    }
    path = "/v1beta/models/gemini-2.0-flash:generateContent"
    assert gemini_failover_unsupported_reason(body, path) is not None
