# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""PII Sanitization Engine for AgentShroud Gateway

Detects and redacts personally identifiable information using:
1. Microsoft Presidio with spaCy (if available)
2. Regex patterns (fallback)
"""
from __future__ import annotations


import asyncio
import logging
import re
from typing import Literal

from .config import PIIConfig
from .models import RedactionDetail, RedactionResult

logger = logging.getLogger("agentshroud.gateway.sanitizer")


class PIISanitizer:
    """PII detection and redaction engine

    Attempts to use Microsoft Presidio with spaCy NLP for accurate detection.
    Falls back to regex patterns if Presidio/spaCy unavailable.
    """

    def __init__(self, config: PIIConfig):
        """Initialize sanitizer

        Args:
            config: PII configuration from agentshroud.yaml
        """
        self.config = config
        self.mode: Literal["presidio", "regex"] = "regex"
        self.analyzer = None
        self.anonymizer = None

        # Precompile regex patterns for block_credentials performance
        self._totp_pattern = re.compile(
            r"(?:totp|otp|one.time|verification|2fa|mfa)[:\s]+\d{6}\b",
            re.IGNORECASE | re.MULTILINE,
        )
        self._entropy_pattern = re.compile(
            r"\b(?=[A-Za-z0-9!@#$%^&*]*[A-Z])(?=[A-Za-z0-9!@#$%^&*]*[a-z])(?=[A-Za-z0-9!@#$%^&*]*[0-9])(?=[A-Za-z0-9!@#$%^&*]*[!@#$%^&*])[A-Za-z0-9!@#$%^&*]{16,}\b"
        )
        self._aws_key_pattern = re.compile(r"\bAKIA[0-9A-Z]{16}\b")

        # Precompiled XML block patterns for filter_xml_blocks
        self._xml_block_patterns = [
            # Closed pairs (DOTALL so .* matches newlines)
            re.compile(r"<function_calls>.*?</function_calls>", re.DOTALL),
            re.compile(r"<function_results>.*?</function_results>", re.DOTALL),
            re.compile(r"<thinking>.*?</thinking>", re.DOTALL),
            re.compile(r"<system-reminder>.*?</system-reminder>", re.DOTALL),
            re.compile(r"<invoke[^>]*>.*?</invoke>", re.DOTALL),
            re.compile(r"<parameter[^>]*>.*?</parameter>", re.DOTALL),
            # Unclosed/truncated variants (match to end of string)
            re.compile(r"<function_calls>(?:(?!</function_calls>).)*$", re.DOTALL),
            re.compile(r"<function_results>(?:(?!</function_results>).)*$", re.DOTALL),
            re.compile(r"<thinking>(?:(?!</thinking>).)*$", re.DOTALL),
            re.compile(r"<system-reminder>(?:(?!</system-reminder>).)*$", re.DOTALL),
            re.compile(r"<invoke[^>]*>(?:(?!</invoke>).)*$", re.DOTALL),
        ]
        # Whitespace cleanup pattern
        self._excessive_newlines_pattern = re.compile(r"\n{3,}")

        if config.engine == "presidio":
            self._init_presidio()
        else:
            logger.info("Using regex-based PII detection (fallback mode)")

    def _init_presidio(self) -> None:
        """Initialize Microsoft Presidio engines

        Falls back to regex if Presidio/spaCy unavailable or incompatible.
        """
        # Check Python version first - Presidio incompatible with Python 3.14+
        import sys

        if sys.version_info >= (3, 14):
            logger.warning(
                f"Python {sys.version_info.major}.{sys.version_info.minor} detected. "
                "Presidio/spaCy not yet compatible with Python 3.14+. Using regex fallback."
            )
            self.mode = "regex"
            return

        try:
            from presidio_analyzer import AnalyzerEngine
            from presidio_anonymizer import AnonymizerEngine

            # Test if spaCy model is available and working
            try:
                import spacy

                # Try to load the model
                spacy.load("en_core_web_sm")
                logger.info("spaCy model en_core_web_sm loaded successfully")

                # Initialize Presidio engines with our specific spaCy model
                from presidio_analyzer.nlp_engine import NlpEngineProvider
                nlp_config = {
                    "nlp_engine_name": "spacy",
                    "models": [{"lang_code": "en", "model_name": "en_core_web_sm"}],
                }
                nlp_engine = NlpEngineProvider(nlp_configuration=nlp_config).create_engine()
                self.analyzer = AnalyzerEngine(nlp_engine=nlp_engine, supported_languages=["en"])
                self.anonymizer = AnonymizerEngine()
                self.mode = "presidio"
                logger.info("Presidio PII detection engine initialized")

            except (OSError, Exception) as e:
                logger.warning(
                    f"spaCy model not available or incompatible: {e}. "
                    "Using regex fallback."
                )
                self.mode = "regex"

        except ImportError as e:
            logger.warning(
                f"Presidio not installed: {e}. Using regex fallback for PII detection."
            )
            self.mode = "regex"

    async def sanitize(self, content: str) -> RedactionResult:
        """Detect and redact PII from content

        Args:
            content: Text to sanitize

        Returns:
            RedactionResult with sanitized content and redaction details

        Raises:
            RuntimeError: If sanitization fails critically
        """
        if not self.config.enabled:
            return RedactionResult(
                sanitized_content=content,
                redactions=[],
                entity_types_found=[],
            )

        if self.mode == "presidio" and self.analyzer and self.anonymizer:
            # Hybrid: run Presidio first, then regex to catch gaps
            # (en_core_web_sm misses SSN/phone; regex catches them)
            presidio_result = await self._sanitize_presidio(content)
            regex_result = await self._sanitize_regex(presidio_result.sanitized_content)
            # Merge redactions from both passes
            all_redactions = presidio_result.redactions + regex_result.redactions
            all_types = list(set(presidio_result.entity_types_found + regex_result.entity_types_found))
            return RedactionResult(
                sanitized_content=regex_result.sanitized_content,
                redactions=all_redactions,
                entity_types_found=all_types,
            )
        else:
            return await self._sanitize_regex(content)

    async def _sanitize_presidio(self, content: str) -> RedactionResult:
        """Sanitize using Microsoft Presidio

        Wraps synchronous Presidio calls in asyncio.to_thread to avoid blocking.
        """

        def _analyze_and_anonymize() -> RedactionResult:
            # Map internal entity names to Presidio names
            entities = self.config.entities

            # Analyze
            results = self.analyzer.analyze(
                text=content, entities=entities, language="en"
            )

            # Filter by confidence
            results = [r for r in results if r.score >= self.config.min_confidence]

            if not results:
                return RedactionResult(
                    sanitized_content=content, redactions=[], entity_types_found=[]
                )

            # Anonymize
            anonymized = self.anonymizer.anonymize(
                text=content, analyzer_results=results
            )

            # Build redaction details
            redactions = [
                RedactionDetail(
                    entity_type=r.entity_type,
                    start=r.start,
                    end=r.end,
                    score=r.score,
                    replacement=f"<{r.entity_type}>",
                )
                for r in results
            ]

            entity_types = list(set(r.entity_type for r in results))

            return RedactionResult(
                sanitized_content=anonymized.text,
                redactions=redactions,
                entity_types_found=entity_types,
            )

        try:
            return await asyncio.to_thread(_analyze_and_anonymize)
        except Exception as e:
            logger.error(f"Presidio sanitization failed: {e}. Falling back to regex.")
            return await self._sanitize_regex(content)

    async def _sanitize_regex(self, content: str) -> RedactionResult:
        """Sanitize using regex patterns (fallback mode)

        Detects:
        - US_SSN: XXX-XX-XXXX
        - CREDIT_CARD: 4111-1111-1111-1111 (with various formats)
        - PHONE_NUMBER: (555) 123-4567, 555-123-4567, etc.
        - EMAIL_ADDRESS: user@domain.com
        - LOCATION: Basic street address patterns
        """
        sanitized = content
        redactions: list[RedactionDetail] = []

        # Define patterns (order matters - longer patterns first)
        patterns = []

        # If no entities configured, detect all by default
        entities = self.config.entities or [
            "US_SSN", "CREDIT_CARD", "PHONE_NUMBER", "EMAIL_ADDRESS", "LOCATION"
        ]

        if "US_SSN" in entities:
            patterns.append(
                (
                    "US_SSN",
                    re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),  # XXX-XX-XXXX
                    "<US_SSN>",
                )
            )

        if "CREDIT_CARD" in entities:
            # Matches various credit card formats
            patterns.append(
                (
                    "CREDIT_CARD",
                    re.compile(
                        r"\b(?:\d{4}[-\s]?){3}\d{4}\b"  # 4111-1111-1111-1111 or 4111 1111 1111 1111
                    ),
                    "<CREDIT_CARD>",
                )
            )

        if "PHONE_NUMBER" in entities:
            patterns.append(
                (
                    "PHONE_NUMBER",
                    re.compile(
                        r"\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
                    ),
                    "<PHONE_NUMBER>",
                )
            )

        if "EMAIL_ADDRESS" in entities:
            patterns.append(
                (
                    "EMAIL_ADDRESS",
                    re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"),
                    "<EMAIL_ADDRESS>",
                )
            )

        if "LOCATION" in entities:
            # Basic street address pattern (number + street name)
            patterns.append(
                (
                    "LOCATION",
                    re.compile(
                        r"\b\d+\s+[A-Z][a-z]+\s+(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct|Way)\b",
                        re.IGNORECASE,
                    ),
                    "<LOCATION>",
                )
            )

        # Apply all patterns
        for entity_type, pattern, replacement in patterns:
            for match in pattern.finditer(content):
                redactions.append(
                    RedactionDetail(
                        entity_type=entity_type,
                        start=match.start(),
                        end=match.end(),
                        score=1.0,  # Regex has 100% confidence in matches
                        replacement=replacement,
                    )
                )

        # Sort redactions by start position (reverse order for replacement)
        redactions.sort(key=lambda r: r.start, reverse=True)

        # Apply replacements (reverse order to maintain positions)
        for redaction in redactions:
            sanitized = (
                sanitized[: redaction.start]
                + redaction.replacement
                + sanitized[redaction.end :]
            )

        # Get unique entity types
        entity_types = list(set(r.entity_type for r in redactions))

        return RedactionResult(
            sanitized_content=sanitized,
            redactions=list(reversed(redactions)),  # Restore original order
            entity_types_found=entity_types,
        )

    def get_supported_entities(self) -> list[str]:
        """Return list of entity types currently enabled

        Returns:
            List of entity type names
        """
        return self.config.entities

    def get_mode(self) -> str:
        """Return current detection mode

        Returns:
            "presidio" or "regex"
        """
        return self.mode

    async def block_credentials(self, content: str, source: str) -> tuple[str, bool]:
        """Block credential display via untrusted sources (e.g., Telegram)

        Args:
            content: Response text to check
            source: Source of request

        Allowed sources (credentials NOT blocked):
            - console: Direct docker exec commands
            - localhost: Browser at 127.0.0.1
            - control_ui: OpenClaw Control UI (localhost or Tailscale)
            - tailscale: Access via Tailscale network
            - api: API calls from trusted sources

        Blocked sources (credentials blocked):
            - telegram: Telegram messaging (remote/untrusted)
            - external_api: External API calls
            - remote: General remote access
            - untrusted: Explicitly untrusted sources

        Returns:
            Tuple of (sanitized_content, was_blocked)
                - sanitized_content: Original or redacted content
                - was_blocked: True if credentials were detected and blocked
        """
        # Only block for untrusted remote sources
        # Allow: console, localhost, control_ui, tailscale, api (from trusted sources)
        blocked_sources = ["telegram", "external_api", "remote", "untrusted"]

        if source not in blocked_sources:
            return (content, False)

        # Patterns that indicate credentials are being displayed
        credential_patterns = [
            # Password displays
            (
                r'password[:\s]+[\w!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]{8,}',
                "password",
            ),
            # JSON formatted credentials (from op item get --format json)
            (
                r'"value":\s*"[\w!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]{8,}"',
                "json_credential",
            ),
            (
                r'"password":\s*"[\w!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]{8,}"',
                "json_password",
            ),
            # API keys
            (r"\b(sk-[a-zA-Z0-9]{20,})", "openai_api_key"),
            (r"\bghp_[a-zA-Z0-9]{36}", "github_token"),
            (self._aws_key_pattern, "aws_access_key"),
            (r"\bops_[a-zA-Z0-9]{26}", "1password_token"),
            # Generic API key patterns
            (r"api[_\s]?key[:\s]+[\w\-]{20,}", "api_key"),
            (r"secret[:\s]+[\w\-]{20,}", "secret"),
            (r"token[:\s]+[\w\-]{20,}", "token"),
            # TOTP codes (only in context of OTP/TOTP/one-time/verification)
            (self._totp_pattern, "totp_code"),
            # High entropy strings that look like passwords (require mixed case + special chars)
            (self._entropy_pattern, "high_entropy_string"),
            # SSH private keys
            (r"-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----", "ssh_private_key"),
            # Credit cards (catch in case PII sanitizer missed)
            (r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b", "credit_card"),
            # SSN (catch in case PII sanitizer missed)
            (r"\b\d{3}-\d{2}-\d{4}\b", "ssn"),
        ]

        # Check for credential patterns
        for pattern, cred_type in credential_patterns:
            # Pattern can be either a string or compiled regex
            if isinstance(pattern, re.Pattern):
                match = pattern.search(content)
            else:
                match = re.search(pattern, content, re.IGNORECASE | re.MULTILINE)

            if match:
                logger.warning(f"Blocked {cred_type} from being displayed via {source}")

                # Return blocking message
                blocked_message = (
                    "🔒 [REDACTED: Credentials cannot be displayed via Telegram]\n\n"
                    "For security, passwords and secrets are only accessible via:\n"
                    "• Console: docker exec openclaw-bot get-credential <name>\n"
                    "• Control UI: http://localhost:18790\n\n"
                    "If you need to configure a service, ask me to do it. "
                    "I can use credentials internally without displaying them."
                )
                return (blocked_message, True)

        return (content, False)

    def filter_xml_blocks(self, content: str) -> tuple[str, bool]:
        """Remove Claude XML function call blocks from responses

        Strips out internal Claude tool use blocks that should not be shown to users:
        - <function_calls>...</function_calls>
        - <function_results>...</function_results>
        - <thinking>...</thinking>
        - <system-reminder>...</system-reminder>

        Args:
            content: Response text from Claude that may contain XML blocks

        Returns:
            Tuple of (filtered_content, was_filtered)
                - filtered_content: Content with XML blocks removed
                - was_filtered: True if any XML blocks were found and removed
        """
        filtered = content

        for pattern in self._xml_block_patterns:
            filtered = pattern.sub("", filtered)

        # Collapse 3+ newlines to 2
        filtered = self._excessive_newlines_pattern.sub("\n\n", filtered)
        filtered = filtered.strip()

        return (filtered, filtered != content.strip())
