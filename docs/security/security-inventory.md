# 🛡️ AgentShroud Security Inventory (v0.8.0)

> **Generated:** 2026-03-07 | **Branch:** `feat/v0.8.0-enforcement-hardening` | **Tests:** 2233/2233 passing
>
> Use this document for manual and automated owner/collaborator testing.

---

## Security Modules (58)

### Inbound Defense (6)
| # | Module | File | Purpose |
|---|--------|------|---------|
| 1 | **PromptGuard** | `prompt_guard.py` | Prompt injection detection — 49 regex patterns, 35+ languages, weighted scoring with block/warn thresholds |
| 2 | **ContextGuard** | `context_guard.py` | Context window poisoning defense — detects conversation hijacking and manipulation |
| 3 | **InputNormalizer** | `input_normalizer.py` | Pre-processes text before scanning — unicode normalization, encoding trick detection |
| 4 | **MultiTurnTracker** | `multi_turn_tracker.py` | Cross-turn manipulation tracking — detects escalation patterns across conversation history |
| 5 | **HeuristicClassifier** | `ml_classifier.py` | Rule-based injection classification (being renamed from ML — no actual ML yet) |
| 6 | **EncodingDetector** | `encoding_detector.py` | Detects encoded/obfuscated payloads — base64, hex, Unicode escapes |

### Outbound Defense (6)
| # | Module | File | Purpose |
|---|--------|------|---------|
| 7 | **OutboundFilter** | `outbound_filter.py` | Blocks sensitive info in bot responses — secrets, internal paths, credentials |
| 8 | **OutputCanary** | `output_canary.py` | Canary token system — plants tokens and detects if they leak in output |
| 9 | **CanaryTripwire** | `canary_tripwire.py` | Scanner bridge for canary detection in pipeline responses |
| 10 | **XmlLeakFilter** | `xml_leak_filter.py` | Prevents XML structures and internal path info from leaking |
| 11 | **PromptProtection** | `prompt_protection.py` | Redacts infrastructure names from output — container names, hostnames, internal IPs |
| 12 | **LogSanitizer** | `log_sanitizer.py` | Strips sensitive data from log output before writing |

### PII & Data Protection (3)
| # | Module | File | Purpose |
|---|--------|------|---------|
| 13 | **ToolResultSanitizer** | `tool_result_sanitizer.py` | PII detection and redaction on tool call results (Presidio-based) |
| 14 | **ToolResultSanitizerEnhanced** | `tool_result_sanitizer_enhanced.py` | Markdown-aware PII sanitization — handles code blocks, tables, links |
| 15 | **ToolResultInjection** | `tool_result_injection.py` | Detects prompt injection hidden inside tool results (second-stage attacks) |

### Access Control (7)
| # | Module | File | Purpose |
|---|--------|------|---------|
| 16 | **RBAC** | `rbac.py` | Role-based access control — owner/admin/user/collaborator role enforcement |
| 17 | **TrustManager** | `trust_manager.py` | Progressive trust scoring — escalate/de-escalate based on agent behavior patterns |
| 18 | **SessionManager** | `session_manager.py` | Per-user session isolation — prevents cross-session data leakage |
| 19 | **SessionSecurity** | `session_security.py` | Secure session management for MCP gateway — token lifecycle, expiry |
| 20 | **FileSandbox** | `file_sandbox.py` | Filesystem access control — restrict file operations by path, owner exemption |
| 21 | **PathIsolation** | `path_isolation.py` | Path isolation enforcement — prevents directory traversal attacks |
| 22 | **AgentIsolation** | `agent_isolation.py` | Per-agent container isolation registry — shared-nothing verification |

### Network & Egress (6)
| # | Module | File | Purpose |
|---|--------|------|---------|
| 23 | **EgressFilter** | `egress_filter.py` | Outbound traffic control — domain allowlist/denylist, per-agent policies |
| 24 | **DnsFilter** | `dns_filter.py` | DNS-level domain filtering — block resolution of prohibited domains |
| 25 | **DnsBlocklist** | `proxy/dns_blocklist.py` | Pi-hole-compatible DNS blocking — 11 blocked domain categories |
| 26 | **DnsForwarder** | `proxy/dns_forwarder.py` | DNS proxy for gateway container — routes queries through filtering |
| 27 | **NetworkValidator** | `network_validator.py` | Container network isolation verification — validates Docker network segmentation |
| 28 | **UrlAnalyzer** | `proxy/url_analyzer.py` | SSRF detection, data exfiltration URL patterns, suspicious redirects |

