# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for SCRUM-89 config hot-reload (config.py).

Covers the validated, fail-safe reload path:
  * A valid on-disk change is applied to the reloadable subset.
  * An invalid on-disk change is rejected; the last-good config is kept.
  * Non-reloadable (startup-only) settings are never hot-swapped, even when
    the new file changes them.
  * The reload function is pure/injectable — the file path is provided via
    tmp_path, so no real filesystem watch runs in the unit test.
  * The mtime-poll watcher triggers a reload only when the file mtime changes.

No network, no sleep, no real background watch.
"""

from __future__ import annotations

import asyncio
from pathlib import Path

import pytest

from gateway.ingest_api.config import (
    RELOADABLE_FIELDS,
    STARTUP_ONLY_FIELDS,
    GatewayConfig,
    _default_mtime,
    apply_reloadable_config,
    config_watcher,
    load_config,
    reload_config,
    resolve_config_path,
)

# A minimal-but-valid YAML that load_config() accepts.
_BASE_YAML = """\
security:
  pii_min_confidence: 0.9
  pii_redaction: true
  redaction_rules:
    - type: "SSN"
      enabled: true
gateway:
  bind: "127.0.0.1"
  port: 8080
  auth_token: "startup-token-original"
proxy:
  allowed_domains:
    - "api.anthropic.com"
logging:
  level: "INFO"
channels:
  email:
    rate_limit_per_hour: 10
