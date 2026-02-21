# AgentShroud Device Pairing Management

**Version**: 1.0
**Last Updated**: 2026-02-16

---

## Overview

Device pairing is a critical security feature in AgentShroud that ensures only explicitly approved devices can access the OpenClaw Control UI. This is a second layer of authentication beyond the gateway password.

**Security Model:**
1. **Gateway Password** - Required for ALL connections (first layer)
2. **Device Pairing** - Each device/browser must be explicitly approved (second layer)

This dual-layer approach prevents unauthorized access even if the gateway password is compromised.

---

## Why Device Pairing Matters

For AgentShroud ("One Shroud Over Every Wire"), device pairing ensures:
- You control exactly which devices can manage the AI agent
- Each new browser/computer requires your explicit approval
- Stolen passwords alone cannot grant access
- Full audit trail of which devices have connected
- Ability to revoke access from compromised devices

**Never disable device pairing** - it's a core AgentShroud security feature.

---

## How Device Pairing Works

When a browser tries to connect to the Control UI:
1. User enters the gateway password (first authentication)
2. Browser requests device pairing
3. OpenClaw creates a **pending pairing request** with a unique device ID
4. Request is stored in: `/home/node/.openclaw/devices/pending.json`
5. Administrator must approve the request via CLI
6. Once approved, device is added to: `/home/node/.openclaw/devices/paired.json`
7. Device can now connect (until revoked)

---

## Finding Pending Pairing Requests

### Method 1: Via CLI (Recommended)

```bash
# List all pending device pairing requests
docker exec openclaw-bot openclaw devices list
```

**Example output:**
```
Pending Devices:
  Request ID: 9d6e6573-d784-4c53-8a55-c347d5e9eee4
  Device ID:  b3d441432a8b6544967a80fb20746ce50c92570d055a25f026c18fc25d14637d
  Platform:   MacIntel
  Client:     openclaw-control-ui
  Remote IP:  172.21.0.1
  Requested:  2026-02-16 06:42:27 UTC

Paired Devices: 1
Pending Requests: 1
```

### Method 2: View Raw Pending File

```bash
# View pending pairing requests directly
docker exec openclaw-bot cat /home/node/.openclaw/devices/pending.json | jq
```

### Method 3: Check Container Logs

```bash
# Search logs for pairing activity
docker logs openclaw-bot 2>&1 | grep -i "pairing\|device" | tail -20
```

**When you see** "disconnected (1008): pairing required" in your browser, there's a pending request waiting for approval.

---

## Approving Device Pairing Requests

### Quick Approval (Single Device)

```bash
# Approve a specific request by Request ID
docker exec openclaw-bot openclaw devices approve <REQUEST_ID>
```

**Example:**
```bash
docker exec openclaw-bot openclaw devices approve 9d6e6573-d784-4c53-8a55-c347d5e9eee4
```

**Output:**
```
✓ Approved b3d441432a8b6544967a80fb20746ce50c92570d055a25f026c18fc25d14637d
```

### Approve All Pending Requests

```bash
# List all pending request IDs
docker exec openclaw-bot openclaw devices list | grep "Request ID" | awk '{print $3}'

# Approve each one (replace IDs with actual values)
docker exec openclaw-bot openclaw devices approve <REQUEST_ID_1>
docker exec openclaw-bot openclaw devices approve <REQUEST_ID_2>
```

### Verify Approval

```bash
# Check that device is now in paired list
docker exec openclaw-bot cat /home/node/.openclaw/devices/paired.json | jq
```

After approval, **refresh your browser** and the connection should succeed.

---

## Listing Paired Devices

### View All Paired Devices

```bash
# List all currently paired devices
docker exec openclaw-bot openclaw devices list
```

### View Detailed Device Information

```bash
# Show full details of all paired devices
docker exec openclaw-bot cat /home/node/.openclaw/devices/paired.json | jq
```

**Example output:**
```json
{
  "b3d441432a8b6544967a80fb20746ce50c92570d055a25f026c18fc25d14637d": {
    "deviceId": "b3d441432a8b6544967a80fb20746ce50c92570d055a25f026c18fc25d14637d",
    "platform": "MacIntel",
    "clientId": "openclaw-control-ui",
    "remoteIp": "172.21.0.1",
    "role": "operator",
    "scopes": ["operator.admin", "operator.approvals", "operator.pairing"],
    "approvedAtMs": 1771224775028
  }
}
```

