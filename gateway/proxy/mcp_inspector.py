# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""MCP Inspector — tool call inspection for injection, PII, and sensitive ops.

Design: log-and-allow for ambiguous cases, block only clear threats.
"""

from __future__ import annotations

import logging
import re
from copy import deepcopy
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Compiled patterns
# ---------------------------------------------------------------------------

_INJECTION_HIGH: List[re.Pattern] = [
    # Canonical ignore-instructions attacks
    re.compile(r"ignore\s+(?:all\s+)?(?:previous|prior|earlier)\s+instructions", re.I),
    re.compile(r"disregard\s+(?:all\s+)?(?:previous|prior)\s+instructions", re.I),
    # Identity/role override
    re.compile(
        r"you\s+are\s+now\s+(?:a\s+)?(?:different|new|another)\s+(?:ai|assistant|bot)",
        re.I,
    ),
    re.compile(r"you\s+(?:now\s+)?have\s+no\s+restrictions", re.I),
    # Fake system prompt (starts a line with "system:")
    re.compile(r"(?:^|[\r\n])system\s*:", re.I),
    # Special LLM control tokens
    re.compile(r"<\|[a-z_]+\|>"),
]

_SENSITIVE_OP: List[re.Pattern] = [
    # Shell execution patterns
    re.compile(r"(?:bash|sh|zsh|fish)\s+-c\b", re.I),
    re.compile(r"\brm\s+-[rf]{1,2}\s", re.I),
    # Network exfiltration
    re.compile(r"\bcurl\s+https?://", re.I),
    re.compile(r"\bwget\s+https?://", re.I),
]

_SSN = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
_CREDIT_CARD = re.compile(r"\b\d{16}\b|\b(?:\d{4}[-\s]){3}\d{4}\b")
_EMAIL = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")
_URL_ENCODED = re.compile(r"%[0-9A-Fa-f]{2}")

# Threshold for "suspicious large blob": any string token > 100 chars with no
# whitespace is flagged as possible base64 / binary payload.
_LARGE_BLOB_THRESHOLD = 100
_URL_ENCODING_COUNT_THRESHOLD = 10


# ---------------------------------------------------------------------------
# Enums and data classes
# ---------------------------------------------------------------------------


class ThreatLevel(Enum):
    """Threat level classification."""

    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class FindingType(Enum):
    """Type of security finding."""

    INJECTION = "injection"
    PII_LEAK = "pii_leak"
    SUSPICIOUS_ENCODING = "suspicious_encoding"
    SENSITIVE_OP = "sensitive_op"


@dataclass
class InspectionFinding:
    """A single finding from inspection."""

    finding_type: FindingType
    threat_level: ThreatLevel
    field_path: str
    description: str
    pattern_matched: Optional[str] = None
    matched_value: Optional[str] = None


@dataclass
class InspectionResult:
    """Result of inspecting a tool call or response."""

    blocked: bool
    block_reason: str
    findings: List[InspectionFinding] = field(default_factory=list)
    sanitized_params: Optional[Dict[str, Any]] = None
    sanitized_result: Optional[Any] = None
    threat_level: ThreatLevel = ThreatLevel.NONE

    @property
    def has_findings(self) -> bool:
        return len(self.findings) > 0

    @property
    def highest_threat(self) -> ThreatLevel:
        """Return the highest threat level from all findings."""
        if not self.findings:
            return ThreatLevel.NONE
        threat_order = {
            ThreatLevel.NONE: -1,
            ThreatLevel.LOW: 0,
            ThreatLevel.MEDIUM: 1,
            ThreatLevel.HIGH: 2,
        }
        return max(self.findings, key=lambda f: threat_order[f.threat_level]).threat_level


# ---------------------------------------------------------------------------
# Inspector
# ---------------------------------------------------------------------------


class MCPInspector:
    """Inspects MCP tool calls and responses for security threats."""

    def __init__(self, strict_mode: bool = False):
        self.strict_mode = strict_mode

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def inspect_tool_call(
        self,
        tool_name: str,
        params: Dict[str, Any],
        check_injection: bool = True,
        check_pii: bool = True,
        check_encoding: bool = True,
        check_sensitive: bool = True,
    ) -> InspectionResult:
        """Inspect an outgoing tool call for security threats."""
        findings: List[InspectionFinding] = []

        self._scan_value(
            params,
            "params",
            findings,
            check_injection,
            check_pii,
            check_encoding,
            check_sensitive,
        )

        sanitized_params = self._redact_pii(params) if check_pii else deepcopy(params)

        blocked, block_reason = self._should_block(findings)
        result = InspectionResult(
            blocked=blocked,
            block_reason=block_reason,
            findings=findings,
            sanitized_params=sanitized_params,
        )
        result.threat_level = result.highest_threat
        return result

    def inspect_tool_result(
        self,
        tool_name: str,
        result_content: Any,
        check_pii: bool = True,
        check_encoding: bool = True,
    ) -> InspectionResult:
        """Inspect a tool result for PII and encoding issues."""
        if result_content is None:
            result = InspectionResult(
                blocked=False,
                block_reason="",
                sanitized_result=None,
            )
            result.threat_level = ThreatLevel.NONE
            return result

        findings: List[InspectionFinding] = []
        self._scan_value(
            result_content,
            "result",
            findings,
            check_injection=False,
            check_pii=check_pii,
            check_encoding=check_encoding,
            check_sensitive=False,
        )

        sanitized = (
            self._redact_pii(result_content)
            if check_pii
            else (
                deepcopy(result_content)
                if isinstance(result_content, (dict, list))
                else result_content
            )
        )

        result = InspectionResult(
            blocked=False,  # results are never blocked, only redacted
            block_reason="",
            findings=findings,
            sanitized_result=sanitized,
        )
        result.threat_level = result.highest_threat
        return result

    # ------------------------------------------------------------------
    # Internal scanning
    # ------------------------------------------------------------------

    def _scan_value(
        self,
        value: Any,
        path: str,
        findings: List[InspectionFinding],
        check_injection: bool,
        check_pii: bool,
        check_encoding: bool,
        check_sensitive: bool,
    ) -> None:
        """Recursively scan a value, appending findings in-place."""
        if isinstance(value, str):
            self._scan_text(
                value,
                path,
                findings,
                check_injection,
                check_pii,
                check_encoding,
                check_sensitive,
            )
        elif isinstance(value, dict):
            for k, v in value.items():
                self._scan_value(
                    v,
                    f"{path}.{k}",
                    findings,
                    check_injection,
                    check_pii,
                    check_encoding,
                    check_sensitive,
                )
        elif isinstance(value, list):
            for i, item in enumerate(value):
                self._scan_value(
                    item,
                    f"{path}[{i}]",
                    findings,
                    check_injection,
                    check_pii,
                    check_encoding,
                    check_sensitive,
                )

    def _scan_text(
        self,
        text: str,
        path: str,
        findings: List[InspectionFinding],
        check_injection: bool,
        check_pii: bool,
        check_encoding: bool,
        check_sensitive: bool,
    ) -> None:
        """Scan a single string for all threat types."""
        if check_injection:
            for pattern in _INJECTION_HIGH:
                if pattern.search(text):
                    findings.append(
                        InspectionFinding(
                            finding_type=FindingType.INJECTION,
                            threat_level=ThreatLevel.HIGH,
                            field_path=path,
                            description="Prompt injection pattern detected",
                            matched_value=FindingType.INJECTION.value,
                        )
                    )
                    break  # one injection finding per field

        if check_pii:
            for match in _SSN.finditer(text):
                findings.append(
                    InspectionFinding(
                        finding_type=FindingType.PII_LEAK,
                        threat_level=ThreatLevel.HIGH,
                        field_path=path,
                        description="Social Security Number detected",
                        matched_value="US_SSN",
                    )
                )

            for match in _CREDIT_CARD.finditer(text):
                # Avoid re-matching SSNs captured as 16-digit sequences
                raw = match.group(0).replace("-", "").replace(" ", "")
                if len(raw) == 16:
                    findings.append(
                        InspectionFinding(
                            finding_type=FindingType.PII_LEAK,
                            threat_level=ThreatLevel.HIGH,
                            field_path=path,
                            description="Credit card number detected",
                            matched_value="CREDIT_CARD",
                        )
                    )

            for match in _EMAIL.finditer(text):
                findings.append(
                    InspectionFinding(
                        finding_type=FindingType.PII_LEAK,
                        threat_level=ThreatLevel.LOW,
                        field_path=path,
                        description="Email address detected",
                        matched_value="EMAIL",
                    )
                )

        if check_encoding:
            # Large opaque blob (potential base64 payload)
            if len(text) > _LARGE_BLOB_THRESHOLD and not re.search(
                r"\s", text[:_LARGE_BLOB_THRESHOLD]
            ):
                findings.append(
                    InspectionFinding(
                        finding_type=FindingType.SUSPICIOUS_ENCODING,
                        threat_level=ThreatLevel.MEDIUM,
                        field_path=path,
                        description="Suspicious large opaque payload detected",
                    )
                )

            # Heavy URL encoding
            url_enc_count = len(_URL_ENCODED.findall(text))
            if url_enc_count >= _URL_ENCODING_COUNT_THRESHOLD:
                findings.append(
                    InspectionFinding(
                        finding_type=FindingType.SUSPICIOUS_ENCODING,
                        threat_level=ThreatLevel.MEDIUM,
                        field_path=path,
                        description=f"Heavy URL encoding detected ({url_enc_count} sequences)",
                    )
                )

        if check_sensitive:
            for pattern in _SENSITIVE_OP:
                if pattern.search(text):
                    findings.append(
                        InspectionFinding(
                            finding_type=FindingType.SENSITIVE_OP,
                            threat_level=ThreatLevel.MEDIUM,
                            field_path=path,
                            description="Potentially sensitive operation pattern detected",
                        )
                    )
                    break  # one sensitive-op finding per field

    # ------------------------------------------------------------------
    # Redaction
    # ------------------------------------------------------------------

    def _redact_pii(self, value: Any) -> Any:
        """Recursively redact HIGH-severity PII from a value."""
        if isinstance(value, str):
            value = _SSN.sub("REDACTED_SSN", value)
            value = _CREDIT_CARD.sub(
                lambda m: (
                    "REDACTED_CC"
                    if len(m.group(0).replace("-", "").replace(" ", "")) == 16
                    else m.group(0)
                ),
                value,
            )
            # Emails (LOW threat) are NOT redacted
            return value
        elif isinstance(value, dict):
            return {k: self._redact_pii(v) for k, v in value.items()}
        elif isinstance(value, list):
            return [self._redact_pii(item) for item in value]
        else:
            return value

    # ------------------------------------------------------------------
    # Blocking decision
    # ------------------------------------------------------------------

    def _should_block(self, findings: List[InspectionFinding]) -> tuple[bool, str]:
        """Decide whether to block based on findings and mode."""
        if self.strict_mode:
            high = [f for f in findings if f.threat_level == ThreatLevel.HIGH]
            if high:
                types = ", ".join(sorted({f.finding_type.value for f in high}))
                return True, f"Blocked in strict mode: HIGH {types}"
            return False, ""

        # Default mode: only HIGH injection blocks
        injections = [
            f
            for f in findings
            if f.finding_type == FindingType.INJECTION and f.threat_level == ThreatLevel.HIGH
        ]
        if injections:
            return True, "injection detected"
        return False, ""
