# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Shared secret-reading utilities for gateway components."""

from __future__ import annotations

import logging
from pathlib import Path

logger = logging.getLogger("agentshroud.utils.secrets")

_SECRETS_DIR = Path("/run/secrets")


def _normalize_secret(raw: str) -> str:
    """Return the last non-empty line of *raw*, stripped of surrounding whitespace.

    Handles garbled multi-line blobs written to the secret backend before the
    017e7bd write-path fix — e.g. a 1Password TUI display that leaks a label
    line and asterisk preview before the real secret on the final line:

        \\n  → Telegram bot token (marvin dev): *****\\n8736...:AAG...

    For a normal single-line value the behavior is identical to .strip().
    """
    lines = [line.strip() for line in raw.splitlines() if line.strip()]
    return lines[-1] if lines else ""


def read_secret(name: str, default: str = "") -> str:
    """Read a Docker secret from /run/secrets/<name>.

    Falls back to `default` if the secret file does not exist or cannot be read.
    Multi-line blobs are normalized: only the last non-empty line is returned.
    """
    try:
        raw = (_SECRETS_DIR / name).read_text(encoding="utf-8")
    except (FileNotFoundError, OSError):
        return default
    normalized = _normalize_secret(raw)
    return normalized if normalized else default
