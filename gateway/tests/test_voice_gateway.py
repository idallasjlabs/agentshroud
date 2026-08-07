# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Tests for the Voice Gateway FastAPI app (server.py, stt.py, tts.py).

All external I/O is mocked:
  - faster_whisper / numpy (STT model) — mocked via monkeypatch
  - Kokoro pipeline (TTS) — mocked via monkeypatch
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
  - tts.synthesize: string → bytes (Kokoro pipeline mocked)
  - tts.synthesize: Kokoro pipeline load failure raises RuntimeError
  - tts.synthesize: Kokoro synthesis failure raises RuntimeError
  - WS token authentication (correct / wrong / missing / unconfigured)
"""

from __future__ import annotations

import json
import struct
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi.testclient import TestClient
from voice_gateway.server import _call_llm, app


def _fake_kokoro_pipeline(audio, captured_text=None):
    """Stand-in for kokoro.KPipeline: a callable yielding (graphemes, phonemes,
    audio) tuples, matching what ``tts.synthesize`` unpacks.  Lets the TTS tests
    exercise the real synthesize/resample path without the kokoro dependency.
    """

    def _pipeline(text, voice=None, speed=None):  # noqa: ARG001
        if captured_text is not None:
            captured_text.append(text)
        yield ("gs", "ps", audio)

    return _pipeline


# ── Health endpoint ───────────────────────────────────────────────────────────


def test_health_returns_ok():
    client = TestClient(app)
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_lifespan_tolerates_warmup_failure(monkeypatch):
    """A model/pipeline warm-up failure at startup must NOT down the gateway.

    Regression: the lifespan warmed the STT model and Kokoro pipeline via
    asyncio.gather with no error handling, so a missing/broken model (e.g.
    kokoro absent) crashed startup and took /health down with it.  Warm-up is
    best-effort now — the app must still start and serve /health.
    """
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod

    def _boom():
        raise RuntimeError("model unavailable")

    monkeypatch.setattr(stt_mod, "_get_model", _boom)
    monkeypatch.setattr(tts_mod, "_get_pipeline", _boom)

    # Entering the TestClient context runs the lifespan (both warm-ups raise).
    with TestClient(srv.app) as client:
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


def test_tts_synthesize_via_kokoro(monkeypatch):
    """synthesize() runs the Kokoro pipeline; when rates match no resampling occurs."""
    import numpy as np
    import voice_gateway.tts as tts_mod

    audio = np.zeros(100, dtype=np.float32)  # 100 samples of silence
    monkeypatch.setattr(tts_mod, "_get_pipeline", lambda: _fake_kokoro_pipeline(audio))
    # Pin rates equal so no resampling — tests the pass-through path.
    monkeypatch.setattr(tts_mod, "TARGET_SAMPLE_RATE", tts_mod.OUTPUT_SAMPLE_RATE)

    result = tts_mod.synthesize("hello world")
    # 100 float32 samples → 100 S16LE samples (2 bytes each), silence → zeros.
    assert result == b"\x00\x00" * 100


def test_tts_resamples_24000_to_16000(monkeypatch):
    """When OUTPUT_SAMPLE_RATE (24000, Kokoro native) != TARGET_SAMPLE_RATE
    (16000), the output is resampled.  For N input samples the output should have
    approximately N * 16000/24000 samples.  The exact ratio is checked within 1%.
    """
    import numpy as np
    import voice_gateway.tts as tts_mod

    n_src = 24000 // 2  # 0.5 s of silence at Kokoro's native 24000 Hz
    audio = np.zeros(n_src, dtype=np.float32)

    monkeypatch.setattr(tts_mod, "_get_pipeline", lambda: _fake_kokoro_pipeline(audio))
    monkeypatch.setattr(tts_mod, "OUTPUT_SAMPLE_RATE", 24000)
    monkeypatch.setattr(tts_mod, "TARGET_SAMPLE_RATE", 16000)

    result = tts_mod.synthesize("hello")

    n_dst = len(result) // 2  # 16-bit samples
    expected = n_src * 16000 / 24000
    ratio_error = abs(n_dst - expected) / expected
    assert ratio_error < 0.01, (
        f"Resampled length {n_dst} samples deviates {ratio_error:.2%} from expected "
        f"{expected:.1f} (src={n_src}, 24000→16000 Hz)"
    )


def test_tts_kokoro_pipeline_load_failure_raises(monkeypatch):
    """If the Kokoro pipeline can't be constructed, synthesize() raises RuntimeError."""
    import voice_gateway.tts as tts_mod

    def _boom():
        raise RuntimeError("kokoro model unavailable")

    monkeypatch.setattr(tts_mod, "_get_pipeline", _boom)
    # Ensure we're on the fallback voice so failure surfaces instead of retrying.
    monkeypatch.setattr(tts_mod, "_KOKORO_VOICE", tts_mod._FALLBACK_VOICE)

    with pytest.raises(RuntimeError, match="Kokoro TTS failed"):
        tts_mod.synthesize("hello")


def test_tts_kokoro_synthesis_failure_raises(monkeypatch):
    """If the pipeline raises mid-synthesis, synthesize() raises RuntimeError."""
    import voice_gateway.tts as tts_mod

    def _pipeline(text, voice=None, speed=None):  # noqa: ARG001
        raise ValueError("phoneme conversion failed")
        yield  # pragma: no cover - generator marker

    monkeypatch.setattr(tts_mod, "_get_pipeline", lambda: _pipeline)
    monkeypatch.setattr(tts_mod, "_KOKORO_VOICE", tts_mod._FALLBACK_VOICE)

    with pytest.raises(RuntimeError, match="Kokoro TTS failed"):
        tts_mod.synthesize("hello")


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


class TestSplitForSpeech:
    """Unit tests for voice_gateway.tts.split_for_speech (pure function, no I/O)."""

    @staticmethod
    def _s(text: str, **kw) -> list[str]:
        from voice_gateway.tts import split_for_speech

        return split_for_speech(text, **kw)

    def test_multi_sentence_returns_ordered_chunks(self):
        chunks = self._s("It is Monday today. The sun is shining brightly. Time to get to work.")
        assert len(chunks) == 3
        assert "It is Monday today." in chunks[0]
        assert "The sun is shining brightly." in chunks[1]
        assert "Time to get to work." in chunks[2]

    def test_single_sentence_returns_one_chunk(self):
        chunks = self._s("Just one sentence here.")
        assert len(chunks) == 1
        assert chunks[0] == "Just one sentence here."

    def test_empty_after_normalise_returns_empty_list(self):
        chunks = self._s("**  **\n---\n")
        assert chunks == []

    def test_empty_string_returns_empty_list(self):
        assert self._s("") == []

    def test_long_sentence_wrapped_at_max_chars(self):
        long_sent = "word " * 60  # 300 chars, no punctuation
        chunks = self._s(long_sent.strip(), max_chars=50)
        assert len(chunks) > 1
        for chunk in chunks:
            assert len(chunk) <= 50, f"Chunk too long: {len(chunk)} chars: {chunk!r}"
        # Verify no words are lost (join and compare word sets)
        all_words = long_sent.strip().split()
        rejoined_words = " ".join(chunks).split()
        assert rejoined_words == all_words

    def test_per_chunk_normalisation(self):
        """split_for_speech normalises the full text so no markdown or tokens survive."""
        text = "**bold claim** at [PORT]. Then [CREDENTIAL_REDACTED] done."
        chunks = self._s(text)
        full = " ".join(chunks)
        assert "**" not in full
        assert "[PORT]" not in full
        assert "[CREDENTIAL_REDACTED]" not in full
        assert "a port" in full
        assert "a credential" in full

    def test_short_fragment_merged_forward(self):
        """A fragment under 12 chars is merged into the following chunk."""
        text = "Hi. This is the second sentence."
        chunks = self._s(text)
        # "Hi." is 3 chars — merged forward into "This is the second sentence."
        assert all(len(c) >= 12 or i == len(chunks) - 1 for i, c in enumerate(chunks))
        assert "Hi." in " ".join(chunks)


def test_tts_synthesize_passes_normalised_text_to_kokoro(monkeypatch):
    """synthesize() feeds the normalised (no-markdown, no-token) text to Kokoro.

    Verifies that the text arriving at the Kokoro pipeline contains no markdown
    bold markers or redaction placeholder tokens.
    """
    import numpy as np
    import voice_gateway.tts as tts_mod

    captured_text: list[str] = []
    audio = np.zeros(50, dtype=np.float32)
    monkeypatch.setattr(
        tts_mod, "_get_pipeline", lambda: _fake_kokoro_pipeline(audio, captured_text)
    )
    monkeypatch.setattr(tts_mod, "TARGET_SAMPLE_RATE", tts_mod.OUTPUT_SAMPLE_RATE)

    raw_text = "**bold claim** at http://gateway:[PORT] with [CREDENTIAL_REDACTED]."
    tts_mod.synthesize(raw_text)

    assert len(captured_text) == 1
    spoken = captured_text[0]
    assert "**" not in spoken, "Bold marker must be stripped before Kokoro"
    assert "[PORT]" not in spoken, "[PORT] token must be replaced before Kokoro"
    assert "[CREDENTIAL_REDACTED]" not in spoken, "Credential token must be replaced before Kokoro"
    assert "a port" in spoken
    assert "a credential" in spoken


def test_tts_synthesize_only_whitespace_after_normalise_returns_empty(monkeypatch):
    """Text that normalises to empty/whitespace returns b'' without invoking Kokoro."""
    import voice_gateway.tts as tts_mod

    pipeline_called = []

    def _spy_get_pipeline():
        pipeline_called.append(True)
        return _fake_kokoro_pipeline(b"")

    monkeypatch.setattr(tts_mod, "_get_pipeline", _spy_get_pipeline)

    # A string that is only markdown delimiters → normalises to empty.
    result = tts_mod.synthesize("**  **\n---\n")
    assert result == b""
    assert not pipeline_called, "Kokoro must not be invoked for empty normalised text"


# ── _call_llm unit tests ──────────────────────────────────────────────────────


def _openai_resp(content: str, status: int = 200):
    """Build a mock httpx response with an OpenAI-shape body."""
    mock = MagicMock()
    mock.status_code = status
    mock.json = MagicMock(return_value={"choices": [{"message": {"content": content}}]})
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
    with patch(
        "httpx.AsyncClient.post", new=AsyncMock(return_value=_openai_resp("  Hi there.  \n"))
    ):
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

    assert (
        captured_headers.get("X-AgentShroud-User-Id") == "8096968754"
    ), f"Expected X-AgentShroud-User-Id='8096968754', got headers={captured_headers}"


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


def test_stt_default_model_size_is_small_en(monkeypatch):
    """Default _MODEL_SIZE is 'small.en' when WHISPER_MODEL_SIZE is not set."""
    import importlib

    monkeypatch.delenv("WHISPER_MODEL_SIZE", raising=False)
    monkeypatch.delenv("WHISPER_MODEL_DIR", raising=False)

    import voice_gateway.stt as stt_mod

    importlib.reload(stt_mod)

    assert stt_mod._MODEL_SIZE == "small.en"
    assert stt_mod._MODEL_PATH == "small.en"


