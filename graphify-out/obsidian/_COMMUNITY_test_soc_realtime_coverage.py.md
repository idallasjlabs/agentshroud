---
type: community
cohesion: 0.03
members: 70
---

# test_soc_realtime_coverage.py

**Cohesion:** 0.03 - loosely connected
**Members:** 70 nodes

## Members
- [[.__init__()_110]] - code - gateway/security/prompt_protection.py
- [[._calculate_similarity()]] - code - gateway/security/prompt_protection.py
- [[._compile_detection_patterns()_1]] - code - gateway/security/prompt_protection.py
- [[._load_protected_content()]] - code - gateway/security/prompt_protection.py
- [[._redact_fuzzy_match()]] - code - gateway/security/prompt_protection.py
- [[._redact_match()]] - code - gateway/security/prompt_protection.py
- [[.add_protected_content()]] - code - gateway/security/prompt_protection.py
- [[.get_protection_stats()]] - code - gateway/security/prompt_protection.py
- [[.register_bot_hostnames()]] - code - gateway/security/prompt_protection.py
- [[.scan_response()_2]] - code - gateway/security/prompt_protection.py
- [[.test_add_protected_content()]] - code - gateway/tests/test_prompt_protection.py
- [[.test_credential_redaction()]] - code - gateway/tests/test_prompt_protection.py
- [[.test_disabled_protection()]] - code - gateway/tests/test_prompt_protection.py
- [[.test_dynamic_bot_hostname_redaction()]] - code - gateway/tests/test_prompt_protection.py
- [[.test_edge_cases()_2]] - code - gateway/tests/test_prompt_protection.py
- [[.test_file_reference_redaction()]] - code - gateway/tests/test_prompt_protection.py
- [[.test_fuzzy_matching()]] - code - gateway/tests/test_prompt_protection.py
- [[.test_hash_fingerprinting()]] - code - gateway/tests/test_prompt_protection.py
- [[.test_infrastructure_redaction()]] - code - gateway/tests/test_prompt_protection.py
- [[.test_initialization()_3]] - code - gateway/tests/test_prompt_protection.py
- [[.test_multiple_redactions()]] - code - gateway/tests/test_prompt_protection.py
- [[.test_normal_content_passes()_1]] - code - gateway/tests/test_prompt_protection.py
- [[.test_product_name_not_redacted()]] - code - gateway/tests/test_prompt_protection.py
- [[.test_protected_content_loading()]] - code - gateway/tests/test_prompt_protection.py
- [[.test_protection_stats()]] - code - gateway/tests/test_prompt_protection.py
- [[.test_structural_pattern_redaction()]] - code - gateway/tests/test_prompt_protection.py
- [[.test_tool_inventory_redaction()]] - code - gateway/tests/test_prompt_protection.py
- [[.test_user_id_redaction()]] - code - gateway/tests/test_prompt_protection.py
- [[A piece of content that should be protected from disclosure.]] - rationale - gateway/security/prompt_protection.py
- [[Add bot container hostnames to the infrastructure detection patterns.          C]] - rationale - gateway/security/prompt_protection.py
- [[Add content to the protected registry.          Args             name Identifi]] - rationale - gateway/security/prompt_protection.py
- [[Any_54]] - code - gateway/security/prompt_protection.py
- [[Calculate similarity between text and protected content.]] - rationale - gateway/security/prompt_protection.py
- [[Compile regex patterns for detecting disclosure attempts.]] - rationale - gateway/security/prompt_protection.py
- [[Create a PromptProtection instance for testing.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Get statistics about the protection system.]] - rationale - gateway/security/prompt_protection.py
- [[Initialize prompt protection system.          Args             config Configur]] - rationale - gateway/security/prompt_protection.py
- [[Load protected content from configured sources.]] - rationale - gateway/security/prompt_protection.py
- [[Main system prompt protection engine.      Maintains fingerprints of sensitive c]] - rationale - gateway/security/prompt_protection.py
- [[Match]] - code - gateway/security/prompt_protection.py
- [[Product name 'agentshroud' and 'agentshroud-openclaw' are public branding — must]] - rationale - gateway/tests/test_prompt_protection.py
- [[PromptProtection]] - code - gateway/security/prompt_protection.py
- [[ProtectedContent]] - code - gateway/security/prompt_protection.py
- [[Redact text that fuzzy matches protected content.]] - rationale - gateway/security/prompt_protection.py
- [[Replace a regex match with a redaction placeholder.]] - rationale - gateway/security/prompt_protection.py
- [[Sample protected content for testing.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Scan text for protected content and return redacted version.          Args]] - rationale - gateway/security/prompt_protection.py
- [[System Prompt Protection Tests]] - code - gateway/tests/test_prompt_protection.py
- [[Test adding protected content.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Test cases for PromptProtection class.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Test edge cases and error conditions._1]] - rationale - gateway/tests/test_prompt_protection.py
- [[Test fuzzy matching against protected content.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Test getting protection statistics.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Test loading protected content from files.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Test proper initialization of PromptProtection.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Test redaction of credential patterns.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Test redaction of file references.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Test redaction of system prompt structural patterns.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Test redaction of targeted infrastructure details.          Generic hostnames (e]] - rationale - gateway/tests/test_prompt_protection.py
- [[Test redaction of tool inventory details.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Test redaction of user ID patterns.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Test text with multiple types of sensitive content.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Test that content is properly fingerprinted with hashes.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Test that disabled protection passes through content unchanged.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Test that dynamically registered bot hostnames are redacted.]] - rationale - gateway/tests/test_prompt_protection.py
- [[Test that normal content passes through without redaction.]] - rationale - gateway/tests/test_prompt_protection.py
- [[TestPromptProtection]] - code - gateway/tests/test_prompt_protection.py
- [[prompt_protection()]] - code - gateway/tests/test_prompt_protection.py
- [[sample_protected_content()]] - code - gateway/tests/test_prompt_protection.py
- [[test_prompt_protection.py]] - code - gateway/tests/test_prompt_protection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_soc_realtime_coveragepy
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_TrustManager]]
- 3 edges to [[_COMMUNITY_DockerEngine]]
- 2 edges to [[_COMMUNITY__wrap_response()]]
- 1 edge to [[_COMMUNITY_RBACConfig]]

## Top bridge nodes
- [[PromptProtection]] - degree 23, connects to 4 communities
- [[.scan_response()_2]] - degree 5, connects to 1 community
- [[ProtectedContent]] - degree 5, connects to 1 community
- [[System Prompt Protection Tests]] - degree 2, connects to 1 community