# Docker Desktop Network Settings — Cisco AnyConnect VPN Compatibility

## Problem

When the Fluence Admin VPN (Cisco AnyConnect, split-tunnel) is connected,
Docker container outbound internet access fails:

- Gateway container → `api.telegram.org` : `[Errno 101] Network is unreachable`
- Docker builds → npm/PyPI registries : `ETIMEDOUT`

This manifests as Telegram proxy 502 errors in the gateway logs:

```
GrammyError: Call to 'setMyCommands' failed! (502: <urlopen error [Errno 101] Network is unreachable>)
```

The AgentShroud internal network (bot ↔ gateway) is unaffected — only
container → internet egress breaks.

---

## Root Cause

### Primary: gVisor networking mode

Docker Desktop defaults to `NetworkType: gvisor`. In gVisor mode, container
traffic flows through a userspace kernel inside Docker Desktop's Linux VM,
then through the VM's virtual network, then through the macOS kernel's
packet filter. When Cisco AnyConnect connects, it loads its `pf` anchor
(`anchor "cisco.anyconnect.vpn"` in `/etc/pf.conf`). These rules disrupt
Docker's NAT translation for the bridge subnets (`172.20.0.0/16`,
`172.21.0.0/16`) — even in split-tunnel mode where Fluence corporate traffic
is the only thing that should go through the VPN.

In `vpnkit-userspace` mode (the fix), VPNKit makes connections directly as a
macOS userspace process. From the macOS network stack's perspective, these
connections originate from the host machine's IP — not from a Docker subnet.
AnyConnect's split-tunnel policy correctly routes macOS process connections
through the physical interface, so Docker container egress works.

### Secondary: transparent HTTPS proxy

`VpnKitTransparentProxy: true` intercepts container HTTPS traffic (ports 80
and 443) and routes it through an additional proxy chain that AnyConnect's
`pf` rules interfere with. Disabling this removes that fragile intermediary.

### Secondary: Python IPv6 fallback (misleading error)

`api.telegram.org` returns both IPv4 and IPv6 addresses. Docker containers
have no IPv6 route, so IPv6 connections fail instantly with `ENETUNREACH`.
Python's `socket.create_connection` raises the last exception — so
`ENETUNREACH` (IPv6) is reported in logs even though the real failure is
IPv4 `ETIMEDOUT`. The `ENETUNREACH` error is a red herring.

---

## Settings Changed

**File:** `~/Library/Group Containers/group.com.docker/settings-store.json`

| Setting | Before | After | Why |
|---------|--------|-------|-----|
| `NetworkType` | `"gvisor"` | `"vpnkit-userspace"` | VPNKit makes connections as a macOS process (host IP), not through the Linux VM (Docker subnet IP) — AnyConnect's pf rules don't block it |
| `VpnKitTransparentProxy` | `true` | `false` | Removes the HTTPS proxy chain that AnyConnect's pf anchor disrupts |
| `ContainersOverrideProxyTransparentPorts` | `"80,443"` | `""` | Clears the intercepted ports; redundant with proxy disabled but prevents auto-reapply |

---

## How to Apply

The settings file is user-owned. Docker Desktop must be **fully quit and
restarted** to pick up changes — a container restart alone is not sufficient.

```bash
# 1. Quit Docker Desktop (all containers will stop)
osascript -e 'quit app "Docker"'

# 2. Wait for full exit (~10 seconds)
sleep 10

# 3. Restart Docker Desktop
open -a Docker

# 4. Wait for Docker to be ready (~30-60 seconds)
# Menu bar whale icon stops animating when ready

# 5. Bring up the AgentShroud stack
docker compose -f docker/docker-compose.yml up -d
```

---

## Verification

```bash
# Gateway logs should show Telegram methods succeeding (all 200)
docker logs agentshroud-gateway --tail 30 | grep -i telegram

# Direct TCP test from inside the gateway container — should connect, not timeout
docker exec agentshroud-gateway python3 -c "
import socket
s = socket.create_connection(('api.telegram.org', 443), timeout=10)
print('Connected OK')
s.close()
"
```

### With VPN connected

Reconnect Cisco AnyConnect, then repeat the same checks. Bot Telegram traffic
should continue flowing without 502 errors. VPNKit's direct connections
appear to AnyConnect as regular macOS process traffic, which split-tunnel
routes through the physical interface.

---

## Network Architecture (unchanged)

```
[ openclaw/bot container ]
        ↓  agentshroud-isolated (172.21.0.0/16) — Docker-internal only
[ agentshroud-gateway container ]
        ↓  VPNKit userspace → macOS physical interface (en0/en1) → internet
[ api.telegram.org / Anthropic API / external services ]
```

The bot has no direct internet path. All egress goes through the gateway.
Only the gateway's egress mechanism changed (vpnkit-userspace instead of
gVisor VM networking).

---

## If It Stops Working After a VPN Reconnect

Check that Docker Desktop hasn't reverted the settings (can happen after a
Docker Desktop update):

```bash
python3 -c "
import json
with open('/Users/ijefferson.admin/Library/Group Containers/group.com.docker/settings-store.json') as f:
    d = json.load(f)
print('NetworkType:', d.get('NetworkType'))
print('VpnKitTransparentProxy:', d.get('VpnKitTransparentProxy'))
"
```

If `NetworkType` reverted to `gvisor` or `VpnKitTransparentProxy` reverted
to `true`, re-run the settings script and restart Docker Desktop.

The permanent fix at the VPN level is to ask Fluence IT to add the Docker
bridge subnets (`172.20.0.0/16`, `172.21.0.0/16`) to the AnyConnect
split-tunnel exclusion list on the VPN server.

---

## Related Files

| File | Relevance |
|------|-----------|
| `docker/docker-compose.yml` | Defines `agentshroud-internal` and `agentshroud-isolated` networks |
| `gateway/proxy/telegram_proxy.py` | Makes outbound HTTPS calls to api.telegram.org |
| `docker/scripts/patch-telegram-sdk.sh` | Routes bot → gateway instead of directly to Telegram |
| `/etc/pf.conf` | macOS packet filter — contains `anchor "cisco.anyconnect.vpn"` |
| `~/Library/Group Containers/group.com.docker/settings-store.json` | Docker Desktop settings (this fix) |
