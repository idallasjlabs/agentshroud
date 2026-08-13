# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""
Workstream C — Full local-model parity for both bots.

Tests that every cloud-mode tool-call shape has a local-mode equivalent,
that local→local-secondary OOM/timeout failover works, and that
ResourceGuard pre-flight VRAM headroom check gates long-context calls.

No real network calls — httpx and urllib are fully mocked.
"""

from __future__ import annotations

import json
from types import SimpleNamespace

import pytest

from gateway.proxy import llm_proxy as llm_proxy_module
from gateway.proxy.llm_proxy import (
    FIELDFLARE_API_BASE,
    LMSTUDIO_API_BASE,
    MLXLM_API_BASE,
    OLLAMA_API_BASE,
    OMLX_API_BASE,
    LLMProxy,
)
from gateway.security.resource_guard import (
    ResourceGuard,
    ResourceLimits,
    VRAMHeadroomError,
)

# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


class _FakeSanitizer:
    async def sanitize(self, text: str):
        return SimpleNamespace(sanitized_content=text, entity_types_found=[], redactions=[])

    def filter_xml_blocks(self, text: str):
        return (text, False)

    async def block_credentials(self, text: str, source: str):
        del source
        return (text, False)


def _make_proxy(**kwargs) -> LLMProxy:
    return LLMProxy(sanitizer=_FakeSanitizer(), **kwargs)


def _openai_ok(model: str = "qwen3-14b") -> bytes:
    return json.dumps(
        {
            "id": "chatcmpl-test",
            "object": "chat.completion",
            "model": model,
            "choices": [
                {
                    "index": 0,
                    "message": {"role": "assistant", "content": "ok"},
                    "finish_reason": "stop",
                }
            ],
        }
    ).encode()


def _anthropic_ok(model: str = "claude-opus-4-6") -> bytes:
    return json.dumps(
        {
            "id": "msg_test",
            "type": "message",
            "role": "assistant",
            "model": model,
            "content": [{"type": "text", "text": "ok"}],
            "stop_reason": "end_turn",
            "usage": {"input_tokens": 5, "output_tokens": 1},
        }
    ).encode()


def _anthropic_tool_use_ok() -> bytes:
    return json.dumps(
        {
            "id": "msg_tool",
            "type": "message",
            "role": "assistant",
            "model": "claude-opus-4-6",
            "content": [
                {
                    "type": "tool_use",
                    "id": "tu_1",
                    "name": "web_search",
                    "input": {"query": "agentshroud"},
                }
            ],
            "stop_reason": "tool_use",
            "usage": {"input_tokens": 20, "output_tokens": 10},
        }
    ).encode()


def _openai_tool_use_ok() -> bytes:
    return json.dumps(
        {
            "id": "chatcmpl-tool",
            "object": "chat.completion",
            "model": "qwen3-14b",
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": None,
                        "tool_calls": [
                            {
                                "id": "call_1",
                                "type": "function",
                                "function": {
                                    "name": "web_search",
                                    "arguments": '{"query":"agentshroud"}',
                                },
                            }
                        ],
                    },
                    "finish_reason": "tool_calls",
                }
            ],
        }
    ).encode()


# ---------------------------------------------------------------------------
# 1. _normalize_local_model: LM Studio dash vs Ollama colon
# ---------------------------------------------------------------------------


def test_normalize_local_model_lmstudio_replaces_colon_with_dash():
    """ollama/qwen3:14b → qwen3-14b for LM Studio backend."""
    raw = "qwen3:14b"
    normalized = LLMProxy._normalize_local_model(raw, LMSTUDIO_API_BASE)
    assert normalized == "qwen3-14b"


def test_normalize_local_model_ollama_keeps_colon():
    """For Ollama backend the colon is kept (Ollama expects it)."""
    raw = "qwen3:14b"
    normalized = LLMProxy._normalize_local_model(raw, OLLAMA_API_BASE)
    assert normalized == "qwen3:14b"


def test_normalize_local_model_mlxlm_keeps_colon():
    """mlx_lm backend: colon is kept (no LM Studio dash convention)."""
    raw = "deepseek-r1:latest"
    normalized = LLMProxy._normalize_local_model(raw, MLXLM_API_BASE)
    assert normalized == "deepseek-r1:latest"


def test_normalize_local_model_already_dashed_is_idempotent():
    """If the model already uses dashes (LM Studio native ID), normalizing again is a no-op."""
    raw = "qwen3-14b"
    normalized = LLMProxy._normalize_local_model(raw, LMSTUDIO_API_BASE)
    assert normalized == "qwen3-14b"


@pytest.mark.asyncio
async def test_normalize_local_model_provider_prefix_stripped_before_normalize(monkeypatch):
    """ollama/ prefix is stripped during proxy_messages dispatch and normalization follows."""
    proxy = _make_proxy()
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "local")

    captured: dict = {}

    async def _fake_forward(url, body, headers):
        captured["url"] = url
        captured["body"] = json.loads(body)
        return 200, {"content-type": "application/json"}, _openai_ok("qwen3-14b")

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    await proxy.proxy_messages(
        "/v1/chat/completions",
        json.dumps(
            {"model": "ollama/qwen3:14b", "messages": [{"role": "user", "content": "hi"}]}
        ).encode(),
        {"content-type": "application/json"},
        user_id="u1",
    )

    # After prefix strip, ollama/qwen3:14b → qwen3:14b; routed to LM Studio → dash-normalized
    assert captured["body"]["model"] == "qwen3-14b"
    assert LMSTUDIO_API_BASE in captured["url"]


# ---------------------------------------------------------------------------
# 2. Cloud tool-call shape → local-mode equivalent
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_local_mode_anthropic_tool_use_shape_passes_through(monkeypatch):
    """Anthropic-format tool_use response returns the same shape in local mode."""
    proxy = _make_proxy()
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "local")

    async def _fake_forward(url, body, headers):
        return 200, {"content-type": "application/json"}, _anthropic_tool_use_ok()

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    status, _, body = await proxy.proxy_messages(
        "/v1/messages",
        json.dumps(
            {
                "model": "claude-opus-4-6",
                "messages": [{"role": "user", "content": "search"}],
                "tools": [{"name": "web_search", "description": "search", "input_schema": {}}],
            }
        ).encode(),
        {"content-type": "application/json"},
        user_id="u1",
    )

    assert status == 200
    data = json.loads(body)
    assert data["type"] == "message"
    content = data["content"]
    assert any(block.get("type") == "tool_use" for block in content)


@pytest.mark.asyncio
async def test_local_mode_openai_tool_call_shape_passes_through(monkeypatch):
    """OpenAI-format tool_calls response returns the same shape in local mode."""
    proxy = _make_proxy()
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "local")

    async def _fake_forward(url, body, headers):
        return 200, {"content-type": "application/json"}, _openai_tool_use_ok()

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    status, _, body = await proxy.proxy_messages(
        "/v1/chat/completions",
        json.dumps(
            {
                "model": "qwen3:14b",
                "messages": [{"role": "user", "content": "search"}],
                "tools": [{"type": "function", "function": {"name": "web_search"}}],
            }
        ).encode(),
        {"content-type": "application/json"},
        user_id="u1",
    )

    assert status == 200
    data = json.loads(body)
    assert "choices" in data
    choice = data["choices"][0]
    assert choice["finish_reason"] == "tool_calls"
    assert choice["message"]["tool_calls"][0]["function"]["name"] == "web_search"


@pytest.mark.asyncio
async def test_cloud_mode_anthropic_tool_use_shape_passes_through(monkeypatch):
    """Cloud mode Anthropic tool_use responses are unmodified (baseline parity)."""
    proxy = _make_proxy()
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "cloud")

    async def _fake_forward(url, body, headers):
        return 200, {"content-type": "application/json"}, _anthropic_tool_use_ok()

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    status, _, body = await proxy.proxy_messages(
        "/v1/messages",
        json.dumps(
            {
                "model": "claude-opus-4-6",
                "messages": [{"role": "user", "content": "search"}],
                "tools": [{"name": "web_search", "description": "search", "input_schema": {}}],
            }
        ).encode(),
        {"content-type": "application/json"},
        user_id="u1",
    )

    assert status == 200
    data = json.loads(body)
    assert any(block.get("type") == "tool_use" for block in data["content"])


# ---------------------------------------------------------------------------
# 3. Local→local-secondary failover on OOM / p99 > 30s timeout
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_local_oom_triggers_secondary_failover(monkeypatch):
    """OOM (503 backend_unavailable from primary local) triggers secondary local failover."""
    proxy = _make_proxy()
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "local")
    monkeypatch.setenv("AGENTSHROUD_LOCAL_MODEL_REF", "ollama/qwen3:14b")
    monkeypatch.setenv("AGENTSHROUD_LOCAL_SECONDARY_MODEL_REF", "ollama/qwen3:1.7b")
    monkeypatch.setenv("AGENTSHROUD_LOCAL_FAILOVER_ON_OOM", "1")

    oom_body = json.dumps(
        {"error": {"type": "backend_unavailable", "message": "out of memory"}}
    ).encode()
    secondary_body = _openai_ok("qwen3:1.7b")

    call_count = [0]

    async def _fake_forward(url, body, headers):
        call_count[0] += 1
        req = json.loads(body)
        if req.get("model") in ("qwen3:14b", "qwen3-14b"):
            return 503, {"content-type": "application/json"}, oom_body
        # Secondary model call
        return 200, {"content-type": "application/json"}, secondary_body

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    status, _, body = await proxy.proxy_messages(
        "/v1/chat/completions",
        json.dumps(
            {"model": "qwen3:14b", "messages": [{"role": "user", "content": "hi"}]}
        ).encode(),
        {"content-type": "application/json"},
        user_id="u1",
    )

    assert status == 200
    data = json.loads(body)
    assert data["choices"][0]["message"]["content"] == "ok"
    assert call_count[0] == 2, f"Expected 2 calls (primary + secondary), got {call_count[0]}"


@pytest.mark.asyncio
async def test_local_p99_timeout_triggers_secondary_failover(monkeypatch):
    """p99 timeout (TimeoutError on primary local) triggers secondary local model."""
    proxy = _make_proxy()
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "local")
    monkeypatch.setenv("AGENTSHROUD_LOCAL_MODEL_REF", "ollama/qwen3:14b")
    monkeypatch.setenv("AGENTSHROUD_LOCAL_SECONDARY_MODEL_REF", "ollama/qwen3:1.7b")
    monkeypatch.setenv("AGENTSHROUD_LOCAL_FAILOVER_ON_OOM", "1")

    secondary_body = _openai_ok("qwen3:1.7b")
    call_count = [0]

    async def _fake_forward(url, body, headers):
        call_count[0] += 1
        req = json.loads(body)
        if req.get("model") in ("qwen3:14b", "qwen3-14b"):
            raise TimeoutError("p99 exceeded 30s")
        return 200, {"content-type": "application/json"}, secondary_body

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    status, _, body = await proxy.proxy_messages(
        "/v1/chat/completions",
        json.dumps(
            {"model": "qwen3:14b", "messages": [{"role": "user", "content": "hi"}]}
        ).encode(),
        {"content-type": "application/json"},
        user_id="u1",
    )

    assert status == 200
    data = json.loads(body)
    assert data["choices"][0]["message"]["content"] == "ok"
    assert call_count[0] == 2


@pytest.mark.asyncio
async def test_local_oom_no_secondary_falls_through_to_503(monkeypatch):
    """If no secondary is configured and primary hits OOM, 503 is returned."""
    proxy = _make_proxy()
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "local")
    monkeypatch.setenv("AGENTSHROUD_LOCAL_MODEL_REF", "ollama/qwen3:14b")
    monkeypatch.delenv("AGENTSHROUD_LOCAL_SECONDARY_MODEL_REF", raising=False)
    monkeypatch.setenv("AGENTSHROUD_LOCAL_FAILOVER_ON_OOM", "1")

    oom_body = json.dumps(
        {"error": {"type": "backend_unavailable", "message": "out of memory"}}
    ).encode()

    async def _fake_forward(url, body, headers):
        return 503, {"content-type": "application/json"}, oom_body

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    status, _, body = await proxy.proxy_messages(
        "/v1/chat/completions",
        json.dumps(
            {"model": "qwen3:14b", "messages": [{"role": "user", "content": "hi"}]}
        ).encode(),
        {"content-type": "application/json"},
        user_id="u1",
    )

    assert status == 503


@pytest.mark.asyncio
async def test_local_oom_failover_disabled_does_not_retry(monkeypatch):
    """When AGENTSHROUD_LOCAL_FAILOVER_ON_OOM=0, OOM passes through without retry."""
    proxy = _make_proxy()
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "local")
    monkeypatch.setenv("AGENTSHROUD_LOCAL_MODEL_REF", "ollama/qwen3:14b")
    monkeypatch.setenv("AGENTSHROUD_LOCAL_SECONDARY_MODEL_REF", "ollama/qwen3:1.7b")
    monkeypatch.setenv("AGENTSHROUD_LOCAL_FAILOVER_ON_OOM", "0")

    oom_body = json.dumps(
        {"error": {"type": "backend_unavailable", "message": "out of memory"}}
    ).encode()
    call_count = [0]

    async def _fake_forward(url, body, headers):
        call_count[0] += 1
        return 503, {"content-type": "application/json"}, oom_body

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    status, _, _ = await proxy.proxy_messages(
        "/v1/chat/completions",
        json.dumps(
            {"model": "qwen3:14b", "messages": [{"role": "user", "content": "hi"}]}
        ).encode(),
        {"content-type": "application/json"},
        user_id="u1",
    )

    assert status == 503
    assert call_count[0] == 1, "Should not retry when failover disabled"


# ---------------------------------------------------------------------------
# 4. ResourceGuard VRAM headroom pre-flight check
# ---------------------------------------------------------------------------


def test_resource_guard_vram_headroom_check_raises_on_insufficient_vram():
    """check_vram_headroom raises VRAMHeadroomError when estimated VRAM exceeds budget."""
    limits = ResourceLimits(
        max_vram_headroom_mb=4096,  # 4 GB headroom required
    )
    guard = ResourceGuard(limits=limits)

    # A 128k token request with a 7B model needs ~3.5 GB just for KV cache;
    # we simulate the guard saying headroom is insufficient.
    with pytest.raises(VRAMHeadroomError, match="insufficient VRAM headroom"):
        guard.check_vram_headroom(
            agent_id="test-agent",
            estimated_tokens=131072,  # 128k tokens
            available_vram_mb=2048,  # only 2 GB free
        )


def test_resource_guard_vram_headroom_check_allows_small_context():
    """Small context request passes VRAM headroom check."""
    limits = ResourceLimits(max_vram_headroom_mb=4096)
    guard = ResourceGuard(limits=limits)

    # Should not raise — small context, plenty of VRAM
    guard.check_vram_headroom(
        agent_id="test-agent",
        estimated_tokens=1024,
        available_vram_mb=8192,
    )


def test_resource_guard_vram_headroom_check_disabled_when_threshold_zero():
    """VRAM check is skipped when max_vram_headroom_mb=0 (disabled)."""
    limits = ResourceLimits(max_vram_headroom_mb=0)
    guard = ResourceGuard(limits=limits)

    # Should not raise regardless of VRAM params
    guard.check_vram_headroom(
        agent_id="test-agent",
        estimated_tokens=200000,
        available_vram_mb=0,
    )


def test_resource_guard_vram_estimate_128k_tokens_triggers_rejection():
    """128k token request at 4 bytes/token KV cache triggers rejection at 4096 MB headroom."""
    limits = ResourceLimits(max_vram_headroom_mb=4096)
    guard = ResourceGuard(limits=limits)

    # 128k * 4 bytes * 2 (k+v) * 32 layers / 1024^2 = ~32 MB per layer for small model
    # We test the rejection boundary directly: available < required
    with pytest.raises(VRAMHeadroomError):
        guard.check_vram_headroom(
            agent_id="collab-123",
            estimated_tokens=131072,
            available_vram_mb=1024,  # less than 4096 threshold
        )


def test_vram_headroom_error_is_not_resource_warning():
    """VRAMHeadroomError must be a distinct exception, not a subclass of ResourceWarning."""
    err = VRAMHeadroomError("insufficient VRAM headroom: need 4096 MB, have 1024 MB")
    assert isinstance(err, Exception)
    assert not isinstance(err, ResourceWarning)
    assert "VRAM" in str(err)


# ---------------------------------------------------------------------------
# 5. get_local_secondary_model + _local_secondary_failover_base helpers
# ---------------------------------------------------------------------------


def test_get_local_secondary_model_reads_env(monkeypatch):
    """_get_local_secondary_model reads AGENTSHROUD_LOCAL_SECONDARY_MODEL_REF."""
    monkeypatch.setenv("AGENTSHROUD_LOCAL_SECONDARY_MODEL_REF", "ollama/qwen3:1.7b")
    proxy = _make_proxy()
    assert proxy._get_local_secondary_model() == "qwen3:1.7b"


def test_get_local_secondary_model_returns_none_when_unset(monkeypatch):
    """_get_local_secondary_model returns None if env var is unset."""
    monkeypatch.delenv("AGENTSHROUD_LOCAL_SECONDARY_MODEL_REF", raising=False)
    proxy = _make_proxy()
    assert proxy._get_local_secondary_model() is None


def test_local_secondary_failover_base_routes_correctly():
    """_local_failover_base resolves correct backend for secondary model."""
    # qwen3 → LM Studio
    base = LLMProxy._local_failover_base("qwen3-14b")
    assert base == LMSTUDIO_API_BASE

    # deepseek-r1 → mlx_lm
    base2 = LLMProxy._local_failover_base("deepseek-r1")
    assert base2 == MLXLM_API_BASE

    # unknown model → Ollama
    base3 = LLMProxy._local_failover_base("llama3.2")
    assert base3 == OLLAMA_API_BASE


def test_local_failover_base_routes_fieldflare_gemma_before_generic_gemma():
    """Turbo Fieldflare's exact model ID must win over the generic 'gemma' LM
    Studio route — regression test for the ordering bug where adding
    'gemma-4-26b-a4b-it' after the pre-existing 'gemma' entry would have made
    it unreachable (first-prefix-match-wins iteration)."""
    base = LLMProxy._local_failover_base("gemma-4-26b-a4b-it")
    assert base == FIELDFLARE_API_BASE


def test_local_failover_base_other_gemma_models_still_route_to_lmstudio():
    """A Gemma model that is NOT Turbo Fieldflare's exact ID still falls
    through to the generic 'gemma' -> LM Studio route (backward compat)."""
    base = LLMProxy._local_failover_base("gemma-2-9b-it")
    assert base == LMSTUDIO_API_BASE


def test_get_local_model_reads_fieldflare_ref(monkeypatch):
    """_get_local_model strips the provider prefix for a Fieldflare ref, same
    as it does for ollama/lmstudio refs."""
    monkeypatch.setenv("AGENTSHROUD_LOCAL_MODEL_REF", "openai-local/gemma-4-26b-a4b-it")
    proxy = _make_proxy()
    assert proxy._get_local_model() == "gemma-4-26b-a4b-it"


def test_local_failover_base_routes_omlx_gemma_before_generic_gemma():
    """oMLX's gemma-4-12B-it-4bit must win over the generic 'gemma' LM Studio
    route, and over Turbo Fieldflare's distinct gemma-4-26b-a4b-it route —
    same ordering-bug class as the Fieldflare regression test above."""
    base = LLMProxy._local_failover_base("gemma-4-12B-it-4bit")
    assert base == OMLX_API_BASE


def test_local_failover_base_routes_omlx_deepseek_r1_qwen3_8b():
    """oMLX's DeepSeek-R1-0528-Qwen3-8B must win over the generic
    'deepseek-r1' -> mlx_lm route (no-tool-calling backend)."""
    base = LLMProxy._local_failover_base("DeepSeek-R1-0528-Qwen3-8B-6bit")
    assert base == OMLX_API_BASE


def test_local_backend_headers_injects_bearer_token_for_omlx(monkeypatch):
    """oMLX requires a bearer token, unlike LM Studio/mlx_lm/Fieldflare."""
    monkeypatch.setattr(llm_proxy_module, "OMLX_API_KEY", "test-omlx-key-123")
    headers = LLMProxy._local_backend_headers(OMLX_API_BASE, {"content-type": "application/json"})
    assert headers["authorization"] == "Bearer test-omlx-key-123"


def test_local_backend_headers_no_auth_for_fieldflare():
    """Fieldflare and other no-auth local backends are left untouched."""
    original = {"content-type": "application/json"}
    headers = LLMProxy._local_backend_headers(FIELDFLARE_API_BASE, original)
    assert "authorization" not in headers
    assert headers == original


def test_local_backend_headers_does_not_mutate_input():
    """Returns a copy — never mutates the caller's headers dict in place."""
    original = {"content-type": "application/json"}
    LLMProxy._local_backend_headers(FIELDFLARE_API_BASE, original)
    assert original == {"content-type": "application/json"}


