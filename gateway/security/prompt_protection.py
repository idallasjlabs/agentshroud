# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""System Prompt Protection for AgentShroud Gateway

Prevents extraction of system prompts, configuration files, and sensitive
internal content by scanning outbound responses and redacting matches.

This module maintains fingerprints of protected content and uses fuzzy
matching to detect disclosure attempts, including verbatim content,
structural patterns, and file references.
"""

from __future__ import annotations

import hashlib
import logging
import re
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

logger = logging.getLogger("agentshroud.security.prompt_protection")


@dataclass
class ProtectedContent:
    """A piece of content that should be protected from disclosure."""

    name: str
    content_hash: str
    patterns: List[re.Pattern]
    structural_markers: List[str]


@dataclass
class RedactionResult:
    """Result of scanning and redacting content."""

    original_text: str
    redacted_text: str
    redactions_made: List[Tuple[str, int, int]]  # (reason, start, end)
    risk_score: float


class PromptProtection:
    """Main system prompt protection engine.

    Maintains fingerprints of sensitive content and scans outbound
    responses to prevent disclosure of system prompts, config files,
    and internal architecture details.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initialize prompt protection system.

        Args:
            config: Configuration dictionary with:
                - fuzzy_threshold: similarity threshold for fuzzy matching (0.0-1.0)
                - protected_files: list of file paths to protect
                - enabled: whether protection is active
        """
        self.config = config or {}
        self.fuzzy_threshold = self.config.get("fuzzy_threshold", 0.7)
        self.enabled = self.config.get("enabled", True)

        # Protected content registry
        self.protected_content: List[ProtectedContent] = []

        # Precompiled patterns for common disclosure attempts
        self._compile_detection_patterns()

        # Load protected content from configuration
        self._load_protected_content()

    def _compile_detection_patterns(self) -> None:
        """Compile regex patterns for detecting disclosure attempts."""

        # File reference patterns
        self.file_patterns = [
            re.compile(r"\b(SOUL\.md|AGENTS\.md|HEARTBEAT\.md|WORKFLOW_AUTO\.md)\b", re.IGNORECASE),
            re.compile(r"\b(memory/\d{4}-\d{2}-\d{2}\.md)\b", re.IGNORECASE),
            re.compile(r"\b(TOOLS\.md|MEMORY\.md|USER\.md)\b", re.IGNORECASE),
        ]

        # System prompt structural patterns
        self.structure_patterns = [
            re.compile(r"## (Core Truths|Boundaries|Safety|Memory)", re.IGNORECASE),
            re.compile(r"\*\*(Stay focused|Complete the task|Don\'t initiate)\*\*", re.IGNORECASE),
            re.compile(r"You are Claude Code|You are a personal assistant", re.IGNORECASE),
            re.compile(r"Tool availability \(filtered by policy\)", re.IGNORECASE),
        ]

        # Tool/MCP inventory patterns
        self.tool_patterns = [
            re.compile(r"Tool names are case-sensitive", re.IGNORECASE),
            re.compile(r"(read|write|edit|exec|process|browser|canvas):\s*[A-Z]", re.IGNORECASE),
            re.compile(r"parameters.*required.*type.*string", re.IGNORECASE),
        ]

        # Infrastructure patterns — targeted only; no generic hostname pattern to avoid
        # false positives on filenames like "file.py" or "test.md".
        self.infrastructure_patterns = [
            re.compile(r"\b((\d{1,3}\.){3}\d{1,3})\b"),  # IP addresses
            re.compile(r"\b([a-zA-Z0-9-]+\.tailscale\.net)\b", re.IGNORECASE),
            # Deployment hostnames are registered dynamically via register_bot_hostnames().
            # No hardcoded host patterns here — they cause false positives on common words.
        ]

        # User ID patterns
        self.user_id_patterns = [
            re.compile(r"\b(\d{9,12})\b"),  # Telegram user IDs
            re.compile(r"@[a-zA-Z0-9_]{3,}"),  # Username patterns
        ]

        # Credential patterns
        self.credential_patterns = [
            re.compile(r"/run/secrets/[a-zA-Z0-9_/-]+", re.IGNORECASE),
            re.compile(r"op://[^\s]+", re.IGNORECASE),
            re.compile(r"\b[a-zA-Z0-9_-]+-vault\b", re.IGNORECASE),
            re.compile(r"\b(API_KEY|TOKEN|SECRET|PASSWORD)\b", re.IGNORECASE),
        ]

    def _load_protected_content(self) -> None:
        """Load protected content from configured sources."""
        protected_files = self.config.get("protected_files", [])

        for file_path in protected_files:
            try:
                path = Path(file_path)
                if path.exists():
                    content = path.read_text(encoding="utf-8")
                    self.add_protected_content(path.name, content)
            except Exception as e:
                logger.warning(f"Failed to load protected file {file_path}: {e}")

    def add_protected_content(self, name: str, content: str) -> None:
        """Add content to the protected registry.

        Args:
            name: Identifier for this content
            content: The sensitive content to protect
        """
        content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()

        # Extract structural markers
        structural_markers = []
        for line in content.split("\n"):
            line = line.strip()
            if line.startswith("#") or line.startswith("**"):
                structural_markers.append(line[:50])  # First 50 chars

        # Create patterns for key phrases
        patterns = []
        sentences = re.split(r"[.!?]+", content)
        for sentence in sentences[:10]:  # Protect first 10 sentences
            sentence = sentence.strip()
            if len(sentence) > 20:
                # Escape special regex chars and make pattern
                escaped = re.escape(sentence)
                patterns.append(re.compile(escaped, re.IGNORECASE))

        protected = ProtectedContent(
            name=name,
            content_hash=content_hash,
            patterns=patterns,
            structural_markers=structural_markers,
        )

        self.protected_content.append(protected)
        logger.info(f"Added protected content: {name} ({len(patterns)} patterns)")

    def scan_response(self, text: str) -> RedactionResult:
        """Scan text for protected content and return redacted version.

        Args:
            text: The text to scan and potentially redact

        Returns:
            RedactionResult with original text, redacted text, and redaction details
        """
        if not self.enabled:
            return RedactionResult(text, text, [], 0.0)

        redacted_text = text
        redactions = []
        risk_score = 0.0

        # Scan for file references
        for pattern in self.file_patterns:
            for match in pattern.finditer(redacted_text):
                redactions.append(("file_reference", match.start(), match.end()))
                risk_score += 15.0
            redacted_text = pattern.sub("[CONTENT]", redacted_text)

        # Scan for structural patterns
        for pattern in self.structure_patterns:
            for match in pattern.finditer(redacted_text):
                redactions.append(("structural_pattern", match.start(), match.end()))
                risk_score += 20.0
            redacted_text = pattern.sub("[STRUCTURE_REDACTED]", redacted_text)

        # Scan for tool inventory disclosure
        for pattern in self.tool_patterns:
            for match in pattern.finditer(redacted_text):
                redactions.append(("tool_inventory", match.start(), match.end()))
                risk_score += 10.0
            redacted_text = pattern.sub("[TOOL_INFO_REDACTED]", redacted_text)

        # Scan for infrastructure details
        for pattern in self.infrastructure_patterns:
            for match in pattern.finditer(redacted_text):
                redactions.append(("infrastructure", match.start(), match.end()))
                risk_score += 25.0
            redacted_text = pattern.sub("[INFRASTRUCTURE_REDACTED]", redacted_text)

        # Scan for user ID patterns
        for pattern in self.user_id_patterns:
            for match in pattern.finditer(redacted_text):
                redactions.append(("user_id", match.start(), match.end()))
                risk_score += 30.0
            redacted_text = pattern.sub("[USER_ID_REDACTED]", redacted_text)

        # Scan for credential patterns
        for pattern in self.credential_patterns:
            for match in pattern.finditer(redacted_text):
                redactions.append(("credential", match.start(), match.end()))
                risk_score += 40.0
            redacted_text = pattern.sub("[CREDENTIAL_REDACTED]", redacted_text)

        # Fuzzy matching against protected content
        for protected in self.protected_content:
            similarity = self._calculate_similarity(text, protected)
            if similarity > self.fuzzy_threshold:
                redacted_text = self._redact_fuzzy_match(redacted_text, protected, similarity)
                redactions.append((f"fuzzy_match_{protected.name}", 0, len(text)))
                risk_score += 50.0 * similarity

        return RedactionResult(
            original_text=text,
            redacted_text=redacted_text,
            redactions_made=redactions,
            risk_score=risk_score,
        )

    def _redact_match(self, text: str, match: re.Match, replacement: str) -> str:
        """Replace a regex match with a redaction placeholder."""
        return text[: match.start()] + replacement + text[match.end() :]

    def _calculate_similarity(self, text: str, protected: ProtectedContent) -> float:
        """Calculate similarity between text and protected content."""
        # Check for exact pattern matches first
        for pattern in protected.patterns:
            if pattern.search(text):
                return 1.0

        # Check structural marker similarity
        text_lines = [line.strip() for line in text.split("\n")]
        marker_matches = 0
        for marker in protected.structural_markers:
            for line in text_lines:
                if SequenceMatcher(None, line, marker).ratio() > 0.8:
                    marker_matches += 1
                    break

        if marker_matches > 0:
            return min(1.0, marker_matches / len(protected.structural_markers))

        return 0.0

    def _redact_fuzzy_match(self, text: str, protected: ProtectedContent, similarity: float) -> str:
        """Redact text that fuzzy matches protected content."""
        confidence = int(similarity * 100)
        return f"[PROTECTED_CONTENT_DETECTED_SIMILARITY_{confidence}%]".strip()

    def register_bot_hostnames(self, hostnames: list[str]) -> None:
        """Add bot container hostnames to the infrastructure detection patterns.

        Called at gateway startup after bots are loaded from config so that
        bot-specific hostnames (e.g. "openclaw", "nanobot") are dynamically
        redacted from responses without hardcoding them here.

        Args:
            hostnames: List of BotConfig.hostname values to protect.
        """
        if not hostnames:
            return
        pattern_str = r"\b(" + "|".join(re.escape(h) for h in hostnames) + r")\b"
        self.infrastructure_patterns.append(re.compile(pattern_str, re.IGNORECASE))
        logger.info("PromptProtection: registered bot hostnames: %s", hostnames)

    def get_protection_stats(self) -> Dict[str, Any]:
        """Get statistics about the protection system."""
        total_patterns = sum(len(pc.patterns) for pc in self.protected_content)

        return {
            "enabled": self.enabled,
            "protected_items": len(self.protected_content),
            "total_patterns": total_patterns,
            "fuzzy_threshold": self.fuzzy_threshold,
            "detection_categories": [
                "file_references",
                "structural_patterns",
                "tool_inventory",
                "infrastructure",
                "user_ids",
                "credentials",
                "fuzzy_matches",
            ],
        }
