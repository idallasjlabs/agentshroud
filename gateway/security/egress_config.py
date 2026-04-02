# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Configuration for the Egress Filter

Defines default allowlists, denylists, and operating modes for egress enforcement.
"""

import os
from dataclasses import dataclass, field
from typing import Dict, List, Set

# Canonical registry of all known service domains that should be pre-approved at startup.
# This is the single source of truth used by EgressFilterConfig.default_allowlist,
# EgressApprovalQueue.SAFE_DOMAINS, and HTTPConnectProxy.ALLOWED_DOMAINS.
#
# SOC retains full runtime control: denying a pre-approved domain via the SOC API
# or Telegram buttons persists a PERMANENT deny rule that overrides this list on
# the next restart (preload_permanent_rules skips domains with existing rules).
PERMANENT_EGRESS_DOMAINS: list[str] = [
    # ── Core Messaging ──
    "api.telegram.org",
    "slack.com",
    "*.slack.com",
    "wss-primary.slack.com",
    "wss-backup.slack.com",
    "edgeapi.slack.com",
    # ── LLM Backends ──
    "api.anthropic.com",
    "api.openai.com",
    "generativelanguage.googleapis.com",
    # ── Google Services ──
    "oauth2.googleapis.com",
    "www.googleapis.com",
    "gmail.googleapis.com",
    # ── Email ──
    "imap.gmail.com",
    "smtp.gmail.com",
    "imap.mail.me.com",
    "smtp.mail.me.com",
    "p154-caldav.icloud.com",
    "*.icloud.com",
    # ── Credential Management ──
    "1password.com",
    "*.1password.com",
    "*.1password.ca",
    "*.b5project.com",
    "*.agilebits.com",
    # ── Search ──
    "api.brave.com",
    "*.brave.com",
    "*.search.brave.com",
    # ── Development & Package Registries ──
    "*.github.com",
    "*.githubusercontent.com",
    "pypi.org",
    "files.pythonhosted.org",
    "registry.npmjs.org",
    "cdnjs.cloudflare.com",
    "unpkg.com",
    "cdn.jsdelivr.net",
    # ── Security Sidecars ──
    "database.clamav.net",
]


@dataclass
class EgressFilterConfig:
    """Configuration for egress filtering enforcement."""

    # Operating mode: "enforce" (block non-allowlisted) or "monitor" (log only)
    mode: str = "enforce"

    # Default domain allowlist - uses canonical PERMANENT_EGRESS_DOMAINS registry
    default_allowlist: List[str] = field(default_factory=lambda: list(PERMANENT_EGRESS_DOMAINS))

    # Denylist - known problematic domains that should always be blocked
    default_denylist: List[str] = field(
        default_factory=lambda: [
            # Pastebin-like services (common exfiltration targets)
            "pastebin.com",
            "*.pastebin.com",
            "hastebin.com",
            "*.hastebin.com",
            "pastie.org",
            "*.pastie.org",
            "paste.ee",
            "*.paste.ee",
            "dpaste.com",
            "*.dpaste.com",
            "controlc.com",
            "*.controlc.com",
            "paste2.org",
            "*.paste2.org",
            "ghostbin.co",
            "*.ghostbin.co",
            "snipplr.com",
            "*.snipplr.com",
            "paste.org.ru",
            "*.paste.org.ru",
            "paste.centos.org",
            "*.paste.centos.org",
            "rentry.co",
            "*.rentry.co",
            # File sharing services
            "wetransfer.com",
            "*.wetransfer.com",
            "sendspace.com",
            "*.sendspace.com",
            "megaupload.com",
            "*.megaupload.com",
            "rapidshare.com",
            "*.rapidshare.com",
            "mediafire.com",
            "*.mediafire.com",
            "zippyshare.com",
            "*.zippyshare.com",
            "temp-mail.org",
            "*.temp-mail.org",
            "10minutemail.com",
            "*.10minutemail.com",
            # URL shorteners (potential for data exfil)
            "bit.ly",
            "tinyurl.com",
            "t.co",
            "goo.gl",
            "ow.ly",
            "short.link",
            "tiny.one",
            # Known malicious/suspect domains
            "discord.com/api/webhooks",  # Discord webhooks often used for exfil
        ]
    )

    # Per-agent allowlist overrides
    agent_allowlists: Dict[str, List[str]] = field(default_factory=dict)

    # Global IP allowlist (CIDR notation supported)
    allowed_ips: List[str] = field(default_factory=list)

    # Allowed ports (empty list means all ports allowed)
    allowed_ports: List[int] = field(default_factory=lambda: [80, 443, 465, 587, 993])

    # Whether to enable strict mode (denylist overrides allowlist)
    strict_mode: bool = True

    # Interactive firewall mode: require approval for all outbound connections,
    # even when destination is allowlisted.
    approval_required_for_all: bool = True

    @classmethod
    def from_environment(cls) -> "EgressFilterConfig":
        """Create config from environment variables and AGENTSHROUD_MODE."""
        mode = "enforce"  # Default to enforce (fail-closed)

        # Check AGENTSHROUD_MODE environment variable
        agentshroud_mode = os.getenv("AGENTSHROUD_MODE", "").lower()
        if agentshroud_mode in ("enforce", "monitor"):
            mode = agentshroud_mode

        # Allow override via specific egress mode env var
        egress_mode = os.getenv("AGENTSHROUD_EGRESS_MODE", "").lower()
        if egress_mode in ("enforce", "monitor"):
            mode = egress_mode

        approval_all_env = os.getenv("AGENTSHROUD_EGRESS_APPROVAL_ALL", "true").strip().lower()
        approval_required_for_all = approval_all_env not in ("0", "false", "no", "off")
        return cls(mode=mode, approval_required_for_all=approval_required_for_all)

    def get_effective_allowlist(self, agent_id: str) -> Set[str]:
        """Get the effective allowlist for a specific agent."""
        allowlist = set(self.default_allowlist)

        # Add agent-specific domains
        if agent_id in self.agent_allowlists:
            allowlist.update(self.agent_allowlists[agent_id])

        # Remove denylisted domains if in strict mode
        if self.strict_mode:
            denylist = set(self.default_denylist)
            # Remove any allowlisted domain that matches a denylist pattern
            allowlist = {
                domain for domain in allowlist if not self._matches_any_pattern(domain, denylist)
            }

        return allowlist

    def is_denylisted(self, domain: str) -> bool:
        """Check if a domain matches the denylist."""
        return self._matches_any_pattern(domain, self.default_denylist)

    def _matches_any_pattern(self, domain: str, patterns: List[str]) -> bool:
        """Check if domain matches any pattern in the list (supports wildcards)."""
        domain = domain.lower().rstrip(".")

        for pattern in patterns:
            pattern = pattern.lower().rstrip(".")

            if pattern.startswith("*."):
                # Wildcard pattern
                base = pattern[2:]
                if domain == base:
                    return True
                if domain.endswith("." + base):
                    # Check it's only one subdomain level
                    prefix = domain[: -(len(base) + 1)]
                    if "." not in prefix:
                        return True
            elif domain == pattern:
                return True

        return False


# Global config instance
_global_config: EgressFilterConfig = EgressFilterConfig.from_environment()


def get_egress_config() -> EgressFilterConfig:
    """Get the global egress filter configuration."""
    return _global_config


def set_egress_config(config: EgressFilterConfig) -> None:
    """Set the global egress filter configuration."""
    global _global_config
    _global_config = config
