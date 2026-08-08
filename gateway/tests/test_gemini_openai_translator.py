# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for gateway/proxy/gemini_openai_translator.py."""

from __future__ import annotations

from gateway.proxy.gemini_openai_translator import (
    gemini_failover_unsupported_reason,
    gemini_to_openai_request,
    gemini_to_openai_response,
    openai_to_gemini_request,
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


# ---------------------------------------------------------------------------
# openai_to_gemini_request — inverse direction, "use Gemini" voice path
# ---------------------------------------------------------------------------


def test_openai_to_gemini_basic_request():
    body = {
        "model": "gemini-2.5-flash",
        "messages": [
            {"role": "system", "content": "You are concise."},
            {"role": "user", "content": "hello"},
        ],
        "max_tokens": 50,
        "temperature": 0.2,
    }
    result = openai_to_gemini_request(body)
    assert result["systemInstruction"] == {"parts": [{"text": "You are concise."}]}
    assert result["contents"] == [{"role": "user", "parts": [{"text": "hello"}]}]
    assert result["generationConfig"]["maxOutputTokens"] == 50
    assert result["generationConfig"]["temperature"] == 0.2


def test_openai_to_gemini_assistant_role_becomes_model():
    body = {
        "messages": [
            {"role": "user", "content": "hi"},
            {"role": "assistant", "content": "hello there"},
        ],
    }
    result = openai_to_gemini_request(body)
    assert result["contents"] == [
        {"role": "user", "parts": [{"text": "hi"}]},
        {"role": "model", "parts": [{"text": "hello there"}]},
    ]


def test_openai_to_gemini_no_system_message_omits_system_instruction():
    body = {"messages": [{"role": "user", "content": "hi"}]}
    result = openai_to_gemini_request(body)
    assert "systemInstruction" not in result


def test_openai_to_gemini_content_block_list_flattened():
    body = {
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "part one"},
                    {"type": "text", "text": "part two"},
                ],
            }
        ],
    }
    result = openai_to_gemini_request(body)
    assert result["contents"][0]["parts"] == [
        {"text": "part one"},
        {"text": "part two"},
    ]


def test_openai_to_gemini_stop_sequences_normalized_to_list():
    body = {"messages": [{"role": "user", "content": "hi"}], "stop": "END"}
    result = openai_to_gemini_request(body)
    assert result["generationConfig"]["stopSequences"] == ["END"]


def test_openai_to_gemini_no_generation_config_keys_omits_block():
    body = {"messages": [{"role": "user", "content": "hi"}]}
    result = openai_to_gemini_request(body)
    assert "generationConfig" not in result


# ---------------------------------------------------------------------------
# gemini_to_openai_response — inverse direction, "use Gemini" voice path
# ---------------------------------------------------------------------------


def test_gemini_to_openai_response_envelope():
    gem = {
        "candidates": [
            {
                "content": {"parts": [{"text": "Hello!"}], "role": "model"},
                "finishReason": "STOP",
                "index": 0,
            }
        ],
        "usageMetadata": {"promptTokenCount": 5, "candidatesTokenCount": 3},
    }
    out = gemini_to_openai_response(gem, original_model="gemini-2.5-flash")
    assert out["object"] == "chat.completion"
    assert out["model"] == "gemini-2.5-flash"
    assert out["choices"][0]["message"]["content"] == "Hello!"
    assert out["choices"][0]["message"]["role"] == "assistant"
    assert out["choices"][0]["finish_reason"] == "stop"
    assert out["usage"]["total_tokens"] == 8


def test_gemini_to_openai_response_max_tokens_finish_reason():
    gem = {
        "candidates": [{"content": {"parts": [{"text": "cut off"}]}, "finishReason": "MAX_TOKENS"}],
    }
    out = gemini_to_openai_response(gem, original_model="gemini-2.5-flash")
    assert out["choices"][0]["finish_reason"] == "length"


def test_gemini_to_openai_response_empty_candidates_yields_empty_text():
    out = gemini_to_openai_response({}, original_model="gemini-2.5-flash")
    assert out["choices"][0]["message"]["content"] == ""
    assert out["usage"]["total_tokens"] == 0


def test_gemini_to_openai_roundtrip_with_openai_to_gemini_response():
    """openai_to_gemini_response (existing failover direction) and
    gemini_to_openai_response (new direct-voice direction) must be true
    inverses on a representative response, so failover-then-direct-call
    sequences produce consistent shapes."""
    original_openai = {
        "choices": [{"message": {"content": "round trip"}, "finish_reason": "stop"}],
        "usage": {"prompt_tokens": 2, "completion_tokens": 2},
        "model": "gemini-2.5-flash",
    }
    gem = openai_to_gemini_response(original_openai)
    back = gemini_to_openai_response(gem, original_model="gemini-2.5-flash")
    assert back["choices"][0]["message"]["content"] == "round trip"
    assert back["choices"][0]["finish_reason"] == "stop"