# ---------------------------------------------------------------------------
# 6. Hermes local-mode equivalence: OPENAI_BASE_URL routed through gateway
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_hermes_openai_path_local_model_routed_correctly(monkeypatch):
    """Hermes sends OpenAI-compat requests; local qwen3 model routes to LM Studio."""
    proxy = _make_proxy()
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "local")

    captured: dict = {}

    async def _fake_forward(url, body, headers):
        captured["url"] = url
        captured["body"] = json.loads(body)
        return 200, {"content-type": "application/json"}, _openai_ok("qwen3-14b")

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    status, _, body = await proxy.proxy_messages(
        "/v1/chat/completions",
        json.dumps(
            {
                "model": "qwen3:14b",
                "messages": [{"role": "user", "content": "hello from hermes"}],
            }
        ).encode(),
        {"content-type": "application/json"},
        user_id="hermes-agent",
    )

    assert status == 200
    # Hermes qwen3:14b → LM Studio (LOCAL_MODEL_ROUTES prefix match)
    assert LMSTUDIO_API_BASE in captured["url"]
    # Model normalized to LM Studio format (dash, not colon)
    assert captured["body"]["model"] == "qwen3-14b"


@pytest.mark.asyncio
async def test_hermes_cloud_mode_uses_anthropic_endpoint(monkeypatch):
    """In cloud mode, Hermes Claude model routes to Anthropic endpoint."""
    proxy = _make_proxy()
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "cloud")

    captured: dict = {}

    async def _fake_forward(url, body, headers):
        captured["url"] = url
        return 200, {"content-type": "application/json"}, _anthropic_ok()

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    status, _, _ = await proxy.proxy_messages(
        "/v1/messages",
        json.dumps(
            {
                "model": "claude-opus-4-6",
                "messages": [{"role": "user", "content": "hello from hermes"}],
            }
        ).encode(),
        {"content-type": "application/json"},
        user_id="hermes-agent",
    )

    assert status == 200
    assert "api.anthropic.com" in captured["url"]


