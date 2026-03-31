# Colima & Docker Operations Guide — AgentShroud

Reference for container management, build troubleshooting, pruning, and Colima VM
lifecycle on Marvin. Commands are differentiated by account where behavior differs.

---

## 1. Environment Overview

### Accounts on Marvin

| Account | Role | Colima socket | Project name |
|---------|------|---------------|--------------|
| `ijefferson.admin` | **Prod** | `~/.colima/default/docker.sock` | `agentshroud` |
| `agentshroud-bot` | **Dev/bot** | `~/.colima/default/docker.sock` | `agentshroud-bot` |

Both accounts share the same Colima VM and Docker daemon. The `agentshroud-bot` account
uses a separate compose override to avoid port and subnet conflicts with prod.

### Container Names

| Account | Gateway container | Bot container |
|---------|------------------|---------------|
| `ijefferson.admin` (prod) | `agentshroud-gateway` | `agentshroud-bot` |
| `agentshroud-bot` (dev/Marvin) | `agentshroud-marvin-gateway` | `agentshroud-marvin-bot` |

### Port Mappings

| Account | Gateway | Bot | Networks |
|---------|---------|-----|----------|
| `ijefferson.admin` | `127.0.0.1:8080` | `127.0.0.1:18790` | `10.254.110-112.0/24` |
| `agentshroud-bot` | `127.0.0.1:9080` | `127.0.0.1:19789` | `172.20-22.0.0/24` |

### Compose Files

| File | Used by |
|------|---------|
| `docker/docker-compose.yml` | Base — both accounts |
| `docker/docker-compose.agentshroud-bot.marvin.yml` | `agentshroud-bot` on Marvin (port + subnet override) |
| `docker/docker-compose.agentshroud-bot.trillian.yml` | `agentshroud-bot` on Trillian |
| `docker/docker-compose.agentshroud-bot.raspberrypi.yml` | `agentshroud-bot` on Raspberry Pi |

---

## 2. `asb` Helper — Primary Interface

The `asb` script at `scripts/asb` auto-selects the correct compose files and project name
based on `$USER` and `$(hostname -s)`. Always use `asb` instead of raw `docker compose`.

```bash
# From the repo root (both accounts):
./scripts/asb up          # Start all services
./scripts/asb down        # Stop and remove containers (volumes preserved)
./scripts/asb restart     # Stop then start
./scripts/asb logs        # Tail logs (Ctrl+C to stop)
./scripts/asb status      # Show container status
./scripts/asb clean-rebuild   # Full wipe of build cache + rebuild (see §6)

# Run from bot account via SSH:
ssh agentshroud-bot@marvin 'cd ~/Development/agentshroud && ./scripts/asb status'
```

**What `asb` selects per account:**

```
ijefferson.admin  →  docker compose -f docker/docker-compose.yml -p agentshroud
agentshroud-bot   →  docker compose -f docker/docker-compose.yml \
                                    -f docker/docker-compose.agentshroud-bot.marvin.yml \
                                    -p agentshroud-bot
```

---

## 3. Colima VM Lifecycle

### Start (required flags)

```bash
colima start --cpu 4 --memory 6 --disk 60 --network-address
```

> `--network-address` is **required** — enables the `col0` vmnet interface needed for
> the VPN routing fix. Without it, Docker egress fails when Cisco AnyConnect is active.

### Stop / Restart

```bash
colima stop
colima restart
```

### Status & Info

```bash
colima status          # VM running, CPU/memory/disk summary
colima version         # Colima + Lima + Docker versions
colima list            # All Colima profiles
```

### SSH into the VM

```bash
colima ssh             # Interactive shell in Lima VM
colima ssh -- <cmd>    # Run a single command and exit
```

---

## 4. Disk & Resource Monitoring

### Check VM disk usage

```bash
colima ssh -- df -h
colima ssh -- df -h /var/lib/docker    # Docker storage specifically
```

### Check Docker disk usage from host

```bash
docker system df           # Summary: images, containers, volumes, build cache
docker system df -v        # Verbose: per-item breakdown
```

