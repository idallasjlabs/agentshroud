# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.

"""
Approval Queue Hardening — Anti-social-engineering measures for the approval queue.

Provides enhanced security measures to prevent social engineering attacks through
misleading approval request descriptions, parameter manipulation, and rapid 
re-submission of denied requests.
"""

import json
import logging
import re
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set

logger = logging.getLogger(__name__)


@dataclass
class DeceptionDetection:
    """Result of deception detection analysis."""

    is_deceptive: bool
    risk_score: float  # 0.0 to 1.0
    issues: List[str] = field(default_factory=list)
    normalized_description: str = ""


@dataclass
class ApprovalHardeningConfig:
    """Configuration for approval queue hardening."""

    # Enable deception detection
    enable_deception_detection: bool = True

    # Enable parameter display enforcement
    always_show_full_parameters: bool = True

    # Enable repeat request blocking
    enable_repeat_request_blocking: bool = True

    # Cooldown period for denied requests (minutes)
    denied_request_cooldown_minutes: int = 5

    # Maximum parameter length to display (0 = no limit)
    max_parameter_display_length: int = 0

    # Enable risk highlighting
    enable_risk_highlighting: bool = True

    # Keywords that indicate high risk actions
    high_risk_keywords: List[str] = field(
        default_factory=lambda: [
            "rm",
            "delete",
            "remove",
            "drop",
            "truncate",
            "format",
            "sudo",
            "chmod",
            "chown",
            "kill",
            "pkill",
            "killall",
            "init",
            "shutdown",
            "reboot",
            "halt",
            "poweroff",
            "mv",
            "move",
            "rename",
            "cp",
            "copy",
            "dd",
            "curl",
            "wget",
            "ssh",
            "scp",
            "ftp",
            "sftp",
            "exec",
            "eval",
            "system",
            "shell",
            "bash",
            "sh",
        ]
    )


@dataclass
class DeniedRequest:
    """Record of a denied approval request."""

    request_id: str
    tool_name: str
    parameters: Dict[str, Any]
    denial_time: float
    agent_id: str


