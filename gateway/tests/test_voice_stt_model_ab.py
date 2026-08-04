# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""SCRUM-57 — STT model A/B (Whisper small.en ↔ base.en).

Covers the config-driven Whisper model selection + measurement harness added to
the voice STT path:

  (1) SELECT   — select_model_size: a pure function that validates a requested
      Whisper model size against the known-good set, falling back to the default
      (unchanged behaviour) when the request is unset/blank/invalid.
  (2) MEASURE  — record_transcription_latency: emits a structured per-transcription
      latency record tagged with the model size so an operator can A/B small.en
      vs base.en straight from the logs (reuses the module logger — no new
      telemetry stack).  Pure + injectable — no real model, no real audio.

All I/O is mocked — no real Whisper model, no real audio, no network, no sleep.
"""

from __future__ import annotations

import logging
import struct
from unittest.mock import MagicMock

import pytest
import voice_gateway.stt as stt

# ── (1) SELECT: select_model_size ─────────────────────────────────────────────


def test_select_model_size_default_when_unset():
    """No requested value → the default is used (behaviour unchanged)."""
    assert stt.select_model_size(None, default="small.en") == "small.en"
    assert stt.select_model_size("", default="small.en") == "small.en"
    assert stt.select_model_size("   ", default="small.en") == "small.en"


def test_select_model_size_env_override_selects_configured_model():
    """A valid requested value overrides the default (the A/B knob)."""
    assert stt.select_model_size("base.en", default="small.en") == "base.en"
    assert stt.select_model_size("tiny.en", default="small.en") == "tiny.en"
    assert stt.select_model_size("medium.en", default="small.en") == "medium.en"


def test_select_model_size_is_case_and_whitespace_insensitive():
    """Operator-friendly: trims + lowercases before matching."""
    assert stt.select_model_size("  BASE.EN ", default="small.en") == "base.en"


def test_select_model_size_invalid_falls_back_to_default():
    """An unknown model size does NOT crash — it falls back to the default."""
    assert stt.select_model_size("gpt-5", default="small.en") == "small.en"
    assert stt.select_model_size("large-v3", default="base.en") == "base.en"


def test_select_model_size_invalid_logs_warning(caplog):
    """The fallback is visible to operators (WARNING, not silent)."""
    with caplog.at_level(logging.WARNING, logger="voice_gateway.stt"):
        out = stt.select_model_size("bogus", default="small.en")
    assert out == "small.en"
    assert any("bogus" in r.message for r in caplog.records)


def test_valid_model_sizes_contains_documented_ab_set():
    """The documented A/B knob values are all accepted."""
    for size in ("tiny.en", "base.en", "small.en", "medium.en"):
        assert size in stt.VALID_MODEL_SIZES


# ── (2) MEASURE: record_transcription_latency ─────────────────────────────────


def test_record_transcription_latency_returns_structured_record():
    """The helper returns a record tagged with model size + duration."""
    rec = stt.record_transcription_latency(
        model_size="base.en", duration_s=0.842, audio_seconds=3.0
    )
    assert rec["event"] == "stt_transcription_latency"
    assert rec["model_size"] == "base.en"
    assert rec["duration_s"] == 0.842
    assert rec["audio_seconds"] == 3.0
    # Real-time factor = wall time / audio duration (data-driven A/B metric),
    # rounded to 4 decimals for stable log-friendly records.
    assert rec["rtf"] == pytest.approx(0.842 / 3.0, abs=1e-4)


def test_record_transcription_latency_rounds_duration():
    """Duration is rounded for stable, log-friendly records."""
    rec = stt.record_transcription_latency(
        model_size="small.en", duration_s=1.23456789, audio_seconds=2.0
    )
    assert rec["duration_s"] == 1.235


def test_record_transcription_latency_handles_zero_audio():
    """Zero / unknown audio length → rtf is None (no divide-by-zero)."""
    rec = stt.record_transcription_latency(model_size="small.en", duration_s=0.5, audio_seconds=0.0)
    assert rec["rtf"] is None


def test_record_transcription_latency_logs_info(caplog):
    """The record is emitted through the module logger for A/B comparison."""
    with caplog.at_level(logging.INFO, logger="voice_gateway.stt"):
        stt.record_transcription_latency(model_size="base.en", duration_s=0.9, audio_seconds=3.0)
    assert any(
        "stt_transcription_latency" in r.message and "base.en" in r.message for r in caplog.records
    )


# ── module wiring: the active model size resolves from the config knob ────────


def test_module_model_size_defaults_to_small_en(monkeypatch):
    """With WHISPER_MODEL_SIZE unset, the resolved size stays small.en."""
    monkeypatch.delenv("WHISPER_MODEL_SIZE", raising=False)
    assert stt._resolve_model_size() == "small.en"


def test_module_model_size_env_override(monkeypatch):
    """Setting WHISPER_MODEL_SIZE=base.en flips the resolved model (A/B)."""
    monkeypatch.setenv("WHISPER_MODEL_SIZE", "base.en")
    assert stt._resolve_model_size() == "base.en"


def test_module_model_size_invalid_env_falls_back(monkeypatch):
    """A garbage WHISPER_MODEL_SIZE env value does not break startup."""
    monkeypatch.setenv("WHISPER_MODEL_SIZE", "not-a-model")
    assert stt._resolve_model_size() == "small.en"


# ── wiring: transcribe() emits a latency record tagged with the model size ────


def test_transcribe_emits_latency_record(monkeypatch, caplog):
    """The A/B measurement fires on the real transcribe path (model mocked).

    Proves the model-size tag + latency record are wired into transcribe()
    without a real Whisper model or real audio.
    """
    stt.reset_model()
    monkeypatch.setattr(stt, "_MODEL_SIZE", "base.en")

    pcm = struct.pack("<h", 1200) * 16000  # 16000 samples @ 16 kHz = 1.0 s audio
    mock_seg = MagicMock()
    mock_seg.text = " hello world"
    mock_model = MagicMock()
    mock_model.transcribe = MagicMock(return_value=([mock_seg], MagicMock()))
    monkeypatch.setattr(stt, "_get_model", lambda: mock_model)

    with caplog.at_level(logging.INFO, logger="voice_gateway.stt"):
        result = stt.transcribe(pcm, sample_rate=16000)

    assert result == "hello world"
    recs = [r for r in caplog.records if "stt_transcription_latency" in r.message]
    assert recs, "transcribe() did not emit a latency record"
    assert "base.en" in recs[0].message
    # 16000 samples @ 16 kHz → 1.0 s of audio reflected in the record
    assert "audio_seconds=1.000" in recs[0].message