### Check container resource usage (live)

```bash
docker stats                                          # All containers
docker stats agentshroud-gateway agentshroud-bot      # Prod
docker stats agentshroud-marvin-gateway agentshroud-marvin-bot  # Dev
```

---

## 5. Container Management

### Logs

```bash
# Prod (ijefferson.admin):
docker logs -f agentshroud-gateway
docker logs -f agentshroud-bot
docker logs --tail 100 agentshroud-gateway

# Dev (agentshroud-bot):
docker logs -f agentshroud-marvin-gateway
docker logs -f agentshroud-marvin-bot

# Via asb (either account):
./scripts/asb logs
```

### Exec into a container

```bash
# Prod:
docker exec -it agentshroud-gateway bash
docker exec -it agentshroud-bot sh       # bot uses sh (node image)

# Dev:
docker exec -it agentshroud-marvin-gateway bash
docker exec -it agentshroud-marvin-bot sh
```

### Health status

```bash
docker inspect --format='{{.State.Health.Status}}' agentshroud-gateway
docker inspect --format='{{.State.Health.Status}}' agentshroud-bot

# All containers at once:
docker ps --format 'table {{.Names}}\t{{.Status}}'
```

### Restart a single container

```bash
docker restart agentshroud-gateway      # Prod gateway
docker restart agentshroud-marvin-bot   # Dev bot
```

---

## 6. Volume Management

### Named volumes for this project

| Volume | Contents | Safe to delete? |
|--------|----------|----------------|
| `agentshroud_gateway-data` | Gateway state, ledger, approval queue | ✅ Recoverable |
| `agentshroud_clamav-db` | ClamAV virus DB (re-downloaded at start) | ✅ Yes |
| `agentshroud_agentshroud-config` | Bot OpenClaw config, agent bindings | ⚠️ Contains agent state |
| `agentshroud_agentshroud-workspace` | Bot workspace files | ⚠️ Contains work product |
| `agentshroud_agentshroud-ssh` | SSH keys | ❌ Requires re-keying |
| `agentshroud_agentshroud-browsers` | Playwright browser cache (~1.5GB) | ✅ Re-downloaded |
| `agentshroud_openclaw-runtime` | npm global packages (`openclaw`, `bun`) | ✅ Re-seeded |
| `agentshroud_security-reports` | Scan reports | ✅ Regenerated |
| `agentshroud_wazuh-alerts` | Wazuh alert logs | ✅ Disposable |
| `agentshroud_memory-backups` | Bot memory backup snapshots | ⚠️ Loss of memory history |

> Dev account volumes are prefixed `agentshroud-bot_` instead of `agentshroud_`.

### List volumes

```bash
docker volume ls
docker volume ls --filter name=agentshroud    # Prod volumes only
docker volume ls --filter name=agentshroud-bot  # Dev volumes only
```

### Inspect a volume (find its mount path in the VM)

```bash
docker volume inspect agentshroud_gateway-data
```

### Remove specific volumes

```bash
# Only the two that clean-rebuild removes (safe — no persistent user data):
docker volume rm agentshroud_gateway-data agentshroud_clamav-db

# Dev account equivalent:
docker volume rm agentshroud-bot_gateway-data agentshroud-bot_clamav-db
```

---

## 7. Build Troubleshooting

### Symptom: `E: You don't have enough free space in /apt-dl/`

**Cause:** Colima VM disk full from accumulated Docker build layers.

```bash
# Step 1: Check disk usage
colima ssh -- df -h /var/lib/docker

# Step 2: Kill any hung prune process on the host
pkill -f "docker system prune" 2>/dev/null || true
pkill -f "docker builder prune" 2>/dev/null || true

# Step 3: Prune from inside the VM (avoids host-side hangs)
colima ssh -- docker system prune -a -f

# Step 4: Retry build
./scripts/asb clean-rebuild
```

**If prune hangs inside the VM too:**

