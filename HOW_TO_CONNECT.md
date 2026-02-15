# How to Connect to SecureClaw Chat

## Web Browser Access

### 1. Start the System
```bash
cd /Users/ijefferson.admin/Development/oneclaw
docker compose -f docker/docker-compose.yml up -d
```

### 2. Wait for Containers to be Healthy (15-20 seconds)
```bash
docker compose -f docker/docker-compose.yml ps
```

Both containers should show `(healthy)`:
- `secureclaw-gateway`
- `openclaw-chat`

### 3. Get Your Auth Token
```bash
docker logs secureclaw-gateway 2>&1 | grep "Generated new token" -A3
```

You'll see something like:
```
Generated new token:

    14bf48103da11537b7207a2fe5487084d39a799a6129f3bbcb644a417c7f091b
```

Copy the token (the long hexadecimal string).

### 4. Open Chat in Browser

**Option A: With Token in URL (Recommended)**
```
http://localhost:8080/?token=YOUR_TOKEN_HERE
```

**Option B: Enter Token When Prompted**
```
http://localhost:8080/
```
The page will prompt you to enter your token.

### 5. Start Chatting!

Type your message and press Enter or click Send.

**You are chatting directly with OpenClaw** (Isaiah's persona powered by OpenAI GPT-4 Turbo).

---

## What's Happening Behind the Scenes

1. Your browser sends messages to the **Gateway** (`localhost:8080/forward`)
2. Gateway sanitizes PII and logs to the audit ledger
3. Gateway forwards sanitized content to **OpenClaw** (`openclaw:18789/chat`)
4. OpenClaw processes with Isaiah's persona via OpenAI API
5. Response flows back through Gateway to your browser

---

## Current System Status

✅ **Gateway**: PII sanitization, audit ledger, secure routing
✅ **OpenClaw Chat**: Isaiah's persona with OpenAI GPT-4 Turbo
✅ **Security**: Read-only containers, non-root execution, localhost-only
✅ **End-to-End Pipeline**: Fully operational

---

## Your Current Auth Token

```
14bf48103da11537b7207a2fe5487084d39a799a6129f3bbcb644a417c7f091b
```

**Direct Link:**
```
http://localhost:8080/?token=14bf48103da11537b7207a2fe5487084d39a799a6129f3bbcb644a417c7f091b
```

---

## Troubleshooting

**Problem: "Failed to connect to SecureClaw Gateway"**
- Check containers are running: `docker compose -f docker/docker-compose.yml ps`
- Restart if needed: `docker compose -f docker/docker-compose.yml restart`

**Problem: "Invalid authentication scheme"**
- Make sure you copied the full token (64 characters)
- Check token hasn't expired (restart generates new token)

**Problem: "No response from agent"**
- Check OpenClaw is healthy: `docker logs openclaw-chat --tail 20`
- Verify OpenAI API key: `docker exec openclaw-chat ls -l /run/secrets/openai_api_key`

---

**Note**: This is OpenClaw chat, not a custom interface. The web UI is just a browser-based client that connects to the same `/forward` API that iOS Shortcuts and browser extensions will use.
