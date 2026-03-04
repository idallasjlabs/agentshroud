# ADR-006: Multi-Runtime Container Support

## Status
**Accepted** — December 2025; updated March 2026

## Context

AgentShroud must run across diverse container runtime environments: macOS developer
workstations (M-series and Intel), Linux servers, and Raspberry Pi edge nodes. Each
host has different OS constraints, security postures, and network topologies.

Additionally, Cisco AnyConnect split-tunnel VPN (Fluence Admin VPN) disrupts
container network egress on macOS when the Docker runtime uses a kernel-level network
path (gVisor, Lima usernet). The fix is to route container egress through a userspace
or vmnet bridge that appears to AnyConnect as a regular macOS process connection.

## Decision

Implement **Multi-Runtime Container Support** with automatic runtime detection and a
defined per-host runtime selection policy. Colima is the **primary** macOS development
runtime as of March 2026.

---

## Supported Runtimes

| Runtime | macOS | Linux | RPi | VM? | Key Advantage | Key Drawback |
|---------|-------|-------|-----|-----|---------------|--------------|
| **Colima** | ✅ | ❌ | ❌ | Yes (Lima/VZ) | Lean, Docker CLI-compatible, Apple Silicon native, no licensing | macOS only |
| **Docker Desktop** | ✅ | ✅ | ❌ | Yes (HyperKit/VZ) | Most polished GUI, broadest ecosystem compat | Licensing restrictions, resource overhead |
| **Podman** | ✅ | ✅ | ✅ | Yes (macOS) | Daemonless, rootless, cross-platform | Occasional Docker tooling edge cases |
| **Apple Container System** | ✅ | ❌ | ❌ | No | No VM, native perf, zero-overhead | Not production-ready (roadmap) |
| **Nix Flakes** | ✅ | ✅ | ✅ | No | Fully reproducible, no VM/daemon | Steep learning curve (roadmap) |

---

## Per-Host Runtime Selection

| Host | Runtime | Notes |
|------|---------|-------|
| **Marvin** (M4 Max MacBook Pro) | **Colima** (primary), Docker Desktop (fallback) | VPN networking fix: col0 vmnet route |
| **Trillian** (Intel Mac Mini) | Docker Desktop or Colima | VPN networking fix applies if AnyConnect active |
| **Raspberry Pi nodes** | Podman or Docker Engine (no Desktop) | Linux native, no VPN issue |
| **Linux CI/CD servers** | Podman (preferred) or Docker Engine | Rootless preferred |

---

## Cisco AnyConnect VPN Networking Fix

### Problem

When Cisco AnyConnect split-tunnel VPN is connected, Docker container egress to
the internet fails silently (`ETIMEDOUT`, `ENETUNREACH`). Root cause: AnyConnect
loads a `pf` anchor (`anchor "cisco.anyconnect.vpn"` in `/etc/pf.conf`) that blocks
NAT for Docker bridge subnets (`172.20.0.0/16`, `172.21.0.0/16`) and VM internal
networks that route through the macOS kernel packet filter.

### Fix (Colima)

Colima's Lima VM has two network interfaces:
- `eth0` at `192.168.5.1/24` — Lima usernet (userspace TCP/IP, metric 200, default)
- `col0` at `192.168.64.24/24` — vmnet bridged interface (metric 300)

Lima usernet routes container traffic through a userspace stack that still passes
through the macOS kernel pf, where AnyConnect's anchor blocks it. The vmnet `col0`
interface uses Apple's vmnet framework, which presents VM traffic to the macOS host
as a regular bridged network connection — bypassing AnyConnect's pf subnet rules.

**Fix:** Set `col0` (vmnet) as the primary default route inside the Colima VM by
giving it a lower metric (100) than `eth0` (200).

This is installed as a persistent systemd service inside the Colima VM:

```ini
# /etc/systemd/system/colima-vmnet-route.service
[Unit]
Description=Set col0 (vmnet) as primary default route to bypass AnyConnect pf
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/bin/bash -c 'ip route del default via 192.168.64.1 dev col0 2>/dev/null; ip route add default via 192.168.64.1 dev col0 metric 100'

[Install]
WantedBy=multi-user.target
```