```bash
colima stop
colima start --cpu 4 --memory 6 --disk 60 --network-address
# Then retry clean-rebuild (loses all build cache — slower but guaranteed)
```

---

### Symptom: `W: GPG error: ... At least one invalid signature was encountered`

**Cause:** Docker BuildKit cache corruption — stale GPG metadata cached from a previous
failed build. The packages are fine; the cache is stale.

```bash
# Targeted: prune just the BuildKit cache
docker builder prune -f

# If that hangs, escalate:
colima ssh -- docker builder prune -f

# Nuclear (from inside the VM):
colima ssh -- docker system prune -a -f
```

> **Note:** This is distinct from the ARM64/bookworm gpgv clearsign bug (see §9 Known Errors).
> The GPG warning during `apt-get update` that shows `Ign:` lines followed by a successful
> package list fetch is the **clearsign bug** — it's already worked around in the Dockerfile.
> A GPG error that causes apt-get to FAIL (exit code 100) with no packages downloaded is
> **cache corruption** and requires a prune.

---

### Symptom: `exit code: 100` on apt-get install

**Cause 1:** BuildKit cache corruption (most common). Fix: prune (see above).

**Cause 2:** Package genuinely unavailable for `arm64`/`bookworm`. Check git log for
packages that have been removed before (`openscap-scanner` was removed in commit `7128946`
due to this exact issue).

**Cause 3:** Network failure downloading packages. Check DNS and VPN state.

---

### Clean rebuild (safe — preserves workspace, config, SSH)

```bash
./scripts/asb clean-rebuild
```

This does:
1. `docker compose down` — stops containers
2. Removes only `gateway-data` and `clamav-db` volumes
3. `docker compose build --no-cache` — full image rebuild
4. `docker compose up -d` — starts everything

> **Workspace, config, SSH keys, browsers, and memory backups are NOT removed.**

---

### Full wipe (destructive — removes all state)

Only use if you need a completely fresh install:

```bash
# Prod:
./scripts/asb down
docker volume rm $(docker volume ls --filter name=agentshroud -q)

# Dev:
ssh agentshroud-bot@marvin 'cd ~/Development/agentshroud && ./scripts/asb down'
docker volume rm $(docker volume ls --filter name=agentshroud-bot -q)
```

---

## 8. Docker System Pruning

### Safe prune (removes only stopped containers + unused images + build cache)

```bash
docker system prune -f             # Keeps named volumes
docker builder prune -f            # BuildKit cache only
docker image prune -f              # Dangling images only
docker image prune -a -f           # ALL unused images (more aggressive)
```

### Check what would be removed (dry run)

```bash
docker system prune --dry-run
docker builder prune --dry-run
```

### Nuclear prune (removes everything including volumes)

```bash
docker system prune -a --volumes -f
```

> ⚠️ **This removes named volumes** including workspace, config, and SSH keys.
> Only use on a dev instance you don't mind rebuilding from scratch.

### Prune from inside Colima VM (use when host-side prune hangs)

```bash
colima ssh -- docker system prune -a -f
colima ssh -- docker builder prune -a -f
```

### Reclaim space from dangling layers in overlay2

If `df -h /var/lib/docker` shows high usage even after prune:

```bash
colima ssh -- docker system prune -a --volumes -f
# Then restart Colima to release overlay2 disk references:
colima stop && colima start --cpu 4 --memory 6 --disk 60 --network-address
```

---

## 9. VPN Networking Fix (Cisco AnyConnect)

When Cisco AnyConnect is active, it installs a `pf` anchor that blocks Docker egress
via Lima's `eth0` usernet interface (`192.168.5.1`).

**Fix:** Route Docker traffic via `col0` vmnet (`192.168.64.x`) instead.

This is **automatically applied** by a systemd service inside the Colima VM
(`/etc/systemd/system/colima-vmnet-route.service`). It sets `col0` as the primary
default route (metric 100) over `eth0` (metric 200).

**If traffic fails after Colima restart:**

