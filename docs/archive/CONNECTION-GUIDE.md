# AgentShroud Control UI Connection Guide

## Quick Fix: Connect to Gateway

Your AgentShroud gateway is running at `ws://127.0.0.1:18789`. Here's how to connect the Control UI.

### Step 1: Open Control UI

Open in your browser:
```
http://localhost:18791
```

### Step 2: Configure Gateway Connection

When the Control UI loads, you'll see a connection settings dialog or gear icon. Click it and enter:

**Gateway URL**:
```
ws://127.0.0.1:18789
```

**Auth Token**:
```
acd0842962070d58c2bb825876aab743c4c45ddbc2eae7e475c4058e0b3f7832
```

### Step 3: Test Connection

The UI should show "Connected" in green. If not, try:

1. **Check if gateway is running**:
   ```bash
   docker ps | grep agentshroud
   ```
   Should show: `Up X minutes (healthy)`

2. **Test WebSocket connection directly**:
   ```bash
   curl -i -N \
     -H "Connection: Upgrade" \
     -H "Upgrade: websocket" \
     -H "Sec-WebSocket-Version: 13" \
     -H "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==" \
     http://localhost:18789/
   ```
   Should return HTTP 101 Switching Protocols

3. **Check gateway logs**:
   ```bash
   docker logs agentshroud_isaiah --tail 50
   ```
   Look for connection attempts or errors

### Alternative: Use Built-In Control UI (If Available)

OpenClaw may have a built-in Control UI accessible at:
```
http://localhost:18789/
```

Try opening this directly in your browser.

## Troubleshooting

### "Cannot connect to gateway"

**Possible causes**:
1. Gateway not running
2. Wrong port (should be 18789)
3. Browser blocking WebSocket connection
4. Wrong auth token

**Solutions**:

1. **Restart everything**:
   ```bash
   ./stop-agentshroud.sh
   ./start-agentshroud.sh
   ```

2. **Check gateway health**:
   ```bash
   docker exec agentshroud_isaiah node openclaw.mjs health
   ```

3. **Verify token**:
   ```bash
   grep OPENCLAW_GATEWAY_TOKEN agentshroud-container/secrets/.env
   ```

### "Disconnected (1006): no reason"

This WebSocket error usually means:
- Authentication failed (wrong token)
- Gateway crashed/restarted
- Network issue

**Fix**:
1. Get fresh token:
   ```bash
   cat agentshroud-container/secrets/.env | grep OPENCLAW_GATEWAY_TOKEN
   ```

2. Clear browser cache and cookies for localhost:18791

3. Restart gateway:
   ```bash
   docker compose -f agentshroud-container/docker-compose.yml restart
   ```

### "Connection timeout"

Check if port 18789 is actually open:
```bash
lsof -i :18789
```

Should show:
```
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
docker    123 you    45u  IPv4  0x...      0t0  TCP localhost:18789 (LISTEN)
```

If nothing, gateway isn't listening. Check logs:
```bash
docker logs agentshroud_isaiah --tail 100
```

## Manual Connection Test

Test the gateway manually with wscat (install if needed):

```bash
# Install wscat
npm install -g wscat

# Connect to gateway
wscat -c ws://127.0.0.1:18789 \
  -H "Authorization: Bearer acd0842962070d58c2bb825876aab743c4c45ddbc2eae7e475c4058e0b3f7832"
```

If connected, you should see:
```
Connected (press CTRL+C to quit)
```

Then type:
```json
{"jsonrpc":"2.0","id":1,"method":"health","params":{}}
```

Gateway should respond with health status.

## Using CLI Instead of Web UI

If the web UI won't connect, you can use the CLI directly:

```bash
# Check status
docker exec agentshroud_isaiah node openclaw.mjs status

# Send a test message
docker exec agentshroud_isaiah node openclaw.mjs message send \
  --target test \
  --message "Hello, this is a test"

# View models
docker exec agentshroud_isaiah node openclaw.mjs models status

# Check logs
docker exec agentshroud_isaiah node openclaw.mjs logs --tail 50
```

## Getting Help

If still having issues:

1. Export logs:
   ```bash
   docker logs agentshroud_isaiah > /tmp/agentshroud-debug.log
   ```

2. Check container status:
   ```bash
   docker inspect agentshroud_isaiah | grep -A 5 State
   ```

3. Open GitHub issue with:
   - Error message
   - Browser console logs (F12 → Console tab)
   - Output of `docker logs agentshroud_isaiah --tail 100`
   - macOS version
   - Docker version

## Success Checklist

- [ ] `docker ps` shows agentshroud_isaiah as "Up" and "healthy"
- [ ] `docker logs agentshroud_isaiah` shows "gateway listening on ws://127.0.0.1:18789"
- [ ] http://localhost:18791 loads the Control UI
- [ ] Control UI shows "Connected" to gateway
- [ ] Can send test message and get response

If all checked ✅ → You're ready to use AgentShroud!

---

**Next Steps After Connection**:
- Read [FIRST-TIME-SETUP.md](./FIRST-TIME-SETUP.md) for usage guide
- Review [SECURITY-ANALYSIS.md](./SECURITY-ANALYSIS.md) for security details
- Check [FUTURE-FEATURES.md](./FUTURE-FEATURES.md) for roadmap
