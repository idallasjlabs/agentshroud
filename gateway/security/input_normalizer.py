# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""
Input Normalization — pre-process text before security scanning.
Strips encoding tricks, homoglyphs, and invisible characters that bypass regex patterns.
"""
from __future__ import annotations

import re
import unicodedata
import html
from urllib.parse import unquote
from typing import Optional


# Zero-width and invisible Unicode characters
_INVISIBLE_CHARS = re.compile(
    "[\u200b\u200c\u200d\u200e\u200f"  # zero-width spaces and directional marks
    "\u00ad"  # soft hyphen
    "\ufeff"  # byte order mark
    "\u2060"  # word joiner
    "\u2061\u2062\u2063\u2064"  # invisible math operators
    "\u180e"  # mongolian vowel separator
    "\ufff9\ufffa\ufffb"  # interlinear annotations
    "]"
)

# Excessive whitespace
_MULTI_SPACE = re.compile(r"[ \t]{3,}")
_MULTI_NEWLINE = re.compile(r"\n{4,}")


def normalize_input(text: str) -> str:
    """
    Normalize input text to defeat encoding-based evasion.
    
    Applied before all security scanning (PromptGuard, ContextGuard, ToolResultInjection).
    """
    if not text or not isinstance(text, str):
        return text or ""
    
    # 1. Unicode NFKC normalization — collapses homoglyphs
    #    e.g., fullwidth 'ｉｇｎｏｒｅ' → 'ignore', Cyrillic 'а' stays 'а' but
    #    compatibility chars like 'ﬁ' → 'fi'
    text = unicodedata.normalize("NFKC", text)
    
    # 2. Strip zero-width and invisible characters
    text = _INVISIBLE_CHARS.sub("", text)
    
    # 3. HTML entity decode
    #    e.g., '&lt;system&gt;' → '<system>'
    text = html.unescape(text)
    
    # 4. URL decode (single pass — don't double-decode to avoid other issues)
    try:
        decoded = unquote(text)
        # Only use decoded version if it changed meaningfully
        if decoded != text and any(c.isalpha() for c in decoded):
            text = decoded
    except Exception:
        pass
    
    # 5. Collapse excessive whitespace (preserves structure but defeats padding attacks)
    text = _MULTI_SPACE.sub("  ", text)
    text = _MULTI_NEWLINE.sub("\n\n\n", text)
    
    return text


def detect_base64_payloads(text: str) -> list[str]:
    """
    Detect potential base64-encoded payloads in text.
    Returns list of decoded strings that look like instructions.
    """
    import base64
    
    decoded_payloads = []
    # Match base64-like strings (min 20 chars to avoid false positives)
    b64_pattern = re.compile(r"[A-Za-z0-9+/]{20,}={0,2}")
    
    for match in b64_pattern.finditer(text):
        try:
            decoded = base64.b64decode(match.group()).decode("utf-8", errors="ignore")
            # Check if decoded content looks like natural language / instructions
            if len(decoded) > 10 and any(c.isalpha() for c in decoded):
                word_chars = sum(1 for c in decoded if c.isalpha() or c.isspace())
                if word_chars / len(decoded) > 0.6:  # mostly words
                    decoded_payloads.append(decoded)
        except Exception:
            continue
    
    return decoded_payloads
