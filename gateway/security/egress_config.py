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
from typing import Dict, Iterable, List, Set

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
    # ── Hermes Agent (NousResearch) ──
    "nousresearch.com",
    "*.nousresearch.com",
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
    # DuckDuckGo (no-key web search for hermes ddgs provider — keeps the competitive
    # cron working when the Anthropic OAuth quota is exhausted and the LLM has fallen
    # back to local qwen3-14b. The ddgs package scrapes the HTML front-end, not an API.)
    "duckduckgo.com",
    "html.duckduckgo.com",
    "duckduckgo-search-private.com",
    "*.duckduckgo.com",
    # Failover search engines for hermes web_search (extend DDG pattern: queried
    # when DDG returns 0 results or rate-limits the front-end scraper). All four
    # observed in the egress approval queue during normal hermes operation.
    "search.yahoo.com",
    "www.google.com",
    "yandex.com",
    "www.mojeek.com",
    # ── Web Search / Research (OpenClaw web_search + research tool) ──
    # Observed generating DENY events in production (2026-06-24, audit.db: 210
    # denials, saturating the SOC risk-score gauge to 100%).  Added here so
    # EgressFilterConfig includes them in the default allowlist for all agents.
    "en.wikipedia.org",
    "*.wikipedia.org",
    "startpage.com",
    "www.startpage.com",
    "*.startpage.com",
    "grokipedia.com",
    "*.grokipedia.com",
    # ── AI-Security Research / Competitive Intel (Hermes research cron, 2026-06-25) ──
    # Domains observed blocked in production during Hermes blue-team/competitive-intel
    # research tasks. All are reputable public AI-security vendors/gov sources.
    # Authorized by Isaiah Jefferson 2026-06-25 for Hermes web_extract tool use.
    "nist.gov",
    "www.nist.gov",
    "lakera.ai",
    "www.lakera.ai",
    "paloaltonetworks.com",
    "www.paloaltonetworks.com",
    "menlosecurity.com",
    "www.menlosecurity.com",
    "adversa.ai",
    "www.adversa.ai",
    "neuraltrust.ai",
    "www.neuraltrust.ai",
    "atlan.com",
    "www.atlan.com",
    "mintmcp.com",
    "www.mintmcp.com",
    # GitHub static asset host — NOT covered by *.github.com (different apex).
    "github.githubassets.com",
    "*.githubassets.com",
    # ── Development & Package Registries ──
    "*.github.com",
    "*.githubusercontent.com",
    "pypi.org",
    "files.pythonhosted.org",
    "registry.npmjs.org",
    "cdnjs.cloudflare.com",
    "unpkg.com",
    "cdn.jsdelivr.net",
    # ── Health Checks ──
    "status.docker.com",
    "status.aws.amazon.com",
    "hc-ping.com",  # Healthchecks.io dead-man's-switch (hermes heartbeat)
    # ── Security Sidecars ──
    "database.clamav.net",
    # ── LLM Routing (local proxy) ──
    "openrouter.ai",
    "*.openrouter.ai",
    # ── Atlassian (Jira + Confluence — SCRUM board, dev-batch ticket tracking) ──
    "atlassian.net",
    "*.atlassian.net",
    "atlassian.com",
    "*.atlassian.com",
    # ── Feedbin / Daily-Brief podcast workstream (owner brief 2026-08-29) ──
    # Service endpoints:
    "api.feedbin.com",  # subscription/tagging/entry management (Basic auth)
    "news.google.com",  # gnews: shorthand feeds in feeds.yaml
    "idallasj.github.io",  # published feed verification (GitHub Pages)
    "api.podcastindex.org",  # weekly podcast discovery
    "itunes.apple.com",  # iTunes Search API (podcast discovery, no key)
    "api.elevenlabs.io",  # pke pipeline TTS (episode audio)
]

