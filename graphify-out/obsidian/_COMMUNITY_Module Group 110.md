---
type: community
cohesion: 0.05
members: 41
---

# Module Group 110

**Cohesion:** 0.05 - loosely connected
**Members:** 41 nodes

## Members
- [[.__init__()_77]] - code - gateway/security/metadata_guard.py
- [[.check_for_exif()]] - code - gateway/security/metadata_guard.py
- [[.check_oversized_headers()]] - code - gateway/security/metadata_guard.py
- [[.sanitize_filename()]] - code - gateway/security/metadata_guard.py
- [[.sanitize_headers()]] - code - gateway/security/metadata_guard.py
- [[.sanitize_image_metadata()]] - code - gateway/security/metadata_guard.py
- [[.test_browser_security_loaded()]] - code - gateway/tests/test_security_audit.py
- [[.test_dns_entropy_calculator()]] - code - gateway/tests/test_security_audit.py
- [[.test_dns_filter_config()]] - code - gateway/tests/test_security_audit.py
- [[.test_dns_low_entropy_legit()]] - code - gateway/tests/test_security_audit.py
- [[.test_egress_monitor_loaded()]] - code - gateway/tests/test_security_audit.py
- [[.test_encrypted_store_error_no_key_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_env_guard_scrubs_output()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_git_guard_no_path_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_log_sanitizer_covers_stack_traces()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_metadata_guard_strips_internal_headers()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_metadata_oversized_headers()]] - code - gateway/tests/test_security_audit.py
- [[.test_metadata_path_traversal_stripped()]] - code - gateway/tests/test_security_audit.py
- [[.test_metadata_sanitize_filename()]] - code - gateway/tests/test_security_audit.py
- [[.test_network_validator_importable()]] - code - gateway/tests/test_security_audit.py
- [[.test_oauth_redirect_mismatch()]] - code - gateway/tests/test_security_audit.py
- [[.test_token_error_no_secret_leak()]] - code - gateway/tests/test_security_audit_advanced.py
- [[Check if binary data contains EXIF metadata.]] - rationale - gateway/security/metadata_guard.py
- [[Check if headers exceed size limits.]] - rationale - gateway/security/metadata_guard.py
- [[Decryption errors shouldn't expose the encryption key.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Environment guard should scrub sensitive output.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Git guard errors shouldn't expose full file paths.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Guards against metadata channel attacks and information disclosure.]] - rationale - gateway/security/metadata_guard.py
- [[High-entropy domains (potential tunneling).]] - rationale - gateway/tests/test_security_audit.py
- [[Internal infrastructure headers should be stripped.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Legit domains have lower entropy.]] - rationale - gateway/tests/test_security_audit.py
- [[MetadataGuard]] - code - gateway/security/metadata_guard.py
- [[Remove EXIF metadata from image data if present.]] - rationale - gateway/security/metadata_guard.py
- [[Sanitize HTTP headers by removing sensitive information.]] - rationale - gateway/security/metadata_guard.py
- [[Sanitize filename by removing unicode control characters and normalizing.]] - rationale - gateway/security/metadata_guard.py
- [[Stack traces containing secrets should be sanitized.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test DNS filtering, SSRF prevention, and egress control.]] - rationale - gateway/tests/test_security_audit.py
- [[Test that errors don't leak sensitive information.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[TestInfoLeakage]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestNetworkSecurity]] - code - gateway/tests/test_security_audit.py
- [[Token validation errors shouldn't expose signing keys.]] - rationale - gateway/tests/test_security_audit_advanced.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_110
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 19 edges to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 12 edges to [[_COMMUNITY_Environment Guard & Leak Detection]]
- 9 edges to [[_COMMUNITY_Alert Dispatcher]]
- 8 edges to [[_COMMUNITY_Module Group 116]]
- 5 edges to [[_COMMUNITY_Subagent Monitor]]
- 4 edges to [[_COMMUNITY_Module Group 66]]
- 3 edges to [[_COMMUNITY_Module Group 88]]
- 3 edges to [[_COMMUNITY_Module Group 80]]
- 2 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 2 edges to [[_COMMUNITY_Module Group 102]]
- 2 edges to [[_COMMUNITY_DNS Filter & Tunneling Detection]]
- 2 edges to [[_COMMUNITY_Module Group 63]]
- 2 edges to [[_COMMUNITY_Module Group 103]]
- 2 edges to [[_COMMUNITY_Context Guard & Integrity]]
- 2 edges to [[_COMMUNITY_Progressive Trust Levels]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Module Group 113]]
- 1 edge to [[_COMMUNITY_Module Group 258]]
- 1 edge to [[_COMMUNITY_Module Group 257]]
- 1 edge to [[_COMMUNITY_Module Group 137]]

## Top bridge nodes
- [[TestNetworkSecurity]] - degree 47, connects to 16 communities
- [[TestInfoLeakage]] - degree 31, connects to 13 communities
- [[MetadataGuard]] - degree 53, connects to 11 communities
- [[.test_encrypted_store_error_no_key_leak()]] - degree 3, connects to 1 community
- [[.test_env_guard_scrubs_output()]] - degree 3, connects to 1 community