"""


def _write(path: Path, text: str) -> Path:
    path.write_text(text)
    return path


def _load(path: Path) -> GatewayConfig:
    return load_config(path)


# --------------------------------------------------------------------------- #
# Field partition sanity
# --------------------------------------------------------------------------- #
def test_field_partition_is_disjoint_and_covers_model():
    """Every GatewayConfig field is classified exactly once, disjointly."""
    model_fields = set(GatewayConfig.model_fields.keys())
    reloadable = set(RELOADABLE_FIELDS)
    startup = set(STARTUP_ONLY_FIELDS)

    assert reloadable.isdisjoint(startup), "a field cannot be both reloadable and startup-only"
    assert reloadable | startup == model_fields, "partition must cover every model field"
    # Security-critical fields must be startup-only (cannot hot-swap safely).
    for f in ("bind", "port", "auth_token", "auth_method", "ledger", "bots"):
        assert f in startup


# --------------------------------------------------------------------------- #
# apply_reloadable_config — pure swap
# --------------------------------------------------------------------------- #
def test_apply_swaps_only_reloadable_fields(tmp_path):
    current = _load(_write(tmp_path / "a.yaml", _BASE_YAML))
    original_token = current.auth_token
    original_port = current.port

    new_yaml = (
        _BASE_YAML.replace('level: "INFO"', 'level: "DEBUG"')
        .replace('auth_token: "startup-token-original"', 'auth_token: "attacker-swapped-token"')
        .replace("port: 8080", "port: 9999")
    )
    new = _load(_write(tmp_path / "b.yaml", new_yaml))

    apply_reloadable_config(current, new)

    # Reloadable field applied.
    assert current.log_level == "DEBUG"
    # Startup-only fields untouched — the swap must NOT change auth or port.
    assert current.auth_token == original_token
    assert current.port == original_port


# --------------------------------------------------------------------------- #
# reload_config — valid change applied
# --------------------------------------------------------------------------- #
def test_reload_applies_valid_change(tmp_path):
    path = _write(tmp_path / "cfg.yaml", _BASE_YAML)
    current = _load(path)
    assert current.log_level == "INFO"
    assert "api.anthropic.com" in current.proxy_allowed_domains

    _write(
        path,
        _BASE_YAML.replace('level: "INFO"', 'level: "WARNING"').replace(
            '- "api.anthropic.com"', '- "api.anthropic.com"\n    - "api.openai.com"'
        ),
    )
    ok, msg = reload_config(current, path)

    assert ok is True, msg
    assert current.log_level == "WARNING"
    assert "api.openai.com" in current.proxy_allowed_domains


# --------------------------------------------------------------------------- #
# reload_config — invalid change rejected, last-good kept
# --------------------------------------------------------------------------- #
def test_reload_rejects_invalid_and_keeps_last_good(tmp_path):
    path = _write(tmp_path / "cfg.yaml", _BASE_YAML)
    current = _load(path)
    good_level = current.log_level
    good_domains = list(current.proxy_allowed_domains)

    # Broken YAML — not a mapping. load_config() raises ValueError.
    _write(path, "- this is a list not a mapping\n- so load_config rejects it\n")
    ok, msg = reload_config(current, path)

    assert ok is False
    assert "error" in msg.lower() or "invalid" in msg.lower() or msg
    # Last-good config preserved, unchanged.
    assert current.log_level == good_level
    assert current.proxy_allowed_domains == good_domains


def test_reload_rejects_schema_violation_and_keeps_last_good(tmp_path):
    """A structurally-valid YAML that violates the pydantic schema is rejected."""
    path = _write(tmp_path / "cfg.yaml", _BASE_YAML)
    current = _load(path)
    good_domains = list(current.proxy_allowed_domains)

    # A structurally-valid YAML whose value violates the pydantic schema:
    # rate_limit_per_hour must be an int; a non-numeric string fails validation.
    _write(
        path,
        _BASE_YAML.replace("rate_limit_per_hour: 10", 'rate_limit_per_hour: "not-an-int"'),
    )
    ok, msg = reload_config(current, path)

    assert ok is False
    assert current.proxy_allowed_domains == good_domains


def test_reload_no_reloadable_field_changed(tmp_path):
    """File mtime changes but no reloadable field differs — reload still succeeds."""
    path = _write(tmp_path / "cfg.yaml", _BASE_YAML)
    current = _load(path)

    # Rewrite an identical (reloadable-equivalent) file: only a comment differs.
    _write(path, "# harmless comment change\n" + _BASE_YAML)
    ok, msg = reload_config(current, path)

    assert ok is True
    assert "0 field" in msg or "none" in msg


def test_reload_missing_file_keeps_last_good(tmp_path):
    path = _write(tmp_path / "cfg.yaml", _BASE_YAML)
    current = _load(path)
    good_level = current.log_level
    path.unlink()

    ok, msg = reload_config(current, path)

    assert ok is False
    assert current.log_level == good_level


# --------------------------------------------------------------------------- #
# config_watcher — mtime poll triggers reload only on change
# --------------------------------------------------------------------------- #
def test_watcher_reloads_on_mtime_change(tmp_path):
    path = _write(tmp_path / "cfg.yaml", _BASE_YAML)
    current = _load(path)
    assert current.log_level == "INFO"

    calls: list[bool] = []

    async def _drive():
        # Fake mtimes: baseline is read once before the loop; poll #1 sees the
        # same value (no change), poll #2 sees a new value (change -> reload).
        mtimes = [100.0, 100.0, 200.0, 200.0]
        idx = {"i": 0}

        def _fake_mtime(_p: Path) -> float:
            i = idx["i"]
            idx["i"] = min(i + 1, len(mtimes) - 1)
            return mtimes[i]

        stop = asyncio.Event()

        def _on_reload(ok: bool, _msg: str) -> None:
            calls.append(ok)

        # Pre-edit the file so the change-triggered reload picks up new content.
        _write(path, _BASE_YAML.replace('level: "INFO"', 'level: "ERROR"'))

        await config_watcher(
            current,
            path,
            interval_seconds=0,  # 0 => no real sleep; loop yields via sleep(0)
            stop_event=stop,
            mtime_fn=_fake_mtime,
            on_reload=_on_reload,
            max_iterations=2,
        )

    asyncio.run(_drive())

    # Exactly one reload happened (only when mtime changed 100 -> 200).
    assert calls == [True]
    assert current.log_level == "ERROR"


def test_default_mtime_reads_real_file_and_handles_missing(tmp_path):
    """_default_mtime returns the file mtime, and -1.0 when the file is absent."""
    path = _write(tmp_path / "cfg.yaml", _BASE_YAML)
    assert _default_mtime(path) == path.stat().st_mtime
    assert _default_mtime(tmp_path / "does-not-exist.yaml") == -1.0


def test_watcher_ignores_missing_file(tmp_path):
    """A missing file (mtime -1.0) must not trigger a reload (no reject storm)."""
    path = _write(tmp_path / "cfg.yaml", _BASE_YAML)
    current = _load(path)

    async def _drive():
        stop = asyncio.Event()
        await config_watcher(
            current,
            path,
            interval_seconds=0,
            stop_event=stop,
            mtime_fn=lambda _p: -1.0,  # always "missing"
            on_reload=lambda ok, msg: pytest.fail("must not reload a missing file"),
            max_iterations=2,
        )

    asyncio.run(_drive())


def test_resolve_config_path_explicit_and_env(tmp_path, monkeypatch):
    """resolve_config_path honors the explicit arg and AGENTSHROUD_CONFIG env."""
    explicit = tmp_path / "explicit.yaml"
    assert resolve_config_path(explicit) == explicit

    env_path = tmp_path / "env.yaml"
    monkeypatch.setenv("AGENTSHROUD_CONFIG", str(env_path))
    assert resolve_config_path() == env_path


def test_watcher_stops_on_event(tmp_path):
    path = _write(tmp_path / "cfg.yaml", _BASE_YAML)
    current = _load(path)

    async def _drive():
        stop = asyncio.Event()
        stop.set()  # already stopped => loop exits immediately

        await config_watcher(
            current,
            path,
            interval_seconds=0,
            stop_event=stop,
            mtime_fn=lambda _p: 1.0,
            on_reload=lambda ok, msg: pytest.fail("reload must not run when stopped"),
            max_iterations=5,
        )

    asyncio.run(_drive())
