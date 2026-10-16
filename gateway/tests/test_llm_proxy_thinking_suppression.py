# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Regression tests for LLMProxy._suppress_qwen3_thinking.

2026-10-16 incident: the '/no_think' suffix (Qwen3-only) was appended to every
Rapid-MLX request regardless of model. After the anchor moved to NVIDIA
Nemotron 3.5, the model treated the suffix as literal user text, reasoned in-band
until max_tokens, and every Hermes/OpenClaw Telegram reply stalled. Non-Qwen
models must get `reasoning_effort: "none"` instead, with the text untouched.
"""

from gateway.proxy.llm_proxy import LLMProxy

RAPID_MLX_NEMOTRON_PATH = (
    "/Users/ijefferson.admin/.cache/lm-studio/models/mlx-community/"
    "NVIDIA-Nemotron-3.5-Lightning-30B-A3B-4bit"
)


def _req(model, content="hello"):
    return {"model": model, "messages": [{"role": "user", "content": content}]}


def test_qwen_model_gets_no_think_suffix():
    req = _req("qwen3-14b")
    assert LLMProxy._suppress_qwen3_thinking(req) is True
    assert req["messages"][0]["content"] == "hello /no_think"
    assert "reasoning_effort" not in req


def test_qwen_model_suffix_already_present_is_noop():
    req = _req("qwen3-14b", "hello /no_think")
    assert LLMProxy._suppress_qwen3_thinking(req) is False
    assert req["messages"][0]["content"] == "hello /no_think"


def test_qwen_list_content_gets_suffix_on_last_text_part():
    req = {
        "model": "qwen3-coder-30b-a3b-instruct",
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": "describe"},
            {"type": "image_url", "image_url": {"url": "data:..."}},
        ]}],
    }
    assert LLMProxy._suppress_qwen3_thinking(req) is True
    assert req["messages"][0]["content"][0]["text"] == "describe /no_think"


def test_nemotron_alias_gets_reasoning_effort_none_and_text_untouched():
    req = _req("nemotron-3.5-lightning-rapid")
    assert LLMProxy._suppress_qwen3_thinking(req) is True
    assert req["reasoning_effort"] == "none"
    assert req["messages"][0]["content"] == "hello"
    assert "/no_think" not in req["messages"][0]["content"]


def test_nemotron_normalized_full_path_gets_reasoning_effort_none():
    # _normalize_local_model rewrites the alias to the on-disk model path
    # before suppression runs (llm_proxy.py:88); the gate must not key on the alias.
    req = _req(RAPID_MLX_NEMOTRON_PATH)
    assert LLMProxy._suppress_qwen3_thinking(req) is True
    assert req["reasoning_effort"] == "none"
    assert req["messages"][0]["content"] == "hello"


def test_non_qwen_reasoning_effort_already_none_is_noop():
    req = _req("nemotron-3.5-lightning-rapid")
    req["reasoning_effort"] = "none"
    assert LLMProxy._suppress_qwen3_thinking(req) is False
    assert req["messages"][0]["content"] == "hello"


def test_non_qwen_caller_supplied_effort_is_overridden_to_none():
    # The gateway owns thinking policy for the local anchor: a caller asking
    # for "high" on Nemotron would reintroduce the in-band reasoning stall.
    req = _req("nemotron-3.5-lightning-rapid")
    req["reasoning_effort"] = "high"
    assert LLMProxy._suppress_qwen3_thinking(req) is True
    assert req["reasoning_effort"] == "none"


def test_missing_model_treated_as_non_qwen():
    req = {"messages": [{"role": "user", "content": "hello"}]}
    assert LLMProxy._suppress_qwen3_thinking(req) is True
    assert req["reasoning_effort"] == "none"
    assert req["messages"][0]["content"] == "hello"
