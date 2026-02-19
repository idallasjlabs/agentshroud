"""MCP Inspector — tool call inspection for injection, PII, and sensitive ops.

Design: log-and-allow for ambiguous cases, block only clear threats.
"""

import base64
import logging
import re
import unicodedata
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Optional
from urllib.parse import unquote

logger = logging.getLogger("secureclaw.proxy.mcp_inspector")


class ThreatLevel(str, Enum):
    NONE = "none"
    LOW = "low"        # Logged, allowed
    MEDIUM = "medium"  # Logged, allowed with warning
    HIGH = "high"      # Blocked


class FindingType(str, Enum):
    INJECTION = "injection"
    PII_LEAK = "pii_leak"
    SENSITIVE_OP = "sensitive_operation"
    SUSPICIOUS_ENCODING = "suspicious_encoding"
    DATA_EXFILTRATION = "data_exfiltration"


@dataclass
class InspectionFinding:
    """A single finding from inspection."""
    finding_type: FindingType
    threat_level: ThreatLevel
    description: str
    field_path: str = ""  # e.g. "params.query" or "result.content"
    matched_value: str = ""  # Redacted snippet of what was found


@dataclass
class InspectionResult:
    """Result of inspecting a tool call or response."""
    blocked: bool = False
    block_reason: str = ""
    findings: list[InspectionFinding] = field(default_factory=list)
    sanitized_params: Optional[dict[str, Any]] = None
    sanitized_result: Optional[Any] = None
    threat_level: ThreatLevel = ThreatLevel.NONE

    @property
    def has_findings(self) -> bool:
        return len(self.findings) > 0

    @property
    def highest_threat(self) -> ThreatLevel:
        if not self.findings:
            return ThreatLevel.NONE
        levels = [ThreatLevel.NONE, ThreatLevel.LOW, ThreatLevel.MEDIUM, ThreatLevel.HIGH]
        return max(self.findings, key=lambda f: levels.index(f.threat_level)).threat_level


# === Injection patterns (only HIGH confidence ones block) ===

# Prompt injection patterns — these are clear attacks
INJECTION_PATTERNS_HIGH: list[tuple[str, str]] = [
    (r"ignore\s+(all\s+)?previous\s+instructions", "prompt override attempt"),
    (r"you\s+are\s+now\s+(?:a\s+)?(?:different|new)\s+(?:ai|assistant|bot)", "identity override"),
    (r"system\s*:\s*you\s+(?:are|must|should|will)", "fake system prompt"),
    (r"<\|(?:im_start|system|endoftext)\|>", "special token injection"),
    (r"\bDAN\b.*\bjailbreak\b", "jailbreak attempt"),
]

# Lower confidence — log but allow
INJECTION_PATTERNS_LOW: list[tuple[str, str]] = [
    (r"(?:forget|disregard)\s+(?:your|all|the)\s+(?:rules|instructions|guidelines)", "instruction override attempt"),
    (r"pretend\s+(?:you\s+are|to\s+be)\s+", "role override attempt"),
]

# === PII patterns ===

PII_PATTERNS: list[tuple[str, str, str]] = [
    (r"\b\d{3}-\d{2}-\d{4}\b", "SSN", "US Social Security Number"),
    (r"\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13})\b", "CREDIT_CARD", "Credit card number"),
    (r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "EMAIL", "Email address"),
]

# SSN and credit cards are always redacted; emails are logged but allowed
PII_REDACT_TYPES = {"SSN", "CREDIT_CARD"}

# === Sensitive operation patterns ===

SENSITIVE_TOOL_PATTERNS: list[tuple[str, str]] = [
    (r"(?:shell|bash|exec|command|terminal|run)", "shell execution"),
    (r"(?:rm\s|unlink|delete|remove|drop|truncate)", "destructive operation"),
    (r"(?:curl|wget|fetch|http|request)\s", "network request"),
    (r"(?:chmod|chown|sudo|su\s)", "privilege escalation"),
]


