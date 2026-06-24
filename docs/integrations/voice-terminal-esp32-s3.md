# Voice Terminal — ESP32-S3-BOX-3 (Optional AgentShroud Add-On)

> **AgentShroud™** — USPTO Serial No. 99728633 · Patent Pending No. 64/018,744

The Voice Terminal turns an [Espressif ESP32-S3-BOX-3](https://github.com/espressif/esp-box)
into a physical voice control surface for any agent proxied by AgentShroud. Say "Hi, ESP" or
tap the touchscreen, speak naturally, and hear the agent's reply through the built-in speaker —
all routed through AgentShroud's full security pipeline (PII redaction, prompt-guard, audit
hash-chain, egress policy).

---

## Architecture

```
ESP32-S3-BOX-3
  Wake word / PTT ──► PCM WebSocket (wss://marvin.tail240ea8.ts.net/voice)
                                        │
                              voice-gateway (port 8765)
                                        │
                            STT (faster-whisper base.en)
                                        │
                              POST /forward?route_to=<agent>
                                        │
                         AgentShroud Gateway security pipeline
                           (PII · prompt-guard · audit · egress)
                                        │
                              ┌─────────────────┐
                              │ Hermes (sync)   │  spoken reply via TTS
                              │ direct (sync)   │  low-latency LLM proxy
                              │ OpenClaw (async)│  reply on Telegram
                              └─────────────────┘
```

The ESP and voice-gateway communicate over Tailscale Funnel (public TLS on port 443).
This means the voice terminal works identically on the home LAN, a phone hotspot, or
any internet connection — no VPN client needed on the device.

---

## Prerequisites

| Requirement | Version | Notes |
|-------------|---------|-------|
| ESP32-S3-BOX-3 | any hardware rev | BSP v1.1.3 |
| ESP-IDF | v5.4 | `~/esp/esp-idf` |
| Conda environment | `gsdl` | includes `xtensa-esp32s3-elf` |
| Docker (colima or CE) | latest | for voice-gateway container |
| Tailscale Funnel | enabled on marvin | `tailscale serve --bg 8765` |
| AgentShroud core stack | v1.2.0+ | gateway + Hermes must be running |

---

## Installation

### 1. Generate the voice gateway token

```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
# → <64-char hex string>
```

Save this as `docker/secrets/voice_gateway_token.txt` on marvin (never commit it).

### 2. Create `wifi_credentials.h`

In `firmware/voice-terminal/main/` create `wifi_credentials.h` (this file is gitignored):

```c
// firmware/voice-terminal/main/wifi_credentials.h
// NEVER COMMIT — gitignored.
#define CONFIG_VT_WIFI_SSID       "your-primary-ssid"
#define CONFIG_VT_WIFI_PASSWORD   "your-primary-password"
// Second network (leave empty strings to disable):
#define CONFIG_VT_WIFI_SSID_2     "your-hotspot-ssid"
#define CONFIG_VT_WIFI_PASSWORD_2 "your-hotspot-password"
// Must match docker/secrets/voice_gateway_token.txt on marvin:
#define CONFIG_VT_VG_WS_TOKEN     "your-64-char-token-here"
```

### 3. Start the voice gateway

```bash
# From the repo root on marvin:
docker-compose -f docker/docker-compose.yml -p agentshroud --profile voice up -d voice-gateway

# Verify:
curl http://localhost:8765/health   # → {"status":"ok"}
```

### 4. Enable Tailscale Funnel

```bash
tailscale serve --bg 8765
# → Available at wss://marvin.tail240ea8.ts.net/voice
```

Verify the public endpoint (from any external machine):
```bash
curl https://marvin.tail240ea8.ts.net/health   # → {"status":"ok"}
```

### 5. Build and flash the firmware

```bash
cd firmware/voice-terminal
conda activate gsdl
source ~/esp/esp-idf/export.sh   # sets up xtensa toolchain

# First time only — full build:
idf.py build

# Flash to the BOX-3 (connect USB-C, find port):
ls /dev/cu.usb*
idf.py -p /dev/cu.usbmodem<XXXX> flash monitor
```

