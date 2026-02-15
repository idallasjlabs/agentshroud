# OpenClaw Device Pairing & Trusted Devices

**Last Updated**: 2026-02-15

---

## Overview

OpenClaw uses a **device pairing system** for security. Each browser or device that connects to the Control UI must be approved as a trusted device.

### Why Device Pairing?

- **Security**: Prevents unauthorized access even if someone gets the password
- **Multi-Device**: Lets you use OpenClaw from multiple browsers/devices securely
- **Audit Trail**: Track which devices have access
- **Revocable**: You can remove device access anytime

---

## How It Works

### 1. First Connection Attempt

When you try to connect from a new browser/device:

1. Enter the gateway password
2. Click "Connect"
3. OpenClaw creates a pairing request
4. You see: `disconnected (1008): pairing required`

### 2. Approve the Device

Run this command to see pending requests:
```bash
docker compose -f docker/docker-compose.yml exec openclaw openclaw devices list
```

You'll see something like:
```
Pending (1)
┌──────────────────────────────────────┬────────────────────────────────────┐
│ Request                              │ Device                             │
├──────────────────────────────────────┼────────────────────────────────────┤
│ 6c16f64f-c3df-4544-aa6b-a89182228d4c │ f74302...ad87                      │
└──────────────────────────────────────┴────────────────────────────────────┘
```

Approve it:
```bash
docker compose -f docker/docker-compose.yml exec openclaw openclaw devices approve REQUEST_ID
```

### 3. Device Connected

After approval:
- Refresh the browser (Cmd+R or click "Refresh" button)
- Status changes to "Connected"
- Device is now trusted

---

## Common Scenarios

### Chrome Already Working, Safari Shows "Pairing Required"

**Why**: Each browser is treated as a separate device.

**Solution**:
1. Enter password in Safari and click "Connect"
2. Run: `docker compose -f docker/docker-compose.yml exec openclaw openclaw devices list`
3. Find the pending request ID
4. Approve: `docker compose -f docker/docker-compose.yml exec openclaw openclaw devices approve REQUEST_ID`
5. Refresh Safari

### iPhone/iPad Control UI

**Why**: Mobile browsers are separate devices.

**Solution**: Same as above - approve each device once.

### Multiple Computers

**Why**: Each computer's browser needs approval.

**Solution**: Approve each device once, then they stay trusted.

---

## Device Management Commands

### List All Devices

```bash
docker compose -f docker/docker-compose.yml exec openclaw openclaw devices list
```

Shows:
- **Pending**: Awaiting approval
- **Paired**: Approved and trusted

### Approve a Device

```bash
docker compose -f docker/docker-compose.yml exec openclaw openclaw devices approve REQUEST_ID
```

Copy the Request ID from the "Pending" section.

### Remove a Device

```bash
docker compose -f docker/docker-compose.yml exec openclaw openclaw devices unpair DEVICE_ID
```

Use the Device ID from the "Paired" section.

### Approve All Pending Devices

```bash
docker compose -f docker/docker-compose.yml exec openclaw openclaw devices approve-all
```

**Warning**: Only use if you're sure all pending requests are yours.

---

## Quick Device Approval Script

I've added this to the management scripts:

```bash
# View pending device requests
./docker/scripts/devices.sh list

# Approve a specific device
./docker/scripts/devices.sh approve REQUEST_ID

# Approve all pending (use with caution)
./docker/scripts/devices.sh approve-all
```

---

## Troubleshooting

### "Pairing Required" After Entering Password

**Status**: Normal - device needs approval

**Fix**:
1. Run: `docker compose -f docker/docker-compose.yml exec openclaw openclaw devices list`
2. Copy the Request ID from "Pending"
3. Approve: `docker compose -f docker/docker-compose.yml exec openclaw openclaw devices approve REQUEST_ID`
4. Refresh browser

### Device List is Empty

**Why**: No pending requests

**Fix**: Try connecting from the browser again, then check the list immediately.

### Still Disconnected After Approval

**Fix**:
1. Click "Refresh" button in the Gateway Access section
2. Or refresh the browser page (Cmd+R)
3. Wait 5 seconds
4. Click "Connect" again

### Want to Re-pair a Browser

**Solution**:
1. Find the device ID: `docker compose -f docker/docker-compose.yml exec openclaw openclaw devices list`
2. Unpair it: `docker compose -f docker/docker-compose.yml exec openclaw openclaw devices unpair DEVICE_ID`
3. Refresh browser and go through pairing again

