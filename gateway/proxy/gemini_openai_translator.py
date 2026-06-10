# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Google Gemini generateContent API ↔ Ollama OpenAI-compat translator.

Pure functions — no I/O, no side effects. Mirrors anthropic_openai_translator:
used by the LLM failover orchestrator to transparently re-route Gemini-format
requests to a local OpenAI-compatible backend when cloud quota is exhausted.

Scope (this iteration): NON-STREAMING TEXT ONLY. Streaming endpoints
(:streamGenerateContent / alt=sse) and requests carrying tool / function
declarations are reported as unsupported by gemini_failover_unsupported_reason()
and must be passed through unchanged (original cloud 429) by the caller.
"""

from __future__ import annotations

import logging

logger = logging.getLogger("agentshroud.proxy.gemini_openai_translator")

# Gemini roles → OpenAI roles. Gemini uses "user" / "model"; anything unknown
# is treated as "user" so content is never silently dropped.
_GEMINI_ROLE_TO_OPENAI: dict[str, str] = {
    "user": "user",
    "model": "assistant",
}

# OpenAI finish_reason → Gemini finishReason.
_FINISH_REASON_TO_GEMINI: dict[str, str] = {
    "stop": "STOP",
    "length": "MAX_TOKENS",
    "content_filter": "SAFETY",
    "tool_calls": "STOP",
}


# ---------------------------------------------------------------------------
# Capability gate
# ---------------------------------------------------------------------------


def gemini_failover_unsupported_reason(body: dict, path: str) -> str | None:
    """Return a reason string if this Gemini request cannot be failed over.

    Returns None when the request is plain non-streaming text and translation
    is supported. Streaming and tool/function-calling requests are out of scope
    for this iteration.
    """
    if ":streamGenerateContent" in path or "alt=sse" in path:
        return "streaming endpoint"
    if body.get("stream"):
        return "streaming requested"
    if body.get("tools") or body.get("toolConfig") or body.get("tool_config"):
        return "tool/function declarations present"
    for content in body.get("contents") or []:
        if not isinstance(content, dict):
            continue
        for part in content.get("parts") or []:
            if isinstance(part, dict) and ("functionCall" in part or "functionResponse" in part):
                return "function call parts present"
    return None


# ---------------------------------------------------------------------------
# Request: Gemini → OpenAI
# ---------------------------------------------------------------------------


def _parts_to_text(parts: list | None) -> str:
    """Flatten a Gemini parts list to plain text (text parts only)."""
    texts: list[str] = []
    for part in parts or []:
        if isinstance(part, dict) and isinstance(part.get("text"), str):
            texts.append(part["text"])
        elif isinstance(part, dict):
            logger.warning(
                "gemini_to_openai: unsupported part keys %s — skipping",
                sorted(part.keys()),
            )
    return "\n".join(texts)


def _system_instruction_text(body: dict) -> str:
    """Extract the system instruction as plain text (camelCase or snake_case key)."""
    si = body.get("systemInstruction") or body.get("system_instruction")
    if si is None:
        return ""
    if isinstance(si, str):
        return si
    if isinstance(si, dict):
        return _parts_to_text(si.get("parts"))
    return ""


def gemini_to_openai_request(body: dict, target_model: str) -> dict:
    """Translate a Gemini generateContent request body to OpenAI chat format.

    Returns a new dict suitable for posting to an Ollama OpenAI-compat endpoint
    at /v1/chat/completions. Text-only — callers must gate with
    gemini_failover_unsupported_reason() first.
    """
    messages: list[dict] = []

    system_text = _system_instruction_text(body)
    if system_text:
        messages.append({"role": "system", "content": system_text})

    for content in body.get("contents") or []:
        if not isinstance(content, dict):
            continue
        role = _GEMINI_ROLE_TO_OPENAI.get(content.get("role", "user"), "user")
        messages.append({"role": role, "content": _parts_to_text(content.get("parts"))})

    openai_req: dict = {
        "model": target_model,
        "messages": messages,
    }

    gen_cfg = body.get("generationConfig") or body.get("generation_config") or {}
    if isinstance(gen_cfg, dict):
        if "maxOutputTokens" in gen_cfg:
            openai_req["max_tokens"] = gen_cfg["maxOutputTokens"]
        if "temperature" in gen_cfg:
            openai_req["temperature"] = gen_cfg["temperature"]
        if "topP" in gen_cfg:
            openai_req["top_p"] = gen_cfg["topP"]
        if "stopSequences" in gen_cfg:
            openai_req["stop"] = gen_cfg["stopSequences"]

    return openai_req


# ---------------------------------------------------------------------------
# Response: OpenAI → Gemini
# ---------------------------------------------------------------------------


def openai_to_gemini_response(openai_resp: dict) -> dict:
    """Translate an Ollama OpenAI-compat response to Gemini candidates format.

    The returned dict is accepted by clients that speak the Gemini
    generateContent API, making the failover transparent.
    """
    choices = openai_resp.get("choices") or []
    choice = choices[0] if choices and isinstance(choices[0], dict) else {}
    message = choice.get("message") or {}
    text = message.get("content") or ""
    finish = _FINISH_REASON_TO_GEMINI.get(choice.get("finish_reason", "stop"), "STOP")

    usage_raw = openai_resp.get("usage") or {}
    prompt_tokens = usage_raw.get("prompt_tokens", 0)
    completion_tokens = usage_raw.get("completion_tokens", 0)

    return {
        "candidates": [
            {
                "content": {"parts": [{"text": text}], "role": "model"},
                "finishReason": finish,
                "index": 0,
            }
        ],
        "usageMetadata": {
            "promptTokenCount": prompt_tokens,
            "candidatesTokenCount": completion_tokens,
            "totalTokenCount": prompt_tokens + completion_tokens,
        },
        "modelVersion": openai_resp.get("model", ""),
    }
