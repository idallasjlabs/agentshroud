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
from voice_gateway.server import _call_llm, app

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


# ── normalize_for_speech unit tests ──────────────────────────────────────────
#
# These tests cover the speech normalisation layer added in SCRUM-46.
# They exercise normalize_for_speech directly (pure function, no I/O) and
# then verify that synthesize() feeds the normalised text to Piper.


class TestNormalizeForSpeech:
    """Unit tests for voice_gateway.tts.normalize_for_speech."""

    @staticmethod
    def _n(text: str) -> str:
        from voice_gateway.tts import normalize_for_speech
        return normalize_for_speech(text)

    # ── markdown stripping ────────────────────────────────────────────────

    def test_bold_double_star_stripped(self):
        assert self._n("**bold** text") == "bold text"

    def test_bold_double_underscore_stripped(self):
        assert self._n("__bold__ text") == "bold text"

    def test_italic_star_stripped(self):
        assert self._n("*italic* text") == "italic text"

    def test_inline_code_backtick_stripped(self):
        assert self._n("`some_var` is set") == "some_var is set"

    def test_code_fence_delimiter_stripped(self):
        result = self._n("```python\nprint('hi')\n```\ndone")
        assert "```" not in result
        assert "print" in result
        assert "done" in result

    def test_heading_stripped(self):
        assert self._n("## Section Title") == "Section Title"
        assert self._n("# H1") == "H1"

    def test_bullet_list_marker_stripped(self):
        result = self._n("- item one\n- item two")
        assert "- " not in result
        assert "item one" in result
        assert "item two" in result

    def test_numbered_list_marker_stripped(self):
        result = self._n("1. First\n2. Second")
        assert "1." not in result
        assert "First" in result

    def test_blockquote_stripped(self):
        assert self._n("> quoted text") == "quoted text"

    def test_horizontal_rule_stripped(self):
        result = self._n("before\n---\nafter")
        assert "---" not in result
        assert "before" in result
        assert "after" in result

    def test_markdown_link_reduced_to_text(self):
        assert self._n("[click here](https://example.com)") == "click here"

    def test_image_link_reduced_to_alt(self):
        assert self._n("![diagram](https://example.com/img.png)") == "diagram"

    def test_plain_prose_unchanged(self):
        prose = "The gateway runs on the server and listens for connections."
        assert self._n(prose) == prose

    # ── redaction token → category-aware phrase ───────────────────────────

    def test_credential_redacted_spoken(self):
        result = self._n("the key is [CREDENTIAL_REDACTED] now")
        assert "[CREDENTIAL_REDACTED]" not in result
        assert "a credential" in result

    def test_credential_var_spoken(self):
        result = self._n("set [CREDENTIAL_VAR] to enable")
        assert "a credential" in result

    def test_secret_path_spoken(self):
        result = self._n("at [SECRET_PATH] you will find it")
        assert "a credential" in result

    def test_port_spoken(self):
        result = self._n("gateway runs on port [PORT]")
        assert "[PORT]" not in result
        assert "a port" in result

    def test_port_inline_colon(self):
        """Reproduces the exact log pattern: http://gateway:[PORT]"""
        result = self._n("http://gateway:[PORT]")
        assert "[PORT]" not in result
        assert "a port" in result

    def test_internal_host_spoken(self):
        result = self._n("connects to [INTERNAL_HOST]")
        assert "an internal host" in result

    def test_internal_url_spoken(self):
        result = self._n("forwarded to [INTERNAL_URL]")
        assert "an internal address" in result

    def test_user_id_spoken(self):
        result = self._n("user [USER_ID] sent this")
        assert "a user" in result

    def test_user_id_redacted_spoken(self):
        result = self._n("[USER_ID_REDACTED] was the sender")
        assert "a user" in result

    def test_tool_spoken(self):
        result = self._n("called [TOOL] with args")
        assert "a tool" in result

    def test_security_module_spoken(self):
        result = self._n("[SECURITY_MODULE] blocked the request")
        assert "a security module" in result

    def test_model_info_spoken(self):
        result = self._n("running model [MODEL_INFO]")
        assert "a model name" in result

    # ── PII angle-bracket tokens ──────────────────────────────────────────

    def test_email_address_spoken(self):
        result = self._n("send to <EMAIL_ADDRESS> for details")
        assert "<EMAIL_ADDRESS>" not in result
        assert "an email address" in result

    def test_phone_number_spoken(self):
        result = self._n("call <PHONE_NUMBER> now")
        assert "a phone number" in result

    def test_us_ssn_spoken(self):
        result = self._n("SSN: <US_SSN>")
        assert "a social security number" in result

    def test_person_spoken(self):
        result = self._n("<PERSON> submitted the form")
        assert "a person's name" in result

    # ── variable-content redaction patterns ───────────────────────────────

    def test_lock_emoji_redacted_spoken(self):
        """🔒 [REDACTED: Credentials cannot be displayed via Telegram]"""
        result = self._n("🔒 [REDACTED: Credentials cannot be displayed via Telegram]")
        assert "[REDACTED:" not in result
        assert "a credential" in result

    def test_angle_redacted_spoken(self):
        """<REDACTED:secret>"""
        result = self._n("value is <REDACTED:secret>")
        assert "<REDACTED:" not in result
        assert "a credential" in result

    # ── fallback for unknown tokens ───────────────────────────────────────

    def test_unknown_bracket_token_fallback(self):
        result = self._n("[FOO_REDACTED] happened")
        assert "[FOO_REDACTED]" not in result
        assert "redacted" in result

    def test_unknown_angle_token_fallback(self):
        result = self._n("value: <CUSTOM_PII_TYPE>")
        assert "<CUSTOM_PII_TYPE>" not in result
        assert "redacted" in result

    def test_lowercase_bracket_not_matched(self):
        """[1], [possible], [note] — not uppercase-only, must not be touched."""
        assert self._n("see [1] for details") == "see [1] for details"

    # ── safety: secret value never leaks ─────────────────────────────────

    def test_raw_secret_value_not_present_after_normalise(self):
        """If a secret somehow reaches normalise (shouldn't — pipeline redacted it),
        the token replacement means the secret string itself is not in the output
        because the token replaced it *before* we see it.  This test checks the
        guarantee that token replacement does not re-introduce secret text.
        """
        # Simulate the pipeline having already replaced the actual secret with a token.
        redacted_text = "key=[CREDENTIAL_REDACTED] in config"
        result = self._n(redacted_text)
        # The original token (not a real secret) is gone; "a credential" appears instead.
        assert "[CREDENTIAL_REDACTED]" not in result
        assert "a credential" in result
        # The word "key" (not secret) is still there — only the placeholder was removed.
        assert "key" in result

    # ── compound real-world example ───────────────────────────────────────

    def test_agent_reply_from_log(self):
        """Reproduces the 2026-06-27 12:38 agent reply that triggered SCRUM-46."""
        sample = (
            "**Your message arrives** at the Hermes API server.\n\n"
            "**The system prompt is assembled** — the server injects the current "
            "date/time as a static string into my system instructions before sending "
            "the request to Claude.\n\n"
            "**My context loads** — I receive the full system prompt (~4000 tokens), "
            "which includes:\n"
            "   - My identity as Hermes/Claude Code\n"
            "   - AgentShroud security details\n"
            "   - Available tools and their schemas (~50+ tool definitions)\n\n"
            "Network round-trip — Request goes through the AgentShroud gateway at "
            "http://gateway:[PORT], which applies audit logging.\n\n"
            "**Token accounting** — Even though you asked 10 words, I'm processing "
            "4000+ [CREDENTIAL_REDACTED] prompt before calling Claude."
        )
        result = self._n(sample)
        # No markdown markers
        assert "**" not in result
        assert "```" not in result
        # No redaction tokens
        assert "[PORT]" not in result
        assert "[CREDENTIAL_REDACTED]" not in result
        # Category phrases present
        assert "a port" in result
        assert "a credential" in result
        # Real content preserved
        assert "Hermes API server" in result
        assert "AgentShroud" in result
        assert "audit logging" in result


