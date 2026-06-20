# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Text-to-Speech using Piper (local CPU inference, outputs S16LE PCM)."""

from __future__ import annotations

import io
import logging
import subprocess
import tempfile
import wave
from pathlib import Path
from typing import Optional

logger = logging.getLogger("voice_gateway.tts")

# Path to the piper binary and voice model; override via env vars.
import os as _os

_PIPER_BIN = _os.environ.get("PIPER_BIN", "piper")
_PIPER_MODEL = _os.environ.get("PIPER_MODEL", "/opt/piper/en_US-lessac-medium.onnx")

# Output sample rate Piper uses for lessac-medium model
OUTPUT_SAMPLE_RATE = 22050


def synthesize(text: str) -> bytes:
    """Synthesize *text* to raw S16LE PCM mono audio bytes.

    Piper is invoked as a subprocess; its stdout is a WAV file from which we
    strip the header and return the raw PCM payload.

    Args:
        text: The text to speak.

    Returns:
        Raw S16LE PCM bytes at OUTPUT_SAMPLE_RATE Hz, mono.

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
    logger.debug("TTS produced %d PCM bytes for %d-char input", len(pcm), len(text))
    return pcm
