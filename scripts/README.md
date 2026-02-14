# Utility Scripts

Security, maintenance, and audit scripts for SecureClaw.

## Scripts (to be implemented throughout development)

### Security Scripts

**security-audit.sh** (Week 4)
- Container security scan
- Network isolation verification
- Permission audit
- Secrets detection
- Outputs security scorecard (0-100)

**drift-detector.sh** (Week 4)
- Validates current config against `secureclaw.yaml`
- Detects unauthorized changes
- Alerts on security posture degradation

**skill-scanner.sh** (Week 3-4)
- Pre-installation vetting of OpenClaw skills
- Static analysis for suspicious patterns
- Checks against known malicious skills
- Sandboxed test execution

### Maintenance Scripts

**memory-scrubber.py** (Week 2-3)
- Auto-cleanup of MEMORY.md
- Removes PII, expired credentials
- Configurable retention policies
- Scheduled execution

### Development Scripts

**test-network-isolation.sh** (Week 1)
- Verifies LAN blocking
- Tests internet-only access
- Validates Tailscale routing

**test-pii-sanitization.sh** (Week 1)
- End-to-end PII redaction tests
- Test cases for SSN, credit cards, emails, etc.
- Validates audit logging

## Implementation Status

🚧 **Not yet implemented** - Scheduled throughout Weeks 1-4