def test_tts_synthesize_passes_normalised_text_to_piper(monkeypatch):
    """synthesize() feeds the normalised (no-markdown, no-token) text to Piper.

    Verifies that the text arriving at subprocess.run contains no markdown
    bold markers or redaction placeholder tokens.
    """
    import voice_gateway.tts as tts_mod

    captured_input: list[bytes] = []

    def _fake_run(*args, **kwargs):
        captured_input.append(kwargs.get("input", b""))
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = b"\x00\x01" * 50
        mock_result.stderr = b""
        return mock_result

    monkeypatch.setattr(subprocess, "run", _fake_run)
    monkeypatch.setattr(tts_mod, "TARGET_SAMPLE_RATE", tts_mod.OUTPUT_SAMPLE_RATE)

    raw_text = "**bold claim** at http://gateway:[PORT] with [CREDENTIAL_REDACTED]."
    tts_mod.synthesize(raw_text)

    assert len(captured_input) == 1
    spoken = captured_input[0].decode()
    assert "**" not in spoken, "Bold marker must be stripped before Piper"
    assert "[PORT]" not in spoken, "[PORT] token must be replaced before Piper"
    assert "[CREDENTIAL_REDACTED]" not in spoken, "Credential token must be replaced before Piper"
    assert "a port" in spoken
    assert "a credential" in spoken


