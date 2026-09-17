---
source_file: "gateway/security/encrypted_store.py"
type: "code"
community: "Encrypted Store & Drift Detector"
location: "L58"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Encrypted_Store__Drift_Detector
---

# EncryptedStore

## Connections
- [[dot-__init__()_73]] - `method` [EXTRACTED]
- [[dot-_derive_key()]] - `method` [EXTRACTED]
- [[dot-_resolve_secret()]] - `method` [EXTRACTED]
- [[dot-decrypt()]] - `method` [EXTRACTED]
- [[dot-decrypt_b64()]] - `method` [EXTRACTED]
- [[dot-decrypt_json()]] - `method` [EXTRACTED]
- [[dot-decrypt_str()]] - `method` [EXTRACTED]
- [[dot-encrypt()]] - `method` [EXTRACTED]
- [[dot-encrypt_b64()]] - `method` [EXTRACTED]
- [[dot-get_blob_key_id()]] - `method` [EXTRACTED]
- [[dot-rotate()]] - `calls` [EXTRACTED]
- [[dot-setup_method()_11]] - `calls` [EXTRACTED]
- [[dot-store()_1]] - `calls` [EXTRACTED]
- [[dot-test_custom_key_id()]] - `calls` [EXTRACTED]
- [[dot-test_encrypt_decrypt_still_works_after_zeroing()]] - `calls` [EXTRACTED]
- [[dot-test_encrypted_store_constant_time()]] - `calls` [INFERRED]
- [[dot-test_encrypted_store_error_no_key_leak()]] - `calls` [INFERRED]
- [[dot-test_env_var_secret()]] - `calls` [EXTRACTED]
- [[dot-test_file_secret()]] - `calls` [EXTRACTED]
- [[dot-test_key_rotation_auto_increment()]] - `calls` [EXTRACTED]
- [[dot-test_key_rotation_with_zeroing()]] - `calls` [EXTRACTED]
- [[dot-test_no_secret_raises()]] - `calls` [EXTRACTED]
- [[dot-test_wrong_key_fails()]] - `calls` [EXTRACTED]
- [[dot-test_wrong_key_fails()_1]] - `calls` [EXTRACTED]
- [[AES-256-GCM encrypted storage with key derivation and rotation support.]] - `rationale_for` [EXTRACTED]
- [[TestAgentIsolation]] - `uses` [INFERRED]
- [[TestAuditTrail]] - `uses` [INFERRED]
- [[TestAuth]] - `uses` [INFERRED]
- [[TestConcurrency]] - `uses` [INFERRED]
- [[TestContainerSecurity]] - `uses` [INFERRED]
- [[TestContextGuard]] - `uses` [INFERRED]
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
- [[TestSupplyChain]] - `uses` [INFERRED]
- [[TestTimingAttacks]] - `uses` [INFERRED]
- [[TestTrustManager]] - `uses` [INFERRED]
- [[TestTrustManagerHardened]] - `uses` [INFERRED]
- [[TestWebSecurity]] - `uses` [INFERRED]
- [[encrypted_store()]] - `calls` [EXTRACTED]
- [[encrypted_store.py]] - `contains` [EXTRACTED]
- [[lifespan()]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_security_audit.py]] - `imports` [EXTRACTED]
- [[test_security_hardening.py]] - `imports` [EXTRACTED]
- [[test_security_integration.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Encrypted_Store__Drift_Detector