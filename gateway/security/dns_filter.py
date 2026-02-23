# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
DNS Exfiltration Prevention — monitor and optionally block DNS tunneling.

Default mode: monitor (log everything, block nothing).
Enforce mode: block tunneling patterns and enforce allowlist.
"""
from __future__ import annotations


import logging
import math
import re
import time
from collections import defaultdict
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger(__name__)


class EntropyCalculator:
    @staticmethod
    def shannon_entropy(s: str) -> float:
        if not s:
            return 0.0
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        length = len(s)
        return -sum(
            (count / length) * math.log2(count / length) for count in freq.values()
        )


@dataclass
class DNSFilterConfig:
    mode: str = "monitor"  # "monitor" or "enforce"
    allowed_domains: Optional[list[str]] = None  # None = allow all
    max_subdomain_length: int = 80
    max_label_length: int = 50
    entropy_threshold: float = 4.0
    max_queries_per_minute: int = 120
    hex_pattern_min_length: int = 24
    base64_pattern_min_length: int = 20


@dataclass
class DNSQuery:
    timestamp: float
    agent_id: str
    domain: str
    allowed: bool
    flagged: bool
    reason: str = ""


@dataclass
class DNSVerdict:
    allowed: bool
    flagged: bool
    reason: str = ""


@dataclass
class TunnelingPattern:
    pattern_type: str
    label: str
    score: float


class DNSFilter:
    MAX_AUDIT_ENTRIES = 50000  # Prevent unbounded growth

    def __init__(self, config: DNSFilterConfig):
        self.config = config
        self._audit: list[DNSQuery] = []
        self._query_times: dict[str, list[float]] = defaultdict(list)
        self._hex_re = re.compile(
            r"^[0-9a-f]{%d,}$" % config.hex_pattern_min_length, re.I
        )
        self._b64_re = re.compile(
            r"^[A-Za-z0-9+/]{%d,}={0,2}$" % config.base64_pattern_min_length
        )

    def check(self, domain: str, agent_id: str) -> DNSVerdict:
        now = time.time()
        flags: list[str] = []

        # Check allowlist
        allowlist_blocked = False
        if self.config.allowed_domains is not None:
            if not self._domain_in_allowlist(domain):
                allowlist_blocked = True
                flags.append("domain not in allowlist")

        # Check tunneling patterns
        patterns = self._detect_tunneling(domain)
        if patterns:
            flags.append("; ".join(p.pattern_type for p in patterns))

        # Check rate limiting
        self._query_times[agent_id].append(now)
        self._cleanup_rate_window(agent_id, now)
        if len(self._query_times[agent_id]) > self.config.max_queries_per_minute:
            flags.append("rate limit exceeded")

        flagged = len(flags) > 0
        reason = "; ".join(flags) if flags else ""

        if self.config.mode == "enforce":
            allowed = not (allowlist_blocked or bool(patterns))
        else:
            allowed = True  # monitor mode never blocks

        query = DNSQuery(
            timestamp=now,
            agent_id=agent_id,
            domain=domain,
            allowed=allowed,
            flagged=flagged,
            reason=reason,
        )
        # Evict oldest entries if at capacity
        if len(self._audit) >= self.MAX_AUDIT_ENTRIES:
            self._audit = self._audit[-(self.MAX_AUDIT_ENTRIES // 2) :]
        self._audit.append(query)

        if flagged:
            logger.warning(
                "DNS query flagged: %s from %s — %s", domain, agent_id, reason
            )

        return DNSVerdict(allowed=allowed, flagged=flagged, reason=reason)

    def _domain_in_allowlist(self, domain: str) -> bool:
        domain = domain.lower().rstrip(".")
        for allowed in self.config.allowed_domains:
            allowed = allowed.lower().rstrip(".")
            if domain == allowed or domain.endswith("." + allowed):
                return True
        return False

    def _detect_tunneling(self, domain: str) -> list[TunnelingPattern]:
        patterns = []
        parts = domain.lower().rstrip(".").split(".")
        # Skip TLD and registered domain (last 2 parts)
        labels = parts[:-2] if len(parts) > 2 else []

        for label in labels:
            if len(label) > self.config.max_label_length:
                patterns.append(TunnelingPattern("long_label", label, 1.0))

            if self._hex_re.match(label):
                patterns.append(TunnelingPattern("hex_encoding", label, 0.8))

            if (
                self._b64_re.match(label)
                and len(label) >= self.config.base64_pattern_min_length
            ):
                patterns.append(TunnelingPattern("base64_encoding", label, 0.9))

            entropy = EntropyCalculator.shannon_entropy(label)
            if len(label) >= 12 and entropy >= self.config.entropy_threshold:
                patterns.append(TunnelingPattern("high_entropy", label, entropy))

        # Check total subdomain length
        subdomain = ".".join(labels)
        if len(subdomain) > self.config.max_subdomain_length:
            patterns.append(TunnelingPattern("long_subdomain", subdomain[:30], 1.0))

        return patterns

    def _cleanup_rate_window(self, agent_id: str, now: float):
        cutoff = now - 60
        self._query_times[agent_id] = [
            t for t in self._query_times[agent_id] if t > cutoff
        ]

    def get_audit_log(self, agent_id: Optional[str] = None) -> list[DNSQuery]:
        if agent_id:
            return [q for q in self._audit if q.agent_id == agent_id]
        return list(self._audit)

    def get_flagged_queries(self, agent_id: Optional[str] = None) -> list[DNSQuery]:
        logs = self.get_audit_log(agent_id)
        return [q for q in logs if q.flagged]