def test_tts_synthesize_only_whitespace_after_normalise_returns_empty(monkeypatch):
    """Text that normalises to empty/whitespace should return b'' without calling Piper."""
    import voice_gateway.tts as tts_mod

    piper_called = []
    monkeypatch.setattr(subprocess, "run", lambda *a, **kw: piper_called.append(True))

    # A string that is only markdown delimiters → normalises to empty.
    result = tts_mod.synthesize("**  **\n---\n")
    assert result == b""
    assert not piper_called, "Piper must not be invoked for empty normalised text"


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
    import asyncio
    import importlib

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


# ── _call_agent unit tests ────────────────────────────────────────────────────


def _forward_resp(agent_response: str, status: int = 201):
    """Build a mock httpx response with a ForwardResponse-shape body."""
    mock = MagicMock()
    mock.status_code = status
    mock.json = MagicMock(
        return_value={
            "id": "abc123",
            "sanitized": False,
            "redactions": [],
            "redaction_count": 0,
            "content_hash": "deadbeef",
            "forwarded_to": "hermes",
            "timestamp": "2026-06-24T00:00:00Z",
            "agent_response": agent_response,
        }
    )
    mock.raise_for_status = MagicMock()
    return mock


@pytest.mark.asyncio
async def test_call_agent_returns_agent_response():
    """_call_agent POSTs to /forward and returns agent_response when non-empty."""
    from voice_gateway.server import _call_agent

    with patch(
        "httpx.AsyncClient.post",
        new=AsyncMock(return_value=_forward_resp("Hello from Hermes!")),
    ):
        result = await _call_agent("what is the weather", "hermes")

    assert result == "Hello from Hermes!"


@pytest.mark.asyncio
async def test_call_agent_async_agent_returns_telegram_notice():
    """_call_agent returns an honest spoken notice for agents with empty agent_response."""
    from voice_gateway.server import _call_agent

    with patch(
        "httpx.AsyncClient.post",
        new=AsyncMock(return_value=_forward_resp("")),
    ):
        result = await _call_agent("do something", "openclaw")

    assert "Telegram" in result
    assert "openclaw" in result.lower() or "Openclaw" in result


@pytest.mark.asyncio
async def test_call_agent_null_agent_response_returns_telegram_notice():
    """agent_response key absent in body → honest Telegram notice, no crash."""
    from voice_gateway.server import _call_agent

    mock = MagicMock()
    mock.status_code = 201
    mock.json = MagicMock(
        return_value={
            "id": "x",
            "sanitized": False,
            "redactions": [],
            "redaction_count": 0,
            "content_hash": "ff",
            "forwarded_to": "openclaw",
            "timestamp": "2026-06-24T00:00:00Z",
            # agent_response key intentionally absent
        }
    )
    mock.raise_for_status = MagicMock()

    with patch("httpx.AsyncClient.post", new=AsyncMock(return_value=mock)):
        result = await _call_agent("hello", "openclaw")

    assert "Telegram" in result


