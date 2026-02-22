# Docker Commands Reference

Commands used to manage, debug, and configure the AgentShroud containers.

## Container management

```bash
# Start all services
docker compose -f docker/docker-compose.yml up -d

# Stop and restart all services
docker compose -f docker/docker-compose.yml restart

# Restart a single container (picks up volume changes, NOT image changes)
docker restart agentshroud-bot
docker restart agentshroud-gateway

# Stop everything (volumes preserved)
docker compose -f docker/docker-compose.yml down

# Stop everything AND delete volumes (WARNING: destroys all bot config/memory)
docker compose -f docker/docker-compose.yml down -v
```

## Container status

```bash
# Show running containers with health status
docker ps

# Show only agentshroud containers
docker ps --filter "name=agentshroud"

# Formatted output: name + status
docker ps --filter "name=agentshroud" --format "{{.Names}}\t{{.Status}}"

# Show resource usage (CPU, memory)
docker stats agentshroud-bot agentshroud-gateway
```

## Exec into containers

```bash
# Run a command inside the bot container
docker exec agentshroud-bot sh -c "some command"

# Run an interactive shell (if the image supports it)
docker exec -it agentshroud-bot sh

# Run a command inside the gateway container
docker exec agentshroud-gateway sh -c "some command"

# Pipe stdin into a container command (works with read-only rootfs)
# Use this when docker cp fails due to read-only filesystem
cat localfile.txt | docker exec -i agentshroud-bot sh -c "cat > /tmp/file.txt"

# Write a multi-line script to /tmp and run it (bypasses read-only rootfs)
cat << 'EOF' | docker exec -i agentshroud-bot sh -c "cat > /tmp/script.sh && sh /tmp/script.sh"
#!/bin/sh
echo "hello from inside the container"
EOF
```

## Reading files from containers

```bash
# Read a file from the bot container
docker exec agentshroud-bot sh -c "cat /home/node/.openclaw/cron/jobs.json"

# Read and pretty-print JSON
docker exec agentshroud-bot sh -c "cat /home/node/.openclaw/openclaw.json" | python3 -m json.tool

# List directory contents
docker exec agentshroud-bot sh -c "ls -lt /home/node/.openclaw/cron/runs/ | head -10"

# Search for text across container files (avoid /proc and /sys)
docker exec agentshroud-bot sh -c "grep -r 'search_term' /home/node/.openclaw/ 2>/dev/null | grep -v '.jsonl'"
```

## Writing files to containers

```bash
# Copy a local file into a container (fails if rootfs is read-only)
docker cp localfile.txt agentshroud-bot:/tmp/localfile.txt

# Write a file via stdin pipe (works with read-only rootfs, writes to tmpfs /tmp)
cat localfile.txt | docker exec -i agentshroud-bot sh -c "cat > /home/node/.openclaw/config.json"
```

## OpenClaw CLI commands (run inside agentshroud-bot)

All OpenClaw commands require the operator device token, stored at:
`/home/node/.openclaw/devices/paired.json` (field: `token`)

```bash
# Get the operator token
docker exec agentshroud-bot sh -c "cat /home/node/.openclaw/devices/paired.json" | python3 -c "import json,sys; print(json.load(sys.stdin)['token'])"

# List cron jobs
docker exec agentshroud-bot sh -c "openclaw cron list --token TOKEN"

# Run a cron job immediately
docker exec agentshroud-bot sh -c "openclaw cron run JOB_UUID --token TOKEN --timeout 90000"

# Edit a cron job schedule
docker exec agentshroud-bot sh -c "openclaw cron edit JOB_UUID --cron '0 9 * * *' --token TOKEN"

# Edit a cron job payload (isolated session + agentTurn)
# Use Python subprocess to avoid shell expansion of $() in payload text
python3 -c "
import subprocess
result = subprocess.run(
    ['docker','exec','agentshroud-bot',
     'openclaw','cron','edit','JOB_UUID',
     '--session','isolated',
     '--agent','main',
     '--message','Your payload text here',
     '--token','TOKEN'],
    capture_output=True, text=True
)
print(result.stdout if result.returncode == 0 else result.stderr)
"

# Remove a cron job
docker exec agentshroud-bot sh -c "openclaw cron rm JOB_UUID --token TOKEN"

# List agents and see which is default
docker exec agentshroud-bot sh -c "openclaw agents list"

# Check channel health
docker exec agentshroud-bot sh -c "openclaw channels status --probe --token TOKEN"
```

## Logs

```bash
# Follow live logs for the bot container
docker logs -f agentshroud-bot

# Follow live logs for the gateway
docker logs -f agentshroud-gateway

# Last 100 lines of bot logs
docker logs --tail 100 agentshroud-bot

# Show logs with timestamps
docker logs -t agentshroud-bot | tail -50
```

## Secrets inspection (read-only check)

```bash
# Verify a secret file exists and is non-empty (does NOT print the value)
docker exec agentshroud-bot sh -c "[ -s /run/secrets/gateway_password ] && echo 'ok' || echo 'missing'"
docker exec agentshroud-bot sh -c "[ -s /run/secrets/1password_service_account ] && echo 'ok' || echo 'missing'"

# Check all secrets are present
for s in gateway_password openai_api_key anthropic_api_key 1password_service_account; do
  docker exec agentshroud-bot sh -c "[ -s /run/secrets/$s ] && echo '$s: ok' || echo '$s: MISSING'"
done
```

## Networking

```bash
# Inspect the internal Docker network
docker network inspect agentshroud_agentshroud-isolated

# Check what networks a container is on
docker inspect agentshroud-bot --format '{{json .NetworkSettings.Networks}}' | python3 -m json.tool
```

## Volume management

```bash
# List Docker volumes
docker volume ls | grep agentshroud

# Inspect a volume (shows mount point on host)
docker volume inspect agentshroud_agentshroud-config

# Back up a volume by copying from container
docker exec agentshroud-bot sh -c "tar czf - /home/node/.openclaw/" > openclaw-backup-$(date +%Y%m%d).tar.gz
```

## Debugging read-only filesystem errors

The `agentshroud-bot` container uses `read_only: true`. Writable paths are:
- `/tmp` (tmpfs, noexec, 500MB)
- `/var/tmp` (tmpfs, noexec, 100MB)
- `/home/node/.openclaw` (Docker volume, fully writable)
- `/home/node/agentshroud/workspace` (Docker volume)

```bash
# If docker cp fails with "read-only filesystem", use stdin pipe to /tmp instead:
cat script.js | docker exec -i agentshroud-bot sh -c "cat > /tmp/script.js && node /tmp/script.js"
```