The service is enabled (`systemctl enable colima-vmnet-route.service`) and survives
Colima restarts.

### Fix (Docker Desktop)

See `docker/DOCKER-VPN-NETWORKING.md`. The equivalent fix for Docker Desktop is
switching `NetworkType` from `gvisor` to `vpnkit-userspace` in
`~/Library/Group Containers/group.com.docker/settings-store.json`.

---

## Runtime Abstraction Layer

The Python gateway runtime abstraction (`gateway/runtime/`) supports all runtimes
via a unified interface:

```python
class ContainerRuntime:
    @abstractmethod
    def create_network(self, name: str, config: NetworkConfig) -> Network

    @abstractmethod
    def deploy_service(self, spec: ServiceSpec) -> Service

    @abstractmethod
    def get_runtime_info(self) -> RuntimeInfo
```

Runtime implementations:
- `gateway/runtime/docker_engine.py` — Docker/Colima
- `gateway/runtime/podman_engine.py` — Podman

Shell-level runtime detection is in `scripts/deploy.sh` (auto-detects Docker,
Podman, or Colima socket).

---

## Colima Initial Setup Procedure

### 1. Pre-cache the Lima disk image

Colima's built-in downloader times out on GitHub redirect resolution when
Cisco AnyConnect is connected. Pre-cache manually:

```bash
URL="https://github.com/abiosoft/colima-core/releases/download/v0.10.1/ubuntu-24.04-minimal-cloudimg-arm64-docker.qcow2"
URL_HASH=$(echo -n "$URL" | shasum -a 256 | cut -d' ' -f1)
CACHE_DIR="$HOME/Library/Caches/lima/download/by-url-sha256/$URL_HASH"
mkdir -p "$CACHE_DIR"

# Resolve the CDN redirect URL first (GitHub TLS times out; CDN does not)
CDN_URL=$(python3 -c "
import urllib.request
req = urllib.request.Request('$URL', method='HEAD')
resp = urllib.request.build_opener().open(req, timeout=20)
print(resp.url)
")

curl --max-time 600 -o "$CACHE_DIR/data" "$CDN_URL"
```

### 2. Start Colima

```bash
colima start --cpu 4 --memory 6 --disk 60 --network-address
```

Resource rationale:
- 4 CPUs — parallel gateway + bot builds (spaCy, npm, Playwright)
- 6 GB RAM — gateway (~1.3 GB) + bot (~4 GB) at runtime
- 60 GB disk — two images (~3 GB each) + volumes + build cache
- `--network-address` — gives VM a routable IP on `192.168.64.0/24` (required for col0 vmnet)

### 3. Apply the VPN networking fix

After first start, SSH into the VM and install the route service (see fix above).
This is a one-time step; the service persists across `colima stop`/`colima start`.

### 4. Verify

```bash
colima status
docker context ls          # "colima" should be active (*)
docker info | grep -i proxy  # should show NO proxy
docker pull hello-world    # connectivity test
```

---

## Roadmap

| Runtime | Target | Notes |
|---------|--------|-------|
| Apple Container System | H2 2026 | Awaiting production readiness; no VM overhead |
| Nix Flakes | H2 2026 | Reproducible dev environments via `nix develop` |

---

## Consequences

### Positive

- **Platform flexibility** — same compose files run on any supported runtime
- **VPN compatibility** — vmnet routing fix solves AnyConnect pf anchor blocking
- **Lean development** — Colima uses ~50% less RAM than Docker Desktop
- **No licensing risk** — Colima is MIT-licensed; no Docker Desktop commercial terms
- **Security options** — Podman rootless available for high-security contexts

### Negative

- **macOS-only for Colima** — Linux hosts must use Docker Engine or Podman
- **VPN fix is VM-internal state** — if Colima VM is deleted and recreated, the
  route service must be reinstalled (mitigation: document and automate)
- **Testing matrix** — changes must be validated on all supported runtimes

### Mitigation

- Runtime detection in `scripts/deploy.sh` abstracts CLI differences
- Feature flags for runtime-specific functionality
- `docker/DOCKER-VPN-NETWORKING.md` documents the VPN fix for Docker Desktop
- This ADR documents the equivalent fix for Colima
