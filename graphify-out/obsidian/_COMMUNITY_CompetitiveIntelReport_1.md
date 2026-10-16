---
type: community
cohesion: 0.07
members: 38
---

# CompetitiveIntelReport

**Cohesion:** 0.07 - loosely connected
**Members:** 38 nodes

## Members
- [[dot-__init__()_67]] - code - gateway/security/citation_verifier.py
- [[dot-__init__()_68]] - code - gateway/security/intel_report.py
- [[dot-_compute_content_hash()]] - code - gateway/security/intel_report.py
- [[dot-_load_latest_file()]] - code - gateway/security/intel_report.py
- [[dot-_verify_url()]] - code - gateway/security/citation_verifier.py
- [[dot-load_all()]] - code - gateway/security/intel_report.py
- [[dot-load_latest()]] - code - gateway/security/intel_report.py
- [[dot-report_id_not_empty()]] - code - gateway/security/intel_report.py
- [[dot-save()]] - code - gateway/security/intel_report.py
- [[dot-source_not_empty()]] - code - gateway/security/intel_report.py
- [[dot-verify_chain()]] - code - gateway/security/intel_report.py
- [[dot-verify_entry()]] - code - gateway/security/citation_verifier.py
- [[dot-verify_integrity()]] - code - gateway/security/intel_report.py
- [[dot-verify_report()]] - code - gateway/security/citation_verifier.py
- [[A verified source backing a competitor claim.      A Citation is only created by]] - rationale - gateway/security/intel_report.py
- [[Citation]] - code - gateway/security/citation_verifier.py
- [[Citation_1]] - code - gateway/security/intel_report.py
- [[CitationVerifier.verify_report()]] - code - gateway/security/citation_verifier.py
- [[CompetitiveIntelReport_1]] - code - gateway/security/citation_verifier.py
- [[CompetitiveIntelReport_2]] - code - gateway/security/intel_report.py
- [[CompetitorEntry_1]] - code - gateway/security/citation_verifier.py
- [[Compute SHA-256 over the canonical content fields of a report.      Fields inclu]] - rationale - gateway/security/intel_report.py
- [[Derive content_hash from the canonical content fields.          Only computed wh]] - rationale - gateway/security/intel_report.py
- [[Fetcher]] - code - gateway/security/citation_verifier.py
- [[Load all reports in chronological order (oldest first).]] - rationale - gateway/security/intel_report.py
- [[Load the most recently saved report.          Args             verify If True,]] - rationale - gateway/security/intel_report.py
- [[Path_18]] - code - gateway/security/intel_report.py
- [[Persist report to the store, linking it to the previous report.          Sets]] - rationale - gateway/security/intel_report.py
- [[Re-fetch url and return a Citation iff it is allowlisted + live.          SSRF]] - rationale - gateway/security/citation_verifier.py
- [[Return True iff the stored content_hash matches recomputation.]] - rationale - gateway/security/intel_report.py
- [[Return a CompetitorEntry with only its valid citations, or None.          None m]] - rationale - gateway/security/citation_verifier.py
- [[Return the most recent JSON file in the store, or None.]] - rationale - gateway/security/intel_report.py
- [[Schema for a Hermes-generated competitive intelligence report.      The ``conten]] - rationale - gateway/security/intel_report.py
- [[Verify every draft claim; return a report of only verified claims.          Clai]] - rationale - gateway/security/citation_verifier.py
- [[Walk the entire report chain and verify hash linkage.          Returns]] - rationale - gateway/security/intel_report.py
- [[_compute_hash()]] - code - gateway/security/intel_report.py
- [[citation_verifier.py]] - code - gateway/security/citation_verifier.py
- [[intel_report.py]] - code - gateway/security/intel_report.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/CompetitiveIntelReport
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_api.py_1]]
- 15 edges to [[_COMMUNITY_CompetitiveIntelReport]]
- 8 edges to [[_COMMUNITY_api.py]]
- 4 edges to [[_COMMUNITY_FetchOutcome]]
- 3 edges to [[_COMMUNITY_EgressFilterConfig]]
- 3 edges to [[_COMMUNITY_FetchOutcome_1]]
- 2 edges to [[_COMMUNITY_socrouter.py]]

## Top bridge nodes
- [[CompetitiveIntelReport_2]] - degree 36, connects to 6 communities
- [[citation_verifier.py]] - degree 10, connects to 5 communities
- [[Citation_1]] - degree 11, connects to 3 communities
- [[intel_report.py]] - degree 7, connects to 2 communities
- [[dot-load_latest()]] - degree 6, connects to 2 communities
