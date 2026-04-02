# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Tool Result Injection Scanner — detect and neutralize prompt injection attempts in tool results.

This scanner protects against indirect prompt injection attacks where malicious instructions
are embedded in web pages, emails, or other tool results that the agent processes.
"""

from __future__ import annotations

import base64
import re
import unicodedata
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Tuple

from gateway.security.input_normalizer import normalize_input, strip_markdown_exfil


class InjectionSeverity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class InjectionAction(str, Enum):
    STRIP = "strip"  # Remove injected content completely
    WARN = "warn"  # Flag and warn but pass through with warning
    LOG = "log"  # Log only, pass through unchanged


@dataclass
class InjectionResult:
    """Result from tool result injection scan."""

    severity: InjectionSeverity
    action: InjectionAction
    patterns: List[str]
    sanitized_content: str
    warning_message: Optional[str] = None


@dataclass
class InjectionRule:
    """Rule for detecting injection patterns in tool results."""

    name: str
    pattern: re.Pattern
    severity: InjectionSeverity
    description: str = ""


# Precompiled injection rules adapted for tool result context
_TOOL_INJECTION_PATTERNS: List[InjectionRule] = [
    # High severity - definite injection attempts
    InjectionRule(
        "ignore_instructions",
        re.compile(
            r"ignore\s+(all\s+)?(previous|prior|above|earlier)\s+(instructions|prompts|rules|context|directives)",
            re.IGNORECASE,
        ),
        severity=InjectionSeverity.HIGH,
        description="Instruction override attempt in tool result",
    ),
    InjectionRule(
        "role_reassignment",
        re.compile(
            r"(you\s+are\s+now|act\s+as\s+(if\s+you\s+are\s+)?|pretend\s+(to\s+be|you\s+are)|from\s+now\s+on\s+you\s+are|roleplay\s+as)\s+(?!.*part of)",
            re.IGNORECASE,
        ),
        severity=InjectionSeverity.HIGH,
        description="Role reassignment attempt",
    ),
    InjectionRule(
        "new_instructions",
        re.compile(
            r"(new\s+instructions?|override\s+(instructions?|rules)|forget\s+(everything|all|your\s+(instructions|rules|prompt)))",
            re.IGNORECASE,
        ),
        severity=InjectionSeverity.HIGH,
        description="New instruction injection",
    ),
    InjectionRule(
        "xml_function_injection",
        re.compile(
            r"<\s*/?antml:function_calls\s*>|<\s*/?function_calls\s*>|<\s*/?antml:invoke\s*>|<\s*/?invoke\s*>",
            re.IGNORECASE,
        ),
        severity=InjectionSeverity.HIGH,
        description="XML function call injection",
    ),
    InjectionRule(
        "system_delimiter_injection",
        re.compile(
            r"</s>|\[INST\]|\[/INST\]|\[SYS\]|\[/SYS\]|###\s*END|---\s*END\s*---",
            re.IGNORECASE,
        ),
        severity=InjectionSeverity.HIGH,
        description="System delimiter injection",
    ),
    InjectionRule(
        "social_engineering_admin",
        re.compile(
            r"(the\s+developer\s+says|admin\s+override|maintenance\s+mode|system\s+administrator\s+(says|requires|requests))",
            re.IGNORECASE,
        ),
        severity=InjectionSeverity.HIGH,
        description="Social engineering with admin authority",
    ),
    # Medium severity - likely injection attempts
    InjectionRule(
        "prompt_extraction",
        re.compile(
            r"(repeat|show|display|print|output|reveal|tell\s+me)\s+(your\s+)?(system\s+prompt|initial\s+prompt|instructions|system\s+message|hidden\s+prompt)",
            re.IGNORECASE,
        ),
        severity=InjectionSeverity.MEDIUM,
        description="System prompt extraction attempt",
    ),
    InjectionRule(
        "jailbreak_attempt",
        re.compile(
            r"(DAN\s+mode|do\s+anything\s+now|jailbreak|developer\s+mode\s+(enabled|on)|DUDE\s+mode|unrestricted)",
            re.IGNORECASE,
        ),
        severity=InjectionSeverity.MEDIUM,
        description="Jailbreak attempt",
    ),
    InjectionRule(
        "xml_system_tag",
        re.compile(
            r"<\s*(system_prompt|sys|SYSTEM|instructions?)\s*>.*?</\s*(system_prompt|sys|SYSTEM|instructions?)\s*>",
            re.IGNORECASE | re.DOTALL,
        ),
        severity=InjectionSeverity.MEDIUM,
        description="XML system tag injection",
    ),
    InjectionRule(
        "delimiter_code_injection",
        re.compile(
            r"```\s*(system|assistant|user|instruction)\s*\n.*?```",
            re.IGNORECASE | re.DOTALL,
        ),
        severity=InjectionSeverity.MEDIUM,
        description="Code block delimiter injection",
    ),
    # Low severity - suspicious patterns worth logging
    InjectionRule(
        "prompt_leak_attempt",
        re.compile(
            r"(what\s+(are|is)\s+your\s+(system\s+)?(instructions|prompt|rules)|beginning\s+of\s+(the\s+)?conversation)",
            re.IGNORECASE,
        ),
        severity=InjectionSeverity.LOW,
        description="Potential prompt leak attempt",
    ),
    InjectionRule(
        "instruction_context_switch",
        re.compile(
            r"(IMPORTANT\s*:\s*ignore|ATTENTION\s*:\s*new\s+instructions|NOTE\s+TO\s+(AI|ASSISTANT|MODEL))",
            re.IGNORECASE,
        ),
        severity=InjectionSeverity.LOW,
        description="Context switching attempt",
    ),
]


class ToolResultInjectionScanner:
    """Scanner for detecting prompt injection in tool results."""

    def __init__(self, custom_rules: Optional[List[InjectionRule]] = None):
        """
        Initialize the scanner with optional custom rules.

        Args:
            custom_rules: Additional injection rules to include in scanning.
        """
        self.rules = list(_TOOL_INJECTION_PATTERNS)
        if custom_rules:
            self.rules.extend(custom_rules)

    def _detect_encoded_injection(self, content: str) -> List[Tuple[str, InjectionSeverity]]:
        """Check for base64 or hex encoded injection attempts."""
        findings = []

        # Base64 detection
        b64_re = re.compile(r"[A-Za-z0-9+/]{20,}={0,2}")
        for match in b64_re.finditer(content):
            try:
                decoded = base64.b64decode(match.group()).decode("utf-8", errors="ignore")
                # Check for injection patterns in decoded content
                for rule in self.rules[:6]:  # Check top-severity patterns only
                    if rule.pattern.search(decoded):
                        findings.append((f"encoded_{rule.name}", InjectionSeverity.HIGH))
                        break
            except Exception:
                continue

        # Hex detection
        hex_re = re.compile(r"(?:0x)?[0-9a-fA-F]{20,}", re.IGNORECASE)
        for match in hex_re.finditer(content):
            try:
                hex_str = match.group().replace("0x", "")
                if len(hex_str) % 2 == 0:
                    decoded = bytes.fromhex(hex_str).decode("utf-8", errors="ignore")
                    # Check for injection patterns in decoded content
                    for rule in self.rules[:6]:  # Check top-severity patterns only
                        if rule.pattern.search(decoded):
                            findings.append((f"hex_{rule.name}", InjectionSeverity.HIGH))
                            break
            except Exception:
                continue

        return findings

    def _detect_unicode_obfuscation(self, content: str) -> List[Tuple[str, InjectionSeverity]]:
        """Detect unicode-based obfuscation techniques."""
        findings = []

        # Zero-width characters
        if re.search(r"[\u200b\u200c\u200d\u2060\ufeff]", content):
            findings.append(("zero_width_obfuscation", InjectionSeverity.MEDIUM))

        # Right-to-left override
        if "\u202e" in content or "\u200f" in content:
            findings.append(("rtl_obfuscation", InjectionSeverity.MEDIUM))

        # Homoglyph detection (mixing scripts)
        if re.search(r"[\u0400-\u04FF]", content) and re.search(r"[a-zA-Z]", content):
            findings.append(("homoglyph_obfuscation", InjectionSeverity.MEDIUM))

        # Fullwidth characters
        if re.search(r"[！-～]", content):
            findings.append(("fullwidth_obfuscation", InjectionSeverity.LOW))

        return findings

    def scan_tool_result(self, tool_name: str, result_content: str) -> InjectionResult:
        """
        Scan tool result content for injection attempts.

        Args:
            tool_name: Name of the tool that produced the result
            result_content: The content returned by the tool

        Returns:
            InjectionResult with detected patterns and sanitized content
        """

        # Normalize to defeat encoding evasion
        result_content = normalize_input(result_content)

        # Strip markdown exfiltration attempts from tool output
        result_content = strip_markdown_exfil(result_content)

        if not result_content or not result_content.strip():
            return InjectionResult(
                severity=InjectionSeverity.LOW,
                action=InjectionAction.LOG,
                patterns=[],
                sanitized_content=result_content or "",
            )

        # Normalize unicode to defeat obfuscation
        normalized_content = unicodedata.normalize("NFKC", result_content)
        # Strip zero-width characters for pattern matching
        stripped_content = re.sub(r"[\u200b\u200c\u200d\u2060\ufeff]", "", normalized_content)

        matched_patterns = []
        max_severity = InjectionSeverity.LOW

        # Pattern matching
        for rule in self.rules:
            if rule.pattern.search(stripped_content):
                matched_patterns.append(rule.name)
                if rule.severity.value == "high":
                    max_severity = InjectionSeverity.HIGH
                elif rule.severity.value == "medium" and max_severity.value != "high":
                    max_severity = InjectionSeverity.MEDIUM

        # Encoded content check
        for pattern_name, severity in self._detect_encoded_injection(result_content):
            matched_patterns.append(pattern_name)
            if severity.value == "high":
                max_severity = InjectionSeverity.HIGH
            elif severity.value == "medium" and max_severity.value != "high":
                max_severity = InjectionSeverity.MEDIUM

        # Unicode obfuscation check
        for pattern_name, severity in self._detect_unicode_obfuscation(result_content):
            matched_patterns.append(pattern_name)
            if severity.value == "high":
                max_severity = InjectionSeverity.HIGH
            elif severity.value == "medium" and max_severity.value != "high":
                max_severity = InjectionSeverity.MEDIUM

        # Determine action based on severity
        if max_severity == InjectionSeverity.HIGH:
            action = InjectionAction.STRIP
        elif max_severity == InjectionSeverity.MEDIUM:
            action = InjectionAction.WARN
        else:
            action = InjectionAction.LOG

        # Create sanitized content
        sanitized_content = result_content
        warning_message = None

        if action == InjectionAction.STRIP:
            # Strip detected injection patterns
            sanitized_content = result_content
            for rule in self.rules:
                sanitized_content = rule.pattern.sub("[CONTENT_FILTERED]", sanitized_content)
            # Also remove encoded content that might contain injections
            sanitized_content = re.sub(
                r"[A-Za-z0-9+/]{20,}={0,2}", "[BASE64_FILTERED]", sanitized_content
            )
            warning_message = f"[AGENTSHROUD SECURITY] Malicious content detected and filtered from {tool_name} result. Patterns: {', '.join(matched_patterns)}"

        elif action == InjectionAction.WARN:
            warning_message = f"[AGENTSHROUD SECURITY WARNING] Suspicious content detected in {tool_name} result. Exercise caution. Patterns: {', '.join(matched_patterns)}"
            # Prepend warning to content
            sanitized_content = f"{warning_message}\n\n{result_content}"

        return InjectionResult(
            severity=max_severity,
            action=action,
            patterns=matched_patterns,
            sanitized_content=sanitized_content,
            warning_message=warning_message,
        )
