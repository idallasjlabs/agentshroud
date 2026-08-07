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


def _openai_content_to_parts(content: str | list) -> list[dict]:
    """Flatten an OpenAI message's content (string or content-block list) to
    Gemini parts (text only — image/tool blocks are dropped with a warning,
    same scope limit as gemini_failover_unsupported_reason: text-only)."""
    if isinstance(content, str):
        return [{"text": content}] if content else []
    parts: list[dict] = []
    for block in content or []:
        if isinstance(block, dict) and block.get("type") == "text":
            parts.append({"text": block.get("text", "")})
        elif isinstance(block, dict):
            logger.warning(
                "openai_to_gemini: unsupported content block type %r — skipping",
                block.get("type"),
            )
    return parts


_OPENAI_ROLE_TO_GEMINI: dict[str, str] = {
    "user": "user",
    "assistant": "model",
}


def openai_to_gemini_request(body: dict) -> dict:
    """Translate an OpenAI chat/completions request body to Gemini's
    generateContent shape.

    Inverse of gemini_to_openai_request — used for the "use Gemini" direct
    voice path (gateway/proxy/llm_proxy.py): a caller speaking OpenAI's
    format wants a real Gemini reply. Text-only, non-streaming (matches this
    module's existing scope limit); system messages become systemInstruction,
    "assistant" turns become Gemini's "model" role. No target_model param —
    unlike OpenAI/Anthropic, Gemini's REST API takes the model from the URL
    path (/v1beta/models/{model}:generateContent), not the request body; the
    caller builds that path from the original model name.
    """
    contents: list[dict] = []
    system_parts: list[str] = []

    for message in body.get("messages") or []:
        if not isinstance(message, dict):
            continue
        role = message.get("role", "user")
        if role == "system":
            text = message.get("content", "")
            if isinstance(text, str) and text:
                system_parts.append(text)
            continue
        gemini_role = _OPENAI_ROLE_TO_GEMINI.get(role, "user")
        contents.append(
            {"role": gemini_role, "parts": _openai_content_to_parts(message.get("content", ""))}
        )

    gemini_req: dict = {"contents": contents}
    if system_parts:
        gemini_req["systemInstruction"] = {"parts": [{"text": "\n".join(system_parts)}]}

    gen_cfg: dict = {}
    if "max_tokens" in body:
        gen_cfg["maxOutputTokens"] = body["max_tokens"]
    if "temperature" in body:
        gen_cfg["temperature"] = body["temperature"]
    if "top_p" in body:
        gen_cfg["topP"] = body["top_p"]
    if "stop" in body:
        stop = body["stop"]
        gen_cfg["stopSequences"] = stop if isinstance(stop, list) else [stop]
    if gen_cfg:
        gemini_req["generationConfig"] = gen_cfg

    return gemini_req


def gemini_to_openai_response(gemini_resp: dict, original_model: str) -> dict:
    """Translate a Gemini generateContent response to OpenAI chat/completions
    shape.

    Inverse of openai_to_gemini_response. original_model is echoed back in
    the "model" field so the caller's own model-name bookkeeping (e.g.
    voice_gateway logging which model answered) stays consistent.
    """
    candidates = gemini_resp.get("candidates") or []
    candidate = candidates[0] if candidates and isinstance(candidates[0], dict) else {}
    text = _parts_to_text((candidate.get("content") or {}).get("parts"))
    finish_reason_gemini = candidate.get("finishReason", "STOP")
    finish_reason = "stop" if finish_reason_gemini == "STOP" else "length"

    usage = gemini_resp.get("usageMetadata") or {}
    prompt_tokens = usage.get("promptTokenCount", 0)
    completion_tokens = usage.get("candidatesTokenCount", 0)

    return {
        "id": "gemini-" + str(abs(hash(text)))[:12],
        "object": "chat.completion",
        "model": original_model,
        "choices": [
            {
                "index": 0,
                "message": {"role": "assistant", "content": text},
                "finish_reason": finish_reason,
            }
        ],
        "usage": {
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": prompt_tokens + completion_tokens,
        },
    }


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