class ApprovalHardening:
    """Anti-social-engineering hardening for approval queue."""

    def __init__(self, config: ApprovalHardeningConfig):
        self.config = config
        self._denied_requests: Dict[str, List[DeniedRequest]] = {}
        self._parameter_fingerprints: Dict[str, Set[str]] = {}

    def analyze_request(
        self,
        tool_name: str,
        description: str,
        parameters: Dict[str, Any],
        agent_id: str = "default",
    ) -> DeceptionDetection:
        """
        Analyze an approval request for potential deception or social engineering.

        Args:
            tool_name: Name of the tool being requested
            description: Human-readable description of the action
            parameters: Tool parameters
            agent_id: Agent making the request

        Returns:
            DeceptionDetection result
        """
        detection = DeceptionDetection(
            is_deceptive=False,
            risk_score=0.0,
            normalized_description=self._normalize_description(description),
        )

        if not self.config.enable_deception_detection:
            return detection

        # Check for description-parameter mismatch
        self._check_description_parameter_mismatch(tool_name, description, parameters, detection)

        # Check for misleading language
        self._check_misleading_language(description, detection)

        # Check for parameter obfuscation
        self._check_parameter_obfuscation(parameters, detection)

        # Check for repeat request patterns
        self._check_repeat_request_patterns(tool_name, parameters, agent_id, detection)

        # Calculate final risk score
        detection.risk_score = min(1.0, len(detection.issues) * 0.25)
        detection.is_deceptive = detection.risk_score >= 0.5

        return detection

    def _normalize_description(self, description: str) -> str:
        """Normalize description by removing misleading language."""
        if not description:
            return description

        # Remove common social engineering phrases
        misleading_phrases = [
            "just",
            "simply",
            "only",
            "harmless",
            "safe",
            "routine",
            "standard",
            "normal",
            "typical",
            "regular",
            "basic",
            "innocent",
            "benign",
            "minor",
            "quick",
            "small",
        ]

        normalized = description.lower()
        for phrase in misleading_phrases:
            normalized = re.sub(rf"\b{phrase}\b", "", normalized)

        # Clean up extra whitespace
        normalized = re.sub(r"\s+", " ", normalized).strip()

        return normalized or description

    def _check_description_parameter_mismatch(
        self,
        tool_name: str,
        description: str,
        parameters: Dict[str, Any],
        detection: DeceptionDetection,
    ) -> None:
        """Check for mismatch between description and actual parameters."""

        # Convert parameters to searchable text
        param_text = json.dumps(parameters, default=str).lower()
        desc_lower = description.lower()

        # Check for dangerous commands in parameters vs benign description
        dangerous_commands = self.config.high_risk_keywords

        has_dangerous_params = any(keyword in param_text for keyword in dangerous_commands)

        has_benign_description = any(
            word in desc_lower
            for word in [
                "check",
                "list",
                "view",
                "show",
                "display",
                "get",
                "read",
                "status",
                "info",
                "help",
                "test",
            ]
        )

        if has_dangerous_params and has_benign_description:
            detection.issues.append(
                "Description suggests benign action but parameters contain potentially dangerous commands"
            )

        # Check for exec tool with misleading description
        if tool_name == "exec":
            command = parameters.get("command", "")
            if isinstance(command, str):
                cmd_lower = command.lower()

                # Check for destructive commands
                if any(danger in cmd_lower for danger in ["rm -rf", "format", "del /q"]):
                    if not any(
                        warn in desc_lower for warn in ["delete", "remove", "format", "destroy"]
                    ):
                        detection.issues.append(
                            "Destructive command execution not clearly indicated in description"
                        )

    def _check_misleading_language(self, description: str, detection: DeceptionDetection) -> None:
        """Check for misleading language patterns in description."""

        desc_lower = description.lower()

        # Check for downplaying language
        downplay_patterns = [
            r"\bjust\s+\w+ing\b",  # "just checking", "just listing"
            r"\bonly\s+\w+ing\b",  # "only viewing", "only reading"
            r"\bsimply\s+\w+ing\b",  # "simply testing"
            r"\bquickly?\s+\w+ing\b",  # "quickly checking"
        ]

        for pattern in downplay_patterns:
            if re.search(pattern, desc_lower):
                detection.issues.append(
                    "Description uses downplaying language that may minimize perceived risk"
                )
                break

        # Check for authority/legitimacy claims
        authority_patterns = [
            r"\b(system|admin|administrator|root|official)\b",
            r"\b(authorized|approved|sanctioned|legitimate)\b",
            r"\b(standard|routine|normal|required|necessary)\b",
        ]

        for pattern in authority_patterns:
            if re.search(pattern, desc_lower):
                detection.issues.append("Description contains authority or legitimacy claims")
                break

    def _check_parameter_obfuscation(
        self, parameters: Dict[str, Any], detection: DeceptionDetection
    ) -> None:
        """Check for obfuscated or encoded parameters."""

        param_str = json.dumps(parameters, default=str)

        # Check for base64 encoding
        base64_pattern = r"[A-Za-z0-9+/]{20,}={0,2}"
        if re.search(base64_pattern, param_str):
            detection.issues.append("Parameters may contain base64-encoded content")

        # Check for hex encoding
        hex_pattern = r"\\x[0-9a-fA-F]{2}"
        if re.search(hex_pattern, param_str):
            detection.issues.append("Parameters may contain hex-encoded content")

        # Check for URL encoding
        url_pattern = r"%[0-9a-fA-F]{2}"
        if re.search(url_pattern, param_str):
            detection.issues.append("Parameters may contain URL-encoded content")

    def _check_repeat_request_patterns(
        self,
        tool_name: str,
        parameters: Dict[str, Any],
        agent_id: str,
        detection: DeceptionDetection,
    ) -> None:
        """Check for patterns indicating repeat request attempts."""

        # Create fingerprint for this request
        fingerprint = self._create_parameter_fingerprint(tool_name, parameters)

        if agent_id not in self._parameter_fingerprints:
            self._parameter_fingerprints[agent_id] = set()

        if fingerprint in self._parameter_fingerprints[agent_id]:
            detection.issues.append("Similar request parameters have been submitted recently")

        self._parameter_fingerprints[agent_id].add(fingerprint)

        # Clean up old fingerprints (keep only recent ones)
        if len(self._parameter_fingerprints[agent_id]) > 100:
            # Remove oldest entries (simple approach - remove half)
            fingerprints_list = list(self._parameter_fingerprints[agent_id])
            self._parameter_fingerprints[agent_id] = set(fingerprints_list[-50:])

    def _create_parameter_fingerprint(self, tool_name: str, parameters: Dict[str, Any]) -> str:
        """Create a fingerprint for request parameters."""
        # Sort parameters for consistent fingerprinting
        sorted_params = json.dumps(
            {"tool": tool_name, "params": parameters}, sort_keys=True, default=str
        )
        return str(hash(sorted_params))

    def is_request_in_cooldown(
        self, tool_name: str, parameters: Dict[str, Any], agent_id: str
    ) -> bool:
        """Check if a similar request is still in cooldown period."""

        if not self.config.enable_repeat_request_blocking:
            return False

        if agent_id not in self._denied_requests:
            return False

        fingerprint = self._create_parameter_fingerprint(tool_name, parameters)
        current_time = time.time()
        cooldown_seconds = self.config.denied_request_cooldown_minutes * 60

        for denied_request in self._denied_requests[agent_id]:
            denied_fingerprint = self._create_parameter_fingerprint(
                denied_request.tool_name, denied_request.parameters
            )

            if denied_fingerprint == fingerprint:
                time_since_denial = current_time - denied_request.denial_time
                if time_since_denial < cooldown_seconds:
                    return True

        return False

    def record_denied_request(
        self, request_id: str, tool_name: str, parameters: Dict[str, Any], agent_id: str
    ) -> None:
        """Record a denied request for cooldown tracking."""

        if not self.config.enable_repeat_request_blocking:
            return

        denied_request = DeniedRequest(
            request_id=request_id,
            tool_name=tool_name,
            parameters=parameters.copy(),
            denial_time=time.time(),
            agent_id=agent_id,
        )

        if agent_id not in self._denied_requests:
            self._denied_requests[agent_id] = []

        self._denied_requests[agent_id].append(denied_request)

        # Clean up old denied requests
        self._cleanup_old_denied_requests(agent_id)

    def _cleanup_old_denied_requests(self, agent_id: str) -> None:
        """Clean up old denied requests beyond cooldown period."""

        if agent_id not in self._denied_requests:
            return

        current_time = time.time()
        cooldown_seconds = self.config.denied_request_cooldown_minutes * 60

        # Keep only requests within cooldown period
        self._denied_requests[agent_id] = [
            req
            for req in self._denied_requests[agent_id]
            if (current_time - req.denial_time) < cooldown_seconds
        ]

        # Remove empty lists
        if not self._denied_requests[agent_id]:
            del self._denied_requests[agent_id]

    def format_hardened_message(
        self,
        tool_name: str,
        description: str,
        parameters: Dict[str, Any],
        detection: DeceptionDetection,
    ) -> str:
        """Format an approval message with hardening measures applied."""

        # Start with normalized description
        message_parts = []

        if detection.normalized_description != description:
            message_parts.append(f"**Original:** {description}")
            message_parts.append(f"**Normalized:** {detection.normalized_description}")
        else:
            message_parts.append(f"**Action:** {description}")

        # Add raw tool information
        message_parts.append(f"**Tool:** {tool_name}")

        # Add parameters with highlighting
        if self.config.always_show_full_parameters:
            param_str = self._format_parameters_with_highlighting(parameters)
            message_parts.append(f"**Parameters:**\n```json\n{param_str}\n```")

        # Add risk information if detected
        if detection.issues:
            message_parts.append("**⚠️ SECURITY CONCERNS:**")
            for issue in detection.issues:
                message_parts.append(f"• {issue}")

        # Add risk score
        if detection.risk_score > 0:
            risk_level = (
                "HIGH"
                if detection.risk_score >= 0.75
                else "MEDIUM" if detection.risk_score >= 0.5 else "LOW"
            )
            message_parts.append(f"**Risk Level:** {risk_level} ({detection.risk_score:.2f})")

        return "\n\n".join(message_parts)

    def _format_parameters_with_highlighting(self, parameters: Dict[str, Any]) -> str:
        """Format parameters with risk highlighting."""

        param_str = json.dumps(parameters, indent=2, default=str)

        if not self.config.enable_risk_highlighting:
            return param_str

        # Highlight dangerous keywords (this is a simplified approach)
        for keyword in self.config.high_risk_keywords:
            # Use regex to highlight whole words only
            pattern = rf"\b{re.escape(keyword)}\b"
            param_str = re.sub(pattern, f"⚠️ {keyword} ⚠️", param_str, flags=re.IGNORECASE)

        return param_str

    def get_stats(self) -> Dict[str, Any]:
        """Get statistics about approval hardening."""

        total_denied = sum(len(requests) for requests in self._denied_requests.values())
        active_cooldowns = len(
            [agent_id for agent_id, requests in self._denied_requests.items() if requests]
        )

        return {
            "total_denied_requests": total_denied,
            "active_cooldowns": active_cooldowns,
            "tracked_agents": len(self._denied_requests),
            "config": {
                "deception_detection_enabled": self.config.enable_deception_detection,
                "cooldown_minutes": self.config.denied_request_cooldown_minutes,
                "full_parameters_shown": self.config.always_show_full_parameters,
            },
        }
