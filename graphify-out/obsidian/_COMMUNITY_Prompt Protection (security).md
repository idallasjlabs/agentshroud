---
type: community
cohesion: 0.09
members: 31
---

# Prompt Protection (security)

**Cohesion:** 0.09 - loosely connected
**Members:** 31 nodes

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
- [[A piece of content that should be protected from disclosure.]] - rationale - gateway/security/prompt_protection.py
- [[Add bot container hostnames to the infrastructure detection patterns.          C]] - rationale - gateway/security/prompt_protection.py
- [[Add content to the protected registry.          Args             name Identifi]] - rationale - gateway/security/prompt_protection.py
- [[Any_54]] - code - gateway/security/prompt_protection.py
- [[Calculate similarity between text and protected content.]] - rationale - gateway/security/prompt_protection.py
- [[Compile regex patterns for detecting disclosure attempts.]] - rationale - gateway/security/prompt_protection.py
- [[Get statistics about the protection system.]] - rationale - gateway/security/prompt_protection.py
- [[Initialize prompt protection system.          Args             config Configur]] - rationale - gateway/security/prompt_protection.py
- [[Load protected content from configured sources.]] - rationale - gateway/security/prompt_protection.py
- [[Main system prompt protection engine.      Maintains fingerprints of sensitive c]] - rationale - gateway/security/prompt_protection.py
- [[Match]] - code - gateway/security/prompt_protection.py
- [[Output Canary System Tests]] - code - gateway/tests/test_output_canary.py
- [[PromptProtection]] - code - gateway/security/prompt_protection.py
- [[ProtectedContent]] - code - gateway/security/prompt_protection.py
- [[Redact text that fuzzy matches protected content.]] - rationale - gateway/security/prompt_protection.py
- [[RedactionResult_2]] - code - gateway/security/prompt_protection.py
- [[Replace a regex match with a redaction placeholder.]] - rationale - gateway/security/prompt_protection.py
- [[Result of scanning and redacting content.]] - rationale - gateway/security/prompt_protection.py
- [[Scan text for protected content and return redacted version.          Args]] - rationale - gateway/security/prompt_protection.py
- [[System Prompt Protection Tests]] - code - gateway/tests/test_prompt_protection.py
- [[prompt_protection.py]] - code - gateway/security/prompt_protection.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Prompt_Protection_security
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_Prompt Protection]]
- 3 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 2 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 2 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 1 edge to [[_COMMUNITY_Outbound Filter]]

## Top bridge nodes
- [[PromptProtection]] - degree 23, connects to 4 communities
- [[prompt_protection.py]] - degree 5, connects to 1 community
- [[Output Canary System Tests]] - degree 2, connects to 1 community