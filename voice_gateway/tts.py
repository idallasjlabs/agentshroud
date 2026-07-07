# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Text-to-Speech using Kokoro (local neural TTS, outputs S16LE PCM)."""

from __future__ import annotations

import logging
import os as _os
import re
from typing import Any

logger = logging.getLogger("voice_gateway.tts")

# Kokoro voice character and speed; override via env vars.
# Available voices: af_heart (warm female), af_alloy, am_adam, am_michael,
#                   bf_emma (British female), bm_george (British male)
_KOKORO_VOICE = _os.environ.get("KOKORO_VOICE", "af_heart")
_KOKORO_SPEED = float(_os.environ.get("KOKORO_SPEED", "1.0"))

# Never let Kokoro/huggingface_hub reach the network at synthesis time.  A
# voice pack missing from the baked cache otherwise triggers a download that
# hangs indefinitely behind the VPN — live incident 2026-07-03/04: the first
# synthesis with KOKORO_VOICE=af_bella (not in cache) hung forever, wedging
# the session in THINKING with the device deaf.  Offline mode turns that hang
# into an immediate exception, which synthesize() converts into a permanent
# fallback to the cached default voice.
_os.environ.setdefault("HF_HUB_OFFLINE", "1")

_FALLBACK_VOICE = "af_heart"

# Kokoro's native output sample rate.
OUTPUT_SAMPLE_RATE = 24000

# Pipeline singleton — lazy-initialised on first synthesis call.
_pipeline: Any = None


def _get_pipeline() -> Any:
    global _pipeline
    if _pipeline is None:
        from kokoro import KPipeline  # type: ignore[import]
        _pipeline = KPipeline(lang_code="a")
    return _pipeline

# Target rate for the ESP32-S3-BOX-3 speaker.  The mic and speaker share one
# full-duplex I²S bus locked to 16 kHz (required by WakeNet).  Piper output
# is resampled to this rate before transmission so replies play at natural speed.
TARGET_SAMPLE_RATE = int(_os.environ.get("VG_OUTPUT_SAMPLE_RATE", "16000"))