@pytest.mark.asyncio
async def test_call_agent_posts_to_forward_endpoint(monkeypatch):
    """_call_agent must POST to /forward, not /v1/chat/completions."""
    import voice_gateway.server as srv

    monkeypatch.setattr(srv, "_GATEWAY_URL", "http://gateway:8080")
    monkeypatch.setattr(srv, "_GATEWAY_TOKEN", "test-bearer")
    monkeypatch.setattr(srv, "_OWNER_USER_ID", "9999")

    captured: dict = {}

    async def _capture(url, json=None, headers=None, **kw):
        captured["url"] = url
        captured["body"] = json or {}
        captured["headers"] = headers or {}
        return _forward_resp("ok")

    with patch("httpx.AsyncClient.post", new=AsyncMock(side_effect=_capture)):
        await srv._call_agent("test query", "hermes")

    assert captured["url"].endswith("/forward"), f"Expected /forward, got {captured['url']!r}"
    assert captured["body"].get("route_to") == "hermes"
    assert captured["body"].get("source") == "api"
    assert captured["body"].get("content") == "test query"
    assert captured["headers"].get("Authorization") == "Bearer test-bearer"
    assert captured["headers"].get("X-AgentShroud-User-Id") == "9999"


@pytest.mark.asyncio
async def test_call_agent_uses_structured_timeout(monkeypatch):
    """_call_agent must pass a structured httpx.Timeout to AsyncClient.

    The read deadline (35 s) is intentionally shorter than the gateway's own
    internal /forward timeout (120 s) so the ESP returns to IDLE quickly on a
    hung agent instead of sitting in THINKING for two minutes.
    """
    import httpx
    import voice_gateway.server as srv

    captured_timeout: dict = {}

    class _FakeClient:
        def __init__(self, *args, **kwargs):
            captured_timeout["timeout"] = kwargs.get("timeout")

        async def __aenter__(self):
            return self

        async def __aexit__(self, *a):
            pass

        async def post(self, url, **kw):
            return _forward_resp("ok")

    monkeypatch.setattr(srv.httpx, "AsyncClient", _FakeClient)

    await srv._call_agent("hi", "hermes")

    assert "timeout" in captured_timeout, "_call_agent must pass a timeout to AsyncClient"
    t = captured_timeout["timeout"]
    assert isinstance(t, httpx.Timeout), (
        f"Expected httpx.Timeout instance, got {type(t)}: {t!r}"
    )
    assert t.read == 35.0, f"Expected read=35.0 (ESP THINKING deadline), got {t.read}"
    assert t.connect == 10.0, f"Expected connect=10.0, got {t.connect}"


# ── Agent dispatch routing tests ──────────────────────────────────────────────


@pytest.mark.asyncio
async def test_ws_direct_agent_calls_call_llm(monkeypatch):
    """?agent=direct must route to _call_llm (fast path), not /forward."""
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod

    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "hello")
    monkeypatch.setattr(tts_mod, "synthesize", lambda t: _pcm_bytes(20))
    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    monkeypatch.setattr(srv, "_DEFAULT_AGENT", "direct")

    llm_called = []
    agent_called = []

    original_call_agent = srv._call_agent if hasattr(srv, "_call_agent") else None

    async def _mock_llm(history):
        llm_called.append(True)
        return "fast reply"

    async def _mock_agent(transcript, agent):
        agent_called.append(agent)
        return "agent reply"

    monkeypatch.setattr(srv, "_call_llm", _mock_llm)
    if original_call_agent:
        monkeypatch.setattr(srv, "_call_agent", _mock_agent)

    with TestClient(app) as client:
        with client.websocket_connect("/voice?agent=direct") as ws:
            ws.receive_text()  # idle
            ws.send_text("LISTEN")
            ws.receive_text()  # listening
            ws.send_bytes(_pcm_bytes())
            ws.send_text("END")
            # drain responses
            for _ in range(15):
                try:
                    msg = ws.receive()
                    if "text" in msg:
                        try:
                            d = json.loads(msg["text"])
                            if d.get("state") == "idle":
                                break
                        except Exception:
                            pass
                except Exception:
                    break

    assert len(llm_called) >= 1, "direct agent must call _call_llm"
    assert len(agent_called) == 0, "direct agent must NOT call _call_agent"


