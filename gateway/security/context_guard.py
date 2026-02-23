# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Context Window Poisoning Defense - Security Hardening Module
Detect attempts to manipulate the AI context window through malicious inputs.
"""

import re
import time
import hashlib
import logging
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass
from collections import defaultdict, deque

logger = logging.getLogger(__name__)


@dataclass
class ContextAttack:
    """Detected context window attack attempt."""

    session_id: str
    attack_type: str
    severity: str  # critical, high, medium, low
    description: str
    message_content: str
    detection_patterns: List[str]
    timestamp: float
    context_size_before: int
    context_size_after: int


@dataclass
class SessionContext:
    """Context tracking for a session."""

    session_id: str
    messages: deque
    total_characters: int
    message_count: int
    context_growth_rate: float
    last_activity: float
    repeated_content_hashes: Dict[str, int]
    instruction_pattern_count: Dict[str, int]


class ContextGuard:
    """Guard against context window poisoning attacks."""

    def __init__(
        self, max_message_length: int = 50000, max_context_size: int = 1000000
    ):
        self.max_message_length = max_message_length
        self.max_context_size = max_context_size
        self.sessions: Dict[str, SessionContext] = {}
        self.detected_attacks: List[ContextAttack] = []

        # Patterns that might indicate instruction injection
        self.instruction_patterns = [
            # Direct instruction attempts
            r"(?i)\b(?:ignore|forget|disregard)\s+(?:all\s+)?(?:previous|prior|above)\s+(?:instructions?|rules?|prompts?)",
            r"(?i)\b(?:you\s+are\s+now|from\s+now\s+on|starting\s+now)\b.*\b(?:assistant|ai|bot|system)",
            r"(?i)\bact\s+(?:as|like)\s+(?:a|an)?\s*(?:different|new|evil|malicious)\s+(?:assistant|ai|character)",
            r"(?i)\bpretend\s+(?:to\s+be|that\s+you\s+are)\b",
            r"(?i)\brole[\s-]?play(?:ing)?\s+(?:as|that)",
            r"(?i)\b(?:system|admin|root|developer)\s+(?:mode|override|prompt|instruction)",
            # Common jailbreak attempts
            r"(?i)\bDAN\s+mode\b",
            r"(?i)\bdo\s+anything\s+now\b",
            r"(?i)\bunhackable\b",
            r"(?i)\bjailbreak\b",
            r"(?i)\bbypass\s+(?:safety|security|restrictions?)",
            r"(?i)\bignore\s+(?:safety|security|guidelines)",
            # Prompt injection patterns
            r"(?i)^\s*[\[\(]?\s*(?:system|user|assistant)\s*[\]\)]?\s*:",
            r"(?i)\b(?:example|sample)\s+(?:conversation|dialogue|chat)",
            r"(?i)```\s*(?:system|user|assistant)",
            r"(?i)<\|(?:system|user|assistant)\|>",
            r"(?i)###\s+(?:system|user|assistant)",
            # Hidden instruction attempts
            r"(?i)<!--.*(?:instruction|system|override).*-->",
            r"(?i)\[(?:hidden|secret|private)\s+(?:instruction|message|note)\]",
            r"(?i)(?:ps|p\.s\.)\s*[:;].*(?:actually|really|instead)",
            # Context stuffing indicators
            r"(?:\w+\s+){50,}",  # Long sequences of words (potential filler)
            r"(?:[\w\s]{100,}\s+){10,}",  # Repeated long chunks
            r"(?:lorem\s+ipsum|the\s+quick\s+brown\s+fox|test\s+test\s+test)",  # Common filler text
        ]

        # Compile patterns for efficiency
        self.compiled_patterns = [
            re.compile(pattern) for pattern in self.instruction_patterns
        ]

        # Patterns for repetition detection
        self.repetition_patterns = [
            r"(.{10,}?)\1{5,}",  # Same string repeated 5+ times
            r"\b(\w+)(?:\s+\1){10,}",  # Same word repeated 10+ times
            r"(.{50,}?)(?:\s+\1){3,}",  # Long phrases repeated 3+ times
        ]

        # Track session metrics
        self.session_metrics = {
            "rapid_context_growth": 0,
            "repetition_attacks": 0,
            "instruction_injection": 0,
            "size_limit_exceeded": 0,
        }

    def analyze_message(self, session_id: str, message: str) -> List[ContextAttack]:
        """
        Analyze a message for context poisoning attempts.

        Args:
            session_id: Session identifier
            message: Message content to analyze

        Returns:
            List of detected attacks
        """
        attacks = []
        current_time = time.time()

        # Get or create session context
        session = self.sessions.get(session_id)
        if not session:
            session = SessionContext(
                session_id=session_id,
                messages=deque(maxlen=100),  # Keep last 100 messages
                total_characters=0,
                message_count=0,
                context_growth_rate=0,
                last_activity=current_time,
                repeated_content_hashes={},
                instruction_pattern_count=defaultdict(int),
            )
            self.sessions[session_id] = session

        context_size_before = session.total_characters
        message_length = len(message)

        # Check message length limits
        if message_length > self.max_message_length:
            attacks.append(
                ContextAttack(
                    session_id=session_id,
                    attack_type="message_size_limit",
                    severity="high",
                    description=f"Message exceeds size limit ({message_length} > {self.max_message_length})",
                    message_content=(
                        message[:1000] + "..." if len(message) > 1000 else message
                    ),
                    detection_patterns=["message_size_limit"],
                    timestamp=current_time,
                    context_size_before=context_size_before,
                    context_size_after=context_size_before + message_length,
                )
            )
            self.session_metrics["size_limit_exceeded"] += 1
            return attacks  # Skip expensive regex analysis on oversized messages

        # Check total context size
        if context_size_before + message_length > self.max_context_size:
            attacks.append(
                ContextAttack(
                    session_id=session_id,
                    attack_type="context_size_limit",
                    severity="high",
                    description=f"Message would exceed total context limit ({context_size_before + message_length} > {self.max_context_size})",
                    message_content=(
                        message[:1000] + "..." if len(message) > 1000 else message
                    ),
                    detection_patterns=["context_size_limit"],
                    timestamp=current_time,
                    context_size_before=context_size_before,
                    context_size_after=context_size_before + message_length,
                )
            )

        # Check for instruction injection
        instruction_attacks = self._detect_instruction_injection(
            session_id, message, current_time, context_size_before
        )
        attacks.extend(instruction_attacks)

        # Check for repetition attacks
        repetition_attacks = self._detect_repetition_attacks(
            session_id, message, current_time, context_size_before
        )
        attacks.extend(repetition_attacks)

        # Check for rapid context growth
        rapid_growth_attacks = self._detect_rapid_context_growth(
            session, message, current_time, context_size_before
        )
        attacks.extend(rapid_growth_attacks)

        # Check for hidden instructions
        hidden_attacks = self._detect_hidden_instructions(
            session_id, message, current_time, context_size_before
        )
        attacks.extend(hidden_attacks)

        # Update session state
        session.messages.append((current_time, message))
        session.total_characters += message_length
        session.message_count += 1
        session.last_activity = current_time

        # Calculate context growth rate
        time_diff = current_time - session.last_activity
        if time_diff > 0:
            session.context_growth_rate = message_length / time_diff

        # Store attacks
        self.detected_attacks.extend(attacks)

        return attacks

    def _detect_instruction_injection(
        self, session_id: str, message: str, timestamp: float, context_size_before: int
    ) -> List[ContextAttack]:
        """Detect instruction injection attempts."""
        attacks = []
        detected_patterns = []

        for i, pattern in enumerate(self.compiled_patterns):
            matches = pattern.findall(message)
            if matches:
                pattern_name = f"instruction_pattern_{i}"
                detected_patterns.append(pattern_name)

                # Update pattern count for this session
                session = self.sessions[session_id]
                session.instruction_pattern_count[pattern_name] += 1

                # Determine severity based on pattern and frequency
                frequency = session.instruction_pattern_count[pattern_name]
                if frequency > 3:
                    severity = "critical"
                elif i < 6:  # First 6 patterns are more critical
                    severity = "high"
                else:
                    severity = "medium"

                break  # Only report one instruction pattern per message

        if detected_patterns:
            attacks.append(
                ContextAttack(
                    session_id=session_id,
                    attack_type="instruction_injection",
                    severity=severity,
                    description=f"Potential instruction injection detected (patterns: {len(detected_patterns)})",
                    message_content=(
                        message[:500] + "..." if len(message) > 500 else message
                    ),
                    detection_patterns=detected_patterns,
                    timestamp=timestamp,
                    context_size_before=context_size_before,
                    context_size_after=context_size_before + len(message),
                )
            )
            self.session_metrics["instruction_injection"] += 1

        return attacks

    def _detect_repetition_attacks(
        self, session_id: str, message: str, timestamp: float, context_size_before: int
    ) -> List[ContextAttack]:
        """Detect repetition-based context stuffing attacks."""
        attacks = []
        detected_patterns = []

        for i, pattern in enumerate(self.repetition_patterns):
            matches = re.findall(pattern, message, re.DOTALL)
            if matches:
                detected_patterns.append(f"repetition_pattern_{i}")

                # Calculate repetition ratio
                total_repeated_chars = sum(
                    len(match) * (message.count(match) - 1) for match in matches
                )
                repetition_ratio = total_repeated_chars / len(message) if message else 0

                if repetition_ratio > 0.5:
                    severity = "high"
                elif repetition_ratio > 0.3:
                    severity = "medium"
                else:
                    severity = "low"

                break  # Only report one repetition pattern per message

        # Check for content hash repetition across messages
        content_hash = hashlib.md5(message.encode()).hexdigest()
        session = self.sessions[session_id]
        session.repeated_content_hashes[content_hash] = (
            session.repeated_content_hashes.get(content_hash, 0) + 1
        )

        if session.repeated_content_hashes[content_hash] > 3:
            detected_patterns.append("content_hash_repetition")
            severity = "high"

        if detected_patterns:
            attacks.append(
                ContextAttack(
                    session_id=session_id,
                    attack_type="repetition_attack",
                    severity=severity,
                    description="Repetition-based context stuffing detected",
                    message_content=(
                        message[:300] + "..." if len(message) > 300 else message
                    ),
                    detection_patterns=detected_patterns,
                    timestamp=timestamp,
                    context_size_before=context_size_before,
                    context_size_after=context_size_before + len(message),
                )
            )
            self.session_metrics["repetition_attacks"] += 1

        return attacks

    def _detect_rapid_context_growth(
        self,
        session: SessionContext,
        message: str,
        timestamp: float,
        context_size_before: int,
    ) -> List[ContextAttack]:
        """Detect rapid context window filling."""
        attacks = []

        # Check if context is growing unusually fast
        if len(session.messages) > 0:
            time_since_last = timestamp - session.last_activity
            if time_since_last < 60:  # Less than 1 minute
                growth_rate = len(message) / time_since_last
                if growth_rate > 1000:  # More than 1000 chars/second
                    attacks.append(
                        ContextAttack(
                            session_id=session.session_id,
                            attack_type="rapid_context_growth",
                            severity="medium",
                            description=f"Rapid context growth detected ({growth_rate:.1f} chars/sec)",
                            message_content=(
                                message[:200] + "..." if len(message) > 200 else message
                            ),
                            detection_patterns=["rapid_growth"],
                            timestamp=timestamp,
                            context_size_before=context_size_before,
                            context_size_after=context_size_before + len(message),
                        )
                    )
                    self.session_metrics["rapid_context_growth"] += 1

        return attacks

    def _detect_hidden_instructions(
        self, session_id: str, message: str, timestamp: float, context_size_before: int
    ) -> List[ContextAttack]:
        """Detect hidden instructions buried in large text blocks."""
        attacks = []
        detected_patterns = []

        # Check for instruction dilution (instructions hidden in large blocks of text)
        lines = message.split("\n")
        if len(lines) > 50:  # Large message
            # Look for suspicious lines that might be hidden instructions
            instruction_like_lines = []
            for line in lines:
                line_stripped = line.strip().lower()
                if any(
                    keyword in line_stripped
                    for keyword in [
                        "ignore",
                        "disregard",
                        "system",
                        "override",
                        "act as",
                        "pretend",
                    ]
                ):
                    instruction_like_lines.append(line)

            if instruction_like_lines:
                # Calculate the ratio of instruction-like content
                instruction_chars = sum(len(line) for line in instruction_like_lines)
                ratio = instruction_chars / len(message) if message else 0

                if ratio < 0.1:  # Less than 10% - might be dilution attack
                    detected_patterns.append("instruction_dilution")
                    attacks.append(
                        ContextAttack(
                            session_id=session_id,
                            attack_type="hidden_instructions",
                            severity="medium",
                            description=f"Potential instruction dilution attack ({len(instruction_like_lines)} suspicious lines in {len(lines)} total)",
                            message_content="; ".join(instruction_like_lines[:3])
                            + ("..." if len(instruction_like_lines) > 3 else ""),
                            detection_patterns=detected_patterns,
                            timestamp=timestamp,
                            context_size_before=context_size_before,
                            context_size_after=context_size_before + len(message),
                        )
                    )

        return attacks

    def get_session_risk_level(self, session_id: str) -> str:
        """Get risk level for a session based on detected attacks."""
        session_attacks = [
            attack
            for attack in self.detected_attacks
            if attack.session_id == session_id
        ]

        if not session_attacks:
            return "low"

        critical_count = len([a for a in session_attacks if a.severity == "critical"])
        high_count = len([a for a in session_attacks if a.severity == "high"])

        if critical_count > 0:
            return "critical"
        elif high_count > 2:
            return "high"
        elif len(session_attacks) > 5:
            return "medium"
        else:
            return "low"

    def should_block_message(
        self, session_id: str, message: str
    ) -> Tuple[bool, List[str]]:
        """
        Determine if a message should be blocked.

        Returns:
            Tuple of (should_block, reasons)
        """
        attacks = self.analyze_message(session_id, message)
        block_reasons = []

        for attack in attacks:
            if attack.severity == "critical":
                block_reasons.append(
                    f"Critical {attack.attack_type}: {attack.description}"
                )
            elif attack.severity == "high" and attack.attack_type in [
                "message_size_limit",
                "context_size_limit",
            ]:
                block_reasons.append(f"Size limit: {attack.description}")

        return len(block_reasons) > 0, block_reasons

    def get_attack_summary(self) -> Dict[str, Any]:
        """Get summary of detected attacks."""
        return {
            "total_attacks": len(self.detected_attacks),
            "by_type": {
                attack_type: len(
                    [a for a in self.detected_attacks if a.attack_type == attack_type]
                )
                for attack_type in set(a.attack_type for a in self.detected_attacks)
            },
            "by_severity": {
                severity: len(
                    [a for a in self.detected_attacks if a.severity == severity]
                )
                for severity in set(a.severity for a in self.detected_attacks)
            },
            "session_metrics": self.session_metrics,
            "active_sessions": len(self.sessions),
            "high_risk_sessions": [
                session_id
                for session_id in self.sessions.keys()
                if self.get_session_risk_level(session_id) in ["critical", "high"]
            ],
        }

    def cleanup_old_sessions(self, max_age_hours: int = 24):
        """Clean up old session data."""
        current_time = time.time()
        cutoff_time = current_time - (max_age_hours * 3600)

        old_sessions = [
            session_id
            for session_id, session in self.sessions.items()
            if session.last_activity < cutoff_time
        ]

        for session_id in old_sessions:
            del self.sessions[session_id]

        # Also clean old attacks
        self.detected_attacks = [
            attack for attack in self.detected_attacks if attack.timestamp > cutoff_time
        ]

        logger.info(f"Cleaned up {len(old_sessions)} old sessions")

    def export_attack_report(self, output_path: str):
        """Export attack detection report."""
        import json

        report = {
            "timestamp": time.time(),
            "summary": self.get_attack_summary(),
            "attacks": [
                {
                    "session_id": a.session_id,
                    "attack_type": a.attack_type,
                    "severity": a.severity,
                    "description": a.description,
                    "detection_patterns": a.detection_patterns,
                    "timestamp": a.timestamp,
                    "context_size_before": a.context_size_before,
                    "context_size_after": a.context_size_after,
                    "message_preview": a.message_content[:200],
                }
                for a in self.detected_attacks
            ],
        }

        with open(output_path, "w") as f:
            json.dump(report, f, indent=2)

        logger.info(f"Context attack report exported to {output_path}")


# Global instance
global_context_guard = ContextGuard()


def get_context_guard() -> ContextGuard:
    """Get the global context guard instance."""
    return global_context_guard


def check_message(text: str) -> tuple[bool, list[str]]:
    """
    Check if message should be allowed, with detailed findings.

    Args:
        text: Message text to check

    Returns:
        (allowed, findings): True/False if allowed, list of findings/issues
    """
    guard = get_context_guard()

    # Use a dummy session for this check
    session_id = "check_session"

    # Analyze the message
    attacks = guard.analyze_message(session_id, text)

    findings = []
    allowed = True

    # Check for various attack patterns
    for attack in attacks:
        if attack.attack_type == "repetition":
            findings.append(
                f"Repeated pattern detected: {attack.details.get('pattern_preview', 'Unknown pattern')}"
            )
            allowed = False
        elif attack.attack_type == "instruction_injection":
            findings.append("Instruction injection detected")
            allowed = False
        elif attack.attack_type == "hidden_instructions":
            findings.append("Hidden instructions detected")
            allowed = False
        elif attack.attack_type == "rapid_growth":
            findings.append("Rapid context growth detected")
            allowed = False

    # Check message length (500KB default)
    max_length = 500 * 1024  # 500KB
    if len(text.encode("utf-8")) > max_length:
        findings.append(
            f"Message too large: {len(text.encode('utf-8'))} bytes (max {max_length})"
        )
        allowed = False

    # Check for instruction dilution (entropy check)
    unique_chars = len(set(text))
    total_chars = len(text)
    if total_chars > 1000:  # Only check for longer messages
        entropy_ratio = unique_chars / total_chars
        if entropy_ratio < 0.1:  # Very low entropy suggests repetition
            findings.append(
                f"Low entropy detected: {entropy_ratio:.3f} (possible instruction dilution)"
            )
            allowed = False

    # If no issues found, provide positive feedback
    if allowed:
        findings.append("Message passed all security checks")

    return allowed, findings
