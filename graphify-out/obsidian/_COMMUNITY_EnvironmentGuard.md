---
type: community
members: 53
---

# EnvironmentGuard

**Members:** 53 nodes

## Members
- [[dot-__init__()_26]] - code - gateway/security/env_guard.py
- [[dot-_contains_env_access_patterns()]] - code - gateway/security/env_guard.py
- [[dot-_looks_like_credential()]] - code - gateway/security/env_guard.py
- [[dot-_make_record()]] - code - gateway/tests/test_security_audit.py
- [[dot-_record_leakage()]] - code - gateway/security/env_guard.py
- [[dot-check_command_execution()]] - code - gateway/security/env_guard.py
- [[dot-check_file_access()]] - code - gateway/security/env_guard.py
- [[dot-clear_detected_leakages()]] - code - gateway/security/env_guard.py
- [[dot-export_leakage_report()]] - code - gateway/security/env_guard.py
- [[dot-get_leakage_summary()]] - code - gateway/security/env_guard.py
- [[dot-monitor_environment_access()]] - code - gateway/security/env_guard.py
- [[dot-scrub_command_output()]] - code - gateway/security/env_guard.py
- [[dot-test_aws_key_redaction()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_aws_key_redaction_via_pattern()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_credit_card_in_logs()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_dns_tunneling_detection()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_egress_monitor_loaded()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_env_guard_command_check()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_env_guard_detects_data_access()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_env_guard_monitoring()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_env_guard_scrub_output()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_git_guard_detects_credential_patterns()]] - code - gateway/tests/test_security_audit_advanced.py
- [[dot-test_git_guard_scan_repo()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_github_token_redaction()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_jwt_redaction()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_natural_language_question_is_allowed()]] - code - gateway/tests/test_round2_hardening.py
- [[dot-test_ssn_redaction_in_logs()]] - code - gateway/tests/test_security_audit.py
- [[dot-test_unparseable_text_is_allowed()]] - code - gateway/tests/test_round2_hardening.py
- [[Any_14]] - code
- [[Check if a value looks like a credential.]] - rationale - gateway/security/env_guard.py
- [[Check if command contains patterns that could access environment.]] - rationale - gateway/security/env_guard.py
- [[Check if command execution should be blocked to prevent environment leakage.…]] - rationale - gateway/security/env_guard.py
- [[Check if file access should be blocked to prevent environment leakage. Args…]] - rationale - gateway/security/env_guard.py
- [[Clear the list of detected leakages.]] - rationale - gateway/security/env_guard.py
- [[Detected environment variable leakage.]] - rationale - gateway/security/env_guard.py
- [[Egress monitoring should be available.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Environment guard should monitor data access patterns.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[EnvironmentGuard]] - code - gateway/security/env_guard.py
- [[EnvironmentLeakage]] - code - gateway/security/env_guard.py
- [[Export leakage findings to a report file.]] - rationale - gateway/security/env_guard.py
- [[Get summary of all detected leakages.]] - rationale - gateway/security/env_guard.py
- [[Git guard should catch credential patterns.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Guard against environment variable leakage and unauthorized access.]] - rationale - gateway/security/env_guard.py
- [[High-entropy DNS queries indicate tunneling.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Monitor an agent's environment access attempts. Args agent_id ID of agent to…]] - rationale - gateway/security/env_guard.py
- [[Record a detected environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Scrub environment variables and API keys from command output. Args output…]] - rationale - gateway/security/env_guard.py
- [[Test detection of data exfiltration patterns.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Test log sanitization and information leakage prevention.]] - rationale - gateway/tests/test_security_audit.py
- [[TestEnvGuardFailOpen]] - code - gateway/tests/test_round2_hardening.py
- [[TestExfiltrationDetection]] - code - gateway/tests/test_security_audit_advanced.py
- [[TestLoggingSecurity]] - code - gateway/tests/test_security_audit.py
- [[t_env()]] - code - gateway/ingest_api/main.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/EnvironmentGuard
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_GitGuard]]
- 4 edges to [[_COMMUNITY_FileSandbox]]
- 3 edges to [[_COMMUNITY_check_command]]
- 3 edges to [[_COMMUNITY_LogSanitizer]]
- 2 edges to [[_COMMUNITY_MiddlewareManager]]
- 2 edges to [[_COMMUNITY_test_env_guard_class.py]]
- 2 edges to [[_COMMUNITY_test_security_audit.py]]
- 2 edges to [[_COMMUNITY_deep_security_test]]
- 2 edges to [[_COMMUNITY_DNSFilterConfig]]
- 2 edges to [[_COMMUNITY_web_proxy.py]]
- 1 edge to [[_COMMUNITY_ingest_apimain.py]]
- 1 edge to [[_COMMUNITY_middleware.py]]
- 1 edge to [[_COMMUNITY_lifespan.py]]

## Top bridge nodes
- [[EnvironmentGuard]] - degree 35, connects to 9 communities
- [[TestExfiltrationDetection]] - degree 14, connects to 5 communities
- [[TestLoggingSecurity]] - degree 17, connects to 4 communities
- [[TestEnvGuardFailOpen]] - degree 4, connects to 1 community
- [[EnvironmentLeakage]] - degree 3, connects to 1 community
