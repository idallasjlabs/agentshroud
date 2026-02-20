"""Browser Security Module - Detects social engineering in web content.

Provides fake dialog/popup detection, URL reputation checking, credential
entry protection, and screenshot analysis hooks.

References:
    - Wu et al. 2026 (arXiv:2601.07263) - Browser-based attacks on AI agents
"""
import re
from dataclasses import dataclass, field
from enum import IntEnum
from typing import List, Callable, Optional
from urllib.parse import urlparse


class ThreatLevel(IntEnum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class SocialEngineeringDetected(Exception):
    pass

class PhishingURLDetected(Exception):
    pass

class CredentialEntryBlocked(Exception):
    pass


@dataclass
class ThreatAssessment:
    threat_level: ThreatLevel
    threats: List[str] = field(default_factory=list)


# Social engineering patterns
_SE_PATTERNS = [
    (re.compile(r'virus|infected|malware', re.I), ThreatLevel.HIGH, "malware scare"),
    (re.compile(r'call\s+\d[\d\-]{6,}|call\s+(now|immediately)', re.I), ThreatLevel.HIGH, "phone scam"),
    (re.compile(r'(windows\s+defender|microsoft\s+support)\s*(alert|error|warning)', re.I), ThreatLevel.HIGH, "tech support scam"),
    (re.compile(r'error\s*#[A-Z0-9]{4,}', re.I), ThreatLevel.HIGH, "fake error code"),
    (re.compile(r'(press\s+win|powershell\s+-e|cmd\.exe)', re.I), ThreatLevel.HIGH, "fake captcha/command execution"),
    (re.compile(r'account\s+(will\s+be\s+)?suspend', re.I), ThreatLevel.MEDIUM, "account suspension threat"),
    (re.compile(r'urgent|immediately|right\s+now', re.I), ThreatLevel.MEDIUM, "urgency manipulation"),
    (re.compile(r'verify\s+your\s+(identity|account)', re.I), ThreatLevel.MEDIUM, "identity verification scam"),
]

# URL phishing patterns
_PHISHING_BRANDS = ["paypal", "google", "apple", "microsoft", "amazon", "facebook", "netflix"]
_LOOKALIKE_PATTERNS = [
    re.compile(r'g0+gle', re.I),
    re.compile(r'payp@l', re.I),
    re.compile(r'amaz0n', re.I),
    re.compile(r'faceb0+k', re.I),
]


class BrowserSecurityGuard:
    def __init__(self):
        self._screenshot_hooks: List[Callable] = []

    def analyze_content(self, content: str) -> ThreatAssessment:
        threats = []
        max_level = ThreatLevel.NONE
        for pattern, level, desc in _SE_PATTERNS:
            if pattern.search(content):
                threats.append(desc)
                if level > max_level:
                    max_level = level
        return ThreatAssessment(threat_level=max_level, threats=threats)

    def check_url_reputation(self, url: str) -> ThreatLevel:
        # Data URIs
        if url.startswith("data:"):
            return ThreatLevel.HIGH

        parsed = urlparse(url)
        hostname = parsed.hostname or ""

        # Homograph detection (non-ASCII in hostname)
        try:
            hostname.encode('ascii')
        except UnicodeEncodeError:
            return ThreatLevel.HIGH

        # Brand impersonation in subdomain
        for brand in _PHISHING_BRANDS:
            if brand in hostname:
                # Check if it's the real domain
                parts = hostname.split(".")
                # e.g. login-paypal.security-verify.com — paypal not in TLD+1
                tld_plus_one = ".".join(parts[-2:]) if len(parts) >= 2 else hostname
                if brand not in tld_plus_one:
                    return ThreatLevel.HIGH

        # Lookalike patterns
        for pat in _LOOKALIKE_PATTERNS:
            if pat.search(hostname):
                return ThreatLevel.HIGH

        # IP address URL
        if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', hostname):
            return ThreatLevel.LOW

        # Excessive subdomains
        if hostname.count(".") >= 4:
            return ThreatLevel.LOW

        return ThreatLevel.NONE

    def can_enter_credentials(self, url: str) -> bool:
        parsed = urlparse(url)
        hostname = parsed.hostname or ""

        # Allow localhost
        if hostname in ("localhost", "127.0.0.1", "::1"):
            return True

        # Block HTTP for non-localhost
        if parsed.scheme != "https":
            raise CredentialEntryBlocked(f"Credential entry blocked on non-HTTPS: {url}")

        # Block IP addresses
        if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', hostname):
            raise CredentialEntryBlocked(f"Credential entry blocked on IP address: {url}")

        # Block lookalikes
        for pat in _LOOKALIKE_PATTERNS:
            if pat.search(hostname):
                raise CredentialEntryBlocked(f"Credential entry blocked on suspicious domain: {url}")

        # Check URL reputation
        if self.check_url_reputation(url) >= ThreatLevel.HIGH:
            raise CredentialEntryBlocked(f"Credential entry blocked - high threat URL: {url}")

        return True

    def register_screenshot_hook(self, hook: Callable):
        self._screenshot_hooks.append(hook)

    def analyze_screenshot(self, image_data: bytes) -> ThreatAssessment:
        if not self._screenshot_hooks:
            return ThreatAssessment(threat_level=ThreatLevel.NONE)
        # Run all hooks, return highest threat
        max_assessment = ThreatAssessment(threat_level=ThreatLevel.NONE)
        for hook in self._screenshot_hooks:
            result = hook(image_data)
            if result.threat_level > max_assessment.threat_level:
                max_assessment = result
        return max_assessment
