# Tailscale Access to OpenClaw Control UI

Access your OpenClaw dashboard from anywhere on your Tailnet at:
**http://marvin.tail240ea8.ts.net:18790**

## Option 1: Tailscale Serve (Recommended - Most Secure)

This keeps the Docker container bound to localhost only, and Tailscale proxies requests securely.

```bash
# Start Tailscale serve for OpenClaw Control UI
sudo tailscale serve --bg --https=443 http://localhost:18790

# Or without HTTPS (if you prefer http://)
sudo tailscale serve --bg http://localhost:18790
```

Access via:
- HTTPS: `https://marvin.tail240ea8.ts.net`
- HTTP: `http://marvin.tail240ea8.ts.net:18790`

To stop:
```bash
sudo tailscale serve off
```

## Option 2: Bind to All Interfaces (Less Secure)

Modify `docker/docker-compose.yml` to bind to all interfaces instead of just localhost:

```yaml
ports:
  - "0.0.0.0:18790:18789"  # Instead of 127.0.0.1:18790:18789
```

Then restart:
```bash
docker compose -f docker/docker-compose.yml restart openclaw
```

**Security Note**: This exposes port 18790 on all network interfaces. Use Tailscale ACLs to restrict access.

## Option 3: Bind to Tailscale IP Only (Best Balance)

Get your Tailscale IP:
```bash
tailscale ip -4
```

Example output: `100.64.0.5`

Modify `docker/docker-compose.yml`:
```yaml
ports:
  - "100.64.0.5:18790:18789"  # Replace with your Tailscale IP
```

Then restart:
```bash
docker compose -f docker/docker-compose.yml restart openclaw
```

## Current Status

Currently bound to: `127.0.0.1:18790` (localhost only)

## Verification

After setup, test from another device on your Tailnet:
```bash
curl http://marvin.tail240ea8.ts.net:18790/api/health
```

Should return:
```json
{"status":"ok","version":"..."}
```

## Tailscale ACLs (Recommended)

Add to your Tailscale ACL to restrict access:

```json
{
  "acls": [
    {
      "action": "accept",
      "src": ["youremail@example.com"],
      "dst": ["marvin:18790"]
    }
  ]
}
```

This ensures only you can access the OpenClaw dashboard.
