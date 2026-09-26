---
type: community
cohesion: 0.04
members: 53
---

# test_approval_queue.py

**Cohesion:** 0.04 - loosely connected
**Members:** 53 nodes

## Members
- [[Audit chain must detect tampering.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Build a SecurityPipeline with all guards wired up.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Combined prompt injection + role override must be caught.]] - rationale - gateway/tests/test_redteam_probes.py
- [[ContextGuard must detect context window poisoning (massive payload).]] - rationale - gateway/tests/test_redteam_probes.py
- [[EncodingDetector must detect base64 in outbound responses.]] - rationale - gateway/tests/test_redteam_probes.py
- [[EncodingDetector must detect base64-encoded payloads on inbound.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Every pipeline operation must produce an audit chain entry.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Minimal approval queue mock that accepts items.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Non-owner collaborators must be blocked by prompt guard.]] - rationale - gateway/tests/test_redteam_probes.py
- [[One agent's session data must not leak to another.]] - rationale - gateway/tests/test_redteam_probes.py
- [[Pipeline must refuse to start without PII sanitizer (fail-closed).]] - rationale - gateway/tests/test_redteam_probes.py
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
- [[SecurityPipeline_1]] - code - gateway/tests/test_redteam_probes.py
- [[Trust level must not allow exec from conversation alone.]] - rationale - gateway/tests/test_redteam_probes.py
- [[_make_approval_queue()]] - code - gateway/tests/test_redteam_probes.py
- [[_make_full_pipeline()]] - code - gateway/tests/test_redteam_probes.py
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
- [[test_pipeline_fails_closed_without_pii()]] - code - gateway/tests/test_redteam_probes.py
- [[test_prompt_extraction_attempt()]] - code - gateway/tests/test_redteam_probes.py
- [[test_prompt_injection_ignore_instructions()]] - code - gateway/tests/test_redteam_probes.py
- [[test_prompt_injection_role_override()]] - code - gateway/tests/test_redteam_probes.py
- [[test_redteam_probes.py]] - code - gateway/tests/test_redteam_probes.py
- [[test_session_isolation()]] - code - gateway/tests/test_redteam_probes.py
- [[test_ssn_redacted_inbound()]] - code - gateway/tests/test_redteam_probes.py
- [[test_ssn_redacted_outbound()]] - code - gateway/tests/test_redteam_probes.py
- [[test_trust_escalation_blocked()]] - code - gateway/tests/test_redteam_probes.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_approval_queuepy
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_ResourceGuard]]
- 5 edges to [[_COMMUNITY_MemoryIntegrityMonitor]]
- 4 edges to [[_COMMUNITY_RBACConfig]]
- 3 edges to [[_COMMUNITY_TrustManager]]
- 3 edges to [[_COMMUNITY_ConsentFramework]]
- 3 edges to [[_COMMUNITY_EgressApprovalQueue]]
- 3 edges to [[_COMMUNITY_Production Safety Checklist (SKILL)]]
- 3 edges to [[_COMMUNITY_EgressFilter]]
- 3 edges to [[_COMMUNITY_ServiceManager]]
- 3 edges to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_DockerEngine]]
- 1 edge to [[_COMMUNITY_OutboundInfoFilter]]

## Top bridge nodes
- [[test_redteam_probes.py]] - degree 40, connects to 11 communities
- [[_make_full_pipeline()]] - degree 20, connects to 10 communities
- [[SecurityPipeline_1]] - degree 14, connects to 10 communities
- [[_make_approval_queue()]] - degree 4, connects to 1 community
- [[test_pipeline_fails_closed_without_pii()]] - degree 4, connects to 1 community