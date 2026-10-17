---
type: community
members: 19
---

# TestPatternDetection

**Members:** 19 nodes

## Members
- [[dot-score_output()]] - code - gateway/security/subagent_governance.py
- [[dot-test_api_key_patterns()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_clean_text_no_patterns()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_credit_card_pattern()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_email_pattern()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_exfil_base64()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_exfil_hex()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_exfil_webhook()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_injection_role()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_injection_system_prompt()]] - code - gateway/tests/test_subagent_governance.py
- [[dot-test_ssn_pattern()]] - code - gateway/tests/test_subagent_governance.py
- [[Check text for PII patterns. Returns list of pattern names found.]] - rationale - gateway/security/subagent_governance.py
- [[Check text for data exfiltration patterns.]] - rationale - gateway/security/subagent_governance.py
- [[Check text for prompt injection patterns.]] - rationale - gateway/security/subagent_governance.py
- [[Score a subagent's output for safety and quality.          In a full deployment,]] - rationale - gateway/security/subagent_governance.py
- [[TestPatternDetection]] - code - gateway/tests/test_subagent_governance.py
- [[_check_exfil_patterns()]] - code - gateway/security/subagent_governance.py
- [[_check_injection_patterns()]] - code - gateway/security/subagent_governance.py
- [[_check_pii_patterns()]] - code - gateway/security/subagent_governance.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestPatternDetection
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_SubagentGovernance]]
- 4 edges to [[_COMMUNITY_GovernanceAction (2)]]
- 3 edges to [[_COMMUNITY_GovernanceAction]]

## Top bridge nodes
- [[dot-score_output()]] - degree 7, connects to 3 communities
- [[TestPatternDetection]] - degree 16, connects to 2 communities
- [[_check_pii_patterns()]] - degree 9, connects to 2 communities
- [[_check_exfil_patterns()]] - degree 8, connects to 2 communities
- [[_check_injection_patterns()]] - degree 7, connects to 2 communities
