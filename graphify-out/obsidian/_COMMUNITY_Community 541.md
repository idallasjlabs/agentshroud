---
type: community
cohesion: 0.18
members: 17
---

# Community 541

**Cohesion:** 0.18 - loosely connected
**Members:** 17 nodes

## Members
- [[.test_api_key_patterns()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_clean_text_no_patterns()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_credit_card_pattern()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_email_pattern()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_exfil_base64()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_exfil_hex()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_exfil_webhook()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_injection_role()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_injection_system_prompt()]] - code - gateway/tests/test_subagent_governance.py
- [[.test_ssn_pattern()]] - code - gateway/tests/test_subagent_governance.py
- [[Check text for PII patterns. Returns list of pattern names found.]] - rationale - gateway/security/subagent_governance.py
- [[Check text for data exfiltration patterns.]] - rationale - gateway/security/subagent_governance.py
- [[Check text for prompt injection patterns.]] - rationale - gateway/security/subagent_governance.py
- [[TestPatternDetection]] - code - gateway/tests/test_subagent_governance.py
- [[_check_exfil_patterns()]] - code - gateway/security/subagent_governance.py
- [[_check_injection_patterns()]] - code - gateway/security/subagent_governance.py
- [[_check_pii_patterns()]] - code - gateway/security/subagent_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_541
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Community 507]]
- 4 edges to [[_COMMUNITY_Community 982]]
- 4 edges to [[_COMMUNITY_Community 483]]
- 2 edges to [[_COMMUNITY_Community 639]]
- 1 edge to [[_COMMUNITY_Community 912]]

## Top bridge nodes
- [[TestPatternDetection]] - degree 18, connects to 5 communities
- [[_check_pii_patterns()]] - degree 9, connects to 3 communities
- [[_check_exfil_patterns()]] - degree 8, connects to 3 communities
- [[_check_injection_patterns()]] - degree 7, connects to 3 communities