# ---------------------------------------------------------------------------
# 7. mlx_lm dispatch (reasoning model)
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_deepseek_r1_routes_to_mlxlm(monkeypatch):
    """deepseek-r1 is routed to mlx_lm endpoint."""
    proxy = _make_proxy()
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "local")

    captured: dict = {}

    async def _fake_forward(url, body, headers):
        captured["url"] = url
        return 200, {"content-type": "application/json"}, _openai_ok("deepseek-r1")

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    await proxy.proxy_messages(
        "/v1/chat/completions",
        json.dumps(
            {"model": "deepseek-r1", "messages": [{"role": "user", "content": "reason"}]}
        ).encode(),
        {"content-type": "application/json"},
        user_id="u1",
    )

    assert MLXLM_API_BASE in captured["url"]


@pytest.mark.asyncio
async def test_mlx_community_deepseek_routes_to_mlxlm(monkeypatch):
    """mlx-community/deepseek-r1 full ID routes to mlx_lm endpoint."""
    proxy = _make_proxy()
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "local")

    captured: dict = {}

    async def _fake_forward(url, body, headers):
        captured["url"] = url
        return 200, {"content-type": "application/json"}, _openai_ok("mlx-community/deepseek-r1")

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    await proxy.proxy_messages(
        "/v1/chat/completions",
        json.dumps(
            {
                "model": "mlx-community/deepseek-r1",
                "messages": [{"role": "user", "content": "reason"}],
            }
        ).encode(),
        {"content-type": "application/json"},
        user_id="u1",
    )

    assert MLXLM_API_BASE in captured["url"]


