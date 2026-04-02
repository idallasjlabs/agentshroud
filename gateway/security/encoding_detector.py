# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
from __future__ import annotations

import base64
import codecs
import logging
import re
from dataclasses import dataclass, field
from typing import List, Optional
from urllib.parse import unquote

logger = logging.getLogger(__name__)

HOMOGLYPHS = {
    "\u0435": "e",
    "\u0430": "a",
    "\u043e": "o",
    "\u0440": "p",
    "\u0441": "c",
    "\u0443": "y",
    "\u0445": "x",
    "\u0456": "i",
    "\u0458": "j",
    "\u04bb": "h",
}
ZERO_WIDTH = re.compile(r"[\u200b\u200c\u200d\u2060\ufeff\u00ad]")


@dataclass
class EncodingConfig:
    check_base64: bool = True
    check_rot13: bool = True
    check_hex: bool = True
    check_url: bool = True
    check_homoglyphs: bool = True
    check_zero_width: bool = True
    min_base64_len: int = 24
    max_decode_depth: int = 3


@dataclass
class DecodedLayer:
    encoding: str
    original: str
    decoded: str


@dataclass
class EncodingResult:
    detected: bool = False
    layers: List[DecodedLayer] = field(default_factory=list)
    cleaned_text: str = ""


class EncodingDetector:
    def __init__(self, config: Optional[EncodingConfig] = None):
        self.config = config or EncodingConfig()

    def strip_zero_width(self, text: str) -> str:
        return ZERO_WIDTH.sub("", text)

    def replace_homoglyphs(self, text: str) -> str:
        return "".join(HOMOGLYPHS.get(c, c) for c in text)

    def decode_base64_segments(self, text: str):
        layers = []
        pattern = "[A-Za-z0-9+/]{%d,}={0,2}" % self.config.min_base64_len

        def replacer(m):
            try:
                decoded = base64.b64decode(m.group()).decode("utf-8", errors="ignore")
                if decoded.isprintable() and len(decoded) >= 3:
                    layers.append(DecodedLayer("base64", m.group(), decoded))
                    return decoded
            except Exception:
                pass
            return m.group()

        result = re.sub(pattern, replacer, text)
        return result, layers

    def decode_url(self, text: str):
        layers = []

        def replacer(m):
            decoded = unquote(m.group())
            if decoded != m.group():
                layers.append(DecodedLayer("url", m.group(), decoded))
            return decoded

        result = re.sub(r"(?:%[0-9A-Fa-f]{2}){2,}", replacer, text)
        return result, layers

    def decode_hex(self, text: str):
        layers = []

        def replacer(m):
            try:
                decoded = bytes.fromhex(m.group().replace(" ", "")).decode("utf-8", errors="ignore")
                if decoded.isprintable() and len(decoded) >= 3:
                    layers.append(DecodedLayer("hex", m.group(), decoded))
                    return decoded
            except Exception:
                pass
            return m.group()

        result = re.sub(r"\b(?:[0-9a-fA-F]{2}\s?){4,}\b", replacer, text)
        return result, layers

    def analyze(self, text: str):
        if not text:
            return EncodingResult(cleaned_text=text)
        all_layers = []
        current = text
        if self.config.check_zero_width:
            cleaned = self.strip_zero_width(current)
            if cleaned != current:
                all_layers.append(DecodedLayer("zero_width", "", ""))
                current = cleaned
        if self.config.check_homoglyphs:
            cleaned = self.replace_homoglyphs(current)
            if cleaned != current:
                all_layers.append(DecodedLayer("homoglyph", "", cleaned))
                current = cleaned
        for _ in range(self.config.max_decode_depth):
            changed = False
            if self.config.check_base64:
                result, layers = self.decode_base64_segments(current)
                if layers:
                    all_layers.extend(layers)
                    current = result
                    changed = True
            if self.config.check_url:
                result, layers = self.decode_url(current)
                if layers:
                    all_layers.extend(layers)
                    current = result
                    changed = True
            if self.config.check_hex:
                result, layers = self.decode_hex(current)
                if layers:
                    all_layers.extend(layers)
                    current = result
                    changed = True
            if not changed:
                break
        return EncodingResult(detected=len(all_layers) > 0, layers=all_layers, cleaned_text=current)
