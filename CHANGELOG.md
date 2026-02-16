# Changelog

All notable changes to SecureClaw will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] - 2026-02-16

### Summary
First tagged release! Complete security hardening (Phase 3A/3B), SSH capability foundation (Phase 4 start), and comprehensive repository organization.

**Security Score**: 26/26 checks passed (1 expected warning)
**Test Coverage**: Gateway 89%
**Documentation**: 74 files organized into 4 categories

---

### Added

#### Security (Phase 3A)
- **Seccomp profiles** re-enabled with ARM64 support (`clone3`, `membarrier`, `rseq` syscalls)
- **Security verification script** (`docker/scripts/verify-security.sh`) with 13 automated checks
- **OpenSCAP compliance scanner** (`docker/scripts/scan.sh`) with HTML/XML report generation
- **Docker secrets** for gateway password (moved from hardcoded value)
- **mDNS/Bonjour disable** (`OPENCLAW_DISABLE_BONJOUR=1`) to prevent information disclosure
- **Tmpfs mounts** for `/home/node/.local` and `/home/node/.config` (read-only fs prep)

#### Emergency Response (Phase 3B)
- **Kill switch script** (`docker/scripts/killswitch.sh`) with 3 modes:
  - `freeze`: Pause containers for forensic investigation
  - `shutdown`: Graceful stop preserving volumes
  - `disconnect`: Nuclear option with credential revocation and incident reporting

#### SSH Capability (Phase 4 - Start)
- **SSH key generation** (Ed25519) for bot container
- **SSH configuration** (`/home/node/.ssh/config`) for authorized hosts
- **Raspberry Pi access** configured (alias: `pi-dev`, `raspberrypi`)
- **SSH helper script** for remote command execution

#### 1Password Integration
- **Authentication helper** (`/home/node/.ssh/scripts/op-auth.sh`) for non-interactive signin
- **Vault access** from bot commands
- **Documentation** for 1Password CLI usage patterns

#### Documentation
- **Repository organization**: 67 markdown files moved to structured directories
  - `docs/setup/` - 18 setup guides
  - `docs/security/` - 11 security docs
  - `docs/architecture/` - 7 design docs
  - `docs/reference/` - 6 quick reference guides
- **Documentation index** (`docs/README.md`) with categorized links
- **Session notes** separated into `session-notes/` directory
- **Archive** created for historical files (24 files)
- **Repository cleanup summary** (`REPOSITORY_CLEANUP.md`)
- **SSH setup guide** (`docs/setup/OPENCLAW_SSH_SETUP.md`)
- **1Password usage guide** (`docs/setup/1PASSWORD_BOT_USAGE.md`)
- **Raspberry Pi setup guide** (`docs/setup/BOT_DEVELOPMENT_TEAM_RPI_SETUP.md`)
- **Distributed node architecture** (future) (`docs/architecture/DISTRIBUTED_OPENCLAW_NODE_ARCHITECTURE.md`)
- **Security scripts reference** (`docs/security/SECURITY_SCRIPTS_REFERENCE.md`)

---

### Changed

#### Security Hardening
- **Removed NET_RAW capability** from OpenClaw container (Tailscale runs on host)
- **Gateway password** moved from environment variable to Docker secret
- **DM policy** verified as "allowlist" mode (user 8096968754)
- **Seccomp profiles** updated with ARM64-specific syscalls

#### Container Configuration
- **OpenClaw container** now has tmpfs for `.local` and `.config`
- **Docker Compose** updated with security secret mounts
- **Startup script** (`docker/scripts/start-openclaw.sh`) loads gateway password from secret

#### Documentation Structure
- **Main README** completely rewritten for v0.1.0
- **All documentation** references updated to new structure
- **Quick start** section added to README
- **Commit message format** defined for GitHub Flow

---

### Fixed
- **SSH config permissions** issues in container (moved to `openclaw-ssh` volume)
- **1Password authentication** non-interactive flow (TTY error resolved)
- **Arithmetic expansion** in bash scripts (`$((VAR + 1))` instead of `((VAR++))`)

---

### Security

#### Threat Mitigations
- **Seccomp**: Default-deny syscall policy, explicit allowlist
- **Capability dropping**: ALL capabilities dropped, no adds (NET_RAW removed)
- **Secrets management**: No hardcoded credentials, Docker secrets only
- **Information disclosure**: mDNS/Bonjour disabled
- **Emergency response**: Kill switch with credential revocation

#### Verification Results
```
✅ 26/26 security checks passed
⚠️  1 warning (read-only disabled during development - expected)
❌ 0 failed checks
```

#### Security Tools
- `verify-security.sh`: 13-check automated validation
- `scan.sh`: OpenSCAP compliance scanning
- `killswitch.sh`: 3-mode emergency shutdown

---

### Deprecated
- None

---

### Removed
- **NET_RAW capability** from OpenClaw container
- **Hardcoded gateway password** from docker-compose.yml
- **67 markdown files** from root directory (moved to organized structure)

---

### Infrastructure

#### Containers
- **Gateway**: FastAPI, Python 3.13, 512MB RAM, read-only filesystem
- **OpenClaw**: Node.js 22, 4GB RAM, seccomp active, non-root execution

#### Integrations
- **Telegram**: @therealidallasj_bot (allowlist mode)
- **1Password**: CLI integration with auto-authentication
- **SSH**: Remote execution on authorized hosts
- **Tailscale**: VPN for remote access (optional)

#### Storage
- **Docker Desktop**: 104GB allocated
- **Actual usage**: ~18GB
- **Free space**: 75GB on Raspberry Pi target

---

## [Unreleased]

### Phase 4: SSH Capability (In Progress)
- [ ] SSH proxy module with approval integration
- [ ] Command allowlist and audit trail
- [ ] Session timeout and limits
- [ ] SSH access logging

### Phase 5: Live Action Dashboard (Planned)
- [ ] Real-time activity feed (WebSocket)
- [ ] Security alerting
- [ ] React frontend
- [ ] Serve from gateway

### Phase 6: Tailscale + Documentation (Planned)
- [ ] Tailscale serve script
- [ ] IEC 62443 compliance matrix
- [ ] Container security policy
- [ ] CI/CD security checklist

### Phase 7: Hardening Skills (Planned)
- [ ] PromptGuard / input filtering
- [ ] Outbound allowlist
- [ ] Read-only reader agent
- [ ] Drift detection

### Phase 8: Polish & Publish (Planned)
- [ ] Production documentation
- [ ] Example deployments
- [ ] Community support
- [ ] Public release

---

## Version History

- **0.1.0** (2026-02-16): First release - Security foundation complete
- More versions coming soon...

---

## Links

- **Documentation**: [docs/README.md](docs/README.md)
- **Setup Guide**: [docs/setup/OPENCLAW_SETUP.md](docs/setup/OPENCLAW_SETUP.md)
- **Security**: [docs/security/SECURITY_ARCHITECTURE.md](docs/security/SECURITY_ARCHITECTURE.md)
- **Latest Session**: [session-notes/CONTINUE.md](session-notes/CONTINUE.md)

---

**Maintained by**: Claude Sonnet 4.5 + @therealidallasj_bot
**Security**: Defense in depth, zero trust architecture
