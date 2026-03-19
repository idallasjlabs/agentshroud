---
title: clamav
type: dependency
tags: [security, malware, scanning]
related: [Security Modules/clamav_scanner.py, Dependencies/All Dependencies, Dependencies/trivy]
status: documented
---

# ClamAV

**Package:** `clamav`, `clamav-daemon`, `clamav-freshclam`
**Installed in:** Both containers via apt
**Used by:** `gateway/security/clamav_scanner.py`

## Purpose

Open-source antivirus and malware detection engine. ClamAV scans:
- Files uploaded by the agent or received via tools
- Content downloaded from external URLs
- Documents and attachments before processing

## Installation

Both containers install ClamAV from apt:
```dockerfile
RUN apt-get install -y clamav clamav-daemon clamav-freshclam clamdscan
```

Virus definitions (`/var/lib/clamav`) are:
- Pre-seeded at image build time via `freshclam --quiet`
- Updated at runtime by the security scheduler (`security-scheduler.sh`)

## Gateway Usage

`clamav_scanner.py` interfaces with the ClamAV daemon:
- Scans file content before processing
- Returns clean/infected verdict
- Infected files are quarantined and operator is notified via `alert_dispatcher.py`

## First Boot

If `freshclam` fails at build time (no internet during build), the virus database is empty. At runtime, `security-scheduler.sh` runs `freshclam` to download definitions.

```
"freshclam: virus DB download deferred to runtime"
```

## Related Notes

- [[Security Modules/clamav_scanner.py|clamav_scanner.py]] — ClamAV integration
- [[Dependencies/trivy]] — Companion vulnerability scanner
- [[Dependencies/All Dependencies]] — Full dependency list
