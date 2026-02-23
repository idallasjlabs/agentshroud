# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
File I/O Sandboxing — monitor and optionally restrict file operations.

Default mode: monitor (log everything, flag sensitive access, block nothing).
Enforce mode: hard path restrictions.
"""

import fnmatch
import logging
import os
import re
import time
from dataclasses import dataclass, field
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class PIIFinding:
    type: str
    match: str
    position: int


@dataclass
class PIIScanResult:
    has_pii: bool
    findings: list[PIIFinding] = field(default_factory=list)


class PIIScanner:
    PATTERNS = [
        ("ssn", re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),
        ("credit_card", re.compile(r"\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b")),
        ("email", re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b")),
        (
            "api_key",
            re.compile(
                r"\b(sk-[a-zA-Z0-9]{20,}|ghp-[a-zA-Z0-9]{20,}|AKIA[0-9A-Z]{16})\b"
            ),
        ),
        ("api_key_generic", re.compile(r"\bsk-proj-[a-zA-Z0-9]{20,}\b")),
    ]

    def scan(self, content: str) -> PIIScanResult:
        findings = []
        for pii_type, pattern in self.PATTERNS:
            for match in pattern.finditer(content):
                findings.append(
                    PIIFinding(
                        type=pii_type,
                        match=match.group(),
                        position=match.start(),
                    )
                )
        return PIIScanResult(has_pii=len(findings) > 0, findings=findings)


@dataclass
class FileOperation:
    timestamp: float
    agent_id: str
    operation: str  # "read" or "write"
    path: str
    size_bytes: int = 0
    flagged: bool = False
    reason: str = ""


@dataclass
class FileVerdict:
    allowed: bool
    flagged: bool
    reason: str = ""


@dataclass
class StagingPattern:
    write_path: str
    write_size: int
    network_time: float
    description: str


@dataclass
class FileSandboxConfig:
    mode: str = "monitor"  # "monitor" or "enforce"
    allowed_read_paths: Optional[list[str]] = None  # None = allow all (monitor)
    allowed_write_paths: Optional[list[str]] = None
    blocked_paths: list[str] = field(
        default_factory=lambda: [
            "/etc/shadow",
            "/etc/passwd",
            "/etc/sudoers",
            "**/.ssh/id_*",
            "**/.ssh/authorized_keys",
            "**/.env",
            "**/.env.*",
            "**/.aws/credentials",
            "**/.aws/config",
            "**/.gnupg/*",
            "**/credentials",
            "**/secrets",
        ]
    )
    staging_size_threshold: int = 50_000  # bytes
    staging_time_window: float = 300.0  # seconds


class FileSandbox:
    def __init__(self, config: FileSandboxConfig):
        self.config = config
        self._audit: list[FileOperation] = []
        self._large_writes: dict[str, list[tuple[str, int, float]]] = {}
        self._network_activity: dict[str, list[float]] = {}
        self._pii_scanner = PIIScanner()

    def check_read(self, path: str, agent_id: str) -> FileVerdict:
        return self._check(path, agent_id, "read")

    def check_write(self, path: str, agent_id: str, content: str = "") -> FileVerdict:
        verdict = self._check(
            path, agent_id, "write", len(content.encode("utf-8", errors="replace"))
        )

        # PII scan on write content
        if content:
            pii = self._pii_scanner.scan(content)
            if pii.has_pii:
                verdict.flagged = True
                types = ", ".join(set(f.type for f in pii.findings))
                verdict.reason = (
                    verdict.reason + "; " if verdict.reason else ""
                ) + f"PII detected: {types}"

        # Track large writes for staging detection
        size = len(content.encode("utf-8", errors="replace")) if content else 0
        if size >= self.config.staging_size_threshold:
            if agent_id not in self._large_writes:
                self._large_writes[agent_id] = []
            self._large_writes[agent_id].append((path, size, time.time()))

        return verdict

    def _check(
        self, path: str, agent_id: str, operation: str, size: int = 0
    ) -> FileVerdict:
        flags: list[str] = []

        # Resolve symlinks to prevent path traversal
        try:
            resolved = os.path.realpath(path)
        except (OSError, ValueError):
            resolved = path

        # Check blocked paths against both original and resolved
        if self._matches_blocked(path) or (
            resolved != path and self._matches_blocked(resolved)
        ):
            flags.append(f"sensitive path: {path}")

        # In enforce mode, check allowed paths against resolved path
        if self.config.mode == "enforce":
            allowed_paths = (
                self.config.allowed_read_paths
                if operation == "read"
                else self.config.allowed_write_paths
            )
            if allowed_paths is not None:
                if not any(resolved.startswith(p) for p in allowed_paths):
                    flags.append(f"path outside allowed: {path}")

        flagged = len(flags) > 0
        reason = "; ".join(flags)

        if self.config.mode == "enforce" and flagged:
            allowed = False
        else:
            allowed = True

        op = FileOperation(
            timestamp=time.time(),
            agent_id=agent_id,
            operation=operation,
            path=path,
            size_bytes=size,
            flagged=flagged,
            reason=reason,
        )
        self._audit.append(op)

        if flagged:
            logger.warning("File %s flagged: %s — %s", operation, path, reason)

        return FileVerdict(allowed=allowed, flagged=flagged, reason=reason)

    def _matches_blocked(self, path: str) -> bool:
        for pattern in self.config.blocked_paths:
            if fnmatch.fnmatch(path, pattern):
                return True
            # Also check if pattern appears as suffix
            if pattern.startswith("**/"):
                suffix = pattern[3:]
                if path.endswith(suffix) or ("/" + suffix) in path:
                    return True
                # Try fnmatch on basename
                if fnmatch.fnmatch(path.split("/")[-1], suffix):
                    return True
                # Check for directory patterns
                if fnmatch.fnmatch(path, "*/" + suffix):
                    return True
        return False

    def record_network_activity(self, agent_id: str):
        if agent_id not in self._network_activity:
            self._network_activity[agent_id] = []
        self._network_activity[agent_id].append(time.time())

    def detect_staging_patterns(self, agent_id: str) -> list[StagingPattern]:
        patterns = []
        writes = self._large_writes.get(agent_id, [])
        network = self._network_activity.get(agent_id, [])

        for path, size, write_time in writes:
            for net_time in network:
                if 0 < (net_time - write_time) < self.config.staging_time_window:
                    patterns.append(
                        StagingPattern(
                            write_path=path,
                            write_size=size,
                            network_time=net_time,
                            description=f"Large write ({size}B) to {path} followed by network activity",
                        )
                    )
                    break
        return patterns

    def get_audit_log(self, agent_id: Optional[str] = None) -> list[FileOperation]:
        if agent_id:
            return [op for op in self._audit if op.agent_id == agent_id]
        return list(self._audit)

    def get_temp_files(self, agent_id: str) -> list[str]:
        return [
            op.path
            for op in self._audit
            if op.agent_id == agent_id
            and op.operation == "write"
            and op.path.startswith("/tmp")
        ]