@pytest.mark.asyncio
async def test_ws_hermes_agent_calls_call_agent(monkeypatch):
    """?agent=hermes must route to _call_agent (gateway /forward), not _call_llm."""
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod

    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "hello hermes")
    monkeypatch.setattr(tts_mod, "synthesize", lambda t: _pcm_bytes(20))
    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")

    llm_called = []
    agent_called = []

    async def _mock_llm(history):
        llm_called.append(True)
        return "fast reply"

    async def _mock_agent(transcript, agent):
        agent_called.append(agent)
        return "Hermes says hi"

    monkeypatch.setattr(srv, "_call_llm", _mock_llm)
    if hasattr(srv, "_call_agent"):
        monkeypatch.setattr(srv, "_call_agent", _mock_agent)

    with TestClient(app) as client:
        with client.websocket_connect("/voice?agent=hermes") as ws:
            ws.receive_text()  # idle
            ws.send_text("LISTEN")
            ws.receive_text()  # listening
            ws.send_bytes(_pcm_bytes())
            ws.send_text("END")
            for _ in range(15):
                try:
                    msg = ws.receive()
                    if "text" in msg:
                        try:
                            d = json.loads(msg["text"])
                            if d.get("state") == "idle":
                                break
                        except Exception:
                            pass
                except Exception:
                    break

    assert len(agent_called) >= 1, "hermes agent must call _call_agent"
    assert "hermes" in agent_called, f"route_to must be 'hermes', got {agent_called}"
    assert len(llm_called) == 0, "hermes agent must NOT call _call_llm"


def test_ws_default_agent_is_hermes(monkeypatch):
    """When ?agent= is absent the default agent must be 'hermes', not 'direct'."""
    import voice_gateway.server as srv

    assert srv._DEFAULT_AGENT == "hermes", (
        f"Expected _DEFAULT_AGENT='hermes', got {srv._DEFAULT_AGENT!r}"
    )


def test_ws_agent_query_param_absent_uses_default(monkeypatch):
    """No ?agent= param → _DEFAULT_AGENT is used for routing."""
    import voice_gateway.server as srv

    # We just verify the server connects and sends idle (doesn't crash with unknown agent).
    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    monkeypatch.setattr(srv, "_DEFAULT_AGENT", "hermes")

    with TestClient(app) as client:
        with client.websocket_connect("/voice") as ws:
            first = ws.receive_text()
            assert json.loads(first) == {"state": "idle"}


# ── Disconnect-handling tests ─────────────────────────────────────────────────
#
# These tests call voice_endpoint() directly (not via TestClient) to avoid the
# ASGI transport boundary that can deadlock: when the server returns without
# sending an explicit close frame, the TestClient's receive hangs indefinitely.
# Direct invocation runs entirely within one asyncio event loop — no threads.


async def _run_disconnect_test(exc_to_raise, monkeypatch, caplog):
    """
    Directly invoke ``voice_endpoint`` with a mocked WebSocket whose second
    ``receive()`` call raises ``exc_to_raise`` (simulating an ungraceful or
    clean client drop from the websockets-library layer).

    Asserts:
      - No ERROR-level log from voice_gateway.server
      - No exc_info / traceback attached to any voice_gateway log record
      - At least one INFO "Disconnected" line emitted
    """
    import logging
    from unittest.mock import AsyncMock, MagicMock

    import voice_gateway.server as srv

    # Build a minimal mock WebSocket.
    ws = MagicMock()
    ws.client = MagicMock()
    ws.client.__str__ = lambda s: "127.0.0.1:9999"
    params = {}
    ws.query_params = MagicMock()
    ws.query_params.get = lambda k, d="": params.get(k, d)
    ws.accept = AsyncMock()
    ws.close = AsyncMock()
    ws.send_text = AsyncMock()

    # First receive: LISTEN command triggers _send_state(LISTENING) on server.
    # Second receive: raises the target exception → exercises the except chain.
    ws.receive = AsyncMock(side_effect=[
        {"text": "LISTEN", "bytes": None},
        exc_to_raise,
    ])

    original_token = srv._VG_AUTH_TOKEN
    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")  # disable auth

    with caplog.at_level(logging.DEBUG, logger="voice_gateway.server"):
        # voice_endpoint is an ASGI WebSocket handler; call it directly.
        await srv.voice_endpoint(ws)

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", original_token)

    vg_records = [r for r in caplog.records if r.name.startswith("voice_gateway")]

    # 1. No ERROR-level logs
    errors = [r for r in vg_records if r.levelno >= logging.ERROR]
    assert not errors, (
        "Expected no ERROR-level log from voice_gateway.server, got:\n"
        + "\n".join(f"  [{r.levelname}] {r.getMessage()}" for r in errors)
    )

    # 2. No exc_info / traceback
    with_tb = [r for r in vg_records if r.exc_info and r.exc_info[0] is not None]
    assert not with_tb, (
        "Expected no traceback in voice_gateway logs, got:\n"
        + "\n".join(f"  {r.getMessage()}" for r in with_tb)
    )

    # 3. At least one INFO "Disconnected" line
    disconnected = [
        r for r in vg_records
        if "disconnected" in r.getMessage().lower() and r.levelno == logging.INFO
    ]
    assert disconnected, (
        "Expected an INFO 'Disconnected' log from voice_gateway.server, got:\n"
        + "\n".join(f"  [{r.levelname}] {r.getMessage()}" for r in vg_records)
    )


