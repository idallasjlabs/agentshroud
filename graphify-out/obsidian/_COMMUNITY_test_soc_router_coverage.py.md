---
type: community
cohesion: 0.03
members: 139
---

# test_soc_router_coverage.py

**Cohesion:** 0.03 - loosely connected
**Members:** 139 nodes

## Members
- [[.__init__()_71]] - code - gateway/security/differential_pii_detector.py
- [[.__init__()_139]] - code - gateway/tests/test_a2a_proxy.py
- [[.__init__()_137]] - code - gateway/tests/test_a2a_proxy.py
- [[.__init__()_148]] - code - gateway/tests/test_differential_pii_detector.py
- [[.__post_init__()_4]] - code - gateway/security/differential_pii_detector.py
- [[._deduplicate()]] - code - gateway/security/differential_pii_detector.py
- [[._detect_pii()]] - code - gateway/security/differential_pii_detector.py
- [[._detect_presidio()]] - code - gateway/security/differential_pii_detector.py
- [[._detect_regex()]] - code - gateway/security/differential_pii_detector.py
- [[._detector_with_fake()]] - code - gateway/tests/test_differential_pii_detector.py
- [[._init_presidio()_1]] - code - gateway/security/differential_pii_detector.py
- [[._redact()]] - code - gateway/security/differential_pii_detector.py
- [[._scan()]] - code - gateway/security/differential_pii_detector.py
- [[.forward()_2]] - code - gateway/tests/test_a2a_proxy.py
- [[.from_confidence()]] - code - gateway/security/differential_pii_detector.py
- [[.log_event()_1]] - code - gateway/tests/test_a2a_proxy.py
- [[.scan_prompt()]] - code - gateway/security/differential_pii_detector.py
- [[.scan_tool_result()_1]] - code - gateway/security/differential_pii_detector.py
- [[.test_bare_city_name_not_flagged_but_street_address_is()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_cannot_set_tool_floor_above_prompt_floor()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_cannot_set_tool_floor_below_minimum()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_clean_content_no_hits()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_core_ssn_unioned_when_presidio_misses_it()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_default_config_has_correct_floors()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_dotted_email_caught_in_tool_result()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_email_redacted_in_output()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_init_does_not_construct_bare_analyzer_engine()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_init_wires_explicit_nlp_engine_when_model_present()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_pii_hit_fields()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_plain_email_caught_in_prompt()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_plain_email_caught_in_tool_result()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_presidio_analyze_restricted_to_pii_entities()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_presidio_exception_falls_back_to_regex()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_presidio_result_becomes_pii_hit()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_redact_on_hit_false_preserves_original()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_redacted_content_is_original_when_no_pii()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_regex_fallback_when_model_absent()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_report_has_required_fields()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_scan_produces_report_with_correct_floor_used()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_spaced_email_caught_in_tool_result()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_tool_specific_floor_override()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_unknown_tool_uses_default_floor()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_us_ssn_caught_in_tool_result()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_weak_hit_present_in_tool_result_only()]] - code - gateway/tests/test_differential_pii_detector.py
- [[.test_zero_width_space_injection_caught()]] - code - gateway/tests/test_differential_pii_detector.py
- [[A SendMessage containing PII must have it redacted in what's forwarded     to He]] - rationale - gateway/tests/test_a2a_proxy.py
- [[A filedata Part must not be silently dropped or mis-scanned as text —     it's]] - rationale - gateway/tests/test_a2a_proxy.py
- [[A single PII detection result.]] - rationale - gateway/security/differential_pii_detector.py
- [[A weak-confidence hit (0.75) must appear in tool results but not prompts.]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[A2APolicyEngine_3]] - code - gateway/tests/test_a2a_proxy.py
- [[A2AProxy_1]] - code - gateway/tests/test_a2a_proxy.py
- [[An unparseable request must be rejected through the same     process_inbound_req]] - rationale - gateway/tests/test_a2a_proxy.py
- [[Asymmetric PII detector lower floor for tool results, 0.9 for prompts.      Thi]] - rationale - gateway/security/differential_pii_detector.py
- [[Attempt to initialise Presidio deterministically; else regex.          SECURITY]] - rationale - gateway/security/differential_pii_detector.py
- [[Configuration for DifferentialPIIDetector.      Attributes         tool_result_]] - rationale - gateway/security/differential_pii_detector.py
- [[Core scan normalize adversarial patterns, then run PII recognition.]] - rationale - gateway/security/differential_pii_detector.py
- [[DifferentialPIIConfig_1]] - code - gateway/tests/test_differential_pii_detector.py
- [[DifferentialPIIConfig]] - code - gateway/security/differential_pii_detector.py
- [[DifferentialPIIDetector_1]] - code - gateway/tests/test_differential_pii_detector.py
- [[DifferentialPIIDetector]] - code - gateway/security/differential_pii_detector.py
- [[Email with Unicode dot separators.]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[Email with spaces added to defeat naive regex a l i c e @ e x a m p l e . c o m]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[Exercise the Presidio detection path with an injected fake analyzer.      The re]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[Full scan result for a tool result or prompt.]] - rationale - gateway/security/differential_pii_detector.py
- [[GET .well-knownagent-card.json must pass through with NO authpeer     require]] - rationale - gateway/tests/test_a2a_proxy.py
- [[PII Sanitizer Mitigation (Presidio + custom regex)]] - rationale - docs/security/threat-model.md
- [[PII split with zero-width space.]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[PIIHit]] - code - gateway/security/differential_pii_detector.py
- [[PIIHitSeverity]] - code - gateway/security/differential_pii_detector.py
- [[Pre-1.0 peers send lowercasepath-style method names — Hermes accepts     both f]] - rationale - gateway/tests/test_a2a_proxy.py
- [[Presidio init must be deterministic and must NEVER trigger a runtime     model a]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[Records what it was asked to forward; returns a canned response.]] - rationale - gateway/tests/test_a2a_proxy.py
- [[Regex-based PII detection (Presidio fallback).]] - rationale - gateway/security/differential_pii_detector.py
- [[Relative risk of a detected PII entity.]] - rationale - gateway/security/differential_pii_detector.py
- [[Remove overlapping hits, preferring higher confidence.]] - rationale - gateway/security/differential_pii_detector.py
- [[Replace detected PII tokens with ENTITY_TYPE placeholders.]] - rationale - gateway/security/differential_pii_detector.py
- [[Run PII detection, returning hits at or above floor.]] - rationale - gateway/security/differential_pii_detector.py
- [[Scan a prompt with the standard (higher) confidence floor.          Args]] - rationale - gateway/security/differential_pii_detector.py
- [[Scan a tool result with the lower confidence floor.          Args             t]] - rationale - gateway/security/differential_pii_detector.py
- [[Strip common adversarial encoding tricks, return (normalized, count_removed).]] - rationale - gateway/security/differential_pii_detector.py
- [[TestAdversarialFormattingCaught]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestAsymmetricFloor]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestDeterministicPresidioInit]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestDifferentialPIIDetectorConstruction]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestPerToolConfiguration]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestPresidioPathContract]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestRedaction]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestStandardPIIAlwaysCaught]] - code - gateway/tests/test_differential_pii_detector.py
- [[TestToolResultPIIReport]] - code - gateway/tests/test_differential_pii_detector.py
- [[The default-model auto-download path must never be taken.          If Presidio i]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[Token comparison must not leak timing information — same guarantee as     Hermes]] - rationale - gateway/tests/test_a2a_proxy.py
- [[ToolResultPIIReport]] - code - gateway/security/differential_pii_detector.py
- [[Use Presidio (entity-restricted) unioned with the core regex.          Two guara]] - rationale - gateway/security/differential_pii_detector.py
- [[When the pinned model loads, Presidio is built with an explicit         ``nlp_en]] - rationale - gateway/tests/test_differential_pii_detector.py
- [[_FakeRecognizerResult]] - code - gateway/tests/test_differential_pii_detector.py
- [[_StubAuditStore]] - code - gateway/tests/test_a2a_proxy.py
- [[_StubForwarder]] - code - gateway/tests/test_a2a_proxy.py
- [[_base_policy_engine()]] - code - gateway/tests/test_a2a_proxy.py
- [[_jsonrpc()_1]] - code - gateway/tests/test_a2a_proxy.py
- [[_normalize_adversarial()]] - code - gateway/security/differential_pii_detector.py
- [[default_config()]] - code - gateway/tests/test_differential_pii_detector.py
- [[detector()]] - code - gateway/tests/test_differential_pii_detector.py
- [[differential_pii_detector.py]] - code - gateway/security/differential_pii_detector.py
- [[forwarder()]] - code - gateway/tests/test_a2a_proxy.py
- [[proxy()_1]] - code - gateway/tests/test_a2a_proxy.py
- [[test_a2a_proxy.py]] - code - gateway/tests/test_a2a_proxy.py
- [[test_agent_card_discovery_is_never_policy_gated()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_agent_card_discovery_is_still_audited()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_differential_pii_detector.py]] - code - gateway/tests/test_differential_pii_detector.py
- [[test_extract_text_concatenates_text_parts()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_extract_text_empty_message_returns_empty_string()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_extract_text_flags_binary_parts_without_scanning_them()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_extract_text_handles_missing_parts_key()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_extract_text_skips_non_dict_entries_in_parts()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_parse_jsonrpc_accepts_legacy_path_style_method_alias()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_parse_jsonrpc_extracts_callback_url_from_set_push_config()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_parse_jsonrpc_extracts_method_and_task_id_from_send_message()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_parse_jsonrpc_extracts_task_id_from_get_task()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_parse_jsonrpc_missing_method_field_raises_value_error()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_parse_jsonrpc_non_dict_body_raises_value_error()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_parse_jsonrpc_tolerates_non_dict_params()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_parse_jsonrpc_unknown_method_raises_value_error()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_allowed_peer_low_risk_forwards()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_binary_part_is_forwarded_unscanned_and_flagged()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_denial_is_also_logged_to_audit_store()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_denied_peer_never_reaches_hermes()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_high_risk_method_without_approval_queue_denied()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_logs_to_audit_store_when_configured()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_malformed_body_is_blocked()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_missing_auth_is_blocked_and_never_forwarded()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_pii_in_message_is_redacted_before_forwarding()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_task_ownership_violation_blocked()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_process_inbound_request_unknown_token_is_blocked()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_resolve_peer_id_from_known_bearer_token()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_resolve_peer_id_malformed_header_returns_none()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_resolve_peer_id_missing_header_returns_none()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_resolve_peer_id_unknown_token_returns_none()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_resolve_peer_id_uses_constant_time_comparison()]] - code - gateway/tests/test_a2a_proxy.py
- [[test_resolve_peer_id_whitespace_only_token_returns_none()]] - code - gateway/tests/test_a2a_proxy.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_soc_router_coveragepy
SORT file.name ASC
```

## Connections to other communities
- 34 edges to [[_COMMUNITY_AgentTarget]]
- 2 edges to [[_COMMUNITY__wrap_response()]]
- 1 edge to [[_COMMUNITY_EncryptedStore]]
- 1 edge to [[_COMMUNITY_Daedalus — Concept Illustrator]]
- 1 edge to [[_COMMUNITY_chatbotmain.py]]
- 1 edge to [[_COMMUNITY_EgressFilter]]
- 1 edge to [[_COMMUNITY_hermesskillsi-icloudscriptscalendar.js]]
- 1 edge to [[_COMMUNITY_version_routes.py]]

## Top bridge nodes
- [[DifferentialPIIDetector]] - degree 38, connects to 4 communities
- [[differential_pii_detector.py]] - degree 9, connects to 3 communities
- [[test_a2a_proxy.py]] - degree 50, connects to 1 community
- [[A2AProxy_1]] - degree 27, connects to 1 community
- [[_StubForwarder]] - degree 26, connects to 1 community