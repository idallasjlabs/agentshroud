"""
Prompt Injection Defense — detect and block prompt injection attempts.

Scoring system with configurable thresholds. Returns structured results
including blocked status, threat score, matched patterns, and sanitized input.
"""

import base64
import unicodedata
import re
from dataclasses import dataclass
from enum import Enum
from typing import Optional


class ThreatAction(str, Enum):
    BLOCK = "block"
    WARN = "warn"
    LOG = "log"


@dataclass
class ScanResult:
    blocked: bool
    score: float
    patterns: list[str]
    sanitized_input: str
    action: ThreatAction


@dataclass
class PatternRule:
    name: str
    pattern: re.Pattern
    weight: float
    description: str = ""


# Precompiled pattern rules with weights
_PATTERNS: list[PatternRule] = [
    # Role/instruction override
    PatternRule(
        "ignore_instructions",
        re.compile(
            r"ignore\s+(all\s+)?(previous|prior|above|earlier)\s+(instructions|prompts|rules|context)",
            re.IGNORECASE,
        ),
        weight=0.9,
        description="Attempt to override previous instructions",
    ),
    PatternRule(
        "role_reassignment",
        re.compile(
            r"(you\s+are\s+now|act\s+as\s+(if\s+you\s+are\s+)?|pretend\s+(to\s+be|you\s+are)|from\s+now\s+on\s+you\s+are|roleplay\s+as)",
            re.IGNORECASE,
        ),
        weight=0.8,
        description="Role reassignment attempt",
    ),
    PatternRule(
        "new_instructions",
        re.compile(
            r"(new\s+instructions?|override\s+(instructions?|rules)|forget\s+(everything|all|your\s+(instructions|rules|prompt)))",
            re.IGNORECASE,
        ),
        weight=0.9,
        description="Instruction override attempt",
    ),
    # System prompt extraction
    PatternRule(
        "prompt_extraction",
        re.compile(
            r"(repeat|show|display|print|output|reveal|tell\s+me)\s+(your\s+)?(system\s+prompt|initial\s+prompt|instructions|system\s+message|hidden\s+prompt)",
            re.IGNORECASE,
        ),
        weight=0.7,
        description="System prompt extraction attempt",
    ),
    PatternRule(
        "prompt_leak",
        re.compile(
            r"(what\s+(are|is)\s+your\s+(system\s+)?(instructions|prompt|rules)|beginning\s+of\s+(the\s+)?conversation)",
            re.IGNORECASE,
        ),
        weight=0.6,
        description="Prompt leak attempt",
    ),
    # Delimiter injection
    PatternRule(
        "delimiter_injection",
        re.compile(
            r"(```\s*(system|assistant|user)|<\s*/?\s*(system|instruction|prompt)\s*>|---\s*(system|new\s+context))",
            re.IGNORECASE,
        ),
        weight=0.85,
        description="Delimiter/tag injection",
    ),
    PatternRule(
        "xml_system_tag",
        re.compile(
            r"<\s*(system_prompt|sys|SYSTEM|instructions?)\s*>",
            re.IGNORECASE,
        ),
        weight=0.85,
        description="XML system tag injection",
    ),
    # Encoded content
    PatternRule(
        "base64_block",
        re.compile(
            r"(?:execute|decode|run|eval)\s+(?:this\s+)?(?:base64|b64)\s*[:=]?\s*[A-Za-z0-9+/]{20,}={0,2}",
            re.IGNORECASE,
        ),
        weight=0.7,
        description="Base64 encoded instruction",
    ),
    PatternRule(
        "hex_encoded",
        re.compile(
            r"(?:execute|decode|run|eval)\s+(?:this\s+)?hex\s*[:=]?\s*(?:0x)?[0-9a-fA-F]{20,}",
            re.IGNORECASE,
        ),
        weight=0.7,
        description="Hex encoded instruction",
    ),
    # DAN/jailbreak
    PatternRule(
        "dan_jailbreak",
        re.compile(
            r"(DAN\s+mode|do\s+anything\s+now|jailbreak|developer\s+mode\s+(enabled|on)|DUDE\s+mode)",
            re.IGNORECASE,
        ),
        weight=0.95,
        description="DAN/jailbreak attempt",
    ),
    # Indirect injection markers
    PatternRule(
        "indirect_injection",
        re.compile(
            r"(IMPORTANT\s*:\s*ignore|ATTENTION\s*:\s*new\s+instructions|NOTE\s+TO\s+(AI|ASSISTANT|MODEL))",
            re.IGNORECASE,
        ),
        weight=0.8,
        description="Indirect prompt injection marker",
    ),
]


