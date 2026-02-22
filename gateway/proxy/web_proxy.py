"""
Web Traffic Proxy — intercept, inspect, and audit all outbound HTTP from OpenClaw.

Design principles:
- Default-allow: all URLs pass unless denied domain or SSRF
- SSRF is the only hard block
- Prompt injection / PII / suspicious patterns are flagged, not blocked
- Every request is audited in the hash chain
- Passthrough mode for debugging
- Async content scanning to minimize latency
"""

import logging
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Optional

from .url_analyzer import URLAnalyzer
from .web_config import WebProxyConfig
from .web_content_scanner import WebContentScanner

logger = logging.getLogger("agentshroud.proxy.web_proxy")


class ProxyAction(str, Enum):
    ALLOW = "allow"  # Passed through cleanly
    FLAG = "flag"  # Passed through but flagged with findings
    BLOCK = "block"  # Hard blocked (SSRF or denied domain)


@dataclass
class WebProxyResult:
    """Result of proxying a web request."""

    url: str
    action: ProxyAction = ProxyAction.ALLOW
    blocked: bool = False
    block_reason: str = ""

    # URL analysis
    url_findings: list[dict[str, str]] = field(default_factory=list)
    is_ssrf: bool = False

    # Content scan (populated after response received)
    content_findings: list[dict[str, str]] = field(default_factory=list)
    prompt_injection_score: float = 0.0
    has_prompt_injection: bool = False

    # Rate limiting
    rate_limited: bool = False

    # Audit
    audit_entry_id: str = ""
    audit_hash: str = ""

    # Timing
    processing_time_ms: float = 0.0

    # Metadata headers to add to the response
    security_headers: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "url": self.url,
            "action": self.action.value,
            "blocked": self.blocked,
            "block_reason": self.block_reason,
            "url_findings": self.url_findings,
            "is_ssrf": self.is_ssrf,
            "content_findings": self.content_findings,
            "prompt_injection_score": self.prompt_injection_score,
            "has_prompt_injection": self.has_prompt_injection,
            "rate_limited": self.rate_limited,
            "processing_time_ms": self.processing_time_ms,
        }

    @property
    def flagged(self) -> bool:
        return bool(self.url_findings or self.content_findings)


class RateLimiter:
    """Simple in-memory per-domain rate limiter using sliding window."""

    MAX_TRACKED_DOMAINS = 10000  # Prevent unbounded growth

    def __init__(self):
        self._windows: dict[str, list[float]] = {}

    def check(self, domain: str, rpm_limit: int) -> bool:
        """Check if request is within rate limit. Returns True if allowed."""
        now = time.time()
        window_start = now - 60.0

        if domain not in self._windows:
            # Evict stale domains if at capacity
            if len(self._windows) >= self.MAX_TRACKED_DOMAINS:
                now_t = time.time()
                stale = [
                    d
                    for d, ts in self._windows.items()
                    if not ts or ts[-1] < now_t - 120
                ]
                for d in stale:
                    del self._windows[d]
                # If still over, drop oldest
                if len(self._windows) >= self.MAX_TRACKED_DOMAINS:
                    oldest_d = min(
                        self._windows,
                        key=lambda d: self._windows[d][-1] if self._windows[d] else 0,
                    )
                    del self._windows[oldest_d]
            self._windows[domain] = []

        # Clean old entries
        self._windows[domain] = [t for t in self._windows[domain] if t > window_start]

        if len(self._windows[domain]) >= rpm_limit:
            return False

        self._windows[domain].append(now)
        return True

    def reset(self, domain: Optional[str] = None) -> None:
        if domain:
            self._windows.pop(domain, None)
        else:
            self._windows.clear()


