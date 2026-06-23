# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Tests for the Voice Gateway FastAPI app (server.py, stt.py, tts.py).

All external I/O is mocked:
  - faster_whisper / numpy (STT model) — mocked via monkeypatch
  - Piper subprocess (TTS) — mocked via monkeypatch
  - httpx (gateway /v1/chat/completions) — mocked via monkeypatch

Tests cover:
  - GET /health returns 200 {"status":"ok"}
  - WS /voice: full utterance → STT → /v1/chat/completions → TTS → PCM back, state sequence
  - WS /voice: empty transcript → idle (no TTS, no LLM call)
  - _call_llm: happy path returns content string from OpenAI-shape response
  - _call_llm: malformed response raises RuntimeError
  - _call_llm: sends correct model, max_tokens, full message history
  - _call_llm: multi-turn history carried in request body
  - X-AgentShroud-User-Id header propagates owner UID
  - stt.transcribe: S16LE bytes → string (model mocked)
  - tts.synthesize: string → bytes (piper mocked)
  - tts.synthesize: piper not found raises RuntimeError
  - tts.synthesize: piper non-zero exit raises RuntimeError
  - WS token authentication (correct / wrong / missing / unconfigured)
"""

from __future__ import annotations

import json
import struct
import subprocess
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from voice_gateway.server import app, _call_llm


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
    """synthesize() invokes piper; when rates match no resampling occurs."""
    import voice_gateway.tts as tts_mod

    pcm_bytes = b"\x00\x01" * 100

    mock_result = MagicMock()
    mock_result.returncode = 0
    mock_result.stdout = pcm_bytes
    mock_result.stderr = b""

    monkeypatch.setattr(subprocess, "run", lambda *a, **kw: mock_result)
    # Pin rates equal so no resampling — tests the pass-through path.
    monkeypatch.setattr(tts_mod, "TARGET_SAMPLE_RATE", tts_mod.OUTPUT_SAMPLE_RATE)

    result = tts_mod.synthesize("hello world")
    assert result == pcm_bytes


def test_tts_resamples_22050_to_16000(monkeypatch):
    """When OUTPUT_SAMPLE_RATE (22050) != TARGET_SAMPLE_RATE (16000), the output
    is resampled.  For N input samples at 22050 Hz the output should have
    approximately N * 16000/22050 samples.  The exact ratio is checked within 1%.
    """
    import math
    import struct as _struct
    import voice_gateway.tts as tts_mod

    # Build 0.5 s of silence at 22050 Hz (the native Piper rate)
    n_src = 22050 // 2  # 0.5 s
    raw_pcm = _struct.pack(f"<{n_src}h", *([0] * n_src))

    mock_result = MagicMock()
    mock_result.returncode = 0
    mock_result.stdout = raw_pcm
    mock_result.stderr = b""

    monkeypatch.setattr(subprocess, "run", lambda *a, **kw: mock_result)
    # Ensure resampling is active (default — but be explicit)
    monkeypatch.setattr(tts_mod, "OUTPUT_SAMPLE_RATE", 22050)
    monkeypatch.setattr(tts_mod, "TARGET_SAMPLE_RATE", 16000)

    result = tts_mod.synthesize("hello")

    n_dst = len(result) // 2  # 16-bit samples
    expected = n_src * 16000 / 22050
    ratio_error = abs(n_dst - expected) / expected
    assert ratio_error < 0.01, (
        f"Resampled length {n_dst} samples deviates {ratio_error:.2%} from expected "
        f"{expected:.1f} (src={n_src}, 22050→16000 Hz)"
    )


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


# ── _call_llm unit tests ──────────────────────────────────────────────────────


def _openai_resp(content: str, status: int = 200):
    """Build a mock httpx response with an OpenAI-shape body."""
    mock = MagicMock()
    mock.status_code = status
    mock.json = MagicMock(
        return_value={"choices": [{"message": {"content": content}}]}
    )
    mock.raise_for_status = MagicMock()
    return mock


@pytest.mark.asyncio
async def test_call_llm_returns_content():
    """_call_llm posts to /v1/chat/completions and returns stripped content."""
    history = [
        {"role": "system", "content": "You are a voice assistant."},
        {"role": "user", "content": "what time is it"},
    ]
    with patch("httpx.AsyncClient.post", new=AsyncMock(return_value=_openai_resp("It is noon."))):
        result = await _call_llm(history)
    assert result == "It is noon."


@pytest.mark.asyncio
async def test_call_llm_strips_whitespace():
    """Leading/trailing whitespace in the model reply is stripped."""
    history = [{"role": "user", "content": "hello"}]
    with patch("httpx.AsyncClient.post", new=AsyncMock(return_value=_openai_resp("  Hi there.  \n"))):
        result = await _call_llm(history)
    assert result == "Hi there."


@pytest.mark.asyncio
async def test_call_llm_malformed_response_raises():
    """A response without choices[0].message.content raises RuntimeError."""
    mock = MagicMock()
    mock.status_code = 200
    mock.json = MagicMock(return_value={"unexpected": "shape"})
    mock.raise_for_status = MagicMock()

    with patch("httpx.AsyncClient.post", new=AsyncMock(return_value=mock)):
        with pytest.raises(RuntimeError, match="Unexpected LLM response shape"):
            await _call_llm([{"role": "user", "content": "hi"}])


@pytest.mark.asyncio
async def test_call_llm_sends_correct_model_and_max_tokens(monkeypatch):
    """Request body must carry the configured model and max_tokens=150."""
    import voice_gateway.server as srv

    monkeypatch.setattr(srv, "_VOICE_MODEL", "claude-haiku-4-5-20251001")

    captured = {}

    async def _capture(url, json=None, **kw):
        captured.update(json or {})
        return _openai_resp("ok")

    with patch("httpx.AsyncClient.post", new=AsyncMock(side_effect=_capture)):
        await _call_llm([{"role": "user", "content": "test"}])

    assert captured["model"] == "claude-haiku-4-5-20251001"
    assert captured["max_tokens"] == 150


@pytest.mark.asyncio
async def test_call_llm_sends_full_history(monkeypatch):
    """The full messages history (system + prior turns) is sent in the request body."""
    history = [
        {"role": "system", "content": "You are a voice assistant."},
        {"role": "user", "content": "what time is it"},
        {"role": "assistant", "content": "It is noon."},
        {"role": "user", "content": "what day is it"},
    ]
    captured = {}

    async def _capture(url, json=None, **kw):
        captured.update(json or {})
        return _openai_resp("It is Monday.")

    with patch("httpx.AsyncClient.post", new=AsyncMock(side_effect=_capture)):
        result = await _call_llm(history)

    assert result == "It is Monday."
    assert captured["messages"] == history, "Full conversation history must be forwarded"


# ── Owner UID header propagation ──────────────────────────────────────────────


def test_owner_user_id_propagated_as_header(monkeypatch):
    """GATEWAY_OWNER_USER_ID is sent as X-AgentShroud-User-Id header (not a body field)."""
    import importlib
    import asyncio
    import voice_gateway.server as srv

    monkeypatch.setenv("GATEWAY_OWNER_USER_ID", "8096968754")
    importlib.reload(srv)

    assert srv._OWNER_USER_ID == "8096968754"

    captured_headers = {}

    async def _capture(url, json=None, headers=None, **kw):
        captured_headers.update(headers or {})
        return _openai_resp("Hello")

    with patch("httpx.AsyncClient.post", new=AsyncMock(side_effect=_capture)):
        asyncio.run(srv._call_llm([{"role": "user", "content": "test"}]))

    assert captured_headers.get("X-AgentShroud-User-Id") == "8096968754", (
        f"Expected X-AgentShroud-User-Id='8096968754', got headers={captured_headers}"
    )


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


# ── WebSocket /voice integration tests ───────────────────────────────────────


def _pcm_bytes(num_samples: int = 160) -> bytes:
    """Minimal S16LE silence."""
    return struct.pack(f"<{num_samples}h", *([0] * num_samples))


def test_ws_full_utterance_state_sequence(monkeypatch):
    """LISTEN → binary PCM → END → STT → /v1/chat/completions → TTS → PCM + END → idle."""
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod

    pcm_reply = _pcm_bytes(100)

    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "what time is it")
    monkeypatch.setattr(tts_mod, "synthesize", lambda t: pcm_reply)

    with patch(
        "httpx.AsyncClient.post",
        new=AsyncMock(return_value=_openai_resp("It is noon.")),
    ):
        with TestClient(app) as client:
            with client.websocket_connect("/voice") as ws:
                state_msg = ws.receive_text()
                assert json.loads(state_msg)["state"] == "idle"

                ws.send_text("LISTEN")
                state_msg = ws.receive_text()
                assert json.loads(state_msg)["state"] == "listening"

                ws.send_bytes(_pcm_bytes())
                ws.send_text("END")

                states_received = []
                binary_received = b""
                end_received = False

                for _ in range(20):
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


# ── Connect-state test ────────────────────────────────────────────────────────


def test_ws_connect_sends_idle_first():
    """The very first frame after WS accept must be idle, not listening."""
    with TestClient(app) as client:
        with client.websocket_connect("/voice") as ws:
            first = ws.receive_text()
            assert json.loads(first) == {"state": "idle"}, (
                f"Expected first frame {{state: idle}}, got {first!r}"
            )


# ── Empty transcript ──────────────────────────────────────────────────────────


def test_ws_empty_transcript_goes_idle(monkeypatch):
    """Empty STT result: no LLM call, state goes directly to idle."""
    import voice_gateway.stt as stt_mod

    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "   ")

    with patch("httpx.AsyncClient.post", new=AsyncMock(side_effect=Exception("should not call"))):
        with TestClient(app) as client:
            with client.websocket_connect("/voice") as ws:
                ws.receive_text()  # initial idle

                ws.send_text("LISTEN")
                ws.receive_text()  # listening

                ws.send_bytes(_pcm_bytes())
                ws.send_text("END")

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


# ── WS token authentication tests ────────────────────────────────────────────


def test_ws_accepts_correct_token(monkeypatch):
    """Connection with correct ?token= query param is accepted and gets idle state."""
    import voice_gateway.server as srv

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "correct-token")

    with TestClient(app) as client:
        with client.websocket_connect("/voice?token=correct-token") as ws:
            first = ws.receive_text()
            assert json.loads(first) == {"state": "idle"}


def test_ws_rejects_wrong_token(monkeypatch):
    """Connection with wrong ?token= is closed (server returns no state frame)."""
    import voice_gateway.server as srv

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "correct-token")

    with TestClient(app) as client:
        with pytest.raises(Exception):
            with client.websocket_connect("/voice?token=wrong-token") as ws:
                ws.receive_text()


def test_ws_rejects_missing_token(monkeypatch):
    """Connection with no token is rejected when auth is configured."""
    import voice_gateway.server as srv

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "correct-token")

    with TestClient(app) as client:
        with pytest.raises(Exception):
            with client.websocket_connect("/voice") as ws:
                ws.receive_text()


def test_ws_accepts_when_auth_not_configured(monkeypatch):
    """When _VG_AUTH_TOKEN is empty, any connection is accepted (dev / backward compat)."""
    import voice_gateway.server as srv

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")

    with TestClient(app) as client:
        with client.websocket_connect("/voice") as ws:
            first = ws.receive_text()
            assert json.loads(first) == {"state": "idle"}
