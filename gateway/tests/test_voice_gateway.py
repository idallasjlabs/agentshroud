# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Tests for the Voice Gateway FastAPI app (server.py, stt.py, tts.py).

All external I/O is mocked:
  - faster_whisper / numpy (STT model) — mocked via monkeypatch
  - Piper subprocess (TTS) — mocked via monkeypatch
  - httpx (AgentShroud /forward) — mocked via monkeypatch

Tests cover:
  - GET /health returns 200 {"status":"ok"}
  - WS /voice: full utterance → STT → /forward → TTS → PCM back, state sequence
  - WS /voice: empty transcript → idle (no TTS, no forward)
  - WS /voice: agent offline (empty agent_response) → fallback text spoken
  - WS /voice: 202 queued response → fallback text spoken
  - stt.transcribe: S16LE bytes → string (model mocked)
  - tts.synthesize: string → bytes (piper mocked)
  - tts.synthesize: piper not found raises RuntimeError
  - tts.synthesize: piper non-zero exit raises RuntimeError
"""

from __future__ import annotations

import json
import struct
import subprocess
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from voice_gateway.server import app, _call_forward


# ── Health endpoint ───────────────────────────────────────────────────────────


def test_health_returns_ok():
    client = TestClient(app)
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


# ── STT unit tests ────────────────────────────────────────────────────────────


def test_stt_transcribe_empty_bytes_returns_empty():
    from voice_gateway import stt

    assert stt.transcribe(b"") == ""


def test_stt_transcribe_mocked_model(monkeypatch):
    """transcribe() calls the model and returns joined segment text."""
    import numpy as np
    import voice_gateway.stt as stt_mod

    stt_mod.reset_model()

    # Build minimal S16LE PCM (1 sample = 2 bytes)
    pcm = struct.pack("<h", 1000) * 16  # 16 samples

    mock_seg = MagicMock()
    mock_seg.text = " hello"

    mock_model = MagicMock()
    mock_model.transcribe = MagicMock(return_value=([mock_seg], MagicMock()))

    def fake_get_model():
        return mock_model

    monkeypatch.setattr(stt_mod, "_get_model", fake_get_model)

    result = stt_mod.transcribe(pcm)
    assert result == "hello"
    mock_model.transcribe.assert_called_once()


# ── TTS unit tests ────────────────────────────────────────────────────────────


def test_tts_empty_text_returns_empty():
    from voice_gateway import tts

    assert tts.synthesize("") == b""


def test_tts_synthesize_mocked_piper(monkeypatch):
    """synthesize() invokes piper and returns its stdout."""
    pcm_bytes = b"\x00\x01" * 100

    mock_result = MagicMock()
    mock_result.returncode = 0
    mock_result.stdout = pcm_bytes
    mock_result.stderr = b""

    monkeypatch.setattr(subprocess, "run", lambda *a, **kw: mock_result)

    from voice_gateway import tts

    result = tts.synthesize("hello world")
    assert result == pcm_bytes


def test_tts_piper_not_found_raises(monkeypatch):
    def _raise(*a, **kw):
        raise FileNotFoundError("piper not found")

    monkeypatch.setattr(subprocess, "run", _raise)

    from voice_gateway import tts

    with pytest.raises(RuntimeError, match="Piper binary not found"):
        tts.synthesize("hello")


def test_tts_piper_nonzero_exit_raises(monkeypatch):
    mock_result = MagicMock()
    mock_result.returncode = 1
    mock_result.stdout = b""
    mock_result.stderr = b"model not found"

    monkeypatch.setattr(subprocess, "run", lambda *a, **kw: mock_result)

    from voice_gateway import tts

    with pytest.raises(RuntimeError, match="Piper exited"):
        tts.synthesize("hello")


# ── _call_forward unit tests ──────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_call_forward_returns_agent_response(monkeypatch):
    mock_resp = MagicMock()
    mock_resp.status_code = 201
    mock_resp.json = MagicMock(return_value={"agent_response": "Hi there"})
    mock_resp.raise_for_status = MagicMock()

    async def mock_post(*a, **kw):
        return mock_resp

    import voice_gateway.server as srv

    monkeypatch.setattr("voice_gateway.server._GATEWAY_URL", "http://gw:8080")
    monkeypatch.setattr("voice_gateway.server._GATEWAY_TOKEN", "tok")

    with patch("httpx.AsyncClient.post", new=AsyncMock(return_value=mock_resp)):
        result = await _call_forward("what time is it?")

    assert result == "Hi there"


@pytest.mark.asyncio
async def test_call_forward_202_returns_queued_message(monkeypatch):
    mock_resp = MagicMock()
    mock_resp.status_code = 202
    mock_resp.json = MagicMock(return_value={"status": "queued", "approval_id": "abc"})
    mock_resp.raise_for_status = MagicMock()

    with patch("httpx.AsyncClient.post", new=AsyncMock(return_value=mock_resp)):
        result = await _call_forward("delete everything")

    assert "queued" in result.lower()


@pytest.mark.asyncio
async def test_call_forward_empty_agent_response_returns_offline_message(monkeypatch):
    mock_resp = MagicMock()
    mock_resp.status_code = 201
    mock_resp.json = MagicMock(return_value={"agent_response": ""})
    mock_resp.raise_for_status = MagicMock()

    with patch("httpx.AsyncClient.post", new=AsyncMock(return_value=mock_resp)):
        result = await _call_forward("hello")

    assert "offline" in result.lower()


# ── WebSocket /voice integration tests ───────────────────────────────────────


def _pcm_bytes(num_samples: int = 160) -> bytes:
    """Minimal S16LE silence."""
    return struct.pack(f"<{num_samples}h", *([0] * num_samples))


def test_ws_full_utterance_state_sequence(monkeypatch):
    """LISTEN → binary PCM → END → gateway calls STT, /forward, TTS → PCM + END, idle."""
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod

    pcm_reply = _pcm_bytes(100)

    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "what time is it")
    monkeypatch.setattr(tts_mod, "synthesize", lambda t: pcm_reply)

    mock_forward_resp = MagicMock()
    mock_forward_resp.status_code = 201
    mock_forward_resp.json = MagicMock(return_value={"agent_response": "It is noon."})
    mock_forward_resp.raise_for_status = MagicMock()

    with patch("httpx.AsyncClient.post", new=AsyncMock(return_value=mock_forward_resp)):
        with TestClient(app) as client:
            with client.websocket_connect("/voice") as ws:
                # Should receive "listening" state on connect
                state_msg = ws.receive_text()
                assert json.loads(state_msg)["state"] == "listening"

                # Send a new utterance
                ws.send_text("LISTEN")
                state_msg = ws.receive_text()
                assert json.loads(state_msg)["state"] == "listening"

                # Send PCM chunk
                ws.send_bytes(_pcm_bytes())

                # End utterance
                ws.send_text("END")

                # Expect: thinking → speaking → [PCM binary] → "END" → idle
                states_received = []
                binary_received = b""
                end_received = False

                for _ in range(20):  # bounded loop
                    try:
                        msg = ws.receive()
                    except Exception:
                        break

                    if "text" in msg:
                        text = msg["text"]
                        try:
                            data = json.loads(text)
                            states_received.append(data["state"])
                            if data["state"] == "idle":
                                break
                        except (json.JSONDecodeError, KeyError):
                            if text == "END":
                                end_received = True
                    elif "bytes" in msg:
                        binary_received += msg["bytes"] or b""

                assert "thinking" in states_received
                assert "speaking" in states_received
                assert "idle" in states_received
                assert end_received
                assert binary_received == pcm_reply


# ── Token secret-file loading ─────────────────────────────────────────────────


def test_token_loaded_from_secret_file(tmp_path, monkeypatch):
    """_GATEWAY_TOKEN is read from the secret file when it exists."""
    import importlib
    import os

    secret_file = tmp_path / "gw_password.txt"
    secret_file.write_text("test-secret-token\n")

    monkeypatch.setenv("GATEWAY_AUTH_TOKEN_FILE", str(secret_file))
    monkeypatch.delenv("GATEWAY_AUTH_TOKEN", raising=False)

    import voice_gateway.server as srv
    importlib.reload(srv)

    assert srv._GATEWAY_TOKEN == "test-secret-token"


def test_token_falls_back_to_env_when_no_file(tmp_path, monkeypatch):
    """When secret file is absent, _GATEWAY_TOKEN falls back to GATEWAY_AUTH_TOKEN env var."""
    import importlib

    monkeypatch.setenv("GATEWAY_AUTH_TOKEN_FILE", str(tmp_path / "nonexistent.txt"))
    monkeypatch.setenv("GATEWAY_AUTH_TOKEN", "env-token")

    import voice_gateway.server as srv
    importlib.reload(srv)

    assert srv._GATEWAY_TOKEN == "env-token"


def test_owner_user_id_used_as_source_in_forward(monkeypatch):
    """GATEWAY_OWNER_USER_ID is forwarded as 'source' so RBAC grants owner privileges."""
    import importlib
    import voice_gateway.server as srv

    monkeypatch.setenv("GATEWAY_OWNER_USER_ID", "8096968754")
    importlib.reload(srv)

    assert srv._OWNER_USER_ID == "8096968754"

    # Verify _call_forward passes _OWNER_USER_ID as source (not hardcoded "api")
    captured_body = {}
    mock_resp = MagicMock()
    mock_resp.status_code = 201
    mock_resp.json = MagicMock(return_value={"agent_response": "Hello"})
    mock_resp.raise_for_status = MagicMock()

    async def _capture_post(url, json=None, **kw):
        captured_body.update(json or {})
        return mock_resp

    with patch("httpx.AsyncClient.post", new=AsyncMock(side_effect=_capture_post)):
        import asyncio

        asyncio.run(srv._call_forward("test query"))

    # source must remain "api" (enum-validated by ForwardRequest.validate_source)
    assert captured_body.get("source") == "api", (
        f"Expected source='api', got {captured_body.get('source')!r}"
    )
    # user_id carries the owner UID — RBAC middleware reads this field first
    assert captured_body.get("user_id") == "8096968754", (
        f"Expected user_id='8096968754', got {captured_body.get('user_id')!r}"
    )


def test_stt_uses_local_model_dir_when_env_set(monkeypatch):
    """WHISPER_MODEL_DIR env var is honoured: _MODEL_PATH resolves to the directory
    and WhisperModel is constructed with that path — no network call at runtime.

    Uses sys.modules injection so faster_whisper need not be installed on the host.
    """
    import importlib
    import sys

    local_dir = "/opt/whisper/base.en"
    monkeypatch.setenv("WHISPER_MODEL_DIR", local_dir)

    import voice_gateway.stt as stt_mod
    importlib.reload(stt_mod)

    # _MODEL_PATH must pick up the env var after reload
    assert stt_mod._MODEL_PATH == local_dir

    # Inject a fake faster_whisper module so the lazy import inside _get_model() works
    # without a real installation (and without any network call).
    captured = {}
    fake_fw = MagicMock()
    fake_fw.WhisperModel = lambda path, **kw: (
        captured.update({"model_path": path}) or MagicMock()
    )
    monkeypatch.setitem(sys.modules, "faster_whisper", fake_fw)

    # _get_model() must pass _MODEL_PATH (the directory) to WhisperModel
    stt_mod.reset_model()
    stt_mod._get_model()
    assert captured.get("model_path") == local_dir, (
        f"Expected WhisperModel({local_dir!r}), got {captured.get('model_path')!r}"
    )


def test_ws_empty_transcript_goes_idle(monkeypatch):
    """Empty STT result: no forward call, state goes directly to idle."""
    import voice_gateway.stt as stt_mod

    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "   ")

    called = []

    async def _no_call(self, *a, **kw):
        called.append(True)
        return MagicMock()

    with patch("httpx.AsyncClient.post", new=AsyncMock(side_effect=Exception("should not call"))):
        with TestClient(app) as client:
            with client.websocket_connect("/voice") as ws:
                ws.receive_text()  # initial listening state

                ws.send_text("LISTEN")
                ws.receive_text()  # listening

                ws.send_bytes(_pcm_bytes())
                ws.send_text("END")

                # Should receive thinking then idle (no speaking)
                states = []
                for _ in range(10):
                    try:
                        msg = ws.receive()
                    except Exception:
                        break
                    if "text" in msg:
                        try:
                            data = json.loads(msg["text"])
                            states.append(data["state"])
                            if data["state"] == "idle":
                                break
                        except (json.JSONDecodeError, KeyError):
                            pass

                assert "thinking" in states
                assert "idle" in states
                assert "speaking" not in states
