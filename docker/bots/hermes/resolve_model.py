#!/usr/bin/env python3
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Resolve the model + provider Hermes should use, honouring local-model parity.

SCRUM-70 (WS-C) — Full local-model parity for both bots.

switch_model.sh writes HERMES_MAIN_MODEL / AGENTSHROUD_MODEL_MODE and docker-compose
passes them into the Hermes container, but nothing inside the container applied them
to Hermes' config.yaml — start.sh hard-locked model.default to a cloud model on every
boot, so Hermes ignored local mode entirely.

This script is the missing Hermes-side resolver. Given the mode and the model refs
already present in the container environment, it emits the bare model name and the
Hermes provider key so start.sh / init-config.sh can run:

    hermes config set model.default  "$(python3 resolve_model.py model)"
    hermes config set model.provider "$(python3 resolve_model.py provider)"

It is intentionally self-contained (no gateway imports) so it runs inside the
nousresearch/hermes-agent image, which does not ship the AgentShroud gateway package.
The routing/normalisation on the wire is done by the gateway LLM proxy
(gateway/proxy/llm_proxy.py); this only decides what name Hermes should *send*.
"""

from __future__ import annotations

import os
import sys

# Provider-prefixed refs emitted by switch_model.sh, e.g. "ollama/qwen3:14b",
# "lmstudio/qwen3-14b", "openai-local/qwen3.8-27b-mlx", "anthropic/claude-opus-4-7".
_KNOWN_PREFIXES = (
    "ollama/",
    "lmstudio/",
    "openai-local/",
    "anthropic/",
    "openai/",
    "google/",
    "gemini/",
)

# Keyword → Hermes provider key. Matched against the bare (prefix-stripped) model
# name, lowercased. Mirrors the local-keyword classification the gateway LLM proxy
# uses (gateway/proxy/llm_proxy.py:582) so both sides agree on what is "local".
#
# "nemotron" added 2026-08-23: NVIDIA Nemotron 3.5 Lightning is the PR #390
# anchor/general local default (gateway/proxy/llm_proxy.py's RAPID_MLX_MODEL_ID),
# but its name has no keyword overlap with the original list. Before this was
# added, a HERMES_MAIN_MODEL naming it directly (e.g.
# "openai-local/nemotron-3.5-lightning-rapid") was misclassified as needing a
# cloud provider and silently fell through to Anthropic even with
# AGENTSHROUD_MODEL_MODE=local — the only reason production didn't hit this
# live is that its env still carries the older "qwen3-14b-rapid" stale-alias
# workaround (recognized via "qwen"), which _apply_stale_alias_correction then
# renames to nemotron *after* the local/cloud decision was already made.
_LOCAL_KEYWORDS = ("qwen", "llama", "mistral", "deepseek", "phi", "gemma", "nemotron")

# Safe fallback when nothing is configured — Hermes must always have a model.
_DEFAULT_CLOUD_MODEL = "claude-haiku-4-5-20251001"
_DEFAULT_CLOUD_PROVIDER = "anthropic"

_LOCAL_MODES = ("local", "local-multi")

# Stale-alias corrections: bare model names that AGENTSHROUD_LOCAL_MODEL_REF /
# HERMES_MAIN_MODEL may still carry from before a backend swap changed what's
# actually served, remapped to the name Hermes should use instead.
#
# "qwen3-14b-rapid" → "nemotron-3.5-lightning-rapid" (2026-08-21): Rapid-MLX's
# served model was switched from Qwen3-14B to NVIDIA Nemotron 3.5 Lightning on
# 2026-08-19 (gateway/proxy/llm_proxy.py's RAPID_MLX_MODEL_ID), but the
# Hermes-facing alias was never renamed to match. Hermes's own
# agent/reasoning_timeouts.py floor table matches by the model name it was
# TOLD (not the real weights the gateway proxies to), so it kept applying the
# "qwen3" family's 180s stale-call floor instead of "nemotron-3.5-lightning"'s
# 300s floor — killing real generation turns ~100s before they would have
# completed (observed: 278s actual vs 180s applied threshold), silently
# leaving every affected cron job's output with just its header. The new
# alias is also registered in llm_proxy.py's LOCAL_MODEL_ROUTES so routing is
# unaffected; only the name Hermes uses to decide its own timeout changes.
_STALE_ALIAS_CORRECTIONS = {
    "qwen3-14b-rapid": "nemotron-3.5-lightning-rapid",
}


def _apply_stale_alias_correction(model: str) -> str:
    return _STALE_ALIAS_CORRECTIONS.get(model, model)


def strip_provider_prefix(ref: str) -> str:
    """Strip a known provider prefix from a model ref, leaving the bare model name.

    'ollama/qwen3:14b' → 'qwen3:14b'; 'qwen3:14b' (no prefix) → 'qwen3:14b'.
    """
    if not ref:
        return ""
    for prefix in _KNOWN_PREFIXES:
        if ref.startswith(prefix):
            return ref[len(prefix) :]
    return ref


def provider_for_model(model: str) -> str:
    """Return the Hermes provider key for a bare model name.

    Local models (qwen/llama/mistral/deepseek/phi/gemma) → 'ollama' (Hermes reaches
    the local backend via OLLAMA_BASE_URL=http://gateway:8080/v1, and the gateway
    proxy routes by model keyword to Ollama / LM Studio / mlx_lm). Claude → anthropic,
    GPT → openai, Gemini → google.
    """
    ml = (model or "").lower()
    if any(kw in ml for kw in _LOCAL_KEYWORDS):
        return "ollama"
    if "claude" in ml:
        return "anthropic"
    if "gpt" in ml or ml.startswith("o1") or ml.startswith("o3"):
        return "openai"
    if "gemini" in ml:
        return "google"
    # Unknown bare name: default to anthropic so cloud auth path is used.
    return _DEFAULT_CLOUD_PROVIDER


def resolve_model(
    mode: str,
    hermes_main_model: str,
    local_model_ref: str,
    cloud_model_ref: str,
) -> tuple[str, str]:
    """Resolve (model, provider) for Hermes from the container environment.

    Precedence:
      local / local-multi mode:
        1. HERMES_MAIN_MODEL if it names a local model
        2. AGENTSHROUD_LOCAL_MODEL_REF
        (a stale *cloud* HERMES_MAIN_MODEL is ignored in local mode — this is the
         exact parity bug being fixed)
      cloud mode (or unknown mode, treated as cloud):
        1. HERMES_MAIN_MODEL
        2. AGENTSHROUD_CLOUD_MODEL_REF
        3. safe Anthropic default
    """
    norm_mode = (mode or "").strip().lower()
    main_bare = strip_provider_prefix(hermes_main_model.strip() if hermes_main_model else "")

    if norm_mode in _LOCAL_MODES:
        # Prefer HERMES_MAIN_MODEL only if it is actually a local model; a leftover
        # cloud ref must not leak into local mode.
        if main_bare and provider_for_model(main_bare) == "ollama":
            model = main_bare
        else:
            model = strip_provider_prefix(local_model_ref.strip() if local_model_ref else "")
        if not model:
            # Local mode requested but no local ref supplied — fall back to the
            # documented anchor default so Hermes still starts locally. Was
            # "qwen3:14b" (pre-PR#390); the dev host's AGENTSHROUD_LOCAL_MODEL_REF
            # was left unset, so it silently kept resolving to this stale
            # fallback for 9+ days after prod moved to the new anchor model
            # (nemotron-3.5-lightning-rapid, PR #390's LOCAL_MODEL_ROUTES).
            model = "nemotron-3.5-lightning-rapid"
        return _apply_stale_alias_correction(model), "ollama"

    # Cloud (or unknown) mode.
    if main_bare:
        model = main_bare
    else:
        model = strip_provider_prefix(cloud_model_ref.strip() if cloud_model_ref else "")
    if not model:
        return _DEFAULT_CLOUD_MODEL, _DEFAULT_CLOUD_PROVIDER
    return model, provider_for_model(model)


def _resolve_from_env() -> tuple[str, str]:
    return resolve_model(
        mode=os.environ.get("AGENTSHROUD_MODEL_MODE", "cloud"),
        hermes_main_model=os.environ.get("HERMES_MAIN_MODEL", ""),
        local_model_ref=os.environ.get("AGENTSHROUD_LOCAL_MODEL_REF", ""),
        cloud_model_ref=os.environ.get("AGENTSHROUD_CLOUD_MODEL_REF", ""),
    )


def main(argv: list[str]) -> int:
    """CLI: `resolve_model.py [model|provider]`. Defaults to 'model'."""
    key = argv[0] if argv else "model"
    if key not in ("model", "provider"):
        sys.stderr.write(f"resolve_model: unknown key {key!r} (expected 'model' or 'provider')\n")
        return 2
    model, provider = _resolve_from_env()
    sys.stdout.write(f"{model if key == 'model' else provider}\n")
    return 0


if __name__ == "__main__":  # pragma: no cover - exercised via main() in tests
    sys.exit(main(sys.argv[1:]))