# ---------------------------------------------------------------------------
# 8. OOM body detection helper
# ---------------------------------------------------------------------------


def test_is_local_oom_detects_backend_unavailable():
    """_is_local_oom returns True for backend_unavailable 503 bodies."""
    oom_body = json.dumps(
        {"error": {"type": "backend_unavailable", "message": "out of memory"}}
    ).encode()
    assert LLMProxy._is_local_oom(503, oom_body) is True


def test_is_local_oom_returns_false_for_200():
    """_is_local_oom returns False for successful responses."""
    ok_body = _openai_ok()
    assert LLMProxy._is_local_oom(200, ok_body) is False


def test_is_local_oom_returns_false_for_quota_429():
    """_is_local_oom returns False for cloud 429 quota errors (different failover path)."""
    quota_body = json.dumps({"error": {"type": "quota_exceeded"}}).encode()
    assert LLMProxy._is_local_oom(429, quota_body) is False


def test_is_local_oom_detects_oom_in_error_message():
    """_is_local_oom detects 'out of memory' in error message string."""
    oom_body = json.dumps({"error": "CUDA out of memory. Tried to allocate 2.50 GiB"}).encode()
    assert LLMProxy._is_local_oom(500, oom_body) is True


def test_is_local_oom_handles_non_json_body():
    """_is_local_oom handles raw non-JSON bodies from some backends."""
    raw_oom = b"CUDA error: out of memory allocating tensor"
    assert LLMProxy._is_local_oom(500, raw_oom) is True