def _resample_s16le_mono(pcm: bytes, src_rate: int, dst_rate: int) -> bytes:
    """Resample raw S16LE mono PCM from *src_rate* Hz to *dst_rate* Hz.

    For downsampling (the 22050→16000 Hz case): applies a Kaiser-windowed sinc
    anti-aliasing filter before linear interpolation.  Pure linear interpolation
    without a low-pass filter aliases high-frequency content into the audible
    band, producing choppy / metallic artefacts on the ESP32 speaker.

    The filter kernel is a length-129 Kaiser-windowed sinc (β=8.0) with a
    normalised cutoff at dst_rate/src_rate, giving >80 dB stopband attenuation
    above the output Nyquist (8 kHz at 16 kHz playback).

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

    # Anti-aliasing: apply a Kaiser-windowed sinc low-pass filter before
    # downsampling so content above the output Nyquist doesn't fold into the
    # audible band as aliasing artefacts.
    if dst_rate < src_rate:
        cutoff = dst_rate / src_rate  # normalised cutoff in (0, 1)
        n_taps = 128  # even → kernel is n_taps+1 samples long (odd, symmetric)
        n = _np.arange(-(n_taps // 2), n_taps // 2 + 1)
        h = cutoff * _np.sinc(cutoff * n) * _np.kaiser(n_taps + 1, 8.0)
        h = h / h.sum()
        samples = _np.convolve(samples, h, mode="same")

    # Resample.  For the common Kokoro path (24000→16000 = exact 2/3 ratio) use
    # true polyphase interpolation: windowed-sinc kernel evaluated at exact
    # fractional offsets (0 and 1/2 source-sample phases after 3:2 decimation),
    # which preserves high-frequency detail that linear interpolation smears —
    # audibly crisper consonants on the ESP32 speaker ("less robotic").
    n_dst = int(round(n_src * dst_rate / src_rate))
    if src_rate == 24000 and dst_rate == 16000:
        # Output sample k lands at source position k*1.5 → phases alternate
        # 0.0, 0.5.  Phase 0.0 → copy; phase 0.5 → 8-tap windowed-sinc midpoint
        # interpolation (far better than 2-tap linear).
        pad = 4
        s = _np.concatenate([_np.zeros(pad, _np.float32), samples,
                             _np.zeros(pad + 2, _np.float32)])
        pos = _np.arange(n_dst, dtype=_np.float64) * 1.5 + pad
        base = _np.floor(pos).astype(_np.int64)
        frac = (pos - base).astype(_np.float32)          # 0.0 or 0.5 exactly
        # 8-tap Kaiser-windowed sinc for the 0.5-phase; identity for 0.0-phase.
        taps = _np.arange(-3, 5, dtype=_np.float32)      # offsets -3..4
        k05 = _np.sinc(taps - 0.5) * _np.kaiser(8, 6.0).astype(_np.float32)
        k05 = k05 / k05.sum()
        gather = s[base[:, None] + taps.astype(_np.int64)]
        interp05 = gather @ k05
        exact = s[base]
        resampled = _np.where(frac < 0.25, exact, interp05)
    else:
        # Generic fallback: linear interpolation (post anti-aliasing filter).
        src_indices = _np.linspace(0, n_src - 1, n_dst)
        lo = _np.floor(src_indices).astype(_np.int32)
        hi = _np.minimum(lo + 1, n_src - 1)
        frac = (src_indices - lo).astype(_np.float32)
        resampled = samples[lo] * (1.0 - frac) + samples[hi] * frac

    out = _np.clip(resampled, -32768, 32767).astype("<i2")
    return out.tobytes()


# ---------------------------------------------------------------------------
# Speech normalisation
# ---------------------------------------------------------------------------
# Explicit token → spoken phrase map.  Tokens are sourced from:
#   gateway/security/outbound_filter.py   (infrastructure, operational, …)
#   gateway/security/prompt_protection.py (CREDENTIAL_REDACTED, …)
#   gateway/ingest_api/sanitizer.py       (PII angle-bracket tokens, REDACTED:)
#   gateway/security/differential_pii_detector.py
# Order: most-specific first to avoid partial matches.
_TOKEN_PHRASES: list[tuple[str, str]] = [
    # ── credentials ──────────────────────────────────────────────────────
    ("[CREDENTIAL_REDACTED]", "a credential"),
    ("[CREDENTIAL_VAR]", "a credential"),
    ("[SECRET_PATH]", "a credential"),
    ("[STRUCTURE_REDACTED]", "a credential"),
    ("[INFRASTRUCTURE_REDACTED]", "a credential"),
    ("[REDACTED]", "redacted"),
    # ── infrastructure ────────────────────────────────────────────────────
    ("[INTERNAL_URL]", "an internal address"),
    ("[INTERNAL_HOST]", "an internal host"),
    ("[INTERNAL_PATH]", "an internal path"),
    ("[CONTAINER_PATH]", "an internal path"),
    ("[PRIVATE_IP]", "a private IP address"),
    ("[TAILNET]", "an internal network"),
    ("[SSH_CMD]", "a command"),
    ("[PORT]", "a port"),
    # ── identity ─────────────────────────────────────────────────────────
    ("[USER_ID_REDACTED]", "a user"),
    ("[USER_ID]", "a user"),
    ("[COLLABORATOR]", "a collaborator"),
    # ── tools / security modules ─────────────────────────────────────────
    ("[TOOL_INFO_REDACTED]", "a tool"),
    ("[TOOL]", "a tool"),
    ("[SECURITY_MODULE]", "a security module"),
    # ── operations / runtime ──────────────────────────────────────────────
    ("[RUNTIME_VERSION]", "a runtime version"),
    ("[OS_VERSION]", "an OS version"),
    ("[ARCH]", "an architecture"),
    ("[MODEL_INFO]", "a model name"),
    # ── response-level filters ────────────────────────────────────────────
    ("[REDACTED_TOOL_CALL]", "a tool call"),
    ("[RESPONSE_FILTERED]", "filtered content"),
    ("[PRIVATE_DATA]", "private data"),
]

# PII angle-bracket tokens emitted by presidio / differential_pii_detector.
_ANGLE_TOKEN_PHRASES: list[tuple[str, str]] = [
    ("<EMAIL_ADDRESS>", "an email address"),
    ("<PHONE_NUMBER>", "a phone number"),
    ("<US_SSN>", "a social security number"),
    ("<US_BANK_NUMBER>", "a bank account number"),
    ("<US_DRIVER_LICENSE>", "a driver's license number"),
    ("<US_PASSPORT>", "a passport number"),
    ("<IBAN_CODE>", "a bank account number"),
    ("<CRYPTO>", "a cryptocurrency address"),
    ("<MEDICAL_LICENSE>", "a medical license number"),
    ("<IP_ADDRESS>", "an IP address"),
    ("<DATE_TIME>", "a date"),
    ("<LOCATION>", "a location"),
    ("<PERSON>", "a person's name"),
    ("<NRP>", "a person's name"),
    ("<URL>", "a URL"),
]

# Fallback regexes for any unmapped [ALL_CAPS] / <ALL_CAPS> tokens.
# Upper-case first character prevents matching footnotes like [1] or prose like [possible].
_RE_BRACKET_FALLBACK = re.compile(r"\[[A-Z][A-Z0-9_]*\]")
# Matches <ANGLE_TOKEN> but not common HTML tags (<p>, <div>, etc.)
_RE_ANGLE_FALLBACK = re.compile(r"<[A-Z][A-Z0-9_]+>")

# Variable-content credential patterns (must be regexes).
# 🔒 [REDACTED: anything]  ← sanitizer.py:499
_RE_LOCK_REDACTED = re.compile(r"🔒 \[REDACTED:[^\]]*\]")
# <REDACTED:secret>  ← sanitizer.py:512
_RE_ANGLE_REDACTED = re.compile(r"<REDACTED:[^>]*>")

# ---------------------------------------------------------------------------
# Markdown strip patterns (applied after token replacement so [text](url)
# handling doesn't accidentally consume redaction brackets first).
# ---------------------------------------------------------------------------
_RE_CODE_FENCE = re.compile(r"```[^\n]*\n?")  # opening/closing ``` lines
_RE_INLINE_CODE = re.compile(r"`([^`\n]+)`")  # `code` → code
_RE_BOLD_DOUBLE_STAR = re.compile(r"\*\*(.*?)\*\*", re.DOTALL)
_RE_BOLD_DOUBLE_UNDER = re.compile(r"__(.*?)__", re.DOTALL)
_RE_ITALIC_STAR = re.compile(r"\*([^*\n]+)\*")
_RE_IMAGE_LINK = re.compile(r"!\[([^\]]*)\]\([^)]*\)")  # ![alt](url) → alt
_RE_LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")  # [text](url) → text
_RE_HEADING = re.compile(r"^#{1,6}\s+", re.MULTILINE)
_RE_LIST_ITEM = re.compile(r"^[ \t]*(?:[-*+]|\d+\.)\s+", re.MULTILINE)
_RE_BLOCKQUOTE = re.compile(r"^[ \t]*>\s?", re.MULTILINE)
_RE_HR = re.compile(r"^\s*(?:---+|\*\*\*+|___+)\s*$", re.MULTILINE)
_RE_WHITESPACE = re.compile(r"[ \t\n\r]+")


def normalize_for_speech(text: str) -> str:
    """Return *text* suitable for TTS synthesis on the ESP32 voice interface.

    Two transformations are applied in order:

    1. **Redaction tokens → category-aware spoken phrases.**  Tokens produced by the
       AgentShroud outbound pipeline (e.g. ``[CREDENTIAL_REDACTED]``, ``[PORT]``,
       ``<EMAIL_ADDRESS>``) are replaced with short natural-language phrases such as
       "a credential" or "a port".  Unknown ALL_CAPS bracket/angle tokens fall back
       to "redacted".  Raw secret values are never surfaced — this function only
       handles the placeholder text that the pipeline already inserted.

    2. **Markdown stripped to plain prose.**  Bold, italic, code fences, inline code,
       headings, list markers, blockquotes, horizontal rules, and markdown links are
       all removed so Piper speaks clean sentences without reading punctuation symbols.

    The raw reply is logged *before* this function is called (server.py:218/308) so
    the audit trail is unaffected.

    Args:
        text: Agent reply text, potentially containing markdown and redaction tokens.

    Returns:
        Plain-text string ready for TTS synthesis.
    """
    # ── Phase 1: redaction token → spoken phrase ─────────────────────────────

    # Variable-content patterns first (regex, before literal replacements).
    text = _RE_LOCK_REDACTED.sub("a credential", text)
    text = _RE_ANGLE_REDACTED.sub("a credential", text)

    # Explicit token literals (longest / most-specific first).
    for token, phrase in _TOKEN_PHRASES:
        text = text.replace(token, phrase)
    for token, phrase in _ANGLE_TOKEN_PHRASES:
        text = text.replace(token, phrase)

    # Fallback: any remaining [ALL_CAPS] or <ALL_CAPS> token.
    text = _RE_BRACKET_FALLBACK.sub("redacted", text)
    text = _RE_ANGLE_FALLBACK.sub("redacted", text)

    # ── Phase 2: markdown → plain prose ──────────────────────────────────────

    text = _RE_CODE_FENCE.sub(" ", text)  # strip ``` delimiters
    text = _RE_INLINE_CODE.sub(r"\1", text)  # `code` → code
    text = _RE_BOLD_DOUBLE_STAR.sub(r"\1", text)  # **bold** → bold
    text = _RE_BOLD_DOUBLE_UNDER.sub(r"\1", text)  # __bold__ → bold
    text = _RE_ITALIC_STAR.sub(r"\1", text)  # *italic* → italic
    text = _RE_IMAGE_LINK.sub(r"\1", text)  # ![alt](url) → alt
    text = _RE_LINK.sub(r"\1", text)  # [text](url) → text
    text = _RE_HEADING.sub("", text)  # ## Heading → Heading
    text = _RE_LIST_ITEM.sub("", text)  # - item → item
    text = _RE_BLOCKQUOTE.sub("", text)  # > quote → quote
    text = _RE_HR.sub("", text)  # --- → (gone)
    text = _RE_WHITESPACE.sub(" ", text).strip()  # collapse whitespace

    return text


_RE_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")


def split_for_speech(text: str, max_chars: int = 240) -> list[str]:
    """Split an agent reply into ordered sentence-sized TTS chunks.

    Applies normalize_for_speech() to the full text first (markdown/code-fence
    context requires whole-text processing), then sentence-splits on sentence
    boundary whitespace.  Each chunk is short enough that Kokoro renders it
    quickly, enabling the first PCM frame to reach the ESP32 while later
    sentences are still synthesizing.

    Short trailing fragments (under 12 chars) are merged forward to prevent
    over-splitting on abbreviations.  Sentences longer than max_chars are
    word-wrapped so each Piper invocation stays bounded.

    Returns an empty list when the text normalises to empty/whitespace.
    """
    normalized = normalize_for_speech(text)
    if not normalized:
        return []

    raw_chunks = _RE_SENTENCE_SPLIT.split(normalized)

    # Merge very short fragments (< 12 chars) forward into the next chunk.
    merged: list[str] = []
    pending = ""
    for chunk in raw_chunks:
        chunk = chunk.strip()
        if not chunk:
            continue
        if pending:
            chunk = pending + " " + chunk
            pending = ""
        if len(chunk) < 12:
            pending = chunk
        else:
            merged.append(chunk)
    if pending:  # leftover short trailing fragment
        if merged:
            merged[-1] = merged[-1] + " " + pending
        else:
            merged.append(pending)

    # Word-wrap any chunk that still exceeds max_chars.
    result: list[str] = []
    for chunk in merged:
        if len(chunk) <= max_chars:
            result.append(chunk)
        else:
            words = chunk.split()
            current = ""
            for word in words:
                if not current:
                    current = word
                elif len(current) + 1 + len(word) <= max_chars:
                    current += " " + word
                else:
                    result.append(current)
                    current = word
            if current:
                result.append(current)

    return result


def synthesize(text: str) -> bytes:
    """Synthesize *text* to raw S16LE PCM mono audio bytes at TARGET_SAMPLE_RATE.

    Kokoro neural TTS produces float32 audio at OUTPUT_SAMPLE_RATE (24000 Hz).
    When TARGET_SAMPLE_RATE differs, the output is resampled via the existing
    Kaiser-windowed sinc resampler so the ESP32-S3-BOX-3 speaker (locked to
    16 kHz by the WakeNet I²S bus) plays audio at the correct pitch and speed.

    Args:
        text: The text to speak.

    Returns:
        Raw S16LE PCM bytes at TARGET_SAMPLE_RATE Hz, mono.

    Raises:
        RuntimeError: If Kokoro fails to synthesize.
    """
    global _KOKORO_VOICE
    import numpy as _np

    text = normalize_for_speech(text)
    if not text:
        return b""

    try:
        pipeline = _get_pipeline()
        chunks: list = []
        for _, _, audio in pipeline(text, voice=_KOKORO_VOICE, speed=_KOKORO_SPEED):
            chunks.append(audio)
    except Exception as exc:
        if _KOKORO_VOICE != _FALLBACK_VOICE:
            # Configured voice unusable (typically: pack not in the offline
            # cache).  Fall back permanently so every later sentence uses one
            # consistent voice instead of failing per call.
            logger.warning(
                "Kokoro voice %r failed (%s) — falling back to %r permanently",
                _KOKORO_VOICE, exc, _FALLBACK_VOICE,
            )
            _KOKORO_VOICE = _FALLBACK_VOICE
            return synthesize(text)
        raise RuntimeError(f"Kokoro TTS failed: {exc}") from exc

    if not chunks:
        return b""

    samples = _np.concatenate(chunks).astype(_np.float32)
    # Amp headroom: Kokoro peaks near full scale, and the BOX-3's small
    # speaker amp clips audibly ("clicking/clipping") once the codec volume
    # exceeds ~75%.  Scaling the digital level down (-2.5 dB default) keeps
    # peaks off the amp rails across the whole 0-100% volume range.
    _headroom = float(_os.environ.get("VG_TTS_HEADROOM", "0.6"))
    samples = samples * _headroom
    # Convert float32 [-1, 1] → S16LE
    pcm = _np.clip(samples * 32767, -32768, 32767).astype("<i2").tobytes()

    if TARGET_SAMPLE_RATE != OUTPUT_SAMPLE_RATE:
        pcm = _resample_s16le_mono(pcm, OUTPUT_SAMPLE_RATE, TARGET_SAMPLE_RATE)
        logger.debug(
            "TTS resampled %d Hz → %d Hz: %d bytes for %d-char input",
            OUTPUT_SAMPLE_RATE,
            TARGET_SAMPLE_RATE,
            len(pcm),
            len(text),
        )
    else:
        logger.debug(
            "TTS produced %d PCM bytes at %d Hz for %d-char input",
            len(pcm),
            TARGET_SAMPLE_RATE,
            len(text),
        )

    # Edge fade (~5 ms): synthesize() runs per sentence, and consecutive Kokoro
    # outputs can start/end at different DC offsets/levels — each seam was an
    # audible click on the ESP32 speaker.  Ramp the first and last 80 samples
    # so sentence joins (and stream start/stop) are silent.
    _n_fade = min(80, len(pcm) // 4)
    if _n_fade > 1:
        s16 = _np.frombuffer(pcm, dtype="<i2").astype(_np.float32).copy()
        ramp = _np.linspace(0.0, 1.0, _n_fade, dtype=_np.float32)
        s16[:_n_fade] *= ramp
        s16[-_n_fade:] *= ramp[::-1]
        pcm = s16.astype("<i2").tobytes()
    return pcm
