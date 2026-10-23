---
type: community
cohesion: 0.05
members: 62
---

# EgressFilterConfig

**Cohesion:** 0.05 - loosely connected
**Members:** 62 nodes

## Members
- [[dot-__init__()_204]] - code - gateway/security/collaborator_tracker.py
- [[dot-_append_contributor_log()]] - code - gateway/security/collaborator_tracker.py
- [[dot-_coerce_timestamp()]] - code - gateway/security/collaborator_tracker.py
- [[dot-_make_proxy()_5]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-_normalize_preview()]] - code - gateway/security/collaborator_tracker.py
- [[dot-_normalize_username()]] - code - gateway/security/collaborator_tracker.py
- [[dot-get_activity()]] - code - gateway/security/collaborator_tracker.py
- [[dot-get_activity_summary()]] - code - gateway/security/collaborator_tracker.py
- [[dot-get_health()_1]] - code - gateway/security/collaborator_tracker.py
- [[dot-record_activity()]] - code - gateway/security/collaborator_tracker.py
- [[dot-test_400_retry_no_loop()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_400_retry_succeeds_when_text_strippable()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_failed_write_makes_unhealthy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_initial_state_healthy()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_accepts_hyphen_delimiter()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_accepts_underscore_delimiter()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_handles_non_string_input()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_matches_cannot_to_access_variant()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_matches_healthcheck_skill_sandbox_error()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_matches_http_status_without_body()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_matches_memory_embedding_provider_error()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_matches_no_response_generated_phrase()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_requires_skill_marker_for_healthcheck_branch()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_rewrite_known_runtime_errors_returns_none_for_unrelated_text()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Append one activity entry for any tracked collaborator or the owner.          Ar]] - rationale - gateway/security/collaborator_tracker.py
- [[B1 one-shot 400-retry for unbalanced HTML parse errors.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Best-effort float timestamp coercion for resilient log reads.]] - rationale - gateway/security/collaborator_tracker.py
- [[CollaboratorActivityTracker]] - code - gateway/tests/test_lifespan_prune.py
- [[CollaboratorActivityTracker_1]] - code - gateway/security/collaborator_tracker.py
- [[CollaboratorActivityTracker.get_health() must return accurate counters.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Create a fake contributor markdown file for the given uid.]] - rationale - gateway/tests/test_lifespan_prune.py
- [[First sendMessage returns 400 'can't parse entities'; retry with plain text succ]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Mirror activity into workspace contributor logs used by daily digests.]] - rationale - gateway/security/collaborator_tracker.py
- [[Normalize previews to single-line safe text for JSONL + markdown mirrors.]] - rationale - gateway/security/collaborator_tracker.py
- [[Normalize username for safe contributor-log tokenization.]] - rationale - gateway/security/collaborator_tracker.py
- [[Path_67]] - code - gateway/security/collaborator_tracker.py
- [[Path_68]] - code - gateway/tests/test_lifespan_prune.py
- [[Persistent 400 returns the error after exactly one retry (no infinite loop).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Real-UID markdown files must never be deleted by the prune pass.]] - rationale - gateway/tests/test_lifespan_prune.py
- [[Return True when uid looks like a test fixture that should be silently dropped.]] - rationale - gateway/security/collaborator_tracker.py
- [[Return a health snapshot suitable for statusdetail.]] - rationale - gateway/security/collaborator_tracker.py
- [[Return activity entries sorted newest-first.          Args             since U]] - rationale - gateway/security/collaborator_tracker.py
- [[Return aggregated statistics over all recorded activity.          Returns]] - rationale - gateway/security/collaborator_tracker.py
- [[Run the same markdown-prune logic as lifespan.py and return pruned count.]] - rationale - gateway/tests/test_lifespan_prune.py
- [[Startup prune must remove fixture markdown files from every contributor dir.]] - rationale - gateway/tests/test_lifespan_prune.py
- [[TestRuntimeRewriteHelpers]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestTelegram400Retry]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestTrackerGetHealth]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Tracks collaborator messages at the gateway level.      Records every inbound me]] - rationale - gateway/security/collaborator_tracker.py
- [[Unit tests for deterministic runtime error rewrite helper behavior.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_is_fixture_uid()]] - code - gateway/security/collaborator_tracker.py
- [[_make_md()]] - code - gateway/tests/test_lifespan_prune.py
- [[_prune_fixture_markdown()]] - code - gateway/tests/test_lifespan_prune.py
- [[collaborator_tracker.py]] - code - gateway/security/collaborator_tracker.py
- [[test_is_fixture_uid_blocks_short_numeric()]] - code - gateway/tests/test_lifespan_prune.py
- [[test_is_fixture_uid_blocks_test_user_prefix()]] - code - gateway/tests/test_lifespan_prune.py
- [[test_is_fixture_uid_passes_real_uids()]] - code - gateway/tests/test_lifespan_prune.py
- [[test_lifespan_prune.py]] - code - gateway/tests/test_lifespan_prune.py
- [[test_prune_keeps_real_uid_markdown()]] - code - gateway/tests/test_lifespan_prune.py
- [[test_prune_walks_all_contributor_dirs()]] - code - gateway/tests/test_lifespan_prune.py
- [[test_unknown_user_recorded_when_dynamic_tracking_enabled()]] - code - gateway/tests/test_collaborator_tracker.py
- [[tracker()]] - code - gateway/tests/test_collaborator_tracker.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EgressFilterConfig
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_test_telegram_proxy_outbound.py]]
- 7 edges to [[_COMMUNITY_DELIVERABLE 1 — Domain-by-Domain Assessment]]
- 5 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 3 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 3 edges to [[_COMMUNITY_openclawskillsi-crSKILL]]
- 3 edges to [[_COMMUNITY_MCPPermissionManager]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_hermesskillsi-bsREADME.md (5)]]
- 1 edge to [[_COMMUNITY_Blue Team Security Assessment — AgentShroud v0.8.0 Round 2]]
- 1 edge to [[_COMMUNITY_ESP32-S3-BOX-3 Voice Terminal for Hermes (behind AgentShroud)]]
- 1 edge to [[_COMMUNITY_TestLooksLikeSafeCollaboratorInfoQuery]]
- 1 edge to [[_COMMUNITY_Phase 3A3B Implementation Verification Results]]
- 1 edge to [[_COMMUNITY_TestDomainValidationHelper]]
- 1 edge to [[_COMMUNITY_TestOutboundScanUnification]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig (4)]]
- 1 edge to [[_COMMUNITY__fw_client]]
- 1 edge to [[_COMMUNITY_All Dependencies.md (2)]]
- 1 edge to [[_COMMUNITY_WebhookReceiver]]

## Top bridge nodes
- [[CollaboratorActivityTracker_1]] - degree 50, connects to 14 communities
- [[TestRuntimeRewriteHelpers]] - degree 16, connects to 4 communities
- [[TestTelegram400Retry]] - degree 9, connects to 4 communities
- [[TestTrackerGetHealth]] - degree 8, connects to 4 communities
- [[test_lifespan_prune.py]] - degree 10, connects to 1 community
