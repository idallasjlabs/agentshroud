---
type: community
cohesion: 0.05
members: 50
---

# test_scanner_integration.py

**Cohesion:** 0.05 - loosely connected
**Members:** 50 nodes

## Members
- [[.__init__()_123]] - code - gateway/security/tool_result_injection.py
- [[._detect_hidden_instructions()]] - code - gateway/security/context_guard.py
- [[._detect_instruction_injection()]] - code - gateway/security/context_guard.py
- [[._detect_rapid_context_growth()]] - code - gateway/security/context_guard.py
- [[._detect_repetition_attacks()]] - code - gateway/security/context_guard.py
- [[.analyze_message()]] - code - gateway/security/context_guard.py
- [[.guard()]] - code - gateway/tests/test_context_guard.py
- [[.scan_tool_result()_3]] - code - gateway/security/tool_result_injection.py
- [[.should_block_message()]] - code - gateway/security/context_guard.py
- [[.test_empty_provenance_for_unknown_session()]] - code - gateway/tests/test_context_guard.py
- [[.test_few_repetitions_allowed()]] - code - gateway/tests/test_context_guard.py
- [[.test_normal_message_allowed()]] - code - gateway/tests/test_context_guard.py
- [[.test_normal_sized_message_allowed()]] - code - gateway/tests/test_context_guard.py
- [[.test_oversized_message_blocked()]] - code - gateway/tests/test_context_guard.py
- [[.test_repeated_pattern_flagged()]] - code - gateway/tests/test_context_guard.py
- [[.test_segment_hash_integrity()]] - code - gateway/tests/test_context_guard.py
- [[.test_segment_provenance_ordering()]] - code - gateway/tests/test_context_guard.py
- [[.test_segment_tagging_basic()]] - code - gateway/tests/test_context_guard.py
- [[.test_separate_sessions_isolated()]] - code - gateway/tests/test_context_guard.py
- [[.test_short_repetitions_allowed()]] - code - gateway/tests/test_context_guard.py
- [[Analyze a message for context poisoning attempts.          Args             ses]] - rationale - gateway/security/context_guard.py
- [[CVE-2026-22708 — AI Agent Container Escape via Prompt Injection]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-30741 — RCE via Request-Side Prompt Injection]] - rationale - docs/security/cve-mitigation-matrix.md
- [[Check if message should be allowed, with detailed findings.      Args         t]] - rationale - gateway/security/context_guard.py
- [[Context tracking for a session.]] - rationale - gateway/security/context_guard.py
- [[ContextAttack]] - code - gateway/security/context_guard.py
- [[Detect hidden instructions buried in large text blocks.]] - rationale - gateway/security/context_guard.py
- [[Detect instruction injection attempts.]] - rationale - gateway/security/context_guard.py
- [[Detect rapid context window filling.]] - rationale - gateway/security/context_guard.py
- [[Detect repetition-based context stuffing attacks.]] - rationale - gateway/security/context_guard.py
- [[Detected context window attack attempt.]] - rationale - gateway/security/context_guard.py
- [[Determine if a message should be blocked.          Returns             Tuple of]] - rationale - gateway/security/context_guard.py
- [[Get the global context guard instance.]] - rationale - gateway/security/context_guard.py
- [[Initialize the scanner with optional custom rules.          Args             cu]] - rationale - gateway/security/tool_result_injection.py
- [[InjectionResult]] - code - gateway/security/tool_result_injection.py
- [[InjectionRule]] - code - gateway/security/tool_result_injection.py
- [[Result from tool result injection scan.]] - rationale - gateway/security/tool_result_injection.py
- [[Rule for detecting injection patterns in tool results.]] - rationale - gateway/security/tool_result_injection.py
- [[Scan tool result content for injection attempts.          Args             tool]] - rationale - gateway/security/tool_result_injection.py
- [[SessionContext]] - code - gateway/security/context_guard.py
- [[Strip potentially malicious markdown from tool results.      Removes     - Mark]] - rationale - gateway/security/input_normalizer.py
- [[TestCheckMessage]] - code - gateway/tests/test_context_guard.py
- [[TestSourceTagging]] - code - gateway/tests/test_context_guard.py
- [[check_message()]] - code - gateway/security/context_guard.py
- [[context_guard.py]] - code - gateway/security/context_guard.py
- [[get_context_guard()]] - code - gateway/security/context_guard.py
- [[input_normalizer.py]] - code - gateway/security/input_normalizer.py
- [[strip_markdown_exfil()]] - code - gateway/security/input_normalizer.py
- [[test_context_guard.py]] - code - gateway/tests/test_context_guard.py
- [[tool_result_injection.py]] - code - gateway/security/tool_result_injection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_scanner_integrationpy
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_TrustManager]]
- 5 edges to [[_COMMUNITY_ServiceManager]]
- 5 edges to [[_COMMUNITY_FileSandbox]]
- 4 edges to [[_COMMUNITY_MCPPermissionManager]]
- 2 edges to [[_COMMUNITY_TestPathIsolationManager]]
- 2 edges to [[_COMMUNITY_URLAnalyzer]]
- 1 edge to [[_COMMUNITY_EncryptedStore]]
- 1 edge to [[_COMMUNITY_StdioConnection]]
- 1 edge to [[_COMMUNITY_TeamsConfig]]
- 1 edge to [[_COMMUNITY_background.js]]
- 1 edge to [[_COMMUNITY_chatbotmain.py]]
- 1 edge to [[_COMMUNITY_DockerEngine]]
- 1 edge to [[_COMMUNITY_test_jira_weekly_review.py]]

## Top bridge nodes
- [[tool_result_injection.py]] - degree 12, connects to 6 communities
- [[.analyze_message()]] - degree 12, connects to 3 communities
- [[context_guard.py]] - degree 9, connects to 3 communities
- [[.scan_tool_result()_3]] - degree 7, connects to 3 communities
- [[input_normalizer.py]] - degree 4, connects to 3 communities