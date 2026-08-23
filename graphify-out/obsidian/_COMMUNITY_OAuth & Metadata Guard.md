---
type: community
cohesion: 0.02
members: 155
---

# OAuth & Metadata Guard

**Cohesion:** 0.02 - loosely connected
**Members:** 155 nodes

## Members
- [[.__init__()_97]] - code - gateway/security/metadata_guard.py
- [[.__init__()_102]] - code - gateway/security/oauth_security.py
- [[.check_for_exif()]] - code - gateway/security/metadata_guard.py
- [[.check_oversized_headers()]] - code - gateway/security/metadata_guard.py
- [[.check_state_reuse()]] - code - gateway/security/oauth_security.py
- [[.create_consent_cookie()]] - code - gateway/security/oauth_security.py
- [[.guard()_6]] - code - gateway/tests/test_security_audit.py
- [[.guard()_5]] - code - gateway/tests/test_security_audit.py
- [[.record_state_used()]] - code - gateway/security/oauth_security.py
- [[.register_known_shared_ids()]] - code - gateway/security/oauth_security.py
- [[.sanitize_filename()]] - code - gateway/security/metadata_guard.py
- [[.sanitize_headers()]] - code - gateway/security/metadata_guard.py
- [[.sanitize_image_metadata()]] - code - gateway/security/metadata_guard.py
- [[.test_agent_isolation_module()]] - code - gateway/tests/test_security_audit.py
- [[.test_agent_registry_module()]] - code - gateway/tests/test_security_audit.py
- [[.test_base64_injection()]] - code - gateway/tests/test_security_audit.py
- [[.test_browser_security_loaded()]] - code - gateway/tests/test_security_audit.py
- [[.test_clamav_binary_not_found()]] - code - gateway/tests/test_security_audit.py
- [[.test_clean_conversation()]] - code - gateway/tests/test_security_audit.py
- [[.test_clean_message_not_blocked()]] - code - gateway/tests/test_security_audit.py
- [[.test_clean_technical_message()]] - code - gateway/tests/test_security_audit.py
- [[.test_consent_framework_loads()]] - code - gateway/tests/test_security_audit.py
- [[.test_context_window_stuffing()]] - code - gateway/tests/test_security_audit.py
- [[.test_conversation_history_manipulation()]] - code - gateway/tests/test_security_audit.py
- [[.test_cookie_custom_max_age_expires_sooner()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_expired_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_tamper_detected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_within_max_age_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_wrong_client_fails()]] - code - gateway/tests/test_oauth_security.py
- [[.test_cookie_wrong_scope_fails()]] - code - gateway/tests/test_oauth_security.py
- [[.test_create_consent_cookie()]] - code - gateway/tests/test_oauth_security.py
- [[.test_dan_jailbreak()]] - code - gateway/tests/test_security_audit.py
- [[.test_different_uri_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_dns_entropy_calculator()]] - code - gateway/tests/test_security_audit.py
- [[.test_dns_low_entropy_legit()]] - code - gateway/tests/test_security_audit.py
- [[.test_egress_monitor_loaded()]] - code - gateway/tests/test_security_audit.py
- [[.test_empty_client_id_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_empty_input()_2]] - code - gateway/tests/test_security_audit.py
- [[.test_empty_state_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_exact_match_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_fake_system_message()]] - code - gateway/tests/test_security_audit.py
- [[.test_http_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_ignore_previous_instructions()]] - code - gateway/tests/test_security_audit.py
- [[.test_indirect_injection_url()]] - code - gateway/tests/test_security_audit.py
- [[.test_instruction_override()]] - code - gateway/tests/test_security_audit.py
- [[.test_json_injection()]] - code - gateway/tests/test_security_audit.py
- [[.test_markdown_heading_injection()]] - code - gateway/tests/test_security_audit.py
- [[.test_metadata_guard_strips_internal_headers()]] - code - gateway/tests/test_security_audit_advanced.py
- [[.test_metadata_oversized_headers()]] - code - gateway/tests/test_security_audit.py
- [[.test_metadata_path_traversal_stripped()]] - code - gateway/tests/test_security_audit.py
- [[.test_metadata_sanitize_filename()]] - code - gateway/tests/test_security_audit.py
- [[.test_multilingual_injection()]] - code - gateway/tests/test_security_audit.py
- [[.test_network_validator_importable()]] - code - gateway/tests/test_security_audit.py
- [[.test_network_validator_init()]] - code - gateway/tests/test_security_audit.py
- [[.test_oauth_confused_deputy()]] - code - gateway/tests/test_security_audit.py
- [[.test_oauth_pkce_violation()]] - code - gateway/tests/test_security_audit.py
- [[.test_oauth_redirect_mismatch()]] - code - gateway/tests/test_security_audit.py
- [[.test_path_traversal_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_pkce_plain_rejected_when_s256_required()]] - code - gateway/tests/test_oauth_security.py
- [[.test_pkce_required_missing_challenge()]] - code - gateway/tests/test_oauth_security.py
- [[.test_pkce_s256_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_pkce_verifier_validation()]] - code - gateway/tests/test_oauth_security.py
- [[.test_prompt_leaking_via_markdown()]] - code - gateway/tests/test_security_audit.py
- [[.test_rapid_fire_messages()]] - code - gateway/tests/test_security_audit.py
- [[.test_reject_empty_token()]] - code - gateway/tests/test_security_audit.py
- [[.test_reject_garbage_token()]] - code - gateway/tests/test_security_audit.py
- [[.test_reject_malformed_jwt()]] - code - gateway/tests/test_security_audit.py
- [[.test_reject_none_algorithm()]] - code - gateway/tests/test_security_audit.py
- [[.test_repeated_injection()]] - code - gateway/tests/test_security_audit.py
- [[.test_role_reassignment()]] - code - gateway/tests/test_security_audit.py
- [[.test_role_switching()]] - code - gateway/tests/test_security_audit.py
- [[.test_security_toolchain_clamav()]] - code - gateway/tests/test_security_audit.py
- [[.test_security_toolchain_falco()]] - code - gateway/tests/test_security_audit.py
- [[.test_security_toolchain_trivy()]] - code - gateway/tests/test_security_audit.py
- [[.test_security_toolchain_wazuh()]] - code - gateway/tests/test_security_audit.py
- [[.test_session_binding()]] - code - gateway/tests/test_security_audit.py
- [[.test_session_different_fingerprints()]] - code - gateway/tests/test_security_audit.py
- [[.test_session_isolation()]] - code - gateway/tests/test_security_audit.py
- [[.test_short_state_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_state_replay_detected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_static_shared_client_id_rejected()]] - code - gateway/tests/test_oauth_security.py
- [[.test_system_prompt_extraction()]] - code - gateway/tests/test_security_audit.py
- [[.test_token_smuggling()]] - code - gateway/tests/test_security_audit.py
- [[.test_unique_client_id_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_valid_state_accepted()]] - code - gateway/tests/test_oauth_security.py
- [[.test_validate_consent_cookie()]] - code - gateway/tests/test_oauth_security.py
- [[.test_xml_injection()]] - code - gateway/tests/test_security_audit.py
- [[.test_xml_tag_injection()]] - code - gateway/tests/test_security_audit.py
- [[.token_validator()]] - code - gateway/tests/test_security_audit.py
- [[.validate_consent_cookie()]] - code - gateway/security/oauth_security.py
- [[.validate_redirect_uri()]] - code - gateway/security/oauth_security.py
- [[.validate_request()]] - code - gateway/security/oauth_security.py
- [[.verify_pkce()]] - code - gateway/security/oauth_security.py
- [[Agent registry should be importable.]] - rationale - gateway/tests/test_security_audit.py
- [[Base64 encoded instruction.]] - rationale - gateway/tests/test_security_audit.py
- [[Check if binary data contains EXIF metadata.]] - rationale - gateway/security/metadata_guard.py
- [[Check if headers exceed size limits.]] - rationale - gateway/security/metadata_guard.py
- [[ConfusedDeputyError]] - code - gateway/security/oauth_security.py
- [[Different fingerprints should create different sessions.]] - rationale - gateway/tests/test_security_audit.py
- [[Different sessions should not share state unsafely.]] - rationale - gateway/tests/test_security_audit.py
- [[Fill context with repeated instructions.]] - rationale - gateway/tests/test_security_audit.py
- [[Guards against metadata channel attacks and information disclosure.]] - rationale - gateway/security/metadata_guard.py
- [[High-entropy domains (potential tunneling).]] - rationale - gateway/tests/test_security_audit.py
- [[Injection in another language.]] - rationale - gateway/tests/test_security_audit.py
- [[Internal infrastructure headers should be stripped.]] - rationale - gateway/tests/test_security_audit_advanced.py
- [[Legit domains have lower entropy.]] - rationale - gateway/tests/test_security_audit.py
- [[Markdown-based injection.]] - rationale - gateway/tests/test_security_audit.py
- [[MetadataGuard]] - code - gateway/security/metadata_guard.py
- [[Normal messages should pass.]] - rationale - gateway/tests/test_security_audit.py
- [[OAuthError]] - code - gateway/security/oauth_security.py
- [[OAuthRequest]] - code - gateway/security/oauth_security.py
- [[OAuthSecurityValidator]] - code - gateway/security/oauth_security.py
- [[PKCEViolation]] - code - gateway/security/oauth_security.py
- [[Rapid messages shouldn't cause errors.]] - rationale - gateway/tests/test_security_audit.py
- [[RedirectMismatch]] - code - gateway/security/oauth_security.py
- [[Reject JWTs with alg=none (classic attack).]] - rationale - gateway/tests/test_security_audit.py
- [[Remove EXIF metadata from image data if present.]] - rationale - gateway/security/metadata_guard.py
- [[Run ClamAV scan and return parsed results.      Args         target Directory]] - rationale - gateway/security/clamav_scanner.py
- [[Same injection multiple times shouldn't bypass.]] - rationale - gateway/tests/test_security_audit.py
- [[Sanitize HTTP headers by removing sensitive information.]] - rationale - gateway/security/metadata_guard.py
- [[Sanitize filename by removing unicode control characters and normalizing.]] - rationale - gateway/security/metadata_guard.py
- [[Session must bind to user identity.]] - rationale - gateway/tests/test_security_audit.py
- [[Technical discussion mentioning 'system' shouldn't trigger.]] - rationale - gateway/tests/test_security_audit.py
- [[Test DNS filtering, SSRF prevention, and egress control.]] - rationale - gateway/tests/test_security_audit.py
- [[Test authentication and authorization enforcement.]] - rationale - gateway/tests/test_security_audit.py
- [[Test container hardening and runtime security.]] - rationale - gateway/tests/test_security_audit.py
- [[Test context manipulation detection.]] - rationale - gateway/tests/test_security_audit.py
- [[Test prompt injection detection with adversarial payloads.]] - rationale - gateway/tests/test_security_audit.py
- [[TestAuth_1]] - code - gateway/tests/test_security_audit.py
- [[TestClientValidation]] - code - gateway/tests/test_oauth_security.py
- [[TestConsentCookieBinding]] - code - gateway/tests/test_oauth_security.py
- [[TestContainerSecurity]] - code - gateway/tests/test_security_audit.py
- [[TestContextGuard_1]] - code - gateway/tests/test_security_audit.py
- [[TestNetworkSecurity]] - code - gateway/tests/test_security_audit.py
- [[TestPKCE]] - code - gateway/tests/test_oauth_security.py
- [[TestPromptGuard]] - code - gateway/tests/test_security_audit.py
- [[TestRedirectURI]] - code - gateway/tests/test_oauth_security.py
- [[TestStateValidation]] - code - gateway/tests/test_oauth_security.py
- [[Token boundary attack.]] - rationale - gateway/tests/test_security_audit.py
- [[URL-based indirect injection.]] - rationale - gateway/tests/test_security_audit.py
- [[gatewaysecuritydns_filter.py (DNSFilterConfig)]] - code - gateway/security/dns_filter.py
- [[gatewaysecuritydrift_detector.py (DriftDetector)]] - code - gateway/security/drift_detector.py
- [[gatewaysecurityencrypted_store.py (EncryptedStore)]] - code - gateway/security/encrypted_store.py
- [[gatewaysecurityfile_sandbox.py (FileSandbox)]] - code - gateway/security/file_sandbox.py
- [[gatewaysecuritykey_vault.py (KeyVault)]] - code - gateway/security/key_vault.py
- [[gatewaysecuritymetadata_guard.py (MetadataGuard)]] - code - gateway/security/metadata_guard.py
- [[gatewaysecuritynetwork_validator.py (NetworkValidator)]] - code - gateway/security/network_validator.py
- [[gatewaysecurityoauth_security.py]] - code - gateway/security/oauth_security.py
- [[gatewaysecurityprompt_guard.py (PromptGuard)]] - code - gateway/security/prompt_guard.py
- [[gatewaysecuritytrust_manager.py (TrustManager)]] - code - gateway/security/trust_manager.py
- [[oauth_security.py]] - code - gateway/security/oauth_security.py
- [[run_clamscan()]] - code - gateway/security/clamav_scanner.py
- [[test_oauth_security.py]] - code - gateway/tests/test_oauth_security.py
- [[test_security_audit.py]] - code - gateway/tests/test_security_audit.py
- [[validator()]] - code - gateway/tests/test_oauth_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OAuth__Metadata_Guard
SORT file.name ASC
```

## Connections to other communities
- 81 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 36 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 17 edges to [[_COMMUNITY_Security Hardening]]
- 17 edges to [[_COMMUNITY_Git Guard (security)]]
- 17 edges to [[_COMMUNITY_Privilege Separation & File Sandbox]]
- 17 edges to [[_COMMUNITY_Resource Guard & Local Model Parity]]
- 12 edges to [[_COMMUNITY_Security Toolchain]]
- 12 edges to [[_COMMUNITY_Key Vault]]
- 12 edges to [[_COMMUNITY_Subagent Monitor]]
- 10 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 9 edges to [[_COMMUNITY_Security Regressions V1 2]]
- 8 edges to [[_COMMUNITY_Browser Security]]
- 7 edges to [[_COMMUNITY_Dns Filter]]
- 7 edges to [[_COMMUNITY_Egress Filter]]
- 6 edges to [[_COMMUNITY_Egress Monitor]]
- 6 edges to [[_COMMUNITY_Metadata Guard]]
- 5 edges to [[_COMMUNITY_Security Audit]]
- 3 edges to [[_COMMUNITY_Daily Cve Report (security)]]
- 2 edges to [[_COMMUNITY_Scanner Integration Coverage]]
- 2 edges to [[_COMMUNITY_Metadata Guard]]
- 2 edges to [[_COMMUNITY_Session Security]]
- 1 edge to [[_COMMUNITY_Ingest API Main & Models]]
- 1 edge to [[_COMMUNITY_Agentshroud.yaml (03 - Configuration)]]
- 1 edge to [[_COMMUNITY_Http Proxy (proxy)]]
- 1 edge to [[_COMMUNITY_Health Report (security)]]
- 1 edge to [[_COMMUNITY_Mfa Guard]]
- 1 edge to [[_COMMUNITY_Security Fixes & SSH Write Endpoint]]

## Top bridge nodes
- [[test_security_audit.py]] - degree 70, connects to 20 communities
- [[TestContainerSecurity]] - degree 45, connects to 16 communities
- [[TestPromptGuard]] - degree 51, connects to 14 communities
- [[TestAuth_1]] - degree 48, connects to 14 communities
- [[TestContextGuard_1]] - degree 46, connects to 14 communities