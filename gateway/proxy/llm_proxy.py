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

from gateway.proxy.anthropic_openai_sse_translator import translate_openai_sse_to_anthropic
from gateway.proxy.anthropic_openai_translator import (
    anthropic_to_openai_request,
    anthropic_to_openai_response,
    openai_to_anthropic_request,
    openai_to_anthropic_response,
)
from gateway.proxy.gemini_openai_translator import (
    gemini_failover_unsupported_reason,
    gemini_to_openai_request,
    gemini_to_openai_response,
    openai_to_gemini_request,
    openai_to_gemini_response,
)
from gateway.proxy.llm_quota_detector import (
    is_overloaded,
    is_quota_exhausted,
    is_rate_limited_post_retry,
)

logger = logging.getLogger("agentshroud.proxy.llm_api")

# Cooldown window (seconds) for "failover active" Telegram notices.
# One notice per window — avoids spamming on every cron tick.
_FAILOVER_NOTIFY_COOLDOWN_SECONDS = 1800
_FAILOVER_NOTIFY_STAMP = "/tmp/.gateway-failover-notify-stamp"

# Connect timeout for outbound LLM requests. Must clear this host's observed
# DNS-resolution latency for api.anthropic.com/api.openai.com (~4.0-4.1s under
# the current VPN/resolver setup) — too tight a margin here surfaces upstream
# as cron "model idle timeout" failures, not as a visible connect error.
LLM_CONNECT_TIMEOUT_SECONDS = 15.0

ANTHROPIC_API_BASE = "https://api.anthropic.com"
OPENAI_API_BASE = "https://api.openai.com"
GOOGLE_API_BASE = "https://generativelanguage.googleapis.com"
OLLAMA_API_BASE = "http://host.docker.internal:11434"
LMSTUDIO_API_BASE = os.environ.get("LMSTUDIO_API_BASE") or "http://host.docker.internal:1234"
MLXLM_API_BASE = os.environ.get("MLXLM_API_BASE") or "http://host.docker.internal:8234"
# Turbo Fieldflare — MLX-native Gemma 4 26B-A4B server (agentshroud_mlx project),
# OpenAI-compatible (/v1/chat/completions, /v1/models), no auth. Default local
# model as of 2026-08 — see docs/planning/LOCAL_LLM_REVIEW.md.
FIELDFLARE_API_BASE = os.environ.get("FIELDFLARE_API_BASE") or "http://host.docker.internal:8238"
# Rapid-MLX — tool-call server (agentshroud_mlx project), 8-bit KV cache for
# faster large-context prefill than plain LM Studio serving of the same base
# model. No auth. Added 2026-08-18 after gemma-4-12B-it-4bit (via oMLX)
# repeatedly showed non-terminating generation under Hermes's real cron
# workload despite temperature/max_tokens tuning — see
# [[project_hermes_local_model_temperature_repetition_loop]]. Switched
# 2026-08-19 from qwen3-14b to NVIDIA Nemotron 3.5 Lightning 30B-A3B after a
# local-llms-repo bake-off found 6/6 perfect multi-step tool-call trials
# (vs. qwen3-14b's frequent silent-completion/hallucinated-success failures)
# at 262K native context — see docker/bots/hermes/CONTINUE-2026-08-17.md /
# session notes for the full investigation. Root cause of the earlier
# crashes was partly an unbounded Metal cache OOM (50.8GB peak observed),
# now capped via RAPID_MLX_CACHE_MB/RAPID_MLX_GPU_UTIL in the local-llms repo.
RAPID_MLX_API_BASE = os.environ.get("RAPID_MLX_API_BASE") or "http://host.docker.internal:8002"
# Rapid-MLX's own /v1/models reports its loaded weights by full local path, not
# a friendly name — a short alias like "qwen3-14b-rapid" must be translated
# before forwarding (see _normalize_local_model). Overridable since this path
# is host-specific.
RAPID_MLX_MODEL_ID = os.environ.get(
    "RAPID_MLX_MODEL_ID",
    "/Users/ijefferson.admin/.cache/lm-studio/models/mlx-community/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-4bit",
)
# oMLX — OpenAI-compatible local server (agentshroud_mlx/local-llms project),
# hosts DeepSeek-R1-0528-Qwen3-8B and gemma-4-12B-it-4bit. Unlike the other
# local backends, oMLX requires a bearer token (see OMLX_API_KEY below) —
# confirmed 2026-08-13: gemma-4-26b-a4b-it via Turbo Fieldflare could not
# reliably produce well-formed tool calls under Hermes's real tool-heavy
# workload (see docs/planning/LOCAL_LLM_REVIEW.md); gemma-4-12B-it-4bit via
# oMLX produced a correct tool call on the same class of request.
OMLX_API_BASE = os.environ.get("OMLX_API_BASE") or "http://host.docker.internal:8000"
OMLX_API_KEY = os.environ.get("OMLX_API_KEY", "")
MAIN_MODEL = os.environ.get("AGENTSHROUD_LOCAL_MODEL", "qwen2.5-coder:7b")
MODEL_MODE = os.environ.get("AGENTSHROUD_MODEL_MODE", "local").lower()

