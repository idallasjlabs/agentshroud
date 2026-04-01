# AgentShroud™ Security Policy

AgentShroud v1.0.0 "Fortress" implements **enforce-by-default** security with 76 defense
modules across 7 layers, protecting against prompt injection, PII exposure, unauthorized
tool access, egress exfiltration, container escape, and privilege escalation.

## Supported Versions

| Version | Status |
|---------|--------|
| v1.0.x  | ✅ Current release — full support |
| v0.9.x  | ⚠️ Critical security fixes only |
| < v0.9  | ❌ Unsupported — upgrade immediately |

## Security Architecture

### Layer 1 — Core Pipeline (P0)
PromptGuard, TrustManager, EgressFilter, PII Sanitizer, Gateway Binding

### Layer 2 — Middleware (P1)
SessionManager, TokenValidator, ConsentFramework, SubagentMonitor, AgentRegistry,
Delegation, SharedMemory, ToolACL, PrivacyPolicy, RBAC, ContextGuard, ContextIntegrity,
EncodingDetector, InputNormalizer, HeuristicClassifier, ApprovalHardening, BrowserSecurity

### Layer 3 — Output Protection
OutboundFilter, OutputCanary, OutputSchema, MultiTurnTracker, LogSanitizer,
MetadataGuard, ToolResultSanitizer, ToolResultInjection, XmlLeakFilter, PromptProtection

### Layer 4 — Tool & Agent Control
ToolACL, ToolChainAnalyzer, ToolResultSanitizer, InstructionEnvelope,
SubagentMonitor, ProgressiveLockdown, KillswitchMonitor

### Layer 5 — Network & Egress
EgressFilter, EgressApproval, EgressMonitor, DNSFilter, NetworkValidator,
WebContentScanner (via BrowserSecurity)

### Layer 6 — File & Memory Integrity
FileSandbox, PathIsolation, DriftDetector, MemoryIntegrity, MemoryLifecycle,
GitGuard, EnvGuard, ConfigIntegrity

### Layer 7 — Infrastructure & Supply Chain
ImageVerifier (cosign/Sigstore), ClamAV Scanner, Trivy Scanner, Falco Monitor,
Wazuh Client, EncryptedStore, KeyVault, KeyRotation, HealthReport,
AlertDispatcher, CanaryTripwire, SOCCorrelation, ScannerIntegration

## Compliance Alignment

- **IEC 62443** — FR3→SL3 (supply chain), FR6→SL3 (integrity), FR7→SL2 (availability)
- **OWASP Top 10 for LLM Applications** — all categories addressed
- **NIST CSF** — Identify, Protect, Detect, Respond, Recover mapped

## Upstream Agent CVE Tracking

AgentShroud maintains a registry of known CVEs in the wrapped AI agent (OpenClaw) and
documents the specific defense layers that mitigate each vulnerability. As of v1.0.0,
all 9 disclosed OpenClaw CVEs (March 2026) are **fully mitigated** by AgentShroud's
defense-in-depth architecture. See the SOC "CVE Intelligence" dashboard for details.

## Monitor Mode Warning

**⚠️ CRITICAL SECURITY NOTICE**

AgentShroud defaults to **enforce mode** for all security modules. Running in monitor
mode (`AGENTSHROUD_MODE=monitor`) disables active protection and should ONLY be used
during initial deployment tuning (1-2 weeks) in non-production environments.

In monitor mode, the following protections are **DISABLED**:
- PII detection and redaction
- Prompt injection blocking
- Tool access control enforcement
- Outbound domain filtering
- File sandbox enforcement

**Never run monitor mode in production with real users.**

## Security Scanning

AgentShroud includes automated security scanning in CI/CD:

- **Semgrep SAST** — 11 custom rules (CWE-78, CWE-22, CWE-798, CWE-918, CWE-502, CWE-89)
- **Gitleaks** — Secret scanning in pre-commit and CI
- **Trivy** — Container image vulnerability scanning
- **pip-audit** — Python dependency vulnerability auditing
- **cosign** — Container image signing and SBOM generation
- **Falco** — Runtime container behavior monitoring
- **ClamAV** — Malware scanning on file operations
- **Wazuh** — Host intrusion detection

## Reporting a Vulnerability

If you discover a security vulnerability in AgentShroud:

1. **GitHub Security Advisories** (preferred): https://github.com/idallasj/agentshroud/security/advisories
2. **Email**: security@agentshroud.ai
3. **Do NOT** create public GitHub issues for security vulnerabilities

### Response Timeline
- **Acknowledgment**: within 48 hours
- **Initial assessment**: within 5 business days
- **Critical fix**: within 7 business days
- **Disclosure coordination**: per reporter preference

## Emergency Response

If security is compromised:
1. Set `AGENTSHROUD_MODE=enforce` immediately
2. Activate kill switch: `scripts/activate-lockdown.sh`
3. Restart the gateway: `asb rebuild`
4. Review audit logs: `GET /soc/v1/egress-log`
5. Update allowlists to close identified gaps

---
*AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)*
*Patent Pending — U.S. Provisional Application No. 64/018,744*
