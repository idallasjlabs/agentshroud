---
title: OpenSCAP
type: dependency
package: openscap-scanner
tags: [security, compliance, scanning, dependencies]
related: [Dependencies/trivy, Dependencies/clamav, Configuration/Dockerfile.gateway, Containers & Services/agentshroud-gateway]
status: documented
---

# OpenSCAP

**Package:** `openscap-scanner` (installed in gateway Dockerfile via apt)
**Tool:** OpenSCAP — Open Security Content Automation Protocol scanner
**Standard:** SCAP (Security Content Automation Protocol) — NIST framework

## Purpose

OpenSCAP performs compliance scanning and vulnerability assessment against standardized security profiles (CIS Benchmarks, DISA STIG, etc.). In AgentShroud, it provides automated compliance posture checking for the gateway container at runtime.

## What It Checks

| Profile Type | Examples |
|-------------|---------|
| **CIS Benchmarks** | Docker/Linux baseline hardening checks |
| **DISA STIG** | Defense security technical implementation guides |
| **CVE Scanning** | Known vulnerability identifiers |
| **Configuration Audit** | File permissions, network settings, service status |

## Installation in Gateway

From `gateway/Dockerfile` (multi-stage build):
```dockerfile
RUN apt-get install -y openscap-scanner
```

Installed alongside ClamAV, Trivy, and 1Password CLI as part of the security tooling layer.

## Key Commands

```bash
# Scan against CIS Docker profile
oscap xccdf eval \
  --profile xccdf_org.ssgproject.content_profile_cis \
  --results /tmp/oscap-results.xml \
  /usr/share/xml/scap/ssg/content/ssg-debian12-ds.xml

# Generate HTML report
oscap xccdf generate report /tmp/oscap-results.xml > /tmp/oscap-report.html
```

## Relationship to Other Security Tools

| Tool | Layer | Focus |
|------|-------|-------|
| **OpenSCAP** | Compliance | SCAP profiles, configuration benchmarks |
| **Trivy** | Image/CVE | Container image vulnerability scanning |
| **ClamAV** | Malware | File-level malware detection |
| **Falco** | Runtime | Live syscall and behavioral monitoring |

## Integration Point

OpenSCAP results are surfaced through `health_report.py` as part of the periodic security posture report. The gateway may run scheduled OpenSCAP scans and expose results via the `/api/health` endpoint.

## Related Notes

- [[Dependencies/trivy]] — Complementary container image scanner
- [[Dependencies/clamav]] — Complementary malware scanner
- [[Configuration/Dockerfile.gateway]] — Where OpenSCAP is installed
- [[Containers & Services/agentshroud-gateway]] — Container where it runs
- [[Security Modules/health_report.py|health_report.py]] — Aggregates scan results