### MCP/Tool Security (6)
| # | Module | File | Purpose |
|---|--------|------|---------|
| 29 | **McpAudit** | `proxy/mcp_audit.py` | Tool call audit logging — tamper-evident chain of all MCP operations |
| 30 | **McpInspector** | `proxy/mcp_inspector.py` | Tool call inspection — injection detection, PII scanning, sensitive op flagging |
| 31 | **McpPermissions** | `proxy/mcp_permissions.py` | Tool permission enforcement — allowlist/denylist per agent/role |
| 32 | **ToolChainAnalyzer** | `tool_chain_analyzer.py` | Multi-tool chain attack detection — catches multi-step exploitation patterns |
| 33 | **OAuthSecurity** | `oauth_security.py` | OAuth confused-deputy attack prevention for MCP proxy flows |
| 34 | **TokenValidation** | `token_validation.py` | MCP token claim validation — ensures token integrity before passthrough |

### Supply Chain & Browser (2)
| # | Module | File | Purpose |
|---|--------|------|---------|
| 35 | **GitGuard** | `git_guard.py` | Git/supply-chain attack pattern detection — malicious commits, hooks, CI injection |
| 36 | **BrowserSecurity** | `browser_security.py` | Social engineering detection in web content — phishing, credential harvesting |

### Audit & Compliance (4)
| # | Module | File | Purpose |
|---|--------|------|---------|
| 37 | **AuditStore** | `audit_store.py` | Tamper-evident audit chain — cryptographic hash chain of all security events |
| 38 | **AlertDispatcher** | `alert_dispatcher.py` | Security alert dispatch with deduplication and rate limiting |
| 39 | **ApprovalHardening** | `approval_hardening.py` | Deception detection for approval workflows — prevents social engineering of approvers |
| 40 | **ConsentFramework** | `consent_framework.py` | Pre-installation consent for MCP servers — user must approve before install |

### Infrastructure Protection (8)
| # | Module | File | Purpose |
|---|--------|------|---------|
| 41 | **EnvGuard** | `env_guard.py` | Environment variable leakage prevention — blocks env dump attacks |
| 42 | **CredentialInjector** | `credential_injector.py` | Transparent credential injection for outbound requests — no secrets in config |
| 43 | **ResourceGuard** | `resource_guard.py` | Resource exhaustion prevention — CPU, memory, disk abuse detection |
| 44 | **DriftDetector** | `drift_detector.py` | Unauthorized container config change detection — alerts on drift from baseline |
| 45 | **KillswitchMonitor** | `killswitch_monitor.py` | Kill switch functionality verification — ensures emergency stop always works |
| 46 | **MemoryIntegrity** | `memory_integrity.py` | Memory file integrity monitoring — detects unauthorized workspace modifications |
| 47 | **MemoryLifecycle** | `memory_lifecycle.py` | Content threat detection in memory files — injection via persisted data |
| 48 | **SubagentMonitor** | `subagent_monitor.py` | Sub-agent activity monitoring — tracks spawned agent behavior |

### Encryption & Key Management (3)
| # | Module | File | Purpose |
|---|--------|------|---------|
| 49 | **EncryptedStore** | `encrypted_store.py` | AES-256-GCM encryption for data at rest |
| 50 | **KeyVault** | `key_vault.py` | Secure key storage — in-memory vault with access controls |
| 51 | **KeyRotation** | `key_rotation.py` | Credential rotation management — automated rotation scheduling |

### External Integrations (4)
| # | Module | File | Purpose |
|---|--------|------|---------|
| 52 | **ClamavScanner** | `clamav_scanner.py` | ClamAV antivirus integration — file scanning for malware |
| 53 | **FalcoMonitor** | `falco_monitor.py` | Falco runtime security monitoring — container behavior anomaly detection |
| 54 | **WazuhClient** | `wazuh_client.py` | Wazuh SIEM integration — centralized security event management |
| 55 | **TrivyReport** | `trivy_report.py` | Trivy vulnerability scan reporting — container image CVE analysis |

### Orchestration (3)
| # | Module | File | Purpose |
|---|--------|------|---------|
| 56 | **SecurityPipeline** | `proxy/pipeline.py` | Central pipeline — wires all modules together, inbound/outbound flow |
| 57 | **TelegramProxy** | `proxy/telegram_proxy.py` | Telegram API interception — man-in-the-middle for all bot↔Telegram traffic |
| 58 | **WebContentScanner** | `proxy/web_content_scanner.py` | Web content security scanning — analyzes fetched pages for threats |

