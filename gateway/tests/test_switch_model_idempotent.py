# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""
Workstream C — switch_model.sh idempotency tests.

Validates that running `switch_model.sh local <model>` twice produces the same
docker/.env and exits 0 both times (idempotent). Tests operate on a temp copy
of the env file — no live docker or Ollama calls.

Environment requirements (all mocked here):
- ollama list: stubbed via subprocess patching
- docker compose: stubbed so no real containers are touched
"""

from __future__ import annotations

import os
import subprocess
import tempfile
from pathlib import Path

# Path to switch_model.sh in the repo root
_SCRIPT_DIR = Path(__file__).parent.parent.parent / "scripts"
SWITCH_MODEL_SH = _SCRIPT_DIR / "switch_model.sh"


def _read_env(env_file: Path) -> dict[str, str]:
    """Parse a docker/.env file into a dict."""
    result: dict[str, str] = {}
    for line in env_file.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            key, _, val = line.partition("=")
            result[key.strip()] = val.strip()
    return result


def _run_switch(
    target: str,
    model_ref: str | None,
    env_file: Path,
    *,
    expect_exit_0: bool = True,
) -> subprocess.CompletedProcess:
    """Run switch_model.sh with mocked external commands."""
    cmd = [str(SWITCH_MODEL_SH), target]
    if model_ref:
        cmd.append(model_ref)

    env = os.environ.copy()
    env["MODEL_ENV_FILE"] = str(env_file)
    # Suppress real docker compose calls inside the script
    env["SWITCH_MODEL_TEST_MODE"] = "1"

    result = subprocess.run(
        cmd,
        env=env,
        capture_output=True,
        text=True,
    )
    if expect_exit_0:
        assert result.returncode == 0, (
            f"switch_model.sh exited {result.returncode}\n"
            f"stdout: {result.stdout}\nstderr: {result.stderr}"
        )
    return result


# ---------------------------------------------------------------------------
# 1. Pure idempotency: running twice produces identical env
# ---------------------------------------------------------------------------


class TestSwitchModelIdempotent:
    """switch_model.sh local <m> twice must leave docker/.env unchanged on second run."""

    def _run_twice(
        self,
        target: str,
        model_ref: str | None = None,
    ) -> tuple[dict, dict]:
        """Returns (env_after_first_run, env_after_second_run)."""
        with tempfile.TemporaryDirectory() as td:
            env_file = Path(td) / ".env"
            env_file.write_text("")

            _run_switch(target, model_ref, env_file)
            after_first = _read_env(env_file)

            _run_switch(target, model_ref, env_file)
            after_second = _read_env(env_file)

        return after_first, after_second

    def test_local_default_idempotent(self):
        """local target: second run leaves env identical."""
        first, second = self._run_twice("local")
        assert first == second, f"Env changed on second run:\nfirst={first}\nsecond={second}"

    def test_local_with_explicit_model_idempotent(self):
        """local qwen3:14b: second run leaves env identical."""
        first, second = self._run_twice("local", "qwen3:14b")
        assert first == second

    def test_local_coder_idempotent(self):
        """local-coder target: second run leaves env identical."""
        first, second = self._run_twice("local-coder")
        assert first == second

    def test_local_anchor_idempotent(self):
        """local-anchor target: second run leaves env identical."""
        first, second = self._run_twice("local-anchor")
        assert first == second

    def test_cloud_anthropic_idempotent(self):
        """anthropic target: second run leaves env identical."""
        first, second = self._run_twice("anthropic")
        assert first == second


# ---------------------------------------------------------------------------
# 2. Key presence after switch
# ---------------------------------------------------------------------------


class TestSwitchModelEnvKeys:
    """Expected keys are present in docker/.env after a switch."""

    _REQUIRED_KEYS = [
        "AGENTSHROUD_MODEL_MODE",
        "AGENTSHROUD_LOCAL_MODEL_REF",
        "AGENTSHROUD_CLOUD_MODEL_REF",
        "AGENTSHROUD_LOCAL_MODEL",
        "OPENCLAW_MAIN_MODEL",
    ]

    def _run_and_read(self, target: str, model_ref: str | None = None) -> dict[str, str]:
        with tempfile.TemporaryDirectory() as td:
            env_file = Path(td) / ".env"
            env_file.write_text("")
            _run_switch(target, model_ref, env_file)
            return _read_env(env_file)

    def test_local_sets_required_keys(self):
        env = self._run_and_read("local")
        for key in self._REQUIRED_KEYS:
            assert key in env, f"Missing key after 'local' switch: {key}"

    def test_local_model_mode_is_local(self):
        env = self._run_and_read("local")
        assert env["AGENTSHROUD_MODEL_MODE"] == "local"

    def test_local_with_model_ref_sets_correct_model(self):
        env = self._run_and_read("local", "qwen3:14b")
        assert env["AGENTSHROUD_LOCAL_MODEL"] == "qwen3:14b"
        assert "qwen3" in env["AGENTSHROUD_LOCAL_MODEL_REF"]

    def test_anthropic_sets_cloud_mode(self):
        env = self._run_and_read("anthropic")
        assert env["AGENTSHROUD_MODEL_MODE"] == "cloud"

    def test_local_coder_sets_local_multi_mode(self):
        env = self._run_and_read("local-coder")
        assert env["AGENTSHROUD_MODEL_MODE"] == "local-multi"

    def test_local_multi_writes_anchor_coding_reasoning(self):
        env = self._run_and_read("local-multi")
        assert "AGENTSHROUD_ANCHOR_MODEL" in env
        assert "AGENTSHROUD_CODING_MODEL" in env
        assert "AGENTSHROUD_REASONING_MODEL" in env


# ---------------------------------------------------------------------------
# 3. --verify flag: script reads back env and validates both bots
# ---------------------------------------------------------------------------


class TestSwitchModelVerifyFlag:
    """--verify flag causes switch_model.sh to check both bots are healthy."""

    def test_verify_flag_accepted_without_error(self):
        """switch_model.sh local --verify exits 0 (mocked health checks)."""
        with tempfile.TemporaryDirectory() as td:
            env_file = Path(td) / ".env"
            env_file.write_text("")

            cmd = [str(SWITCH_MODEL_SH), "local", "--verify"]
            env = os.environ.copy()
            env["MODEL_ENV_FILE"] = str(env_file)
            env["SWITCH_MODEL_TEST_MODE"] = "1"
            # Mock health endpoint for both bots
            env["SWITCH_MODEL_HEALTH_MOCK"] = "1"

            result = subprocess.run(cmd, env=env, capture_output=True, text=True)
            # Must exit 0 in test mode (health checks mocked/skipped)
            assert result.returncode == 0, (
                f"--verify flag failed: exit={result.returncode}\n"
                f"stdout={result.stdout}\nstderr={result.stderr}"
            )

    def test_verify_flag_with_model_ref(self):
        """switch_model.sh local qwen3:14b --verify exits 0."""
        with tempfile.TemporaryDirectory() as td:
            env_file = Path(td) / ".env"
            env_file.write_text("")

            cmd = [str(SWITCH_MODEL_SH), "local", "qwen3:14b", "--verify"]
            env = os.environ.copy()
            env["MODEL_ENV_FILE"] = str(env_file)
            env["SWITCH_MODEL_TEST_MODE"] = "1"
            env["SWITCH_MODEL_HEALTH_MOCK"] = "1"

            result = subprocess.run(cmd, env=env, capture_output=True, text=True)
            assert result.returncode == 0, (
                f"--verify with model ref failed: {result.stderr}"
            )


# ---------------------------------------------------------------------------
# 4. Both-bots mode: HERMES_MAIN_MODEL env var is written alongside OPENCLAW
# ---------------------------------------------------------------------------


class TestSwitchModelBothBots:
    """switch_model.sh must write model config for both OpenClaw and Hermes."""

    def _run_and_read(self, target: str, model_ref: str | None = None) -> dict[str, str]:
        with tempfile.TemporaryDirectory() as td:
            env_file = Path(td) / ".env"
            env_file.write_text("")
            _run_switch(target, model_ref, env_file)
            return _read_env(env_file)

    def test_local_switch_writes_hermes_main_model(self):
        """After local switch, HERMES_MAIN_MODEL is written to .env."""
        env = self._run_and_read("local")
        assert "HERMES_MAIN_MODEL" in env, (
            "HERMES_MAIN_MODEL not written to .env after local switch. "
            "Both bots must be updated atomically."
        )

    def test_local_switch_hermes_and_openclaw_models_match(self):
        """HERMES_MAIN_MODEL and OPENCLAW_MAIN_MODEL must reference the same model."""
        env = self._run_and_read("local")
        openclaw_model = env.get("OPENCLAW_MAIN_MODEL", "")
        hermes_model = env.get("HERMES_MAIN_MODEL", "")
        assert openclaw_model == hermes_model, (
            f"OPENCLAW_MAIN_MODEL={openclaw_model!r} != "
            f"HERMES_MAIN_MODEL={hermes_model!r}; bots must switch atomically"
        )

    def test_cloud_switch_writes_hermes_main_model(self):
        """After cloud switch, HERMES_MAIN_MODEL is written for Hermes too."""
        env = self._run_and_read("anthropic")
        assert "HERMES_MAIN_MODEL" in env

    def test_local_coder_switch_both_bots(self):
        """local-coder switch writes matching HERMES_MAIN_MODEL."""
        env = self._run_and_read("local-coder")
        assert "HERMES_MAIN_MODEL" in env
        assert env["OPENCLAW_MAIN_MODEL"] == env["HERMES_MAIN_MODEL"]