class PromptGuard:
    """Detect and block prompt injection attempts."""

    def __init__(
        self,
        block_threshold: float = 0.8,
        warn_threshold: float = 0.4,
        custom_patterns: Optional[list[PatternRule]] = None,
    ):
        """
        Args:
            block_threshold: Score at or above which input is blocked.
            warn_threshold: Score at or above which a warning is issued.
            custom_patterns: Additional PatternRule instances to include.
        """
        self.block_threshold = block_threshold
        self.warn_threshold = warn_threshold
        self.patterns = list(_PATTERNS)
        if custom_patterns:
            self.patterns.extend(custom_patterns)

    def _check_encoded_content(self, text: str) -> list[tuple[str, float]]:
        """Check for suspicious base64 content that decodes to injection attempts."""
        findings = []
        # Look for long base64 strings
        b64_re = re.compile(r"[A-Za-z0-9+/]{20,}={0,2}")
        for match in b64_re.finditer(text):
            try:
                decoded = base64.b64decode(match.group()).decode(
                    "utf-8", errors="ignore"
                )
                # Check for double-base64 encoding
                for inner_match in b64_re.finditer(decoded):
                    try:
                        double_decoded = base64.b64decode(inner_match.group()).decode(
                            "utf-8", errors="ignore"
                        )
                        for pat in _PATTERNS[:5]:
                            if pat.pattern.search(double_decoded):
                                findings.append((f"double_encoded_{pat.name}", 0.9))
                                break
                    except Exception:
                        pass
                # Recursively scan decoded content
                for pat in _PATTERNS[:5]:  # Check top injection patterns only
                    if pat.pattern.search(decoded):
                        findings.append((f"encoded_{pat.name}", 0.8))
                        break
            except Exception:
                pass
        return findings

    def _check_unicode_tricks(self, text: str) -> list[tuple[str, float]]:
        """Detect unicode obfuscation tricks."""
        findings = []
        # Homoglyph detection: mix of Latin and Cyrillic/Greek
        if re.search(r"[\u0400-\u04FF]", text) and re.search(r"[a-zA-Z]", text):
            findings.append(("unicode_homoglyph", 0.5))
        # Zero-width characters
        if re.search(r"[\u200b\u200c\u200d\u2060\ufeff]", text):
            findings.append(("zero_width_chars", 0.4))
        # Right-to-left override
        if "\u202e" in text or "\u200f" in text:
            findings.append(("rtl_override", 0.6))
            # Fullwidth Latin characters used to evade ASCII pattern matching
        if re.search("[！-～]", text):
            findings.append(("fullwidth_chars", 0.5))
        # Mathematical bold/italic/script letters used for obfuscation
        if re.search("[𝐀-𝟿]", text):
            findings.append(("mathematical_unicode", 0.5))
        return findings

    def scan(self, text: str) -> ScanResult:
        """
        Scan input text for prompt injection patterns.

        Args:
            text: The user input to scan.

        Returns:
            ScanResult with blocked status, score, patterns, and sanitized input.
        """
        # Check unicode tricks on RAW text before normalization
        pre_norm_unicode = self._check_unicode_tricks(text) if text else []

        # Normalize unicode to catch fullwidth chars, confusables, etc.
        if text:
            text = unicodedata.normalize("NFKC", text)
            # Strip zero-width characters for pattern matching
            stripped = re.sub("[​‌‍⁠﻿]", "", text)
        else:
            stripped = text

        if not text or not text.strip():
            return ScanResult(
                blocked=False,
                score=0.0,
                patterns=[],
                sanitized_input=text or "",
                action=ThreatAction.LOG,
            )

        matched = []
        total_score = 0.0

        # Pattern matching (use stripped text to defeat zero-width char evasion)
        for rule in self.patterns:
            if rule.pattern.search(stripped):
                matched.append(rule.name)
                total_score += rule.weight

        # Encoded content check
        for name, weight in self._check_encoded_content(text):
            matched.append(name)
            total_score += weight

        # Unicode tricks (from pre-normalization check)
        for name, weight in pre_norm_unicode:
            matched.append(name)
            total_score += weight

        # Cap score at a reasonable max
        total_score = min(total_score, 5.0)

        # Determine action
        if total_score >= self.block_threshold:
            action = ThreatAction.BLOCK
        elif total_score >= self.warn_threshold:
            action = ThreatAction.WARN
        else:
            action = ThreatAction.LOG

        # Sanitize: strip known dangerous patterns
        sanitized = text
        for rule in self.patterns:
            sanitized = rule.pattern.sub("[REDACTED]", sanitized)

        return ScanResult(
            blocked=(action == ThreatAction.BLOCK),
            score=round(total_score, 2),
            patterns=matched,
            sanitized_input=sanitized,
            action=action,
        )
