---
type: community
cohesion: 0.07
members: 42
---

# Intel Report (security)

**Cohesion:** 0.07 - loosely connected
**Members:** 42 nodes

## Members
- [[.__init__()_61]] - code - gateway/security/citation_verifier.py
- [[.__init__()_87]] - code - gateway/security/intel_report.py
- [[._compute_content_hash()]] - code - gateway/security/intel_report.py
- [[._load_latest_file()]] - code - gateway/security/intel_report.py
- [[._verify_url()]] - code - gateway/security/citation_verifier.py
- [[.load_all()_1]] - code - gateway/security/intel_report.py
- [[.load_latest()]] - code - gateway/security/intel_report.py
- [[.matches_allowlist()]] - code - gateway/security/egress_config.py
- [[.report_id_not_empty()]] - code - gateway/security/intel_report.py
- [[.save()_1]] - code - gateway/security/intel_report.py
- [[.source_not_empty()]] - code - gateway/security/intel_report.py
- [[.verify_chain()_2]] - code - gateway/security/intel_report.py
- [[.verify_entry()]] - code - gateway/security/citation_verifier.py
- [[.verify_integrity()]] - code - gateway/security/intel_report.py
- [[.verify_report()]] - code - gateway/security/citation_verifier.py
- [[A verified source backing a competitor claim.      A Citation is only created by]] - rationale - gateway/security/intel_report.py
- [[Citation]] - code - gateway/security/citation_verifier.py
- [[Citation_1]] - code - gateway/security/intel_report.py
- [[CitationVerifier.verify_report()]] - code - gateway/security/citation_verifier.py
- [[CompetitiveIntelReport]] - code - gateway/security/citation_verifier.py
- [[CompetitiveIntelReport_1]] - code - gateway/security/intel_report.py
- [[CompetitorEntry]] - code - gateway/security/citation_verifier.py
- [[Compute SHA-256 over the canonical content fields of a report.      Fields inclu]] - rationale - gateway/security/intel_report.py
- [[Derive content_hash from the canonical content fields.          Only computed wh]] - rationale - gateway/security/intel_report.py
- [[Fetcher]] - code - gateway/security/citation_verifier.py
- [[Load all reports in chronological order (oldest first).]] - rationale - gateway/security/intel_report.py
- [[Load the most recently saved report.          Args             verify If True,]] - rationale - gateway/security/intel_report.py
- [[Path_14]] - code - gateway/security/intel_report.py
- [[Persist report to the store, linking it to the previous report.          Sets]] - rationale - gateway/security/intel_report.py
- [[Public does domain match any pattern in the effective default allowlist]] - rationale - gateway/security/egress_config.py
- [[Re-fetch url and return a Citation iff it is allowlisted + live.          SSRF]] - rationale - gateway/security/citation_verifier.py
- [[Return True if domain matches any pattern (exact or ``.`` wildcard).      Sin]] - rationale - gateway/security/egress_config.py
- [[Return True iff the stored content_hash matches recomputation.]] - rationale - gateway/security/intel_report.py
- [[Return a CompetitorEntry with only its valid citations, or None.          None m]] - rationale - gateway/security/citation_verifier.py
- [[Return the most recent JSON file in the store, or None.]] - rationale - gateway/security/intel_report.py
- [[Schema for a Hermes-generated competitive intelligence report.      The ``conten]] - rationale - gateway/security/intel_report.py
- [[Verify every draft claim; return a report of only verified claims.          Clai]] - rationale - gateway/security/citation_verifier.py
- [[Walk the entire report chain and verify hash linkage.          Returns]] - rationale - gateway/security/intel_report.py
- [[_compute_hash()]] - code - gateway/security/intel_report.py
- [[citation_verifier.py]] - code - gateway/security/citation_verifier.py
- [[domain_matches()]] - code - gateway/security/egress_config.py
- [[intel_report.py]] - code - gateway/security/intel_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Intel_Report_security
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_Citation Verifier]]
- 15 edges to [[_COMMUNITY_Intel Pipeline]]
- 8 edges to [[_COMMUNITY_Api (web)]]
- 7 edges to [[_COMMUNITY_Intel Endpoint]]
- 4 edges to [[_COMMUNITY_Egress Filter]]
- 2 edges to [[_COMMUNITY_Router (soc)]]

## Top bridge nodes
- [[CompetitiveIntelReport_1]] - degree 36, connects to 5 communities
- [[citation_verifier.py]] - degree 10, connects to 4 communities
- [[Citation_1]] - degree 11, connects to 3 communities
- [[intel_report.py]] - degree 7, connects to 2 communities
- [[.load_latest()]] - degree 6, connects to 2 communities