def test_is_local_oom_raw_body_false_on_normal_500():
    """_is_local_oom returns False for non-OOM raw 500 bodies."""
    raw_err = b"Internal Server Error"
    assert LLMProxy._is_local_oom(500, raw_err) is False


# ---------------------------------------------------------------------------
# 8b. _local_secondary_failover_request: Anthropic path
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_local_secondary_failover_anthropic_path(monkeypatch):
    """Secondary failover for Anthropic-format (/v1/messages) path translates and returns."""
    proxy = _make_proxy()
    monkeypatch.setenv("AGENTSHROUD_LOCAL_SECONDARY_MODEL_REF", "ollama/qwen3:1.7b")

    secondary_ok = _openai_ok("qwen3-1.7b")

    async def _fake_forward(url, body, headers):
        return 200, {"content-type": "application/json"}, secondary_ok

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    result = await proxy._local_secondary_failover_request(
        "/v1/messages",
        {"model": "claude-opus-4-6", "messages": [{"role": "user", "content": "hi"}]},
        is_openai=False,
    )

    assert result is not None
    assert result[0] == 200


@pytest.mark.asyncio
async def test_local_secondary_failover_unknown_path_returns_none(monkeypatch):
    """Unknown path (not /v1/messages, not is_openai) returns None."""
    proxy = _make_proxy()
    monkeypatch.setenv("AGENTSHROUD_LOCAL_SECONDARY_MODEL_REF", "ollama/qwen3:1.7b")

    result = await proxy._local_secondary_failover_request(
        "/v1beta/generateContent",  # Google path — no translator
        {"model": "gemini-pro"},
        is_openai=False,
    )

    assert result is None


