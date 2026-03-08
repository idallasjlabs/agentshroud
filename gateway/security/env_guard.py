# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Environment Leakage Guard - Security Hardening Module
Block agent access to environment variables and prevent credential leakage.
"""
from __future__ import annotations


import os
import re
import logging
from typing import List, Dict, Any
from dataclasses import dataclass
import shlex

logger = logging.getLogger(__name__)


@dataclass
class EnvironmentLeakage:
    """Detected environment variable leakage."""

    source: str  # command, file_path, etc.
    leaked_vars: List[str]
    severity: str  # critical, high, medium, low
    detection_method: str
    context: str


class EnvironmentGuard:
    """Guard against environment variable leakage and unauthorized access."""

    def __init__(self):
        self.blocked_paths = [
            "/proc/self/environ",
            "/proc/1/environ",
            "/proc/*/environ",
        ]

        self.blocked_commands = ["env", "printenv", "set", "export", "declare -p"]

        self.api_key_patterns = [
            re.compile(r"\bsk-[A-Za-z0-9]{48}\b"),  # OpenAI
            re.compile(r"\bAKIA[0-9A-Z]{16}\b"),  # AWS Access Key
            re.compile(r"\bAWSsecretkey[A-Za-z0-9+/]{40}\b"),  # AWS Secret
            re.compile(r"\bghp_[A-Za-z0-9]{36}\b"),  # GitHub Personal Access Token
            re.compile(r"\bop_[A-Za-z0-9]{26}\b"),  # 1Password Service Account
            re.compile(
                r"\bxoxb-[A-Za-z0-9]{11}-[A-Za-z0-9]{11}-[A-Za-z0-9]{24}\b"
            ),  # Slack Bot Token
            re.compile(
                r"\bxoxp-[A-Za-z0-9]{11}-[A-Za-z0-9]{11}-[A-Za-z0-9]{11}-[A-Za-z0-9]{32}\b"
            ),  # Slack User Token
            re.compile(r"\b[a-zA-Z0-9]{32,}\b"),  # Generic long alphanumeric (API keys)
        ]

        self.credential_env_vars = {
            # Common credential environment variables
            "API_KEY",
            "SECRET_KEY",
            "ACCESS_TOKEN",
            "PRIVATE_KEY",
            "PASSWORD",
            "PASSWD",
            "PWD",
            "TOKEN",
            "BEARER_TOKEN",
            "OPENAI_API_KEY",
            "ANTHROPIC_API_KEY",
            "ANTHROPIC_OAUTH_TOKEN",
            "GOOGLE_API_KEY",
            "AWS_ACCESS_KEY_ID",
            "AWS_SECRET_ACCESS_KEY",
            "AWS_SESSION_TOKEN",
            "GITHUB_TOKEN",
            "GH_TOKEN",
            "GITHUB_PAT",
            "SLACK_TOKEN",
            "SLACK_WEBHOOK_URL",
            "OP_SERVICE_ACCOUNT_TOKEN",
            "OP_SESSION",
            "DATABASE_URL",
            "DB_PASSWORD",
            "MYSQL_PASSWORD",
            "POSTGRES_PASSWORD",
            "SMTP_PASSWORD",
            "EMAIL_PASSWORD",
            "ENCRYPTION_KEY",
            "SIGNING_KEY",
            "JWT_SECRET",
        }

        self.detected_leakages: List[EnvironmentLeakage] = []

    def check_file_access(self, file_path: str, agent_id: str) -> bool:
        """
        Check if file access should be blocked to prevent environment leakage.

        Args:
            file_path: Path being accessed
            agent_id: ID of the agent attempting access

        Returns:
            True if access allowed, False if blocked
        """
        normalized_path = os.path.normpath(file_path)

        # Block direct access to environment files
        for blocked_path in self.blocked_paths:
            if "*" in blocked_path:
                # Handle wildcard patterns
                pattern = blocked_path.replace("*", "[0-9]+")
                if re.match(pattern, normalized_path):
                    logger.warning(
                        f"Agent {agent_id} blocked from accessing {file_path} - environment leakage risk"
                    )
                    self._record_leakage(
                        source=f"file_access:{file_path}",
                        leaked_vars=[],
                        severity="critical",
                        detection_method="path_block",
                        context=f"Agent {agent_id} attempted to access {file_path}",
                    )
                    return False
            elif normalized_path == blocked_path:
                logger.warning(
                    f"Agent {agent_id} blocked from accessing {file_path} - environment leakage risk"
                )
                self._record_leakage(
                    source=f"file_access:{file_path}",
                    leaked_vars=[],
                    severity="critical",
                    detection_method="path_block",
                    context=f"Agent {agent_id} attempted to access {file_path}",
                )
                return False

        return True

    def check_command_execution(self, command: str, agent_id: str) -> bool:
        """
        Check if command execution should be blocked to prevent environment leakage.

        Args:
            command: Command being executed
            agent_id: ID of the agent attempting execution

        Returns:
            True if execution allowed, False if blocked
        """
        # Parse command to get the base command
        try:
            parsed_cmd = shlex.split(command)
            if not parsed_cmd:
                return True

            base_cmd = parsed_cmd[0]

            # Check against blocked commands
            if base_cmd in self.blocked_commands:
                logger.warning(
                    f"Agent {agent_id} blocked from executing '{command}' - environment leakage risk"
                )
                self._record_leakage(
                    source=f"command:{command}",
                    leaked_vars=[],
                    severity="high",
                    detection_method="command_block",
                    context=f"Agent {agent_id} attempted to execute {command}",
                )
                return False

            # Check for indirect environment access
            if self._contains_env_access_patterns(command):
                logger.warning(
                    f"Agent {agent_id} blocked from executing '{command}' - potential environment access"
                )
                self._record_leakage(
                    source=f"command:{command}",
                    leaked_vars=[],
                    severity="medium",
                    detection_method="pattern_block",
                    context=f"Agent {agent_id} attempted indirect env access via {command}",
                )
                return False

        except Exception as e:
            logger.error(f"Error parsing command '{command}': {e}")
            # Fail-closed: deny on parse error
            return False

        return True

    def _contains_env_access_patterns(self, command: str) -> bool:
        """Check if command contains patterns that could access environment."""
        env_access_patterns = [
            r"\$\w+",  # Environment variable expansion like $PATH
            r"\$\{\w+\}",  # Environment variable expansion like ${PATH}
            r"cat\s+/proc/(?:\d+|self)/environ",  # Direct environ file access
            r"strings\s+/proc/(?:\d+|self)/environ",  # Strings on environ file
            r"grep\s+.*\s+/proc/(?:\d+|self)/environ",  # Grep on environ file
        ]

        for pattern in env_access_patterns:
            if re.search(pattern, command, re.IGNORECASE):
                return True

        return False

    def scrub_command_output(self, output: str, command: str) -> str:
        """
        Scrub environment variables and API keys from command output.

        Args:
            output: Command output to scrub
            command: Original command (for context)

        Returns:
            Scrubbed output
        """
        scrubbed_output = output
        leaked_vars = []

        # Scrub API key patterns
        for pattern in self.api_key_patterns:
            matches = pattern.findall(output)
            if matches:
                leaked_vars.extend(
                    [f"api_key_pattern:{len(match)}" for match in matches]
                )
                scrubbed_output = pattern.sub("[REDACTED-API-KEY]", scrubbed_output)

        # Scrub environment variable patterns
        env_var_pattern = re.compile(r"([A-Z_][A-Z0-9_]*)\s*=\s*([^\s\n]+)")
        matches = env_var_pattern.findall(output)

        for var_name, var_value in matches:
            if var_name in self.credential_env_vars:
                leaked_vars.append(var_name)
                scrubbed_output = scrubbed_output.replace(
                    f"{var_name}={var_value}", f"{var_name}=[REDACTED]"
                )
            elif self._looks_like_credential(var_value):
                leaked_vars.append(f"{var_name}:credential_pattern")
                scrubbed_output = scrubbed_output.replace(
                    f"{var_name}={var_value}", f"{var_name}=[REDACTED]"
                )

        # Record leakage if any credentials were found
        if leaked_vars:
            self._record_leakage(
                source=f"command_output:{command}",
                leaked_vars=leaked_vars,
                severity=(
                    "high"
                    if any(var in self.credential_env_vars for var in leaked_vars)
                    else "medium"
                ),
                detection_method="output_scrub",
                context=f"Credentials found in output of: {command}",
            )

        return scrubbed_output

    def _looks_like_credential(self, value: str) -> bool:
        """Check if a value looks like a credential."""
        if len(value) < 8:
            return False

        # Check against API key patterns
        for pattern in self.api_key_patterns:
            if pattern.match(value):
                return True

        # Check for long alphanumeric strings (potential tokens)
        if len(value) > 20 and re.match(r"^[A-Za-z0-9+/=_-]+$", value):
            return True

        # Check for base64-like patterns
        if len(value) > 16 and value.endswith("=="):
            return True

        return False

    def monitor_environment_access(self, agent_id: str) -> Dict[str, Any]:
        """
        Monitor an agent's environment access attempts.

        Args:
            agent_id: ID of agent to monitor

        Returns:
            Dictionary with monitoring results
        """
        monitoring_results = {
            "agent_id": agent_id,
            "environment_access_attempts": 0,
            "blocked_attempts": 0,
            "suspicious_patterns": [],
            "risk_level": "low",
        }

        # Check recent leakages for this agent
        agent_leakages = [
            leakage for leakage in self.detected_leakages if agent_id in leakage.context
        ]

        if agent_leakages:
            monitoring_results["environment_access_attempts"] = len(agent_leakages)
            monitoring_results["blocked_attempts"] = len(
                [
                    leak
                    for leak in agent_leakages
                    if leak.detection_method
                    in ["path_block", "command_block", "pattern_block"]
                ]
            )

            # Determine risk level
            critical_attempts = len(
                [leak for leak in agent_leakages if leak.severity == "critical"]
            )
            high_attempts = len(
                [leak for leak in agent_leakages if leak.severity == "high"]
            )

            if critical_attempts > 0:
                monitoring_results["risk_level"] = "critical"
            elif high_attempts > 2:
                monitoring_results["risk_level"] = "high"
            elif len(agent_leakages) > 5:
                monitoring_results["risk_level"] = "medium"

        return monitoring_results

    def _record_leakage(
        self,
        source: str,
        leaked_vars: List[str],
        severity: str,
        detection_method: str,
        context: str,
    ):
        """Record a detected environment leakage."""
        leakage = EnvironmentLeakage(
            source=source,
            leaked_vars=leaked_vars,
            severity=severity,
            detection_method=detection_method,
            context=context,
        )
        self.detected_leakages.append(leakage)

        # Log the leakage
        logger.warning(f"Environment leakage detected - {severity}: {context}")
        if leaked_vars:
            logger.warning(f"  Leaked variables: {', '.join(leaked_vars)}")

    def get_leakage_summary(self) -> Dict[str, Any]:
        """Get summary of all detected leakages."""
        summary = {
            "total_leakages": len(self.detected_leakages),
            "by_severity": {},
            "by_detection_method": {},
            "unique_sources": set(),
            "leaked_variables": set(),
        }

        for leakage in self.detected_leakages:
            # Count by severity
            summary["by_severity"][leakage.severity] = (
                summary["by_severity"].get(leakage.severity, 0) + 1
            )

            # Count by detection method
            method = leakage.detection_method
            summary["by_detection_method"][method] = (
                summary["by_detection_method"].get(method, 0) + 1
            )

            # Collect sources and variables
            summary["unique_sources"].add(leakage.source)
            summary["leaked_variables"].update(leakage.leaked_vars)

        # Convert sets to lists for JSON serialization
        summary["unique_sources"] = list(summary["unique_sources"])
        summary["leaked_variables"] = list(summary["leaked_variables"])

        return summary

    def clear_detected_leakages(self):
        """Clear the list of detected leakages."""
        self.detected_leakages.clear()
        logger.info("Cleared detected environment leakages")

    def export_leakage_report(self, output_path: str):
        """Export leakage findings to a report file."""
        import json
        import time

        report = {
            "timestamp": time.time(),
            "summary": self.get_leakage_summary(),
            "leakages": [
                {
                    "source": leak.source,
                    "leaked_vars": leak.leaked_vars,
                    "severity": leak.severity,
                    "detection_method": leak.detection_method,
                    "context": leak.context,
                }
                for leak in self.detected_leakages
            ],
        }

        with open(output_path, "w") as f:
            json.dump(report, f, indent=2)

        logger.info(f"Environment leakage report exported to {output_path}")


# Global instance for easy access
global_env_guard = EnvironmentGuard()


def get_env_guard() -> EnvironmentGuard:
    """Get the global environment guard instance."""
    return global_env_guard


def check_command(cmd: str) -> tuple[bool, str]:
    """
    Check if command execution should be allowed.

    Args:
        cmd: Command to check

    Returns:
        (allowed, reason): True if allowed with reason, False if blocked with reason
    """
    guard = get_env_guard()
    allowed = guard.check_command_execution(cmd, "agent")

    if allowed:
        return True, "Command allowed"
    else:
        # Check specific patterns to provide better error message
        if any(
            pattern in cmd.lower()
            for pattern in ["/proc/self/environ", "/proc/", "printenv", "env |"]
        ):
            return False, "Command blocked: environment access detected"
        elif any(pattern in cmd for pattern in ["$ENV{", "$env:", "${ENV"]):
            return False, "Command blocked: environment variable access detected"
        else:
            return False, "Command blocked: potential environment leakage"


def scrub_output(text: str) -> str:
    """
    Scrub API keys and sensitive patterns from text output.

    Args:
        text: Text to scrub

    Returns:
        Scrubbed text with sensitive patterns replaced
    """
    # API key patterns to scrub
    patterns = {
        "openai_key": re.compile(r"\bsk-[A-Za-z0-9]{48}\b"),
        "aws_access_key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
        "aws_secret_key": re.compile(r"[A-Za-z0-9+/]{40}"),
        "github_token": re.compile(r"\bghp_[A-Za-z0-9]{36}\b"),
        "op_key": re.compile(r"\bop_[A-Za-z0-9]{26}\b"),
        "generic_api_key": re.compile(r"\b[A-Za-z0-9]{32,}\b"),
    }

    scrubbed = text
    for pattern_name, pattern in patterns.items():
        scrubbed = pattern.sub(f"[SCRUBBED-{pattern_name.upper()}]", scrubbed)

    return scrubbed
