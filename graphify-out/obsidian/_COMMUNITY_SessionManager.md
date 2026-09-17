---
type: community
cohesion: 0.05
members: 76
---

# SessionManager

**Cohesion:** 0.05 - loosely connected
**Members:** 76 nodes

## Members
- [[.__init__()_160]] - code - gateway/security/session_security.py
- [[._fingerprint()]] - code - gateway/security/session_security.py
- [[.cleanup_expired()_1]] - code - gateway/security/session_security.py
- [[.create_session()]] - code - gateway/security/session_security.py
- [[.destroy_session()]] - code - gateway/security/session_security.py
- [[.generate_instruction_nonce()]] - code - gateway/security/session_security.py
- [[.get_document_tag()]] - code - gateway/security/metadata_guard.py
- [[.guard()_6]] - code - gateway/tests/test_metadata_guard.py
- [[.manager()_2]] - code - gateway/tests/test_session_security.py
- [[.register_event_source()]] - code - gateway/security/session_security.py
- [[.rotate_session()]] - code - gateway/security/session_security.py
- [[.tag_document()]] - code - gateway/security/metadata_guard.py
- [[.test_cleanup_expired()]] - code - gateway/tests/test_session_security.py
- [[.test_create_session()]] - code - gateway/tests/test_session_security.py
- [[.test_destroy_session()]] - code - gateway/tests/test_session_security.py
- [[.test_different_ips_not_rate_limited()]] - code - gateway/tests/test_session_security.py
- [[.test_document_tag_creation()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_document_tag_lookup_by_hash()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_document_tag_untrusted_source()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_expired_session_rejected()]] - code - gateway/tests/test_session_security.py
- [[.test_get_document_tag_unknown_hash_returns_none()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_nonce_expired_rejected()]] - code - gateway/tests/test_session_security.py
- [[.test_nonce_first_use_passes()]] - code - gateway/tests/test_session_security.py
- [[.test_nonce_generation_unique()]] - code - gateway/tests/test_session_security.py
- [[.test_nonce_replay_blocked()]] - code - gateway/tests/test_session_security.py
- [[.test_rate_limit_exceeded()_1]] - code - gateway/tests/test_session_security.py
- [[.test_rate_limit_resets_after_window()]] - code - gateway/tests/test_session_security.py
- [[.test_rotate_session()]] - code - gateway/tests/test_session_security.py
- [[.test_rotated_session_valid()]] - code - gateway/tests/test_session_security.py
- [[.test_session_bound_to_identity()]] - code - gateway/tests/test_session_security.py
- [[.test_session_id_is_cryptographically_random()]] - code - gateway/tests/test_session_security.py
- [[.test_tag_document_different_content_different_hash()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_unknown_event_source_rejected()]] - code - gateway/tests/test_session_security.py
- [[.test_unknown_session_rejected()]] - code - gateway/tests/test_session_security.py
- [[.test_unregistered_session_event_rejected()]] - code - gateway/tests/test_session_security.py
- [[.test_valid_event_source_accepted()]] - code - gateway/tests/test_session_security.py
- [[.test_valid_session_accepted()]] - code - gateway/tests/test_session_security.py
- [[.test_wrong_ip_rejected()]] - code - gateway/tests/test_session_security.py
- [[.test_wrong_user_agent_rejected()]] - code - gateway/tests/test_session_security.py
- [[.validate_event()]] - code - gateway/security/session_security.py
- [[.validate_nonce()]] - code - gateway/security/session_security.py
- [[.validate_session()]] - code - gateway/security/session_security.py
- [[A freshly generated nonce validates on first use.]] - rationale - gateway/tests/test_session_security.py
- [[A nonce with a timestamp outside the 5-min window is rejected.]] - rationale - gateway/tests/test_session_security.py
- [[Any_59]] - code - gateway/security/session_security.py
- [[Chen et al. 2026 (arXiv2602.14364) — Session Hijacking]] - paper - docs/vault/02 - Modules/Security Modules/session_security.py.md
- [[Create and store a provenance tag for a document.]] - rationale - gateway/security/metadata_guard.py
- [[DocumentTag]] - code - gateway/security/metadata_guard.py
- [[Each call generates a distinct nonce.]] - rationale - gateway/tests/test_session_security.py
- [[EventInjectionError]] - code - gateway/security/session_security.py
- [[Generate a single-use, time-bound nonce for an instruction.          Format ``]] - rationale - gateway/security/session_security.py
- [[Look up a document tag by its SHA-256 content hash.]] - rationale - gateway/security/metadata_guard.py
- [[Numbered security control catalog (C8, C9, C18, C47, ...)]] - concept - gateway/tests/test_prompt_guard.py
- [[Provenance record for a document ingested into the agent context.]] - rationale - gateway/security/metadata_guard.py
- [[RateLimitExceeded]] - code - gateway/security/session_security.py
- [[Replaying the same nonce is rejected.]] - rationale - gateway/tests/test_session_security.py
- [[Return True if the nonce is valid (not replayed, within 5-min window).]] - rationale - gateway/security/session_security.py
- [[SessionBindingError]] - code - gateway/security/session_security.py
- [[SessionError]] - code - gateway/security/session_security.py
- [[SessionExpired]] - code - gateway/security/session_security.py
- [[SessionManager]] - code - gateway/security/session_security.py
- [[TestDocumentTagging]] - code - gateway/tests/test_metadata_guard.py
- [[TestEventInjection]] - code - gateway/tests/test_session_security.py
- [[TestInstructionNonce]] - code - gateway/tests/test_session_security.py
- [[TestRateLimiting_2]] - code - gateway/tests/test_session_security.py
- [[TestSessionCleanup]] - code - gateway/tests/test_session_security.py
- [[TestSessionCreation]] - code - gateway/tests/test_session_security.py
- [[TestSessionRotation]] - code - gateway/tests/test_session_security.py
- [[TestSessionValidation]] - code - gateway/tests/test_session_security.py
- [[Wang et al. 2026 (arXiv2602.08412) — Confused Deputy  Event Injection Attacks]] - paper - docs/vault/02 - Modules/Security Modules/oauth_security.py.md
- [[Wang et al. 2026 — Event injection attacks (arXiv2602.08412)]] - paper - gateway/security/session_security.py
- [[manager()_4]] - code - gateway/tests/test_session_security.py
- [[metadata_guard.py]] - code - gateway/security/metadata_guard.py
- [[session_security.py]] - code - gateway/security/session_security.py
- [[test_metadata_guard.py]] - code - gateway/tests/test_metadata_guard.py
- [[test_session_security.py]] - code - gateway/tests/test_session_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/SessionManager
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_lifespan.py]]
- 4 edges to [[_COMMUNITY_ConsentFramework]]
- 2 edges to [[_COMMUNITY_test_security_audit.py]]
- 2 edges to [[_COMMUNITY_TestMetadataGuard]]
- 1 edge to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_TestAuth]]
- 1 edge to [[_COMMUNITY_MiddlewareManager]]

## Top bridge nodes
- [[session_security.py]] - degree 14, connects to 4 communities
- [[SessionManager]] - degree 40, connects to 3 communities
- [[test_metadata_guard.py]] - degree 5, connects to 2 communities
- [[SessionError]] - degree 16, connects to 1 community
- [[TestDocumentTagging]] - degree 9, connects to 1 community