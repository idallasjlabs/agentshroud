# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Shared secret-reading utilities for gateway components."""
from __future__ import annotations

import logging
from pathlib import Path

logger = logging.getLogger("agentshroud.utils.secrets")

_SECRETS_DIR = Path("/run/secrets")


def read_secret(name: str, default: str = "") -> str:
    """Read a Docker secret from /run/secrets/<name>.

    Falls back to `default` if the secret file does not exist or cannot be read.
    """
    try:
        return (_SECRETS_DIR / name).read_text(encoding="utf-8").strip()
    except (FileNotFoundError, OSError):
        return default
