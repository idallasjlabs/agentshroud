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
                            STT (faster-whisper small.en)
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

#### Voice-gateway configuration (env vars, set in `docker/docker-compose.yml`)

| Variable | Default | Purpose |
|----------|---------|---------|
| `VOICE_DEFAULT_AGENT` | `hermes` | Agent used when the device supplies no `?agent=` param |
| `VOICE_MODEL` | `claude-haiku-4-5-20251001` | LLM for the `direct` fast path only |
| `WHISPER_MODEL_SIZE` | `small.en` | faster-whisper STT model (pre-baked in the image) |
| `KOKORO_VOICE` | `af_bella` | Kokoro TTS voice (falls back to `af_heart` if the pack is missing) |
| `KOKORO_SPEED` | `0.92` | TTS speaking rate (1.0 = native) |
| `VG_TTS_HEADROOM` | `0.75` | Digital gain applied to TTS samples (clipping guard) |
| `VG_TTS_SENTENCE_TIMEOUT_S` | `30` | Per-sentence synthesis budget — a wedged synth can't strand the device in THINKING |
| `VG_AGENT_READ_TIMEOUT_S` | `100` | Max wait for an agent reply before the spoken fallback |
| `FIRMWARE_BIN_PATH` | `/firmware/build/voice_terminal.bin` | OTA binary path (bind-mounted, see **Updating the firmware**) |
| `HF_HUB_OFFLINE` | `1` | Never download voice packs at runtime (VPN-proof) |

The container needs `mem_limit: 4g` (Whisper + Kokoro resident) and belongs to both
`agentshroud-internal` and `agentshroud-isolated` networks.

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

## Updating the firmware (OTA — the normal deploy path)

After the first USB flash the device updates **over the air**; no cable needed
for routine builds. The voice-gateway container serves a **promoted** build:
`docker-compose.yml` bind-mounts `firmware/voice-terminal/ota-release/` (NOT
`build/`) read-only at `/firmware/build`, and `GET /firmware/bin` serves
`voice_terminal.bin` with a SHA-256 `ETag`. On every boot the device compares
that ETag against its running partition and, if it differs, downloads,
self-flashes the inactive OTA slot, and reboots into it (with automatic
bootloader rollback if the new image fails to boot).

> **Changed 2026-07-27** — this used to bind-mount `build/` directly, so any
> local `idf.py build` immediately became what the one physical production
> device downloaded next, with no verification step at all. A one-line
> sdkconfig change (an untested WS-URL/port change, never boot-tested on real
> hardware) went out this way, crashed early enough that the device never
> reached `esp_ota_mark_app_valid_cancel_rollback()`, and could not self-heal:
> its own OTA-check endpoint used the same broken address as its WS
> connection, so it could not even download a fix. `scripts/promote-firmware.sh`
> is now the *only* path from `build/` to what devices actually see, and it
> requires typing a confirmation that five specific things were verified over a
> real USB serial connection first (see the script for the checklist). **Never
> bypass this for anything that changes network config, WiFi credentials, or
> anything else that affects whether the device can reach the network at
> all** — those are exactly the changes that can strand a device with no
> remaining recovery path if they're wrong.

Deploy procedure:

```bash
cd firmware/voice-terminal
source ~/esp/esp-idf/export.sh

# 1. Bump the build tag — the ONLY reliable build identifier
#    (esp_app_desc compile stamps go stale across rebuilds):
#    edit main/app_main.c → #define VT_BUILD_TAG "<something-new>"

# 2. Build, and verify by EXIT CODE (never by grepping output):
idf.py build; echo "exit: $?"

# 3. Boot-test over USB BEFORE promoting — non-negotiable for any change that
#    touches network/WiFi/URL config (see warning above). For pure-firmware-
#    logic changes with no network-reachability impact, this is still strongly
#    recommended, just less critical:
idf.py -p /dev/cu.usbmodemXXXX flash monitor
#    Confirm: boots cleanly, WiFi connects, reaches "mark_app_valid" (implicit —
#    no crash/reset before the voice WS connects), a real voice round-trip works.
#    Ctrl-] to exit monitor.

# 4. Only after that passes, promote it to what OTA actually serves:
cd ../..   # repo root
scripts/promote-firmware.sh
#    Requires typing VERIFIED to confirm the checklist above was actually done.

# 5. Power-cycle the device (or wait for its next natural reboot).

# 6. Confirm the device is running the new build:
docker logs agentshroud-voice-gateway --tail 100 | grep "boot: tag="
#    → [device …] boot: tag=<something-new> …
```

