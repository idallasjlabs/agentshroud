# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Tests for the Hermes model resolver (SCRUM-70 — WS-C local-model parity).

The resolver is the missing Hermes-side half of local-model parity: switch_model.sh
already writes HERMES_MAIN_MODEL / AGENTSHROUD_MODEL_MODE and docker-compose passes
them into the Hermes container, but nothing inside the container applied them to
config.yaml — start.sh hard-locked model.default to a cloud model on every boot.

This resolver maps (mode, refs) → the (model, provider) Hermes must set via
`hermes config set`, so Hermes runs fully local with no cloud dependency.

The module under test lives in the Hermes image (docker/bots/hermes/resolve_model.py)
and is self-contained (no gateway imports) so it works inside that image. We load it
here by file path.
"""

from __future__ import annotations

import importlib.util
import pathlib

import pytest

_RESOLVER_PATH = (
    pathlib.Path(__file__).resolve().parents[2] / "docker" / "bots" / "hermes" / "resolve_model.py"
)


def _load_resolver():
    spec = importlib.util.spec_from_file_location("hermes_resolve_model", _RESOLVER_PATH)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


resolver = _load_resolver()
resolve_model = resolver.resolve_model
strip_provider_prefix = resolver.strip_provider_prefix
provider_for_model = resolver.provider_for_model


# ---------------------------------------------------------------------------
# strip_provider_prefix
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "ref,expected",
    [
        ("ollama/qwen3:14b", "qwen3:14b"),
        ("lmstudio/qwen3-14b", "qwen3-14b"),
        ("openai-local/qwen3.6-27b", "qwen3.6-27b"),
        ("anthropic/claude-opus-4-7", "claude-opus-4-7"),
        ("google/gemini-3-pro", "gemini-3-pro"),
        ("qwen3:14b", "qwen3:14b"),  # no prefix — unchanged
        ("", ""),
    ],
)
def test_strip_provider_prefix(ref, expected):
    assert strip_provider_prefix(ref) == expected


# ---------------------------------------------------------------------------
# provider_for_model — Hermes provider keyword classification
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "model,expected",
    [
        ("qwen3:14b", "ollama"),
        ("qwen3-14b", "ollama"),
        ("llama3.1:8b", "ollama"),
        ("mistral-7b", "ollama"),
        ("deepseek-r1", "ollama"),
        ("phi-4", "ollama"),
        ("claude-opus-4-7", "anthropic"),
        ("claude-haiku-4-5-20251001", "anthropic"),
        ("gpt-5", "openai"),
        ("gpt-4o-mini", "openai"),
        ("gemini-3-pro", "google"),
        ("some-unknown-model", "anthropic"),  # unknown bare name → safe cloud default
    ],
)
def test_provider_for_model(model, expected):
    assert provider_for_model(model) == expected


def test_local_mode_empty_local_ref_falls_back_to_default_local_model():
    """local mode requested but neither HERMES_MAIN_MODEL nor local ref is local.

    Must still start locally on the documented default (qwen3:14b), never cloud.
    """
    model, provider = resolve_model(
        mode="local",
        hermes_main_model="",
        local_model_ref="",
        cloud_model_ref="anthropic/claude-opus-4-7",
    )
    assert model == "qwen3:14b"
    assert provider == "ollama"


# ---------------------------------------------------------------------------
# resolve_model — full mode-aware resolution
# ---------------------------------------------------------------------------


def test_local_mode_uses_hermes_main_model():
    """local mode with HERMES_MAIN_MODEL set → bare local model + ollama provider."""
    model, provider = resolve_model(
        mode="local",
        hermes_main_model="ollama/qwen3:14b",
        local_model_ref="ollama/qwen3:14b",
        cloud_model_ref="anthropic/claude-opus-4-7",
    )
    assert model == "qwen3:14b"
    assert provider == "ollama"


def test_local_mode_falls_back_to_local_ref_when_main_unset():
    """local mode, HERMES_MAIN_MODEL empty → use AGENTSHROUD_LOCAL_MODEL_REF."""
    model, provider = resolve_model(
        mode="local",
        hermes_main_model="",
        local_model_ref="ollama/qwen3:14b",
        cloud_model_ref="anthropic/claude-opus-4-7",
    )
    assert model == "qwen3:14b"
    assert provider == "ollama"


def test_local_multi_mode_uses_lmstudio_dash_model():
    """local-multi mode: LM Studio dash-style anchor model → ollama provider."""
    model, provider = resolve_model(
        mode="local-multi",
        hermes_main_model="openai-local/qwen3-coder-30b-a3b-instruct",
        local_model_ref="openai-local/qwen3-coder-30b-a3b-instruct",
        cloud_model_ref="anthropic/claude-opus-4-7",
    )
    assert model == "qwen3-coder-30b-a3b-instruct"
    assert provider == "ollama"


def test_cloud_mode_uses_hermes_main_model_when_claude():
    """cloud mode with a Claude HERMES_MAIN_MODEL → that model + anthropic provider."""
    model, provider = resolve_model(
        mode="cloud",
        hermes_main_model="anthropic/claude-opus-4-7",
        local_model_ref="ollama/qwen3:14b",
        cloud_model_ref="anthropic/claude-opus-4-7",
    )
    assert model == "claude-opus-4-7"
    assert provider == "anthropic"


def test_cloud_mode_openai_model():
    """cloud mode with an OpenAI HERMES_MAIN_MODEL → openai provider."""
    model, provider = resolve_model(
        mode="cloud",
        hermes_main_model="openai/gpt-5",
        local_model_ref="ollama/qwen3:14b",
        cloud_model_ref="openai/gpt-5",
    )
    assert model == "gpt-5"
    assert provider == "openai"


def test_cloud_mode_falls_back_to_cloud_ref_when_main_unset():
    """cloud mode, HERMES_MAIN_MODEL empty → use AGENTSHROUD_CLOUD_MODEL_REF."""
    model, provider = resolve_model(
        mode="cloud",
        hermes_main_model="",
        local_model_ref="ollama/qwen3:14b",
        cloud_model_ref="anthropic/claude-opus-4-7",
    )
    assert model == "claude-opus-4-7"
    assert provider == "anthropic"


def test_cloud_mode_no_refs_returns_safe_default():
    """cloud mode with everything unset → safe Anthropic default, never empty."""
    model, provider = resolve_model(
        mode="cloud",
        hermes_main_model="",
        local_model_ref="",
        cloud_model_ref="",
    )
    assert model  # never empty — Hermes must always have a model
    assert provider == "anthropic"


def test_unknown_mode_treated_as_cloud():
    """An unrecognized mode value is treated conservatively as cloud."""
    model, provider = resolve_model(
        mode="banana",
        hermes_main_model="anthropic/claude-opus-4-7",
        local_model_ref="ollama/qwen3:14b",
        cloud_model_ref="anthropic/claude-opus-4-7",
    )
    assert model == "claude-opus-4-7"
    assert provider == "anthropic"


def test_local_mode_ignores_stale_cloud_main_model():
    """local mode must not use a stale cloud HERMES_MAIN_MODEL.

    Guards against the exact parity bug: env carrying a leftover cloud model ref
    while mode=local. Local mode must resolve to a local model, never Claude.
    """
    model, provider = resolve_model(
        mode="local",
        hermes_main_model="anthropic/claude-opus-4-7",  # stale cloud ref
        local_model_ref="ollama/qwen3:14b",
        cloud_model_ref="anthropic/claude-opus-4-7",
    )
    assert model == "qwen3:14b"
    assert provider == "ollama"


def test_mode_case_insensitive_and_whitespace_tolerant():
    """Mode comparison tolerates case and surrounding whitespace from env files."""
    model, provider = resolve_model(
        mode="  LOCAL  ",
        hermes_main_model="ollama/qwen3:14b",
        local_model_ref="ollama/qwen3:14b",
        cloud_model_ref="anthropic/claude-opus-4-7",
    )
    assert model == "qwen3:14b"
    assert provider == "ollama"


# ---------------------------------------------------------------------------
# CLI entry point — start.sh calls `python3 resolve_model.py <key>`
# ---------------------------------------------------------------------------


def test_cli_emits_model_line(monkeypatch, capsys):
    monkeypatch.setenv("AGENTSHROUD_MODEL_MODE", "local")
    monkeypatch.setenv("HERMES_MAIN_MODEL", "ollama/qwen3:14b")
    monkeypatch.setenv("AGENTSHROUD_LOCAL_MODEL_REF", "ollama/qwen3:14b")
    monkeypatch.setenv("AGENTSHROUD_CLOUD_MODEL_REF", "anthropic/claude-opus-4-7")
    rc = resolver.main(["model"])
    out = capsys.readouterr().out.strip()
    assert rc == 0
    assert out == "qwen3:14b"


def test_cli_emits_provider_line(monkeypatch, capsys):
    monkeypatch.setenv("AGENTSHROUD_MODEL_MODE", "local")
    monkeypatch.setenv("HERMES_MAIN_MODEL", "ollama/qwen3:14b")
    monkeypatch.setenv("AGENTSHROUD_LOCAL_MODEL_REF", "ollama/qwen3:14b")
    monkeypatch.setenv("AGENTSHROUD_CLOUD_MODEL_REF", "anthropic/claude-opus-4-7")
    rc = resolver.main(["provider"])
    out = capsys.readouterr().out.strip()
    assert rc == 0
    assert out == "ollama"


def test_cli_unknown_key_returns_nonzero(monkeypatch, capsys):
    monkeypatch.setenv("AGENTSHROUD_MODEL_MODE", "cloud")
    rc = resolver.main(["bogus"])
    assert rc == 2


def test_cli_default_key_is_model(monkeypatch, capsys):
    """No arg → emit the model (start.sh convenience)."""
    monkeypatch.setenv("AGENTSHROUD_MODEL_MODE", "cloud")
    monkeypatch.setenv("HERMES_MAIN_MODEL", "anthropic/claude-opus-4-7")
    rc = resolver.main([])
    out = capsys.readouterr().out.strip()
    assert rc == 0
    assert out == "claude-opus-4-7"
