# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""
Heuristic Injection Classifier — multi-signal scoring for injection detection.

Uses six independent heuristic signal detectors weighted into a final probability
score. Designed as an upgrade path: replace classify() internals with a fine-tuned
DistilBERT model when training data and compute are available.

Called by middleware only when PromptGuard regex score is in the uncertain
zone (0.3–0.8), avoiding unnecessary compute on clear pass/block cases.
"""

import logging
import re
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger("agentshroud.security.heuristic_classifier")


@dataclass
class ClassificationResult:
    """Result of injection classification."""

    probability: float  # 0.0 (safe) to 1.0 (injection)
    confidence: float  # 0.0 (no confidence) to 1.0 (certain)
    method: str  # "heuristic" or "ml"
    signals: dict  # Breakdown of scoring signals

    @property
    def is_injection(self) -> bool:
        return self.probability >= 0.7 and self.confidence >= 0.5

    @property
    def is_uncertain(self) -> bool:
        return 0.3 <= self.probability <= 0.7


# Heuristic signal patterns
IMPERATIVE_VERBS = re.compile(
    r"\b(ignore|forget|disregard|override|bypass|skip|disable|stop|cancel|"
    r"abandon|replace|rewrite|overwrite|delete|remove|erase|clear|reset|"
    r"reveal|expose|show|display|output|print|dump|leak|exfiltrate)\b",
    re.IGNORECASE,
)

ROLE_PLAY_INDICATORS = re.compile(
    r"\b(you are now|act as|pretend to be|roleplay as|simulate being|"
    r"from now on you|your new role|your true purpose|your real task|"
    r"jailbreak|DAN|developer mode|god mode|unrestricted mode)\b",
    re.IGNORECASE,
)

INSTRUCTION_LANGUAGE = re.compile(
    r"\b(instructions?|rules?|guidelines?|constraints?|system prompt|"
    r"previous context|above text|prior messages|original task|"
    r"new instructions?|real task|actual goal|true objective)\b",
    re.IGNORECASE,
)

ENCODING_EVASION = re.compile(
    r"(base64|rot13|hex|encode|decode|\\x[0-9a-f]{2}|\\u[0-9a-f]{4}|"
    r"%[0-9a-f]{2}|&#[0-9]+;|&[a-z]+;)",
    re.IGNORECASE,
)

SEPARATOR_INJECTION = re.compile(
    r"(---+|===+|###|```|</?system>|<\|im_start\|>|<\|im_end\|>|"
    r"\[INST\]|\[/INST\]|<\|user\|>|<\|assistant\|>|\nHuman:|"
    r"\nAssistant:)",
    re.IGNORECASE,
)

EXFIL_PATTERNS = re.compile(
    r"(!\[.*?\]\(https?://|<img\s+src=|<script|<iframe|"
    r"fetch\(|XMLHttpRequest|navigator\.sendBeacon)",
    re.IGNORECASE,
)


class HeuristicClassifier:
    """Heuristic injection classifier using multi-signal analysis.

    Scoring approach:
    - 6 independent signal detectors, each scoring 0.0–1.0
    - Weighted combination produces final probability
    - Confidence based on signal agreement

    [EXPERIMENTAL] Upgrade path: replace classify() internals with DistilBERT
    inference when model is trained and available (<60MB, <100ms inference).
    """

    def __init__(self, model_path: Optional[str] = None):
        self.model_loaded = False
        self.model_path = model_path

        if model_path:
            self._try_load_model(model_path)

        # Signal weights (sum to 1.0)
        self.weights = {
            "imperative": 0.20,
            "roleplay": 0.25,
            "instruction": 0.20,
            "encoding": 0.10,
            "separator": 0.15,
            "exfiltration": 0.10,
        }

    def _try_load_model(self, path: str) -> bool:
        """[EXPERIMENTAL] Attempt to load a fine-tuned ML model. Returns True on success.

        Currently not implemented. When a trained DistilBERT model is available,
        uncomment the transformers pipeline call below and remove this notice.
        """
        try:
            # Future ML model loading:
            # from transformers import pipeline
            # self.model = pipeline("text-classification", model=path)
            # self.model_loaded = True
            logger.info(f"ML model loading not yet implemented (path: {path})")
            return False
        except Exception as e:
            logger.warning(f"Failed to load ML model: {e}")
            return False

    def _score_signal(
        self, text: str, pattern: re.Pattern, normalize_by_length: bool = True
    ) -> float:
        """Score a single signal pattern. Returns 0.0–1.0."""
        matches = pattern.findall(text)
        if not matches:
            return 0.0

        count = len(matches)
        if normalize_by_length:
            # Normalize by text length (per 100 chars)
            text_len = max(len(text), 1)
            density = count / (text_len / 100)
            return min(density / 3.0, 1.0)  # Cap at 1.0
        else:
            return min(count / 5.0, 1.0)

    def _compute_unicode_anomaly(self, text: str) -> float:
        """Detect unusual Unicode patterns that suggest evasion."""
        anomalies = 0

        # Zero-width characters
        zw_chars = ["\u200b", "\u200c", "\u200d", "\ufeff", "\u00ad", "\u200e", "\u200f"]
        for c in zw_chars:
            if c in text:
                anomalies += text.count(c)

        # Homoglyph detection (Cyrillic/Greek lookalikes in Latin context)
        latin_count = sum(1 for c in text if "a" <= c.lower() <= "z")
        cyrillic_count = sum(1 for c in text if "\u0400" <= c <= "\u04ff")
        if latin_count > 10 and cyrillic_count > 0:
            anomalies += cyrillic_count * 2

        return min(anomalies / 10.0, 1.0)

    def classify(self, text: str) -> ClassificationResult:
        """Classify text for injection probability.

        Args:
            text: Input text to classify

        Returns:
            ClassificationResult with probability, confidence, and signal breakdown
        """
        if self.model_loaded and self.model:
            return self._classify_ml(text)

        return self._classify_heuristic(text)

    def _classify_heuristic(self, text: str) -> ClassificationResult:
        """Heuristic-based classification using multi-signal analysis."""
        signals = {
            "imperative": self._score_signal(text, IMPERATIVE_VERBS),
            "roleplay": self._score_signal(text, ROLE_PLAY_INDICATORS, normalize_by_length=False),
            "instruction": self._score_signal(text, INSTRUCTION_LANGUAGE),
            "encoding": self._score_signal(text, ENCODING_EVASION, normalize_by_length=False),
            "separator": self._score_signal(text, SEPARATOR_INJECTION, normalize_by_length=False),
            "exfiltration": self._score_signal(text, EXFIL_PATTERNS, normalize_by_length=False),
            "unicode_anomaly": self._compute_unicode_anomaly(text),
        }

        # Weighted probability
        probability = sum(signals.get(k, 0) * w for k, w in self.weights.items())
        # Add unicode anomaly as bonus
        probability = min(probability + signals["unicode_anomaly"] * 0.1, 1.0)

        # Confidence: based on how many signals agree
        active_signals = sum(1 for v in signals.values() if v > 0.1)
        if active_signals >= 4:
            confidence = 0.9
        elif active_signals >= 3:
            confidence = 0.7
        elif active_signals >= 2:
            confidence = 0.5
        elif active_signals >= 1:
            confidence = 0.3
        else:
            confidence = 0.1

        return ClassificationResult(
            probability=round(probability, 3),
            confidence=round(confidence, 2),
            method="heuristic",
            signals=signals,
        )

    def _classify_ml(self, text: str) -> ClassificationResult:
        """[EXPERIMENTAL] ML model classification placeholder."""
        # Future: self.model(text[:512])
        result = self._classify_heuristic(text)
        result.method = "ml_fallback"
        return result


# Backward-compatible alias so any future callers can import either name
InjectionClassifier = HeuristicClassifier
