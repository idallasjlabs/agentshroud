# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
URL Analyzer — detect SSRF, data exfiltration, and suspicious URL patterns.

Hard blocks: SSRF (private IPs) only.
Flags: PII in URLs, base64 payloads, suspiciously long query strings.
"""

import base64
import ipaddress
import logging
import re
import socket
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from urllib.parse import parse_qs, urlparse, unquote

logger = logging.getLogger("agentshroud.proxy.url_analyzer")


class URLVerdict(str, Enum):
    ALLOW = "allow"
    FLAG = "flag"  # Suspicious but let through
    BLOCK = "block"  # Hard block (SSRF only)


@dataclass
class URLFinding:
    """A single finding from URL analysis."""

    category: str  # ssrf, pii, exfiltration, suspicious
    severity: str  # critical, high, medium, low
    description: str
    detail: str = ""


@dataclass
class URLAnalysisResult:
    """Result of analyzing a URL."""

    url: str
    verdict: URLVerdict = URLVerdict.ALLOW
    findings: list[URLFinding] = field(default_factory=list)
    resolved_ip: Optional[str] = None
    domain: str = ""
    is_ssrf: bool = False

    @property
    def flagged(self) -> bool:
        return len(self.findings) > 0


# --- PII patterns for URL detection ---
_PII_PATTERNS = [
    ("email", re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")),
    ("ssn", re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),
    ("phone", re.compile(r"\b(?:\+?1[-.]?)?\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}\b")),
    (
        "credit_card",
        re.compile(
            r"\b(?:4\d{3}|5[1-5]\d{2}|3[47]\d{2}|6(?:011|5\d{2}))[- ]?\d{4}[- ]?\d{4}[- ]?\d{3,4}\b"
        ),
    ),
]

# Known private/reserved networks
_PRIVATE_NETWORKS = [
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
    ipaddress.ip_network("127.0.0.0/8"),
    ipaddress.ip_network("169.254.0.0/16"),
    ipaddress.ip_network("0.0.0.0/8"),
    ipaddress.ip_network("::1/128"),
    ipaddress.ip_network("fc00::/7"),  # IPv6 ULA
    ipaddress.ip_network("fe80::/10"),  # IPv6 link-local
]

# Localhost hostname variants
_LOCALHOST_NAMES = frozenset(
    {
        "localhost",
        "ip6-localhost",
        "ip6-loopback",
        "localhost.localdomain",
        "0.0.0.0",
        "127.0.0.1",
        "[::1]",
    }
)


class URLAnalyzer:
    """Analyze URLs for SSRF, data exfiltration, and suspicious patterns."""

    def __init__(self, resolve_dns: bool = False):
        """
        Args:
            resolve_dns: If True, resolve hostnames to IPs and check those too.
                        Disabled by default to avoid latency.
        """
        self.resolve_dns = resolve_dns

    def analyze(self, url: str) -> URLAnalysisResult:
        """Analyze a URL for security issues.

        Returns URLAnalysisResult with verdict and findings.
        Only SSRF gets a BLOCK verdict; everything else is FLAG.
        """
        result = URLAnalysisResult(url=url)

        try:
            parsed = urlparse(url)
        except Exception:
            result.findings.append(
                URLFinding(
                    category="malformed",
                    severity="medium",
                    description="Malformed URL",
                    detail=url[:200],
                )
            )
            result.verdict = URLVerdict.FLAG
            return result

        hostname = parsed.hostname or ""
        result.domain = hostname.lower().rstrip(".")

        # --- SSRF checks (hard block) ---
        if self._is_ssrf(hostname):
            result.is_ssrf = True
            result.verdict = URLVerdict.BLOCK
            result.findings.append(
                URLFinding(
                    category="ssrf",
                    severity="critical",
                    description="SSRF: private/reserved IP or localhost",
                    detail=f"host={hostname}",
                )
            )
            return result

        # DNS resolution check
        if self.resolve_dns and hostname:
            resolved = self._resolve_host(hostname)
            if resolved:
                result.resolved_ip = resolved
                if self._is_private_ip(resolved):
                    result.is_ssrf = True
                    result.verdict = URLVerdict.BLOCK
                    result.findings.append(
                        URLFinding(
                            category="ssrf",
                            severity="critical",
                            description="SSRF: hostname resolves to private IP",
                            detail=f"host={hostname} -> {resolved}",
                        )
                    )
                    return result

        # --- Data exfiltration checks (flag only) ---
        full_url = unquote(url)

        # Check for PII in URL
        for pii_type, pattern in _PII_PATTERNS:
            if pattern.search(full_url):
                result.findings.append(
                    URLFinding(
                        category="pii",
                        severity="high",
                        description=f"Possible {pii_type} in URL",
                        detail=f"pattern={pii_type}",
                    )
                )

        # Check for base64 in path or query
        self._check_base64(parsed, result)

        # Check for suspiciously long query strings
        query = parsed.query or ""
        if len(query) > 2000:
            result.findings.append(
                URLFinding(
                    category="exfiltration",
                    severity="medium",
                    description="Unusually long query string",
                    detail=f"length={len(query)}",
                )
            )

        # Check for many query parameters (potential data dump)
        if query:
            params = parse_qs(query)
            if len(params) > 30:
                result.findings.append(
                    URLFinding(
                        category="exfiltration",
                        severity="medium",
                        description="Large number of query parameters",
                        detail=f"count={len(params)}",
                    )
                )

        # Set verdict
        if result.findings:
            result.verdict = URLVerdict.FLAG

        return result

    def _is_ssrf(self, hostname: str) -> bool:
        """Check if hostname is a private/reserved address (SSRF attempt)."""
        if not hostname:
            return False

        normalized = hostname.lower().rstrip(".")

        # Strip brackets from IPv6
        if normalized.startswith("[") and normalized.endswith("]"):
            normalized = normalized[1:-1]

        # Check localhost names
        if normalized in _LOCALHOST_NAMES:
            return True

        # Check for decimal IP encoding (e.g., 2130706433 = 127.0.0.1)
        if normalized.isdigit():
            try:
                num = int(normalized)
                if 0 <= num <= 0xFFFFFFFF:
                    ip_str = str(ipaddress.ip_address(num))
                    return self._is_private_ip(ip_str)
            except (ValueError, OverflowError):
                pass

        # Check for octal/hex IP encodings (e.g., 0x7f000001, 0177.0.0.1)
        if re.match(r"^0[xX][0-9a-fA-F]+$", normalized):
            try:
                num = int(normalized, 16)
                if 0 <= num <= 0xFFFFFFFF:
                    ip_str = str(ipaddress.ip_address(num))
                    return self._is_private_ip(ip_str)
            except (ValueError, OverflowError):
                pass

        # Direct IP check
        if self._is_private_ip(normalized):
            return True

        return False

    @staticmethod
    def _is_private_ip(ip_str: str) -> bool:
        """Check if an IP address is private/reserved/loopback."""
        try:
            addr = ipaddress.ip_address(ip_str)
        except ValueError:
            return False

        # Handle IPv4-mapped IPv6 (e.g., ::ffff:127.0.0.1)
        if isinstance(addr, ipaddress.IPv6Address) and addr.ipv4_mapped:
            addr = addr.ipv4_mapped

        for network in _PRIVATE_NETWORKS:
            if isinstance(addr, type(network.network_address)) and addr in network:
                return True

        return (
            addr.is_private
            or addr.is_loopback
            or addr.is_link_local
            or addr.is_reserved
        )

    @staticmethod
    def _resolve_host(hostname: str) -> Optional[str]:
        """Resolve hostname to IP. Returns None on failure.

        NOTE: DNS rebinding attacks can change resolution between this check
        and the actual request. For full protection, the HTTP client should
        connect through this proxy and pin the resolved IP for the request.
        """
        try:
            result = socket.getaddrinfo(
                hostname, None, socket.AF_UNSPEC, socket.SOCK_STREAM
            )
            if result:
                return result[0][4][0]
        except (socket.gaierror, OSError):
            pass
        return None

    @staticmethod
    def _check_base64(parsed, result: URLAnalysisResult) -> None:
        """Check for base64-encoded data in URL path and query values."""
        # Check path segments
        path_segments = (parsed.path or "").split("/")
        for seg in path_segments:
            if len(seg) > 50 and _looks_like_base64(seg):
                result.findings.append(
                    URLFinding(
                        category="exfiltration",
                        severity="medium",
                        description="Possible base64-encoded data in URL path",
                        detail=f"segment_length={len(seg)}",
                    )
                )
                break

        # Check query values
        if parsed.query:
            params = parse_qs(parsed.query)
            for key, values in params.items():
                for val in values:
                    if len(val) > 50 and _looks_like_base64(val):
                        result.findings.append(
                            URLFinding(
                                category="exfiltration",
                                severity="medium",
                                description="Possible base64-encoded data in query parameter",
                                detail=f"param={key}, length={len(val)}",
                            )
                        )
                        return  # One finding is enough

    def analyze_and_pin(self, url: str) -> URLAnalysisResult:
        """Analyze URL and pin resolved IP to mitigate DNS rebinding TOCTOU.

        When resolve_dns=True, this method resolves the hostname ONCE and
        returns the resolved IP in the result. Callers MUST use resolved_ip
        for the actual HTTP connection instead of re-resolving the hostname.

        This prevents attackers from changing DNS records between our security
        check and the actual request.
        """
        result = self.analyze(url)
        if not result.is_ssrf and self.resolve_dns and result.domain:
            resolved = self._resolve_host(result.domain)
            if resolved:
                result.resolved_ip = resolved
                # Double-check the resolved IP isn't private
                if self._is_private_ip(resolved):
                    result.is_ssrf = True
                    result.verdict = URLVerdict.BLOCK
                    result.findings.append(
                        URLFinding(
                            category="ssrf",
                            severity="critical",
                            description="SSRF: hostname resolves to private IP (pinned)",
                            detail=f"host={result.domain} -> {resolved}",
                        )
                    )
        return result


def _looks_like_base64(s: str) -> bool:
    """Heuristic: does this string look like base64-encoded data?"""
    if len(s) < 20:
        return False
    # Base64 charset: A-Za-z0-9+/= (or URL-safe: A-Za-z0-9-_=)
    if not re.match(r"^[A-Za-z0-9+/=_-]+$", s):
        return False
    # Must have mix of upper, lower, digits
    has_upper = any(c.isupper() for c in s)
    has_lower = any(c.islower() for c in s)
    has_digit = any(c.isdigit() for c in s)
    if not (has_upper and has_lower and has_digit):
        return False
    # Try to actually decode
    try:
        decoded = base64.b64decode(s + "==", validate=False)
        # If it decodes to mostly printable text, suspicious
        if len(decoded) > 10:
            return True
    except Exception:
        pass
    return False
