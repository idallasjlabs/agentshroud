# Copyright (c) 2026 Isaiah Dallas Jefferson, Jr. AgentShroud. All rights reserved.
# AgentShroud is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Credential Injector — transparent credential injection for outbound requests.

The gateway is the sole credential holder. The agent container has NO access
to secrets. When the agent makes outbound requests, the gateway's egress proxy
intercepts them and injects the appropriate credentials based on destination domain.

Red Team Finding (05-credential-isolation.md):
  Agent had direct access to /run/secrets/ and env vars with credentials.
  "Key isolation is security theater" — the agent could read and export everything.

This module ensures:
  R-10: Gateway is the exclusive credential holder
  R-11: Agent container has no secret files or credential env vars
  R-12: All authenticated requests route through gateway with server-side injection
"""

from __future__ import annotations

import logging
import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)


# Patterns that indicate credential leakage in outbound content
CREDENTIAL_LEAK_PATTERNS: List[Tuple[str, str]] = [
    (r"sk-[a-zA-Z0-9_-]{20,}", "API key (OpenAI/Anthropic format)"),
    (r"AKIA[0-9A-Z]{16}", "AWS access key"),
    (r"ghp_[a-zA-Z0-9]{36}", "GitHub personal access token"),
    (r"gho_[a-zA-Z0-9]{36}", "GitHub OAuth token"),
    (r"op_[a-zA-Z0-9]{26,}", "1Password service account token"),
    (r"eyJ[a-zA-Z0-9_-]{10,}\.eyJ[a-zA-Z0-9_-]{10,}\.", "JWT token"),
    (r"xox[bprs]-[a-zA-Z0-9-]{10,}", "Slack token"),
    (r"GOCSPX-[a-zA-Z0-9_-]{20,}", "Google OAuth client secret"),
    (r"ya29\.[a-zA-Z0-9_-]{50,}", "Google OAuth access token"),
]

_compiled_leak_patterns = [(re.compile(p), desc) for p, desc in CREDENTIAL_LEAK_PATTERNS]


@dataclass
class CredentialMapping:
    """Maps a destination domain to its credential injection config."""

    domain: str
    header_name: str  # e.g., "Authorization", "x-api-key"
    secret_file: str  # path to secret file in /run/secrets/
    header_prefix: str = ""  # e.g., "Bearer " for Authorization headers
    loaded_value: Optional[str] = field(default=None, repr=False)


@dataclass
class CredentialInjectorConfig:
    """Configuration for the credential injector."""

    secrets_dir: str = "/run/secrets"
    enabled: bool = True
    leak_detection: bool = True  # scan outbound content for credential patterns
    mappings: List[CredentialMapping] = field(default_factory=list)


class CredentialInjector:
    """Injects credentials into outbound requests based on destination domain.

    The gateway reads credentials from Docker Secrets at startup and injects
    them into outbound requests server-side. The agent never sees raw credentials.
    """

    def __init__(self, config: Optional[CredentialInjectorConfig] = None):
        self.config = config or CredentialInjectorConfig()
        self._domain_map: Dict[str, CredentialMapping] = {}
        self._load_default_mappings()
        self._load_credentials()

    def _load_default_mappings(self) -> None:
        """Register default domain → credential mappings."""
        defaults = [
            CredentialMapping(
                domain="api.anthropic.com",
                header_name="Authorization",
                secret_file="anthropic_oauth_token",
                header_prefix="Bearer ",
            ),
            CredentialMapping(
                domain="api.openai.com",
                header_name="Authorization",
                secret_file="openai_api_key",
                header_prefix="Bearer ",
            ),
            CredentialMapping(
                domain="generativelanguage.googleapis.com",
                header_name="x-goog-api-key",
                secret_file="google_api_key",
            ),
        ]

        # Add custom mappings from config
        all_mappings = defaults + self.config.mappings

        for mapping in all_mappings:
            self._domain_map[mapping.domain] = mapping

    def _load_credentials(self) -> None:
        """Load credential values from Docker Secrets directory."""
        secrets_dir = Path(self.config.secrets_dir)

        loaded = 0
        for domain, mapping in self._domain_map.items():
            secret_path = secrets_dir / mapping.secret_file
            if secret_path.exists():
                try:
                    value = secret_path.read_text().strip()
                    if value:
                        mapping.loaded_value = value
                        loaded += 1
                        logger.debug(f"Loaded credential for {domain}")
                except Exception as e:
                    logger.warning(f"Failed to load credential for {domain}: {e}")
            else:
                logger.debug(f"Secret file not found for {domain}: {secret_path}")

        logger.info(f"CredentialInjector loaded {loaded}/{len(self._domain_map)} credentials")

    def inject_headers(self, destination_domain: str, headers: Dict[str, str]) -> Dict[str, str]:
        """Inject credentials into request headers based on destination domain.

        Args:
            destination_domain: The target domain (e.g., "api.anthropic.com")
            headers: Mutable dict of request headers

        Returns:
            Updated headers dict (same reference, mutated in place)
        """
        if not self.config.enabled:
            return headers

        mapping = self._domain_map.get(destination_domain)
        if mapping and mapping.loaded_value:
            headers[mapping.header_name] = f"{mapping.header_prefix}{mapping.loaded_value}"
            logger.debug(f"Injected credential for {destination_domain}")

        return headers

    def has_credential(self, domain: str) -> bool:
        """Check if we have a loaded credential for a domain."""
        mapping = self._domain_map.get(domain)
        return mapping is not None and mapping.loaded_value is not None

    def scan_for_credential_leak(self, content: str) -> Optional[str]:
        """Scan outbound content for credential patterns.

        Returns description of detected credential type, or None if clean.
        """
        if not self.config.leak_detection:
            return None

        for pattern, description in _compiled_leak_patterns:
            if pattern.search(content):
                logger.warning(f"CREDENTIAL LEAK DETECTED: {description} found in outbound content")
                return description

        return None

    def get_status(self) -> Dict:
        """Return status for /manage/modules endpoint."""
        loaded = sum(1 for m in self._domain_map.values() if m.loaded_value)
        return {
            "enabled": self.config.enabled,
            "leak_detection": self.config.leak_detection,
            "domains_configured": len(self._domain_map),
            "credentials_loaded": loaded,
            "domains": {
                domain: {"has_credential": m.loaded_value is not None}
                for domain, m in self._domain_map.items()
            },
        }
