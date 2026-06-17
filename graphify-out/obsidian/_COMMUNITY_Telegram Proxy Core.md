---
type: community
cohesion: 0.03
members: 123
---

# Telegram Proxy Core

**Cohesion:** 0.03 - loosely connected
**Members:** 123 nodes

## Members
- [[._bot_is_mentioned()]] - code - gateway/proxy/telegram_proxy.py
- [[._contains_critical_collaborator_leakage()]] - code - gateway/proxy/telegram_proxy.py
- [[._contains_internal_approval_banner()]] - code - gateway/proxy/telegram_proxy.py
- [[._contains_legacy_block_notice()]] - code - gateway/proxy/telegram_proxy.py
- [[._extract_first_egress_target()]] - code - gateway/proxy/telegram_proxy.py
- [[._extract_owner_target()]] - code - gateway/proxy/telegram_proxy.py
- [[._extract_owner_target_resolved()]] - code - gateway/proxy/telegram_proxy.py
- [[._filter_inbound_updates()]] - code - gateway/proxy/telegram_proxy.py
- [[._get_user_projects()]] - code - gateway/proxy/telegram_proxy.py
- [[._is_group_message()]] - code - gateway/proxy/telegram_proxy.py
- [[._is_valid_domain_name()]] - code - gateway/proxy/telegram_proxy.py
- [[._is_within_project_scope()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_allowlist_bypass_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_approval_action_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_approval_queue_probe()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_approval_token_probe()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_archive_exfil_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_collaborator_privacy_query()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_command_enumeration_query()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_cross_tenant_data_probe()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_cross_user_messaging_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_encoded_exfil_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_env_secret_probe()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_execution_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_file_metadata_question()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_file_query()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_filename_reference()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_guardrail_modification_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_hidden_channel_exfil_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_hypothetical_execution_question()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_identity_enumeration_query()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_incremental_exfil_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_internal_network_probe()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_log_access_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_memory_access_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_metadata_endpoint_probe()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_model_status_question()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_model_switch_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_obfuscated_command_probe()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_pairing_or_access_probe()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_path_traversal_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_plugin_discovery_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_policy_bypass_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_safe_collaborator_info_query()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_scheduler_or_autorun_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_secret_value_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_sensitive_path_probe()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_service_control_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_system_prompt_probe()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_tool_payload_text()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_tool_trace_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_unicode_obfuscation_bypass_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_unsafe_scheme_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._looks_like_web_access_request()]] - code - gateway/proxy/telegram_proxy.py
- [[._normalize_command_token()]] - code - gateway/proxy/telegram_proxy.py
- [[._resolve_pending_username_target()]] - code - gateway/proxy/telegram_proxy.py
- [[._strip_json_fence()]] - code - gateway/proxy/telegram_proxy.py
- [[._teams_config()]] - code - gateway/proxy/telegram_proxy.py
- [[._trigger_web_fetch_approval()]] - code - gateway/proxy/telegram_proxy.py
- [[.get_stats()_9]] - code - gateway/proxy/telegram_proxy.py
- [[Allow conceptual securityprocess questions that don't request executiondata ac]] - rationale - gateway/proxy/telegram_proxy.py
- [[Best-effort check to avoid treating local file names as egress domains.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Best-effort guardrail collaborator prompts requesting direct file access.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect chunkedpartial extraction prompts intended to bypass output controls.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator probes asking for direct commandtool inventories.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts asking about other userssessionsidentities.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts asking for raw secrettokenpassword values.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts asking to bypass controls via unicodeinvisible tric]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts asking to bypassdisable approvals or protections.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts asking to decodedeobfuscate and execute commands.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts attempting cross-tenantworkspace data access.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts attempting ownercollaborator identity disclosure.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts attempting path traversal style file access.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts attempting scheduledautomatic task execution.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts attempting securityconfig guardrail changes.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts attempting servicecontainer lifecycle control.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts attempting to approvedeny queued actions.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts probing sensitive filesystem pathssecrets.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts requesting archivebulk export of internal content.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts requesting direct memory contentsearch access.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts requesting direct messaging to other users.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts requesting direct systemaudit log contents.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts requesting environment variablesecret listings.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts requesting external webnetwork fetch behavior.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts requesting pairingaccess bootstrap artifacts.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts requesting plugintool auto-discovery inventory.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts requesting raw tool tracesargumentsresults.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts requesting system promptagent instruction leakage.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts targeting cloud metadata endpoints.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts targeting localinternal network hosts.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts trying to bypass domain allowlistegress policy.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts trying to inspect approval queue internalsmetadata.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts trying to obtaincraft approval callback tokens.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator prompts trying to switch runtime modelprovider configuratio]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator requests to run commands or perform direct execution.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect collaborator requests using disallowed URL schemes.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect conceptual file-purpose questions without direct content requests.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect internal approvalegress banner text that must remain owner-only.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect legacy bracket-style block notices for collaborator normalization.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect patterns that must redact for ALL non-owner chats, including full_access.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect plain-language model status questions for deterministic local reply.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect policy questions about execution behavior (not actual execution asks).]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect rawembedded tool payload text in user input.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect requests to encode sensitiveinternal content for exfiltration.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Detect requests to extract hidden-channel content from sensitiveinternal source]] - rationale - gateway/proxy/telegram_proxy.py
- [[Extract first outbound web target (URL or bare domain) for egress preflight.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Normalize first command token so small obfuscations don't bypass local handlers.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Normalize input text to defeat encoding-based evasion.      Applied before all s]] - rationale - gateway/security/input_normalizer.py
- [[Parse owner command target as numeric id or known collaborator alias.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Proxies Telegram Bot API calls through the security pipeline.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Queue an interactive egress approval when raw web_fetch JSON leaks.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Resolve owner target from pending-request username aliases (e.g., approve ana).]] - rationale - gateway/proxy/telegram_proxy.py
- [[Resolve target by id, static alias, or pending username alias.          Resoluti]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return TeamsConfig from app_state if available.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return True if message originates from a group or supergroup chat.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return True if text has any keyword overlap with the user's project focus_topics]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return True if the bot is @mentioned or a bot_command targets this bot.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Return list of ProjectConfig objects for this user, or empty list.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Scan inbound messages from getUpdates for security threats.]] - rationale - gateway/proxy/telegram_proxy.py
- [[Strip optional markdown json fences around model output.]] - rationale - gateway/proxy/telegram_proxy.py
- [[TelegramAPIProxy]] - code - gateway/proxy/telegram_proxy.py
- [[Validate normalized domain labels to avoid malformed allowlist entries.]] - rationale - gateway/proxy/telegram_proxy.py
- [[normalize_input()]] - code - gateway/security/input_normalizer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Telegram_Proxy_Core
SORT file.name ASC
```

## Connections to other communities
- 45 edges to [[_COMMUNITY_Module Group 60]]
- 31 edges to [[_COMMUNITY_Module Group 87]]
- 25 edges to [[_COMMUNITY_Module Group 160]]
- 17 edges to [[_COMMUNITY_Collaborator Responses]]
- 12 edges to [[_COMMUNITY_Progressive Lockdown]]
- 11 edges to [[_COMMUNITY_Module Group 177]]
- 10 edges to [[_COMMUNITY_Authentication & Rate Limiting]]
- 9 edges to [[_COMMUNITY_Environment Guard & Leak Detection]]
- 7 edges to [[_COMMUNITY_Tool Result Sanitizer]]
- 6 edges to [[_COMMUNITY_Module Group 159]]
- 4 edges to [[_COMMUNITY_Telegram Proxy Inbound Tests]]
- 4 edges to [[_COMMUNITY_Module Group 127]]
- 2 edges to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 2 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 2 edges to [[_COMMUNITY_Module Group 208]]
- 2 edges to [[_COMMUNITY_Telegram Proxy Outbound Tests]]
- 2 edges to [[_COMMUNITY_Module Group 190]]
- 2 edges to [[_COMMUNITY_Tool ACL & RBAC Config]]
- 2 edges to [[_COMMUNITY_Module Group 69]]
- 2 edges to [[_COMMUNITY_Module Group 133]]
- 2 edges to [[_COMMUNITY_Module Group 464]]
- 1 edge to [[_COMMUNITY_Slack Proxy]]
- 1 edge to [[_COMMUNITY_Module Group 358]]
- 1 edge to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 1 edge to [[_COMMUNITY_Module Group 74]]
- 1 edge to [[_COMMUNITY_Telegram Inbound Test Rationale]]
- 1 edge to [[_COMMUNITY_Module Group 308]]
- 1 edge to [[_COMMUNITY_Module Group 260]]
- 1 edge to [[_COMMUNITY_Module Group 445]]
- 1 edge to [[_COMMUNITY_Module Group 248]]
- 1 edge to [[_COMMUNITY_Module Group 235]]
- 1 edge to [[_COMMUNITY_Module Group 249]]
- 1 edge to [[_COMMUNITY_Module Group 225]]
- 1 edge to [[_COMMUNITY_Module Group 309]]
- 1 edge to [[_COMMUNITY_Module Group 234]]
- 1 edge to [[_COMMUNITY_Module Group 217]]
- 1 edge to [[_COMMUNITY_Module Group 187]]
- 1 edge to [[_COMMUNITY_Telegram Outbound Test Rationale]]
- 1 edge to [[_COMMUNITY_Module Group 287]]
- 1 edge to [[_COMMUNITY_Module Group 446]]
- 1 edge to [[_COMMUNITY_Module Group 339]]
- 1 edge to [[_COMMUNITY_Module Group 472]]
- 1 edge to [[_COMMUNITY_Module Group 140]]
- 1 edge to [[_COMMUNITY_Module Group 338]]
- 1 edge to [[_COMMUNITY_SOC Router & Correlation]]
- 1 edge to [[_COMMUNITY_Gateway Config & Lifespan]]
- 1 edge to [[_COMMUNITY_Context Guard & Integrity]]
- 1 edge to [[_COMMUNITY_Module Group 76]]

## Top bridge nodes
- [[TelegramAPIProxy]] - degree 224, connects to 40 communities
- [[normalize_input()]] - degree 79, connects to 10 communities
- [[._filter_inbound_updates()]] - degree 82, connects to 7 communities
- [[._trigger_web_fetch_approval()]] - degree 8, connects to 1 community
- [[._contains_critical_collaborator_leakage()]] - degree 4, connects to 1 community