async def test_ws_connectionclosed_error_logs_info_no_traceback(monkeypatch, caplog):
    """ConnectionClosedError (WS code 1006 — ungraceful ESP disconnect, e.g. device
    loses WiFi/power mid-session) must be caught and logged at INFO with no traceback.

    Regression guard: previously fell through to ``except Exception … exc_info=True``
    and dumped a full Starlette/uvicorn traceback on every device reboot/drop.
    """
    from websockets.exceptions import ConnectionClosedError

    await _run_disconnect_test(
        ConnectionClosedError(rcvd=None, sent=None), monkeypatch, caplog
    )


async def test_ws_connectionclosed_ok_logs_info_no_traceback(monkeypatch, caplog):
    """ConnectionClosedOK (WS code 1000/1001 — clean websockets-library close path)
    must also be caught and logged at INFO with no traceback.

    This covers the case where the websockets library signals a graceful close via
    ``ConnectionClosedOK`` rather than Starlette's ``WebSocketDisconnect``.
    """
    from websockets.exceptions import ConnectionClosedOK

    await _run_disconnect_test(
        ConnectionClosedOK(rcvd=None, sent=None), monkeypatch, caplog
    )


async def test_ws_pipeline_error_logs_and_recovers_to_idle(monkeypatch, caplog):
    """When the STT→LLM→TTS pipeline raises, the inner exception handler must:
      1. log the pipeline error at ERROR with exc_info
      2. send the IDLE state back to the client
      3. continue the receive loop (next receive exits via WebSocketDisconnect → INFO log)
    Covers voice_gateway/server.py lines 334-344 and 347.
    """
    import logging
    from unittest.mock import AsyncMock, MagicMock

    import voice_gateway.server as srv
    from fastapi.websockets import WebSocketDisconnect

    # Mock WebSocket
    ws = MagicMock()
    ws.client = MagicMock()
    ws.client.__str__ = lambda s: "127.0.0.1:8888"
    ws.query_params = MagicMock()
    ws.query_params.get = lambda k, d="": "hermes" if k == "agent" else d
    ws.accept = AsyncMock()
    ws.close = AsyncMock()
    ws.send_text = AsyncMock()
    ws.send_bytes = AsyncMock()

    # receive() sequence:
    # 1. LISTEN   → server sends "listening" state
    # 2. PCM bytes → buffered
    # 3. END       → triggers pipeline (STT raises) → inner except catches, sends idle
    # 4. WebSocketDisconnect → outer except WebSocketDisconnect handler (line 347)
    ws.receive = AsyncMock(side_effect=[
        {"text": "LISTEN", "bytes": None},
        {"bytes": b"\x00\x01\x02\x03", "text": None},
        {"text": "END", "bytes": None},
        WebSocketDisconnect(code=1000),
    ])

    # Patch STT to raise so the inner pipeline exception handler fires
    def _failing_transcribe(raw):
        raise RuntimeError("synthetic STT failure for coverage")

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    monkeypatch.setattr(srv._stt, "transcribe", _failing_transcribe)

    with caplog.at_level(logging.DEBUG, logger="voice_gateway.server"):
        await srv.voice_endpoint(ws)

    vg = [r for r in caplog.records if r.name.startswith("voice_gateway")]

    # Inner except: "Pipeline error" at ERROR with exc_info
    pipeline_errors = [r for r in vg if "Pipeline error" in r.getMessage()]
    assert pipeline_errors, f"Expected 'Pipeline error' log, got: {[r.getMessage() for r in vg]}"
    assert pipeline_errors[0].levelno == logging.ERROR
    assert pipeline_errors[0].exc_info is not None

    # Outer except WebSocketDisconnect: "Disconnected" at INFO (line 347)
    disconnected = [
        r for r in vg
        if "disconnected" in r.getMessage().lower() and r.levelno == logging.INFO
    ]
    assert disconnected, f"Expected INFO 'Disconnected' log, got: {[r.getMessage() for r in vg]}"

    # Recovery send: _send_state(IDLE) was called after the pipeline error
    send_calls = [str(c) for c in ws.send_text.call_args_list]
    idle_sends = [c for c in send_calls if '"idle"' in c]
    # At minimum: initial idle + recovery idle = 2 idle sends
    assert len(idle_sends) >= 2, f"Expected ≥2 idle sends (initial + recovery), got: {send_calls}"


