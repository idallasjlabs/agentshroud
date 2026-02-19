# Security Supply Chain Analysis

**SecureClaw v0.9.0 — February 2026**

## Overview

"Who watches the watchmen?" SecureClaw's security is only as strong as the tools and libraries it's built on. This document profiles every critical dependency in our security toolchain.

## Verdict Summary

| Component | Maintainer | Security Grade | Known CVEs | Risk |
|-----------|-----------|---------------|------------|------|
| Python 3.11 | PSF | A | Patched regularly | Low |
| FastAPI | Sebastián Ramírez | A | None critical | Low |
| SQLite | D. Richard Hipp | A+ | Most-tested SW in history | Negligible |
| spaCy + Presidio | Microsoft | A | Enterprise-maintained | Low |
| Trivy | Aqua Security / CNCF | A | No self-CVEs | Low |
| ClamAV | Cisco/Talos | A- | CVE-2024-20328 (fixed) | Low |
| Falco | Sysdig / CNCF Graduated | A | No critical CVEs | Low |
| Wazuh | Wazuh Inc. | B+ | **CVE-2025-24016 (CVSS 9.9)** | Medium |
| OpenSCAP | NIST/Red Hat | A | Government-grade | Low |
| cryptography (Python) | PyCA | A | Regular audits | Low |
| Docker Engine | Docker Inc. | A- | Regular CVE patches | Low |
| Podman | Red Hat | A | Rootless by default | Low |

## Detailed Profiles

### Python 3.11 — Runtime
- **Maintainer:** Python Software Foundation
- **Security posture:** Active security team, regular patch releases, CVE response within days
- **Notable:** stdlib `hashlib`, `hmac`, `secrets` modules used for our crypto operations
- **Risk:** Low. Python 3.11 is actively maintained through October 2027
- **Our mitigation:** Pin to specific minor version, run Trivy scans on base image

### FastAPI / Starlette / Uvicorn — Web Framework
- **Maintainer:** Sebastián Ramírez (Tiangolo), Encode
- **Security posture:** No critical CVEs to date, well-reviewed async framework
- **Notable:** Starlette handles request parsing — our attack surface for HTTP
- **Risk:** Low. High adoption (70K+ GitHub stars), active development
- **Our mitigation:** Pin versions, input validation at gateway layer before FastAPI

### SQLite — Approval Queue / Audit Storage
- **Maintainer:** D. Richard Hipp (Hwaci)
- **Security posture:** **Most thoroughly tested software in history** — 100% branch coverage, billions of test cases via TH3 test harness
- **Notable:** Used by every browser, every phone, every OS
- **Risk:** Negligible
- **Our mitigation:** WAL journal mode, parameterized queries (no SQL injection possible)

### spaCy + Presidio — PII Detection
- **Maintainer:** Explosion AI (spaCy), Microsoft (Presidio)
- **Security posture:** Enterprise-grade. Presidio used in Azure Cognitive Services
- **Notable:** NLP models can have adversarial evasion (mitigated by our regex fallback layer)
- **Risk:** Low. Microsoft's security team maintains Presidio
- **Our mitigation:** Dual-layer detection (Presidio + regex patterns), cross-parameter concatenation checks

### Trivy — Container Image Scanning
- **Maintainer:** Aqua Security, CNCF project
- **Security posture:** No self-CVEs reported. Scans for vulnerabilities in others
- **Notable:** Comprehensive: OS packages, language deps, IaC misconfigs, secrets
- **Risk:** Low. Widely adopted in enterprise CI/CD pipelines
- **Our mitigation:** Baked into container build, runs at build time + daily

### ClamAV — Malware Detection
- **Maintainer:** Cisco Talos Intelligence Group
- **Security posture:** 20+ year track record. CVE-2024-20328 (filename handling) patched promptly
- **Notable:** Handles 1M+ daily signature updates. Used by ISPs and enterprises globally
- **Risk:** Low. Cisco's security resources behind it
- **Our mitigation:** Pin to latest stable, auto-update signatures daily, run in read-only container

### Falco — Runtime Security Monitoring
- **Maintainer:** Sysdig, **CNCF Graduated** (highest maturity level)
- **Security posture:** No critical self-CVEs. Kernel-level eBPF/kprobe monitoring
- **Notable:** Detects container escapes, privilege escalation, anomalous syscalls in real-time
- **Risk:** Low. CNCF graduation requires rigorous security audit
- **Our mitigation:** Read-only access, alert-only mode (cannot modify system)

### Wazuh — Host Integrity Monitoring ⚠️
- **Maintainer:** Wazuh Inc.
- **Security posture:** **CVE-2025-24016 (CVSS 9.9)** — RCE via deserialization in Wazuh server API. Patched in v4.9.1 (October 2024). Actively exploited by Mirai botnets in 2025.
- **Notable:** Despite the CVE, Wazuh is HIPAA, PCI-DSS, GDPR compliant and used by 10K+ enterprises
- **Risk:** **Medium**. The CVE was severe but patched. Must ensure we use 4.9.1+
- **Our mitigation:**
  - Pin to v4.9.1+ minimum
  - Wazuh server NOT exposed externally (internal network only)
  - Monitor Wazuh's own security advisories
  - Can operate without Wazuh (graceful degradation — other tools cover most overlap)

### OpenSCAP — Compliance Scanning
- **Maintainer:** NIST, Red Hat
- **Security posture:** Government-grade. Used by DoD, federal agencies
- **Notable:** Implements SCAP (Security Content Automation Protocol) — NIST standard
- **Risk:** Low. Backed by US government security infrastructure
- **Our mitigation:** Read-only scanning, no network access needed

### cryptography (Python) — Encryption Library
- **Maintainer:** Python Cryptographic Authority (PyCA)
- **Security posture:** Regular third-party audits, OpenSSL bindings, Rust backend
- **Notable:** Used for our AES-256-GCM encrypted memory
- **Risk:** Low. One of the most-audited Python packages
- **Our mitigation:** Pin version, use only high-level APIs (Fernet, AESGCM), never roll own crypto

### Docker Engine
- **Maintainer:** Docker Inc.
- **Security posture:** Regular CVE patches, container runtime isolation via namespaces/cgroups
- **Notable:** Container escapes are rare but possible (CVE-2019-5736, CVE-2024-21626)
- **Risk:** Low with proper configuration
- **Our mitigation:** seccomp profiles, cap_drop ALL, read-only root filesystem, no docker socket mount, two-network isolation

### Podman
- **Maintainer:** Red Hat
- **Security posture:** Rootless by default — smaller attack surface than Docker
- **Notable:** No daemon = no docker socket attack vector
- **Risk:** Low. Preferred for security-sensitive deployments
- **Our mitigation:** Supported as alternative runtime, auto-detected by installer

## Recommendations

1. **Pin all dependency versions** in requirements.txt and Dockerfiles
2. **Run Trivy on our own images** at build time (already implemented)
3. **Monitor Wazuh advisories** — only component with a recent critical CVE
4. **Maintain graceful degradation** — if any tool has a zero-day, the system continues without it
5. **Quarterly dependency audit** — review all pinned versions against CVE databases
6. **Consider Wazuh alternative** — OSSEC (Wazuh's upstream) for lighter footprint if Wazuh risks are unacceptable
