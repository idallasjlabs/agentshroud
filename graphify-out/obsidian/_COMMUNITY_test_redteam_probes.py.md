---
type: community
cohesion: 0.02
members: 92
---

# test_redteam_probes.py

**Cohesion:** 0.02 - loosely connected
**Members:** 92 nodes

## Members
- [[.filter_response()]] - code - gateway/security/xml_leak_filter.py
- [[.scan_command_injection()]] - code - gateway/security/xml_leak_filter.py
- [[.setup_method()_29]] - code - gateway/tests/test_xml_leak_filter.py
- [[.test_clean_response_passes_through()]] - code - gateway/tests/test_xml_leak_filter.py
- [[.test_clean_text_passes()]] - code - gateway/tests/test_xml_leak_filter.py
- [[.test_empty_text_returns_clean()]] - code - gateway/tests/test_xml_leak_filter.py
- [[.test_file_path_removal()]] - code - gateway/tests/test_xml_leak_filter.py
- [[.test_function_calls_xml_removal()]] - code - gateway/tests/test_xml_leak_filter.py
- [[.test_python_eval_detected()]] - code - gateway/tests/test_xml_leak_filter.py
- [[.test_quick_function_calls_filter()]] - code - gateway/tests/test_xml_leak_filter.py
- [[.test_shell_injection_detected()]] - code - gateway/tests/test_xml_leak_filter.py
- [[.test_sql_injection_detected()]] - code - gateway/tests/test_xml_leak_filter.py
- [[.xml_filter()]] - code - gateway/tests/test_xml_leak_filter.py
- [[AgentShroud Blue Team Security Auditor (SEC-DEFENSE)]] - document - .agents/skills/i-sec-defense/SKILL.md
- [[AgentShroud Red Team Adversarial Tester (SEC-OFFENSE)]] - document - .agents/skills/i-sec-offense/SKILL.md
- [[Audit chain must detect tampering.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Blue Team Security Auditor README]] - document - .agents/skills/i-sec-defense/README.md
- [[Build a SecurityPipeline with all guards wired up.]] - rationale - gateway/tests/test_redteam_probes.py
- [[CVE-2026-22172 — WebSocket Scope Self-Declaration]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-32922 — Token Scope Expansion via device.token.rotate]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-34425 — Preflight Validation Bypass (Shell-Bleed)]] - rationale - docs/security/cve-mitigation-matrix.md
- [[CVE-2026-3690 — Canvas Authentication Bypass]] - rationale - docs/security/cve-mitigation-matrix.md
- [[Combined prompt injection + role override must be caught.]] - rationale - gateway/tests/test_redteam_probes.py
- [[ContextGuard must detect context window poisoning (massive payload).]] - rationale - gateway/tests/test_redteam_probes.py
- [[Create a real PII sanitizer in regex mode (no spaCy).]] - rationale - gateway/tests/test_redteam_probes.py
- [[EncodingDetector must detect base64 in outbound responses.]] - rationale - gateway/tests/test_redteam_probes.py
- [[EncodingDetector must detect base64-encoded payloads on inbound.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Every pipeline operation must produce an audit chain entry.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Filter outbound response content to remove sensitive information.          Args]] - rationale - gateway/security/xml_leak_filter.py
- [[FilterResult_1]] - code - gateway/security/xml_leak_filter.py
- [[Minimal approval queue mock that accepts items.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Non-owner collaborators must be blocked by prompt guard.]] - rationale - gateway/tests/test_redteam_probes.py
- [[One agent's session data must not leak to another.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Probe 1.1 Agent exec must go through approval queue or be blocked.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Probe 1.1b delete_file action must go through approval or be blocked.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Probe 1.1c admin_action must require approval or be trust-blocked.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Probe 1.6 EgressFilter must block non-allowlisted domains.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Probe 1.6b EgressFilter must block direct IP exfiltration.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Probe 1.6c EgressFilter must block internalprivate IP ranges.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Probe 1.9 PII sanitizer must redact SSN on inbound messages.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Probe 1.9b PII sanitizer must redact SSN on outbound responses.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Probe 1.9c PII sanitizer must redact credit card numbers.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Probe 1.9d PII sanitizer must redact email addresses on outbound.]] - rationale - gateway/tests/test_redteam_probes.py
- [[PromptGuard must block classic 'ignore instructions' injection.]] - rationale - gateway/tests/test_redteam_probes.py
- [[PromptGuard must block role-override injection.]] - rationale - gateway/tests/test_redteam_probes.py
- [[PromptGuard must detect system prompt extraction attempts.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Red Team Adversarial Tester README]] - document - .agents/skills/i-sec-offense/README.md
- [[Result from XML leak filtering.]] - rationale - gateway/security/xml_leak_filter.py
- [[STPA-Sec Methodology]] - concept - .agents/skills/i-sec-defense/SKILL.md
- [[Scan outbound text for command  code injection patterns.          Does NOT modi]] - rationale - gateway/security/xml_leak_filter.py
- [[Set up test fixtures._2]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Steve Hay Adversary Model]] - concept - .agents/skills/i-sec-offense/SKILL.md
- [[Test cases for XMLLeakFilter.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test removal of file paths from responses.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test removal of function call XML blocks.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test that clean responses pass through unchanged.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[Test the performance-optimized function calls only filter.]] - rationale - gateway/tests/test_xml_leak_filter.py
- [[TestCommandInjectionScan]] - code - gateway/tests/test_xml_leak_filter.py
- [[TestXMLLeakFilter]] - code - gateway/tests/test_xml_leak_filter.py
- [[Trust level must not allow exec from conversation alone.]] - rationale - gateway/tests/test_redteam_probes.py
- [[_make_approval_queue()]] - code - gateway/tests/test_redteam_probes.py
- [[_make_full_pipeline()]] - code - gateway/tests/test_redteam_probes.py
- [[_make_pii_sanitizer()]] - code - gateway/tests/test_redteam_probes.py
- [[cve-mitigation-matrix]] - document - docs/security/cve-mitigation-matrix.md
- [[docsreviewsblue-team-audit-v0.7.0]] - concept - docs/reviews/blue-team-audit-v0.7.0.md
- [[docsreviewsred-team-report-v0.7.0]] - concept - docs/reviews/red-team-report-v0.7.0.md
- [[pipeline()_2]] - code - gateway/tests/test_redteam_probes.py
- [[test_admin_action_requires_approval()]] - code - gateway/tests/test_redteam_probes.py
- [[test_audit_chain_records_all_events()]] - code - gateway/tests/test_redteam_probes.py
- [[test_audit_chain_tamper_detection()]] - code - gateway/tests/test_redteam_probes.py
- [[test_combined_injection_techniques()]] - code - gateway/tests/test_redteam_probes.py
- [[test_context_poisoning_blocked()]] - code - gateway/tests/test_redteam_probes.py
- [[test_credit_card_redacted_inbound()]] - code - gateway/tests/test_redteam_probes.py
- [[test_egress_blocks_internal_ip()]] - code - gateway/tests/test_redteam_probes.py
- [[test_egress_blocks_ip_exfil()]] - code - gateway/tests/test_redteam_probes.py
- [[test_egress_blocks_unknown_domain()]] - code - gateway/tests/test_redteam_probes.py
- [[test_email_redacted_outbound()]] - code - gateway/tests/test_redteam_probes.py
- [[test_encoding_detector_base64_outbound()]] - code - gateway/tests/test_redteam_probes.py
- [[test_encoding_detector_catches_base64_inbound()]] - code - gateway/tests/test_redteam_probes.py
- [[test_exec_delete_file_requires_approval()]] - code - gateway/tests/test_redteam_probes.py
- [[test_exec_requires_approval()]] - code - gateway/tests/test_redteam_probes.py
- [[test_non_owner_blocked_by_prompt_guard()]] - code - gateway/tests/test_redteam_probes.py
- [[test_prompt_extraction_attempt()]] - code - gateway/tests/test_redteam_probes.py
- [[test_prompt_injection_ignore_instructions()]] - code - gateway/tests/test_redteam_probes.py
- [[test_prompt_injection_role_override()]] - code - gateway/tests/test_redteam_probes.py
- [[test_redteam_probes.py]] - code - gateway/tests/test_redteam_probes.py
- [[test_session_isolation()]] - code - gateway/tests/test_redteam_probes.py
- [[test_ssn_redacted_inbound()]] - code - gateway/tests/test_redteam_probes.py
- [[test_ssn_redacted_outbound()]] - code - gateway/tests/test_redteam_probes.py
- [[test_trust_escalation_blocked()]] - code - gateway/tests/test_redteam_probes.py
- [[test_xml_leak_filter.py]] - code - gateway/tests/test_xml_leak_filter.py
- [[xml_leak_filter.py]] - code - gateway/security/xml_leak_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_redteam_probespy
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_TrustManager]]
- 13 edges to [[_COMMUNITY_lifespan.py]]
- 5 edges to [[_COMMUNITY_ingest_apimain.py]]
- 4 edges to [[_COMMUNITY_EgressFilterConfig]]
- 3 edges to [[_COMMUNITY_tool_result_injection.py]]
- 2 edges to [[_COMMUNITY_TrustConfig]]
- 2 edges to [[_COMMUNITY_EgressFilter]]
- 2 edges to [[_COMMUNITY_EgressPolicy]]
- 2 edges to [[_COMMUNITY_ToolResultSanitizer]]
- 2 edges to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_TrustLevel]]
- 1 edge to [[_COMMUNITY_EncryptedStore]]
- 1 edge to [[_COMMUNITY_DeceptionDetection]]
- 1 edge to [[_COMMUNITY_AuditStore]]
- 1 edge to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_MemoryIntegrityMonitor]]
- 1 edge to [[_COMMUNITY_system-requirements]]
- 1 edge to [[_COMMUNITY_test_daily_cve_report.py]]
- 1 edge to [[_COMMUNITY_AgentShroud™ CVE Mitigation Matrix]]
- 1 edge to [[_COMMUNITY_DNSFilterConfig]]
- 1 edge to [[_COMMUNITY_ToolACLEnforcer]]
- 1 edge to [[_COMMUNITY_ApprovalRequest]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_KeyRotationConfig]]
- 1 edge to [[_COMMUNITY_PromptProtection]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_LLMProxy.proxy_messages]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_OutboundInfoFilter]]
- 1 edge to [[_COMMUNITY_FileSandbox]]
- 1 edge to [[_COMMUNITY_AgentShroud Security Verification (13-check driv]]

## Top bridge nodes
- [[AgentShroud Blue Team Security Auditor (SEC-DEFENSE)]] - degree 29, connects to 19 communities
- [[cve-mitigation-matrix]] - degree 13, connects to 8 communities
- [[test_redteam_probes.py]] - degree 40, connects to 7 communities
- [[_make_full_pipeline()]] - degree 20, connects to 6 communities
- [[xml_leak_filter.py]] - degree 6, connects to 3 communities