Notes:
- The device's serial console is unavailable in normal operation *while it's
  running network-connected* — the diagnostic trace above is mirrored over the
  WebSocket: watch `docker logs -f agentshroud-voice-gateway` for `[device …]`
  lines (boot marker, VAD endpoints, delivery attempts, errors). But that
  mirror *only works once the device can reach the network* — it is useless
  for diagnosing exactly the failure mode (network-breaking firmware) that
  matters most, which is why step 3's real USB boot-test cannot be skipped.
- A build that fails to boot cleanly (crashes/resets before reaching the voice
  WS connection) safely rolls back via the bootloader to the previous slot —
  **but only if the currently-running image can still reach `/firmware/bin`
  to fetch a fix.** If the previous slot's own baked network config is what's
  broken (not just the new one), there is no remaining OTA recovery path at
  all and USB is required. This is exactly what happened 2026-07-27: don't
  assume "rollback is automatic" means "network config changes are safe to
  OTA" — they are the one category of change rollback cannot fully protect
  against.
- Never change the BSP I2S DMA descriptor sizing — it exhausts internal DMA RAM
  and the image will not boot (proven 2026-07-07).

---

## Usage

### Wake word

Say **"Hi, ESP"** — the display enters LISTENING state.

### Tap to talk

Tap anywhere on the touchscreen — same as the wake word.
- **Tap, then speak**: the utterance ends automatically ~0.8 s after you stop
  speaking (VAD silence endpointing; 15 s server-side safety cap)
- **Tap while LISTENING**: ends the utterance immediately
- **Tap while SPEAKING**: stops playback (server aborts the rest of the reply)

### Voice volume

Say **"set volume &lt;X&gt; percent"** (0–100, digits or words — "set volume
eighty percent"). Chained commands work: *"Set volume 80. What time is it?"*
applies the volume AND answers the question. The level persists across reboots
and is mapped onto the codec's distortion-free range; changes ramp smoothly.

> Audio quality note: the BOX-3 speaker faithfully reproduces USB supply noise.
> If replies click or crackle on every word, **swap the charger first** — use a
> dedicated 2 A+ wall brick, never a laptop/hub/monitor USB port.

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
| STT produces empty transcript | Too much background noise / very short utterance | Speak closer; speak for at least ~0.3 s. |
| Clicking/static on every word | **Noisy USB power supply** (WiFi bursts modulate the rail; mimics firmware bugs) | Swap to a dedicated 2 A+ wall charger. Check power BEFORE touching playback code. |
| TTS reply is silent / device wedged in THINKING | Kokoro voice pack missing (blocked download) | `HF_HUB_OFFLINE=1` + `af_heart` fallback should prevent this; check `docker logs agentshroud-voice-gateway` for synthesis timeouts. |
| Long THINKING on hotspot | Upload retries over a lossy link | Normal: watch `delivery n/5` + `LISTEN resume at <offset>` lines — resume sends only the un-delivered tail. |
| Spoken "I'm having trouble connecting" | Agent exceeded `VG_AGENT_READ_TIMEOUT_S` (100 s) | Retry; if persistent check `docker logs agentshroud-gateway` for `Timeout forwarding to hermes`. |
| Reply audio starts a few seconds after THINKING ends | By design | Playback is END-gated: the whole reply is buffered before the speaker starts, so audio never competes with TLS receive. |
| OpenClaw spoken but no Telegram reply | OpenClaw container down | `docker logs agentshroud-openclaw` |
| Hermes takes > 30 s | Hermes making web search calls | Expected for agentic tasks; `direct` is faster for simple Q&A. |
| Device trace needed (no USB) | — | `docker logs -f agentshroud-voice-gateway` — all `[device …]` lines are the firmware's remote-diag mirror. |

---

## Success pattern — `docker logs agentshroud-voice-gateway`

```
… | [device …] boot: tag=playdrive-0707m fw=… reset=1 tts_buf=1048576 (remote-diag online)
… | [device …] VAD endpoint: speech=1312ms silence=800ms — ending
… | [device …] delivery 1/5: dropped at 135168/258048 bytes — retrying   ← lossy link, normal
… | LISTEN resume at 126976 (126976 cached bytes) from …                 ← resume, not restart
… | Transcript: 'What time is it?'
… | Agent reply: "It's Tuesday, July 07, 2026 at 1:24 PM EDT."
… | [device …] utterance DELIVERED: 258048 bytes (attempt 2)
```

A healthy turn: VAD endpoint ~0.8 s after you stop speaking → delivery (with
resume retries on a lossy link) → transcript → agent reply → the device buffers
the full TTS reply, then plays it with the radio quiet. Follow-ups require a
tap or "Hi, ESP" (auto-listen is disabled — no echo cancellation on-device).

---

*AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. — USPTO Serial No. 99728633.*
*Patent Pending — U.S. Provisional Application No. 64/018,744.*
