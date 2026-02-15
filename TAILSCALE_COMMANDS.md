# Tailscale Remote Access Setup

## Access OpenClaw Dashboard Remotely

Run these commands on your Mac to enable remote access via Tailscale:

### Option 1: OpenClaw Control UI on Port 18790

```bash
# Serve the OpenClaw Control UI
sudo tailscale serve --bg --https=18790 http://localhost:18790
```

Access from anywhere on your Tailnet:
- **URL**: `https://marvin.tail240ea8.ts.net:18790`

### Option 2: Gateway Dashboard on Port 8080

```bash
# Serve the SecureClaw Gateway Dashboard
sudo tailscale serve --bg --https=443 http://localhost:8080
```

Access from anywhere on your Tailnet:
- **URL**: `https://marvin.tail240ea8.ts.net`

### Option 3: Both Services

```bash
# Serve both (recommended)
sudo tailscale serve --bg --https=443 http://localhost:8080
sudo tailscale serve --bg --https=18790 http://localhost:18790
```

Access:
- **Gateway Dashboard**: `https://marvin.tail240ea8.ts.net`
- **OpenClaw Control UI**: `https://marvin.tail240ea8.ts.net:18790`

## Stop Tailscale Serve

```bash
# Stop all Tailscale serve instances
sudo tailscale serve off
```

## Verify Tailscale Serve Status

```bash
# Check what's being served
sudo tailscale serve status
```

## Security: Tailscale ACLs

Add this to your Tailscale ACL policy to restrict access to only your account:

```json
{
  "acls": [
    {
      "action": "accept",
      "src": ["youremail@example.com"],
      "dst": ["marvin:8080", "marvin:18790"]
    }
  ]
}
```

Replace `youremail@example.com` with your actual Tailscale email.

## Current Status

- **OpenClaw Control UI**: http://localhost:18790 (local only)
- **Gateway Dashboard**: http://localhost:8080 (local only)
- **Telegram Bot**: @therealidallasj_bot (active)
- **Gmail**: Not yet configured

## Next Steps

1. Enable Tailscale serve with the commands above
2. Test access from another device on your Tailnet (iPhone, iPad, etc.)
3. Set up Gmail integration
4. Start using your bot remotely!
