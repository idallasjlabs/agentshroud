# Competitive Security Matrix — AgentShroud vs AI Agent Platforms

**June 2026 | 28 Security Modules Compared** *(updated v1.2.0 — added modules 27–28)*

## Module Comparison

| # | Security Module | AgentShroud | OpenClaw | NanoClaw | Zetherion | HyperAgent | CogniShield | Autonomix | SentinelBot | VoxMind | NeuralNest | AgentForge | MindWeave |
|---|----------------|-----------|----------|----------|-----------|------------|-------------|-----------|-------------|---------|------------|------------|-----------|
| 1 | PII Sanitizer (Presidio + regex) | ✅ | ❌ | ❌ | ⚠️ | ❌ | ⚠️ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 2 | Tamper-Evident Audit (SHA-256 chain) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 3 | Human Approval Queue | ✅ | ❌ | ❌ | ⚠️ | ❌ | ❌ | ❌ | ⚠️ | ❌ | ❌ | ❌ | ❌ |
| 4 | Three-Mode Kill Switch | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 5 | SSH Proxy + Injection Detection | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 6 | Real-Time Security Dashboard | ✅ | ❌ | ❌ | ⚠️ | ❌ | ⚠️ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 7 | AES-256-GCM Encrypted Memory | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 8 | Prompt Injection Defense (11+ patterns) | ✅ | ❌ | ❌ | ⚠️ | ❌ | ⚠️ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 9 | Progressive Trust System (5 levels) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 10 | Egress Domain Filtering | ✅ | ❌ | ⚠️ | ⚠️ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 11 | Container Drift Detection | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 12 | MCP Proxy (per-tool permissions) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 13 | Web Traffic Proxy (SSRF + content scan) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 14 | DNS Tunneling Detection | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 15 | File I/O Sandbox (symlink-safe) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 16 | API Key Vault (zero-exposure) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 17 | Sub-Agent Spawn Monitoring | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 18 | Log Sanitizer (PII/creds in logs) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 19 | Environment Leakage Guard | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 20 | Context Window Poisoning Defense | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 21 | Git Hook Guard | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 22 | Metadata Channel Guard | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 23 | Network Isolation Validator | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 24 | Resource Exhaustion Guard | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 25 | Tool Result Injection Scanning | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 26 | Port Conflict Auto-Detection | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 27 | Cross-Bot Trust Ledger *(v1.2.0)* | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 28 | Differential PII Detector — tool results 0.7-floor *(v1.2.0)* | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

## Security Score (out of 28)

| Platform | Score | Percentage |
|----------|-------|-----------|
| **AgentShroud** | **28/28** | **100%** |
| Zetherion | 4/28 | 14% |
| CogniShield | 3/28 | 11% |
| NanoClaw | 1.5/28 | 5% |
| SentinelBot | 0.5/28 | 2% |
| All others | 0/28 | 0% |

## Container Security Toolchain Comparison

| Tool | AgentShroud | OpenClaw | NanoClaw | Zetherion | All Others |
|------|-----------|----------|----------|-----------|-----------|
| Trivy (CVE scanning) | ✅ Baked in | ❌ | ❌ | ❌ | ❌ |
| ClamAV (malware) | ✅ Baked in | ❌ | ❌ | ❌ | ❌ |
| Falco (runtime) | ✅ Baked in | ❌ | ❌ | ❌ | ❌ |
| Wazuh (SIEM) | ✅ Baked in | ❌ | ❌ | ❌ | ❌ |
| OpenSCAP (compliance) | ✅ Baked in | ❌ | ❌ | ❌ | ❌ |
| seccomp profiles | ✅ | ❌ | ❌ | ⚠️ | ❌ |
| Capability dropping | ✅ | ❌ | ❌ | ⚠️ | ❌ |
| Read-only root FS | ✅ | ❌ | ❌ | ❌ | ❌ |
| Two-network isolation | ✅ | ❌ | ❌ | ❌ | ❌ |

## Key Takeaways

1. **AgentShroud is the only platform with ANY of modules 12-28** — these are novel security capabilities that don't exist anywhere in the AI agent ecosystem
2. **No competitor has a tamper-evident audit trail** — hash chains for audit integrity are unique to AgentShroud
3. **No competitor inspects MCP tool calls** — AgentShroud is the only platform that can see what tools are doing
4. **No competitor scans web content for prompt injection** — CVE-2026-22708 remains unmitigated on all other platforms
5. **Zero competitors have baked-in container security tools** — AgentShroud ships with 5 enterprise security tools by default

## Updated Magic Quadrant Position

| Platform | Features (x) | Security (y) | Quadrant |
|----------|-------------|-------------|----------|
| **AgentShroud** | **9.5** | **10.0** | **Leaders** |
| Zetherion | 7.0 | 3.0 | Visionaries |
| CogniShield | 5.0 | 2.5 | Niche |
| OpenClaw | 9.0 | 1.5 | Challengers |
| NanoClaw | 7.0 | 1.5 | Challengers |
| All others | 3-6 | 0-1 | Niche |

AgentShroud's security score increased from 9.5 to **10.0** with the addition of 8 deep hardening modules (v1.1.x) and further to **10.0+** in v1.2.0 with Cross-Bot Trust Ledger (Module 27) and Differential PII Detector (Module 28) — attack vectors no other platform has even identified, let alone mitigated.
