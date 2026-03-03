# Docker Desktop Network Settings — Cisco AnyConnect VPN Compatibility

## Problem

When the Fluence Admin VPN (Cisco AnyConnect, split-tunnel) is connected,
Docker container outbound internet access fails silently:

- Gateway container → `api.telegram.org` : `[Errno 101] Network is unreachable`
- Docker builds → npm/PyPI registries : `ETIMEDOUT`
- Docker containers → `host.docker.internal` : `ETIMEDOUT`

This manifests as Telegram proxy 502 errors in the gateway logs:

```
GrammyError: Call to 'deleteWebhook' failed! (502: <urlopen error [Errno 101] Network is unreachable>)
```

The AgentShroud stack itself (bot ↔ gateway internal Docker network) is
unaffected — only container → internet egress breaks.

---

## Root Cause

Docker Desktop uses **VPNKit** with a **transparent HTTPS proxy** by default
(`VpnKitTransparentProxy: true`, intercepting ports 80 and 443).

When Cisco AnyConnect connects, it loads its `pf` anchor
(`anchor "cisco.anyconnect.vpn"` in `/etc/pf.conf`). These rules interfere
with Docker Desktop's VPNKit userspace proxy chain — the layer responsible
for forwarding container HTTPS traffic to the internet. Even in split-tunnel
mode (where only Fluence corporate traffic goes through the VPN, and all
other traffic uses the physical interface), AnyConnect's `pf` rules disrupt
Docker's NAT translation for the Docker bridge subnets
(`172.20.0.0/16`, `172.21.0.0/16`).

Secondary symptom: Python's `socket.create_connection` tries IPv6 addresses
from `getaddrinfo` before falling back to IPv4. Docker containers have no
IPv6 route, so IPv6 fails instantly with `ENETUNREACH`. Python raises the
last exception seen, so `ENETUNREACH` is reported even though the real
failure is IPv4 `ETIMEDOUT`.

---

## Affected Configuration

**File:** `~/Library/Group Containers/group.com.docker/settings-store.json`

### Settings changed

| Setting | Before | After |
|---------|--------|-------|
| `VpnKitTransparentProxy` | `true` | `false` |
| `ContainersOverrideProxyTransparentPorts` | `"80,443"` | `""` |
| `IPv4Only` | `false` | `true` |

### What each change does

**`VpnKitTransparentProxy: false`**
Disables Docker Desktop's userspace HTTPS interceptor. Without the transparent
proxy, VPNKit makes direct TCP connections on behalf of containers. These
connections originate from the macOS process (`vpnkitd`), not from a proxy
chain — AnyConnect's split-tunnel policy correctly routes them through the
physical interface (en0/en1), not the VPN tunnel.

**`ContainersOverrideProxyTransparentPorts: ""`**
Clears the port list that Docker was transparently intercepting. With the
transparent proxy disabled this is redundant but prevents the setting from
being re-applied by Docker Desktop on update.

**`IPv4Only: true`**
Forces Docker Desktop to configure container networking in IPv4-only mode.
Eliminates the misleading `ENETUNREACH` error from Python's IPv6 fallback
and ensures all container DNS lookups and socket connections use IPv4, which
has the correct routing via the Docker bridge default gateway.

---

## How to Apply

The settings file is user-owned and can be written directly. Docker Desktop
must be restarted to pick up changes.

```bash
# 1. Quit Docker Desktop (stops all containers)
osascript -e 'quit app "Docker"'

# 2. Wait for Docker Desktop to fully exit (~10 seconds)
sleep 10

# 3. Restart Docker Desktop
open -a Docker

# 4. Wait for Docker to be ready
# Watch the menu bar icon until it stops animating (~30-60 seconds)

# 5. Bring up the AgentShroud stack
docker compose -f docker/docker-compose.yml up -d
```

---

## Verification

After the stack is up, verify the gateway can reach Telegram:

```bash
# Should show deleteWebhook, getMe, setMyCommands, getUpdates — all 200
docker logs agentshroud-gateway --tail 30 | grep -i telegram

# Confirm IPv4-only is in effect inside a container
docker exec agentshroud-gateway python3 -c "
import socket
r = socket.getaddrinfo('api.telegram.org', 443)
print([x[0].name for x in r])  # should only show AF_INET
"

# Test direct TCP connectivity (should connect, not ENETUNREACH or ETIMEDOUT)
docker exec agentshroud-gateway python3 -c "
import socket
s = socket.create_connection(('api.telegram.org', 443), timeout=10)
print('Connected OK')
s.close()
"
```

### With VPN connected

Reconnect Cisco AnyConnect, then repeat the same checks. Bot Telegram traffic
should continue flowing through the gateway without 502 errors because VPNKit
now makes direct connections that AnyConnect's split-tunnel policy routes
through the physical interface, not the VPN tunnel.

---

## Network Architecture (unchanged)

```
[ openclaw/bot container ]
        ↓ (agentshroud-isolated: 172.21.0.0/16 — internal Docker only)
[ agentshroud-gateway container ]
        ↓ (VPNKit direct TCP — macOS physical interface → internet)
[ api.telegram.org / Anthropic API / external services ]
```

The bot container has no direct internet path. All egress goes through the
gateway. This architecture is unchanged — only the gateway's own internet
egress mechanism changed (direct VPNKit TCP instead of transparent proxy).

---

## If It Stops Working After a VPN Reconnect

AnyConnect occasionally flushes and reloads its `pf` anchor on reconnect.
With `VpnKitTransparentProxy: false`, this should no longer affect Docker.
If 502 errors return:

1. Check if Docker Desktop was updated (a Docker update may reset settings):
   ```bash
   python3 -c "
   import json
   with open('/Users/ijefferson.admin/Library/Group Containers/group.com.docker/settings-store.json') as f:
       d = json.load(f)
   print('TransparentProxy:', d.get('VpnKitTransparentProxy'))
   print('IPv4Only:', d.get('IPv4Only'))
   "
   ```
   If `VpnKitTransparentProxy` reverted to `true`, re-apply the settings and
   restart Docker Desktop.

2. Restart the gateway container (does not require Docker Desktop restart):
   ```bash
   docker compose -f docker/docker-compose.yml restart gateway
   ```

3. If the issue persists, the long-term fix is to ask Fluence IT to add the
   Docker bridge subnets (`172.20.0.0/16`, `172.21.0.0/16`) to the AnyConnect
   split-tunnel exclusion list on the VPN server.

---

## Related Files

| File | Relevance |
|------|-----------|
| `docker/docker-compose.yml` | Defines `agentshroud-internal` and `agentshroud-isolated` networks |
| `gateway/proxy/telegram_proxy.py` | Gateway's Telegram API proxy — makes the outbound HTTPS calls |
| `docker/scripts/patch-telegram-sdk.sh` | Patches grammY SDK to route bot → gateway instead of directly to Telegram |
| `/etc/pf.conf` | macOS packet filter config — contains `anchor "cisco.anyconnect.vpn"` |
| `~/Library/Group Containers/group.com.docker/settings-store.json` | Docker Desktop settings (this fix) |
