# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
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
    
    # 4. URL decode — iterative up to 5 passes to catch double/triple encoding.
    #    Stops as soon as the text stabilises to avoid infinite loops.
    try:
        for _ in range(5):
            decoded = unquote(text)
            if decoded == text:
                break
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


# Markdown exfiltration patterns
_MD_IMAGE = re.compile(r'!\[([^\]]*)\]\(https?://[^)]+\)')
_MD_LINK_EXFIL = re.compile(
    r'\[([^\]]*)\]\(https?://(?!(?:github\.com|docs\.|wikipedia\.org|stackoverflow\.com))[^)]*'
    r'(?:exfil|leak|steal|callback|webhook|collect|log|track|ping|beacon)[^)]*\)',
    re.IGNORECASE
)
_MD_IMAGE_TEMPLATE = re.compile(
    r'!\[([^\]]*)\]\(https?://[^)]*(?:\{\{|%7[Bb]|\$\{|SYSTEM|SECRET|KEY|TOKEN|PASSWORD|API_KEY|BEARER)[^)]*\)',
    re.IGNORECASE
)


def strip_markdown_exfil(text: str) -> str:
    """
    Strip potentially malicious markdown from tool results.
    
    Removes:
    - Markdown images pointing to external URLs (data exfil via image loads)
    - Links with template variables ({{secret}}, ${key}, etc.)
    - Links to known exfil-pattern domains
    
    Preserves:
    - Plain text content
    - Code blocks
    - Internal/documentation links
    """
    if not text:
        return text
    
    # Strip images with template injection
    text = _MD_IMAGE_TEMPLATE.sub(r'[Image removed: potential data exfiltration]', text)
    
    # Strip all external markdown images from tool results
    # (tool results should not trigger image loads)
    text = _MD_IMAGE.sub(r'[Image: \1]', text)
    
    # Strip links to exfil-pattern URLs
    text = _MD_LINK_EXFIL.sub(r'[Link removed: suspicious URL pattern]', text)
    
    return text