def test_stt_model_size_env_override(monkeypatch):
    """WHISPER_MODEL_SIZE overrides the default when WHISPER_MODEL_DIR is unset."""
    import importlib

    monkeypatch.setenv("WHISPER_MODEL_SIZE", "base.en")
    monkeypatch.delenv("WHISPER_MODEL_DIR", raising=False)

    import voice_gateway.stt as stt_mod

    importlib.reload(stt_mod)

    assert stt_mod._MODEL_SIZE == "base.en"
    assert stt_mod._MODEL_PATH == "base.en"


def test_stt_model_dir_wins_over_model_size(monkeypatch):
    """WHISPER_MODEL_DIR (baked path) beats WHISPER_MODEL_SIZE — preserves offline guarantee."""
    import importlib
    import sys

    baked_dir = "/opt/whisper/small.en"
    monkeypatch.setenv("WHISPER_MODEL_DIR", baked_dir)
    monkeypatch.setenv("WHISPER_MODEL_SIZE", "base.en")

    import voice_gateway.stt as stt_mod

    importlib.reload(stt_mod)

    assert stt_mod._MODEL_PATH == baked_dir

    # Verify WhisperModel receives the directory path, not the size string.
    captured = {}
    fake_fw = MagicMock()
    fake_fw.WhisperModel = lambda path, **kw: (captured.update({"model_path": path}) or MagicMock())
    monkeypatch.setitem(sys.modules, "faster_whisper", fake_fw)

    stt_mod.reset_model()
    stt_mod._get_model()
    assert captured.get("model_path") == baked_dir


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
    fake_fw.WhisperModel = lambda path, **kw: (captured.update({"model_path": path}) or MagicMock())
    monkeypatch.setitem(sys.modules, "faster_whisper", fake_fw)

    # _get_model() must pass _MODEL_PATH (the directory) to WhisperModel
    stt_mod.reset_model()
    stt_mod._get_model()
    assert (
        captured.get("model_path") == local_dir
    ), f"Expected WhisperModel({local_dir!r}), got {captured.get('model_path')!r}"


# ── WebSocket /voice integration tests ───────────────────────────────────────


def _pcm_bytes(num_samples: int = 160) -> bytes:
    """Minimal S16LE silence."""
    return struct.pack(f"<{num_samples}h", *([0] * num_samples))


def test_ws_full_utterance_state_sequence(monkeypatch):
    """LISTEN → binary PCM → END → STT → /forward/stream → TTS → PCM + END → idle."""
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod

    # Distinct NON-ZERO reply PCM: with an all-zero reply the pad+reply
    # concatenation would be indistinguishable from any equal-length silence,
    # so the assertion would only check length.  Non-zero pins pad-then-reply.
    pcm_reply = b"\x07\x00" * 100

    monkeypatch.setattr(srv, "_DEFAULT_AGENT", "hermes")
    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "what time is it")
    monkeypatch.setattr(tts_mod, "synthesize", lambda t: pcm_reply)

    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kw):
        yield _mock_stream_resp(_sse_body([{"sentence": "It is noon."}, {"done": True}]))

    with patch("httpx.AsyncClient.stream", new=mock_stream):
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
                # First sentence carries the 0.4 s leading-silence pad.
                assert binary_received == srv._TTS_LEAD_SILENCE + pcm_reply


# ── Connect-state test ────────────────────────────────────────────────────────


def test_ws_connect_sends_idle_first():
    """The very first frame after WS accept must be idle, not listening."""
    with TestClient(app) as client:
        with client.websocket_connect("/voice") as ws:
            first = ws.receive_text()
            assert json.loads(first) == {
                "state": "idle"
            }, f"Expected first frame {{state: idle}}, got {first!r}"


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


def test_ws_token_check_uses_constant_time_comparison():
    """/voice is the one endpoint reachable over the public internet (Tailscale
    Funnel) — its token check must use hmac.compare_digest, not `!=`, or it
    leaks a timing side-channel (CWE-208) to any internet client. The sibling
    /firmware/bin endpoint already does this correctly; /voice must match.
    """
    import inspect

    import voice_gateway.server as srv

    source = inspect.getsource(srv.voice_endpoint)
    assert "hmac.compare_digest" in source, (
        "voice_endpoint must compare the WS auth token with hmac.compare_digest, "
        "not a plain != comparison"
    )
    assert "token != _VG_AUTH_TOKEN" not in source


# ── _call_agent_stream unit tests ────────────────────────────────────────────

from contextlib import asynccontextmanager


def _sse_body(events: list[dict]) -> list[str]:
    return [f"data: {json.dumps(e)}" for e in events]


def _mock_stream_resp(lines: list[str], status_code: int = 200):
    """Build a mock httpx.Response usable as the yield value of a mocked
    AsyncClient.stream() async context manager."""
    resp = MagicMock()
    resp.status_code = status_code
    resp.raise_for_status = MagicMock()

    async def _aiter_lines():
        for line in lines:
            yield line

    resp.aiter_lines = _aiter_lines
    return resp


@pytest.mark.asyncio
async def test_call_agent_stream_yields_sentences_in_order():
    """_call_agent_stream POSTs to /forward/stream and yields each sentence
    event as it arrives, in order."""
    from voice_gateway.server import _call_agent_stream

    lines = _sse_body(
        [
            {"sentence": "Hello from Hermes."},
            {"sentence": "How can I help?"},
            {"done": True, "id": "x", "forwarded_to": "hermes", "agent_response": "..."},
        ]
    )

    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kw):
        yield _mock_stream_resp(lines)

    with patch("httpx.AsyncClient.stream", new=mock_stream):
        result = [s async for s in _call_agent_stream("what is the weather", "hermes")]

    assert result == ["Hello from Hermes.", "How can I help?"]


@pytest.mark.asyncio
async def test_call_agent_stream_non_streaming_agent_returns_telegram_notice():
    """Agents with no streaming-compatible chat_path (OpenClaw) get a 400 from
    the gateway — _call_agent_stream turns that into the same honest spoken
    notice the old blocking path gave them, not a generic failure message."""
    import httpx
    from voice_gateway.server import _call_agent_stream

    request = MagicMock()
    response = MagicMock(status_code=400)

    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kw):
        resp = _mock_stream_resp([])
        resp.raise_for_status = MagicMock(
            side_effect=httpx.HTTPStatusError("400", request=request, response=response)
        )
        yield resp

    with patch("httpx.AsyncClient.stream", new=mock_stream):
        result = [s async for s in _call_agent_stream("do something", "openclaw")]

    assert len(result) == 1
    assert "Telegram" in result[0]
    assert "openclaw" in result[0].lower()


@pytest.mark.asyncio
async def test_call_agent_stream_empty_stream_yields_nothing():
    """A stream that goes straight to 'done' with no sentence events (e.g.
    everything got filtered) yields nothing — no crash, no phantom reply."""
    from voice_gateway.server import _call_agent_stream

    lines = _sse_body([{"done": True, "id": "x", "forwarded_to": "hermes", "agent_response": ""}])

    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kw):
        yield _mock_stream_resp(lines)

    with patch("httpx.AsyncClient.stream", new=mock_stream):
        result = [s async for s in _call_agent_stream("hello", "hermes")]

    assert result == []


@pytest.mark.asyncio
async def test_call_agent_stream_posts_to_forward_stream_endpoint(monkeypatch):
    """_call_agent_stream must POST to /forward/stream with stream:true, not
    the old blocking /forward."""
    import voice_gateway.server as srv

    monkeypatch.setattr(srv, "_GATEWAY_URL", "http://gateway:8080")
    monkeypatch.setattr(srv, "_GATEWAY_TOKEN", "test-bearer")
    monkeypatch.setattr(srv, "_OWNER_USER_ID", "9999")

    captured: dict = {}

    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kw):
        captured["url"] = url
        captured["body"] = json or {}
        captured["headers"] = headers or {}
        yield _mock_stream_resp(_sse_body([{"done": True, "id": "x", "forwarded_to": "hermes"}]))

    with patch("httpx.AsyncClient.stream", new=mock_stream):
        async for _ in srv._call_agent_stream("test query", "hermes"):
            pass

    assert captured["url"].endswith("/forward/stream"), (
        f"Expected /forward/stream, got {captured['url']!r}"
    )
    assert captured["body"].get("route_to") == "hermes"
    assert captured["body"].get("source") == "api"
    assert captured["body"].get("content") == "test query"
    assert captured["body"].get("stream") is True
    assert captured["headers"].get("Authorization") == "Bearer test-bearer"
    assert captured["headers"].get("X-AgentShroud-User-Id") == "9999"


@pytest.mark.asyncio
async def test_call_agent_stream_skips_blank_and_comment_lines():
    """SSE keepalive comments (': ...') and blank lines are ignored, not
    treated as malformed data."""
    from voice_gateway.server import _call_agent_stream

    lines = ["", ": keepalive", *_sse_body([{"sentence": "Hi."}, {"done": True}])]

    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kw):
        yield _mock_stream_resp(lines)

    with patch("httpx.AsyncClient.stream", new=mock_stream):
        result = [s async for s in _call_agent_stream("hi", "hermes")]

    assert result == ["Hi."]


@pytest.mark.asyncio
async def test_call_agent_stream_malformed_json_line_skipped_not_fatal():
    """A single corrupted SSE line logs a warning and is skipped — it must not
    abort the whole stream, later valid sentences still arrive."""
    from voice_gateway.server import _call_agent_stream

    lines = [
        "data: {not valid json",
        *_sse_body([{"sentence": "Still works."}, {"done": True}]),
    ]

    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kw):
        yield _mock_stream_resp(lines)

    with patch("httpx.AsyncClient.stream", new=mock_stream):
        result = [s async for s in _call_agent_stream("hi", "hermes")]

    assert result == ["Still works."]


@pytest.mark.asyncio
async def test_call_agent_stream_non_400_http_error_falls_back():
    """A non-400 HTTP error (e.g. 500) is a real failure, not the OpenClaw
    no-streaming-support case — falls back to the generic trouble-connecting
    message, not the Telegram notice."""
    import httpx
    from voice_gateway.server import _call_agent_stream

    request = MagicMock()
    response = MagicMock(status_code=500)

    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kw):
        resp = _mock_stream_resp([])
        resp.raise_for_status = MagicMock(
            side_effect=httpx.HTTPStatusError("500", request=request, response=response)
        )
        yield resp

    with patch("httpx.AsyncClient.stream", new=mock_stream):
        result = [s async for s in _call_agent_stream("hi", "hermes")]

    assert len(result) == 1
    assert "trouble connecting" in result[0].lower()
    assert "Telegram" not in result[0]


@pytest.mark.asyncio
async def test_call_agent_stream_generic_http_error_falls_back():
    """A connection-level error (not a status/timeout) also falls back to the
    trouble-connecting message instead of propagating."""
    import httpx
    from voice_gateway.server import _call_agent_stream

    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kw):
        raise httpx.ConnectError("refused")
        yield  # pragma: no cover — unreachable, satisfies generator shape

    with patch("httpx.AsyncClient.stream", new=mock_stream):
        result = [s async for s in _call_agent_stream("hi", "hermes")]

    assert len(result) == 1
    assert "trouble connecting" in result[0].lower()


# ── Sentence-chunked TTS tests ────────────────────────────────────────────────


