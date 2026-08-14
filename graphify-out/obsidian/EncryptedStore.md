---
source_file: "gateway/security/encrypted_store.py"
type: "code"
community: "Bot Skill Config"
location: "L58"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Bot_Skill_Config
---

# EncryptedStore

## Connections
- [[.__init__()_75]] - `method` [EXTRACTED]
- [[._derive_key()]] - `method` [EXTRACTED]
- [[._resolve_secret()]] - `method` [EXTRACTED]
- [[.decrypt()]] - `method` [EXTRACTED]
- [[.decrypt_b64()]] - `method` [EXTRACTED]
- [[.decrypt_json()]] - `method` [EXTRACTED]
- [[.decrypt_str()]] - `method` [EXTRACTED]
- [[.encrypt()]] - `method` [EXTRACTED]
- [[.encrypt_b64()]] - `method` [EXTRACTED]
- [[.get_blob_key_id()]] - `method` [EXTRACTED]
- [[.rotate()]] - `calls` [EXTRACTED]
- [[.setup_method()_26]] - `calls` [EXTRACTED]
- [[.store()_2]] - `calls` [EXTRACTED]
- [[.test_custom_key_id()]] - `calls` [EXTRACTED]
- [[.test_encrypt_decrypt_still_works_after_zeroing()]] - `calls` [EXTRACTED]
- [[.test_encrypted_store_constant_time()]] - `calls` [INFERRED]
- [[.test_encrypted_store_error_no_key_leak()]] - `calls` [INFERRED]
- [[.test_env_var_secret()]] - `calls` [EXTRACTED]
- [[.test_file_secret()]] - `calls` [EXTRACTED]
- [[.test_key_rotation_auto_increment()]] - `calls` [EXTRACTED]
- [[.test_key_rotation_with_zeroing()]] - `calls` [EXTRACTED]
- [[.test_no_secret_raises()]] - `calls` [EXTRACTED]
- [[.test_wrong_key_fails()]] - `calls` [EXTRACTED]
- [[.test_wrong_key_fails()_1]] - `calls` [EXTRACTED]
- [[AES-256-GCM encrypted storage with key derivation and rotation support.]] - `rationale_for` [EXTRACTED]
- [[TestAgentIsolation]] - `uses` [INFERRED]
- [[TestAuditTrail_1]] - `uses` [INFERRED]
- [[TestAuth_1]] - `uses` [INFERRED]
- [[TestConcurrency]] - `uses` [INFERRED]
- [[TestContainerSecurity]] - `uses` [INFERRED]
- [[TestContextGuard_1]] - `uses` [INFERRED]
- [[TestCryptography]] - `uses` [INFERRED]
- [[TestDependencySecurity]] - `uses` [INFERRED]
- [[TestDoSPrevention]] - `uses` [INFERRED]
- [[TestDriftDetector]] - `uses` [INFERRED]
- [[TestDriftDetectorHardened]] - `uses` [INFERRED]
- [[TestEgressFilter]] - `uses` [INFERRED]
- [[TestEgressSSRF]] - `uses` [INFERRED]
- [[TestEncryptedStore]] - `uses` [INFERRED]
- [[TestExfiltrationDetection]] - `uses` [INFERRED]
- [[TestFileSandbox]] - `uses` [INFERRED]
- [[TestHTTPSecurity]] - `uses` [INFERRED]
- [[TestInfoLeakage]] - `uses` [INFERRED]
- [[TestLoggingSecurity]] - `uses` [INFERRED]
- [[TestMCPSecurity]] - `uses` [INFERRED]
- [[TestNetworkSecurity]] - `uses` [INFERRED]
- [[TestPIIDetection_1]] - `uses` [INFERRED]
- [[TestPrivilegeEscalation]] - `uses` [INFERRED]
- [[TestPromptGuard]] - `uses` [INFERRED]
- [[TestPromptGuard_1]] - `uses` [INFERRED]
- [[TestPromptGuardEvasion]] - `uses` [INFERRED]
- [[TestResourceProtection]] - `uses` [INFERRED]
- [[TestSecureZero]] - `uses` [INFERRED]
- [[TestSupplyChain_1]] - `uses` [INFERRED]
- [[TestTimingAttacks]] - `uses` [INFERRED]
- [[TestTrustManager]] - `uses` [INFERRED]
- [[TestTrustManagerHardened]] - `uses` [INFERRED]
- [[TestWebSecurity]] - `uses` [INFERRED]
- [[encrypted_store()]] - `calls` [EXTRACTED]
- [[encrypted_store.py]] - `contains` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]
- [[test_security_hardening.py]] - `imports` [EXTRACTED]
- [[test_security_integration.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Bot_Skill_Config