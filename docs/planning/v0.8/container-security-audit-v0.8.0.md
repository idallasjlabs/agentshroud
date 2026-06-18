# Container Security Audit — AgentShroud v0.8.0

**Date:** 2026-03-05  
**Auditor:** AgentShroud Bot (Claude Code)  
**Methodology:** CIS Docker Benchmark, OWASP Container Security, MITRE ATT&CK for Containers, manual penetration testing  
**Scope:** 50+ attack vectors tested from inside the bot container  

---

## Architecture

```
┌──────────────────────────────────────────────────────────────┐
│  Marvin (Mac Studio)                                         │
│  ┌──────────────────── Colima VM ──────────────────────────┐ │
│  │  iptables DOCKER-USER chain (firewall rules)            │ │
│  │                                                          │ │
│  │  ┌─── agentshroud-isolated (172.21.0.0/16, internal) ──┐│ │
│  │  │                                                      ││ │
│  │  │  Bot (172.21.0.3)                                    ││ │
│  │  │    ├── HTTP_PROXY → gateway:8181 (all egress)        ││ │
│  │  │    ├── DNS: 127.0.0.11 only (Docker internal)        ││ │
│  │  │    ├── No host.docker.internal                       ││ │
│  │  │    └── iptables: blocked from host:22, pihole:53/80  ││ │
│  │  │                                                      ││ │
│  │  │  Gateway (172.21.0.2)                                ││ │
│  │  │    ├── HTTP CONNECT proxy (:8181, domain allowlist)   ││ │
│  │  │    ├── API gateway (:8080, auth required)            ││ │
│  │  │    ├── DNS via pihole (172.21.0.10)                  ││ │
│  │  │    └── Logs all CONNECT tunnels (audit trail)        ││ │
│  │  │                                                      ││ │
│  │  │  Pi-hole (172.21.0.10)                               ││ │
│  │  │    └── DNS sinkhole (blocks malicious domains)       ││ │
│  │  └──────────────────────────────────────────────────────┘│ │
│  │                                                          │ │
│  │  ┌─── agentshroud-internal (172.20.0.0/16) ───────────┐ │ │
│  │  │  Gateway + Pi-hole (dual-homed for internet access)  │ │ │
│  │  └─────────────────────────────────────────────────────┘ │ │
│  └──────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

---

## Findings & Mitigations

### 🔴 C1: SSH Config Bypass (`-F /dev/null`)

**Vector:** The bot's SSH config uses `ProxyCommand /bin/false` to block connections. However, `ssh -F /dev/null` ignores the config file entirely, allowing direct SSH to the host.

**Risk:** Any code execution inside the container could SSH to the host and gain full access to Docker, the repo, and all credentials.

**Mitigation (IMPLEMENTED):**
1. **Removed `extra_hosts: host.docker.internal:host-gateway`** from compose — bot cannot resolve the host IP by name
2. **iptables DOCKER-USER rules** block all TCP port 22 traffic from the bot subnet (172.21.0.0/16) to the host (192.168.5.0/24) and Docker bridge gateway (172.21.0.1)
3. Rules applied via `docker/scripts/colima-firewall.sh`

**Verification:**
```
$ docker exec agentshroud-bot ssh -F /dev/null agentshroud-bot@192.168.5.2 echo test
ssh: connect to host 192.168.5.2 port 22: Network is unreachable
```

**Commit:** `17fc765` (compose), `40ea003` (firewall script)

---

### 🔴 C2: Raw TCP to Host Port 22

**Vector:** Node.js `net.Socket` can connect directly to `host.docker.internal:22` (or by IP). The Docker isolated network does not block outbound connections to the host.

**Risk:** Same as C1 — code could establish raw TCP connections to the host SSH daemon, bypassing all OpenClaw approval controls.

**Mitigation (IMPLEMENTED):**
Same iptables rules as C1. The bot container cannot establish TCP connections to port 22 on any host-reachable IP.

**Verification:**
```
$ docker exec agentshroud-bot node -e "
const s = new (require('net').Socket)();
s.connect(22, '192.168.5.2', () => console.log('CONNECTED'));
s.on('error', (e) => console.log('BLOCKED:', e.code));
"
BLOCKED: ENETUNREACH
```

---

### 🔴 C3: PID1 Environment Readable (`/proc/1/environ`)

**Vector:** `/proc/1/environ` is readable from inside the container and contains all environment variables, including secrets like `ANTHROPIC_OAUTH_TOKEN`, `BRAVE_API_KEY`, and `ICLOUD_APP_PASSWORD`.

**Risk:** Any code execution (including via prompt injection → tool call) can read all secrets from the process environment.

**Mitigation (IMPLEMENTED — pending image rebuild):**
1. **Secrets written to tmpfs files** (`/tmp/secrets/`) after being fetched from 1Password
2. Env vars remain set for OpenClaw startup (SDKs expect them), but are isolated in tmpfs files for audit
3. **Long-term fix:** OpenClaw `_FILE` suffix support would allow removing env vars entirely after startup

**Why env vars can't be fully eliminated yet:** The Anthropic SDK reads `ANTHROPIC_OAUTH_TOKEN` directly from the environment. The process that sets these vars is PID 1, so even if we `unset` them, `/proc/1/environ` retains the original values (Linux kernel behavior). Full elimination requires either:
- SDK support for file-based credentials
- A multi-process architecture where PID 1 never holds secrets (e.g., `exec` into a clean env)

**Commit:** `17fc765` (start-agentshroud.sh patch)

**Defense in depth:** Even if secrets are read, the bot has no direct internet access — all outbound traffic goes through the gateway proxy which enforces a domain allowlist. Exfiltrating secrets requires going through the gateway.

---

### 🟠 H1: Writable `~/.ssh` Directory

**Vector:** The SSH volume is mounted read-write, allowing runtime modification of SSH config, creation of new key files, and changes to `known_hosts`.

**Risk:** Persistent SSH configuration changes that survive container restarts.

**Mitigation (IMPLEMENTED — pending image rebuild):**
1. **SSH volume mounted as `:ro`** in compose — key persists but can't be modified
2. **SSH config written to tmpfs** (`/home/node/.ssh-tmp/`) on startup from image defaults
3. `known_hosts` stored in tmpfs — ephemeral, resets on every restart
4. Init script (`init-openclaw-config.sh`) updated to handle RO volume

**Current state:** Temporarily reverted to writable because the current image still uses the old init script. Will activate RO mount on next image rebuild.

**Commit:** `17fc765` (compose + init script), `40ea003` (temporary revert)

---

### 🟠 H2: Secrets in Environment Variables

**Vector:** `ANTHROPIC_OAUTH_TOKEN`, `BRAVE_API_KEY`, and `ICLOUD_APP_PASSWORD` are stored as plain environment variables. Every child process inherits them, and they appear in `/proc/*/environ` for all processes.

**Risk:** Secret exposure through process environment.

**Mitigation:** Same as C3 — secrets written to tmpfs files. See C3 for full details.

---

### 🟠 H3: `resolv.conf` Leaks DNS Architecture

**Vector:** Docker adds comments to `/etc/resolv.conf` that reveal internal network topology:
```
# ExtServers: [172.21.0.10]
# Based on host file: '/etc/resolv.conf'
```

**Risk:** Information disclosure — reveals pihole IP and network structure.

**Mitigation (IMPLEMENTED — pending image rebuild):**
1. `start-agentshroud.sh` strips Docker-generated comments from `/etc/resolv.conf` on startup
2. Only `nameserver 127.0.0.11` remains (Docker internal resolver)

**Commit:** `17fc765` (start-agentshroud.sh patch)

---

### 🟠 H4: All Internal Container Ports Reachable

**Vector:** The bot can reach all services on the isolated network: gateway API (8080), gateway proxy (8181), pihole DNS (53), pihole web admin (80).

**Risk:** If pihole or gateway has a vulnerability, the bot can exploit it directly. Pihole web admin is particularly risky — it provides DNS configuration access.

**Mitigation (IMPLEMENTED):**
1. **iptables rules block bot → pihole:80** (web admin)
2. **iptables rules block bot → pihole:53** (direct DNS, both TCP and UDP)
3. Bot can only reach **gateway:8080** (API, auth required) and **gateway:8181** (proxy)
4. Gateway acts as the sole intermediary for DNS resolution and internet access
5. Rules applied via `docker/scripts/colima-firewall.sh`

**Accepted risk:** Bot must reach gateway:8080 and gateway:8181 for normal operation. The gateway requires authentication for all sensitive endpoints.

**Verification:**
```
$ docker exec agentshroud-bot curl -sf http://pihole:80/ 
# Times out — blocked by iptables
```

---

### 🟡 M1: `apt` Available (Permissions Blocked)

**Vector:** `apt-get` binary exists but can't run due to permission errors on lock files. `npm` global installs are blocked by the gateway proxy (403). Local npm installs could theoretically work to writable directories.

**Risk:** Limited package installation capability.

**Mitigation (EXISTING):**
1. **`read_only: true`** on the container filesystem — prevents writing to system dirs
2. **npm proxy returns 403** — gateway blocks npm registry traffic
3. **`apt-get` permission denied** — runs as user `node`, not root
4. **`no-new-privileges`** security option prevents privilege escalation
5. **`/tmp` mounted `noexec`** — downloaded binaries can't be executed

**Accepted risk:** Local `npm install` to writable dirs (workspace) could download JavaScript libraries through the proxy, but:
- The proxy domain allowlist would need to permit `registry.npmjs.org` (currently blocked)
- Downloaded files land on `noexec` tmpfs
- No native compilation tools available (no `gcc`, `make`)

---

### 🟡 M2: `perl` and `bash` Available as Interpreters

**Vector:** Perl (from base image) and bash provide scripting environments that could be used for attack tooling without needing to install packages.

**Risk:** Complex attack scripts can be written using built-in interpreters.

**Mitigation (IMPLEMENTED — pending image rebuild):**
1. **Dockerfile updated to remove perl** — `apt-get purge perl-base` after all installs
2. `bash` and `sh` cannot be removed (required for container operation)
3. `node` is required for OpenClaw

**Accepted risk:** `bash`, `sh`, and `node` must remain. An attacker with code execution already has significant capability regardless of available interpreters. The real defense is preventing code execution in the first place (prompt injection guards, approval queue).

**Commit:** `17fc765` (Dockerfile patch)

---

### 🟡 M3: `/proc/1/ns/` Namespace Files Visible

**Vector:** Process namespace IDs are readable at `/proc/1/ns/`. These can be used to enumerate container isolation boundaries.

**Risk:** Low — useful in container escape chains but not exploitable alone. All known namespace-based escapes require additional capabilities (CAP_SYS_ADMIN, CAP_SYS_PTRACE) that are dropped.

**Mitigation (EXISTING):**
1. **ALL capabilities dropped** (`cap_drop: ALL`) — `CapBnd: 0x0`
2. **Seccomp profile active** — blocks dangerous syscalls
3. **AppArmor `docker-default`** — enforces mandatory access control
4. **`no-new-privileges`** — prevents capability escalation
5. **No Docker socket** — can't manipulate container namespaces

**Accepted risk:** Namespace enumeration provides minimal value to an attacker when all escape-enabling capabilities are dropped.

---

## Controls Summary

| Category | Control | Status |
|----------|---------|--------|
| **Network** | No host.docker.internal | ✅ Active |
| **Network** | iptables: bot ✗→ host:22 | ✅ Active |
| **Network** | iptables: bot ✗→ pihole:53/80 | ✅ Active |
| **Network** | All egress via gateway proxy | ✅ Active |
| **Network** | No external DNS resolver | ✅ Active |
| **Network** | Domain allowlist on proxy | ✅ Active |
| **Network** | Tailscale unreachable | ✅ Active |
| **Network** | Cloud metadata unreachable | ✅ Active |
| **Filesystem** | Container root read-only | ✅ Active |
| **Filesystem** | /app read-only | ✅ Active |
| **Filesystem** | /tmp noexec | ✅ Active |
| **Filesystem** | SSH volume read-only | ⏳ Pending rebuild |
| **Secrets** | Docker secrets (file-mounted) | ✅ Active |
| **Secrets** | Env vars to tmpfs files | ⏳ Pending rebuild |
| **Secrets** | resolv.conf comment strip | ⏳ Pending rebuild |
| **Process** | Capabilities: ALL dropped | ✅ Active |
| **Process** | Seccomp: active (level 2) | ✅ Active |
| **Process** | AppArmor: docker-default | ✅ Active |
| **Process** | no-new-privileges | ✅ Active |
| **Process** | ptrace: scope=1 | ✅ Active |
| **Process** | Runs as uid=1000 (node) | ✅ Active |
| **Process** | setuid/setgid bits stripped | ✅ Active |
| **Process** | PID limit: 512 | ✅ Active |
| **Process** | Memory limit: 4GB | ✅ Active |
| **Image** | Base image SHA256 pinned | ✅ Active |
| **Image** | Trivy/1Password GPG verified | ✅ Active |
| **Image** | Perl removed | ⏳ Pending rebuild |
| **Runtime** | OpenClaw approval queue | ✅ Active |
| **Runtime** | Gateway auth on all endpoints | ✅ Active |
| **Runtime** | npm registry blocked (403) | ✅ Active |

---

## Colima VM Networking

**Known issue:** The Colima VM (vz driver on macOS) periodically loses outbound internet routing. The `eth0` default route to `192.168.5.2` loses NAT connectivity.

**Self-healing:** `docker/scripts/colima-firewall.sh` detects this condition and switches the default route to the `col0` interface (native macOS Virtualization.Framework path).

**Recommendation:** Run `colima-firewall.sh` via macOS cron every 5 minutes and on Colima startup (provision script).

---

## Items Pending Image Rebuild

The following fixes are committed but require `docker compose build agentshroud`:
1. SSH volume read-only (H1) — init script writes to tmpfs
2. Perl removal (M2) — `apt-get purge perl-base`
3. Secrets to tmpfs files (C3/H2) — `start-agentshroud.sh` writes to `/tmp/secrets/`
4. resolv.conf comment strip (H3) — sed in startup script

**Rebuild blocked by:** Colima VM internet connectivity (trivy download fails). Fix VM routing first, then rebuild.

---

## Audit Methodology

50+ vectors tested including:
- CIS Docker Benchmark 1.6 (sections 4, 5)
- OWASP Docker Security Cheat Sheet
- MITRE ATT&CK for Containers (TA0001–TA0011)
- CVE-2024-21626 (Leaky Vessels), CVE-2022-0185 (namespace escape)
- Raw socket testing, SSH bypass, proc filesystem enumeration
- Package manager testing, interpreter availability
- Metadata service probing (AWS, GCP)
- Docker socket/capability/namespace testing