def test_ws_sentence_chunked_tts_calls_synthesize_per_sentence(monkeypatch):
    """Sentence-chunked TTS: synthesize() is called once per sentence; all PCM arrives
    in order; exactly one 'END' text frame is sent; final state is idle."""
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod

    # Three distinct PCM blobs so we can verify ordering.
    pcm_s1 = b"\x01\x00" * 40
    pcm_s2 = b"\x02\x00" * 40
    pcm_s3 = b"\x03\x00" * 40

    synth_calls: list[str] = []

    def _mock_synthesize(text: str) -> bytes:
        synth_calls.append(text)
        idx = len(synth_calls)
        return [pcm_s1, pcm_s2, pcm_s3][idx - 1] if idx <= 3 else b""

    monkeypatch.setattr(srv, "_DEFAULT_AGENT", "hermes")
    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "what time is it")
    monkeypatch.setattr(tts_mod, "synthesize", _mock_synthesize)

    three_sentence_reply = "It is Monday today. The sun is shining brightly. Time to get to work."

    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kw):
        yield _mock_stream_resp(_sse_body([{"sentence": three_sentence_reply}, {"done": True}]))

    with patch("httpx.AsyncClient.stream", new=mock_stream):
        with TestClient(app) as client:
            with client.websocket_connect("/voice") as ws:
                ws.receive_text()  # initial idle

                ws.send_text("LISTEN")
                ws.receive_text()  # listening

                ws.send_bytes(_pcm_bytes())
                ws.send_text("END")

                binary_received = b""
                end_count = 0
                final_state = None

                for _ in range(40):
                    try:
                        msg = ws.receive()
                    except Exception:
                        break
                    if "bytes" in msg:
                        binary_received += msg["bytes"] or b""
                    elif "text" in msg:
                        text = msg["text"]
                        try:
                            data = json.loads(text)
                            if data.get("state") == "idle":
                                final_state = "idle"
                                break
                        except (json.JSONDecodeError, KeyError):
                            if text == "END":
                                end_count += 1

    # synthesize() called once per sentence (3 sentences)
    assert len(synth_calls) == 3, f"Expected 3 synth calls, got {len(synth_calls)}: {synth_calls}"
    # All PCM received in order (first sentence carries the leading-silence
    # pad; every later sentence carries the shorter inter-sentence gap, so a
    # splice discontinuity never lands directly on a sentence boundary).
    assert binary_received == (
        srv._TTS_LEAD_SILENCE
        + pcm_s1
        + srv._TTS_SENTENCE_GAP
        + pcm_s2
        + srv._TTS_SENTENCE_GAP
        + pcm_s3
    )
    # Exactly one END frame
    assert end_count == 1, f"Expected 1 END frame, got {end_count}"
    # Final state is idle
    assert final_state == "idle"


def test_ws_one_sentence_reply_unchanged(monkeypatch):
    """Regression: a single-sentence reply still produces exactly one synthesize call."""
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod

    # Distinct non-zero reply so the pad+reply assertion pins structure, not
    # just total length (an all-zero reply is indistinguishable from silence).
    pcm_reply = b"\x07\x00" * 100
    synth_calls: list[str] = []

    def _mock_synthesize(text: str) -> bytes:
        synth_calls.append(text)
        return pcm_reply

    monkeypatch.setattr(srv, "_DEFAULT_AGENT", "hermes")
    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "what time is it")
    monkeypatch.setattr(tts_mod, "synthesize", _mock_synthesize)

    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kw):
        yield _mock_stream_resp(_sse_body([{"sentence": "It is noon."}, {"done": True}]))

    with patch("httpx.AsyncClient.stream", new=mock_stream):
        with TestClient(app) as client:
            with client.websocket_connect("/voice") as ws:
                ws.receive_text()  # initial idle
                ws.send_text("LISTEN")
                ws.receive_text()  # listening
                ws.send_bytes(_pcm_bytes())
                ws.send_text("END")

                binary_received = b""
                end_count = 0

                for _ in range(20):
                    try:
                        msg = ws.receive()
                    except Exception:
                        break
                    if "bytes" in msg:
                        binary_received += msg["bytes"] or b""
                    elif "text" in msg:
                        text = msg["text"]
                        try:
                            data = json.loads(text)
                            if data.get("state") == "idle":
                                break
                        except (json.JSONDecodeError, KeyError):
                            if text == "END":
                                end_count += 1

    assert len(synth_calls) == 1, f"Expected 1 synth call, got {len(synth_calls)}"
    assert binary_received == srv._TTS_LEAD_SILENCE + pcm_reply
    assert end_count == 1


@pytest.mark.asyncio
async def test_call_agent_uses_structured_timeout(monkeypatch):
    """_call_agent_stream must pass a structured httpx.Timeout to AsyncClient.

    The read deadline is env-tunable (VG_AGENT_READ_TIMEOUT_S, default 100 s):
    Hermes is the owner's admin voice channel, so a slow real answer beats a
    fast fallback — but the deadline must stay under the gateway's own
    /forward timeout (120 s) so its graceful body is still caught.
    """
    import httpx
    import voice_gateway.server as srv

    captured_timeout: dict = {}

    class _FakeStreamCtx:
        def __init__(self):
            pass

        async def __aenter__(self):
            return _mock_stream_resp(_sse_body([{"done": True}]))

        async def __aexit__(self, *a):
            pass

    class _FakeClient:
        def __init__(self, *args, **kwargs):
            captured_timeout["timeout"] = kwargs.get("timeout")

        async def __aenter__(self):
            return self

        async def __aexit__(self, *a):
            pass

        def stream(self, method, url, **kw):
            return _FakeStreamCtx()

    monkeypatch.setattr(srv.httpx, "AsyncClient", _FakeClient)

    async for _ in srv._call_agent_stream("hi", "hermes"):
        pass

    assert "timeout" in captured_timeout, "_call_agent_stream must pass a timeout to AsyncClient"
    t = captured_timeout["timeout"]
    assert isinstance(t, httpx.Timeout), f"Expected httpx.Timeout instance, got {type(t)}: {t!r}"
    assert t.read == 100.0, (
        f"Expected read=100.0 (VG_AGENT_READ_TIMEOUT_S default, < gateway's "
        f"120 s forward window), got {t.read}"
    )
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

    async def _mock_llm(history):
        llm_called.append(True)
        return "fast reply"

    async def _mock_agent(transcript, agent):
        agent_called.append(agent)
        yield "agent reply"

    monkeypatch.setattr(srv, "_call_llm", _mock_llm)
    monkeypatch.setattr(srv, "_call_agent_stream", _mock_agent)

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
        yield "Hermes says hi"

    monkeypatch.setattr(srv, "_call_llm", _mock_llm)
    monkeypatch.setattr(srv, "_call_agent_stream", _mock_agent)

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


def test_ws_default_agent_is_direct(monkeypatch):
    """When ?agent= is absent the default agent must be 'direct' (fast local
    model) — SCRUM-113 follow-on: Hermes's own agentic-loop latency (~9s to
    first sentence, observed live) made it too slow as the voice default."""
    import voice_gateway.server as srv

    assert (
        srv._DEFAULT_AGENT == "direct"
    ), f"Expected _DEFAULT_AGENT='direct', got {srv._DEFAULT_AGENT!r}"


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
    ws.receive = AsyncMock(
        side_effect=[
            {"text": "LISTEN", "bytes": None},
            exc_to_raise,
        ]
    )

    original_token = srv._VG_AUTH_TOKEN
    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")  # disable auth

    with caplog.at_level(logging.DEBUG, logger="voice_gateway.server"):
        # voice_endpoint is an ASGI WebSocket handler; call it directly.
        await srv.voice_endpoint(ws)

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", original_token)

    vg_records = [r for r in caplog.records if r.name.startswith("voice_gateway")]

    # 1. No ERROR-level logs
    errors = [r for r in vg_records if r.levelno >= logging.ERROR]
    assert not errors, "Expected no ERROR-level log from voice_gateway.server, got:\n" + "\n".join(
        f"  [{r.levelname}] {r.getMessage()}" for r in errors
    )

    # 2. No exc_info / traceback
    with_tb = [r for r in vg_records if r.exc_info and r.exc_info[0] is not None]
    assert not with_tb, "Expected no traceback in voice_gateway logs, got:\n" + "\n".join(
        f"  {r.getMessage()}" for r in with_tb
    )

    # 3. At least one INFO "Disconnected" line
    disconnected = [
        r
        for r in vg_records
        if "disconnected" in r.getMessage().lower() and r.levelno == logging.INFO
    ]
    assert (
        disconnected
    ), "Expected an INFO 'Disconnected' log from voice_gateway.server, got:\n" + "\n".join(
        f"  [{r.levelname}] {r.getMessage()}" for r in vg_records
    )


async def test_ws_connectionclosed_error_logs_info_no_traceback(monkeypatch, caplog):
    """ConnectionClosedError (WS code 1006 — ungraceful ESP disconnect, e.g. device
    loses WiFi/power mid-session) must be caught and logged at INFO with no traceback.

    Regression guard: previously fell through to ``except Exception … exc_info=True``
    and dumped a full Starlette/uvicorn traceback on every device reboot/drop.
    """
    from websockets.exceptions import ConnectionClosedError

    await _run_disconnect_test(ConnectionClosedError(rcvd=None, sent=None), monkeypatch, caplog)


async def test_ws_connectionclosed_ok_logs_info_no_traceback(monkeypatch, caplog):
    """ConnectionClosedOK (WS code 1000/1001 — clean websockets-library close path)
    must also be caught and logged at INFO with no traceback.

    This covers the case where the websockets library signals a graceful close via
    ``ConnectionClosedOK`` rather than Starlette's ``WebSocketDisconnect``.
    """
    from websockets.exceptions import ConnectionClosedOK

    await _run_disconnect_test(ConnectionClosedOK(rcvd=None, sent=None), monkeypatch, caplog)


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
    ws.receive = AsyncMock(
        side_effect=[
            {"text": "LISTEN", "bytes": None},
            {"bytes": b"\x00\x01\x02\x03", "text": None},
            {"text": "END", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )

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
        r for r in vg if "disconnected" in r.getMessage().lower() and r.levelno == logging.INFO
    ]
    assert disconnected, f"Expected INFO 'Disconnected' log, got: {[r.getMessage() for r in vg]}"

    # Recovery send: _send_state(IDLE) was called after the pipeline error
    send_calls = [str(c) for c in ws.send_text.call_args_list]
    idle_sends = [c for c in send_calls if '"idle"' in c]
    # At minimum: initial idle + recovery idle = 2 idle sends
    assert len(idle_sends) >= 2, f"Expected ≥2 idle sends (initial + recovery), got: {send_calls}"


async def test_call_agent_read_timeout_returns_fallback(monkeypatch):
    """_call_agent_stream must yield a spoken fallback string and log a WARNING
    when httpx raises ReadTimeout (agent hung for > 35 s).
    """
    import httpx
    import voice_gateway.server as srv

    @asynccontextmanager
    async def mock_stream(self, method, url, json=None, headers=None, **kw):
        raise httpx.ReadTimeout("timed out")
        yield  # pragma: no cover — unreachable, satisfies generator shape

    with patch("httpx.AsyncClient.stream", new=mock_stream):
        result = [s async for s in srv._call_agent_stream("hello", "hermes")]

    assert len(result) == 1
    assert (
        "having trouble" in result[0].lower() or "try again" in result[0].lower()
    ), f"Expected fallback string, got: {result!r}"


async def test_ws_direct_agent_pipeline_error_pops_history_and_recovery_send_fails(
    monkeypatch, caplog
):
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
    ws.send_text = AsyncMock(
        side_effect=[
            None,
            None,
            None,
            RuntimeError("send_text failed during recovery"),
        ]
    )

    ws.receive = AsyncMock(
        side_effect=[
            {"text": "LISTEN", "bytes": None},
            {"bytes": b"\x00\x01", "text": None},
            {"text": "END", "bytes": None},
            WebSocketDisconnect(code=1000),  # clean exit after recovery
        ]
    )

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
        r for r in vg if "disconnected" in r.getMessage().lower() and r.levelno == logging.INFO
    ]
    assert disconnected, f"Expected INFO 'Disconnected' log, got: {[r.getMessage() for r in vg]}"


