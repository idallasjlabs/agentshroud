---
title: trivy
type: dependency
tags: [security, scanning, vulnerabilities]
related: [Security Modules/trivy_report.py, Dependencies/All Dependencies, Dependencies/clamav]
status: documented
---

# Trivy

**Source:** Aqua Security
**Installation:** Both containers via `curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh`
**Used by:** `gateway/security/trivy_report.py`, `docker/scripts/security-scan.sh`

## Purpose

Container and file system vulnerability scanner. Trivy scans:
- OS packages for known CVEs
- Application dependencies (Python, Node.js)
- Container images
- Configuration files for misconfigurations

## Gateway Usage

`trivy_report.py` runs Trivy scans programmatically:
- Triggered by the security scheduler
- Results included in health reports
- Critical/high vulnerabilities generate alerts via `alert_dispatcher.py`

## Script Usage

`docker/scripts/security-scan.sh` runs Trivy as part of scheduled security scanning:
```bash
# Example invocation
trivy image --severity HIGH,CRITICAL agentshroud-gateway:latest
trivy fs --severity HIGH,CRITICAL /app
```

## ARM64 Support

Installation script supports both `amd64` and `arm64` architectures. Compatible with Raspberry Pi and Apple Silicon Mac.

## Related Notes

- [[Security Modules/trivy_report.py|trivy_report.py]] — Programmatic Trivy integration
- [[Dependencies/clamav]] — Companion malware scanner
- [[Dependencies/All Dependencies]] — Full dependency list
