# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Output Schema Enforcement — C25

Validates and sanitizes outbound agent responses against structural rules.

Default schema enforces:
  - max 100 000 characters
  - no raw JSON tool call payloads
  - no base64 blocks > 1 KB
  - no raw absolute file paths

Custom schemas can be registered per-context via register_schema().
"""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional

logger = logging.getLogger("agentshroud.security.output_schema")

# Pre-compiled patterns for the default schema
_RAW_TOOL_PAYLOAD = re.compile(
    r'"tool_name"\s*:\s*"[^"]*"|"function"\s*:\s*\{.*?"name"\s*:\s*"[^"]*"',
    re.IGNORECASE | re.DOTALL,
)
_LARGE_BASE64 = re.compile(
    r"[A-Za-z0-9+/]{1370,}={0,2}"  # 1370 chars ≈ 1 KB decoded
)
_RAW_FILE_PATH = re.compile(
    r"(?:/(?:Users|home|app|tmp|var|etc|root)/[^\s]{3,}|[A-Z]:\\[^\s]{3,})"
)


@dataclass
class SchemaRule:
    """Definition for a named output schema."""
    name: str
    max_length: int = 100_000
    forbidden_patterns: List[re.Pattern] = field(default_factory=list)
    required_fields: List[str] = field(default_factory=list)
    content_type: str = "text"


@dataclass
class SchemaValidationResult:
    """Result of validating output against a schema."""
    valid: bool
    violations: List[str]
    sanitized_output: str


class OutputSchemaEnforcer:
    """Validates outbound responses against structural schemas.

    Usage::

        enforcer = OutputSchemaEnforcer()
        result = enforcer.validate(response_text)
        if not result.valid:
            logger.warning("Output violations: %s", result.violations)
    """

    def __init__(self) -> None:
        self._schemas: Dict[str, SchemaRule] = {}
        self._register_default_schema()

    def _register_default_schema(self) -> None:
        """Register the built-in default schema."""
        self._schemas["default"] = SchemaRule(
            name="default",
            max_length=100_000,
            forbidden_patterns=[
                _RAW_TOOL_PAYLOAD,
                _LARGE_BASE64,
                _RAW_FILE_PATH,
            ],
            content_type="text",
        )

    def register_schema(self, name: str, rule: SchemaRule) -> None:
        """Register or replace a named schema."""
        self._schemas[name] = rule
        logger.debug("OutputSchemaEnforcer: registered schema %r", name)

    def validate(
        self, output: str, schema_name: str = "default"
    ) -> SchemaValidationResult:
        """Validate output against the named schema.

        Args:
            output: The agent response text to validate.
            schema_name: Which schema to validate against (default: "default").

        Returns:
            SchemaValidationResult.  sanitized_output has violations removed.
        """
        rule = self._schemas.get(schema_name, self._schemas["default"])
        violations: List[str] = []
        sanitized = output

        # Length check
        if len(output) > rule.max_length:
            violations.append(
                f"output_too_long:{len(output)}>{rule.max_length}"
            )
            sanitized = sanitized[: rule.max_length]
            logger.warning(
                "OutputSchema '%s': response trimmed %d -> %d chars",
                schema_name, len(output), rule.max_length,
            )

        # Forbidden pattern checks
        for pat in rule.forbidden_patterns:
            matches = pat.findall(sanitized)
            if matches:
                violations.append(f"forbidden_pattern:{pat.pattern[:60]}")
                sanitized = pat.sub("[SCHEMA_REDACTED]", sanitized)

        return SchemaValidationResult(
            valid=len(violations) == 0,
            violations=violations,
            sanitized_output=sanitized,
        )
