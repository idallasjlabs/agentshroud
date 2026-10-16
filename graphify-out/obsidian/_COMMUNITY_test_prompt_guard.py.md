---
type: community
cohesion: 0.04
members: 60
---

# test_prompt_guard.py

**Cohesion:** 0.04 - loosely connected
**Members:** 60 nodes

## Members
- [[--- new instructions patterns should be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[dot-_get_hmac_key()]] - code - gateway/security/prompt_guard.py
- [[dot-get_document_tag()]] - code - gateway/security/metadata_guard.py
- [[dot-guard()_4]] - code - gateway/tests/test_metadata_guard.py
- [[dot-guard()_5]] - code - gateway/tests/test_prompt_guard.py
- [[dot-guard()_6]] - code - gateway/tests/test_prompt_guard.py
- [[dot-pg()_1]] - code - gateway/tests/test_prompt_guard.py
- [[dot-register_system_prompt()]] - code - gateway/security/prompt_guard.py
- [[dot-tag_document()]] - code - gateway/security/metadata_guard.py
- [[dot-test_benign_tool_result_passes()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_direct_injection_in_tool_result_blocked()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_document_tag_creation()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_document_tag_lookup_by_hash()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_document_tag_untrusted_source()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_empty_prompt()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_empty_tool_result_passes()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_explicit_key_used()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_get_document_tag_unknown_hash_returns_none()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_lower_threshold_than_direct_scan()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_preserves_legitimate_markdown()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_register_and_verify()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_role_override_in_tool_result_blocked()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_strips_fake_system_tags()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_strips_separator_overrides()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-test_tag_document_different_content_different_hash()]] - code - gateway/tests/test_metadata_guard.py
- [[dot-test_tamper_detected()]] - code - gateway/tests/test_prompt_guard.py
- [[dot-verify_system_prompt()]] - code - gateway/security/prompt_guard.py
- [[system style fake tags should be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[CVE-2026-31045 — indirect prompt injection via tool results]] - concept - gateway/tests/test_prompt_guard.py
- [[Compute and return an HMAC-SHA256 fingerprint for the system prompt.]] - rationale - gateway/security/prompt_guard.py
- [[Create a PromptGuard instance for testing]] - rationale - gateway/tests/test_prompt_guard.py
- [[Create and store a provenance tag for a document.]] - rationale - gateway/security/metadata_guard.py
- [[DocumentTag]] - code - gateway/security/metadata_guard.py
- [[Empty prompt should still register and verify cleanly.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Explicit ignore-instructions payload embedded in a tool result.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Explicit key parameter should override session key.]] - rationale - gateway/tests/test_prompt_guard.py
- [[HMAC-SHA256 fingerprint for a registered system prompt.]] - rationale - gateway/security/prompt_guard.py
- [[Look up a document tag by its SHA-256 content hash.]] - rationale - gateway/security/metadata_guard.py
- [[Normal markdown headers ( Title) should not be stripped.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Numbered security control catalog (C8, C9, C18, C47, ...)]] - concept - gateway/tests/test_prompt_guard.py
- [[Provenance record for a document ingested into the agent context.]] - rationale - gateway/security/metadata_guard.py
- [[Return HMAC key env var preferred, session-scoped random fallback.]] - rationale - gateway/security/prompt_guard.py
- [[Return True if prompt_text matches the stored HMAC fingerprint.]] - rationale - gateway/security/prompt_guard.py
- [[SystemPromptFingerprint]] - code - gateway/security/prompt_guard.py
- [[Test PromptGuard initialization]] - rationale - gateway/tests/test_prompt_guard.py
- [[Test that normal messages pass through]] - rationale - gateway/tests/test_prompt_guard.py
- [[TestDocumentTagging]] - code - gateway/tests/test_metadata_guard.py
- [[TestReanchorDelimiters]] - code - gateway/tests/test_prompt_guard.py
- [[TestSystemPromptHMAC]] - code - gateway/tests/test_prompt_guard.py
- [[TestToolResultScan]] - code - gateway/tests/test_prompt_guard.py
- [[Tests for indirect prompt injection detection in tool results.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Tool result scan blocks at score ≥ 0.6 vs direct scan threshold of 0.8.]] - rationale - gateway/tests/test_prompt_guard.py
- [[Verifying a tampered prompt should return False.]] - rationale - gateway/tests/test_prompt_guard.py
- [[metadata_guard.py]] - code - gateway/security/metadata_guard.py
- [[prompt_guard()_2]] - code - gateway/tests/test_prompt_guard.py
- [[register_system_prompt + verify_system_prompt should succeed.]] - rationale - gateway/tests/test_prompt_guard.py
- [[test_benign_message()]] - code - gateway/tests/test_prompt_guard.py
- [[test_metadata_guard.py]] - code - gateway/tests/test_metadata_guard.py
- [[test_prompt_guard.py]] - code - gateway/tests/test_prompt_guard.py
- [[test_prompt_guard_init()]] - code - gateway/tests/test_prompt_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_prompt_guardpy
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_PIIConfig]]
- 6 edges to [[_COMMUNITY_AlertDispatcher]]
- 5 edges to [[_COMMUNITY_AuditChain]]
- 4 edges to [[_COMMUNITY_ContextSegment]]
- 2 edges to [[_COMMUNITY_TestNewPatternsV080]]
- 2 edges to [[_COMMUNITY_TestMetadataGuard]]
- 1 edge to [[_COMMUNITY_EgressFilterConfig]]
- 1 edge to [[_COMMUNITY_SessionManager]]

## Top bridge nodes
- [[test_prompt_guard.py]] - degree 14, connects to 4 communities
- [[SystemPromptFingerprint]] - degree 13, connects to 3 communities
- [[TestToolResultScan]] - degree 11, connects to 2 communities
- [[TestSystemPromptHMAC]] - degree 9, connects to 2 communities
- [[TestReanchorDelimiters]] - degree 8, connects to 2 communities