# Maps model name prefixes to specific backend base URLs.
# Checked before the generic Ollama fallback — only needed for models that do NOT
# run under Ollama (e.g. mlx_lm or LM Studio on a different port).
# Models not listed here fall through to OLLAMA_API_BASE automatically.
#
# Order matters: matching is first-prefix-wins (see _local_failover_base), so
# "gemma-4-26b-a4b-it" (Turbo Fieldflare's exact model ID) MUST precede the
# generic "gemma" entry below, or it would incorrectly match "gemma" first and
# route to LM Studio instead of Fieldflare.
LOCAL_MODEL_ROUTES: dict[str, str] = {
    "mlx-community/deepseek-r1": MLXLM_API_BASE,  # mlx-lm full-ID: DeepSeek-R1-0528-Qwen3-8B-4bit
    "deepseek-r1-0528-qwen3-8b": OMLX_API_BASE,  # oMLX — reasoning model, tool-calling capable
    "deepseek-r1": MLXLM_API_BASE,  # Reasoning — mlx_lm on :8234 (no tool calling)
    "gemma-4-26b-a4b-it": FIELDFLARE_API_BASE,  # Turbo Fieldflare — MLX Gemma 4 on :8238
    "gemma-4-12b-it-4bit": OMLX_API_BASE,  # oMLX — Gemma 4 12B, confirmed tool-calling works
    # qwen3.8-27b-mlx MUST be listed before the generic "qwen3" prefix below —
    # dict iteration is insertion-order and the lookup returns the first
    # startswith() match, so a less-specific earlier entry would shadow this
    # one forever. LM Studio cannot load this model's qwen3_5 architecture
    # yet (confirmed 2026-08-17 — needs an LM Studio engine update); it's
    # served via mlx_lm on :8234 instead, opt-in (`services.sh mlx-lm start`).
    "qwen3.8-27b-mlx": MLXLM_API_BASE,  # Qwen3.8-27B — mlx_lm on :8234, NOT LM Studio
    # qwen3-14b-rapid MUST precede the generic "qwen3" entry below for the same
    # first-prefix-wins reason as qwen3.8-27b-mlx above.
    "qwen3-14b-rapid": RAPID_MLX_API_BASE,  # Rapid-MLX — tool-call-optimized, 8-bit KV, :8002
    # Renamed 2026-08-21: "qwen3-14b-rapid" was a stale alias left over from
    # before the 2026-08-19 Rapid-MLX model swap to NVIDIA Nemotron 3.5
    # Lightning — RAPID_MLX_MODEL_ID below already pointed at the real
    # Nemotron weights, but Hermes was still told the model was named
    # "qwen3-14b-rapid", so its own reasoning_timeouts.py floor table
    # (agent/reasoning_timeouts.py) matched the "qwen3" family's 180s stale-
    # call floor instead of "nemotron-3.5-lightning"'s 300s floor — killing
    # real newsletter/report generation turns ~100s before they would have
    # completed (observed: 278s actual, 180s applied threshold), leaving
    # every affected cron job's output file with just its header. New alias
    # matches Hermes's own floor-table pattern so it gets the correct budget.
    "nemotron-3.5-lightning-rapid": RAPID_MLX_API_BASE,  # Rapid-MLX — same backend, correctly-named alias
    # qwen3-coder MUST precede the generic "qwen3" entry below for the same
    # first-prefix-wins reason as qwen3.8-27b-mlx/qwen3-14b-rapid above.
    # Registered opt-in coding model (2026-08-22 default set) — served via
    # oMLX on :8000 when enabled (`services.sh omlx-coder-enable`), not
    # LM Studio, so it must not fall through to the generic "qwen3" entry.
    "qwen3-coder": OMLX_API_BASE,  # oMLX — Qwen3-Coder-30B-A3B, opt-in coding model
    "qwen3": LMSTUDIO_API_BASE,  # Qwen3 family (14b, etc.) — LM Studio on :1234
    "qwen2.5-coder": LMSTUDIO_API_BASE,  # Coding — LM Studio on :1234
    "gemma": LMSTUDIO_API_BASE,  # Other Gemma models — LM Studio on :1234
}

# Per-backend operator hints returned in the structured 503 body when a local
# backend (mlx_lm / Ollama / LM Studio / Turbo Fieldflare) is unreachable at
# connect time.
_LOCAL_BACKEND_HINTS: dict[str, str] = {
    MLXLM_API_BASE: (
        "mlx_lm backend is not running on the host. " "Start it with: mlx_lm.server --port 8234"
    ),
    OLLAMA_API_BASE: ("Ollama backend is not running on the host. Start it with: ollama serve"),
    LMSTUDIO_API_BASE: (
        "LM Studio backend is not running on the host. "
        "Start the LM Studio local server (default port 1234)."
    ),
    FIELDFLARE_API_BASE: (
        "Turbo Fieldflare backend is not running on the host. Start it with: tf-start"
    ),
    RAPID_MLX_API_BASE: (
        "Rapid-MLX backend is not running on the host. "
        "Start it with: services.sh rapid-mlx start"
    ),
}

# Minimum seconds between repeated "backend unavailable" WARNING logs per backend
# (avoids per-request log spam while a backend is down).
_BACKEND_UNAVAILABLE_WARN_INTERVAL_SECONDS = 300


