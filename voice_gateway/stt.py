# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Speech-to-Text using faster-whisper (local CPU inference)."""

from __future__ import annotations

import logging
import os
import struct

logger = logging.getLogger("voice_gateway.stt")

# Lazy-loaded to avoid slow import at startup
_model = None
_MODEL_SIZE = os.environ.get("WHISPER_MODEL_SIZE", "small.en")

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
        _model = WhisperModel(
            _MODEL_PATH, device="cpu", compute_type="int8", cpu_threads=2
        )
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
        raise RuntimeError(
            "numpy is required for STT; install voice_gateway dependencies"
        )

    num_samples = len(pcm_bytes) // 2
    samples = struct.unpack(f"<{num_samples}h", pcm_bytes)
    audio = np.array(samples, dtype=np.float32) / 32768.0

    model = _get_model()
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
    logger.debug("STT result: %r", text)
    return text


def reset_model() -> None:
    """Release the loaded model (for testing / memory pressure)."""
    global _model
    _model = None