async def test_call_agent_read_timeout_returns_fallback(monkeypatch):
    """_call_agent must return a spoken fallback string and log a WARNING when
    httpx raises ReadTimeout (agent hung for > 35 s).
    Covers voice_gateway/server.py lines 224-228.
    """
    from unittest.mock import AsyncMock, patch

    import httpx
    import voice_gateway.server as srv

    with patch(
        "httpx.AsyncClient.post",
        new=AsyncMock(side_effect=httpx.ReadTimeout("timed out")),
    ):
        result = await srv._call_agent("hello", "hermes")

    assert "having trouble" in result.lower() or "try again" in result.lower(), (
        f"Expected fallback string, got: {result!r}"
    )


async def test_ws_direct_agent_pipeline_error_pops_history_and_recovery_send_fails(monkeypatch, caplog):
    """When the LLM raises in the 'direct' agent path:
      - the user message appended to history must be popped (line 339)
      - if the recovery _send_state(IDLE) also raises, lines 343-344 silence it
    Covers server.py lines 339, 343-344 and the outer WebSocketDisconnect handler (347).
    """
    import logging
    from unittest.mock import AsyncMock, MagicMock

    import voice_gateway.server as srv
    from fastapi.websockets import WebSocketDisconnect

    ws = MagicMock()
    ws.client = MagicMock()
    ws.client.__str__ = lambda s: "127.0.0.1:7777"
    ws.query_params = MagicMock()
    # ?agent is absent → default; we'll patch _DEFAULT_AGENT to "direct"
    ws.query_params.get = lambda k, d="": d
    ws.accept = AsyncMock()
    ws.close = AsyncMock()
    ws.send_bytes = AsyncMock()

    # send_text side_effect:
    #  call 1 → initial _send_state(IDLE) — succeeds
    #  call 2 → _send_state(LISTENING)    — succeeds
    #  call 3 → _send_state(THINKING)     — succeeds
    #  call 4 → recovery _send_state(IDLE) after pipeline error — raises → line 343-344
    ws.send_text = AsyncMock(side_effect=[
        None,
        None,
        None,
        RuntimeError("send_text failed during recovery"),
    ])

    ws.receive = AsyncMock(side_effect=[
        {"text": "LISTEN", "bytes": None},
        {"bytes": b"\x00\x01", "text": None},
        {"text": "END", "bytes": None},
        WebSocketDisconnect(code=1000),       # clean exit after recovery
    ])

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    monkeypatch.setattr(srv, "_DEFAULT_AGENT", "direct")
    # STT succeeds so a user message is appended to history before the LLM is called
    monkeypatch.setattr(srv._stt, "transcribe", lambda raw: "test utterance for history pop")

    # LLM raises — triggers inner pipeline except with user message in history
    async def _fail_llm(history):
        raise RuntimeError("synthetic LLM failure for line-339 coverage")

    monkeypatch.setattr(srv, "_call_llm", _fail_llm)

    with caplog.at_level(logging.DEBUG, logger="voice_gateway.server"):
        await srv.voice_endpoint(ws)

    vg = [r for r in caplog.records if r.name.startswith("voice_gateway")]

    # Inner pipeline exception logged at ERROR
    pipeline_errors = [r for r in vg if "Pipeline error" in r.getMessage()]
    assert pipeline_errors, f"Expected 'Pipeline error' log, got: {[r.getMessage() for r in vg]}"

    # Outer WebSocketDisconnect logged at INFO (line 347)
    disconnected = [
        r for r in vg
        if "disconnected" in r.getMessage().lower() and r.levelno == logging.INFO
    ]
    assert disconnected, f"Expected INFO 'Disconnected' log, got: {[r.getMessage() for r in vg]}"