@pytest.mark.asyncio
async def test_local_secondary_failover_secondary_non_200_returns_none(monkeypatch):
    """Secondary model returning non-200 increments failed stat and returns None."""
    proxy = _make_proxy()
    monkeypatch.setenv("AGENTSHROUD_LOCAL_SECONDARY_MODEL_REF", "ollama/qwen3:1.7b")

    async def _fake_forward(url, body, headers):
        return 503, {"content-type": "application/json"}, b'{"error":"overloaded"}'

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    result = await proxy._local_secondary_failover_request(
        "/v1/chat/completions",
        {"model": "qwen3:1.7b", "messages": [{"role": "user", "content": "hi"}]},
        is_openai=True,
    )

    assert result is None
    assert proxy.get_stats().get("failover_local_secondary_failed", 0) == 1


@pytest.mark.asyncio
async def test_local_secondary_failover_exception_returns_none(monkeypatch):
    """Exception during secondary dispatch increments failed stat and returns None."""
    proxy = _make_proxy()
    monkeypatch.setenv("AGENTSHROUD_LOCAL_SECONDARY_MODEL_REF", "ollama/qwen3:1.7b")

    async def _fake_forward(url, body, headers):
        raise ConnectionRefusedError("secondary also down")

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    result = await proxy._local_secondary_failover_request(
        "/v1/chat/completions",
        {"model": "qwen3:1.7b", "messages": [{"role": "user", "content": "hi"}]},
        is_openai=True,
    )

    assert result is None
    assert proxy.get_stats().get("failover_local_secondary_failed", 0) == 1


