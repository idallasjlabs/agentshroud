# Security Policy

## Reporting a Vulnerability

We take security seriously. If you discover a vulnerability in OneClaw, please report it responsibly.

### Preferred: GitHub Security Advisories

1. Go to [Security Advisories](https://github.com/idallasj/oneclaw/security/advisories)
2. Click **"Report a vulnerability"**
3. Provide a detailed description, steps to reproduce, and impact assessment

### Alternative: Email

- **Security contact:** security@secureclaw.dev
- **PGP key:** Available on request

### What to Include

- Description of the vulnerability
- Steps to reproduce
- Affected versions
- Potential impact
- Suggested fix (if any)

## Disclosure Policy

We follow **coordinated disclosure** with a **90-day timeline**:

1. **Day 0:** Report received, acknowledgment sent within 48 hours
2. **Day 1–14:** Triage, reproduce, assess severity (CVSS scoring)
3. **Day 14–60:** Develop and test fix
4. **Day 60–90:** Release fix, notify reporters, publish advisory
5. **Day 90:** Public disclosure (with or without fix, per agreement)

We will credit reporters unless they prefer anonymity.

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0.x   | ✅ Active |
| 0.2.x   | ⚠️ Security fixes only |
| < 0.2   | ❌ End of life |

## Security Features Overview

OneClaw provides 12 security modules (see [README](README.md) for details):

- **PII Sanitizer** — Redacts personal data before it reaches the AI agent
- **Approval Queue** — Human-in-the-loop for sensitive operations
- **Audit Ledger** — Immutable record of all data flows
- **Prompt Guard** — Blocks prompt injection and jailbreak attempts
- **Egress Filter** — Controls outbound network connections
- **Trust Manager** — Cryptographic integrity verification
- **Drift Detector** — Monitors for unauthorized filesystem changes
- **Encrypted Store** — At-rest encryption for secrets
- **SSH Proxy** — Approved, audited SSH access with command allowlists
- **Kill Switch** — Emergency shutdown with credential revocation
- **Agent Isolation** — Seccomp, rootless, read-only rootfs, resource limits
- **Live Dashboard** — Real-time monitoring and alerting

## Known Issues

### CVE-2026-22708 — OpenClaw Upstream

**Severity:** Medium
**Affected:** OpenClaw versions prior to latest patched release
**Impact:** Potential information disclosure through gateway API when authentication is misconfigured
**Mitigation:** OneClaw enforces authentication by default. Ensure `GATEWAY_AUTH_TOKEN` is set and `auth_method` is not `none`.
**Status:** Mitigated in OneClaw via mandatory auth enforcement. Upstream fix pending.

## Security Best Practices

1. **Always set `GATEWAY_AUTH_TOKEN`** — never run with default/empty tokens
2. **Enable all security modules** in production (see `examples/paranoid.env`)
3. **Use read-only rootfs** — prevents agent from modifying its own container
4. **Enable Seccomp profiles** — restricts available system calls
5. **Review the approval queue** — don't auto-approve sensitive actions
6. **Monitor the dashboard** — watch for anomalous activity patterns
7. **Keep OneClaw updated** — use the version manager for security-reviewed upgrades
8. **Rotate credentials** regularly via the encrypted store