```bash
# Verify the route is active inside the VM:
colima ssh -- ip route show

# Expected output includes:
#   default via 192.168.64.1 dev col0 metric 100
#   default via 192.168.5.2 dev eth0 metric 200

# If missing, re-apply manually:
colima ssh -- sudo ip route del default via 192.168.5.2 dev eth0 2>/dev/null || true
colima ssh -- sudo ip route add default via 192.168.64.1 dev col0 metric 100
```

**If Colima VM is recreated (e.g., after `colima delete`):**

The systemd service is lost. Re-install it:

```bash
colima ssh
# Inside VM:
cat > /etc/systemd/system/colima-vmnet-route.service << 'EOF'
[Unit]
Description=Route Docker traffic via col0 (bypass Cisco AnyConnect pf rules)
After=network.target

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/bin/bash -c 'ip route del default via 192.168.5.2 dev eth0 2>/dev/null; ip route add default via 192.168.64.1 dev col0 metric 100'

[Install]
WantedBy=multi-user.target
EOF
systemctl daemon-reload && systemctl enable --now colima-vmnet-route.service
exit
```

---

## 10. Common Errors — Quick Reference

| Error | Likely Cause | Fix |
|-------|-------------|-----|
| `E: You don't have enough free space in /apt-dl/` | Colima VM disk full | `colima ssh -- docker system prune -a -f` then retry |
| `W: GPG error: ... invalid signature` + build fails | BuildKit cache stale | `docker builder prune -f` or prune from inside VM |
| `exit code: 100` on apt-get (no GPG warning) | Package unavailable on arm64/bookworm | Check if package was removed in git history; may need a code fix |
| `Cannot connect to the Docker daemon` | Colima VM not running | `colima start --cpu 4 --memory 6 --disk 60 --network-address` |
| `docker system prune` hangs | Docker daemon unresponsive | Kill it, run `colima ssh -- docker system prune -a -f` instead |
| `permission denied: /apt-dl/partial` | Docker socket permission | `chmod g+rw ~/.colima/default/docker.sock` (handled by `asb`) |
| Gateway container `unhealthy` | Python app crash or startup timeout | `docker logs agentshroud-gateway \| tail -50` |
| Bot container `unhealthy` | OpenClaw crash or gateway dependency | Check gateway is healthy first; `docker logs agentshroud-bot \| tail -50` |
| Build: `CONNECT proxy rejected: 502` during WSS | Gateway not yet up when bot starts | Expected transient; bot auto-reconnects. Suppressed in `setup-https-proxy.js` |
| `Slack pong timeout` in bot logs | VPN reconnect / DNS hiccup | Harmless; demoted to debug in `patch-slack-sdk.sh` |
| `No space left on device` during `npm install` | `openclaw-runtime` volume full | `docker volume rm agentshroud_openclaw-runtime` then `./scripts/asb up` |

---

## 11. Dev Account (agentshroud-bot) Operations

All `asb` commands work the same when run as `agentshroud-bot` — the script auto-detects
the account and applies the Marvin overlay.

```bash
# SSH to bot account:
ssh agentshroud-bot@marvin

# Or run commands remotely:
ssh agentshroud-bot@marvin 'cd ~/Development/agentshroud && ./scripts/asb status'
ssh agentshroud-bot@marvin 'cd ~/Development/agentshroud && ./scripts/asb logs'
ssh agentshroud-bot@marvin 'cd ~/Development/agentshroud && ./scripts/asb clean-rebuild'

# Dev-specific container names:
docker logs -f agentshroud-marvin-gateway
docker logs -f agentshroud-marvin-bot
docker exec -it agentshroud-marvin-bot sh

# Dev-specific volumes (prefixed agentshroud-bot_):
docker volume ls --filter name=agentshroud-bot
docker volume rm agentshroud-bot_gateway-data agentshroud-bot_clamav-db
```

> **Note:** Both prod (`ijefferson.admin`) and dev (`agentshroud-bot`) share the same
> Colima VM. A `colima restart` or disk-full event on one account affects the other.
> Coordinate before running `colima stop` if prod is serving live traffic.
