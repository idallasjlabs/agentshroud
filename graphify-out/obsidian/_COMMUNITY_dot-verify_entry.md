---
type: community
members: 7
---

# .verify_entry

**Members:** 7 nodes

## Members
- [[dot-_verify_url()]] - code - gateway/security/citation_verifier.py
- [[dot-verify_entry()]] - code - gateway/security/citation_verifier.py
- [[dot-verify_report()]] - code - gateway/security/citation_verifier.py
- [[Re-fetch url and return a Citation iff it is allowlisted + live. SSRF…]] - rationale - gateway/security/citation_verifier.py
- [[Return a CompetitorEntry with only its valid citations, or None. None means the…]] - rationale - gateway/security/citation_verifier.py
- [[Verify every draft claim; return a report of only verified claims. Claims…]] - rationale - gateway/security/citation_verifier.py
- [[_fetch()]] - code - gateway/security/citation_verifier.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/verify_entry
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_DraftEntry]]
- 3 edges to [[_COMMUNITY_CompetitiveIntelReport]]
- 1 edge to [[_COMMUNITY_test_intel_endpoint.py]]
- 1 edge to [[_COMMUNITY_EgressFilter]]
- 1 edge to [[_COMMUNITY_make_httpx_fetcher]]

## Top bridge nodes
- [[dot-_verify_url()]] - degree 6, connects to 3 communities
- [[dot-verify_entry()]] - degree 6, connects to 2 communities
- [[dot-verify_report()]] - degree 5, connects to 2 communities
- [[_fetch()]] - degree 3, connects to 2 communities
