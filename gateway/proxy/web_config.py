"""
Web Proxy Configuration — settings for HTTP traffic proxying.

Default-allow policy: everything passes unless explicitly denied or SSRF.
"""

import logging
from dataclasses import dataclass, field
from typing import Optional

logger = logging.getLogger("secureclaw.proxy.web_config")


@dataclass
class DomainSettings:
    """Per-domain configuration overrides."""
    max_response_bytes: int = 15 * 1024 * 1024  # 15MB
    allowed_content_types: list[str] = field(default_factory=list)  # empty = all
    rate_limit_rpm: int = 120  # requests per minute
    timeout_seconds: float = 30.0


@dataclass
class WebProxyConfig:
    """Configuration for the web traffic proxy.

    Default-allow: all URLs pass unless they hit the denylist or are SSRF.
    Prompt injection / PII findings are flagged, not blocked.
    """

    # --- Domain lists ---
    # Denylist: hard-blocked domains (known malicious, phishing, etc.)
    denied_domains: list[str] = field(default_factory=lambda: [
        "evil.com",
        "malware-payload.net",
        "phishing-site.org",
        "prompt-inject.attacker.com",
    ])

    # Per-domain settings overrides (domain -> DomainSettings)
    domain_settings: dict[str, DomainSettings] = field(default_factory=dict)

    # --- Response limits ---
    default_max_response_bytes: int = 15 * 1024 * 1024  # 15MB
    default_timeout_seconds: float = 30.0

    # --- Rate limiting ---
    default_rate_limit_rpm: int = 120  # per domain, per minute

    # --- Content type filtering ---
    # Empty = allow all. If set, only these content types pass without a flag.
    allowed_content_types: list[str] = field(default_factory=list)
    # Content types that always get flagged (but still passed through)
    suspicious_content_types: list[str] = field(default_factory=lambda: [
        "application/x-executable",
        "application/x-msdos-program",
        "application/x-msdownload",
    ])

    # --- Prompt injection scanning ---
    scan_responses: bool = True
    # Flag threshold (0.0-1.0). Content above this gets flagged but still returned.
    prompt_injection_flag_threshold: float = 0.3

    # --- PII detection ---
    detect_pii_in_urls: bool = True
    detect_pii_in_responses: bool = True

    # --- SSRF protection (always hard-block) ---
    block_private_ips: bool = True

    # --- Passthrough / debug mode ---
    passthrough_mode: bool = False  # If True, skip all checks, just log

    # --- Logging ---
    log_request_headers: bool = False
    log_response_headers: bool = True
    log_response_body_preview: int = 500  # chars of body to log (0 = none)

    def get_domain_settings(self, domain: str) -> DomainSettings:
        """Get settings for a specific domain, falling back to defaults."""
        if domain in self.domain_settings:
            return self.domain_settings[domain]
        # Check wildcard matches
        parts = domain.split(".")
        for i in range(len(parts) - 1):
            wildcard = "*." + ".".join(parts[i + 1:])
            if wildcard in self.domain_settings:
                return self.domain_settings[wildcard]
        return DomainSettings(
            max_response_bytes=self.default_max_response_bytes,
            rate_limit_rpm=self.default_rate_limit_rpm,
            timeout_seconds=self.default_timeout_seconds,
        )

    def is_domain_denied(self, domain: str) -> bool:
        """Check if a domain is on the denylist."""
        domain = domain.lower().rstrip(".")
        for denied in self.denied_domains:
            denied = denied.lower().rstrip(".")
            if domain == denied:
                return True
            if domain.endswith("." + denied):
                return True
        return False
