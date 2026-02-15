# OpenClaw Access Information

**Last Updated**: 2026-02-15

---

## Control UI Access

### URL
```
http://localhost:18790
```

### Gateway Password
```
b539ae0c7a720f71e9b26cfab1b53c58ae362a0ad40d857eaed9a44a15932a05
```

---

## How to Connect

### First Time Setup (Chrome or Safari)

1. **Open the URL**: http://localhost:18790
2. **Wait for the page to load**
3. **Look for "Gateway Access" section** in Settings or on the main page
4. **Enter the password** in the "Password (not stored)" field
5. **Click "Connect"** or similar button
6. **Status should change to "Connected"**

### If Safari Shows "Disconnected"

Safari may have cached the old connection state. Try these steps:

#### Option 1: Clear Safari Cache
1. Go to Safari → Settings → Privacy
2. Click "Manage Website Data"
3. Search for "localhost"
4. Click "Remove" then "Done"
5. Refresh the page (Cmd+R)
6. Enter the password again

#### Option 2: Force Refresh
1. Open http://localhost:18790
2. Press **Cmd+Shift+R** (force reload)
3. Enter the password when prompted
4. Click Connect

#### Option 3: Use Private Window
1. Open Safari Private Window (Cmd+Shift+N)
2. Go to http://localhost:18790
3. Enter the password
4. Click Connect

---

## Current Configuration Status

### ✅ Working
- **Containers**: Both healthy
- **API Keys**: OpenAI and Anthropic configured
- **Gateway**: Healthy (http://localhost:8080)
- **Control UI**: Available at http://localhost:18790

### ⏳ Needs Configuration
- **Telegram Bot**: Removed old @idallasj_bot
- **Next Step**: Add @therealidallasj_bot with token from @BotFather

---

## Verify Connection

### Test 1: Check Containers
```bash
docker compose -f docker/docker-compose.yml ps
```

Both should show "(healthy)":
- openclaw-bot
- secureclaw-gateway

### Test 2: Check Gateway
```bash
curl http://localhost:8080/status
```

Should return JSON with "status": "healthy"

### Test 3: Check UI is Accessible
```bash
curl http://localhost:18790
```

Should return HTML (OpenClaw Control UI page)

---

## Troubleshooting

### "Connection Failed" or "Disconnected"

1. **Verify containers are running**:
   ```bash
   docker compose -f docker/docker-compose.yml ps
   ```

2. **Check if port 18790 is accessible**:
   ```bash
   curl http://localhost:18790
   ```

3. **Restart if needed**:
   ```bash
   ./docker/scripts/restart.sh
   ```

### "Invalid Password" or "Unauthorized"

Make sure you're copying the entire password:
```
b539ae0c7a720f71e9b26cfab1b53c58ae362a0ad40d857eaed9a44a15932a05
```

### Safari Keeps Showing "Disconnected"

1. Try Chrome first to verify it works
2. Clear Safari cache completely
3. Use Safari Private Window
4. If still issues, use Chrome for OpenClaw

---

## API Keys Status

Both API keys are configured and working:

### OpenAI
- Status: ✅ Configured
- Source: /run/secrets/openai_api_key
- Loaded: Via environment variable

### Anthropic
- Status: ✅ Configured  
- Source: /run/secrets/anthropic_api_key
- Loaded: Via environment variable

To verify:
```bash
./docker/scripts/check-status.sh
```

Look for:
```
- anthropic effective=env:sk-ant-a...
- openai effective=env:sk-proj-...
```

---

## Next Steps

1. ✅ **Access Control UI**: http://localhost:18790 with password
2. ⏳ **Add Telegram Bot**:
   - Get token from @BotFather for @therealidallasj_bot
   - Run: `./docker/scripts/telegram.sh add TOKEN`
   - Approve pairing
3. ⏳ **Test Bot**: Message @therealidallasj_bot on Telegram

---

## Quick Access

**Copy and paste these into your browser**:

- Control UI: http://localhost:18790
- Gateway Status: http://localhost:8080/status

**Password** (click to copy):
```
b539ae0c7a720f71e9b26cfab1b53c58ae362a0ad40d857eaed9a44a15932a05
```

---

## Summary

| Item | Status |
|------|--------|
| OpenClaw Container | ✅ Healthy |
| Gateway Container | ✅ Healthy |
| OpenAI API Key | ✅ Configured |
| Anthropic API Key | ✅ Configured |
| Control UI URL | http://localhost:18790 |
| Telegram Channel | ⏳ Needs @therealidallasj_bot token |

**Everything is working! Just add your Telegram bot token to complete the setup.**
