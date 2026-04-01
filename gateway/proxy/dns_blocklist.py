"""
AgentShroud DNS Blocklist — Pi-hole-compatible domain blocking for the gateway.

Downloads and parses standard adblock/hosts-format blocklists (same sources
Pi-hole uses), checks every DNS query against them, and returns 0.0.0.0/::
for blocked domains.

Supports:
  - hosts-format lists (0.0.0.0 domain.com or 127.0.0.1 domain.com)
  - domain-only lists (one domain per line)
  - comments (#) and blank lines
  - Wildcard blocking (block *.example.com by blocking example.com)
  - Custom allow/deny lists
  - Periodic background updates

Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""

import asyncio
import logging
import os
import re
import time
from pathlib import Path
from typing import Optional, Set

logger = logging.getLogger("agentshroud.dns_blocklist")

# ── Default blocklists (same as Pi-hole defaults) ────────────────────────────
DEFAULT_BLOCKLISTS = [
    # StevenBlack's unified hosts (ads + malware)
    "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
    # Hagezi light blocklist (maintained, hosts format)
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/hosts/light.txt",
]

# Domains that should NEVER be blocked (critical infrastructure)
SYSTEM_ALLOWLIST = {
    "localhost",
    "gateway",
    "agentshroud",
    # API endpoints the bot needs
    "api.anthropic.com",
    "api.telegram.org",
    "api.openai.com",
    "my.1password.com",
    "api.brave.com",
    "imap.gmail.com",
    "smtp.gmail.com",
}

# Data directory for cached blocklists
DATA_DIR = Path(os.environ.get("AGENTSHROUD_DATA_DIR", "/app/data")) / "dns"

# How often to refresh blocklists (24 hours)
UPDATE_INTERVAL_SECONDS = 86400


class DNSBlocklist:
    """Domain blocklist with Pi-hole-compatible list parsing."""

    def __init__(
        self,
        blocklist_urls: Optional[list] = None,
        custom_allowlist: Optional[Set[str]] = None,
        custom_denylist: Optional[Set[str]] = None,
        data_dir: Optional[Path] = None,
    ):
        self.blocklist_urls = blocklist_urls or DEFAULT_BLOCKLISTS
        self.blocked_domains: Set[str] = set()
        self.allowlist: Set[str] = SYSTEM_ALLOWLIST.copy()
        self.denylist: Set[str] = set()
        self.data_dir = data_dir or DATA_DIR
        self.last_update: float = 0
        self.update_task: Optional[asyncio.Task] = None
        self._lock = asyncio.Lock()

        if custom_allowlist:
            self.allowlist.update(custom_allowlist)
        if custom_denylist:
            self.denylist.update(custom_denylist)

        # Create data directory
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def is_blocked(self, domain: str) -> bool:
        """Check if a domain should be blocked.

        Checks the domain and all parent domains (wildcard blocking).
        Allowlist takes priority over blocklist.
        Custom denylist always blocks.
        """
        domain = domain.lower().rstrip(".")

        # Allowlist always wins
        if domain in self.allowlist:
            return False

        # Custom denylist always blocks
        if domain in self.denylist:
            return True

        # Check exact match
        if domain in self.blocked_domains:
            return True

        # Check parent domains (wildcard blocking)
        # e.g., if "doubleclick.net" is blocked, "ad.doubleclick.net" is also blocked
        parts = domain.split(".")
        for i in range(1, len(parts)):
            parent = ".".join(parts[i:])
            if parent in self.allowlist:
                return False
            if parent in self.blocked_domains:
                return True

        return False

    def parse_hosts_line(self, line: str) -> Optional[str]:
        """Parse a single line from a hosts-format or domain-only blocklist.

        Supports:
          - "0.0.0.0 domain.com" (hosts format)
          - "127.0.0.1 domain.com" (hosts format)
          - "domain.com" (domain-only format)
          - "||domain.com^" (adblock filter format, basic)
        """
        line = line.strip()

        # Skip empty lines and comments
        if not line or line.startswith("#") or line.startswith("!"):
            return None

        # Hosts format: "0.0.0.0 domain.com" or "127.0.0.1 domain.com"
        if line.startswith(("0.0.0.0", "127.0.0.1")):
            parts = line.split()
            if len(parts) >= 2:
                domain = parts[1].lower().strip()
                # Skip localhost entries
                if domain in ("localhost", "localhost.localdomain", "local",
                              "broadcasthost", "ip6-localhost", "ip6-loopback",
                              "ip6-localnet", "ip6-mcastprefix", "ip6-allnodes",
                              "ip6-allrouters", "ip6-allhosts"):
                    return None
                # Basic domain validation
                if "." in domain and not domain.startswith("."):
                    return domain
            return None

        # Adblock filter format: "||domain.com^"
        if line.startswith("||") and line.endswith("^"):
            domain = line[2:-1].lower().strip()
            if "." in domain and re.match(r'^[a-z0-9.-]+$', domain):
                return domain
            return None

        # Domain-only format (one domain per line)
        line_lower = line.lower().split("#")[0].strip()  # Remove inline comments
        if line_lower and "." in line_lower and re.match(r'^[a-z0-9.-]+$', line_lower):
            if " " not in line_lower and len(line_lower) < 256:
                return line_lower

        return None

    def load_from_text(self, text: str) -> int:
        """Parse blocklist text and add domains. Returns count of new domains."""
        count = 0
        for line in text.split("\n"):
            domain = self.parse_hosts_line(line)
            if domain and domain not in self.allowlist:
                self.blocked_domains.add(domain)
                count += 1
        return count

    async def download_blocklist(self, url: str) -> Optional[str]:
        """Download a blocklist URL. Uses the gateway's own HTTP client."""
        cache_file = self.data_dir / f"blocklist_{hash(url) & 0xFFFFFFFF:08x}.txt"

        try:
            import urllib.request
            import ssl

            # Download with timeout
            ctx = ssl.create_default_context()
            req = urllib.request.Request(url, headers={"User-Agent": "AgentShroud/1.0.0"})
            response = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: urllib.request.urlopen(req, timeout=30, context=ctx).read().decode("utf-8", errors="replace"),
            )

            # Cache to disk
            cache_file.write_text(response)
            logger.info(f"Downloaded blocklist: {url} ({len(response)} bytes)")
            return response

        except Exception as e:
            logger.warning(f"Failed to download blocklist {url}: {e}")

            # Fall back to cached version
            if cache_file.exists():
                logger.info(f"Using cached blocklist for {url}")
                return cache_file.read_text()

            return None

    async def update(self):
        """Download all blocklists and rebuild the blocked domains set."""
        async with self._lock:
            logger.info(f"Updating DNS blocklists ({len(self.blocklist_urls)} sources)...")
            start = time.monotonic()

            new_domains: Set[str] = set()
            new_domains.update(self.denylist)  # Always include custom denylist

            for url in self.blocklist_urls:
                text = await self.download_blocklist(url)
                if text:
                    count_before = len(new_domains)
                    for line in text.split("\n"):
                        domain = self.parse_hosts_line(line)
                        if domain and domain not in self.allowlist:
                            new_domains.add(domain)
                    added = len(new_domains) - count_before
                    logger.info(f"  {url}: +{added} domains")

            self.blocked_domains = new_domains
            self.last_update = time.time()
            elapsed = time.monotonic() - start

            logger.info(
                f"DNS blocklist updated: {len(self.blocked_domains)} blocked domains "
                f"({elapsed:.1f}s)"
            )

    async def start_periodic_updates(self):
        """Start background task for periodic blocklist updates."""
        self.update_task = asyncio.create_task(self._periodic_update_loop())

    async def _periodic_update_loop(self):
        """Background loop: update blocklists every UPDATE_INTERVAL_SECONDS."""
        while True:
            await asyncio.sleep(UPDATE_INTERVAL_SECONDS)
            try:
                await self.update()
            except Exception as e:
                logger.error(f"Blocklist update failed: {e}")

    def stop(self):
        """Stop periodic updates."""
        if self.update_task and not self.update_task.done():
            self.update_task.cancel()

    def stats(self) -> dict:
        """Return blocklist statistics."""
        return {
            "blocked_domains": len(self.blocked_domains),
            "allowlist_size": len(self.allowlist),
            "denylist_size": len(self.denylist),
            "last_update": self.last_update,
            "blocklist_sources": len(self.blocklist_urls),
        }
