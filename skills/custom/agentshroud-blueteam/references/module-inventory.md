# AgentShroud Module Inventory

## Original 33 Modules (v0.6.0)

| # | Module | File | Tier |
|---|--------|------|------|
| 1 | PII Sanitizer | gateway/ingest_api/sanitizer.py | P0 |
| 2 | Audit Ledger | gateway/security/audit_ledger.py | P0 |
| 3 | Approval Queue | gateway/approval_queue/enhanced_queue.py | P0 |
| 4 | Kill Switch | scripts/killswitch.sh | P0 |
| 5 | SSH Proxy | gateway/security/ssh_proxy.py | P1 |
| 6 | Dashboard | gateway/web/ | P1 |
| 7 | Encrypted Memory | gateway/security/encrypted_store.py | P1 |
| 8 | Prompt Injection Defense | gateway/security/prompt_guard.py | P0 |
| 9 | Progressive Trust | gateway/security/trust_manager.py | P1 |
| 10 | Egress Filtering | gateway/security/egress_filter.py | P1 |
| 11 | Drift Detection | gateway/security/drift_detector.py | P2 |
| 12 | Trivy | gateway/security/trivy_scanner.py | P2 |
| 13 | ClamAV | gateway/security/clamav_scanner.py | P2 |
| 14 | Falco | gateway/security/falco_monitor.py | P2 |
| 15 | Wazuh | gateway/security/wazuh_monitor.py | P2 |
| 16 | OpenSCAP | gateway/security/openscap_scanner.py | P2 |
| 17 | Container Hardening | gateway/security/container_hardening.py | P2 |
| 18 | Daily Security Report | gateway/security/daily_report.py | P3 |
| 19 | MCP Proxy | gateway/proxy/mcp_proxy.py | P0 |
| 20 | Web Traffic Proxy | gateway/security/web_proxy.py | P1 |
| 21 | DNS Tunneling Detection | gateway/security/dns_filter.py | P1 |
| 22 | Sub-Agent Monitoring | gateway/security/subagent_monitor.py | P1 |
| 23 | File I/O Sandboxing | gateway/security/file_sandbox.py | P0 |
| 24 | API Key Vault | gateway/security/key_vault.py | P1 |
| 25 | Unified Egress Monitoring | gateway/security/egress_monitor.py | P2 |
| 26 | Log Sanitizer | gateway/security/log_sanitizer.py | P2 |
| 27 | Environment Leakage Guard | gateway/security/env_guard.py | P2 |
| 28 | Context Window Poisoning | gateway/security/context_guard.py | P1 |
| 29 | Git Hook Guard | gateway/security/git_guard.py | P2 |
| 30 | Metadata Channel Guard | gateway/security/metadata_guard.py | P1 |
| 31 | Network Isolation Validator | gateway/security/network_validator.py | P2 |
| 32 | Resource Exhaustion Guard | gateway/security/rate_limiter.py | P2 |
| 33 | Tool Result Injection | gateway/security/tool_result_guard.py | P1 |

## v0.7.0 New Modules (Tier 2+3 + Hardening)

| Module | File | Sprint |
|--------|------|--------|
| RBAC Manager | gateway/security/rbac.py | Tier 2 |
| Audit Exporter | gateway/security/audit_export.py | Tier 2 |
| Audit Store | gateway/security/audit_store.py | Tier 2 |
| Kill Switch Monitor | gateway/security/killswitch_monitor.py | Tier 2 |
| Tool Result Sanitizer | gateway/security/tool_result_sanitizer.py | Tier 2 |
| Memory Integrity Monitor | gateway/security/memory_integrity.py | Tier 2 |
| Memory Lifecycle Manager | gateway/security/memory_lifecycle.py | Tier 2 |
| Egress Config (enforce) | gateway/security/egress_config.py | Tier 2 |
| Key Rotation Manager | gateway/security/key_rotation.py | Tier 3 |
| Progressive Trust Config | gateway/security/progressive_trust_config.py | Tier 3 |
| Canary Tripwire | gateway/security/canary_tripwire.py | Hardening |
| Encoding Detector | gateway/security/encoding_detector.py | Hardening |
| Tool Result Injection Scanner | gateway/security/tool_result_injection.py | Hardening |
| XML Leak Filter | gateway/security/xml_leak_filter.py | Hardening |
| Prompt Protection | gateway/security/prompt_protection.py | Hardening |
| Multi-Turn Tracker | gateway/security/multi_turn_tracker.py | Hardening |
| Tool Chain Analyzer | gateway/security/tool_chain_analyzer.py | Hardening |
| Path Isolation Manager | gateway/security/path_isolation.py | Hardening |
| Approval Hardening | gateway/security/approval_hardening.py | Hardening |

## Pipeline Integration Points

- **Inbound (user → agent):** middleware.py `process_request()` → PII sanitizer → prompt guard → RBAC → session isolation → approval queue
- **Tool calls:** MCP proxy `process_tool_call()` → approval queue → tool chain analyzer → execute → tool result sanitizer → tool result injection scanner
- **Outbound (agent → user):** outbound info filter → prompt protection → canary tripwire → encoding detector → XML leak filter → multi-turn tracker → PII sanitizer
- **File ops:** FileSandbox `check_read/write()` → path isolation → memory integrity
- **Egress:** egress filter → DNS filter → egress monitor
