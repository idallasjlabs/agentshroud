---
type: community
members: 67
---

# Community 115

**Members:** 67 nodes

## Members
- [[._add_disclosure_event()]] - code - gateway/security/multi_turn_tracker.py
- [[._analyze_agent_response()]] - code - gateway/security/multi_turn_tracker.py
- [[._analyze_user_message()]] - code - gateway/security/multi_turn_tracker.py
- [[._check_thresholds()]] - code - gateway/security/multi_turn_tracker.py
- [[._cleanup_old_sessions()]] - code - gateway/security/multi_turn_tracker.py
- [[._detect_hidden_instructions()]] - code - gateway/security/context_guard.py
- [[._detect_instruction_injection()]] - code - gateway/security/context_guard.py
- [[._detect_rapid_context_growth()]] - code - gateway/security/context_guard.py
- [[._detect_repetition_attacks()]] - code - gateway/security/context_guard.py
- [[._normalize_query()]] - code - gateway/security/multi_turn_tracker.py
- [[._score_message_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[._score_response_patterns()]] - code - gateway/security/multi_turn_tracker.py
- [[._trigger_alert()]] - code - gateway/security/multi_turn_tracker.py
- [[.analyze_message()]] - code - gateway/security/context_guard.py
- [[.guard()]] - code - gateway/tests/test_context_guard.py
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
- [[.track_message()]] - code - gateway/security/multi_turn_tracker.py
- [[A single disclosure event in a session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Add a disclosure event to the session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Analyze a message for context poisoning attempts.          Args             ses]] - rationale - gateway/security/context_guard.py
- [[Analyze agent response for potential information leaks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Analyze user message for disclosure patterns.]] - rationale - gateway/security/multi_turn_tracker.py
- [[CVE-2026-22172 — WebSocket Scope Self-Declaration]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-22708 — AI Agent Container Escape via Prompt Injection]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-30741 — RCE via Request-Side Prompt Injection]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-32922 — Token Scope Expansion via device.token.rotate]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-34425 — Preflight Validation Bypass (Shell-Bleed)]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-3690 — Canvas Authentication Bypass]] - rationale - docs/security/cve-mitigation-matrix.md
- [[Check if message should be allowed, with detailed findings.      Args         t]] - rationale - gateway/security/context_guard.py
- [[Check session score against thresholds and take action.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Context tracking for a session.]] - rationale - gateway/security/context_guard.py
- [[Context tracking for a single session.]] - rationale - gateway/security/multi_turn_tracker.py
- [[ContextAttack]] - code - gateway/security/context_guard.py
- [[Detect hidden instructions buried in large text blocks.]] - rationale - gateway/security/context_guard.py
- [[Detect instruction injection attempts.]] - rationale - gateway/security/context_guard.py
- [[Detect rapid context window filling.]] - rationale - gateway/security/context_guard.py
- [[Detect repetition-based context stuffing attacks.]] - rationale - gateway/security/context_guard.py
- [[Detected context window attack attempt.]] - rationale - gateway/security/context_guard.py
- [[Determine if a message should be blocked.          Returns             Tuple of]] - rationale - gateway/security/context_guard.py
- [[DisclosureEvent]] - code - gateway/security/multi_turn_tracker.py
- [[Get the global context guard instance.]] - rationale - gateway/security/context_guard.py
- [[Normalize query for repeated query detection.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Remove old sessions to prevent memory bloat.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Score agent response for potential leaks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[Score message based on disclosure patterns.]] - rationale - gateway/security/multi_turn_tracker.py
- [[SessionContext]] - code - gateway/security/context_guard.py
- [[SessionContext_1]] - code - gateway/security/multi_turn_tracker.py
- [[TestCheckMessage]] - code - gateway/tests/test_context_guard.py
- [[TestSourceTagging]] - code - gateway/tests/test_context_guard.py
- [[Track a message and response pair for disclosure analysis.          Args]] - rationale - gateway/security/multi_turn_tracker.py
- [[Trigger alert callbacks.]] - rationale - gateway/security/multi_turn_tracker.py
- [[check_message()]] - code - gateway/security/context_guard.py
- [[context_guard.py]] - code - gateway/security/context_guard.py
- [[cve-mitigation-matrix]] - document - docs/security/cve-mitigation-matrix.md
- [[get_context_guard()]] - code - gateway/security/context_guard.py
- [[test_context_guard.py]] - code - gateway/tests/test_context_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_115
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_Community 0]]
- 12 edges to [[_COMMUNITY_Community 72]]
- 4 edges to [[_COMMUNITY_Community 22]]
- 4 edges to [[_COMMUNITY_Community 8]]
- 3 edges to [[_COMMUNITY_Community 6]]
- 2 edges to [[_COMMUNITY_Community 14]]
- 2 edges to [[_COMMUNITY_Community 154]]
- 1 edge to [[_COMMUNITY_Community 9]]
- 1 edge to [[_COMMUNITY_Community 17]]
- 1 edge to [[_COMMUNITY_Community 141]]
- 1 edge to [[_COMMUNITY_Community 91]]
- 1 edge to [[_COMMUNITY_Community 118]]
- 1 edge to [[_COMMUNITY_Community 215]]

## Top bridge nodes
- [[cve-mitigation-matrix]] - degree 13, connects to 6 communities
- [[.analyze_message()]] - degree 12, connects to 3 communities
- [[context_guard.py]] - degree 9, connects to 3 communities
- [[TestCheckMessage]] - degree 9, connects to 2 communities
- [[TestSourceTagging]] - degree 9, connects to 2 communities