**Key Fields:**
- `deviceId` - Unique device identifier (SHA-256 hash)
- `platform` - Operating system (MacIntel, Linux, etc.)
- `remoteIp` - IP address of device
- `role` - Permission level (operator = full access)
- `approvedAtMs` - When device was approved (Unix timestamp)

---

## Rejecting Pairing Requests

If you see an unfamiliar device requesting access:

```bash
# Reject a specific pairing request
docker exec openclaw-bot openclaw devices reject <REQUEST_ID>
```

**Example:**
```bash
docker exec openclaw-bot openclaw devices reject 9d6e6573-d784-4c53-8a55-c347d5e9eee4
```

The device will be denied and removed from pending requests.

---

## Revoking Device Access

If a device is compromised or you want to remove access:

```bash
# Revoke a paired device's operator token
docker exec openclaw-bot openclaw devices revoke <DEVICE_ID> operator
```

**Example:**
```bash
docker exec openclaw-bot openclaw devices revoke b3d441432a8b6544967a80fb20746ce50c92570d055a25f026c18fc25d14637d operator
```

**What this does:**
- Immediately invalidates the device's access token
- Device can no longer connect to Control UI
- Device must re-request pairing to regain access
- Previous pairing record is preserved for audit trail

---

## Common Scenarios

### Scenario 1: New Browser/Computer

**Symptoms:** Browser shows "disconnected (1008): pairing required"

**Solution:**
1. Check for pending requests:
   ```bash
   docker exec openclaw-bot openclaw devices list
   ```
2. Approve your device:
   ```bash
   docker exec openclaw-bot openclaw devices approve <REQUEST_ID>
   ```
3. Refresh browser

### Scenario 2: Safari Private Window

**Issue:** Each private window is treated as a new device

**Solution:** Either:
- Approve each private window session separately (more secure)
- Use regular Safari window (device stays paired)

### Scenario 3: Multiple Computers

**Issue:** Want to access from Mac, iPhone, and work laptop

**Solution:**
1. Connect from each device
2. Approve each device's pairing request separately:
   ```bash
   docker exec openclaw-bot openclaw devices list  # See all pending
   docker exec openclaw-bot openclaw devices approve <MAC_REQUEST_ID>
   docker exec openclaw-bot openclaw devices approve <IPHONE_REQUEST_ID>
   docker exec openclaw-bot openclaw devices approve <LAPTOP_REQUEST_ID>
   ```
3. Each device is now independently tracked

### Scenario 4: Lost/Stolen Device

**Issue:** Need to immediately revoke access from compromised device

**Solution:**
1. Identify the device:
   ```bash
   docker exec openclaw-bot openclaw devices list
   ```
2. Note the device ID and IP address
3. Revoke immediately:
   ```bash
   docker exec openclaw-bot openclaw devices revoke <DEVICE_ID> operator
   ```
4. Check that device is no longer in paired list

### Scenario 5: Clear All Devices (Nuclear Option)

**Issue:** Want to reset all device pairings

**⚠️ WARNING:** This will disconnect ALL devices including yours.

```bash
# Backup current pairings first
docker exec openclaw-bot cat /home/node/.openclaw/devices/paired.json > paired-backup.json

# Clear all pairings
docker exec openclaw-bot sh -c 'echo "{}" > /home/node/.openclaw/devices/paired.json'
docker exec openclaw-bot sh -c 'echo "{}" > /home/node/.openclaw/devices/pending.json'

# Restart container to apply
docker compose -f docker/docker-compose.yml restart openclaw
```

After this, you'll need to re-pair all devices from scratch.

---

## Security Best Practices

### 1. Regular Audits

**Monthly:** Review paired devices and revoke any you don't recognize:
```bash
docker exec openclaw-bot openclaw devices list
```

### 2. Principle of Least Privilege

- Only approve devices you personally use
- Reject unknown or suspicious pairing requests immediately
- Revoke access when devices are no longer needed

### 3. Monitor Remote IPs

Check that paired devices connect from expected IP addresses:
```bash
docker exec openclaw-bot cat /home/node/.openclaw/devices/paired.json | jq '.[] | {deviceId, remoteIp, platform}'
```

Unexpected IPs may indicate:
- VPN usage (normal if you use VPN)
- Network compromise (investigate)
- Unauthorized access attempt (revoke immediately)

### 4. Document Your Devices

