# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Citation verifier for competitive-intelligence reports (SCRUM-75).

IEC 62443 FR3 (System Integrity) / FR6 (Audit): a competitive claim must not
reach a published report on the strength of an LLM's self-asserted "[verified]"
tag.  This module ENFORCES that every claim is backed by a real source —
independently, at verify time — rather than trusting the generator.

Enforcement (anti-security-theater)
-----------------------------------
For each draft claim the verifier re-fetches every candidate source URL through
the gateway's allowlisted web proxy (the injected ``fetcher``).  A citation is
valid only if:
  * its host matches the egress allowlist (reuses ``egress_config.domain_matches``
    against ``PERMANENT_EGRESS_DOMAINS`` — the SAME approved competitor/research
    domains egress enforcement uses; no duplicate domain list); AND
  * the re-fetch returned a 2xx status with non-empty content (a SHA-256 is
    recorded as evidence).

A claim with zero valid citations is DROPPED — this is the enforced removal of
``[unverified]`` claims, counted in ``CompetitiveIntelReport.dropped_unverified``.

The verifier never performs network I/O itself: the ``fetcher`` is injected, so
production wires it to the real gateway web-proxy fetch path while tests inject
a deterministic fake (no real network, per the repo test rules).
"""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from typing import Callable, Iterable, Optional
from urllib.parse import urlparse

from .egress_config import PERMANENT_EGRESS_DOMAINS, domain_matches
from .intel_report import Citation, CompetitiveIntelReport, CompetitorEntry

logger = logging.getLogger("agentshroud.security.citation_verifier")


@dataclass(frozen=True)
class FetchOutcome:
    """Result of re-fetching a candidate citation URL through the web proxy."""

    url: str
    status: int
    content_sha256: Optional[str]
    fetched_at: float

    @property
    def ok(self) -> bool:
        """A source counts as proven only on a 2xx with non-empty content."""
        return 200 <= self.status < 300 and bool(self.content_sha256)


# A fetcher re-fetches a URL and returns proof of what came back.  Injected so
# production uses the gateway web proxy and tests use a deterministic fake.
Fetcher = Callable[[str], FetchOutcome]


@dataclass
class DraftEntry:
    """An unverified competitor claim submitted for citation checking."""

    name: str
    security_score: int
    module_count: int
    notes: str = ""
    candidate_urls: list[str] = field(default_factory=list)


class CitationVerifier:
    """Verifies competitor claims against re-fetched, allowlisted sources."""

    def __init__(
        self,
        fetcher: Fetcher,
        allowed_domains: Optional[Iterable[str]] = None,
    ) -> None:
        self._fetch = fetcher
        # Reuse the canonical egress allowlist (approved competitor + research
        # domains) rather than maintaining a second list.
        self._allowlist: list[str] = list(
            allowed_domains if allowed_domains is not None else PERMANENT_EGRESS_DOMAINS
        )

    # ------------------------------------------------------------------
    # Per-URL / per-claim verification
    # ------------------------------------------------------------------

    def _verify_url(self, url: str) -> Optional[Citation]:
        """Re-fetch *url* and return a Citation iff it is allowlisted + live.

        SSRF hardening: the allowlist decision uses ``urlparse().hostname``, but
        WHATWG-compliant HTTP clients disagree with ``urlparse`` on authorities
        containing ``\\`` or userinfo (``https://evil.com\\@lakera.ai`` parses to
        host ``lakera.ai`` but a browser/curl connects to ``evil.com``).  To make
        the check and the fetch agree regardless of which client PR2 injects, we
        reject any URL that is not a clean ``http(s)`` URL with no userinfo and no
        backslash BEFORE the allowlist gate — so the fetched string can never
        resolve to a different host than the one we validated.
        """
        parsed = urlparse(url)
        host = parsed.hostname
        if not host:
            logger.debug("citation rejected — unparseable host: %r", url)
            return None
        if parsed.scheme not in ("http", "https"):
            logger.info("citation rejected — non-http(s) scheme: %s", parsed.scheme)
            return None
        if parsed.username or parsed.password or "\\" in url:
            logger.info("citation rejected — embedded credentials / backslash authority")
            return None
        if not domain_matches(host, self._allowlist):
            logger.info("citation rejected — host not allowlisted: %s", host)
            return None
        outcome = self._fetch(url)
        sha = outcome.content_sha256
        # Proven live only on a 2xx with non-empty content.  Single reachable
        # gate (no assert — must hold under `python -O`); `sha` narrows to str.
        if not (sha and 200 <= outcome.status < 300):
            logger.info(
                "citation rejected — re-fetch not proven (status=%s): %s",
                outcome.status,
                url,
            )
            return None
        return Citation(
            url=url,
            domain=host.lower(),
            status=outcome.status,
            content_sha256=sha,
            fetched_at=outcome.fetched_at,
        )

    def verify_entry(self, draft: DraftEntry) -> Optional[CompetitorEntry]:
        """Return a CompetitorEntry with only its valid citations, or None.

        None means the claim had no allowlisted, re-fetch-proven source and must
        be dropped from the report.
        """
        citations: list[Citation] = []
        for url in draft.candidate_urls:
            citation = self._verify_url(url)
            if citation is not None:
                citations.append(citation)
        if not citations:
            return None
        return CompetitorEntry(
            name=draft.name,
            security_score=draft.security_score,
            module_count=draft.module_count,
            notes=draft.notes,
            sources=citations,
        )

    # ------------------------------------------------------------------
    # Report-level verification
    # ------------------------------------------------------------------

    def verify_report(
        self,
        *,
        report_id: str,
        source: str,
        draft_entries: Iterable[DraftEntry],
        summary: str = "",
        agentshroud_score: Optional[int] = None,
        lead_delta: Optional[int] = None,
        generated_at: Optional[float] = None,
    ) -> CompetitiveIntelReport:
        """Verify every draft claim; return a report of only verified claims.

        Claims lacking a proven citation are excluded and counted in
        ``dropped_unverified`` — the enforced, auditable removal of unverified
        competitive intelligence.
        """
        verified: list[CompetitorEntry] = []
        dropped = 0
        for draft in draft_entries:
            entry = self.verify_entry(draft)
            if entry is None:
                dropped += 1
                logger.info("claim dropped (unverified): %s", draft.name)
            else:
                verified.append(entry)
        return CompetitiveIntelReport(
            report_id=report_id,
            generated_at=generated_at if generated_at is not None else time.time(),
            source=source,
            summary=summary,
            competitors=verified,
            agentshroud_score=agentshroud_score,
            lead_delta=lead_delta,
            dropped_unverified=dropped,
        )
