---
type: community
cohesion: 0.04
members: 63
---

# GroupApprovalRouter

**Cohesion:** 0.04 - loosely connected
**Members:** 63 nodes

## Members
- [[._contains_env_access_patterns()]] - code - gateway/security/env_guard.py
- [[._derive_key()]] - code - gateway/security/encrypted_store.py
- [[._looks_like_credential()]] - code - gateway/security/env_guard.py
- [[._record_leakage()]] - code - gateway/security/env_guard.py
- [[.check_command_execution()]] - code - gateway/security/env_guard.py
- [[.check_file_access()]] - code - gateway/security/env_guard.py
- [[.decrypt()]] - code - gateway/security/encrypted_store.py
- [[.decrypt_b64()]] - code - gateway/security/encrypted_store.py
- [[.decrypt_json()]] - code - gateway/security/encrypted_store.py
- [[.decrypt_str()]] - code - gateway/security/encrypted_store.py
- [[.encrypt()]] - code - gateway/security/encrypted_store.py
- [[.encrypt_b64()]] - code - gateway/security/encrypted_store.py
- [[.rotate()]] - code - gateway/security/encrypted_store.py
- [[.scrub_command_output()]] - code - gateway/security/env_guard.py
- [[.test_secure_zero_bytearray()]] - code - gateway/tests/test_security_hardening.py
- [[.test_secure_zero_empty()]] - code - gateway/tests/test_security_hardening.py
- [[Alert Levels]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Best-effort zeroing of key material using ctypes.memset.      Works on bytearray]] - rationale - gateway/security/encrypted_store.py
- [[Check if a value looks like a credential.]] - rationale - gateway/security/env_guard.py
- [[Check if command contains patterns that could access environment.]] - rationale - gateway/security/env_guard.py
- [[Check if command execution should be blocked to prevent environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Check if file access should be blocked to prevent environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Decrypt a base64-encoded blob.]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt an AES-256-GCM encrypted blob.          Args             blob The encr]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt and return as UTF-8 string.]] - rationale - gateway/security/encrypted_store.py
- [[Decrypt and return as parsed JSON dict.]] - rationale - gateway/security/encrypted_store.py
- [[Derive a 256-bit key from master secret using PBKDF2-HMAC-SHA256.]] - rationale - gateway/security/encrypted_store.py
- [[Detected environment variable leakage.]] - rationale - gateway/security/env_guard.py
- [[Encrypt and return as base64-encoded string.]] - rationale - gateway/security/encrypted_store.py
- [[Encrypt data using AES-256-GCM.          Args             data String, bytes,]] - rationale - gateway/security/encrypted_store.py
- [[EnvironmentLeakage]] - code - gateway/security/env_guard.py
- [[Extend AGENTSHROUD_RULES with bot-specific name prefixes.      Called at gateway]] - rationale - gateway/security/falco_monitor.py
- [[Get the global environment guard instance.]] - rationale - gateway/security/env_guard.py
- [[Integration]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Integration with Gateway]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Key OSSEC Config Sections (Inferred)]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Network Enforcement]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Priority Levels_1]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Purpose_178]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Purpose_183]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Re-encrypt blobs with a new master secret.          Args             blobs Lis]] - rationale - gateway/security/encrypted_store.py
- [[Record a detected environment leakage.]] - rationale - gateway/security/env_guard.py
- [[Related Notes_22]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Related Notes_27]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Relationship to Other Security Modules]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[Rules Defined]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[Scrub environment variables and API keys from command output.          Args]] - rationale - gateway/security/env_guard.py
- [[Shell Spawning Exceptions]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[What Wazuh Monitors in AgentShroud]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[_secure_zero()]] - code - gateway/security/encrypted_store.py
- [[alert_dispatcher.py]] - code - gateway/security/alert_dispatcher.py
- [[canary.py]] - code - gateway/security/canary.py
- [[configure_rules()]] - code - gateway/security/falco_monitor.py
- [[encrypted_store.py]] - code - gateway/security/encrypted_store.py
- [[env_guard.py]] - code - gateway/security/env_guard.py
- [[falco-rules]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[falco-rules.yaml]] - document - docs/vault/03 - Configuration/falco-rules.md
- [[falco_monitor.py]] - code - gateway/security/falco_monitor.py
- [[get_env_guard()]] - code - gateway/security/env_guard.py
- [[health_report.py]] - code - gateway/security/health_report.py
- [[wazuh-ossec.conf]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[wazuh-ossec]] - document - docs/vault/03 - Configuration/wazuh-ossec.md
- [[wazuh_client.py]] - code - gateway/security/wazuh_client.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/GroupApprovalRouter
SORT file.name ASC
```

## Connections to other communities
- 22 edges to [[_COMMUNITY_lifespan.py]]
- 15 edges to [[_COMMUNITY_LLMProxy]]
- 8 edges to [[_COMMUNITY_gateway.security.daily_cve_report]]
- 4 edges to [[_COMMUNITY_GSDE&G Skills Reference Guide]]
- 3 edges to [[_COMMUNITY__wrap_response()]]
- 3 edges to [[_COMMUNITY_chatbotmain.py]]
- 3 edges to [[_COMMUNITY_KillSwitchMonitor]]
- 3 edges to [[_COMMUNITY_ConsentFramework]]
- 2 edges to [[_COMMUNITY_SSHProxy]]
- 2 edges to [[_COMMUNITY_wazuh_client.py]]
- 2 edges to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_test_bots_ssh_exec_wrapper.py]]
- 1 edge to [[_COMMUNITY_lvgl_kawaii_face.c]]
- 1 edge to [[_COMMUNITY_Mode A — Single task]]
- 1 edge to [[_COMMUNITY_test_runtime_engines.py]]
- 1 edge to [[_COMMUNITY_URLAnalyzer]]
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]
- 1 edge to [[_COMMUNITY_AsyncMock]]
- 1 edge to [[_COMMUNITY_iCloud Services]]
- 1 edge to [[_COMMUNITY_Phase 3 MITIGATE (Rollback First!)]]
- 1 edge to [[_COMMUNITY_climain.py]]
- 1 edge to [[_COMMUNITY_CollaboratorGreeter]]
- 1 edge to [[_COMMUNITY_SlackSocketClient]]

## Top bridge nodes
- [[falco_monitor.py]] - degree 17, connects to 8 communities
- [[health_report.py]] - degree 18, connects to 7 communities
- [[wazuh_client.py]] - degree 15, connects to 6 communities
- [[env_guard.py]] - degree 10, connects to 6 communities
- [[alert_dispatcher.py]] - degree 10, connects to 5 communities