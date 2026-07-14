# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Speech-to-Text using faster-whisper (local CPU inference)."""

from __future__ import annotations

import logging
import os
import struct
import time
from typing import Dict, Optional

logger = logging.getLogger("voice_gateway.stt")

# ── Model A/B knob (SCRUM-57) ────────────────────────────────────────────────
# WHISPER_MODEL_SIZE selects the faster-whisper model.  base.en is faster but
# less accurate; small.en is the historical default (more accurate, slower).
# Kept as a config knob so the small.en↔base.en latency/accuracy tradeoff is
# measured, not guessed.  Valid values below; an unset/blank/invalid value keeps
# the default (behaviour unchanged unless the operator opts in).
DEFAULT_MODEL_SIZE = "small.en"
VALID_MODEL_SIZES = ("tiny.en", "base.en", "small.en", "medium.en")


def select_model_size(requested: Optional[str], *, default: str = DEFAULT_MODEL_SIZE) -> str:
    """Resolve a requested Whisper model size, with a safe default fallback.

    Pure function (no I/O, no env reads) so the A/B selection is unit-testable
    without a real model.  Trims + lowercases the request for operator-friendly
    matching.  An unset, blank, or unrecognised value falls back to ``default``
    and logs a WARNING — an invalid config knob never crashes STT startup.
    """
    if requested is None:
        return default
    normalized = requested.strip().lower()
    if not normalized:
        return default
    if normalized not in VALID_MODEL_SIZES:
        logger.warning(
            "WHISPER_MODEL_SIZE=%r is not one of %s — falling back to %r",
            requested,
            list(VALID_MODEL_SIZES),
            default,
        )
        return default
    return normalized


def _resolve_model_size() -> str:
    """Read WHISPER_MODEL_SIZE from the environment and validate it (A/B knob)."""
    return select_model_size(os.environ.get("WHISPER_MODEL_SIZE"))


def record_transcription_latency(
    model_size: str,
    duration_s: float,
    audio_seconds: float,
) -> Dict[str, object]:
    """Emit a structured per-transcription latency record for the STT A/B.

    Tags each transcription with the active Whisper ``model_size`` plus the
    wall-clock ``duration_s`` and the real-time factor (RTF = wall time / audio
    duration) so an operator can compare small.en vs base.en straight from the
    logs.  Reuses the module ``logger`` (no new telemetry stack).  Pure — no
    model, no audio — so it is unit-testable in isolation.  Returns the record
    dict so callers/tests can assert on it without parsing log output.
    """
    rtf: Optional[float]
    if audio_seconds > 0:
        rtf = round(duration_s / audio_seconds, 4)
    else:
        rtf = None
    record: Dict[str, object] = {
        "event": "stt_transcription_latency",
        "model_size": model_size,
        "duration_s": round(duration_s, 3),
        "audio_seconds": round(audio_seconds, 3),
        "rtf": rtf,
    }
    logger.info(
        "stt_transcription_latency model_size=%s duration_s=%.3f audio_seconds=%.3f rtf=%s",
        model_size,
        duration_s,
        audio_seconds,
        rtf,
    )
    return record


# Lazy-loaded to avoid slow import at startup
_model = None
_MODEL_SIZE = _resolve_model_size()

# In the Docker image the model is pre-baked at build time into WHISPER_MODEL_DIR
# (set by Dockerfile ENV).  Passing a local directory path to WhisperModel loads from
# disk with zero network calls — required because voice-gateway runs on
# agentshroud-isolated and all egress goes through a default-deny proxy that blocks
# huggingface.co.  Falls back to the model size string for local dev (with internet).
_MODEL_PATH = os.environ.get("WHISPER_MODEL_DIR", _MODEL_SIZE)


def _get_model():
    global _model
    if _model is None:
        from faster_whisper import WhisperModel  # type: ignore[import]

        logger.info("Loading faster-whisper model from '%s'…", _MODEL_PATH)
        _model = WhisperModel(_MODEL_PATH, device="cpu", compute_type="int8", cpu_threads=2)
        logger.info("faster-whisper model loaded")
    return _model


def transcribe(pcm_bytes: bytes, sample_rate: int = 16000) -> str:
    """Transcribe raw 16-bit signed PCM mono audio to text.

    Args:
        pcm_bytes: Raw S16LE PCM samples, 16 kHz mono.
        sample_rate: Sample rate (must match the stream; default 16000 Hz).

    Returns:
        Transcribed text, stripped. Empty string if silent/inaudible.
    """
    if not pcm_bytes:
        return ""

    # Convert S16LE bytes → float32 numpy array that faster-whisper expects
    try:
        import numpy as np  # type: ignore[import]
    except ImportError:
        raise RuntimeError("numpy is required for STT; install voice_gateway dependencies")

    num_samples = len(pcm_bytes) // 2
    samples = struct.unpack(f"<{num_samples}h", pcm_bytes)
    audio = np.array(samples, dtype=np.float32) / 32768.0
    audio_seconds = num_samples / sample_rate if sample_rate else 0.0

    model = _get_model()
    _t0 = time.perf_counter()
    segments, _ = model.transcribe(
        audio,
        beam_size=3,
        language="en",
        # Suppress hallucinated punctuation on near-silence (dots, ellipses, etc.)
        no_speech_threshold=0.6,
        condition_on_previous_text=False,
        compression_ratio_threshold=2.4,
    )
    text = " ".join(seg.text for seg in segments).strip()
    # A/B measurement: tag this transcription with the active model size + wall
    # time so small.en vs base.en can be compared from the logs (SCRUM-57).
    record_transcription_latency(_MODEL_SIZE, time.perf_counter() - _t0, audio_seconds)
    logger.debug("STT result: %r", text)
    return text


def reset_model() -> None:
    """Release the loaded model (for testing / memory pressure)."""
    global _model
    _model = None