# ---------------------------------------------------------------------------
# 9. Stats counters for local→secondary failover
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_stats_local_secondary_failover_succeeded_incremented(monkeypatch):
    """failover_local_secondary_succeeded stat increments on successful secondary dispatch."""
    proxy = _make_proxy()
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "local")
    monkeypatch.setenv("AGENTSHROUD_LOCAL_MODEL_REF", "ollama/qwen3:14b")
    monkeypatch.setenv("AGENTSHROUD_LOCAL_SECONDARY_MODEL_REF", "ollama/qwen3:1.7b")
    monkeypatch.setenv("AGENTSHROUD_LOCAL_FAILOVER_ON_OOM", "1")

    oom_body = json.dumps(
        {"error": {"type": "backend_unavailable", "message": "out of memory"}}
    ).encode()

    async def _fake_forward(url, body, headers):
        req = json.loads(body)
        model = req.get("model", "")
        if model in ("qwen3:14b", "qwen3-14b"):
            return 503, {"content-type": "application/json"}, oom_body
        return 200, {"content-type": "application/json"}, _openai_ok("qwen3:1.7b")

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    await proxy.proxy_messages(
        "/v1/chat/completions",
        json.dumps(
            {"model": "qwen3:14b", "messages": [{"role": "user", "content": "hi"}]}
        ).encode(),
        {"content-type": "application/json"},
        user_id="u1",
    )

    stats = proxy.get_stats()
    assert stats.get("failover_local_secondary_succeeded", 0) == 1


