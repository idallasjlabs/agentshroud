# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Configuration for the Egress Filter

Defines default allowlists, denylists, and operating modes for egress enforcement.
"""

import os
from dataclasses import dataclass, field
from typing import Dict, List, Set


@dataclass 
class EgressFilterConfig:
    """Configuration for egress filtering enforcement."""
    
    # Operating mode: "enforce" (block non-allowlisted) or "monitor" (log only)
    mode: str = "enforce"
    
    # Default domain allowlist - essential domains for agent operation
    default_allowlist: List[str] = field(default_factory=lambda: [
        # AI API endpoints
        "api.anthropic.com",
        "api.openai.com",
        
        # Email services
        "imap.gmail.com", 
        "smtp.gmail.com",
        "p154-caldav.icloud.com",
        "*.icloud.com",
        
        # Communication
        "api.telegram.org",
        
        # Search and web services
        "api.brave.com",
        
        # Development and package registries
        "*.github.com",
        "*.githubusercontent.com", 
        "registry.npmjs.org",
        "pypi.org",
        "files.pythonhosted.org",
    ])
    
    # Denylist - known problematic domains that should always be blocked
    default_denylist: List[str] = field(default_factory=lambda: [
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
    ])
    
    # Per-agent allowlist overrides
    agent_allowlists: Dict[str, List[str]] = field(default_factory=dict)
    
    # Global IP allowlist (CIDR notation supported)
    allowed_ips: List[str] = field(default_factory=list)
    
    # Allowed ports (empty list means all ports allowed)
    allowed_ports: List[int] = field(default_factory=lambda: [80, 443])
    
    # Whether to enable strict mode (denylist overrides allowlist)
    strict_mode: bool = True

    @classmethod
    def from_environment(cls) -> "EgressFilterConfig":
        """Create config from environment variables and AGENTSHROUD_MODE."""
        mode = "monitor"  # Default to monitor
        
        # Check AGENTSHROUD_MODE environment variable
        agentshroud_mode = os.getenv("AGENTSHROUD_MODE", "").lower()
        if agentshroud_mode == "enforce":
            mode = "enforce"
        
        # Allow override via specific egress mode env var
        egress_mode = os.getenv("AGENTSHROUD_EGRESS_MODE", "").lower()
        if egress_mode in ("enforce", "monitor"):
            mode = egress_mode
            
        return cls(mode=mode)

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
                domain for domain in allowlist 
                if not self._matches_any_pattern(domain, denylist)
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
                    prefix = domain[:-(len(base) + 1)]
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