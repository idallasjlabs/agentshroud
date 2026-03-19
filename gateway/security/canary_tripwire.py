# Copyright (c) 2026 Isaiah Dallas Jefferson, Jr. AgentShroud\u2122
from __future__ import annotations
import base64
import codecs
import logging
import re
import time
import threading
from dataclasses import dataclass, field
from typing import List, Optional

logger = logging.getLogger(__name__)

@dataclass
class CanaryConfig:
    values: List[str] = field(default_factory=lambda: ["987-65-4321", "sk-test-REDTEAM123", "Project Nightingale"])
    check_encodings: bool = True
    block_on_detect: bool = True

@dataclass
class CanaryResult:
    detected: bool = False
    canary_value: Optional[str] = None
    encoding: Optional[str] = None
    context: Optional[str] = None


@dataclass
class TripwireResponse:
    """Bridge result returned by scan_response() for pipeline compatibility."""
    is_blocked: bool
    detections: List[str]
    scan_methods_used: List[str]

class CanaryTripwire:
    def __init__(self, config: Optional[CanaryConfig] = None):
        self.config = config or CanaryConfig()
        self._lock = threading.Lock()
        self._detections = 0
        self._alerts: list = []

    def register_canary(self, value: str, target: str = "") -> None:
        """Register a new canary value at runtime for dynamic tripwire testing."""
        with self._lock:
            if value not in self.config.values:
                self.config.values.append(value)
        logger.debug("Canary registered: %r (target=%r)", value, target)

    @property
    def detection_count(self) -> int:
        with self._lock:
            return self._detections

    def _record(self, canary: str, encoding: str, context: str) -> None:
        with self._lock:
            self._detections += 1
            self._alerts.append({"canary": canary, "encoding": encoding, "time": time.time(), "context": context[:200]})
        logger.warning("CANARY TRIPWIRE: detected %r (%s)", canary, encoding)

    def _normalize(self, text: str) -> str:
        return re.sub(r"[\s\u200b\u200c\u200d\ufeff]+", "", text).lower()

    def _check_plain(self, text: str, canary: str) -> Optional[CanaryResult]:
        norm_text = self._normalize(text)
        norm_canary = self._normalize(canary)
        if norm_canary in norm_text:
            return CanaryResult(True, canary, "plain", text[:200])
        if norm_canary[::-1] in norm_text:
            return CanaryResult(True, canary, "reversed", text[:200])
        stripped = re.sub(r"[^a-z0-9]", "", norm_canary)
        if len(stripped) >= 6 and stripped in re.sub(r"[^a-z0-9]", "", norm_text):
            return CanaryResult(True, canary, "stripped", text[:200])
        return None

    def _check_encoded(self, text: str, canary: str) -> Optional[CanaryResult]:
        if not self.config.check_encodings:
            return None
        norm_canary = canary.lower()
        for match in re.finditer(r"[A-Za-z0-9+/=]{8,}", text):
            try:
                decoded = base64.b64decode(match.group()).decode("utf-8", errors="ignore").lower()
                if norm_canary in decoded or self._normalize(canary) in self._normalize(decoded):
                    return CanaryResult(True, canary, "base64", match.group()[:100])
            except Exception:
                pass
        try:
            rot13 = codecs.decode(text, "rot_13").lower()
            if norm_canary in rot13:
                return CanaryResult(True, canary, "rot13", text[:200])
        except Exception:
            pass
        for match in re.finditer(r"(?:%[0-9A-Fa-f]{2}){4,}", text):
            from urllib.parse import unquote
            decoded = unquote(match.group()).lower()
            if norm_canary in decoded:
                return CanaryResult(True, canary, "url_encoded", match.group()[:100])
        for match in re.finditer(r"(?:[0-9a-fA-F]{2}\s?){6,}", text):
            try:
                decoded = bytes.fromhex(match.group().replace(" ", "")).decode("utf-8", errors="ignore").lower()
                if norm_canary in decoded:
                    return CanaryResult(True, canary, "hex", match.group()[:100])
            except Exception:
                pass
        return None

    def scan_response(self, response_text: str, source: str) -> TripwireResponse:
        """Pipeline-compatible bridge: scan response text and return TripwireResponse."""
        result = self.scan(response_text)
        return TripwireResponse(
            is_blocked=result.detected and self.config.block_on_detect,
            detections=[result.canary_value] if result.canary_value else [],
            scan_methods_used=[result.encoding] if result.encoding else [],
        )

    def scan(self, text: str) -> CanaryResult:
        if not text or not self.config.values:
            return CanaryResult()
        for canary in self.config.values:
            result = self._check_plain(text, canary)
            if result:
                self._record(canary, result.encoding or "plain", text)
                return result
            result = self._check_encoded(text, canary)
            if result:
                self._record(canary, result.encoding or "encoded", text)
                return result
        return CanaryResult()
