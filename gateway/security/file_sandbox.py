# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
File I/O Sandboxing — monitor and optionally restrict file operations.

Default mode: monitor (log everything, flag sensitive access, block nothing).
Enforce mode: hard path restrictions with separation of privilege protections.
"""


import fnmatch
import logging
import os
import sys
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
    mode: str = "enforce"  # "monitor" or "enforce"
    allowed_read_paths: Optional[list[str]] = None  # None = allow all (monitor)
    allowed_write_paths: Optional[list[str]] = None
    blocked_paths: list[str] = field(
        default_factory=lambda: [
            # System security files
            "/etc/shadow",
            "/etc/passwd",
            "/etc/sudoers",
            
            # SSH keys and authentication
            "**/.ssh/id_*",
            "**/.ssh/authorized_keys",
            "**/.ssh/*_rsa",
            "**/.ssh/*_ed25519",
            "**/.ssh/config",
            
            # Environment and secrets
            "**/.env",
            "**/.env.*",
            "**/secrets/**",
            "/run/secrets/**",
            
            # AWS credentials
            "**/.aws/credentials",
            "**/.aws/config",
            
            # Other credential files
            "**/.gnupg/*",
            "**/credentials",
            
            # AgentShroud gateway source code - CRITICAL: agent cannot modify its own security
            "/app/agentshroud/**",
            "/app/config/**",
            "**/gateway/**/*.py",
            "**/modules/**/*.py",
            "**/security/**/*.py",
            
            # Security policies and behavioral instructions - IMMUTABLE
            "**/SOUL.md",
            "**/system_prompt*",
            
            # Docker configuration - prevent container escape/manipulation
            "**/docker-compose*.yml",
            "**/docker-compose*.yaml",
            "**/Dockerfile*",
            "**/seccomp/*.json",
            
            # Cross-session memory protection - prevent users from accessing each other's memory
            "**/memory/*/",  # Block access to other users' memory directories
            "**/workspace/memory/*/",  # Block cross-session memory access in any bot workspace
            "**/MEMORY.md",  # Block access to other users' MEMORY.md files (except own session)
            "**/workspace/*/memory/**",  # Block cross-workspace memory access
            "**/session_*/memory/**",  # Block cross-session memory access
            "**/agent_*/memory/**",  # Block cross-agent memory access
            
            # Shared memory and temporary file isolation
            "/tmp/agentshroud/*/",  # Block cross-user temp directory access (handled by PathIsolation)
            "/var/tmp/agentshroud/*/",  # Block cross-user var temp access
                        # Host system paths that should never be accessible from container
            "/etc/**",
            "/var/log/**",
            "/var/lib/**",
            "/usr/bin/**",
            "/usr/sbin/**",
            "/bin/**",
            "/sbin/**",
            "/proc/sys/**",
            "/sys/**",
            
            # Gateway runtime and configuration
            "**/agentshroud.yaml",
            "**/config.yaml",
            "**/tool_risk_tiers.yaml",
            
            # Development and deployment configs
            "**/.git/**",
            "**/terraform/**",
            "**/ansible/**",
            "**/.github/**",
            # macOS-compatible patterns (handle /System/Volumes/Data prefix)
            "**/agentshroud/**",
            "**/config/**",
            "**/modules/**",
            "**/security/**",
            "**/gateway/**",
        ]
    )
    # Allowed write paths - agent can only write to its own workspace.
    # Use the generic /home/** pattern so any bot's home directory is permitted;
    # fine-grained workspace scoping is enforced via WorkspaceIsolation at runtime.
    allowed_write_default: list[str] = field(
        default_factory=lambda: [
            "/tmp/**",
            "/home/**",
            "/app/data/**",  # Gateway can write to its data directory
            "/app/logs/**",  # Gateway can write logs
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

    def _detect_raw_traversal(self, path: str) -> str:
        """Detect path traversal attempts in raw input before normalization."""
        # Detect double-dot patterns (including double-encoded)
        if re.search(r'\.\.+[/\\]', path) or re.search(r'[/\\]\.\.+', path):
            return "path traversal sequence detected"
        
        # Detect Windows-style traversal with backslashes  
        if '\\' in path and ('system32' in path.lower() or 'windows' in path.lower()):
            return "Windows-style path traversal detected"
            
        # Detect encoded traversal patterns
        if '....//....' in path or '....//' in path:
            return "double-encoded traversal detected"
            
        return ""

    def _check(
        self, path: str, agent_id: str, operation: str, size: int = 0
    ) -> FileVerdict:
        flags: list[str] = []

        # Pre-normalization traversal detection
        raw_traversal = self._detect_raw_traversal(path)
        if raw_traversal:
            flags.append(raw_traversal)

        # Resolve symlinks to prevent path traversal
        try:
            resolved = os.path.realpath(path)
        except (OSError, ValueError):
            resolved = path
        # macOS: /tmp -> /private/tmp, /etc -> /private/etc - normalize for pattern matching
        if sys.platform == "darwin" and resolved.startswith("/private/"):
            resolved_canonical = resolved[len("/private"):]  # /private/tmp/x -> /tmp/x
        else:
            resolved_canonical = resolved

        # Check blocked paths against both original and resolved
        if self._matches_blocked(path) or (
            resolved != path and self._matches_blocked(resolved)) or self._matches_blocked(resolved_canonical
        ):
            flags.append(f"security-sensitive path: {path}")

        # Special check for immutable files (security policies)
        if self._is_immutable_file(path) or (resolved != path and self._is_immutable_file(resolved)):
            flags.append(f"immutable security file: {path}")

        # In enforce mode, check allowed paths against resolved path
        if self.config.mode == "enforce":
            if operation == "write":
                # For writes, use explicit allowed list or defaults
                allowed_paths = self.config.allowed_write_paths or self.config.allowed_write_default
                if not (self._matches_allowed_paths(path, allowed_paths) or self._matches_allowed_paths(resolved, allowed_paths) or self._matches_allowed_paths(resolved_canonical, allowed_paths)):
                    flags.append(f"write outside allowed workspace: {path}")
            elif operation == "read":
                # For reads, check if it's in blocked paths
                allowed_paths = self.config.allowed_read_paths
                if allowed_paths is not None and not (self._matches_allowed_paths(path, allowed_paths) or self._matches_allowed_paths(resolved, allowed_paths)):
                    flags.append(f"read outside allowed paths: {path}")

        flagged = len(flags) > 0
        reason = "; ".join(flags)

        # In enforce mode, block flagged operations
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
            if self.config.mode == "enforce" and not allowed:
                logger.critical("File %s BLOCKED: %s — %s", operation, path, reason)

        return FileVerdict(allowed=allowed, flagged=flagged, reason=reason)

    def _matches_blocked(self, path: str) -> bool:
        """Check if path matches any blocked pattern."""
        for pattern in self.config.blocked_paths:
            if self._match_pattern(path, pattern):
                return True
        return False

    def _is_immutable_file(self, path: str) -> bool:
        """Check if this is an immutable security file by name."""
        immutable_names = {
            "SOUL.md",
            "system_prompt.txt", 
            "system_prompt.md",
            "agentshroud.yaml",
            "config.yaml",
            "docker-compose.yml",
            "docker-compose.yaml",
        }
        filename = os.path.basename(path)
        return filename in immutable_names

    def _matches_allowed_paths(self, path: str, allowed_paths: list[str]) -> bool:
        """Check if path is within any allowed pattern."""
        for pattern in allowed_paths:
            if self._match_pattern(path, pattern):
                return True
        return False

    def _match_pattern(self, path: str, pattern: str) -> bool:
        """Enhanced pattern matching for file paths."""
        # Direct fnmatch
        if fnmatch.fnmatch(path, pattern):
            return True
        
        # Handle ** patterns 
        if pattern.startswith("**/"):
            suffix = pattern[3:]
            # Check if path ends with suffix
            if path.endswith(suffix) or ("/" + suffix) in path:
                return True
            # Check basename match
            if fnmatch.fnmatch(os.path.basename(path), suffix):
                return True
            # Check if any parent directory + suffix matches
            path_parts = path.split("/")
            for i in range(len(path_parts)):
                subpath = "/".join(path_parts[i:])
                if fnmatch.fnmatch(subpath, suffix):
                    return True
                    
        # Handle trailing ** patterns (directory and all contents)
        if pattern.endswith("/**"):
            prefix = pattern[:-3]
            if path.startswith(prefix + "/") or path == prefix:
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

    def get_security_violations(self, agent_id: Optional[str] = None) -> list[FileOperation]:
        """Get all flagged operations that indicate security violations."""
        violations = []
        for op in self.get_audit_log(agent_id):
            if op.flagged and ("security-sensitive" in op.reason or "immutable" in op.reason):
                violations.append(op)
        return violations
