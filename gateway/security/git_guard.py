# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Git Hook Guard - Security Hardening Module
Scan git hooks and package installation scripts for malicious content.
"""
from __future__ import annotations


import os
import stat
import re
import json
import logging
import tempfile
import time
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)


class ThreatLevel(str, Enum):
    """Threat levels for detected issues."""

    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


@dataclass
class SecurityFinding:
    """A security finding in git hooks or install scripts."""

    file_path: str
    threat_level: ThreatLevel
    category: str
    description: str
    matched_pattern: str
    line_number: Optional[int] = None
    context: Optional[str] = None


class GitGuard:
    """Monitor and analyze git hooks and package installation scripts."""

    def __init__(self, mode: str = "monitor"):
        """
        Args:
            mode: 'monitor' (log findings) or 'enforce' (quarantine suspicious files)
        """
        self.mode = mode
        self.findings: List[SecurityFinding] = []
        self.quarantine_dir = Path(tempfile.gettempdir()) / "agentshroud_quarantine"
        self.quarantine_dir.mkdir(exist_ok=True)

        # Patterns for detecting malicious content
        self.malicious_patterns = {
            # Network communication
            "reverse_shell": (
                ThreatLevel.CRITICAL,
                [
                    r"bash\s+-i\s+>&?\s*/dev/tcp/",
                    r"nc\s+.*-[le].*sh",
                    r"netcat.*-[le].*sh",
                    r"/bin/sh.*>&.*tcp",
                    r"perl.*socket.*exec",
                    r"python.*socket.*subprocess",
                ],
            ),
            "outbound_requests": (
                ThreatLevel.HIGH,
                [
                    r"curl\s+.*https?://",
                    r"wget\s+.*https?://",
                    r"fetch\s+.*https?://",
                    r"http\.get\(",
                    r"requests\.get\(",
                    r"urllib.*urlopen",
                ],
            ),
            "data_exfiltration": (
                ThreatLevel.HIGH,
                [
                    r"cat\s+.*\|\s*curl",
                    r"tar\s+.*\|\s*curl",
                    r"zip\s+.*\|\s*curl",
                    r"env\s*\|\s*curl",
                    r"history\s*\|\s*curl",
                ],
            ),
            "encoded_payloads": (
                ThreatLevel.CRITICAL,
                [
                    r"base64\s+-d.*exec",
                    r"echo\s+[A-Za-z0-9+/=]{50,}\s*\|\s*base64",
                    r"printf.*\\x[0-9a-f]{2}.*exec",
                    r"eval\s*\$\([^)]*base64",
                    r"python.*-c.*base64",
                ],
            ),
            "file_manipulation": (
                ThreatLevel.MEDIUM,
                [
                    r"chmod\s+\+x.*\.(sh|py|pl|rb)",
                    r"cp\s+.*/(bin|sbin)/",
                    r"mv\s+.*/(bin|sbin)/",
                    r"install\s+-m.*/(bin|sbin)/",
                ],
            ),
            "privilege_escalation": (
                ThreatLevel.CRITICAL,
                [
                    r"sudo\s+.*NOPASSWD",
                    r"setuid\(",
                    r"chmod\s+[0-9]*[4-7][0-9]*",
                    r"su\s+-\s+root",
                    r"/etc/passwd",
                    r"/etc/shadow",
                ],
            ),
            "persistence": (
                ThreatLevel.HIGH,
                [
                    r"crontab\s+-[er]",
                    r"/etc/cron",
                    r"systemctl.*enable",
                    r"service.*start",
                    r"~/.ssh/authorized_keys",
                    r"~/.bashrc",
                    r"~/.bash_profile",
                ],
            ),
        }

        # Package.json script patterns
        self.package_patterns = {
            "postinstall_risks": (
                ThreatLevel.HIGH,
                [
                    r'"postinstall":\s*"[^"]*curl',
                    r'"postinstall":\s*"[^"]*wget',
                    r'"postinstall":\s*"[^"]*sh\s',
                    r'"postinstall":\s*"[^"]*bash',
                    r'"postinstall":\s*"[^"]*node.*-e"',
                ],
            ),
            "preinstall_risks": (
                ThreatLevel.HIGH,
                [
                    r'"preinstall":\s*"[^"]*curl',
                    r'"preinstall":\s*"[^"]*wget',
                    r'"preinstall":\s*"[^"]*rm\s+-rf',
                    r'"prepare":\s*"[^"]*curl',
                ],
            ),
        }

    def scan_content(self, content: str, label: str = "message") -> List[SecurityFinding]:
        """Scan arbitrary text content for malicious git/supply-chain patterns.

        This is the primary entry point for middleware use.  Unlike
        ``scan_git_repository`` (which walks files on disk) this method checks
        in-memory content — e.g. a user message or tool result — against the
        same pattern library.

        Args:
            content: The text to scan.
            label: A human-readable label used in finding metadata (default: "message").

        Returns:
            List of SecurityFinding objects; empty list if clean.
        """
        return self._analyze_script_content(f"<{label}>", content, label)

    def scan_git_repository(self, repo_path: str) -> List[SecurityFinding]:
        """
        Scan a git repository for malicious hooks and scripts.

        Args:
            repo_path: Path to the git repository

        Returns:
            List of security findings
        """
        findings = []
        repo_path = Path(repo_path)

        # Scan git hooks
        hooks_dir = repo_path / ".git" / "hooks"
        if hooks_dir.exists():
            findings.extend(self._scan_git_hooks(hooks_dir))

        # Scan package.json files
        for package_json in repo_path.rglob("package.json"):
            findings.extend(self._scan_package_json(package_json))

        # Scan setup.py files
        for setup_py in repo_path.rglob("setup.py"):
            findings.extend(self._scan_setup_py(setup_py))

        # Scan pyproject.toml files
        for pyproject in repo_path.rglob("pyproject.toml"):
            findings.extend(self._scan_pyproject_toml(pyproject))

        self.findings.extend(findings)

        if self.mode == "enforce":
            self._quarantine_suspicious_files(findings)

        return findings

    def _scan_git_hooks(self, hooks_dir: Path) -> List[SecurityFinding]:
        """Scan git hooks directory for malicious content."""
        findings = []

        for hook_file in hooks_dir.iterdir():
            if hook_file.is_file() and not hook_file.name.endswith(".sample"):
                # Check if hook is executable
                # Check if hook has execute permissions (using stat to avoid noexec filesystem issues)
                file_stat = os.stat(hook_file)
                has_execute_permission = bool(file_stat.st_mode & stat.S_IXUSR)
                if has_execute_permission:
                    findings.extend(self._analyze_script_file(hook_file, "git_hook"))
                else:
                    # Non-executable hook - still analyze but lower severity
                    script_findings = self._analyze_script_file(hook_file, "git_hook")
                    for finding in script_findings:
                        if finding.threat_level == ThreatLevel.CRITICAL:
                            finding.threat_level = ThreatLevel.HIGH
                        elif finding.threat_level == ThreatLevel.HIGH:
                            finding.threat_level = ThreatLevel.MEDIUM
                    findings.extend(script_findings)

        return findings

    def _scan_package_json(self, package_file: Path) -> List[SecurityFinding]:
        """Scan package.json for suspicious install scripts."""
        findings = []

        try:
            with open(package_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Parse JSON to check scripts section
            try:
                package_data = json.loads(content)
                scripts = package_data.get("scripts", {})

                for script_name, script_content in scripts.items():
                    if script_name in [
                        "postinstall",
                        "preinstall",
                        "prepare",
                        "install",
                    ]:
                        findings.extend(
                            self._analyze_script_content(
                                str(package_file),
                                script_content,
                                f"package_script_{script_name}",
                            )
                        )
            except json.JSONDecodeError:
                findings.append(
                    SecurityFinding(
                        file_path=str(package_file),
                        threat_level=ThreatLevel.LOW,
                        category="malformed",
                        description="Malformed package.json file",
                        matched_pattern="json_parse_error",
                    )
                )

            # Also scan raw content for patterns
            findings.extend(
                self._analyze_file_content(package_file, content, "package_json")
            )

        except Exception as e:
            logger.error(f"Error scanning {package_file}: {e}")
            findings.append(
                SecurityFinding(
                    file_path=str(package_file),
                    threat_level=ThreatLevel.LOW,
                    category="scan_error",
                    description=f"Failed to scan file: {str(e)}",
                    matched_pattern="scan_error",
                )
            )

        return findings

    def _scan_setup_py(self, setup_file: Path) -> List[SecurityFinding]:
        """Scan setup.py for suspicious installation scripts."""
        return self._analyze_script_file(setup_file, "setup_script")

    def _scan_pyproject_toml(self, pyproject_file: Path) -> List[SecurityFinding]:
        """Scan pyproject.toml for suspicious build scripts."""
        findings = []

        try:
            with open(pyproject_file, "r", encoding="utf-8") as f:
                content = f.read()

            findings.extend(
                self._analyze_file_content(pyproject_file, content, "pyproject")
            )

        except Exception as e:
            logger.error(f"Error scanning {pyproject_file}: {e}")

        return findings

    def _analyze_script_file(
        self, file_path: Path, category: str
    ) -> List[SecurityFinding]:
        """Analyze a script file for malicious patterns."""
        findings = []

        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            findings.extend(self._analyze_file_content(file_path, content, category))

        except Exception as e:
            logger.error(f"Error analyzing {file_path}: {e}")

        return findings

    def _analyze_file_content(
        self, file_path: Path, content: str, category: str
    ) -> List[SecurityFinding]:
        """Analyze file content for malicious patterns."""
        findings = []
        lines = content.split("\n")

        for pattern_category, (
            threat_level,
            patterns,
        ) in self.malicious_patterns.items():
            for pattern in patterns:
                regex = re.compile(pattern, re.IGNORECASE | re.MULTILINE)
                for line_num, line in enumerate(lines, 1):
                    matches = regex.findall(line)
                    if matches:
                        findings.append(
                            SecurityFinding(
                                file_path=str(file_path),
                                threat_level=threat_level,
                                category=f"{category}_{pattern_category}",
                                description=f"Suspicious {pattern_category} pattern detected",
                                matched_pattern=pattern,
                                line_number=line_num,
                                context=line.strip(),
                            )
                        )

        # Also check package-specific patterns for package.json
        if file_path.name == "package.json":
            for pattern_category, (
                threat_level,
                patterns,
            ) in self.package_patterns.items():
                for pattern in patterns:
                    regex = re.compile(pattern, re.IGNORECASE | re.MULTILINE)
                    matches = regex.findall(content)
                    if matches:
                        findings.append(
                            SecurityFinding(
                                file_path=str(file_path),
                                threat_level=threat_level,
                                category=f"package_{pattern_category}",
                                description=f"Suspicious package script: {pattern_category}",
                                matched_pattern=pattern,
                            )
                        )

        return findings

    def _analyze_script_content(
        self, file_path: str, script_content: str, category: str
    ) -> List[SecurityFinding]:
        """Analyze script content string for malicious patterns."""
        findings = []

        for pattern_category, (
            threat_level,
            patterns,
        ) in self.malicious_patterns.items():
            for pattern in patterns:
                regex = re.compile(pattern, re.IGNORECASE)
                if regex.search(script_content):
                    findings.append(
                        SecurityFinding(
                            file_path=file_path,
                            threat_level=threat_level,
                            category=f"{category}_{pattern_category}",
                            description=f"Suspicious {pattern_category} in script",
                            matched_pattern=pattern,
                            context=script_content,
                        )
                    )

        return findings

    def _quarantine_suspicious_files(self, findings: List[SecurityFinding]):
        """Move suspicious files to quarantine directory."""
        quarantined_files = set()

        for finding in findings:
            if finding.threat_level in [ThreatLevel.CRITICAL, ThreatLevel.HIGH]:
                file_path = Path(finding.file_path)
                if file_path.exists() and str(file_path) not in quarantined_files:
                    try:
                        # Create quarantine subdirectory
                        quarantine_subdir = self.quarantine_dir / file_path.parent.name
                        quarantine_subdir.mkdir(exist_ok=True)

                        # Move file to quarantine
                        quarantine_path = quarantine_subdir / file_path.name
                        file_path.rename(quarantine_path)

                        logger.warning(
                            f"Quarantined suspicious file: {file_path} -> {quarantine_path}"
                        )
                        quarantined_files.add(str(file_path))

                    except Exception as e:
                        logger.error(f"Failed to quarantine {file_path}: {e}")

    def monitor_git_operations(self):
        """Monitor for git clone and npm install operations."""
        # This would typically be implemented as a file system watcher
        # or integrated into the command execution pipeline
        pass

    def get_findings_summary(self) -> Dict[str, Any]:
        """Get a summary of all findings."""
        summary = {
            "total_findings": len(self.findings),
            "by_threat_level": {},
            "by_category": {},
            "critical_files": [],
        }

        for finding in self.findings:
            # Count by threat level
            level = finding.threat_level.value
            summary["by_threat_level"][level] = (
                summary["by_threat_level"].get(level, 0) + 1
            )

            # Count by category
            summary["by_category"][finding.category] = (
                summary["by_category"].get(finding.category, 0) + 1
            )

            # Collect critical files
            if finding.threat_level == ThreatLevel.CRITICAL:
                summary["critical_files"].append(finding.file_path)

        return summary

    def export_findings_report(self, output_path: str):
        """Export findings to a detailed report."""
        report = {
            "scan_timestamp": time.time(),
            "mode": self.mode,
            "summary": self.get_findings_summary(),
            "findings": [
                {
                    "file_path": f.file_path,
                    "threat_level": f.threat_level.value,
                    "category": f.category,
                    "description": f.description,
                    "matched_pattern": f.matched_pattern,
                    "line_number": f.line_number,
                    "context": f.context,
                }
                for f in self.findings
            ],
        }

        with open(output_path, "w") as f:
            json.dump(report, f, indent=2)

        logger.info(f"Git guard report exported to {output_path}")


def scan_repository(repo_path: str, mode: str = "monitor") -> GitGuard:
    """Convenience function to scan a repository."""
    guard = GitGuard(mode=mode)
    guard.scan_git_repository(repo_path)
    return guard
