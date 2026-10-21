---
type: community
members: 21
---

# ApprovalQueueConfig (4)

**Members:** 21 nodes

## Members
- [[dot-_blocking_prompt_guard()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-_check_encoded_content()]] - code - gateway/security/prompt_guard.py
- [[dot-_check_unicode_tricks()]] - code - gateway/security/prompt_guard.py
- [[dot-_passthrough_pii()_1]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-scan()_4]] - code - gateway/security/prompt_guard.py
- [[dot-scan_tool_result()_2]] - code - gateway/security/prompt_guard.py
- [[dot-test_full_trust_tool_result_injection_audited_not_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_standard_trust_tool_result_injection_is_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[dot-test_untrusted_tool_result_injection_is_blocked()]] - code - gateway/tests/test_pipeline_unit.py
- [[Check for suspicious base64 content that decodes to injection attempts.]] - rationale - gateway/security/prompt_guard.py
- [[Detect potential base64-encoded payloads in text.     Returns list of decoded st]] - rationale - gateway/security/input_normalizer.py
- [[Detect unicode obfuscation tricks.]] - rationale - gateway/security/prompt_guard.py
- [[FULL-trust owner response scan runs, detection audited, delivery NOT blocked.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[STANDARD-trust source also blocked — only FULL bypasses the block.]] - rationale - gateway/tests/test_pipeline_unit.py
- [[Scan input text for prompt injection patterns.          Args             text]] - rationale - gateway/security/prompt_guard.py
- [[Scan tool result content for indirect prompt injection.          Tool results (w]] - rationale - gateway/security/prompt_guard.py
- [[ScanResult_4]] - code - gateway/security/prompt_guard.py
- [[Step 1.76 PromptGuard tool-result scan must respect user_trust_level.      CVE-2]] - rationale - gateway/tests/test_pipeline_unit.py
- [[TestPromptGuardToolResultTrustGate]] - code - gateway/tests/test_pipeline_unit.py
- [[UNTRUSTED source tool-result injection scan blocks as before (CVE-2026-31045).]] - rationale - gateway/tests/test_pipeline_unit.py
- [[detect_base64_payloads()]] - code - gateway/security/input_normalizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ApprovalQueueConfig_4
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_ApprovalQueueConfig]]
- 7 edges to [[_COMMUNITY_ApprovalQueueConfig (2)_1]]
- 6 edges to [[_COMMUNITY_ApprovalQueueConfig (3)_1]]
- 5 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 2 edges to [[_COMMUNITY_socrouter.py]]
- 2 edges to [[_COMMUNITY_DelegationManager]]
- 1 edge to [[_COMMUNITY_api.py (2)]]
- 1 edge to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_FetchOutcome]]
- 1 edge to [[_COMMUNITY_TestCheckCommandExecution]]
- 1 edge to [[_COMMUNITY_A2AGovernanceProxy]]

## Top bridge nodes
- [[TestPromptGuardToolResultTrustGate]] - degree 22, connects to 7 communities
- [[ScanResult_4]] - degree 17, connects to 4 communities
- [[dot-scan()_4]] - degree 8, connects to 2 communities
- [[dot-_passthrough_pii()_1]] - degree 7, connects to 2 communities
- [[detect_base64_payloads()]] - degree 5, connects to 2 communities
