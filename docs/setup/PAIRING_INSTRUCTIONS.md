# OpenClaw Control UI Pairing Instructions

**Status**: Action required to complete pairing

---

## ✅ Step-by-Step Pairing Process

### Step 1: Open the Control UI

Go to: http://localhost:18790

You should see the OpenClaw Control interface with a "Disconnected from gateway" message.

---

### Step 2: Open Settings

1. Look for the **Settings** icon (usually a gear icon ⚙️) in the top-right corner of the UI
2. Click on **Settings**

---

### Step 3: Enter the Gateway Token

1. In the Settings panel, find the **"Gateway Token"** or **"Token"** field
2. Paste this token:

```
YOUR_GATEWAY_PASSWORD_HERE
```

3. Click **"Save"** or **"Connect"**

---

### Step 4: Verify Connection

The UI should now show **"Connected"** status and you can start using OpenClaw.

---

## Alternative: Auto-Pairing URL

If the UI has a field to paste a pairing URL, use this:

```
http://localhost:18790/#token=YOUR_GATEWAY_PASSWORD_HERE
```

---

##  Troubleshooting

### Still shows "pairing required"

Try clearing your browser cache and cookies for localhost:18790, then:

1. Close all tabs with the OpenClaw UI
2. Open a new incognito/private window
3. Go to: http://localhost:18790
4. Enter the token in Settings as described above

### Token field not visible

Some OpenClaw versions show the token field only after clicking:
- "Configure" or "Settings" button
- "Pair with Gateway" link
- Look for a connection status message with a link

### Cannot save token

Make sure:
- The token is copied exactly (no extra spaces)
- You're using a supported browser (Chrome, Firefox, Safari, Edge)
- JavaScript is enabled in your browser

---

## Security Note

✅ **This token is required and secure**
- 64-character cryptographic random hex string
- Required for all access to OpenClaw Control UI
- Stored only in browser localStorage (not sent over network except to gateway)
- Keep this token secure - it grants full control of OpenClaw

---

## After Pairing

Once paired, your browser will remember the token. You can then:

1. **Add OpenAI API Key**: Settings → Providers → Add → OpenAI
2. **Configure Telegram**: See [TELEGRAM_SETUP.md](TELEGRAM_SETUP.md)
3. **Start chatting**: Use the chat interface in the Control UI

---

## Get Token Again

If you lose the token or need it again:

```bash
cd /Users/ijefferson.admin/Development/agentshroud
docker compose -f docker/docker-compose.yml exec openclaw \
  printenv OPENCLAW_GATEWAY_TOKEN
```

Output:
```
YOUR_GATEWAY_PASSWORD_HERE
```