class WebProxy:
    """HTTP web traffic proxy for OpenClaw.

    Intercepts all outbound web requests, runs security checks,
    and audits everything through the hash chain.

    Usage:
        proxy = WebProxy()
        result = proxy.check_request("https://example.com/page")
        if not result.blocked:
            # proceed with request
            response_body = fetch(url)
            content_result = proxy.scan_response(url, response_body, "text/html")
    """

    def __init__(
        self,
        config: Optional[WebProxyConfig] = None,
        audit_chain=None,
        url_analyzer: Optional[URLAnalyzer] = None,
        content_scanner: Optional[WebContentScanner] = None,
    ):
        self.config = config or WebProxyConfig()
        self.audit_chain = audit_chain
        self.url_analyzer = url_analyzer or URLAnalyzer()
        self.content_scanner = content_scanner or WebContentScanner()
        self.rate_limiter = RateLimiter()
        self._stats = {
            "total_requests": 0,
            "allowed": 0,
            "flagged": 0,
            "blocked": 0,
            "blocked_ssrf": 0,
            "blocked_domain": 0,
            "blocked_rate_limit": 0,
            "content_scans": 0,
            "prompt_injections_detected": 0,
            "pii_in_urls": 0,
            "pii_in_responses": 0,
        }

    def check_request(
        self, url: str, method: str = "GET", headers: Optional[dict] = None
    ) -> WebProxyResult:
        """Check an outbound HTTP request before it's sent.

        This is the pre-flight check. Only SSRF and denied domains are blocked.
        Everything else passes through.

        Args:
            url: The URL being requested.
            method: HTTP method.
            headers: Request headers (for logging).

        Returns:
            WebProxyResult — check .blocked to see if request should proceed.
        """
        start = time.time()
        self._stats["total_requests"] += 1
        result = WebProxyResult(url=url)

        # --- Passthrough mode ---
        if self.config.passthrough_mode:
            result.action = ProxyAction.ALLOW
            result.security_headers["X-AgentShroud-Mode"] = "passthrough"
            self._audit("web_request_passthrough", url, {"method": method})
            result.processing_time_ms = (time.time() - start) * 1000
            self._stats["allowed"] += 1
            return result

        # --- URL analysis ---
        url_result = self.url_analyzer.analyze(url)

        # Hard block: SSRF
        if url_result.is_ssrf:
            result.action = ProxyAction.BLOCK
            result.blocked = True
            result.is_ssrf = True
            result.block_reason = f"SSRF blocked: {url_result.domain or url}"
            self._stats["blocked"] += 1
            self._stats["blocked_ssrf"] += 1
            self._audit(
                "web_request_blocked_ssrf",
                url,
                {
                    "method": method,
                    "findings": [f.description for f in url_result.findings],
                },
            )
            result.processing_time_ms = (time.time() - start) * 1000
            return result

        # Hard block: domain policy check
        domain = url_result.domain
        if self.config.mode == "allowlist":
            # Default-deny: block unless explicitly listed
            if not domain or not self.config.is_domain_allowed(domain):
                result.action = ProxyAction.BLOCK
                result.blocked = True
                result.block_reason = f"Domain not in allowlist: {domain or url}"
                self._stats["blocked"] += 1
                self._stats["blocked_domain"] += 1
                self._audit(
                    "web_request_blocked_allowlist",
                    url,
                    {"method": method, "domain": domain or ""},
                )
                result.processing_time_ms = (time.time() - start) * 1000
                return result
        elif domain and self.config.is_domain_denied(domain):
            # Default-allow: block only explicitly denied domains
            result.action = ProxyAction.BLOCK
            result.blocked = True
            result.block_reason = f"Domain denied: {domain}"
            self._stats["blocked"] += 1
            self._stats["blocked_domain"] += 1
            self._audit(
                "web_request_blocked_domain",
                url,
                {
                    "method": method,
                    "domain": domain,
                },
            )
            result.processing_time_ms = (time.time() - start) * 1000
            return result

        # Rate limit check (soft — blocks request but not a security issue)
        if domain:
            settings = self.config.get_domain_settings(domain)
            if not self.rate_limiter.check(domain, settings.rate_limit_rpm):
                result.action = ProxyAction.BLOCK
                result.blocked = True
                result.rate_limited = True
                result.block_reason = (
                    f"Rate limited: {domain} ({settings.rate_limit_rpm} rpm)"
                )
                self._stats["blocked"] += 1
                self._stats["blocked_rate_limit"] += 1
                self._audit(
                    "web_request_rate_limited",
                    url,
                    {
                        "method": method,
                        "domain": domain,
                        "limit": settings.rate_limit_rpm,
                    },
                )
                result.processing_time_ms = (time.time() - start) * 1000
                return result

        # URL findings (flag, don't block)
        if url_result.flagged:
            result.url_findings = [
                {
                    "category": f.category,
                    "severity": f.severity,
                    "description": f.description,
                    "detail": f.detail,
                }
                for f in url_result.findings
            ]
            result.action = ProxyAction.FLAG
            result.security_headers["X-AgentShroud-URL-Flags"] = str(
                len(url_result.findings)
            )
            if any(f.category == "pii" for f in url_result.findings):
                self._stats["pii_in_urls"] += 1

        # Audit the request
        if result.action == ProxyAction.FLAG:
            self._stats["flagged"] += 1
            self._audit(
                "web_request_flagged",
                url,
                {
                    "method": method,
                    "findings": result.url_findings,
                },
            )
        else:
            self._stats["allowed"] += 1
            self._audit("web_request", url, {"method": method})

        result.security_headers["X-AgentShroud-Proxy"] = "active"
        result.processing_time_ms = (time.time() - start) * 1000
        return result

    def scan_response(
        self,
        url: str,
        body: str,
        content_type: str = "text/html",
        status_code: int = 200,
        response_size: int = 0,
    ) -> WebProxyResult:
        """Scan a response body for prompt injection, PII, and hidden content.

        This is called AFTER the response is received. Content always passes
        through; findings are returned as metadata.

        Args:
            url: The URL that was fetched.
            body: Response body text.
            content_type: Response content type.
            status_code: HTTP status code.
            response_size: Response size in bytes (if known).

        Returns:
            WebProxyResult with content findings.
        """
        start = time.time()
        result = WebProxyResult(url=url)
        self._stats["content_scans"] += 1

        if self.config.passthrough_mode:
            result.action = ProxyAction.ALLOW
            result.processing_time_ms = (time.time() - start) * 1000
            return result

        # Content type check (flag suspicious types)
        if content_type and any(
            ct in content_type.lower() for ct in self.config.suspicious_content_types
        ):
            result.content_findings.append(
                {
                    "category": "content_type",
                    "severity": "medium",
                    "description": f"Suspicious content type: {content_type}",
                }
            )

        # Response size check (flag but don't block)
        domain = ""
        try:
            from urllib.parse import urlparse

            domain = (urlparse(url).hostname or "").lower()
        except Exception:
            pass

        if domain:
            settings = self.config.get_domain_settings(domain)
            effective_size = response_size or len(
                body.encode("utf-8", errors="replace")
            )
            if effective_size > settings.max_response_bytes:
                result.content_findings.append(
                    {
                        "category": "size",
                        "severity": "low",
                        "description": f"Response exceeds size limit ({effective_size} > {settings.max_response_bytes})",
                    }
                )

        # Content scanning
        if self.config.scan_responses and body:
            scan = self.content_scanner.scan(body, content_type)

            if scan.flagged:
                for finding in scan.findings:
                    result.content_findings.append(
                        {
                            "category": finding.category,
                            "severity": finding.severity.value,
                            "description": finding.description,
                            "evidence": finding.evidence[:200],
                        }
                    )

            result.prompt_injection_score = scan.prompt_injection_score
            result.has_prompt_injection = scan.has_prompt_injection

            if scan.has_prompt_injection:
                self._stats["prompt_injections_detected"] += 1
                result.security_headers["X-AgentShroud-Injection-Score"] = (
                    f"{scan.prompt_injection_score:.2f}"
                )
                result.security_headers["X-AgentShroud-Injection-Warning"] = "true"

            if scan.has_pii:
                self._stats["pii_in_responses"] += 1

        # Set action based on findings
        if result.content_findings:
            result.action = ProxyAction.FLAG
            self._audit(
                "web_response_flagged",
                url,
                {
                    "content_type": content_type,
                    "status_code": status_code,
                    "findings": result.content_findings,
                    "injection_score": result.prompt_injection_score,
                },
            )
        else:
            result.action = ProxyAction.ALLOW
            self._audit(
                "web_response",
                url,
                {
                    "content_type": content_type,
                    "status_code": status_code,
                },
            )

        result.processing_time_ms = (time.time() - start) * 1000
        return result

    def _audit(
        self, event_type: str, url: str, metadata: dict[str, Any]
    ) -> Optional[str]:
        """Record an audit entry in the hash chain."""
        if self.audit_chain is None:
            return None
        try:
            entry = self.audit_chain.append(
                content=f"{event_type}:{url}",
                direction="web",
                metadata={"event": event_type, "url": url, **metadata},
            )
            return entry.id
        except Exception as e:
            logger.error(f"Audit chain error: {e}")
            return None

    def get_stats(self) -> dict[str, Any]:
        """Get proxy statistics."""
        return dict(self._stats)