---

## Security Best Practices

### Regular Device Audit

Periodically check paired devices:
```bash
docker compose -f docker/docker-compose.yml exec openclaw openclaw devices list
```

Remove any you don't recognize:
```bash
docker compose -f docker/docker-compose.yml exec openclaw openclaw devices unpair DEVICE_ID
```

### When to Remove Devices

- Old computer you no longer use
- Browser you don't use anymore
- If you suspect unauthorized access
- After selling/giving away a device

### Password Protection

The device pairing system works **in addition to** the password:
- **Password**: First layer of security
- **Device Pairing**: Second layer of security

Both are required for access.

---

## Examples

### Example 1: Approve Safari

```bash
# 1. Check pending devices
$ docker compose -f docker/docker-compose.yml exec openclaw openclaw devices list

Pending (1)
┌──────────────────────────────────────┬────────────────────────────────────┐
│ Request                              │ Device                             │
├──────────────────────────────────────┼────────────────────────────────────┤
│ 6c16f64f-c3df-4544-aa6b-a89182228d4c │ f74302...ad87                      │
└──────────────────────────────────────┴────────────────────────────────────┘

# 2. Approve it
$ docker compose -f docker/docker-compose.yml exec openclaw openclaw devices approve 6c16f64f-c3df-4544-aa6b-a89182228d4c

Approved f7430240d88e55f247615b818afcfcc374bf1100827979ca11062b4f8784ad87

# 3. Refresh Safari - now connected!
```

### Example 2: Remove Old Chrome

```bash
# 1. List all paired devices
$ docker compose -f docker/docker-compose.yml exec openclaw openclaw devices list

Paired (3)
┌────────────────────────────────────────────┬────────────┐
│ Device                                     │ Roles      │
├────────────────────────────────────────────┼────────────┤
│ 542982a6190c3b6e9c7383fa484df6ec18a07b...  │ operator   │
│ 9e55851403622fadb5b214712c20a3f892af99...  │ operator   │
│ f7430240d88e55f247615b818afcfcc374bf11...  │ operator   │
└────────────────────────────────────────────┴────────────┘

# 2. Unpair the old one (copy full device ID from above)
$ docker compose -f docker/docker-compose.yml exec openclaw openclaw devices unpair 542982a6190c3b6e9c7383fa484df6ec18a07b0745b24696a6ea6137f38550cd

Device unpaired successfully
```

### Example 3: Setup New iPhone

```bash
# On iPhone:
# 1. Open Safari to http://localhost:18790 (if on same network)
#    Or use Tailscale/VPN to access remotely
# 2. Enter password and click Connect
# 3. See "pairing required" error

# On Mac terminal:
# 4. List pending
$ docker compose -f docker/docker-compose.yml exec openclaw openclaw devices list

# 5. Approve the iPhone request
$ docker compose -f docker/docker-compose.yml exec openclaw openclaw devices approve REQUEST_ID

# On iPhone:
# 6. Refresh Safari - now connected!
```

---

## Current Paired Devices

As of this setup, you have these approved:
- **Chrome** (542982a6...) - Already working
- **Safari** (f7430240...) - Just approved
- **Previous device** (9e55851...) - From earlier session

---

## Summary

| Action | Command |
|--------|---------|
| List devices | `docker compose -f docker/docker-compose.yml exec openclaw openclaw devices list` |
| Approve device | `docker compose -f docker/docker-compose.yml exec openclaw openclaw devices approve REQUEST_ID` |
| Remove device | `docker compose -f docker/docker-compose.yml exec openclaw openclaw devices unpair DEVICE_ID` |
| Approve all | `docker compose -f docker/docker-compose.yml exec openclaw openclaw devices approve-all` |

---

## Device Pairing Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│ New Browser/Device Attempts to Connect                     │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ User enters gateway password                                │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Password accepted, but shows "pairing required"             │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Pairing request created (visible in "devices list")         │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Admin approves device: "devices approve REQUEST_ID"         │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Browser refreshes and connects successfully                 │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Device is now trusted - no approval needed on future visits │
└─────────────────────────────────────────────────────────────┘
```

---

**Remember**: This is a security feature, not a bug. Each new browser/device needs one-time approval to ensure only you have access to your AI assistant.