# ---------------------------------------------------------------------------
# 10. Model-ref round-trip: every ref survives normalize→dispatch→model-in-body
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "input_ref,expected_model,expected_backend",
    [
        ("ollama/qwen3:14b", "qwen3-14b", LMSTUDIO_API_BASE),
        ("ollama/llama3.2:3b", "llama3.2:3b", OLLAMA_API_BASE),
        ("ollama/deepseek-r1:latest", "deepseek-r1:latest", MLXLM_API_BASE),
        ("lmstudio/qwen3.6-27b", "qwen3.6-27b", LMSTUDIO_API_BASE),
        ("qwen3:14b", "qwen3-14b", LMSTUDIO_API_BASE),
        ("deepseek-r1", "deepseek-r1", MLXLM_API_BASE),
    ],
)
@pytest.mark.asyncio
async def test_model_ref_round_trip(input_ref, expected_model, expected_backend, monkeypatch):
    """Full round-trip: each model ref is normalized and dispatched to the correct backend."""
    proxy = _make_proxy()
    monkeypatch.setattr(llm_proxy_module, "MODEL_MODE", "local")

    captured: dict = {}

    async def _fake_forward(url, body, headers):
        captured["url"] = url
        captured["body"] = json.loads(body)
        return 200, {"content-type": "application/json"}, _openai_ok(expected_model)

    proxy._forward_request = _fake_forward  # type: ignore[method-assign]

    await proxy.proxy_messages(
        "/v1/chat/completions",
        json.dumps({"model": input_ref, "messages": [{"role": "user", "content": "hi"}]}).encode(),
        {"content-type": "application/json"},
        user_id="u1",
    )

    assert captured["body"]["model"] == expected_model, (
        f"model ref {input_ref!r}: expected body model={expected_model!r}, "
        f"got {captured['body']['model']!r}"
    )
    assert expected_backend in captured["url"], (
        f"model ref {input_ref!r}: expected backend {expected_backend!r}, "
        f"got {captured['url']!r}"
    )