class MCPInspector:
    """Inspects MCP tool calls and responses for security threats.
    
    Philosophy: block clear attacks, log ambiguous signals, allow everything else.
    """

    def __init__(self, strict_mode: bool = False):
        """
        Args:
            strict_mode: If True, MEDIUM findings also block. Default False (log-and-allow).
        """
        self.strict_mode = strict_mode
        self._compiled_high = [(re.compile(p, re.IGNORECASE), d) for p, d in INJECTION_PATTERNS_HIGH]
        self._compiled_low = [(re.compile(p, re.IGNORECASE), d) for p, d in INJECTION_PATTERNS_LOW]
        self._compiled_pii = [(re.compile(p), t, d) for p, t, d in PII_PATTERNS]
        self._compiled_sensitive = [(re.compile(p, re.IGNORECASE), d) for p, d in SENSITIVE_TOOL_PATTERNS]

    def _extract_strings(self, obj: Any, path: str = "") -> list[tuple[str, str]]:
        """Recursively extract all string values from nested dicts/lists."""
        results = []
        if isinstance(obj, str):
            results.append((obj, path))
        elif isinstance(obj, dict):
            for k, v in obj.items():
                results.extend(self._extract_strings(v, f"{path}.{k}" if path else k))
        elif isinstance(obj, (list, tuple)):
            for i, v in enumerate(obj):
                results.extend(self._extract_strings(v, f"{path}[{i}]"))
        return results

    @staticmethod
    def _normalize_unicode(text: str) -> str:
        """Normalize Unicode homoglyphs to ASCII for pattern matching.
        
        Converts confusable characters (Cyrillic а→a, fullwidth Ａ→A, etc.)
        to their ASCII equivalents so injection patterns can't be bypassed
        by substituting look-alike characters.
        """
        # NFKC normalization maps fullwidth, compatibility, and many
        # confusable code points to their canonical forms.
        return unicodedata.normalize('NFKC', text)

    @staticmethod
    def _decode_layers(text: str, max_depth: int = 3) -> list[str]:
        """Decode base64 and URL-encoded layers to catch hidden payloads.
        
        Returns list of decoded versions (including original).
        """
        results = [text]
        current = text
        for _ in range(max_depth):
            decoded_any = False

            # Try URL decoding
            url_decoded = unquote(current)
            if url_decoded != current:
                results.append(url_decoded)
                current = url_decoded
                decoded_any = True
                continue

            # Try base64 decoding
            try:
                # Only attempt if it looks like base64
                stripped = current.strip()
                if len(stripped) >= 20 and re.match(r'^[A-Za-z0-9+/=_-]+$', stripped):
                    padded = stripped + '=' * (-len(stripped) % 4)
                    raw = base64.b64decode(padded, validate=True)
                    decoded_str = raw.decode('utf-8', errors='strict')
                    # Only keep if it produced printable text
                    if decoded_str.isprintable() or chr(10) in decoded_str:
                        results.append(decoded_str)
                        current = decoded_str
                        decoded_any = True
                        continue
            except Exception:
                pass

            if not decoded_any:
                break

        return results

    def _check_injection(self, text: str, field_path: str) -> list[InspectionFinding]:
        """Check text for prompt injection patterns.
        
        Normalizes Unicode homoglyphs and decodes base64/URL-encoded layers
        before pattern matching to prevent bypass via encoding tricks.
        """
        findings = []
        # Build list of text variants to check
        normalized = self._normalize_unicode(text)
        variants = set()
        for t in [text, normalized]:
            for decoded in self._decode_layers(t):
                variants.add(decoded)
                variants.add(self._normalize_unicode(decoded))

        for variant in variants:
            for pattern, desc in self._compiled_high:
                if pattern.search(variant):
                    findings.append(InspectionFinding(
                        finding_type=FindingType.INJECTION,
                        threat_level=ThreatLevel.HIGH,
                        description=f"Prompt injection: {desc}",
                        field_path=field_path,
                        matched_value=text[:100] + "..." if len(text) > 100 else text,
                    ))
                    break  # One match per pattern is enough
            for pattern, desc in self._compiled_low:
                if pattern.search(variant):
                    findings.append(InspectionFinding(
                        finding_type=FindingType.INJECTION,
                        threat_level=ThreatLevel.LOW,
                        description=f"Possible injection: {desc}",
                        field_path=field_path,
                        matched_value=text[:100] + "..." if len(text) > 100 else text,
                    ))
                    break  # One match per pattern is enough

        # Deduplicate findings by description
        seen = set()
        unique = []
        for f in findings:
            if f.description not in seen:
                seen.add(f.description)
                unique.append(f)
        return unique

    def _check_pii(self, text: str, field_path: str) -> list[InspectionFinding]:
        """Check text for PII patterns."""
        findings = []
        for pattern, pii_type, desc in self._compiled_pii:
            matches = pattern.findall(text)
            if matches:
                threat = ThreatLevel.HIGH if pii_type in PII_REDACT_TYPES else ThreatLevel.LOW
                findings.append(InspectionFinding(
                    finding_type=FindingType.PII_LEAK,
                    threat_level=threat,
                    description=f"PII detected: {desc}",
                    field_path=field_path,
                    matched_value=f"[{pii_type}]",
                ))
        return findings

    def _check_suspicious_encoding(self, text: str, field_path: str) -> list[InspectionFinding]:
        """Check for suspicious encoded content."""
        findings = []
        # Large base64 blobs (>200 chars) are suspicious
        b64_pattern = re.compile(r"[A-Za-z0-9+/]{200,}={0,2}")
        if b64_pattern.search(text):
            findings.append(InspectionFinding(
                finding_type=FindingType.SUSPICIOUS_ENCODING,
                threat_level=ThreatLevel.LOW,
                description="Large base64 encoded content detected",
                field_path=field_path,
                matched_value="[base64 blob]",
            ))
        # Percent-encoded strings that might hide payloads
        pct_pattern = re.compile(r"(?:%[0-9A-Fa-f]{2}){10,}")
        if pct_pattern.search(text):
            findings.append(InspectionFinding(
                finding_type=FindingType.SUSPICIOUS_ENCODING,
                threat_level=ThreatLevel.LOW,
                description="Heavy URL encoding detected",
                field_path=field_path,
                matched_value="[encoded content]",
            ))
        return findings

    def _check_sensitive_ops(self, text: str, field_path: str) -> list[InspectionFinding]:
        """Check for sensitive operations in tool parameters."""
        findings = []
        for pattern, desc in self._compiled_sensitive:
            if pattern.search(text):
                findings.append(InspectionFinding(
                    finding_type=FindingType.SENSITIVE_OP,
                    threat_level=ThreatLevel.MEDIUM,
                    description=f"Sensitive operation: {desc}",
                    field_path=field_path,
                    matched_value=text[:100] + "..." if len(text) > 100 else text,
                ))
        return findings

    def _redact_pii_in_text(self, text: str) -> str:
        """Redact high-severity PII from text."""
        result = text
        for pattern, pii_type, _ in self._compiled_pii:
            if pii_type in PII_REDACT_TYPES:
                result = pattern.sub(f"[REDACTED_{pii_type}]", result)
        return result

    def _redact_pii_in_obj(self, obj: Any) -> Any:
        """Recursively redact PII in nested structures."""
        if isinstance(obj, str):
            return self._redact_pii_in_text(obj)
        elif isinstance(obj, dict):
            return {k: self._redact_pii_in_obj(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._redact_pii_in_obj(v) for v in obj]
        return obj

    def inspect_tool_call(
        self,
        tool_name: str,
        params: dict[str, Any],
        check_injection: bool = True,
        check_pii: bool = True,
        check_encoding: bool = True,
        check_sensitive: bool = True,
    ) -> InspectionResult:
        """Inspect an outgoing tool call (params heading to MCP server).
        
        Returns InspectionResult with findings and optionally sanitized params.
        Only blocks on HIGH threat findings (unless strict_mode).
        """
        findings: list[InspectionFinding] = []
        strings = self._extract_strings(params, "params")
        # Also inspect the tool name itself
        strings.append((tool_name, "tool_name"))

        for text, path in strings:
            if check_injection:
                findings.extend(self._check_injection(text, path))
            if check_pii:
                findings.extend(self._check_pii(text, path))
            if check_encoding:
                findings.extend(self._check_suspicious_encoding(text, path))
            if check_sensitive:
                findings.extend(self._check_sensitive_ops(text, path))

        # Cross-parameter PII check: concatenate all param values to catch
        # PII split across multiple fields (e.g., SSN digits in separate params)
        if check_pii and len(strings) > 1:
            concatenated = " ".join(s for s, _ in strings if s != tool_name)
            cross_findings = self._check_pii(concatenated, "params[concatenated]")
            # Only add findings we didn't already catch in individual fields
            existing_descs = {f.description for f in findings}
            for cf in cross_findings:
                if cf.description not in existing_descs:
                    cf.field_path = "params[cross-field]"
                    findings.append(cf)

        # Determine if we should block
        block_threshold = ThreatLevel.MEDIUM if self.strict_mode else ThreatLevel.HIGH
        block_findings = [
            f for f in findings
            if f.threat_level == ThreatLevel.HIGH or
            (self.strict_mode and f.threat_level == ThreatLevel.MEDIUM)
        ]
        # Only block for injection findings at HIGH level
        injection_blocks = [f for f in block_findings if f.finding_type == FindingType.INJECTION]

        blocked = len(injection_blocks) > 0
        block_reason = injection_blocks[0].description if injection_blocks else ""

        # Sanitize PII in params (redact SSN/CC even if allowing)
        sanitized = self._redact_pii_in_obj(params) if check_pii else params

        result = InspectionResult(
            blocked=blocked,
            block_reason=block_reason,
            findings=findings,
            sanitized_params=sanitized,
        )
        result.threat_level = result.highest_threat
        return result

    def inspect_tool_result(
        self,
        tool_name: str,
        result_data: Any,
        check_pii: bool = True,
        check_encoding: bool = True,
    ) -> InspectionResult:
        """Inspect a tool result coming back from an MCP server.
        
        Focus: PII leakage and suspicious encoding in responses.
        We do NOT block responses (the call already happened) — we redact and log.
        """
        findings: list[InspectionFinding] = []
        strings = self._extract_strings(result_data, "result")

        for text, path in strings:
            if check_pii:
                findings.extend(self._check_pii(text, path))
            if check_encoding:
                findings.extend(self._check_suspicious_encoding(text, path))

        sanitized = self._redact_pii_in_obj(result_data) if check_pii else result_data

        result = InspectionResult(
            blocked=False,  # Never block responses, just redact
            findings=findings,
            sanitized_result=sanitized,
        )
        result.threat_level = result.highest_threat
        return result
