# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Text-to-Speech using Piper (local CPU inference, outputs S16LE PCM)."""

from __future__ import annotations

import logging
import os as _os
import subprocess

logger = logging.getLogger("voice_gateway.tts")

# Path to the piper binary and voice model; override via env vars.
_PIPER_BIN = _os.environ.get("PIPER_BIN", "piper")
_PIPER_MODEL = _os.environ.get("PIPER_MODEL", "/opt/piper/en_US-lessac-medium.onnx")

# Native sample rate for the lessac-medium voice model.
OUTPUT_SAMPLE_RATE = 22050

# Target rate for the ESP32-S3-BOX-3 speaker.  The mic and speaker share one
# full-duplex I²S bus locked to 16 kHz (required by WakeNet).  Piper output
# is resampled to this rate before transmission so replies play at natural speed.
TARGET_SAMPLE_RATE = int(_os.environ.get("VG_OUTPUT_SAMPLE_RATE", "16000"))


def _resample_s16le_mono(pcm: bytes, src_rate: int, dst_rate: int) -> bytes:
    """Resample raw S16LE mono PCM from *src_rate* Hz to *dst_rate* Hz.

    Uses numpy linear interpolation — already a requirement for STT.  Clips
    to int16 range after resampling to avoid wrap-around artefacts.

    Args:
        pcm:      Raw S16LE mono PCM bytes at *src_rate*.
        src_rate: Source sample rate in Hz.
        dst_rate: Destination sample rate in Hz.

    Returns:
        Raw S16LE mono PCM bytes at *dst_rate*.
    """
    import numpy as _np  # lazy — same pattern as stt.py

    n_src = len(pcm) // 2
    if n_src == 0:
        return b""

    samples = _np.frombuffer(pcm, dtype="<i2").astype(_np.float32)

    # Build the output sample positions in terms of source indices.
    n_dst = int(round(n_src * dst_rate / src_rate))
    src_indices = _np.linspace(0, n_src - 1, n_dst)

    # Linear interpolation (fast, no external dep beyond numpy).
    lo = _np.floor(src_indices).astype(_np.int32)
    hi = _np.minimum(lo + 1, n_src - 1)
    frac = (src_indices - lo).astype(_np.float32)
    resampled = samples[lo] * (1.0 - frac) + samples[hi] * frac

    out = _np.clip(resampled, -32768, 32767).astype("<i2")
    return out.tobytes()


def synthesize(text: str) -> bytes:
    """Synthesize *text* to raw S16LE PCM mono audio bytes at TARGET_SAMPLE_RATE.

    Piper is invoked with ``--output_raw`` (no WAV header); its stdout is raw
    S16LE PCM at OUTPUT_SAMPLE_RATE (22050 Hz for lessac-medium).  When
    TARGET_SAMPLE_RATE differs, the output is resampled via numpy linear
    interpolation before returning so the ESP32-S3-BOX-3 speaker (locked to
    16 kHz by the WakeNet I²S bus) plays audio at the correct pitch and speed.

    Args:
        text: The text to speak.

    Returns:
        Raw S16LE PCM bytes at TARGET_SAMPLE_RATE Hz, mono.

    Raises:
        RuntimeError: If Piper returns a non-zero exit code or is not found.
    """
    if not text:
        return b""

    try:
        result = subprocess.run(
            [_PIPER_BIN, "--model", _PIPER_MODEL, "--output_raw"],
            input=text.encode(),
            capture_output=True,
            timeout=30,
        )
    except FileNotFoundError:
        raise RuntimeError(
            f"Piper binary not found at '{_PIPER_BIN}'. "
            "Set PIPER_BIN env var or install piper in the container."
        )
    except subprocess.TimeoutExpired:
        raise RuntimeError("Piper TTS timed out after 30 seconds")

    if result.returncode != 0:
        raise RuntimeError(
            f"Piper exited {result.returncode}: {result.stderr.decode(errors='replace')}"
        )

    pcm = result.stdout
    if TARGET_SAMPLE_RATE != OUTPUT_SAMPLE_RATE:
        pcm = _resample_s16le_mono(pcm, OUTPUT_SAMPLE_RATE, TARGET_SAMPLE_RATE)
        logger.debug(
            "TTS resampled %d Hz → %d Hz: %d bytes for %d-char input",
            OUTPUT_SAMPLE_RATE, TARGET_SAMPLE_RATE, len(pcm), len(text),
        )
    else:
        logger.debug(
            "TTS produced %d PCM bytes at %d Hz for %d-char input",
            len(pcm), TARGET_SAMPLE_RATE, len(text),
        )
    return pcm