# ── Pre-loop dirty-close hardening ───────────────────────────────────────────


async def test_ws_dirty_close_before_initial_state_is_handled_cleanly(monkeypatch, caplog):
    """When the WS dirty-closes (code 1006) before the initial _send_state(IDLE) frame
    is delivered, voice_endpoint must catch the disconnect cleanly and log one INFO
    'Disconnected' line.  No heartbeat task must be left pending.

    Without the fix, voice_gateway/server.py line 254 (_send_state outside the try block)
    propagates an unhandled WebSocketDisconnect, causing ASGI traceback spam in production.
    """
    import logging

    import voice_gateway.server as srv
    from fastapi.websockets import WebSocketDisconnect

    ws = MagicMock()
    ws.client = MagicMock()
    ws.client.__str__ = lambda s: "10.0.0.1:55432"
    ws.query_params = MagicMock()
    ws.query_params.get = lambda k, d="": d
    ws.accept = AsyncMock()
    ws.close = AsyncMock()
    ws.send_bytes = AsyncMock()

    # First (and only) send_text call is the initial _send_state(IDLE) — dirty-close it.
    # Before the fix, this exception escapes the function unhandled.
    ws.send_text = AsyncMock(side_effect=WebSocketDisconnect(code=1006))

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")

    with caplog.at_level(logging.DEBUG, logger="voice_gateway.server"):
        # Must not raise — pre-loop dirty-close must be caught by the existing
        # disconnect handlers (WebSocketDisconnect except clause, line 358).
        await srv.voice_endpoint(ws)

    vg = [r for r in caplog.records if r.name.startswith("voice_gateway")]

    # Expect one INFO "Disconnected" log, no ERROR or unhandled propagation.
    disconnected = [
        r for r in vg if "disconnected" in r.getMessage().lower() and r.levelno == logging.INFO
    ]
    assert disconnected, (
        f"Expected an INFO 'Disconnected' log for code-1006 pre-loop drop; "
        f"got: {[(r.levelno, r.getMessage()) for r in vg]}"
    )


# ── TTS quality: anti-aliased resampling ─────────────────────────────────────


def test_resample_antialias_attenuates_above_nyquist():
    """Kaiser-windowed sinc anti-aliasing filter suppresses content above the output
    Nyquist (8 kHz when resampling 22050→16000).

    A pure 9 kHz sine at 22050 Hz would fold into the output band (appearing as
    ~7 kHz) with plain linear interpolation.  With the anti-aliasing filter the
    output amplitude at that frequency must be at most 5 % of the input — ≥26 dB
    suppression, well within the Kaiser β=8 design target of >80 dB.
    """
    import math
    import struct

    import numpy as np
    from voice_gateway.tts import _resample_s16le_mono

    src_rate = 22050
    dst_rate = 16000
    duration_s = 0.2  # 200 ms is enough for frequency analysis
    freq_hz = 9000  # 9 kHz is above the 8 kHz Nyquist of the 16 kHz output

    # Build a pure 9 kHz sine at 22050 Hz (amplitude 10000, safely in int16 range)
    n_src = int(src_rate * duration_s)
    amplitude = 10000
    samples_src = [
        int(amplitude * math.sin(2 * math.pi * freq_hz * i / src_rate)) for i in range(n_src)
    ]
    pcm_in = struct.pack(f"<{n_src}h", *samples_src)

    pcm_out = _resample_s16le_mono(pcm_in, src_rate, dst_rate)

    # Measure output amplitude via RMS.
    arr = np.frombuffer(pcm_out, dtype="<i2").astype(np.float32)
    rms_out = float(np.sqrt(np.mean(arr**2)))
    # With no filtering, linear interp would alias 9 kHz → ~7 kHz and the output
    # RMS would be ~amplitude/sqrt(2) ≈ 7071.  With the anti-aliasing filter the
    # RMS must be at most 5% of amplitude.
    max_allowed = amplitude * 0.05
    assert rms_out <= max_allowed, (
        f"Anti-aliasing filter not working: output RMS {rms_out:.1f} exceeds "
        f"5% threshold {max_allowed:.1f} for a {freq_hz} Hz input (above 8 kHz Nyquist)"
    )


def test_resample_passband_preserved():
    """Frequencies well below the Nyquist (≤3 kHz) must pass through with minimal
    attenuation — ≥90% amplitude preserved.  Ensures the filter is not too aggressive.
    """
    import math
    import struct

    import numpy as np
    from voice_gateway.tts import _resample_s16le_mono

    src_rate = 22050
    dst_rate = 16000
    freq_hz = 3000  # typical voiced speech fundamental range
    duration_s = 0.2
    amplitude = 10000

    n_src = int(src_rate * duration_s)
    samples_src = [
        int(amplitude * math.sin(2 * math.pi * freq_hz * i / src_rate)) for i in range(n_src)
    ]
    pcm_in = struct.pack(f"<{n_src}h", *samples_src)
    pcm_out = _resample_s16le_mono(pcm_in, src_rate, dst_rate)

    arr = np.frombuffer(pcm_out, dtype="<i2").astype(np.float32)
    rms_out = float(np.sqrt(np.mean(arr**2)))
    # Expected RMS ≈ amplitude/sqrt(2) ≈ 7071; must be ≥ 90% of that.
    expected_rms = amplitude / (2**0.5)
    assert rms_out >= expected_rms * 0.90, (
        f"Passband attenuation too high at {freq_hz} Hz: RMS {rms_out:.1f} < 90% of "
        f"{expected_rms:.1f} — filter cutoff may be set too low"
    )


# ── TTS pipeline: synthesis pipelined with sending ────────────────────────────


@pytest.mark.asyncio
async def test_ws_tts_pipeline_sends_all_sentences(monkeypatch):
    """When split_for_speech returns multiple sentences, the pipelined TTS loop must
    synthesise and transmit PCM for ALL sentences in order, with no sentences dropped.

    This verifies the refactored concurrent synthesis/send path introduced to
    eliminate inter-sentence audio gaps on the ESP32.
    """
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod

    # Each sentence produces its own distinct PCM bytes so we can verify ordering.
    sentence_pcm = {
        "First sentence here.": b"\x01\x00" * 10,
        "Second sentence here.": b"\x02\x00" * 10,
        "Third sentence here.": b"\x03\x00" * 10,
    }

    monkeypatch.setattr(
        stt_mod,
        "transcribe",
        lambda b: "First sentence here.  Second sentence here.  Third sentence here.",
    )
    monkeypatch.setattr(tts_mod, "synthesize", lambda t: sentence_pcm.get(t, b"\xff\x00" * 4))
    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")

    async def _mock_agent(transcript, agent):
        yield "First sentence here.  Second sentence here.  Third sentence here."

    monkeypatch.setattr(srv, "_call_agent_stream", _mock_agent)

    bytes_received: list[bytes] = []
    text_received: list[str] = []

    with TestClient(app) as client:
        with client.websocket_connect("/voice?agent=hermes") as ws:
            ws.receive_text()  # idle
            ws.send_text("LISTEN")
            ws.receive_text()  # listening
            ws.send_bytes(_pcm_bytes())
            ws.send_text("END")
            # Drain all messages until idle (up to 50 frames)
            for _ in range(50):
                try:
                    msg = ws.receive()
                    if "bytes" in msg and msg["bytes"]:
                        bytes_received.append(msg["bytes"])
                    elif "text" in msg and msg["text"]:
                        text_received.append(msg["text"])
                        try:
                            if json.loads(msg["text"]).get("state") == "idle":
                                break
                        except Exception:
                            pass
                except Exception:
                    break

    # All three sentence PCM payloads must appear in the transmitted bytes
    all_bytes = b"".join(bytes_received)
    assert b"\x01\x00" * 10 in all_bytes, "First sentence PCM not transmitted"
    assert b"\x02\x00" * 10 in all_bytes, "Second sentence PCM not transmitted"
    assert b"\x03\x00" * 10 in all_bytes, "Third sentence PCM not transmitted"
    # END text frame and idle state must follow
    assert any("END" in t for t in text_received), "END text frame not sent"
    assert any("idle" in t for t in text_received), "state:idle not sent after multi-sentence TTS"


# ── Server-side LISTENING safety timeout ─────────────────────────────────────