Keep a list of which devices you've approved:
```
# My Approved Devices
- MacBook Pro (platform: MacIntel, IP: 192.168.1.x)
- iPhone 15 (platform: iPhone, IP: 192.168.1.y)
- Work Laptop (platform: MacIntel, IP: 10.0.0.z)
```

### 5. Rotate on Compromise

If you suspect any security incident:
1. Immediately revoke ALL device tokens
2. Change gateway password (in `docker/secrets/gateway_password.txt`)
3. Restart OpenClaw container
4. Re-pair only trusted devices

---

## Troubleshooting

### Problem: "pairing required" but no pending requests

**Cause:** Request expired or was already processed

**Solution:**
1. Force refresh browser: `⌘⇧R` (Mac) or `Ctrl+Shift+R` (Windows)
2. Clear browser cache for localhost:18790
3. Try connecting again in private window
4. Check for new pending request:
   ```bash
   docker exec openclaw-bot openclaw devices list
   ```

### Problem: Approved device still can't connect

**Possible causes:**
1. Browser cache has old device ID
   - **Fix:** Clear browser cache, use private window
2. Gateway password is wrong
   - **Fix:** Verify password in `docker/secrets/gateway_password.txt`
3. Container restarted and device ID changed
   - **Fix:** Check pending requests and approve new ID

### Problem: Too many pending requests

**Cause:** Multiple browsers/tabs creating requests

**Solution:**
```bash
# See all pending requests
docker exec openclaw-bot openclaw devices list

# Approve only the most recent one (check timestamp)
docker exec openclaw-bot openclaw devices approve <LATEST_REQUEST_ID>

# Reject old requests
docker exec openclaw-bot openclaw devices reject <OLD_REQUEST_ID_1>
docker exec openclaw-bot openclaw devices reject <OLD_REQUEST_ID_2>
```

---

## Integration with AgentShroud Workflow

Device pairing integrates with other AgentShroud security features:

1. **Gateway Password** (First layer)
   - Stored in: `docker/secrets/gateway_password.txt`
   - Required for ALL connections
   - Rotate regularly

2. **Device Pairing** (Second layer - THIS DOCUMENT)
   - Stored in: `/home/node/.openclaw/devices/`
   - Per-device approval required
   - Revocable at any time

3. **Telegram Allowlist** (Channel security)
   - Stored in: `/home/node/.openclaw/openclaw.json`
   - Only whitelisted Telegram user IDs can message bot
   - Independent of Control UI access

4. **Approval Queue** (Action gating)
   - Skills marked with `requiresApproval: true`
   - Must approve via Control UI before execution
   - Full audit trail in gateway ledger

All four layers work together to implement "One Shroud Over Every Wire."

---

## Quick Reference Commands

```bash
# List pending and paired devices
docker exec openclaw-bot openclaw devices list

# Approve a pairing request
docker exec openclaw-bot openclaw devices approve <REQUEST_ID>

# Reject a pairing request
docker exec openclaw-bot openclaw devices reject <REQUEST_ID>

# Revoke a paired device
docker exec openclaw-bot openclaw devices revoke <DEVICE_ID> operator

# View pending requests (raw)
docker exec openclaw-bot cat /home/node/.openclaw/devices/pending.json | jq

# View paired devices (raw)
docker exec openclaw-bot cat /home/node/.openclaw/devices/paired.json | jq

# Monitor pairing activity in logs
docker logs openclaw-bot --follow 2>&1 | grep -i "pairing\|device"
```

---

## File Locations

| File | Purpose | Location |
|------|---------|----------|
| Pending requests | Unapproved pairing requests | `/home/node/.openclaw/devices/pending.json` |
| Paired devices | Approved devices with tokens | `/home/node/.openclaw/devices/paired.json` |
| Gateway password | Primary authentication | `docker/secrets/gateway_password.txt` |
| OpenClaw config | Telegram allowlist, settings | `/home/node/.openclaw/openclaw.json` |

---

## Security Notes

- Device IDs are **SHA-256 hashes** of browser fingerprints
- Each private browsing session generates a **new device ID**
- Device tokens use **public key cryptography** for secure authentication
- Pairing records include **timestamps** for audit trail
- Revoking a device **does not delete** the pairing record (preserves audit)

---

**Remember:** Device pairing is security, not inconvenience. Each approval step ensures only YOU control what accesses your AI agent.

**Questions or Issues?** Check logs, verify file contents, and always err on the side of rejecting unknown devices.
