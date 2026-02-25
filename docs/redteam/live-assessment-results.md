# AgentShroud Red Team Assessment — Live Results

## Test Environment
- **Instance:** agentshroud-marvin-test (Colima, Docker)
- **Version:** v0.6.0 (tag `v0.6.0`, commit `8c4b93d`)
- **Date:** 2026-02-25 00:26 UTC
- **Gateway:** v0.5.0, OpenClaw 2026.2.22-2

## v0.6.0 Baseline Results

### Module Status: 33/33 Active
All 33 security modules operational across 4 tiers:
- P0 (Core): 6 modules — pii_sanitizer, prompt_guard, egress_filter, security_pipeline, trust_manager, approval_queue
- P1 (Middleware): 12 modules — file_sandbox, context_guard, env_guard, git_guard, log_sanitizer, metadata_guard, resource_guard, session_manager, subagent_monitor, token_validator, agent_registry, consent_framework
- P2 (Network): 4 modules — dns_filter, egress_monitor, browser_security, oauth_security
- P3 (Infrastructure): 11 modules — alert_dispatcher, canary, clamav_scanner, drift_detector, encrypted_store, falco_monitor, health_report, key_vault, network_validator, trivy_scanner, wazuh_client

### Deep Integration Test: 36/37 (97%)
| # | Test | Status | Detail |
|---|------|--------|--------|
| 1 | PII: SSN | ✅ PASS | `123-45-6789` → REDACTED |
| 2 | PII: Phone | ✅ PASS | `555-867-5309` → REDACTED |
| 3 | PII: Email | ✅ PASS | `john.doe@example.com` → REDACTED |
| 4 | PII: Credit Card | ✅ PASS | `4111-1111-1111-1111` → REDACTED |
| 5 | PII: Multi-entity | ✅ PASS | `987-65-4321` → REDACTED |
| 6 | Prompt Guard: injection | ✅ PASS | action=BLOCK, patterns=ignore_instructions |
| 7 | Prompt Guard: jailbreak | ✅ PASS | action=BLOCK, patterns=role_reassignment, dan_jailbreak |
| 8 | Prompt Guard: system override | ✅ PASS | action=BLOCK, patterns=new_instructions |
| 9 | Context Guard: system injection | ✅ PASS | 1 attack detected |
| 10 | Context Guard: role switch | ✅ PASS | 1 attack detected |
| 11 | File Sandbox: path traversal | ✅ PASS | 3 paths checked, 2 flagged/blocked |
| 12 | DNS Filter: active | ✅ PASS | DNS filter mode: monitor |
| 13 | Egress Filter: policy loaded | ✅ PASS | EgressPolicy loaded |
| 14 | Env Guard: monitoring | ✅ PASS | 0 environment access attempts |
| 15 | Git Guard: repo scan | ✅ PASS | 0 findings |
| 16 | Log Sanitizer: API key redaction | ✅ PASS | key=[REDACTED-CREDENTIAL] |
| 17 | Metadata Guard: header sanitization | ✅ PASS | Oversized header detected, sanitized |
| 18 | Encrypted Store: AES-256-GCM | ✅ PASS | Round-trip verified |
| 19 | Audit Chain: integrity | ✅ PASS | Chain valid (30 entries) |
| 20 | Drift Detector: baseline | ✅ PASS | Baseline set and verified |
| 21 | Key Vault: ready | ✅ PASS | Initialized |
| 22 | Resource Guard: limits | ✅ PASS | Memory limit check: allowed |
| 23 | Session Security: creation | ✅ PASS | Session created |
| 24 | Token Validator: reject invalid | ✅ PASS | AudienceMismatch raised |
| 25 | Trust Manager: registration | ✅ PASS | Agent registered, trust level 1 |
| 26 | Network Validator: active | ✅ PASS | Active |
| 27 | Alert Dispatcher: write + verify | ✅ PASS | Alert dispatched and verified |
| 28 | ClamAV: live scan | ✅ PASS | rc=0, 0 infected |
| 29 | Trivy: Dockerfile misconfig | ✅ PASS | 27/27 passed |
| 30 | Canary: pipeline verification | ✅ PASS | 4/4 verified (PII, audit, chain, proxy) |
| 31 | Auth: unauthenticated blocked | ✅ PASS | 3/3 blocked |
| 32 | Browser Security | ✅ PASS | Loaded |
| 33 | OAuth Security | ✅ PASS | Loaded |
| 34 | Subagent Monitor | ✅ PASS | Loaded |
| 35 | Consent Framework | ✅ PASS | Loaded |
| 36 | Container Hardening: 5-point | ✅ PASS | non-root, ro-rootfs, no-new-privs, secrets-files, no-setuid |
| 37 | Op-Proxy: credential broker | ❌ FAIL | Timed out (1Password cold start >60s) |

### Container Security Profile: 12/12 (100%)
- Non-root user (UID 1000)
- Read-only rootfs
- No effective capabilities
- No setuid binaries
- Secrets via Docker Secrets
- No new privileges
- Tmpfs for writable paths
- AppArmor/SELinux enforcing

### CIS Docker Benchmark: 12/12 (100%)
All checks PASS per CIS Docker Benchmark v1.6.0

### Unit Tests: 1953 passed, 0 failures

### Identified Gaps (Steve Hay's Assessment)
Despite 100% detection capability, v0.6.0 had:
1. 0% effective enforcement (all core modules in monitor mode)
2. No outbound information filtering
3. No human-in-the-loop approval
4. No per-user session isolation
5. No separation of privilege
6. Credentials in agent container

## v0.7.0 Remediation (In Progress)

### Sprint Status
| Sprint | Feature | Status | New Tests |
|--------|---------|--------|-----------|
| 1 | Enforce-by-Default | ✅ Complete | 11 |
| 2 | Outbound Info Filter | ✅ Complete | 27 |
| 3 | Approval Queue | ✅ Complete | Full suite |
| 4 | Session Isolation | ⏳ In progress | — |
| 5 | Privilege Separation | ✅ Complete | 28 |
| 6 | Credential Isolation | ✅ Complete | 18 |

### Expected v0.7.0 Results
- Effective enforcement: 0% → 100% (core modules)
- Outbound filtering: absent → active (15 regex patterns, 7 categories)
- Approval queue: monitor → enforce (4-tier tool risk classification)
- Session isolation: absent → per-user partitioning
- Privilege separation: absent → immutable security paths
- Credential isolation: agent-accessible → gateway-only
