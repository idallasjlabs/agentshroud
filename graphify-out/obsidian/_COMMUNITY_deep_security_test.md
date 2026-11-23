---
type: community
members: 39
---

# deep_security_test

**Members:** 39 nodes

## Members
- [[dot-__init__()_39]] - code - gateway/security/log_sanitizer.py
- [[dot-_compile_patterns()]] - code - gateway/security/log_sanitizer.py
- [[dot-_sanitize_text()]] - code - gateway/security/log_sanitizer.py
- [[dot-filter()]] - code - gateway/security/log_sanitizer.py
- [[dot-get_log_sanitizer()]] - code - gateway/ingest_api/middleware.py
- [[dot-setup_method()_9]] - code - gateway/tests/test_log_sanitizer.py
- [[Compile regex patterns for sensitive data detection.]] - rationale - gateway/security/log_sanitizer.py
- [[Comprehensive security integration test — tests every module with real payloads.]] - rationale - gateway/ingest_api/main.py
- [[Custom logging filter that sanitizes sensitive data from log records.]] - rationale - gateway/security/log_sanitizer.py
- [[Filter log record, sanitizing sensitive content.]] - rationale - gateway/security/log_sanitizer.py
- [[Get the log sanitizer for integration with logging system.]] - rationale - gateway/ingest_api/middleware.py
- [[LogRecord]] - code
- [[LogSanitizer]] - code - gateway/security/log_sanitizer.py
- [[Pattern_3]] - code
- [[Sanitize sensitive data in text.]] - rationale - gateway/security/log_sanitizer.py
- [[Test Log Sanitizer PII Scrubbing]] - code - gateway/tests/test_log_sanitizer.py
- [[_check_mod()]] - code - gateway/ingest_api/main.py
- [[_pii()]] - code - gateway/ingest_api/main.py
- [[atest()]] - code - gateway/ingest_api/main.py
- [[deep_security_test()]] - code - gateway/ingest_api/main.py
- [[t_alert()]] - code - gateway/ingest_api/main.py
- [[t_audit()]] - code - gateway/ingest_api/main.py
- [[t_auth()]] - code - gateway/ingest_api/main.py
- [[t_canary()]] - code - gateway/ingest_api/main.py
- [[t_clamav()]] - code - gateway/ingest_api/main.py
- [[t_context()]] - code - gateway/ingest_api/main.py
- [[t_drift()]] - code - gateway/ingest_api/main.py
- [[t_egress()]] - code - gateway/ingest_api/main.py
- [[t_encrypt()]] - code - gateway/ingest_api/main.py
- [[t_git()]] - code - gateway/ingest_api/main.py
- [[t_hardening()]] - code - gateway/ingest_api/main.py
- [[t_keyvault()]] - code - gateway/ingest_api/main.py
- [[t_log()]] - code - gateway/ingest_api/main.py
- [[t_op()]] - code - gateway/ingest_api/main.py
- [[t_prompt()]] - code - gateway/ingest_api/main.py
- [[t_sandbox()]] - code - gateway/ingest_api/main.py
- [[t_trivy()]] - code - gateway/ingest_api/main.py
- [[t_trust()]] - code - gateway/ingest_api/main.py
- [[test()]] - code - gateway/ingest_api/main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/deep_security_test
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_TestLogSanitizer]]
- 5 edges to [[_COMMUNITY_middleware.py]]
- 4 edges to [[_COMMUNITY_ingest_apimain.py]]
- 3 edges to [[_COMMUNITY_EnvironmentGuard]]
- 3 edges to [[_COMMUNITY_ContextGuard]]
- 3 edges to [[_COMMUNITY_ResourceGuard]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_TestInfoLeakage]]
- 2 edges to [[_COMMUNITY_EgressPolicy]]
- 2 edges to [[_COMMUNITY_test_security_audit.py]]
- 2 edges to [[_COMMUNITY_ContainerSnapshot]]
- 2 edges to [[_COMMUNITY_DNSFilterConfig]]
- 2 edges to [[_COMMUNITY_TokenValidator]]
- 2 edges to [[_COMMUNITY_MetadataGuard]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 2 edges to [[_COMMUNITY_GitGuard]]
- 2 edges to [[_COMMUNITY_PromptGuard]]
- 2 edges to [[_COMMUNITY_TestAuth_1]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_test_security_integration.py]]

## Top bridge nodes
- [[deep_security_test()]] - degree 48, connects to 14 communities
- [[LogSanitizer]] - degree 24, connects to 9 communities
- [[t_sandbox()]] - degree 3, connects to 1 community
- [[dot-get_log_sanitizer()]] - degree 3, connects to 1 community
- [[t_context()]] - degree 2, connects to 1 community
