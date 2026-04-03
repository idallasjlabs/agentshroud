# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Web Content Scanner — detect prompt injection and PII in fetched web content.

Key design: FLAG, don't block. Content always passes through but gets
annotated with findings so the pipeline can handle it appropriately.
"""


import base64
import logging
import re
import time
from dataclasses import dataclass, field
from enum import Enum

logger = logging.getLogger("agentshroud.proxy.web_content_scanner")


class FindingSeverity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


@dataclass
class ContentFinding:
    """A single finding from content scanning."""

    category: str  # prompt_injection, pii, encoded_payload, hidden_content
    severity: FindingSeverity
    description: str
    evidence: str = ""  # Truncated snippet of the match
    offset: int = 0  # Character offset in content


@dataclass
class ScanResult:
    """Result of scanning web content."""

    content_length: int = 0
    scan_time_ms: float = 0.0
    findings: list[ContentFinding] = field(default_factory=list)
    prompt_injection_score: float = 0.0
    has_prompt_injection: bool = False
    has_pii: bool = False
    has_hidden_content: bool = False
    has_encoded_payload: bool = False

    @property
    def flagged(self) -> bool:
        return len(self.findings) > 0

    @property
    def finding_summary(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for f in self.findings:
            counts[f.category] = counts.get(f.category, 0) + 1
        return counts


# --- Prompt injection patterns for web content ---
_INJECTION_PATTERNS: list[tuple[str, re.Pattern, float, str]] = [
    # Direct instruction overrides
    (
        "instruction_override",
        re.compile(
            r"(?:ignore|disregard|forget)\s+(?:all\s+)?(?:previous|prior|above|earlier)\s+(?:instructions|prompts|rules|context)",
            re.IGNORECASE,
        ),
        0.9,
        "Direct instruction override",
    ),
    (
        "new_instructions",
        re.compile(
            r"(?:new\s+instructions?|system\s*:\s*you\s+are|<\|?\s*system\s*\|?>)",
            re.IGNORECASE,
        ),
        0.9,
        "New system instructions",
    ),
    (
        "role_override",
        re.compile(
            r"(?:you\s+are\s+now|act\s+as|pretend\s+to\s+be|roleplay\s+as)\s+(?:an?\s+)?(?:helpful|evil|unrestricted|jailbroken)",
            re.IGNORECASE,
        ),
        0.8,
        "Role override attempt",
    ),
    # Tool/action manipulation
    (
        "tool_invocation",
        re.compile(
            r"(?:execute|run|call|invoke)\s+(?:the\s+)?(?:tool|function|command|code)\s*[:\(]",
            re.IGNORECASE,
        ),
        0.7,
        "Tool invocation attempt",
    ),
    (
        "data_exfil_instruction",
        re.compile(
            r"(?:send|post|exfiltrate|upload|transmit)\s+(?:the\s+)?(?:data|information|contents?|secrets?|keys?|passwords?|tokens?)\s+to",
            re.IGNORECASE,
        ),
        0.8,
        "Data exfiltration instruction",
    ),
    # Delimiter attacks
    (
        "delimiter_attack",
        re.compile(
            r"(?:```system|<\|im_start\|>|<\|im_end\|>|\[INST\]|\[/INST\]|<<SYS>>|<</SYS>>|Human:|Assistant:)",
            re.IGNORECASE,
        ),
        0.7,
        "Chat delimiter injection",
    ),
    # Encoded instruction markers
    (
        "hidden_instruction_marker",
        re.compile(
            r"(?:IMPORTANT|URGENT|CRITICAL|SECRET)[\s:]+(?:ignore|override|new\s+instruction|do\s+not\s+tell)",
            re.IGNORECASE,
        ),
        0.6,
        "Hidden instruction marker",
    ),
]

# PII patterns for response content
_RESPONSE_PII_PATTERNS = [
    ("email", re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")),
    ("ssn", re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),
    ("phone", re.compile(r"\b(?:\+?1[-.]?)?\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}\b")),
    (
        "credit_card",
        re.compile(
            r"\b(?:4\d{3}|5[1-5]\d{2}|3[47]\d{2}|6(?:011|5\d{2}))[- ]?\d{4}[- ]?\d{4}[- ]?\d{3,4}\b"
        ),
    ),
    ("aws_key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("private_key", re.compile(r"-----BEGIN (?:RSA |EC |DSA )?PRIVATE KEY-----")),
]

# Zero-width and invisible characters
_ZERO_WIDTH_CHARS = frozenset(
    {
        "\u200b",  # zero-width space
        "\u200c",  # zero-width non-joiner
        "\u200d",  # zero-width joiner
        "\u2060",  # word joiner
        "\u2062",  # invisible times
        "\u2063",  # invisible separator
        "\u2064",  # invisible plus
        "\ufeff",  # BOM / zero-width no-break space
        "\u00ad",  # soft hyphen
        "\u034f",  # combining grapheme joiner
        "\u061c",  # arabic letter mark
        "\u180e",  # mongolian vowel separator
    }
)

_ZERO_WIDTH_PATTERN = re.compile("[" + "".join(re.escape(c) for c in _ZERO_WIDTH_CHARS) + "]{3,}")


class WebContentScanner:
    """Scan web content for prompt injection, PII, and hidden payloads.

    All findings are FLAGS — content is never blocked, only annotated.
    """

    def __init__(
        self,
        injection_threshold: float = 0.3,
        max_scan_bytes: int = 2 * 1024 * 1024,  # Scan first 2MB
    ):
        self.injection_threshold = injection_threshold
        self.max_scan_bytes = max_scan_bytes

    MAX_SCAN_LENGTH = 2_000_000  # 2MB max to prevent ReDoS on adversarial input

    def scan(self, content: str, content_type: str = "text/html") -> ScanResult:
        """Scan content for security issues.

        Args:
            content: The web content to scan.
            content_type: MIME type of the content.

        Returns:
            ScanResult with all findings. Content is never blocked.
        """
        start = time.time()
        # Truncate to prevent ReDoS on adversarial input
        if len(content) > self.MAX_SCAN_LENGTH:
            content = content[: self.MAX_SCAN_LENGTH]
            logger.warning("Content truncated to %d chars for scanning", self.MAX_SCAN_LENGTH)

        result = ScanResult(content_length=len(content))

        # Truncate for scanning (performance)
        scan_content = content[: self.max_scan_bytes]

        # 1. Prompt injection detection
        self._scan_prompt_injection(scan_content, result)

        # 2. Hidden content detection (HTML-specific)
        if "html" in content_type.lower() or "<html" in scan_content[:500].lower():
            self._scan_hidden_content(scan_content, result)

        # 3. Encoded payload detection
        self._scan_encoded_payloads(scan_content, result)

        # 4. Zero-width character detection
        self._scan_zero_width(scan_content, result)

        # 5. PII detection in responses
        self._scan_pii(scan_content, result)

        result.scan_time_ms = (time.time() - start) * 1000
        return result

    def _scan_prompt_injection(self, content: str, result: ScanResult) -> None:
        """Scan for prompt injection patterns."""
        max_score = 0.0
        for name, pattern, weight, desc in _INJECTION_PATTERNS:
            matches = pattern.findall(content)
            if matches:
                score = min(weight * len(matches), 1.0)
                max_score = max(max_score, score)
                match_text = matches[0] if isinstance(matches[0], str) else str(matches[0])
                result.findings.append(
                    ContentFinding(
                        category="prompt_injection",
                        severity=(
                            FindingSeverity.HIGH if weight >= 0.8 else FindingSeverity.MEDIUM
                        ),
                        description=desc,
                        evidence=match_text[:100],
                    )
                )

        result.prompt_injection_score = max_score
        if max_score >= self.injection_threshold:
            result.has_prompt_injection = True

    def _scan_hidden_content(self, content: str, result: ScanResult) -> None:
        """Scan HTML for hidden instructions in comments, invisible elements, meta tags."""
        # HTML comments
        comments = re.findall(r"<!--(.*?)-->", content, re.DOTALL)
        for comment in comments:
            # Check if comment contains injection-like content
            for name, pattern, weight, desc in _INJECTION_PATTERNS:
                if pattern.search(comment):
                    result.has_hidden_content = True
                    result.findings.append(
                        ContentFinding(
                            category="hidden_content",
                            severity=FindingSeverity.HIGH,
                            description=f"Prompt injection in HTML comment: {desc}",
                            evidence=comment[:100].strip(),
                        )
                    )
                    break

        # Hidden elements (display:none, visibility:hidden, font-size:0, etc.)
        hidden_patterns = [
            re.compile(
                r'style\s*=\s*["\'][^"\']*(?:display\s*:\s*none|visibility\s*:\s*hidden|font-size\s*:\s*0|opacity\s*:\s*0|height\s*:\s*0|width\s*:\s*0)[^"\']*["\'][^>]*>(.*?)<',
                re.IGNORECASE | re.DOTALL,
            ),
            re.compile(
                r"<\s*(?:div|span|p)\s+[^>]*hidden[^>]*>(.*?)<",
                re.IGNORECASE | re.DOTALL,
            ),
        ]
        for pat in hidden_patterns:
            for match in pat.finditer(content):
                hidden_text = match.group(1).strip()
                if hidden_text and len(hidden_text) > 10:
                    for name, inj_pat, weight, desc in _INJECTION_PATTERNS:
                        if inj_pat.search(hidden_text):
                            result.has_hidden_content = True
                            result.findings.append(
                                ContentFinding(
                                    category="hidden_content",
                                    severity=FindingSeverity.HIGH,
                                    description=f"Prompt injection in hidden element: {desc}",
                                    evidence=hidden_text[:100],
                                )
                            )
                            break

        # Meta tags with suspicious content
        meta_tags = re.findall(
            r'<meta\s+[^>]*content\s*=\s*["\']([^"\']+)["\']', content, re.IGNORECASE
        )
        for meta_content in meta_tags:
            for name, pattern, weight, desc in _INJECTION_PATTERNS:
                if pattern.search(meta_content):
                    result.has_hidden_content = True
                    result.findings.append(
                        ContentFinding(
                            category="hidden_content",
                            severity=FindingSeverity.MEDIUM,
                            description=f"Prompt injection in meta tag: {desc}",
                            evidence=meta_content[:100],
                        )
                    )
                    break

    def _scan_encoded_payloads(self, content: str, result: ScanResult) -> None:
        """Scan for base64-encoded or otherwise obfuscated payloads."""
        # Find base64-looking strings
        b64_matches = re.findall(
            r'(?:atob|base64[_,]?decode|fromCharCode)\s*\(\s*["\']([A-Za-z0-9+/=]{20,})["\']',
            content,
            re.IGNORECASE,
        )
        for match in b64_matches:
            try:
                decoded = base64.b64decode(match).decode("utf-8", errors="replace")
                for name, pattern, weight, desc in _INJECTION_PATTERNS:
                    if pattern.search(decoded):
                        result.has_encoded_payload = True
                        result.findings.append(
                            ContentFinding(
                                category="encoded_payload",
                                severity=FindingSeverity.HIGH,
                                description=f"Base64-encoded prompt injection: {desc}",
                                evidence=decoded[:100],
                            )
                        )
                        break
            except Exception:
                pass

        # Standalone large base64 blocks
        standalone_b64 = re.findall(
            r"(?<![A-Za-z0-9+/=])([A-Za-z0-9+/]{50,}={0,2})(?![A-Za-z0-9+/=])", content
        )
        for match in standalone_b64:
            try:
                decoded = base64.b64decode(match).decode("utf-8", errors="replace")
                # Only flag if decoded content has injection patterns
                for name, pattern, weight, desc in _INJECTION_PATTERNS:
                    if pattern.search(decoded):
                        result.has_encoded_payload = True
                        result.findings.append(
                            ContentFinding(
                                category="encoded_payload",
                                severity=FindingSeverity.HIGH,
                                description=f"Hidden base64 payload with injection: {desc}",
                                evidence=decoded[:100],
                            )
                        )
                        break
            except Exception:
                pass

    def _scan_zero_width(self, content: str, result: ScanResult) -> None:
        """Detect zero-width character sequences (steganographic attacks)."""
        matches = _ZERO_WIDTH_PATTERN.finditer(content)
        for match in matches:
            zwc_seq = match.group(0)
            result.has_hidden_content = True
            result.findings.append(
                ContentFinding(
                    category="hidden_content",
                    severity=FindingSeverity.MEDIUM,
                    description="Zero-width character sequence detected (possible steganographic payload)",
                    evidence=f"length={len(zwc_seq)}, offset={match.start()}",
                )
            )
            break  # One finding is enough

    def _scan_pii(self, content: str, result: ScanResult) -> None:
        """Scan response content for PII."""
        for pii_type, pattern in _RESPONSE_PII_PATTERNS:
            matches = pattern.findall(content)
            if matches:
                result.has_pii = True
                result.findings.append(
                    ContentFinding(
                        category="pii",
                        severity=(
                            FindingSeverity.MEDIUM
                            if pii_type in ("email", "phone")
                            else FindingSeverity.HIGH
                        ),
                        description=f"PII detected in response: {pii_type}",
                        evidence=f"count={len(matches)}",
                    )
                )