---

## Security Configuration Files (9)

| # | Config | File | Configures |
|---|--------|------|------------|
| 1 | **RBACConfig** | `rbac_config.py` | Owner ID, user roles, role permissions |
| 2 | **EgressConfig** | `egress_config.py` | Egress filtering enforcement mode, domain lists |
| 3 | **OutboundFilterConfig** | `outbound_filter_config.py` | Outbound info filter patterns, severity levels |
| 4 | **KillswitchConfig** | `killswitch_config.py` | Kill switch monitoring intervals, verification checks |
| 5 | **KeyRotationConfig** | `key_rotation_config.py` | Per-credential rotation policies, schedules |
| 6 | **MemoryConfig** | `memory_config.py` | Memory file integrity monitoring thresholds |
| 7 | **ProgressiveTrustConfig** | `progressive_trust_config.py` | Trust levels (untrusted→verified), escalation rules |
| 8 | **McpConfig** | `proxy/mcp_config.py` | MCP proxy tool allowlists, inspection rules |
| 9 | **WebConfig** | `proxy/web_config.py` | Web proxy security settings, content scanning rules |

---

## Security Architecture Documents (24)

| # | Document | Path | Purpose |
|---|----------|------|---------|
| **Policy & Architecture** ||||
| 1 | Security Policy | `SECURITY.md` | Top-level security policy and disclosure |
| 2 | Security Architecture | `docs/security/SECURITY_ARCHITECTURE.md` | System-wide security architecture overview |
| 3 | Security Architecture (detailed) | `docs/security/security-architecture.md` | Detailed architecture diagrams and flows |
| 4 | Security Plan | `docs/SECURITY_PLAN.md` | Roadmap and implementation plan |
| 5 | Security Policy Final | `docs/security/SECURITY-POLICY-FINAL.md` | Finalized security policy document |
| 6 | Threat Model | `docs/security/threat-model.md` | STRIDE threat model for all attack surfaces |
| 7 | Incident Response | `docs/security/incident-response.md` | Incident response procedures and playbook |
| **Access & Container** ||||
| 8 | Access Control Matrix | `docs/security/access-control-matrix.md` | Per-role permission matrix |
| 9 | Container Policy | `docs/security/container-policy.md` | Docker container security policies |
| 10 | Container Audit | `docs/security/container-security-audit-v0.8.0.md` | v0.8.0 container security audit |
| **Assessments & Audits** ||||
| 11 | Blue Team Assessment | `docs/security/blue-team-assessment-v0.8.0.md` | Initial blue team assessment |
| 12 | Blue Team R2 | `docs/security/blue-team-assessment-v0.8.0-r2.md` | Revision 2 |
| 13 | Blue Team R3 | `docs/security/blue-team-assessment-v0.8.0-r3.md` | Revision 3 |
| 14 | Blue Team Final | `docs/security/blue-team-assessment-v0.8.0-final.md` | Final blue team assessment |
| 15 | Security Verification | `docs/security/SECURITY_VERIFICATION.md` | Verification test results |
| 16 | Verification Results | `docs/security/VERIFICATION_RESULTS.md` | Detailed verification output |
| 17 | Implementation Verification | `docs/security/SECURITY-IMPLEMENTATION-VERIFICATION.md` | Implementation correctness checks |
| **Specialized** ||||
| 18 | Credential Protection | `docs/security/CREDENTIAL-PROTECTION-IMPLEMENTED.md` | Credential protection implementation details |
| 19 | Credential Policy | `docs/security/CREDENTIAL-SECURITY-POLICY.md` | Credential handling policy |
| 20 | Audit Specification | `docs/security/audit-specification.md` | Audit chain format and requirements |
| 21 | Supply Chain | `docs/security/security-supply-chain.md` | Supply chain security controls |
| 22 | Competitive Matrix | `docs/security/competitive-security-matrix.md` | Security comparison vs competitors |
| 23 | Value Proposition | `docs/security/SECURITY_VALUE_PROPOSITION.md` | Security as differentiator |
| 24 | Scripts Reference | `docs/security/SECURITY_SCRIPTS_REFERENCE.md` | Security automation scripts |

---

## Security Test Files (38)