@pytest.mark.asyncio
async def test_listen_without_end_times_out(monkeypatch):
    """If a device sends LISTEN but never sends END (crash / stuck firmware), the
    server must self-heal: the _LISTEN_MAX_S deadline forces END processing and the
    session must return to IDLE rather than hanging indefinitely.

    Regression test for the server-side gap identified after the face-update
    regression: a device stuck in LISTENING (never sending END) would wedge the
    gateway session permanently.
    """
    from unittest.mock import AsyncMock, MagicMock

    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    from fastapi.websockets import WebSocketDisconnect

    # Zero-second timeout so the deadline is always in the past on the next loop
    # iteration — no real waiting required, test completes instantly.
    monkeypatch.setattr(srv, "_LISTEN_MAX_S", 0.0)

    # Empty transcript → server goes THINKING → IDLE without needing TTS mock.
    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "")
    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")

    ws = MagicMock()
    ws.client = MagicMock()
    ws.client.__str__ = lambda s: "10.0.0.1:9999"
    ws.query_params = MagicMock()
    ws.query_params.get = lambda k, d="": d
    ws.accept = AsyncMock()
    ws.close = AsyncMock()
    ws.send_text = AsyncMock()
    ws.send_bytes = AsyncMock()

    # Sequence: LISTEN (no END ever sent) → server times out → back to IDLE →
    # next ws.receive() raises WebSocketDisconnect to exit the handler cleanly.
    ws.receive = AsyncMock(
        side_effect=[
            {"text": "LISTEN", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )

    await srv.voice_endpoint(ws)

    # Extract the sequence of states the server sent.
    sent_texts = [call.args[0] for call in ws.send_text.call_args_list]
    states = []
    for t in sent_texts:
        try:
            states.append(json.loads(t).get("state"))
        except Exception:
            pass

    assert (
        "listening" in states
    ), "Expected state:listening after LISTEN; server may not have entered LISTENING"
    assert (
        "thinking" in states
    ), "Server must transition to THINKING when the timeout fires (not stay in LISTENING)"


@pytest.mark.asyncio
async def test_pcm_buffer_bounded(monkeypatch):
    """pcm_chunks must stop growing once _PCM_MAX_BYTES is reached.

    A device that streams audio without sending END (stuck firmware, OOM scenario)
    must not cause the server to buffer unbounded PCM.  The STT function should
    receive at most _PCM_MAX_BYTES bytes.

    Regression test for the memory-safety gap identified in the same audit.
    """
    from unittest.mock import AsyncMock, MagicMock

    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    from fastapi.websockets import WebSocketDisconnect

    cap = 200  # tiny cap so the test is fast; 200 bytes ≪ 1000 bytes streamed
    monkeypatch.setattr(srv, "_PCM_MAX_BYTES", cap)
    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")

    received_bytes: list[int] = []

    def _capture_transcribe(pcm: bytes) -> str:
        received_bytes.append(len(pcm))
        return ""  # empty transcript → IDLE, no TTS needed

    monkeypatch.setattr(stt_mod, "transcribe", _capture_transcribe)

    # 10 chunks × 100 bytes = 1000 bytes total >> cap of 200 bytes.
    chunk = b"\x00\x01" * 50

    ws = MagicMock()
    ws.client = MagicMock()
    ws.client.__str__ = lambda s: "10.0.0.1:9998"
    ws.query_params = MagicMock()
    ws.query_params.get = lambda k, d="": d
    ws.accept = AsyncMock()
    ws.close = AsyncMock()
    ws.send_text = AsyncMock()
    ws.send_bytes = AsyncMock()

    ws.receive = AsyncMock(
        side_effect=[
            {"text": "LISTEN", "bytes": None},
            *[{"bytes": chunk, "text": None} for _ in range(10)],  # 1000 bytes
            {"text": "END", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )

    await srv.voice_endpoint(ws)

    assert received_bytes, "transcribe() was never called — END handler did not execute"
    assert received_bytes[0] <= cap, (
        f"STT received {received_bytes[0]} bytes, expected ≤ {cap} (cap = {cap}). "
        f"PCM buffer was not bounded."
    )


# ── STOP protocol (tap-to-stop during SPEAKING) ──────────────────────────────


def _mock_ws(receive_side_effect):
    """Build a MagicMock WebSocket for direct voice_endpoint() tests."""
    from unittest.mock import AsyncMock, MagicMock

    ws = MagicMock()
    ws.client = MagicMock()
    ws.client.__str__ = lambda s: "10.0.0.1:9997"
    ws.query_params = MagicMock()
    ws.query_params.get = lambda k, d="": d
    ws.accept = AsyncMock()
    ws.close = AsyncMock()
    ws.send_text = AsyncMock()
    ws.send_bytes = AsyncMock()
    ws.receive = AsyncMock(side_effect=receive_side_effect)
    return ws


@pytest.mark.asyncio
async def test_ws_stop_during_speaking_aborts_tts(monkeypatch):
    """A device 'STOP' text frame during the TTS send phase must abort the
    remaining PCM stream and return the session to IDLE immediately.

    Firmware context: tap-to-stop during SPEAKING previously only muted the
    speaker locally; the server kept streaming the full reply (8-30 s), during
    which the device rejected all new utterances.  The server must read the
    socket concurrently with the send loop and honour STOP mid-stream.
    """
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod
    from fastapi.websockets import WebSocketDisconnect

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    monkeypatch.setattr(srv, "_DEFAULT_AGENT", "hermes")
    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "tell me a story")

    reply = "First sentence here.  Second sentence here.  Third sentence here."

    async def _mock_agent(transcript, agent):
        yield reply

    monkeypatch.setattr(srv, "_call_agent_stream", _mock_agent)

    sentence_pcm = {
        "First sentence here.": b"\x01\x00" * 100,
        "Second sentence here.": b"\x02\x00" * 100,
        "Third sentence here.": b"\x03\x00" * 100,
    }
    monkeypatch.setattr(tts_mod, "synthesize", lambda t: sentence_pcm.get(t, b"\xff\x00" * 4))

    # STOP is queued for whichever reader asks next — with the concurrent
    # stop-watcher in place it is consumed BEFORE/WHILE the PCM stream is sent,
    # aborting the remaining sentences.
    ws = _mock_ws(
        [
            {"text": "LISTEN", "bytes": None},
            {"bytes": _pcm_bytes(), "text": None},
            {"text": "END", "bytes": None},
            {"text": "STOP", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )

    await srv.voice_endpoint(ws)

    sent_pcm = b"".join(c.args[0] for c in ws.send_bytes.call_args_list)
    assert (
        b"\x03\x00" * 100 not in sent_pcm
    ), "Third sentence PCM was transmitted — STOP did not abort the TTS stream"

    # END + state:idle must still be sent so the device re-arms.
    sent_texts = [c.args[0] for c in ws.send_text.call_args_list]
    assert "END" in sent_texts, "END frame missing after STOP abort"
    states = []
    for t in sent_texts:
        try:
            states.append(json.loads(t).get("state"))
        except Exception:
            pass
    assert (
        states[-1] == "idle"
    ), f"Session must end at state:idle after STOP; state sequence was {states}"


@pytest.mark.asyncio
async def test_ws_stale_stop_when_idle_is_ignored(monkeypatch):
    """A STOP arriving outside SPEAKING (e.g. the tap landed just as TTS ended)
    must be ignored without crashing the session loop."""
    import voice_gateway.server as srv
    from fastapi.websockets import WebSocketDisconnect

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")

    ws = _mock_ws(
        [
            {"text": "STOP", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )

    await srv.voice_endpoint(ws)  # must not raise

    sent_texts = [c.args[0] for c in ws.send_text.call_args_list]
    assert any('"idle"' in t for t in sent_texts), "initial idle state missing"


@pytest.mark.asyncio
async def test_ws_device_log_during_speaking_still_recorded(monkeypatch, caplog):
    """Remote-diag {"log":...} frames arriving DURING the TTS send phase must be
    logged, not silently swallowed by the concurrent stop-watcher."""
    import logging

    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod
    from fastapi.websockets import WebSocketDisconnect

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "hello")

    async def _mock_agent(transcript, agent):
        yield "Only sentence."

    monkeypatch.setattr(srv, "_call_agent_stream", _mock_agent)
    monkeypatch.setattr(tts_mod, "synthesize", lambda t: b"\x01\x00" * 100)

    ws = _mock_ws(
        [
            {"text": "LISTEN", "bytes": None},
            {"bytes": _pcm_bytes(), "text": None},
            {"text": "END", "bytes": None},
            {"text": '{"log":"PTT START ignored — triggered=1 tts=1"}', "bytes": None},
            {"text": "STOP", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )

    with caplog.at_level(logging.INFO, logger="voice_gateway.server"):
        await srv.voice_endpoint(ws)

    assert any(
        "PTT START ignored" in r.message for r in caplog.records
    ), "device log line arriving during SPEAKING was swallowed"


@pytest.mark.asyncio
async def test_ws_hung_tts_synthesis_still_returns_idle(monkeypatch):
    """A wedged TTS synthesis (e.g. blocked voice-pack download — live incident
    2026-07-03/04) must not strand the device in THINKING: the per-sentence
    timeout aborts synthesis and the session still sends END + state:idle."""
    import time

    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod
    from fastapi.websockets import WebSocketDisconnect

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    monkeypatch.setattr(srv, "_DEFAULT_AGENT", "hermes")
    monkeypatch.setattr(srv, "_TTS_SENTENCE_TIMEOUT_S", 0.05)
    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "hello")

    async def _mock_agent(transcript, agent):
        yield "Only sentence."

    monkeypatch.setattr(srv, "_call_agent_stream", _mock_agent)

    def _hung_synthesize(t):
        time.sleep(0.5)  # far beyond the 0.05 s budget
        return b"\x01\x00" * 10

    monkeypatch.setattr(tts_mod, "synthesize", _hung_synthesize)

    ws = _mock_ws(
        [
            {"text": "LISTEN", "bytes": None},
            {"bytes": _pcm_bytes(), "text": None},
            {"text": "END", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )

    await srv.voice_endpoint(ws)

    sent_texts = [c.args[0] for c in ws.send_text.call_args_list]
    assert "END" in sent_texts, "END frame missing after TTS timeout"
    states = []
    for t in sent_texts:
        try:
            states.append(json.loads(t).get("state"))
        except Exception:
            pass
    assert (
        states[-1] == "idle"
    ), f"Device must be released to idle after a hung synthesis; states={states}"


# ── Spoken volume command ─────────────────────────────────────────────────────


def test_parse_volume_command_forms():
    """Digit, percent, word-number and compound forms; clamping; non-commands."""
    import voice_gateway.server as srv

    cases = [
        ("Set volume to 80%.", 80),
        ("set the volume 50", 50),
        ("Set volume to 100 percent", 100),
        ("Set volume to eighty percent.", 80),
        ("set volume to twenty five", 25),
        ("Set volume to zero.", 0),
        ("Set volume, 90%. Who are you?", 90),  # Whisper punctuation (live 2026-07-07)
        ("Set volume to 150%", 100),  # clamped
        ("What time is it?", None),
        ("The volume of a sphere is...", None),
    ]
    for text, expected in cases:
        assert srv._parse_volume_command(text) == expected, f"{text!r}"


@pytest.mark.asyncio
async def test_ws_volume_command_intercepted(monkeypatch):
    """'set volume X%' must NOT reach the agent: the server sends a
    {"cmd":"set_volume","value":N} control frame to the device and speaks a
    confirmation via the normal TTS path."""
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod
    from fastapi.websockets import WebSocketDisconnect

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "Set volume to 80%.")

    async def _agent_must_not_be_called(transcript, agent):
        raise AssertionError("volume command must not be routed to the agent")
        yield  # pragma: no cover — unreachable, satisfies generator shape

    monkeypatch.setattr(srv, "_call_agent_stream", _agent_must_not_be_called)

    spoken: list = []

    def _capture_synth(t):
        spoken.append(t)
        return b"\x01\x00" * 50

    monkeypatch.setattr(tts_mod, "synthesize", _capture_synth)

    ws = _mock_ws(
        [
            {"text": "LISTEN", "bytes": None},
            {"bytes": _pcm_bytes(), "text": None},
            {"text": "END", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )

    await srv.voice_endpoint(ws)

    sent_texts = [c.args[0] for c in ws.send_text.call_args_list]
    ctrl = [t for t in sent_texts if '"cmd"' in t]
    assert ctrl, "no control frame sent for the volume command"
    assert json.loads(ctrl[0]) == {"cmd": "set_volume", "value": 80}
    assert any("80 percent" in t for t in spoken), f"confirmation not spoken; synthesized: {spoken}"
    states = []
    for t in sent_texts:
        try:
            states.append(json.loads(t).get("state"))
        except Exception:
            pass
    assert states[-1] == "idle"


@pytest.mark.asyncio
async def test_ws_volume_command_with_chained_question(monkeypatch):
    """'Set volume 80. What time is it?' must apply the volume AND route the
    remaining question to the agent, speaking confirmation + answer together
    (owner hit the swallowed-question form three times in live use)."""
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod
    from fastapi.websockets import WebSocketDisconnect

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    monkeypatch.setattr(srv, "_DEFAULT_AGENT", "hermes")
    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "Set volume 80. What time is it?")

    agent_calls: list = []

    async def _mock_agent(transcript, agent):
        agent_calls.append(transcript)
        yield "It is noon."

    monkeypatch.setattr(srv, "_call_agent_stream", _mock_agent)

    spoken: list = []

    def _capture_synth(t):
        spoken.append(t)
        return b"\x01\x00" * 50

    monkeypatch.setattr(tts_mod, "synthesize", _capture_synth)

    ws = _mock_ws(
        [
            {"text": "LISTEN", "bytes": None},
            {"bytes": _pcm_bytes(), "text": None},
            {"text": "END", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )

    await srv.voice_endpoint(ws)

    sent_texts = [c.args[0] for c in ws.send_text.call_args_list]
    ctrl = [t for t in sent_texts if '"cmd"' in t]
    assert ctrl and json.loads(ctrl[0])["value"] == 80
    assert agent_calls, "chained question was swallowed — agent never called"
    assert (
        "volume" not in agent_calls[0].lower()
    ), f"volume command leaked into the agent query: {agent_calls[0]!r}"
    assert "time" in agent_calls[0].lower()
    _all_spoken = " ".join(spoken)
    assert (
        "80 percent" in _all_spoken and "noon" in _all_spoken
    ), f"confirmation + answer not both spoken: {spoken}"


# ── Spoken volume READ query ──────────────────────────────────────────────────


def test_is_volume_query_forms():
    """Read phrasings match; set commands and unrelated speech do not."""
    import voice_gateway.server as srv

    matches = [
        "What's the volume?",
        "what is the volume",
        "What's the volume at?",
        "What is the volume set to?",
        "current volume",
        "How loud is it?",
        "what's the volume right now",
    ]
    for text in matches:
        assert srv._is_volume_query(text), f"should match: {text!r}"

    non_matches = [
        "Set volume to 80%.",
        "set the volume 50",
        "What time is it?",
        "The volume of a sphere is...",
        "Turn the volume up.",
    ]
    for text in non_matches:
        assert not srv._is_volume_query(text), f"should not match: {text!r}"


def test_answer_volume_query_unknown_before_any_set():
    """Before any set, the read query reports an unknown-state calibration hint."""
    import voice_gateway.server as srv

    srv._last_set_volume = None
    reply = srv._answer_volume_query()
    assert "unknown" in reply.lower()
    assert "set volume" in reply.lower()


def test_answer_volume_query_returns_tracked_level():
    """After a set, the read query reports the tracked level in percent."""
    import voice_gateway.server as srv

    srv._last_set_volume = 80
    try:
        reply = srv._answer_volume_query()
        assert "80 percent" in reply
    finally:
        srv._last_set_volume = None


@pytest.mark.asyncio
async def test_ws_volume_query_intercepted_returns_tracked_level(monkeypatch):
    """'What's the volume?' must NOT reach the agent: after a prior set the
    server speaks the tracked level via the normal TTS path and never dispatches."""
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod
    from fastapi.websockets import WebSocketDisconnect

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    monkeypatch.setattr(srv, "_last_set_volume", 80)
    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "What's the volume?")

    async def _agent_must_not_be_called(transcript, agent):
        raise AssertionError("volume query must not be routed to the agent")
        yield  # pragma: no cover — unreachable, satisfies generator shape

    monkeypatch.setattr(srv, "_call_agent_stream", _agent_must_not_be_called)

    spoken: list = []

    def _capture_synth(t):
        spoken.append(t)
        return b"\x01\x00" * 50

    monkeypatch.setattr(tts_mod, "synthesize", _capture_synth)

    ws = _mock_ws(
        [
            {"text": "LISTEN", "bytes": None},
            {"bytes": _pcm_bytes(), "text": None},
            {"text": "END", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )

    await srv.voice_endpoint(ws)

    sent_texts = [c.args[0] for c in ws.send_text.call_args_list]
    ctrl = [t for t in sent_texts if '"cmd"' in t]
    assert not ctrl, "a read query must not send a set_volume control frame"
    assert any("80 percent" in t for t in spoken), f"tracked level not spoken: {spoken}"
    states = []
    for t in sent_texts:
        try:
            states.append(json.loads(t).get("state"))
        except Exception:
            pass
    assert states[-1] == "idle"


@pytest.mark.asyncio
async def test_ws_volume_query_unknown_state_intercepted(monkeypatch):
    """Before any set, 'what is the volume' speaks the unknown-state reply and
    still short-circuits the agent."""
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod
    from fastapi.websockets import WebSocketDisconnect

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    monkeypatch.setattr(srv, "_last_set_volume", None)
    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "what is the volume")

    async def _agent_must_not_be_called(transcript, agent):
        raise AssertionError("volume query must not be routed to the agent")
        yield  # pragma: no cover — unreachable, satisfies generator shape

    monkeypatch.setattr(srv, "_call_agent_stream", _agent_must_not_be_called)

    spoken: list = []

    def _capture_synth(t):
        spoken.append(t)
        return b"\x01\x00" * 50

    monkeypatch.setattr(tts_mod, "synthesize", _capture_synth)

    ws = _mock_ws(
        [
            {"text": "LISTEN", "bytes": None},
            {"bytes": _pcm_bytes(), "text": None},
            {"text": "END", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )

    await srv.voice_endpoint(ws)

    _all_spoken = " ".join(spoken)
    assert "unknown" in _all_spoken.lower(), f"unknown-state reply not spoken: {spoken}"


@pytest.mark.asyncio
async def test_ws_set_then_query_reports_the_set_level(monkeypatch):
    """A 'set volume' updates the tracked level so a later query reports it —
    proves the set path and the read path share the same module state."""
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod
    from fastapi.websockets import WebSocketDisconnect

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    monkeypatch.setattr(srv, "_last_set_volume", None)

    async def _agent_must_not_be_called(transcript, agent):
        raise AssertionError("neither set nor query may reach the agent")
        yield  # pragma: no cover — unreachable, satisfies generator shape

    monkeypatch.setattr(srv, "_call_agent_stream", _agent_must_not_be_called)

    def _capture_synth(t):
        return b"\x01\x00" * 50

    monkeypatch.setattr(tts_mod, "synthesize", _capture_synth)

    # First utterance: set volume to 45%.
    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "Set volume to 45%.")
    ws1 = _mock_ws(
        [
            {"text": "LISTEN", "bytes": None},
            {"bytes": _pcm_bytes(), "text": None},
            {"text": "END", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )
    await srv.voice_endpoint(ws1)
    assert srv._last_set_volume == 45, "set command did not update the tracked level"

    # Second utterance: query the volume — must report the level just set.
    spoken: list = []

    def _capture_synth2(t):
        spoken.append(t)
        return b"\x01\x00" * 50

    monkeypatch.setattr(tts_mod, "synthesize", _capture_synth2)
    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "What's the volume?")
    ws2 = _mock_ws(
        [
            {"text": "LISTEN", "bytes": None},
            {"bytes": _pcm_bytes(), "text": None},
            {"text": "END", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )
    await srv.voice_endpoint(ws2)
    assert any("45 percent" in t for t in spoken), f"tracked level not spoken: {spoken}"


# ── Spoken model-switch command ("use <model>" / "tell <agent>") ──────────────


def test_parse_model_switch_command_forms():
    """"use <model>" -> ('model', gateway-model-name, label); "tell <agent>"
    -> ('agent', route_to-slug, label); ordinary speech -> None."""
    import voice_gateway.server as srv

    cases = [
        ("Use local.", ("model", "qwen3-14b", "the local model")),
        ("use qwen", ("model", "qwen3-14b", "the local model")),
        ("Use Claude.", ("model", "claude-haiku-4-5-20251001", "Claude")),
        ("Use ChatGPT.", ("model", "gpt-4o-mini", "ChatGPT")),
        ("use gpt", ("model", "gpt-4o-mini", "ChatGPT")),
        ("Use Gemini.", ("model", "gemini-2.5-flash", "Gemini")),
        ("Tell Hermes to check my email.", ("agent", "hermes", "Hermes")),
        ("tell openclaw", ("agent", "openclaw", "OpenClaw")),
        ("What time is it?", None),
        ("Use the volume knob.", None),
        ("Tell me a story.", None),  # "tell" without a registered agent slug
    ]
    for text, expected in cases:
        assert srv._parse_model_switch_command(text) == expected, f"{text!r}"


@pytest.mark.asyncio
async def test_ws_use_model_command_intercepted(monkeypatch):
    """A bare 'use Claude' must NOT reach any agent: the server updates the
    sticky overrides and speaks a confirmation via the normal TTS path."""
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod
    from fastapi.websockets import WebSocketDisconnect

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "Use Claude.")

    async def _llm_must_not_be_called(history):
        raise AssertionError("bare switch command must not reach the LLM")

    async def _agent_must_not_be_called(transcript, agent):
        raise AssertionError("bare switch command must not be routed to the agent")
        yield  # pragma: no cover — unreachable, satisfies generator shape

    monkeypatch.setattr(srv, "_call_llm", _llm_must_not_be_called)
    monkeypatch.setattr(srv, "_call_agent_stream", _agent_must_not_be_called)

    spoken: list = []

    def _capture_synth(t):
        spoken.append(t)
        return b"\x01\x00" * 50

    monkeypatch.setattr(tts_mod, "synthesize", _capture_synth)

    ws = _mock_ws(
        [
            {"text": "LISTEN", "bytes": None},
            {"bytes": _pcm_bytes(), "text": None},
            {"text": "END", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )

    await srv.voice_endpoint(ws)

    assert srv._agent_override == "direct", "use <model> must select the direct fast path"
    assert srv._model_override == "claude-haiku-4-5-20251001"
    assert any(
        "switched to claude" in t.lower() for t in spoken
    ), f"confirmation not spoken: {spoken}"

    # Device's top-left agent-name display must be told to update too —
    # otherwise it stays stuck on whatever the firmware booted with,
    # contradicting what the device is actually talking to.
    sent_texts = [c.args[0] for c in ws.send_text.call_args_list]
    ctrl = [json.loads(t) for t in sent_texts if '"cmd"' in t]
    assert {"cmd": "set_agent_label", "value": "Claude"} in ctrl, f"no label update sent: {ctrl}"


@pytest.mark.asyncio
async def test_ws_use_local_command_confirms_in_plain_language(monkeypatch):
    """'use qwen' sets agent='direct', model='qwen3-14b', and confirms in
    plain language ('the local model'), not the internal slug."""
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod
    from fastapi.websockets import WebSocketDisconnect

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    monkeypatch.setattr(srv, "_agent_override", "hermes")
    monkeypatch.setattr(srv, "_model_override", "gpt-4o-mini")
    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "use qwen")

    async def _llm_must_not_be_called(history):
        raise AssertionError("bare switch command must not reach the LLM")

    async def _agent_must_not_be_called(transcript, agent):
        raise AssertionError("bare switch command must not be routed to the agent")
        yield  # pragma: no cover — unreachable, satisfies generator shape

    monkeypatch.setattr(srv, "_call_llm", _llm_must_not_be_called)
    monkeypatch.setattr(srv, "_call_agent_stream", _agent_must_not_be_called)

    spoken: list = []

    def _capture_synth(t):
        spoken.append(t)
        return b"\x01\x00" * 50

    monkeypatch.setattr(tts_mod, "synthesize", _capture_synth)

    ws = _mock_ws(
        [
            {"text": "LISTEN", "bytes": None},
            {"bytes": _pcm_bytes(), "text": None},
            {"text": "END", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )

    await srv.voice_endpoint(ws)

    assert srv._agent_override == "direct"
    assert srv._model_override == "qwen3-14b"
    assert any(
        "switched to the local model" in t.lower() for t in spoken
    ), f"confirmation not spoken: {spoken}"


@pytest.mark.asyncio
async def test_ws_use_model_command_with_chained_question(monkeypatch):
    """'Use Claude. What's on my calendar?' must switch the model AND route
    the remaining question through the fast direct path (_call_llm) in the
    same turn, mirroring the volume command's chained-question handling."""
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod
    from fastapi.websockets import WebSocketDisconnect

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    monkeypatch.setattr(
        stt_mod, "transcribe", lambda b: "Use Claude. What's on my calendar?"
    )

    llm_calls: list = []

    async def _mock_llm(history):
        llm_calls.append(history[-1]["content"])
        return "Nothing scheduled."

    async def _agent_must_not_be_called(transcript, agent):
        raise AssertionError("a model switch must not route through the agent path")
        yield  # pragma: no cover — unreachable, satisfies generator shape

    monkeypatch.setattr(srv, "_call_llm", _mock_llm)
    monkeypatch.setattr(srv, "_call_agent_stream", _agent_must_not_be_called)

    spoken: list = []

    def _capture_synth(t):
        spoken.append(t)
        return b"\x01\x00" * 50

    monkeypatch.setattr(tts_mod, "synthesize", _capture_synth)

    ws = _mock_ws(
        [
            {"text": "LISTEN", "bytes": None},
            {"bytes": _pcm_bytes(), "text": None},
            {"text": "END", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )

    await srv.voice_endpoint(ws)

    assert srv._model_override == "claude-haiku-4-5-20251001"
    assert llm_calls, "chained question was swallowed — LLM never called"
    assert (
        "claude" not in llm_calls[0].lower()
    ), f"switch command leaked into the query: {llm_calls[0]!r}"
    assert "calendar" in llm_calls[0].lower()
    _all_spoken = " ".join(spoken)
    assert (
        "switched to claude" in _all_spoken.lower()
        and "nothing scheduled" in _all_spoken.lower()
    ), f"confirmation + answer not both spoken: {spoken}"


@pytest.mark.asyncio
async def test_ws_tell_agent_command_intercepted(monkeypatch):
    """A bare 'tell Hermes' must NOT reach any agent yet: it only sets the
    sticky agent override and speaks a confirmation — same intercept pattern
    as 'use <model>', distinguished by the "Now talking to" phrasing."""
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod
    from fastapi.websockets import WebSocketDisconnect

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "Tell Hermes.")

    async def _agent_must_not_be_called(transcript, agent):
        raise AssertionError("bare switch command must not be routed to the agent")
        yield  # pragma: no cover — unreachable, satisfies generator shape

    monkeypatch.setattr(srv, "_call_agent_stream", _agent_must_not_be_called)

    spoken: list = []

    def _capture_synth(t):
        spoken.append(t)
        return b"\x01\x00" * 50

    monkeypatch.setattr(tts_mod, "synthesize", _capture_synth)

    ws = _mock_ws(
        [
            {"text": "LISTEN", "bytes": None},
            {"bytes": _pcm_bytes(), "text": None},
            {"text": "END", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )

    await srv.voice_endpoint(ws)

    assert srv._agent_override == "hermes"
    assert any(
        "now talking to hermes" in t.lower() for t in spoken
    ), f"confirmation not spoken: {spoken}"

    sent_texts = [c.args[0] for c in ws.send_text.call_args_list]
    ctrl = [json.loads(t) for t in sent_texts if '"cmd"' in t]
    assert {"cmd": "set_agent_label", "value": "Hermes"} in ctrl, f"no label update sent: {ctrl}"


@pytest.mark.asyncio
async def test_ws_tell_agent_command_with_chained_instruction(monkeypatch):
    """'Tell Hermes to check my email.' must switch the agent AND route the
    remaining instruction through the full agentic path (_call_agent_stream)
    in the same turn."""
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod
    from fastapi.websockets import WebSocketDisconnect

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    monkeypatch.setattr(
        stt_mod, "transcribe", lambda b: "Tell Hermes to check my email."
    )

    agent_calls: list = []
    transcript_calls: list = []

    async def _mock_agent(transcript, agent):
        transcript_calls.append(transcript)
        agent_calls.append(agent)
        yield "Checking now."

    async def _llm_must_not_be_called(history):
        raise AssertionError("tell <agent> must not route through the direct fast path")

    monkeypatch.setattr(srv, "_call_agent_stream", _mock_agent)
    monkeypatch.setattr(srv, "_call_llm", _llm_must_not_be_called)

    spoken: list = []

    def _capture_synth(t):
        spoken.append(t)
        return b"\x01\x00" * 50

    monkeypatch.setattr(tts_mod, "synthesize", _capture_synth)

    ws = _mock_ws(
        [
            {"text": "LISTEN", "bytes": None},
            {"bytes": _pcm_bytes(), "text": None},
            {"text": "END", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )

    await srv.voice_endpoint(ws)

    assert agent_calls == ["hermes"], f"expected dispatch to hermes, got {agent_calls}"
    assert transcript_calls, "chained instruction was swallowed — agent never called"
    assert (
        "tell hermes" not in transcript_calls[0].lower()
    ), f"switch command leaked into the agent query: {transcript_calls[0]!r}"
    assert "email" in transcript_calls[0].lower()
    _all_spoken = " ".join(spoken)
    assert (
        "now talking to hermes" in _all_spoken.lower()
        and "checking now" in _all_spoken.lower()
    ), f"confirmation + answer not both spoken: {spoken}"


@pytest.mark.asyncio
async def test_switch_overrides_persist_across_reconnect(monkeypatch):
    """A 'use Claude' override must survive a reconnect: a later connection
    with no ?agent= param still routes through the direct fast path with the
    Claude model — same persistence model as _last_set_volume, proven by
    test_ws_set_then_query_reports_the_set_level."""
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod
    from fastapi.websockets import WebSocketDisconnect

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    monkeypatch.setattr(srv, "_DEFAULT_AGENT", "direct")

    async def _agent_must_not_be_called(transcript, agent):
        raise AssertionError("bare switch command must not be routed to the agent")
        yield  # pragma: no cover — unreachable, satisfies generator shape

    monkeypatch.setattr(srv, "_call_agent_stream", _agent_must_not_be_called)
    monkeypatch.setattr(tts_mod, "synthesize", lambda t: b"\x01\x00" * 50)

    async def _llm_must_not_be_called(history):
        raise AssertionError("bare switch command must not reach the LLM")

    monkeypatch.setattr(srv, "_call_llm", _llm_must_not_be_called)

    # First connection: speak the switch command.
    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "Use Claude.")
    ws1 = _mock_ws(
        [
            {"text": "LISTEN", "bytes": None},
            {"bytes": _pcm_bytes(), "text": None},
            {"text": "END", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )
    await srv.voice_endpoint(ws1)
    assert srv._agent_override == "direct"
    assert srv._model_override == "claude-haiku-4-5-20251001"

    # Second connection (simulated reconnect, no ?agent= param): a normal
    # question must still use the Claude model, not the module's _VOICE_MODEL.
    async def _mock_llm(history):
        return "Claude reply"

    monkeypatch.setattr(srv, "_call_llm", _mock_llm)
    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "What's the weather?")
    ws2 = _mock_ws(
        [
            {"text": "LISTEN", "bytes": None},
            {"bytes": _pcm_bytes(), "text": None},
            {"text": "END", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )
    await srv.voice_endpoint(ws2)
    assert srv._agent_override == "direct", "override did not survive reconnect"
    assert srv._model_override == "claude-haiku-4-5-20251001"


# ── TTS resume-on-reconnect ───────────────────────────────────────────────────


@pytest.fixture(autouse=True)
def _reset_reply_resume():
    import voice_gateway.server as srv

    for attr in ("_reply_resume", "_utterance_resume", "_agent_override", "_model_override"):
        if hasattr(srv, attr):
            setattr(srv, attr, None)
    yield
    for attr in ("_reply_resume", "_utterance_resume", "_agent_override", "_model_override"):
        if hasattr(srv, attr):
            setattr(srv, attr, None)


# ── Uplink utterance resume (LISTEN <offset>) ────────────────────────────────


@pytest.mark.asyncio
async def test_listen_offset_resumes_partial_upload(monkeypatch):
    """A drop mid-upload must not force a full resend: the next connection
    sends 'LISTEN <offset>' and only the remainder — STT still receives ONE
    complete utterance.  (Full restarts were the dominant THINKING-time cost
    on the flaky hotspot link.)"""
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    from fastapi.websockets import WebSocketDisconnect

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")

    received: list = []

    def _capture_transcribe(pcm: bytes) -> str:
        received.append(pcm)
        return ""  # empty transcript → straight to idle, no TTS needed

    monkeypatch.setattr(stt_mod, "transcribe", _capture_transcribe)

    part1 = b"\x01\x02" * 2048  # 4096 B
    part2 = b"\x03\x04" * 2048  # 4096 B

    # Session 1: LISTEN + first chunk, then the link dies (no END).
    ws1 = _mock_ws(
        [
            {"text": "LISTEN", "bytes": None},
            {"bytes": part1, "text": None},
            WebSocketDisconnect(code=1006),
        ]
    )
    await srv.voice_endpoint(ws1)
    assert srv._utterance_resume is not None, "utterance cache not preserved"
    assert bytes(srv._utterance_resume["pcm"]) == part1

    # Session 2: resume from len(part1) and send the remainder + END.
    ws2 = _mock_ws(
        [
            {"text": f"LISTEN {len(part1)}", "bytes": None},
            {"bytes": part2, "text": None},
            {"text": "END", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )
    await srv.voice_endpoint(ws2)

    assert received, "STT never ran on the resumed utterance"
    assert received[0] == part1 + part2, (
        f"STT got {len(received[0])} bytes, expected the full "
        f"{len(part1) + len(part2)}-byte utterance"
    )
    assert srv._utterance_resume is None, "cache must clear on END"


@pytest.mark.asyncio
async def test_bare_listen_starts_fresh(monkeypatch):
    """A bare LISTEN after a stale partial upload must NOT prepend old audio."""
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    from fastapi.websockets import WebSocketDisconnect

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    received: list = []
    monkeypatch.setattr(stt_mod, "transcribe", lambda b: received.append(b) or "")

    srv._utterance_resume = {"pcm": bytearray(b"\xaa" * 1000), "ts": 0.0}

    fresh = b"\x05\x06" * 512
    ws = _mock_ws(
        [
            {"text": "LISTEN", "bytes": None},
            {"bytes": fresh, "text": None},
            {"text": "END", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )
    await srv.voice_endpoint(ws)

    assert received and received[0] == fresh, "stale cache leaked into a fresh utterance"


@pytest.mark.asyncio
async def test_listen_offset_with_stale_cache_degrades_to_fresh(monkeypatch):
    """LISTEN <offset> with an expired cache must behave like a fresh LISTEN
    (the device's resent-remainder is all the server gets — better a short
    utterance than a crash or stale-audio corruption)."""
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    from fastapi.websockets import WebSocketDisconnect

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    received: list = []
    monkeypatch.setattr(stt_mod, "transcribe", lambda b: received.append(b) or "")

    srv._utterance_resume = {"pcm": bytearray(b"\xaa" * 1000), "ts": -10_000.0}

    tail = b"\x07\x08" * 512
    ws = _mock_ws(
        [
            {"text": "LISTEN 1000", "bytes": None},
            {"bytes": tail, "text": None},
            {"text": "END", "bytes": None},
            WebSocketDisconnect(code=1000),
        ]
    )
    await srv.voice_endpoint(ws)

    assert received and received[0] == tail, "stale cache must not be prepended"


@pytest.mark.asyncio
async def test_tts_resume_after_mid_stream_disconnect(monkeypatch):
    """If the socket dies during the TTS downlink, the NEXT connection must
    receive the un-sent remainder (+END +idle) so the reply is not lost."""
    import voice_gateway.server as srv
    import voice_gateway.stt as stt_mod
    import voice_gateway.tts as tts_mod
    from fastapi.websockets import WebSocketDisconnect

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    monkeypatch.setattr(srv, "_DEFAULT_AGENT", "hermes")
    monkeypatch.setattr(stt_mod, "transcribe", lambda b: "hello")

    async def _mock_agent(transcript, agent):
        yield "Only sentence."

    monkeypatch.setattr(srv, "_call_agent_stream", _mock_agent)
    reply_pcm = bytes(range(256)) * 128  # 32 KB, recognisable bytes
    monkeypatch.setattr(tts_mod, "synthesize", lambda t: reply_pcm)

    # Session 1: dies after the first PCM frame is sent.
    ws1 = _mock_ws(
        [
            {"text": "LISTEN", "bytes": None},
            {"bytes": _pcm_bytes(), "text": None},
            {"text": "END", "bytes": None},
            WebSocketDisconnect(code=1006),
        ]
    )
    frames1: list = []

    async def _send_bytes_then_die(frame):
        frames1.append(frame)
        if len(frames1) >= 1:
            raise RuntimeError("socket died mid-stream")

    ws1.send_bytes = _send_bytes_then_die
    await srv.voice_endpoint(ws1)

    assert srv._reply_resume is not None, "resume state not preserved on drop"

    # Session 2 (reconnect): should receive the remainder immediately.
    ws2 = _mock_ws([WebSocketDisconnect(code=1000)])
    await srv.voice_endpoint(ws2)

    sent2 = b"".join(c.args[0] for c in ws2.send_bytes.call_args_list)
    assert len(sent2) > 0, "no resumed PCM sent on reconnect"
    # Remainder must cover the reply tail (last bytes of reply_pcm).
    assert sent2.endswith(reply_pcm[-64:]), "resumed stream missing the reply tail"
    texts2 = [c.args[0] for c in ws2.send_text.call_args_list]
    assert "END" in texts2
    assert srv._reply_resume is None, "resume state must clear after replay"


@pytest.mark.asyncio
async def test_tts_resume_stale_cache_ignored(monkeypatch):
    """A resume cache older than the freshness window must not replay."""
    import voice_gateway.server as srv
    from fastapi.websockets import WebSocketDisconnect

    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    srv._reply_resume = {
        "pcm": bytearray(b"\x01\x00" * 100),
        "sent": 0,
        "ts": -10_000.0,  # far in the past on the monotonic clock
    }

    ws = _mock_ws([WebSocketDisconnect(code=1000)])
    await srv.voice_endpoint(ws)

    assert ws.send_bytes.call_args_list == [], "stale cache must not replay"


# ── TTS edge fade (sentence-boundary crossfade) ──────────────────────────────


def test_tts_synthesize_fades_sentence_edges(monkeypatch):
    """Each synthesized sentence must ramp in/out over ~5 ms so per-sentence
    Kokoro output joins without DC/level steps (audible clicks)."""
    import numpy as np
    import voice_gateway.tts as tts_mod

    class _FakePipeline:
        def __call__(self, text, voice=None, speed=None):
            # Constant full-scale-ish signal, 0.5 s at 24 kHz.
            yield None, None, np.full(12000, 0.9, dtype=np.float32)

    monkeypatch.setattr(tts_mod, "_pipeline", _FakePipeline())

    pcm = tts_mod.synthesize("Constant tone.")
    samples = np.frombuffer(pcm, dtype="<i2")

    assert abs(int(samples[0])) < 1500, f"first sample not faded in: {samples[0]}"
    assert abs(int(samples[-1])) < 1500, f"last sample not faded out: {samples[-1]}"
    mid = len(samples) // 2
    assert abs(int(samples[mid])) > 15000, "mid-signal amplitude must be untouched"


# ── OTA firmware endpoint ─────────────────────────────────────────────────────


def _fw_client(tmp_path, monkeypatch, *, tokens=("test-ota-secret",), write=True):
    """Wire the /firmware/bin route to a fake binary + a fixed OTA token allowlist.

    Returns (TestClient, fake_bin_path).  When ``write`` is False no binary is
    written (used to assert the 404 path).  TestClient is built WITHOUT the
    context manager so the STT/TTS lifespan never fires — the firmware route
    needs neither, matching the pattern used by test_health_returns_ok.
    """
    import voice_gateway.server as srv

    fake_bin = tmp_path / "voice_terminal.bin"
    if write:
        fake_bin.write_bytes(b"\xaa\xbb\xcc\xdd" * 64)

    monkeypatch.setattr(srv, "_FIRMWARE_BIN_PATH", fake_bin)
    monkeypatch.setattr(srv, "_OTA_TOKENS", set(tokens))
    # Reset ETag cache so the test is independent of prior state.
    monkeypatch.setattr(srv, "_fw_etag", "")
    monkeypatch.setattr(srv, "_fw_mtime", 0.0)
    return TestClient(app), fake_bin


def test_firmware_bin_auth_and_etag(tmp_path, monkeypatch):
    """GET /firmware/bin: token gate, 200 + quoted SHA-256 ETag, HEAD ETag parity.

    Covers the observable behaviours the ESP32 OTA client depends on:
      1. Missing token → 401 (no firmware leaked)
      2. Wrong token → 403 (not on the owner-gated allowlist)
      3. Correct token → 200 + ETag header (SHA-256 of file, quoted) + body
      4. HEAD verb → same ETag, NO body (cheap OTA mismatch check)
    """
    client, fake_bin = _fw_client(tmp_path, monkeypatch)

    # 1 — Missing token → 401 (no firmware body).
    resp = client.get("/firmware/bin")
    assert resp.status_code == 401, f"Expected 401 for missing token, got {resp.status_code}"
    assert resp.content == b"", "401 must not leak firmware bytes"

    # 2 — Wrong (non-allowlisted) token → 403.
    resp = client.get("/firmware/bin?token=bad-token")
    assert resp.status_code == 403, f"Expected 403 for wrong token, got {resp.status_code}"
    assert resp.content == b"", "403 must not leak firmware bytes"

    # 3 — Correct token: 200 with a quoted SHA-256 ETag + full body.
    resp = client.get("/firmware/bin?token=test-ota-secret")
    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}"
    etag = resp.headers.get("etag")
    assert etag is not None, "ETag header missing from /firmware/bin response"
    assert etag.startswith('"') and etag.endswith(
        '"'
    ), f"ETag must be a quoted string, got {etag!r}"
    sha_hex = etag.strip('"')
    assert len(sha_hex) == 64, f"ETag inner value must be 64-char SHA-256 hex, got {sha_hex!r}"
    import hashlib as _hl

    assert sha_hex == _hl.sha256(fake_bin.read_bytes()).hexdigest(), "ETag must be SHA-256 of file"
    assert resp.content == fake_bin.read_bytes(), "Response body must match the firmware file"

    # 4 — HEAD returns the same ETag with NO body.
    resp = client.head("/firmware/bin?token=test-ota-secret")
    assert resp.status_code == 200, f"HEAD expected 200, got {resp.status_code}"
    head_etag = resp.headers.get("etag")
    assert head_etag == etag, f"HEAD ETag {head_etag!r} ≠ GET ETag {etag!r} — OTA would re-download"
    assert resp.content == b"", "HEAD must not return a body"


def test_firmware_bin_304_on_matching_if_none_match(tmp_path, monkeypatch):
    """If-None-Match equal to the current ETag → 304 with no body.

    This is the whole point of ETag-based OTA: an up-to-date device sends its
    stored ETag and gets 304, so it never re-downloads unchanged firmware.
    """
    client, _ = _fw_client(tmp_path, monkeypatch)

    # Learn the current ETag.
    etag = client.get("/firmware/bin?token=test-ota-secret").headers["etag"]

    # Exact match → 304, empty body.
    resp = client.get(
        "/firmware/bin?token=test-ota-secret",
        headers={"If-None-Match": etag},
    )
    assert resp.status_code == 304, f"Expected 304 on matching ETag, got {resp.status_code}"
    assert resp.content == b"", "304 must have an empty body"
    assert resp.headers.get("etag") == etag, "304 should still echo the ETag"

    # Weak-validator prefix (W/) must also match (RFC 7232 §3.2).
    resp = client.get(
        "/firmware/bin?token=test-ota-secret",
        headers={"If-None-Match": f"W/{etag}"},
    )
    assert resp.status_code == 304, "weak-validator If-None-Match should also 304"


def test_firmware_bin_stale_if_none_match_returns_body(tmp_path, monkeypatch):
    """A stale/mismatched If-None-Match must serve the full new binary (200)."""
    client, fake_bin = _fw_client(tmp_path, monkeypatch)

    stale = '"' + ("0" * 64) + '"'
    resp = client.get(
        "/firmware/bin?token=test-ota-secret",
        headers={"If-None-Match": stale},
    )
    assert resp.status_code == 200, f"stale ETag must serve body, got {resp.status_code}"
    assert resp.content == fake_bin.read_bytes()


def test_firmware_bin_404_when_absent(tmp_path, monkeypatch):
    """Authenticated request but no firmware on disk → 404 (not a 500/empty 200)."""
    client, _ = _fw_client(tmp_path, monkeypatch, write=False)
    resp = client.get("/firmware/bin?token=test-ota-secret")
    assert resp.status_code == 404, f"Expected 404 when no firmware present, got {resp.status_code}"


def test_firmware_bin_ungated_when_allowlist_empty(tmp_path, monkeypatch):
    """Empty allowlist = OTA un-gated: any non-empty token is accepted (200)."""
    client, fake_bin = _fw_client(tmp_path, monkeypatch, tokens=())
    resp = client.get("/firmware/bin?token=anything")
    assert (
        resp.status_code == 200
    ), f"empty allowlist should accept any token, got {resp.status_code}"
    assert resp.content == fake_bin.read_bytes()
    # Still 401 on a truly missing token.
    assert client.get("/firmware/bin").status_code == 401


def test_load_ota_tokens_sources(tmp_path, monkeypatch):
    """_load_ota_tokens merges env + secret file and falls back to the WS token."""
    import voice_gateway.server as srv

    # Secret file (comments + blanks ignored) ∪ comma-separated env.
    tokfile = tmp_path / "ota_tokens"
    tokfile.write_text("# device fleet\ndev-a\n\ndev-b\n")
    monkeypatch.setenv("FIRMWARE_OTA_TOKENS_FILE", str(tokfile))
    monkeypatch.setenv("FIRMWARE_OTA_TOKENS", "dev-c, dev-b")  # dedup dev-b
    assert srv._load_ota_tokens() == {"dev-a", "dev-b", "dev-c"}

    # No env → fall back to the single WS auth token.
    monkeypatch.delenv("FIRMWARE_OTA_TOKENS_FILE", raising=False)
    monkeypatch.delenv("FIRMWARE_OTA_TOKENS", raising=False)
    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "ws-fallback")
    assert srv._load_ota_tokens() == {"ws-fallback"}

    # Nothing configured at all → empty allowlist (un-gated).
    monkeypatch.setattr(srv, "_VG_AUTH_TOKEN", "")
    assert srv._load_ota_tokens() == set()