# Feed-source hosts for full-article fetches of top Daily-Brief clusters —
# GENERATED from feeds.yaml via `feedbin.py hosts` (see feed_hosts.py header);
# extends the same canonical registry rather than a second policy surface.
from gateway.security.feed_hosts import FEED_HOSTS  # noqa: E402

PERMANENT_EGRESS_DOMAINS.extend(h for h in FEED_HOSTS if h not in PERMANENT_EGRESS_DOMAINS)


def domain_matches(domain: str, patterns: Iterable[str]) -> bool:
    """Return True if *domain* matches any pattern (exact or ``*.`` wildcard).

    Single source of truth for allowlist/denylist domain matching, shared by
    ``EgressFilterConfig`` and the citation verifier.  Wildcards match exactly
    one subdomain level (``*.example.com`` matches ``a.example.com`` and
    ``example.com`` but not ``a.b.example.com``).
    """
    domain = domain.lower().rstrip(".")
    for pattern in patterns:
        pattern = pattern.lower().rstrip(".")
        if pattern.startswith("*."):
            base = pattern[2:]
            if domain == base:
                return True
            if domain.endswith("." + base):
                prefix = domain[: -(len(base) + 1)]
                if "." not in prefix:
                    return True
        elif domain == pattern:
            return True
    return False


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
    # Populated from AGENTSHROUD_ALLOWED_IPS env var (comma-separated)
    allowed_ips: List[str] = field(default_factory=list)

    # Allowed ports (empty list means all ports allowed)
    # Populated from AGENTSHROUD_ALLOWED_PORTS env var (comma-separated)
    # Defaults: 80, 443, 465 (SMTPS), 587 (submission), 993 (IMAPS)
    allowed_ports: List[int] = field(default_factory=lambda: [80, 443, 465, 587, 993])

    # Whether to enable strict mode (denylist overrides allowlist)
    strict_mode: bool = True

    # Interactive firewall mode: require approval for all outbound connections,
    # even when destination is allowlisted.
    # Default is False — production deployment sets AGENTSHROUD_EGRESS_APPROVAL_ALL=false
    # in docker-compose.yml.  Set to True only for maximum-friction environments.
    approval_required_for_all: bool = False

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

        # Parse allowed IPs from env (comma-separated, e.g. "192.168.7.137/32,10.0.0.5/32")
        allowed_ips: List[str] = []
        allowed_ips_env = os.getenv("AGENTSHROUD_ALLOWED_IPS", "").strip()
        if allowed_ips_env:
            allowed_ips = [ip.strip() for ip in allowed_ips_env.split(",") if ip.strip()]

        # Parse allowed ports from env (comma-separated, e.g. "22,80,443")
        # Falls back to class default if env var is absent
        allowed_ports_env = os.getenv("AGENTSHROUD_ALLOWED_PORTS", "").strip()
        kwargs: dict = dict(
            mode=mode,
            approval_required_for_all=approval_required_for_all,
            allowed_ips=allowed_ips,
        )
        if allowed_ports_env:
            kwargs["allowed_ports"] = [
                int(p.strip()) for p in allowed_ports_env.split(",") if p.strip().isdigit()
            ]

        return cls(**kwargs)

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
        return domain_matches(domain, patterns)

    def matches_allowlist(self, domain: str) -> bool:
        """Public: does *domain* match any pattern in the effective default allowlist?

        Exposes the same exact / single-level-wildcard semantics used by egress
        enforcement so other modules (e.g. the citation verifier) can check
        allowlist membership without reaching into a private method.
        """
        return domain_matches(domain, self.default_allowlist)


# Global config instance
_global_config: EgressFilterConfig = EgressFilterConfig.from_environment()


def get_egress_config() -> EgressFilterConfig:
    """Get the global egress filter configuration."""
    return _global_config


def set_egress_config(config: EgressFilterConfig) -> None:
    """Set the global egress filter configuration."""
    global _global_config
    _global_config = config