| # | Test File | Covers |
|---|-----------|--------|
| 1 | `test_prompt_guard.py` | PromptGuard patterns, scoring, multilingual |
| 2 | `test_prompt_protection.py` | Infrastructure redaction, dynamic hostnames |
| 3 | `test_context_guard.py` | Context window poisoning |
| 4 | `test_file_sandbox.py` | Filesystem access control |
| 5 | `test_file_sandbox_message_gate.py` | Message-level sandbox enforcement |
| 6 | `test_egress_filter.py` | Domain allowlist/denylist |
| 7 | `test_egress_enforce.py` | Egress enforcement mode |
| 8 | `test_egress_approval.py` | Egress approval workflows |
| 9 | `test_egress_monitor.py` | Egress monitoring |
| 10 | `test_egress_telegram_notify.py` | Telegram notifications for egress blocks |
| 11 | `test_canary.py` | Canary token planting |
| 12 | `test_canary_tripwire.py` | Canary detection scanning |
| 13 | `test_output_canary.py` | Output canary system |
| 14 | `test_git_guard.py` | Git/supply chain patterns |
| 15 | `test_env_guard.py` | Environment variable leakage |
| 16 | `test_metadata_guard.py` | Metadata injection |
| 17 | `test_rbac.py` | Role-based access control |
| 18 | `test_trust_manager.py` | Progressive trust scoring |
| 19 | `test_resource_guard.py` | Resource exhaustion |
| 20 | `test_browser_security.py` | Social engineering detection |
| 21 | `test_oauth_security.py` | OAuth confused-deputy |
| 22 | `test_session_security.py` | Session management |
| 23 | `test_tool_chain_analyzer.py` | Multi-tool chain attacks |
| 24 | `test_tool_injection_scan.py` | Tool result injection |
| 25 | `test_tool_result_pii.py` | Tool result PII sanitization |
| 26 | `test_tool_result_sanitizer_enhanced.py` | Enhanced markdown PII |
| 27 | `test_web_proxy_security.py` | Web proxy security |
| 28 | `test_url_analyzer.py` | URL/SSRF analysis |
| 29 | `test_security.py` | Core security pipeline |
| 30 | `test_security_audit.py` | Audit chain tests |
| 31 | `test_security_audit_advanced.py` | Advanced audit scenarios |
| 32 | `test_security_fixes.py` | Regression tests for fixed vulns |
| 33 | `test_security_hardening.py` | Hardening verification |
| 34 | `test_security_integration.py` | Integration tests |
| 35 | `test_security_toolchain.py` | Toolchain security |
| 36 | `test_e2e.py` | End-to-end security flow |
| 37 | `test_e2e_proxy.py` | E2E proxy pipeline |
| 38 | `test_e2e_watchtower.py` | E2E Watchtower (v0.8.0 features) |

---

## Summary

| Category | Count |
|----------|-------|
| Security modules | **58** |
| Config files | **9** |
| Architecture docs | **24** |
| Test files | **38** |
| Tests passing | **2233/2233** |
| **Total security artifacts** | **129** |

---

## Testing Checklist

### Owner Testing
- [ ] Send message that triggers PromptGuard — should be **allowed** (owner exemption)
- [ ] Send message that triggers GitGuard — should be **allowed** (owner exemption)
- [ ] Verify ContextGuard bypass for owner
- [ ] Verify FileSandbox bypass for owner
- [ ] Verify MultiTurnTracker owner exemption (logs but doesn't block)
- [ ] Confirm all 58 modules load without errors on startup
- [ ] Confirm audit chain records owner-exempted events

### Collaborator Testing
- [ ] Verify MOTD disclosure appears on first message
- [ ] Verify Sonnet model (not Opus) is used
- [ ] Verify `exec` tool is denied
- [ ] Verify `gateway` tool is denied
- [ ] Verify `memory_search`/`memory_get` tools are denied
- [ ] Verify `sessions_spawn`/`sessions_send` tools are denied
- [ ] Verify `cron` tool is denied
- [ ] Verify 1Password skill is NOT available
- [ ] Verify web search/fetch works (allowed tools)
- [ ] Verify file read works within collaborator workspace
- [ ] Verify file write outside collaborator workspace is blocked
- [ ] Send message that triggers PromptGuard — should be **blocked** (not owner)
- [ ] Verify block notification is sent to user with friendly explanation
- [ ] Verify collaborator cannot access owner's MEMORY.md or daily notes