The firmware will:
1. Connect to WiFi (tries primary SSID first, then secondary on failure)
2. Open a TLS WebSocket to `wss://marvin.tail240ea8.ts.net/voice?token=<TOKEN>&agent=hermes`
3. Show the animated face and "Hermes" label in the top-left corner

---

## Usage

### Wake word

Say **"Hi, ESP"** — the display enters LISTENING state.

### Tap to talk

Tap anywhere on the touchscreen — same as the wake word.
- **Short tap** (< 1 s): stays in LISTENING; speak after lifting finger (8 s VAD timeout)
- **Long press** (≥ 1 s): ends the utterance when you release

### Physical button (top button — BSP_BUTTON_MAIN)

Same as touchscreen PTT.

### Agent toggle (MUTE button — BSP_BUTTON_MUTE)

Press the MUTE button to cycle through agents at runtime:

| Agent label | `?agent=` slug | Behaviour |
|-------------|---------------|-----------|
| **Hermes** (default) | `hermes` | Hermes agentic assistant — full tools (web search, memory, skills), synchronous spoken reply |
| **Fast LLM** | `direct` | Gateway LLM proxy (Claude Haiku) — low-latency, no agentic tools, multi-turn context |
| **OpenClaw** | `openclaw` | OpenClaw Telegram bot — async; message is forwarded and "OpenClaw received your message and will reply on Telegram" is spoken |

The active agent name is shown in the top-left of the face display (blue text).

The device reconnects automatically with the new `?agent=` query parameter — no reflash needed.

### Adding a future agent

1. Add the agent to `agentshroud.yaml bots:` on marvin.
2. Add an entry to `VT_AGENTS[]` in `firmware/voice-terminal/main/app_main.c`:
   ```c
   { "myagent", "MyAgent" },
   ```
3. Rebuild and reflash: `idf.py build && idf.py flash`
4. No voice-gateway server change needed.

---

## Security notes

- The `?token=` query parameter is a 64-character random hex string. It authenticates
  the device to the voice gateway. Keep `wifi_credentials.h` and
  `docker/secrets/voice_gateway_token.txt` secret — never commit them.
- All voice traffic routes through AgentShroud's security pipeline. Utterances are
  PII-redacted before reaching any agent.
- The voice gateway runs on the `agentshroud-internal` + `agentshroud-isolated` Docker
  networks. Its only outbound path to agents is via `gateway:8080`.
- Hermes and future agents see `source:"api"` with `user_id` set to the owner Telegram
  UID — requests carry full RBAC identity through the pipeline.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| ESP shows "Reconnecting…" for > 60 s | DNS resolution of `*.ts.net` slow on first boot | Wait; it will retry. First attempt often fails (~22 s cycle). |
| Token rejected (WS closes immediately) | Token mismatch | Check `wifi_credentials.h` matches `docker/secrets/voice_gateway_token.txt` exactly. |
| STT produces empty transcript | Too much background noise / very short utterance | Speak closer; hold the button for > 1 s before speaking. |
| TTS reply is silent | Piper model not found | Check `PIPER_MODEL` env var in docker-compose points to `.onnx` file. |
| OpenClaw spoken but no Telegram reply | OpenClaw container down | `docker logs agentshroud-openclaw` |
| Hermes takes > 30 s | Hermes making web search calls | Expected for agentic tasks; `direct` is faster for simple Q&A. |

---

## Firmware serial log — success pattern

```
I (5432) vt: WiFi connected — IP 192.168.x.y
I (6891) vt: Connecting to voice gateway: wss://marvin.tail240ea8.ts.net/voice?token=...
I (28764) wsc: WebSocket connected
I (28764) vt: Ready. Voice terminal active → agent: Hermes
I (28764) ui_face: Agent label → Hermes
W (31000) wakeword: WakeNet: 'Hi, ESP' detected
I (31100) vt: Utterance started
I (31450) vt: Utterance ended
I (32100) voice_gateway.server: Transcript: 'what time is it'
I (34200) voice_gateway.server: Agent reply: 'It is 2:15 PM Eastern time.'
I (36300) vt: TTS playback complete → auto-listen window open
```

---

*AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. — USPTO Serial No. 99728633.*
*Patent Pending — U.S. Provisional Application No. 64/018,744.*
