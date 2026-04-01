# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Consent Framework Module - Pre-configuration consent for MCP server installations.

Validates server configs before execution, blocks malicious startup commands,
and provides whitelist/blacklist management for known-safe/dangerous patterns.

References:
    - Maloyan & Namiot 2026 (arXiv:2601.17548) - MCP security analysis
    - Chen et al. 2026 (arXiv:2602.14364) - Agent configuration vulnerabilities
"""
from __future__ import annotations


import re
import time
from dataclasses import dataclass, field
from typing import List, Optional, Dict


class ConfigValidationError(Exception):
    # TODO(v1.1.0): implement
    pass


class ShellInjectionDetected(ConfigValidationError):
    # TODO(v1.1.0): implement
    pass


@dataclass
class ServerConfig:
    name: str
    command: str
    args: List[str] = field(default_factory=list)
    env: Optional[Dict[str, str]] = None


@dataclass
class ConsentDecision:
    approved: bool
    reason: str
    timestamp: float = field(default_factory=time.time)
    warnings: List[str] = field(default_factory=list)


# Patterns that indicate shell injection attempts
_DANGEROUS_PATTERNS = [
    re.compile(r"curl\s+.+\|\s*(sh|bash)", re.I),
    re.compile(r"wget\s+.+&&", re.I),
    re.compile(r"rm\s+-rf\s+/", re.I),
    re.compile(r"\|\s*nc\s+", re.I),
    re.compile(r"`[^`]+`"),
    re.compile(r"\$\([^)]+\)"),
    re.compile(r"\|\s*(sh|bash)\b", re.I),
    re.compile(r"eval\s+", re.I),
    re.compile(r"base64\s+-d", re.I),
    re.compile(r"powershell", re.I),
    re.compile(r"curl\s+https?://\S+\s+\|", re.I),
]

# Patterns suggesting secrets in env values
_SECRET_PATTERNS = [
    re.compile(r"^sk-[a-zA-Z0-9]{10,}"),
    re.compile(r"^(ghp|gho|ghu|ghs|ghr)_[a-zA-Z0-9]{20,}"),
    re.compile(r"^[a-zA-Z0-9/+=]{40,}$"),
]


class ConsentFramework:
    def __init__(self):
        self._whitelist: set = set()
        self._blacklist: set = set()

    def add_to_whitelist(self, command: str):
        self._whitelist.add(command)

    def remove_from_whitelist(self, command: str):
        self._whitelist.discard(command)

    def get_whitelist(self) -> set:
        return set(self._whitelist)

    def add_to_blacklist(self, command: str):
        self._blacklist.add(command)

    def remove_from_blacklist(self, command: str):
        self._blacklist.discard(command)

    def get_blacklist(self) -> set:
        return set(self._blacklist)

    def validate_config(self, config: ServerConfig) -> ConsentDecision:
        """Validate a server configuration before execution."""
        if not config.command:
            return ConsentDecision(approved=False, reason="empty command")

        # Check blacklist first
        if config.command in self._blacklist:
            return ConsentDecision(approved=False, reason="blacklisted")

        # Check for shell injection in args
        full_args = " ".join(config.args)
        for pattern in _DANGEROUS_PATTERNS:
            if pattern.search(full_args) or pattern.search(config.command):
                raise ShellInjectionDetected(
                    f"Dangerous pattern detected: {pattern.pattern}"
                )

        # Check whitelist
        if config.command in self._whitelist:
            return ConsentDecision(approved=True, reason="whitelisted")

        # Check environment variables
        warnings = []
        if config.env:
            for key, value in config.env.items():
                if key.upper() == "PATH" and "/tmp" in value:
                    warnings.append(f"PATH manipulation detected: {value}")
                for sp in _SECRET_PATTERNS:
                    if sp.search(value):
                        warnings.append(f"Possible secret/key in env var {key}")
                        break

        return ConsentDecision(approved=True, reason="validated", warnings=warnings)

    def validate_configs(self, configs: List[ServerConfig]) -> List[ConsentDecision]:
        return [self.validate_config(c) for c in configs]
