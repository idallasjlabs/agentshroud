---
type: community
cohesion: 0.29
members: 7
---

# Tool Result Injection (security)

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[.scan_tool_result()_3]] - code - gateway/security/tool_result_injection.py
- [[InjectionResult]] - code - gateway/security/tool_result_injection.py
- [[Result from tool result injection scan.]] - rationale - gateway/security/tool_result_injection.py
- [[Scan tool result content for injection attempts.          Args             tool]] - rationale - gateway/security/tool_result_injection.py
- [[Strip potentially malicious markdown from tool results.      Removes     - Mark]] - rationale - gateway/security/input_normalizer.py
- [[input_normalizer.py]] - code - gateway/security/input_normalizer.py
- [[strip_markdown_exfil()]] - code - gateway/security/input_normalizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Tool_Result_Injection_security
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Telegram Proxy Core]]
- 4 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 1 edge to [[_COMMUNITY_Group Config & Collaborator Responses]]
- 1 edge to [[_COMMUNITY_Agentshroud.yaml (03 - Configuration)]]
- 1 edge to [[_COMMUNITY_Prompt Guard (security)]]
- 1 edge to [[_COMMUNITY_RBAC & Ingest Middleware]]

## Top bridge nodes
- [[strip_markdown_exfil()]] - degree 7, connects to 3 communities
- [[.scan_tool_result()_3]] - degree 7, connects to 3 communities
- [[input_normalizer.py]] - degree 4, connects to 3 communities
- [[InjectionResult]] - degree 3, connects to 1 community