class LLMProxy:
    """Proxies LLM API calls (Anthropic, OpenAI, Google) through the security pipeline."""

    def __init__(
        self,
        pipeline=None,
        middleware_manager=None,
        sanitizer=None,
        tool_acl_enforcer=None,
        credential_injector=None,
    ):
        self.pipeline = pipeline
        self.middleware_manager = middleware_manager
        self.sanitizer = sanitizer
        self.tool_acl_enforcer = tool_acl_enforcer
        self.credential_injector = credential_injector
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
            "failover_quota_succeeded": 0,
            "failover_quota_failed": 0,
            "failover_active": False,
            "failover_last_provider": None,
            "failover_last_event": None,
        }
        # Optional AuditChain for persistent failover event logging.
        # Injected by lifespan.py if available.
        self.audit_chain = None
        # Per-backend monotonic timestamp of the last "backend unavailable"
        # WARNING — rate-limits the log to one per interval per backend.
        self._backend_unavailable_last_warn: dict[str, float] = {}

    def get_stats(self) -> dict:
        return dict(self._stats)

    # ---------------------------------------------------------------------------
    # Quota failover helpers
    # ---------------------------------------------------------------------------

    def _get_local_model(self) -> str:
        ref = os.environ.get("AGENTSHROUD_LOCAL_MODEL_REF", "ollama/qwen3:14b")
        return ref.split("/", 1)[-1]

    def _get_local_secondary_model(self) -> str | None:
        """Return the bare secondary local model name, or None if not configured.

        Reads AGENTSHROUD_LOCAL_SECONDARY_MODEL_REF (e.g. 'ollama/qwen3:1.7b')
        and strips the provider prefix. Returns None when the env var is unset or empty.
        """
        ref = os.environ.get("AGENTSHROUD_LOCAL_SECONDARY_MODEL_REF", "")
        if not ref:
            return None
        return ref.split("/", 1)[-1]

    @staticmethod
    def _is_local_oom(status: int, body: bytes) -> bool:
        """Return True if the response indicates a local-model OOM or backend_unavailable.

        Detects:
        - HTTP 503 with error.type == 'backend_unavailable' (our own structured error)
        - Any HTTP 5xx response body containing 'out of memory' (GPU/CPU OOM)
        - CUDA OOM string patterns from Ollama / LM Studio / mlx_lm error messages
        """
        if status == 200:
            return False
        if status == 429:
            # Cloud quota error — handled by quota failover, not OOM failover
            return False
        try:
            data = json.loads(body)
            # Our structured 503: {"error": {"type": "backend_unavailable", ...}}
            err = data.get("error", {})
            if isinstance(err, dict) and err.get("type") == "backend_unavailable":
                return True
            # Generic error string containing OOM keywords
            err_str = json.dumps(data).lower()
            return any(kw in err_str for kw in ("out of memory", "cuda out of memory", "oom"))
        except (json.JSONDecodeError, AttributeError):
            # Raw string body from some backends
            body_lower = body.decode("utf-8", errors="replace").lower()
            return any(kw in body_lower for kw in ("out of memory", "cuda out of memory", "oom"))

    async def _local_secondary_failover_request(
        self,
        path: str,
        request_data: dict | None,
        is_openai: bool,
    ) -> tuple[int, dict, bytes] | None:
        """Attempt a local→local-secondary failover when the primary local model hits OOM.

        Returns (status, headers, body) from the secondary local model, or None if:
        - No secondary model is configured (AGENTSHROUD_LOCAL_SECONDARY_MODEL_REF unset)
        - The secondary dispatch also fails

        Entry point: gateway/proxy/llm_proxy.py:proxy_messages (OOM/timeout detected)
        Routing: _local_secondary_failover_request dispatches to secondary backend
        Handler: _forward_request forwards to secondary local model HTTP endpoint
        """
        secondary_model = self._get_local_secondary_model()
        if secondary_model is None:
            return None

        fo_base = self._local_failover_base(secondary_model)
        secondary_model_normalized = self._normalize_local_model(secondary_model, fo_base)

        logger.info(
            "Local→secondary failover: dispatching to %s at %s",
            secondary_model_normalized,
            fo_base,
        )

        try:
            if is_openai:
                fo_data = dict(request_data or {})
                fo_data["model"] = secondary_model_normalized
                fo_body = json.dumps(fo_data).encode()
                fo_url = f"{fo_base}/v1/chat/completions"
            elif path and "/v1/messages" in path:
                oai_req = anthropic_to_openai_request(
                    request_data or {}, secondary_model_normalized
                )
                fo_body = json.dumps(oai_req).encode()
                fo_url = f"{fo_base}/v1/chat/completions"
            else:
                return None

            fo_headers = self._local_backend_headers(fo_base, {"content-type": "application/json"})
            f_status, f_headers, f_body = await self._forward_request(fo_url, fo_body, fo_headers)

            if f_status == 200 and f_body:
                self._stats["failover_local_secondary_succeeded"] = (
                    self._stats.get("failover_local_secondary_succeeded", 0) + 1
                )
                logger.info(
                    "Local→secondary failover succeeded: %s HTTP 200", secondary_model_normalized
                )
                return f_status, f_headers, f_body

            logger.warning(
                "Local→secondary failover model %s returned HTTP %s",
                secondary_model_normalized,
                f_status,
            )
        except Exception as e:
            logger.warning("Local→secondary failover error: %s", e)

        self._stats["failover_local_secondary_failed"] = (
            self._stats.get("failover_local_secondary_failed", 0) + 1
        )
        return None

    @staticmethod
    def _local_failover_base(local_model: str) -> str:
        """Resolve the local backend for failover dispatch via LOCAL_MODEL_ROUTES.

        Failover previously hardcoded Ollama, which fails when the configured
        local model is actually served by LM Studio or mlx_lm."""
        ml = local_model.lower()
        for prefix, route_url in LOCAL_MODEL_ROUTES.items():
            if ml.startswith(prefix):
                return route_url
        return OLLAMA_API_BASE

    @staticmethod
    def _normalize_local_model(local_model: str, base_url: str) -> str:
        # LM Studio identifiers use dashes ('qwen3-14b'); ollama-style refs use
        # colons ('qwen3:14b'). Normalize so the dispatch matches a loaded model.
        if base_url == LMSTUDIO_API_BASE:
            return local_model.replace(":", "-")
        # Rapid-MLX only recognizes its weights by full local path — confirmed
        # live 2026-08-18: requesting "qwen3-14b-rapid" 404s with "model does
        # not exist. Available: /Users/.../Qwen3-14B-MLX-4bit".
        if base_url == RAPID_MLX_API_BASE:
            return RAPID_MLX_MODEL_ID
        # oMLX's own /v1/models catalog only recognizes exact, case-sensitive
        # IDs — confirmed live 2026-08-23: "gemma-4-12b-it-4bit" (lowercase b)
        # happens to still match "gemma-4-12B-it-4bit" (oMLX does a case-
        # insensitive compare), but "deepseek-r1-0528-qwen3-8b" — the
        # documented LOCAL_MODEL_ROUTES alias, matching the AgentShroud
        # default-model-set naming convention — has a genuinely different
        # final segment from the real catalog ID "DeepSeek-R1-0528-Qwen3-8B-
        # 6bit" ("-qwen3-8b" vs "-6bit"), so it 404s: "Model
        # 'deepseek-r1-0528-qwen3-8b' not found. Available models:
        # DeepSeek-R1-0528-Qwen3-8B-6bit, gemma-4-12B-it-4bit". Every caller
        # using the documented alias (including every Hermes cron job that
        # would route to this "reasoning default" model) got a hard 404 on
        # every single call. Same stale-alias-correction pattern as
        # RAPID_MLX_MODEL_ID above.
        if base_url == OMLX_API_BASE and local_model.lower() == "deepseek-r1-0528-qwen3-8b":
            return "DeepSeek-R1-0528-Qwen3-8B-6bit"
        return local_model

    @staticmethod
    def _suppress_qwen3_thinking(request_data: dict) -> bool:
        """Append '/no_think' to the last user message, in place, if not already present.

        Qwen3-family models emit chain-of-thought ("reasoning_content") before
        the real answer by default. Under Hermes/OpenClaw's real agentic
        workload this repeatedly produced non-terminating generation (see
        [[project_hermes_local_model_temperature_repetition_loop]]) — the same
        failure class that disqualified qwen3.8-27b-mlx earlier. The
        'chat_template_kwargs': {'enable_thinking': false} field is silently
        ignored by this serving stack (confirmed live 2026-08-18); only the
        '/no_think' suffix in the message text actually disables it. Applied
        at the gateway so every caller (Hermes cron, OpenClaw agents, direct
        API use) gets this automatically, not just hand-patched jobs.

        Returns True if the request body was modified (caller must re-encode).
        """
        messages = request_data.get("messages")
        if not isinstance(messages, list):
            return False
        for msg in reversed(messages):
            if not isinstance(msg, dict) or msg.get("role") != "user":
                continue
            content = msg.get("content")
            if isinstance(content, str):
                if "/no_think" in content:
                    return False
                msg["content"] = content + " /no_think"
                return True
            if isinstance(content, list):
                for part in reversed(content):
                    if isinstance(part, dict) and part.get("type") == "text":
                        text = part.get("text", "")
                        if "/no_think" in text:
                            return False
                        part["text"] = text + " /no_think"
                        return True
            return False
        return False

    @staticmethod
    def _widen_optional_tool_param_types(request_data: dict) -> bool:
        """Add 'null' as an accepted type for every non-required tool parameter, in place.

        Rapid-MLX's constrained tool-call decoding fills every optional
        argument with JSON null instead of omitting the key (confirmed live
        2026-08-19: Hermes's skills_list(category: str = None) call was
        rejected with "HTTP 400: ... Expected string, got NoneType" even
        though 'category' is correctly absent from the schema's 'required'
        list). The tool schemas themselves are correct OpenAI-style JSON
        Schema — 'string' alone just doesn't permit null per spec. Widening
        every non-required property's declared type to also accept null lets
        the model's actual (harmless — it means "omitted") output pass
        validation without touching any tool's own schema definition.

        Returns True if the request body was modified (caller must re-encode).
        """
        tools = request_data.get("tools")
        if not isinstance(tools, list):
            return False
        changed = False
        for tool in tools:
            if not isinstance(tool, dict):
                continue
            fn = tool.get("function") if tool.get("type") == "function" else tool
            if not isinstance(fn, dict):
                continue
            params = fn.get("parameters")
            if not isinstance(params, dict):
                continue
            properties = params.get("properties")
            if not isinstance(properties, dict):
                continue
            required = set(params.get("required") or [])
            for prop_name, prop_schema in properties.items():
                if prop_name in required or not isinstance(prop_schema, dict):
                    continue
                prop_type = prop_schema.get("type")
                if isinstance(prop_type, str) and prop_type != "null":
                    prop_schema["type"] = [prop_type, "null"]
                    changed = True
                elif isinstance(prop_type, list) and "null" not in prop_type:
                    prop_type.append("null")
                    changed = True
        return changed

    @staticmethod
    def _local_backend_headers(base_url: str, headers: dict) -> dict:
        """Inject per-backend auth for local backends that require it.

        Unlike LM Studio / mlx_lm / Turbo Fieldflare (no auth), oMLX requires
        a bearer token. Returns a copy of headers — never mutates the input,
        matching the OpenAI-path convention above.
        """
        if base_url == OMLX_API_BASE and OMLX_API_KEY:
            headers = dict(headers)
            headers["authorization"] = f"Bearer {OMLX_API_KEY}"
            headers.pop("Authorization", None)
            headers.pop("x-api-key", None)
        return headers

    def _emit_failover_notice(self, token: str, translated: bool) -> None:
        """Send a single Telegram notice per cooldown window when failover activates."""
        import time as _time

        now = int(_time.time())
        try:
            if os.path.exists(_FAILOVER_NOTIFY_STAMP):
                with open(_FAILOVER_NOTIFY_STAMP) as f:
                    parts = f.read().strip().split()
                    last_ts = int(parts[0]) if parts else 0
                    last_token = parts[1] if len(parts) > 1 else ""
                    if now - last_ts < _FAILOVER_NOTIFY_COOLDOWN_SECONDS and last_token == token:
                        return  # cooldown active
        except Exception:
            pass

        try:
            with open(_FAILOVER_NOTIFY_STAMP, "w") as f:
                f.write(f"{now} {token}")
        except Exception:
            pass

        local_model = self._get_local_model()
        if translated:
            msg = (
                f"\U0001f501 LLM failover active — cloud quota exhausted ({token}). "
                f"Cron jobs running on {local_model} until cloud quota resets."
            )
        else:
            msg = (
                f"⚠️ LLM failover triggered ({token}) but no translator "
                f"available for this provider — cron job will fail."
            )

        try:
            gw_url = os.environ.get("GATEWAY_OP_PROXY_URL", "http://gateway:8080")
            bot_token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
            auth_token = os.environ.get("GATEWAY_AUTH_TOKEN", "")
            owner_chat = os.environ.get("AGENTSHROUD_OWNER_CHAT_ID", "8096968754")
            if not bot_token:
                return
            payload = json.dumps({"chat_id": owner_chat, "text": msg}).encode()
            req = urllib.request.Request(
                f"{gw_url}/telegram-api/bot{bot_token}/sendMessage",
                data=payload,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {auth_token}",
                    "X-AgentShroud-System": "1",
                },
            )
            urllib.request.urlopen(req, timeout=10)
        except Exception as e:
            logger.debug("Failover notification failed (non-fatal): %s", e)

    def _record_failover_event(self, provider: str, outcome: str, model: str) -> None:
        """Persist a failover event to the audit chain if wired."""
        import time as _time

        ts = _time.strftime("%Y-%m-%dT%H:%M:%SZ", _time.gmtime())
        self._stats["failover_active"] = outcome == "success"
        self._stats["failover_last_provider"] = provider
        self._stats["failover_last_event"] = ts

        if self.audit_chain is None:
            return
        try:
            content = f"LLM failover {outcome}: {provider} → {model} at {ts}"
            metadata = {
                "provider": provider,
                "outcome": outcome,
                "local_model": model,
                "timestamp": ts,
            }
            self.audit_chain.append(content, direction="llm_failover", metadata=metadata)
        except Exception as e:
            logger.debug("Failover audit log failed (non-fatal): %s", e)

    async def _failover_request(
        self,
        path: str,
        request_data: dict | None,
        _body: bytes,
        model_name: str,
        is_openai: bool,
    ) -> tuple[int, dict, bytes] | None:
        """Attempt a cloud→local failover dispatch.

        Returns (status, headers, body) from the local model, or None if the
        failover itself fails (caller should return the original cloud 429 body).
        """
        local_model = self._get_local_model()
        fo_base = self._local_failover_base(local_model)
        local_model = self._normalize_local_model(local_model, fo_base)
        is_google = "/v1beta" in path or "google" in path.lower()
        translate_back: str | None = None  # "anthropic" | "gemini" | None
        try:
            if is_openai:
                # OpenAI-compat is drop-in with local backends — just rewrite model
                fo_data = dict(request_data or {})
                fo_data["model"] = local_model
                fo_body = json.dumps(fo_data).encode()
                fo_url = f"{fo_base}/v1/chat/completions"
            elif "/v1/messages" in path:
                # Anthropic → translate to OpenAI, re-dispatch, translate response
                oai_req = anthropic_to_openai_request(request_data or {}, local_model)
                fo_body = json.dumps(oai_req).encode()
                fo_url = f"{fo_base}/v1/chat/completions"
                translate_back = "anthropic"
            elif is_google:
                # Gemini → translate to OpenAI, re-dispatch, translate response.
                # Non-streaming text only — streaming/tool requests pass through.
                reason = gemini_failover_unsupported_reason(request_data or {}, path)
                if reason is not None:
                    logger.warning(
                        "Gemini failover: streaming/tool requests unsupported — "
                        "passing through 429 (%s)",
                        reason,
                    )
                    return None
                oai_req = gemini_to_openai_request(request_data or {}, local_model)
                fo_body = json.dumps(oai_req).encode()
                fo_url = f"{fo_base}/v1/chat/completions"
                translate_back = "gemini"
            else:
                return None  # Unknown provider — no translator

            fo_headers = self._local_backend_headers(fo_base, {"content-type": "application/json"})
            f_status, f_headers, f_body = await self._forward_request(fo_url, fo_body, fo_headers)

            if f_status == 200 and f_body:
                if translate_back == "anthropic":
                    # Translate Ollama OpenAI response back to Anthropic format
                    try:
                        oai_resp = json.loads(f_body)
                        f_body = json.dumps(
                            openai_to_anthropic_response(oai_resp, model_name)
                        ).encode()
                    except Exception as te:
                        logger.warning("Response translation failed: %s", te)
                        return None
                elif translate_back == "gemini":
                    # Translate Ollama OpenAI response back to Gemini format
                    try:
                        oai_resp = json.loads(f_body)
                        f_body = json.dumps(openai_to_gemini_response(oai_resp)).encode()
                    except Exception as te:
                        logger.warning("Response translation failed: %s", te)
                        return None
                return f_status, f_headers, f_body

            logger.warning(
                "Failover local model returned HTTP %s — trying OpenAI cloud fallback", f_status
            )
        except Exception as e:
            logger.warning("Failover dispatch error: %s — trying OpenAI cloud fallback", e)
        # Cloud fallback: local model failed → try OpenAI gpt-4o-mini (non-streaming)
        _oai_key: str | None = None
        try:
            with open("/run/secrets/openai_api_key") as _kf:
                _oai_key = _kf.read().strip() or None
        except OSError:
            pass
        if _oai_key:
            try:
                _oai_model = "gpt-4o-mini"
                if is_openai:
                    _fo2_data = dict(request_data or {})
                    _fo2_data["model"] = _oai_model
                elif "/v1/messages" in path:
                    _fo2_data = anthropic_to_openai_request(request_data or {}, _oai_model)
                elif is_google:
                    _fo2_data = gemini_to_openai_request(request_data or {}, _oai_model)
                else:
                    return None
                if _fo2_data.get("max_tokens", 0) > 16384:
                    _fo2_data["max_tokens"] = 16384
                _fo2_body = json.dumps(_fo2_data).encode()
                _fo2_url = f"{OPENAI_API_BASE}/v1/chat/completions"
                _f2_status, _f2_hdrs, _f2_body = await self._forward_request(
                    _fo2_url,
                    _fo2_body,
                    {
                        "content-type": "application/json",
                        "authorization": f"Bearer {_oai_key}",
                    },
                )
                if _f2_status == 200 and _f2_body:
                    logger.info("Cloud failover (non-streaming) → OpenAI %s", _oai_model)
                    if translate_back == "anthropic":
                        _oai_resp = json.loads(_f2_body)
                        _f2_body = json.dumps(
                            openai_to_anthropic_response(_oai_resp, model_name)
                        ).encode()
                    elif translate_back == "gemini":
                        _oai_resp = json.loads(_f2_body)
                        _f2_body = json.dumps(openai_to_gemini_response(_oai_resp)).encode()
                    return _f2_status, _f2_hdrs, _f2_body
                logger.warning("Cloud failover (non-streaming) OpenAI returned HTTP %s", _f2_status)
            except Exception as _fe2:
                logger.warning("Cloud failover (non-streaming) error: %s", _fe2)
        return None

    # ---------------------------------------------------------------------------
    # Local backend availability helpers
    # ---------------------------------------------------------------------------

    @staticmethod
    def _is_connect_error(exc: BaseException) -> bool:
        """True for connection-level failures (refused / unreachable / reset).

        Unwraps urllib URLError to its underlying OS-level reason. HTTPError
        (a valid HTTP response) is never a connect error. Also matches httpx
        ConnectError/ConnectTimeout by name without importing httpx.
        """
        if isinstance(exc, urllib.error.HTTPError):
            return False
        if type(exc).__name__ in ("ConnectError", "ConnectTimeout"):
            return True
        if isinstance(exc, urllib.error.URLError) and isinstance(exc.reason, BaseException):
            exc = exc.reason
        return isinstance(exc, (ConnectionError, TimeoutError, OSError))

    def _local_backend_unavailable_response(
        self, base_url: str, exc: BaseException
    ) -> tuple[int, dict, bytes]:
        """Build a structured 503 for an unreachable local backend.

        Logs one WARNING per backend per _BACKEND_UNAVAILABLE_WARN_INTERVAL_SECONDS
        window (DEBUG otherwise) to avoid per-request log spam.
        """
        hint = _LOCAL_BACKEND_HINTS[base_url]
        now = time.monotonic()
        last = self._backend_unavailable_last_warn.get(base_url, float("-inf"))
        if now - last >= _BACKEND_UNAVAILABLE_WARN_INTERVAL_SECONDS:
            self._backend_unavailable_last_warn[base_url] = now
            logger.warning("Local LLM backend unreachable (%s): %s — %s", base_url, exc, hint)
        else:
            logger.debug("Local LLM backend unreachable (%s): %s", base_url, exc)
        body = json.dumps({"error": {"type": "backend_unavailable", "message": hint}}).encode()
        return 503, {"content-type": "application/json"}, body

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

        # Hermes v0.16.0+ routes ALL provider calls through its OpenAI client,
        # so a request for a Claude model arrives at /v1/chat/completions
        # with auth=`Bearer None` (hermes's empty api_key turned into a
        # literal "None" string).  Forwarding upstream to OpenAI fails with
        # 401 "no API key", killing competitive-intel cron jobs.
        #
        # When we detect this combo: rewrite path to /v1/messages, translate
        # the OpenAI body to Anthropic shape, substitute Authorization with
        # the gateway's own Anthropic key from /run/secrets/, translate the
        # response back to OpenAI shape on the way out.
        _claude_translation = False
        _original_model_name = model_name
        if is_openai and model_name and "claude" in model_name.lower() and request_data:
            try:
                anth_body = openai_to_anthropic_request(request_data, target_model=model_name)
                body = json.dumps(anth_body).encode()
                request_data = anth_body
                path = "/v1/messages"
                is_openai = False
                _claude_translation = True
                # Substitute Authorization with the gateway-side Anthropic
                # token.  Keep the original headers untouched otherwise.
                headers = dict(headers)
                try:
                    with open("/run/secrets/anthropic_oauth_token") as _f:
                        _gw_anthropic_key = _f.read().strip()
                except Exception:
                    _gw_anthropic_key = ""
                if _gw_anthropic_key:
                    headers["x-api-key"] = _gw_anthropic_key
                    headers["anthropic-version"] = "2023-06-01"
                    # Strip the broken Bearer header
                    headers.pop("authorization", None)
                    headers.pop("Authorization", None)
                logger.info(
                    "Claude-via-OpenAI-path: rewrote /v1/chat/completions → /v1/messages "
                    "for model %s",
                    model_name,
                )
            except Exception as e:
                logger.warning("Claude-via-OpenAI-path translation failed: %s", e)
                _claude_translation = False

        # "use Gemini" direct voice path (voice_gateway/server.py): a caller
        # speaking OpenAI's chat/completions format wants a real Gemini
        # reply. Mirrors the Claude-translation branch above: rewrite path to
        # Gemini's generateContent endpoint, translate the body, substitute
        # the gateway's own Google API key, translate the response back to
        # OpenAI shape on the way out (see _gemini_translation below).
        _gemini_translation = False
        if is_openai and model_name and "gemini" in model_name.lower() and request_data:
            try:
                gem_body = openai_to_gemini_request(request_data)
                body = json.dumps(gem_body).encode()
                request_data = gem_body
                path = f"/v1beta/models/{model_name}:generateContent"
                is_openai = False
                is_google = True
                _gemini_translation = True
                headers = dict(headers)
                try:
                    with open("/run/secrets/google_api_key") as _f:
                        _gw_google_key = _f.read().strip()
                except Exception:
                    _gw_google_key = ""
                if _gw_google_key:
                    headers["x-goog-api-key"] = _gw_google_key
                    headers.pop("authorization", None)
                    headers.pop("Authorization", None)
                logger.info(
                    "Gemini-via-OpenAI-path: rewrote /v1/chat/completions → "
                    "generateContent for model %s",
                    model_name,
                )
            except Exception as e:
                logger.warning("Gemini-via-OpenAI-path translation failed: %s", e)
                _gemini_translation = False

        local_keywords = [
            "qwen",
            "llama",
            "mistral",
            "deepseek",
            "phi",
            "ollama",
            "lmstudio",
            "mlxlm",
            "gemma",
            "fieldflare",
            # Rapid-MLX serves NVIDIA Nemotron 3.5 Lightning as of 2026-08-19
            # (RAPID_MLX_MODEL_ID below) — missing here meant any model alias
            # containing "nemotron" fell through to the is_openai branch and
            # got proxied to the real OpenAI.com API instead of routed via
            # LOCAL_MODEL_ROUTES, 404'ing with OpenAI's own "model not found"
            # (2026-08-21, found while fixing the qwen3-14b-rapid stale alias
            # in resolve_model.py — that rename alone wasn't sufficient).
            "nemotron",
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
                bare = model_name.split("/", 1)[1]
                if request_data is not None:
                    request_data["model"] = bare
                model_name = bare
                model_lower = model_name.lower()
                break

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
            # Round-trip model name through normalization so LM Studio receives
            # dash-separated IDs ('qwen3-14b') and Ollama keeps colons ('qwen3:14b').
            # Must happen after prefix stripping (ollama/ lmstudio/) above.
            if request_data:
                normalized = self._normalize_local_model(model_name, base_url)
                if normalized != model_name:
                    request_data["model"] = normalized
                    model_name = normalized
                    model_lower = model_name.lower()
                    body = json.dumps(request_data).encode()
                if base_url == RAPID_MLX_API_BASE:
                    changed_thinking = self._suppress_qwen3_thinking(request_data)
                    changed_tools = self._widen_optional_tool_param_types(request_data)
                    if changed_thinking or changed_tools:
                        body = json.dumps(request_data).encode()
            headers = self._local_backend_headers(base_url, headers)
        elif is_openai:
            base_url = OPENAI_API_BASE
            # Same gap the Claude-translation branch above exists to close:
            # callers of this plain (non-Claude, non-Gemini, non-local)
            # OpenAI path arrive with the GATEWAY's own internal auth token
            # (e.g. voice_gateway's "use ChatGPT" direct path sends
            # Authorization: Bearer <gateway token>), which OpenAI correctly
            # rejects with 401 — this proxy exists specifically so callers
            # never need their own real provider key. Substitute it here,
            # same secret-file convention as anthropic_oauth_token/google_api_key.
            headers = dict(headers)
            try:
                with open("/run/secrets/openai_api_key") as _f:
                    _gw_openai_key = _f.read().strip()
            except Exception:
                _gw_openai_key = ""
            if _gw_openai_key:
                headers["authorization"] = f"Bearer {_gw_openai_key}"
                headers.pop("Authorization", None)
                headers.pop("x-api-key", None)
        elif is_google:
            base_url = GOOGLE_API_BASE

        url = f"{base_url}{path}"

        # Check if streaming
        is_streaming = request_data and request_data.get("stream", False)

        # Per-request opt-out: X-AgentShroud-No-Failover: 1 skips quota failover
        _failover_opt_out = headers.get("x-agentshroud-no-failover", "") == "1"

        try:
            status, resp_headers, resp_body = await self._forward_request(url, body, headers)
        except TimeoutError as e:
            logger.error(f"LLM proxy timeout: {e}")
            # === LOCAL→SECONDARY FAILOVER: p99 timeout on primary local model ===
            # Before returning a graceful timeout, try the secondary local model.
            _local_oom_failover_enabled = (
                os.environ.get("AGENTSHROUD_LOCAL_FAILOVER_ON_OOM", "1") == "1"
            )
            if is_ollama and _local_oom_failover_enabled and not _failover_opt_out:
                logger.info("Local p99 timeout on primary — trying secondary local model")
                _sec_result = await self._local_secondary_failover_request(
                    path, request_data, is_openai
                )
                if _sec_result is not None:
                    return 200, {"content-type": "application/json"}, _sec_result[2]
            fallback_body = self._build_timeout_fallback_response(
                is_openai=is_openai,
                is_google=is_google,
                is_ollama=is_ollama,
                model_name=model_name or (request_data or {}).get("model", ""),
            )
            return 200, {"content-type": "application/json"}, fallback_body
        except Exception as e:
            # Local backend (mlx_lm / Ollama / LM Studio) connect failure →
            # structured 503 with an operator hint instead of a raw 502.
            if base_url in _LOCAL_BACKEND_HINTS and self._is_connect_error(e):
                return self._local_backend_unavailable_response(base_url, e)
            logger.error(f"LLM proxy error: {e}")
            error_resp = json.dumps(
                {
                    "type": "error",
                    "error": {"type": "api_error", "message": f"Gateway proxy error: {e}"},
                }
            ).encode()
            return 502, {"content-type": "application/json"}, error_resp

        # === LOCAL→SECONDARY FAILOVER: OOM on primary local model ===
        # Triggered when primary local backend returns OOM or backend_unavailable.
        # Only active for local model dispatches with AGENTSHROUD_LOCAL_FAILOVER_ON_OOM=1.
        _local_oom_failover_enabled = (
            os.environ.get("AGENTSHROUD_LOCAL_FAILOVER_ON_OOM", "1") == "1"
        )
        if (
            is_ollama
            and _local_oom_failover_enabled
            and not _failover_opt_out
            and not is_streaming
            and self._is_local_oom(status, resp_body)
        ):
            logger.info(
                "Local OOM detected (HTTP %s) — attempting local→secondary failover", status
            )
            _sec_result = await self._local_secondary_failover_request(
                path, request_data, is_openai
            )
            if _sec_result is not None:
                return 200, {"content-type": "application/json"}, _sec_result[2]
            # Secondary also failed — fall through to return original OOM response

        # === QUOTA FAILOVER: cloud→local on quota-exhausted responses ===
        _failover_enabled = os.environ.get("AGENTSHROUD_FAILOVER_ON_QUOTA", "1") == "1"
        if _failover_enabled and not _failover_opt_out and not is_ollama and not is_streaming:
            quota_hit, quota_token = is_quota_exhausted(status, resp_body)
            if not quota_hit:
                # Anthropic emits overloaded_error with HTTP 200/503/529 —
                # invisible to status-code checks but just as fatal to cron jobs.
                quota_hit, quota_token = is_overloaded(status, resp_body)
            if not quota_hit:
                # A 429 that survived _forward_request's retry loop
                # ({429,503,529}) is a persistent rate-limit, not a transient
                # one. Hermes treats the final 429 as AssertionError and
                # kills the cron run (observed 2026-06-13/14/15 — 3 days of
                # competitive reports missed). Failover so the run completes.
                quota_hit, quota_token = is_rate_limited_post_retry(status, resp_body)
            if quota_hit:
                local_model = self._get_local_model()
                logger.info(
                    "Quota failover triggered (%s) — attempting local model %s",
                    quota_token,
                    local_model,
                )
                fo_result = await self._failover_request(
                    path, request_data, body, model_name, is_openai
                )
                if fo_result is not None:
                    self._stats["failover_quota_succeeded"] = (
                        self._stats.get("failover_quota_succeeded", 0) + 1
                    )
                    self._record_failover_event(quota_token, "success", local_model)
                    self._emit_failover_notice(quota_token, translated=True)
                    return 200, {"content-type": "application/json"}, fo_result[2]
                else:
                    self._stats["failover_quota_failed"] = (
                        self._stats.get("failover_quota_failed", 0) + 1
                    )
                    self._record_failover_event(quota_token, "failed", local_model)
                    # Untranslatable provider/request: notify that no translation
                    # path exists. Gemini non-streaming text HAS a translator, so
                    # only notify for unsupported Gemini requests (streaming/tools)
                    # or truly unknown providers.
                    if not is_openai and "/v1/messages" not in path:
                        _no_translator = True
                        if is_google:
                            _no_translator = (
                                gemini_failover_unsupported_reason(request_data or {}, path)
                                is not None
                            )
                        if _no_translator:
                            self._emit_failover_notice(quota_token, translated=False)
                    # Fall through → return original cloud 429

        # Translate Anthropic response → OpenAI shape if we did the inbound flip
        if _claude_translation and status == 200 and resp_body:
            try:
                anth_resp = json.loads(resp_body)
                resp_body = json.dumps(
                    anthropic_to_openai_response(anth_resp, original_model=_original_model_name)
                ).encode()
                resp_headers = {**resp_headers, "content-type": "application/json"}
            except Exception as e:
                logger.warning("Claude→OpenAI response translation failed: %s", e)

        # Translate Gemini response → OpenAI shape if we did the inbound flip
        if _gemini_translation and status == 200 and resp_body:
            try:
                gem_resp = json.loads(resp_body)
                resp_body = json.dumps(
                    gemini_to_openai_response(gem_resp, original_model=_original_model_name)
                ).encode()
                resp_headers = {**resp_headers, "content-type": "application/json"}
            except Exception as e:
                logger.warning("Gemini→OpenAI response translation failed: %s", e)

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
            "gemma",
            "fieldflare",
            # Rapid-MLX serves NVIDIA Nemotron 3.5 Lightning as of 2026-08-19
            # (RAPID_MLX_MODEL_ID below) — missing here meant any model alias
            # containing "nemotron" fell through to the is_openai branch and
            # got proxied to the real OpenAI.com API instead of routed via
            # LOCAL_MODEL_ROUTES, 404'ing with OpenAI's own "model not found"
            # (2026-08-21, found while fixing the qwen3-14b-rapid stale alias
            # in resolve_model.py — that rename alone wasn't sufficient).
            "nemotron",
        ]
        is_ollama = (
            any(k in model_lower for k in local_keywords)
            or model_lower.startswith("ollama/")
            or model_lower.startswith("lmstudio/")
        )

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
            # Same normalization + thinking-suppression as proxy_messages — this
            # streaming path resolved base_url correctly but never rewrote the
            # payload itself, so "qwen3-14b-rapid" was forwarded unchanged and
            # 404'd against Rapid-MLX (confirmed live 2026-08-18: every OpenClaw
            # job failed with "couldn't generate a response" because OpenClaw
            # always sends stream:true, which only ever hit this function).
            if request_data:
                normalized = self._normalize_local_model(model_name, base_url)
                if normalized != model_name:
                    request_data["model"] = normalized
                    model_name = normalized
                    model_lower = model_name.lower()
                if base_url == RAPID_MLX_API_BASE:
                    self._suppress_qwen3_thinking(request_data)
                    self._widen_optional_tool_param_types(request_data)
                body = json.dumps(request_data).encode()
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

        if self.credential_injector and base_url == ANTHROPIC_API_BASE:
            self.credential_injector.inject_headers("api.anthropic.com", forward_headers)
        if is_ollama:
            forward_headers = self._local_backend_headers(base_url, forward_headers)

        _failover_opt_out = headers.get("x-agentshroud-no-failover", "") == "1"
        _failover_enabled = os.environ.get("AGENTSHROUD_FAILOVER_ON_QUOTA", "1") == "1"

        async def _stream() -> AsyncIterator[bytes]:
            import httpx as _httpx

            collected_status: list[int] = []

            try:
                async with _httpx.AsyncClient(
                    verify=True, timeout=_httpx.Timeout(LLM_CONNECT_TIMEOUT_SECONDS, read=1800.0)
                ) as client:
                    async with client.stream(
                        "POST", url, content=body, headers=forward_headers
                    ) as response:
                        collected_status.append(response.status_code)
                        # Quota failover only possible on error status codes (429, 402).
                        # For 200 responses stream immediately — buffering first_chunk and
                        # yielding it last caused content_block_start to arrive before
                        # message_start, breaking the Anthropic SDK streaming parser.
                        if (
                            _failover_enabled
                            and not _failover_opt_out
                            and not is_ollama
                            # 400 included so the Claude.ai OAuth "out of extra usage"
                            # quota wall (returned as invalid_request_error / HTTP 400)
                            # still triggers failover instead of crash-looping cron jobs.
                            # 500 included for provider capacity errors (SCRUM-60) —
                            # is_overloaded requires capacity wording at 500, so
                            # deterministic request-caused 500s never fail over.
                            and response.status_code in (400, 429, 402, 500, 503, 529)
                        ):
                            # Error body is small JSON — safe to read in full
                            error_body = await response.aread()
                            quota_hit, quota_token = is_quota_exhausted(
                                response.status_code, error_body
                            )
                            if not quota_hit:
                                quota_hit, quota_token = is_overloaded(
                                    response.status_code, error_body
                                )
                            if quota_hit:
                                local_model = self._get_local_model()
                                fo_base = self._local_failover_base(local_model)
                                local_model = self._normalize_local_model(local_model, fo_base)
                                logger.info(
                                    "Streaming quota failover (%s) → %s",
                                    quota_token,
                                    local_model,
                                )
                                try:
                                    if is_openai:
                                        fo_data = dict(request_data or {})
                                        fo_data["model"] = local_model
                                        fo_body = json.dumps(fo_data).encode()
                                        fo_url = f"{fo_base}/v1/chat/completions"
                                    elif "/v1/messages" in path:
                                        oai_req = anthropic_to_openai_request(
                                            request_data or {}, local_model
                                        )
                                        fo_body = json.dumps(oai_req).encode()
                                        fo_url = f"{fo_base}/v1/chat/completions"
                                    else:
                                        self._emit_failover_notice(quota_token, translated=False)
                                        yield error_body
                                        return

                                    async with _httpx.AsyncClient(
                                        verify=True,
                                        timeout=_httpx.Timeout(
                                            LLM_CONNECT_TIMEOUT_SECONDS, read=1800.0
                                        ),
                                    ) as fo_client:
                                        async with fo_client.stream(
                                            "POST",
                                            fo_url,
                                            content=fo_body,
                                            headers=self._local_backend_headers(
                                                fo_base, {"content-type": "application/json"}
                                            ),
                                        ) as fo_resp:
                                            if fo_resp.status_code == 200:
                                                self._stats["failover_quota_succeeded"] = (
                                                    self._stats.get("failover_quota_succeeded", 0)
                                                    + 1
                                                )
                                                self._record_failover_event(
                                                    quota_token, "success", local_model
                                                )
                                                self._emit_failover_notice(
                                                    quota_token, translated=True
                                                )
                                                if "/v1/messages" in path:
                                                    async for (
                                                        translated
                                                    ) in translate_openai_sse_to_anthropic(
                                                        fo_resp.aiter_bytes(), model_name
                                                    ):
                                                        yield translated
                                                else:
                                                    async for fo_chunk in fo_resp.aiter_bytes():
                                                        if fo_chunk:
                                                            yield fo_chunk
                                                return
                                except Exception as fe:
                                    logger.warning("Streaming failover error: %s", fe)
                                # Failover failed — fall through, yield original error body
                                self._stats["failover_quota_failed"] = (
                                    self._stats.get("failover_quota_failed", 0) + 1
                                )
                                # Cloud failover: local model unavailable → try OpenAI
                                _oai_key: str | None = None
                                try:
                                    with open("/run/secrets/openai_api_key") as _kf:
                                        _oai_key = _kf.read().strip() or None
                                except OSError:
                                    pass
                                if _oai_key:
                                    try:
                                        _oai_model = "gpt-4o-mini"
                                        if is_openai:
                                            _fo2_data = dict(request_data or {})
                                            _fo2_data["model"] = _oai_model
                                        else:
                                            _fo2_data = anthropic_to_openai_request(
                                                request_data or {}, _oai_model
                                            )
                                        # gpt-4o-mini max completion tokens = 16384
                                        if _fo2_data.get("max_tokens", 0) > 16384:
                                            _fo2_data["max_tokens"] = 16384
                                        _fo2_body = json.dumps(_fo2_data).encode()
                                        _fo2_url = f"{OPENAI_API_BASE}/v1/chat/completions"
                                        async with _httpx.AsyncClient(
                                            verify=True,
                                            timeout=_httpx.Timeout(
                                                LLM_CONNECT_TIMEOUT_SECONDS, read=1800.0
                                            ),
                                        ) as _fo2_client:
                                            async with _fo2_client.stream(
                                                "POST",
                                                _fo2_url,
                                                content=_fo2_body,
                                                headers={
                                                    "content-type": "application/json",
                                                    "authorization": f"Bearer {_oai_key}",
                                                },
                                            ) as _fo2_resp:
                                                if _fo2_resp.status_code == 200:
                                                    logger.info(
                                                        "Cloud failover → OpenAI %s",
                                                        _oai_model,
                                                    )
                                                    if "/v1/messages" in path:
                                                        async for (
                                                            _t
                                                        ) in translate_openai_sse_to_anthropic(
                                                            _fo2_resp.aiter_bytes(),
                                                            model_name,
                                                        ):
                                                            yield _t
                                                    else:
                                                        async for (
                                                            _fo2_chunk
                                                        ) in _fo2_resp.aiter_bytes():
                                                            if _fo2_chunk:
                                                                yield _fo2_chunk
                                                    return
                                                else:
                                                    _fo2_err = await _fo2_resp.aread()
                                                    logger.warning(
                                                        "Cloud failover OpenAI %s: %s",
                                                        _fo2_resp.status_code,
                                                        _fo2_err[:300],
                                                    )
                                    except Exception as _fe2:
                                        logger.warning("Cloud failover (OpenAI) error: %s", _fe2)
                            yield error_body
                        else:
                            # Normal streaming — forward chunks immediately, no buffering
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
                            cleaned = re.sub(
                                r"<think>[\s\S]*?</think>\s*", "", msg["content"]
                            ).strip()
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
        if self.tool_acl_enforcer is None:
            return resp_body
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
        """Filter buffered SSE-like streaming responses for XML/credential leaks and ToolACL."""

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

            modified_event = await self._filter_streaming_event(event, user_id=user_id)
            if modified_event is not event:
                modified_any = True
            out_lines.append(f"data: {json.dumps(modified_event, separators=(',', ':'))}")

        if not modified_any:
            return resp_body

        self._stats["streaming_responses_scanned"] += 1
        return ("\n".join(out_lines) + "\n").encode("utf-8")

    async def _filter_streaming_event(
        self, event: dict[str, Any], user_id: str = "unknown"
    ) -> dict[str, Any]:
        """Apply outbound text filters to known streaming response formats.

        Also enforces ToolACL on Anthropic content_block_start events so that
        streaming responses receive the same terminal_tool / PRIVATE_TOOLS protection
        as non-streaming responses (CVE-2026-9367 streaming path fix).
        """
        # CVE-2026-9367: gate tool_use blocks in Anthropic streaming events.
        if (
            self.tool_acl_enforcer
            and user_id != "unknown"
            and event.get("type") == "content_block_start"
        ):
            cb = event.get("content_block", {})
            if isinstance(cb, dict) and cb.get("type") == "tool_use":
                tool_name = cb.get("name", "")
                allowed, reason = self.tool_acl_enforcer.can_use_tool(user_id, tool_name)
                if not allowed:
                    logger.warning(
                        "LLMProxy ToolACL (streaming): blocked tool_use user=%s tool=%s reason=%s",
                        user_id,
                        tool_name,
                        reason,
                    )
                    self._stats["responses_filtered"] += 1
                    return {
                        "type": "content_block_start",
                        "index": event.get("index", 0),
                        "content_block": {
                            "type": "text",
                            "text": f"[AgentShroud] Tool '{tool_name}' is not permitted for your role. {reason}",
                        },
                    }

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

        if self.credential_injector and url.startswith(ANTHROPIC_API_BASE):
            self.credential_injector.inject_headers("api.anthropic.com", forward_headers)

        _RETRYABLE = {429, 503, 529}  # 529 = Anthropic "overloaded"
        _MAX_RETRIES = 3
        if headers.get("x-agentshroud-interactive", "") == "1":
            # Interactive callers (voice gateway) need an answer in seconds:
            # skip the ~15 s retry preamble so the first 429/503 falls straight
            # through to quota failover (local model).  Cron/batch callers keep
            # the full retry loop — for them, waiting out a transient 429 for a
            # cloud-quality reply beats a fast local-model answer.
            _MAX_RETRIES = 0
        loop = asyncio.get_event_loop()

        for _attempt in range(_MAX_RETRIES + 1):
            req = urllib.request.Request(url, data=body, headers=forward_headers)

            def _urlopen_and_read(_req=req):
                # SCRUM-154: the ENTIRE urlopen+read+close sequence must run
                # on the executor thread, not just urlopen(). response.read()
                # blocks until the full body arrives — for a chunked stream
                # from a slow/stalled backend (local model server, cloud
                # API), that used to happen directly on the event loop,
                # freezing every other request the gateway was handling
                # (including bare GET /status, which has no dependency on
                # this code path at all) for up to the full socket timeout.
                # Confirmed live via py-spy: MainThread blocked in exactly
                # this read() during a real production hang.
                response = urllib.request.urlopen(_req, timeout=1800, context=self._ssl_context)
                try:
                    return response.status, dict(response.headers), response.read()
                finally:
                    response.close()

            try:
                response_status, resp_headers, resp_body = await loop.run_in_executor(
                    None, _urlopen_and_read
                )
                return response_status, resp_headers, resp_body
            except urllib.error.HTTPError as e:

                def _read_error_body(_e=e):
                    try:
                        return dict(_e.headers), _e.read()
                    finally:
                        _e.close()

                resp_headers, resp_body = await loop.run_in_executor(None, _read_error_body)
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

        # Final-attempt always returns inside the except block above; this is unreachable.
        return 503, {}, b'{"error":{"type":"max_retries_exceeded"}}'
