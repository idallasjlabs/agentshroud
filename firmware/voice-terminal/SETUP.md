# ESP32-S3-BOX-3 Voice Terminal — Manual Setup Runbook

> **Status / Location note:**
> This firmware lives at `firmware/voice-terminal/` inside the AgentShroud™ repository as an
> **optional, standalone component**. It is intended to move to its own repository in a future
> sprint; this runbook is written to be self-contained so it ports cleanly.
>
> Related design document (architecture, ADRs, bring-up order):
> `docs/planning/v1.3/esp32-s3-hermes-voice-terminal.md`

---

## What you're building

```
[ESP32-S3-BOX-3]
  dual mic ──► (wake word / push-to-talk)
  speaker  ◄── (spoken reply from Hermes)
  320×240 screen ◄── animated face reacting to states
        │
        │  MicroLink (native Tailscale on-device; uses 16 MB PSRAM for TLS)
        │  plain internet — iPhone hotspot, home WiFi, hotel WiFi
        ▼
  ══ Tailscale encrypted tunnel ══════════════════════════════════════════
        │
        ▼  marvin (100.90.175.83 / marvin.tail240ea8.ts.net)
  [Voice Gateway container  :8765]
        • STT  — faster-whisper (local, no extra egress)
        • TTS  — Piper (local, no extra egress)
        • submits TEXT → POST /forward {route_to: "hermes"}
        │
        ▼
  [AgentShroud™ gateway  :8080]
        • PromptGuard  • PII redaction  • approval queue
        │
        ▼
  [Hermes agent  :8642  (agentshroud-isolated network)]
```

**Voice in, voice out, animated face:** when you speak, the BOX-3 streams audio to
the Voice Gateway on `marvin`; the gateway transcribes it, sends the text through
the AgentShroud governed path to Hermes, TTS-encodes the reply, and streams PCM back
to the BOX-3 speaker. The animated face (LVGL) reacts to states: connecting →
listening → thinking → speaking → idle. High-risk spoken commands ("delete that
file") pause for owner approval before Hermes acts — by design.

**Important:** the Tailscale tunnel, Voice Gateway, STT/TTS, and animated face are
**pending firmware/server phases**. The current firmware delivers WiFi + display
only. Sections covering pending pieces are marked **⏳ PENDING**.

---

## 1. Hardware prep

| Item | Action |
|------|--------|
| Screen protector | **Peel it off.** It covers the mic ports and muffles them. |
| USB-C cable | Use a **data** cable, not a charge-only cable. |
| Port | macOS: `/dev/cu.usbmodem5101` (native S3 USB-Serial/JTAG). |
| Power during flash | Keep the BOX-3 on USB power from the Mac while flashing. |

---

## 2. Toolchain — install ESP-IDF v5.4

> **Python constraint:** system Python on this Mac is 3.14, which ESP-IDF v5.x
> rejects. Use the `gsdl` conda environment (Python 3.11.9).
> GitHub downloads can time out under Cisco AnyConnect VPN. If a clone stalls,
> disconnect VPN for the download, then reconnect.

```bash
# Step 1 — activate conda env with Python 3.11.9
conda activate gsdl

# Step 2 — clone ESP-IDF v5.4 (one-time, ~1 GB)
mkdir -p ~/esp && cd ~/esp
git clone -b v5.4 --recursive https://github.com/espressif/esp-idf.git

# Step 3 — install toolchains for ESP32-S3
cd ~/esp/esp-idf
./install.sh esp32s3
# Installs xtensa toolchain + Python venv at:
#   ~/.espressif/python_env/idf5.4_py3.11_env

# Step 4 — activate IDF environment (do this every shell session)
. ~/esp/esp-idf/export.sh

# Step 5 — verify
idf.py --version          # expect: ESP-IDF v5.4.x
which xtensa-esp32s3-elf-gcc   # must resolve
```

---

## 3. Get the firmware

The firmware lives in the `feat/esp32-s3-hermes-voice` worktree of the AgentShroud
repository.

```bash
# If you already have the worktree checked out:
ls ~/Development/agentshroud-worktrees/esp32-s3-hermes-voice/firmware/voice-terminal/

# If you're starting fresh (separate clone):
git clone -b feat/esp32-s3-hermes-voice \
    https://github.com/<org>/agentshroud.git hermes-voice-terminal
cd hermes-voice-terminal/firmware/voice-terminal/
```

**Project layout:**

```
firmware/voice-terminal/
├── CMakeLists.txt          ← auto-applies 3 IDF v5.4 compat patches on build
├── sdkconfig.defaults      ← board + PSRAM + LVGL font config (committed)
├── partitions.csv          ← 16 MB partition table (reserve for WakeNet model)
├── main/
│   ├── app_main.c          ← state machine: WiFi, LVGL display
│   ├── CMakeLists.txt
│   ├── Kconfig.projbuild   ← CONFIG_VT_WIFI_* Kconfig definitions
│   ├── idf_component.yml   ← pins esp-box-3 v1.1.3, button <4.0.0
│   └── wifi_credentials.h  ← GITIGNORED — create from template (§4)
├── wifi_credentials.h.template  ← committed placeholder (REPLACE_ME)
└── SETUP.md                ← this file
```

---

## 4. Configure WiFi credentials

The file `main/wifi_credentials.h` is **gitignored** — never committed.
Create it from the template:

```bash
cd firmware/voice-terminal/main
cp ../wifi_credentials.h.template wifi_credentials.h
```

Then edit `wifi_credentials.h` and fill in your SSID(s) and password(s):

```c
// Primary network — e.g. your iPhone hotspot
#define CONFIG_VT_WIFI_SSID      "your-iphone-hotspot-name"
#define CONFIG_VT_WIFI_PASSWORD  "your-hotspot-password"

// Optional second network — e.g. home WiFi
#define CONFIG_VT_WIFI_SSID_2    "your-home-ssid"
#define CONFIG_VT_WIFI_PASSWORD_2 "your-home-password"
```

**iPhone hotspot notes:**
- Keep the Personal Hotspot settings screen open during the BOX-3's first connect —
  iOS naps the hotspot radio until a non-Apple device completes the handshake.
- The firmware uses `WIFI_AUTH_OPEN` threshold so it works with WPA2/WPA3 mixed-mode
  hotspots without an explicit mode selection.
- Never add the corporate network SSID — you want cellular at the office.

**Kconfig / sdkconfig note:** `sdkconfig.defaults` commits the SSID pre-set to
`ford-prefect` with a blank password. The real credentials in
`wifi_credentials.h` use `#ifndef` guards, but **sdkconfig values win over header
defaults**. If `CONFIG_VT_WIFI_SSID` appears in `sdkconfig`, that value is used
regardless of the header. After editing the header, run `idf.py reconfigure` to
ensure the header values are picked up.

---

## 5. Build · flash · monitor

```bash
# Ensure the conda+IDF env is active in this shell:
conda activate gsdl
. ~/esp/esp-idf/export.sh

cd firmware/voice-terminal

# First time (or after adding a new sdkconfig.defaults key):
idf.py reconfigure

# Build + flash + open serial monitor:
idf.py build flash monitor -p /dev/cu.usbmodem5101
# Ctrl-] to exit monitor.
```

**What to expect on success:**
```
I (312) vt: Voice terminal starting
I (344) vt: PSRAM: 15424 KB available   ← 15 MB octal PSRAM confirmed
I (356) vt: Display initialised
I (400) vt: Connecting to 'ford-prefect'...
I (8200) vt: Got IP: 192.168.x.x
I (10200) vt: Ready. Tunnel and voice streaming in next phase.
```

The screen shows:

| Phase | Top label | Bottom label |
|-------|-----------|--------------|
| Boot | "Starting…" | |
| Connecting | "Connecting to WiFi…" | your SSID |
| Connected | "WiFi connected" | IP address (28pt, legible) |
| Ready | "Hermes online" | Say "hey buddy" |

**Serial monitor triggers a USB reset:** opening the monitor briefly resets the BOX-3
via the native USB-JTAG RTS line. This is normal; the device reconnects to WiFi
in ~10 s.

---

## 5a. IDF v5.4 auto-patches (applied automatically — for reference)

`CMakeLists.txt` applies three patches before/after `include(project.cmake)` on
every build. They are idempotent and survive `idf.py fullclean`.

| # | File patched | Problem | Fix |
|---|-------------|---------|-----|
| 1 | `managed_components/espressif__esp-box-3/esp-box-3.c` | `scl_speed_hz ≠ 0` crashes touch I2C init on IDF v5.3+ | Insert `tp_io_config.scl_speed_hz = 0;` before each `esp_lcd_new_panel_io_i2c()` call |
| 2 | `managed_components/espressif__esp_codec_dev/CMakeLists.txt` | Codec links `esp_driver_i2c` (new); legacy BSP driver calls `abort()` on conflict | Replace `esp_driver_i2c` with `driver` (legacy shim) |
| 3 | (global build property) | Kconfig `CONFIG_CODEC_I2C_BACKWARD_COMPATIBLE` gate never fires without `ESP_IDF_VERSION` env var | Inject `-DCONFIG_CODEC_I2C_BACKWARD_COMPATIBLE=1` globally via `idf_build_set_property` |

Additional pin: `espressif/button: ">=3.2.0,<4.0.0"` in `idf_component.yml` — BSP
v1.1.3 uses the old button API; v4.x has breaking changes.

---

## 6. Tailscale — secure ESP→Hermes link ✅ LIVE (see docs/integrations/voice-terminal-esp32-s3.md)

> This section documents what to do **when Phase 5 firmware work begins**. No code
> changes are needed until then.

### 6a. marvin is your tailnet host

This Mac (`marvin`, `100.90.175.83`, `marvin.tail240ea8.ts.net`) is the AgentShroud
host. The BOX-3 will join the same tailnet as its own node, then connect to marvin's
Voice Gateway port over the encrypted tunnel.

### 6b. Generate an auth key for the device

1. Go to [Tailscale Admin Console → Settings → Keys](https://login.tailscale.com/admin/settings/keys)
2. Generate auth key → enable **Reusable** + **Pre-approved**, apply tag `tag:iot`
3. Copy the `tskey-auth-…` string — treat it like a password; never commit to git
4. Paste it into the firmware (§6c below); store the key in 1Password "Agent Shroud
   Bot Credentials" vault

### 6c. Add MicroLink to the firmware (SUPERSEDED — production uses Tailscale Funnel, no on-device client)

```bash
# In firmware/voice-terminal/components/ (create dir first):
mkdir -p components
cd components
git clone https://github.com/CamM2325/microlink.git
# Pin a known-good commit:
cd microlink && git checkout <commit-sha>
```

Then in `main/app_main.c`:

```c
#include "microlink.h"

static void tailscale_init(void) {
    microlink_config_t ts = {
        .auth_key     = "tskey-auth-XXXXXXXX",  // key from §6b — never commit
        .hostname     = "hermes-box3",
        .enable_psram = true,                    // mandatory — TLS needs the 16 MB PSRAM
    };
    microlink_init(&ts);
    // Success: "hermes-box3" appears in tailscale admin console
}
```

**Tuning notes (ESP32-S3 specifics):**
- Raise STUN/peer-discovery timeout (~3 s → ~6 s)
- Bind DISCO to a port separate from WireGuard's 51820 (e.g. 51821)
- Suppress the aggressive heartbeat that otherwise drops the link on mobile
- Check MicroLink's Kconfig for current option names

### 6d. Expose the Voice Gateway on marvin ✅ LIVE (`tailscale serve --bg 8765`)

The Voice Gateway (port 8765) doesn't exist yet as a container and isn't in the
Tailscale serve config. When it does:

```bash
# On marvin — add port 8765 to scripts/tailscale-serve.sh and run:
sudo scripts/tailscale-serve.sh start
```

The BOX-3 WebSocket target becomes:
`wss://marvin.tail240ea8.ts.net/voice`  (Tailscale serve terminates TLS)

### 6e. ACL lock-down (recommended)

In the Tailscale admin console, restrict `tag:iot` to only reach `marvin:8765`.
The BOX-3 should not have access to the rest of the tailnet:

```json
// tailnet policy file excerpt
{
  "acls": [
    {
      "action": "accept",
      "src":    ["tag:iot"],
      "dst":    ["marvin:8765"]
    }
  ]
}
```

---

## 7. Voice Gateway — server-side ✅ LIVE (install/config/OTA: docs/integrations/voice-terminal-esp32-s3.md)

The Voice Gateway is a Python service that will live at `voice_gateway/` in the
AgentShroud repo and run as a Docker container on `marvin`.

Responsibilities:
- Accept BOX-3 WebSocket on `/voice` (port 8765)
- Receive 16-bit PCM, mono, 16 kHz frames while button held / wake word active
- **STT** locally with `faster-whisper`
- Submit transcript: `POST http://gateway:8080/forward` with
  `{"content": "<text>", "source": "api", "content_type": "text", "route_to": "hermes"}`
- **TTS** the `agent_response` with Piper; stream PCM back to the BOX-3
- Emit state events (`{"type":"state","value":"listening"|"thinking"|"speaking"|"approval"}`)
  so the BOX-3 screen updates in real time

**Security note:** the governed `POST /forward` path passes through PromptGuard, PII
redaction, and the approval queue. Do **not** post directly to Hermes's `:8642`
endpoint — that bypasses governance. High-risk commands ("delete that file") will
pause for owner approval automatically; the BOX-3 screen will show "Awaiting approval."

---

## 8. Connect to Hermes (governed path) ✅ LIVE — Hermes is the boot-default agent

There is a **schema gap** (documented at §2.2 of the design guide): the generic
`POST /forward` payload does not match Hermes's OpenAI-compatible `/v1/chat/completions`
endpoint. The Voice Gateway must either:

- (a) The gateway router translates the generic payload → OpenAI `messages[]` body
  when the target uses an OpenAI-compatible `chat_path` (recommended; change is
  inside `gateway/proxy/router.py`); **or**
- (b) A thin `/chat` shim is added to the Hermes container

This fix must land before full governed round-trips work. Tracked in the design doc §2.2.

---

## 9. Bring-up order — one cause per failure

Follow this order; only proceed to the next step when the current one passes:

| Step | Test | Pass criteria |
|------|------|---------------|
| 1 | Display example renders | Screen shows LVGL UI, no I2C abort |
| 2 | Mic → speaker loopback | BSP mic→speaker example works |
| 3 | WiFi joins the list | IP appears in serial log + on screen |
| 4 | ⏳ MicroLink registers | `hermes-box3` visible in Tailscale admin console |
| 5 | ⏳ BOX-3 reaches marvin | `ping marvin.tail240ea8.ts.net` from BOX-3 UART |
| 6 | ⏳ Voice Gateway WS connects | WebSocket echoes a test message |
| 7 | ⏳ Governed round-trip | `POST /forward {route_to:"hermes"}` returns real `agent_response` |
| 8 | ⏳ Full loop | Wake word / button → speak → transcript on screen → spoken reply |
| 9 | ⏳ Approval path | Speak a high-risk command → screen shows "Awaiting approval" → approve → reply plays |
| 10 | ⏳ Roam test | Kill active network mid-session → device falls back, re-tunnels, WebSocket recovers without reboot |

---

## 10. Troubleshooting

### WiFi won't connect — reason=201 NO_AP_FOUND
The hotspot isn't broadcasting. Keep the iPhone Personal Hotspot screen **open**
during first connect. After the handshake completes, iOS keeps the hotspot alive.

### Boot loop — abort() in i2c.c before app_main
The three auto-patches in `CMakeLists.txt` (§5a) weren't applied. This usually
happens after `idf.py fullclean` when `managed_components/` is re-downloaded.
The patches are designed to re-run automatically; if they still fail, run
`idf.py reconfigure` and check that `CMakeLists.txt` hasn't been manually modified.

### Button component v4.x API error at build time
`idf_component.yml` pins `espressif/button: ">=3.2.0,<4.0.0"`. If the
`dependencies.lock` resolves a v4 version, delete `dependencies.lock` and rebuild.

### LVGL compile error — undefined symbol `lv_screen_active` or `.rotate` field
The BSP uses LVGL **v8.4.0**, not v9. Use `lv_scr_act()` (not `lv_screen_active()`);
there is no `rotate` field in `bsp_display_cfg_t`.

### Undeclared symbol `lv_font_montserrat_28`
Add `CONFIG_LV_FONT_MONTSERRAT_28=y` to `sdkconfig.defaults` and run
`idf.py reconfigure`. The font symbol is only compiled when the Kconfig flag is set.

### Opening serial monitor resets the device
Normal behaviour — the native USB-JTAG RTS line triggers a reset when the monitor
opens. The device reboots and reconnects to WiFi in ~10 seconds.

### sdkconfig.defaults SSID change doesn't take
The real `sdkconfig` (gitignored) wins over `sdkconfig.defaults`. After changing the
SSID/password in `wifi_credentials.h`, run `idf.py reconfigure` so the new values
are written into `sdkconfig`.

### PSRAM shows 0 KB in logs
`CONFIG_SPIRAM=y` and `CONFIG_SPIRAM_MODE_OCT=y` must be in `sdkconfig.defaults`
(they are). If PSRAM shows 0 KB after a `fullclean`, run `idf.py reconfigure` —
`sdkconfig.defaults` settings are merged into the fresh `sdkconfig`.

---

## 11. Current status (v1.2.0)

| Feature | Status | Notes |
|---------|--------|-------|
| Toolchain (ESP-IDF v5.4 + conda) | ✅ Done | `~/.espressif/python_env/idf5.4_py3.11_env` |
| 3× IDF v5.4 compat patches | ✅ Done | Auto-apply on every build via `CMakeLists.txt` |
| WiFi — roaming list + state machine | ✅ Done | Up to 2 SSIDs; retry + network-swap |
| Display — LVGL 28pt status + IP | ✅ Done | Montserrat 28, 320×240, legible |
| PSRAM — 16 MB octal | ✅ Done | 15424 KB available at runtime |
| Tailscale Funnel transport | ✅ Done | `wss://marvin.tail240ea8.ts.net/voice` port 443; works on cellular |
| Voice Gateway container on marvin | ✅ Done | FastAPI, port 8765; `docker --profile voice` |
| STT (faster-whisper base.en) | ✅ Done | `/opt/whisper/base.en`; `run_in_executor` (non-blocking) |
| TTS (Piper en_US-lessac-medium) | ✅ Done | 22050→16000 Hz resample; chunked streaming |
| Agent routing via `POST /forward` | ✅ Done | `?agent=hermes/direct/openclaw`; full security pipeline |
| Runtime agent toggle button | ✅ Done | BSP_BUTTON_MUTE cycles agents; label shown top-left |
| Animated face reacting to states | ✅ Done | IDLE / LISTENING / THINKING / SPEAKING / DISCONNECTED |
| Auto-follow-up listen window | ✅ Done | 8 s VAD timeout after TTS; tap-to-talk UX fix |
| "Hi, ESP" WakeNet wake word | ✅ Done | WN9 model in `model` SPIFFS partition |
| OpenClaw async notice | ✅ Done | Spoken Telegram-redirect; no fake reply |
| LVGL 8.4 → 9.5 upgrade | ✅ Done | PR #241 — 6 API renames, BSP 3.2.0, Kconfig cleanup |
| Kawaii animated face | ✅ Done | PR #242 — lvgl_kawaii_face submodule; face_set_emotion() |
| OTA wireless firmware updates | ✅ Done | PR #243 — HEAD ETag check + GET streaming via voice gateway |
| Bootloader rollback (anti-brick) | ✅ Done | PR #243 — auto-revert if new image doesn't mark itself valid |

### Credentials file

`wifi_credentials.h` is **gitignored and never committed**. It lives at
`firmware/voice-terminal/main/wifi_credentials.h` and contains:

```c
#define CONFIG_VT_WIFI_SSID      "your-ssid"
#define CONFIG_VT_WIFI_PASSWORD  "your-password"
// Optional second network (leave empty to disable):
#define CONFIG_VT_WIFI_SSID_2    ""
#define CONFIG_VT_WIFI_PASSWORD_2 ""
// Voice Gateway auth token (64-char hex, must match docker/secrets/voice_gateway_token.txt):
#define CONFIG_VT_VG_WS_TOKEN    "your-64-char-token"
```

The token must match `docker/secrets/voice_gateway_token.txt` on marvin. Generate once with:
```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

### Agent toggle — runtime button

- **BSP_BUTTON_MUTE** (top-right physical button on the BOX-3) cycles the active agent.
- The on-screen label (top-left, blue) shows the current agent name.
- Cycling is safe to do at any time when not mid-utterance.
- The WebSocket reconnects automatically with the new `?agent=<slug>` parameter.

### Adding a future agent

1. Add an entry to `agentshroud.yaml bots:` on marvin.
2. Add a row to `VT_AGENTS[]` in `firmware/voice-terminal/main/app_main.c`.
3. Rebuild firmware (`idf.py build`) and redeploy the voice gateway.
4. No voice-gateway code change needed — routing is data-driven.

---

## 12. OTA Wireless Firmware Updates

All future firmware changes push wirelessly — no USB required after the one-time
bootstrap below. The flow: build on marvin → redeploy voice-gateway → reboot ESP
→ device downloads the new binary and reflashes itself.

### How it works

On every boot, after WiFi connects, the firmware:
1. Sends `HEAD https://marvin.tail240ea8.ts.net/firmware/bin?token=<VG_TOKEN>` to the
   voice gateway (same Tailscale Funnel path as WebSocket; no new infra).
2. Compares the `ETag` (SHA-256 of the binary) against the value stored in NVS.
3. **Match → skip.** Logs `Firmware current` and continues normal boot in <1 s.
4. **Mismatch → update.** Streams the GET response into the inactive OTA partition
   (`ota_0` ↔ `ota_1`), switches the boot partition, and restarts.
5. After the first successful WebSocket connect, marks the new image valid
   (`esp_ota_mark_app_valid_cancel_rollback`). If the device crashes before this
   point, the bootloader automatically reverts to the previous working slot —
   a bad OTA update **cannot brick the device**.

### One-time bootstrap (USB flash — do this when back at marvin)

This procedure is required exactly once because the partition table changed to add
the second OTA slot. After it, every update is wireless.

**Prerequisites:**
- BOX-3 connected to marvin via a **data** USB-C cable (charge-only cables won't work)
- `conda activate gsdl && . ~/esp/esp-idf/export.sh` active in your shell
- Voice gateway deployed and healthy (`curl http://localhost:8765/health`)

```bash
cd ~/Development/agentshroud

# 1. Pull the merged OTA firmware (PR #243)
git checkout main && git pull

# 2. Pick up new sdkconfig.defaults key (CONFIG_BOOTLOADER_APP_ROLLBACK_ENABLE)
cd firmware/voice-terminal
idf.py reconfigure

# 3. Clean build (partition table changed — must start fresh)
rm -rf build
idf.py build
# Expect: voice_terminal.bin  ~1.9 MB  (build/voice_terminal.bin)

# 4. Redeploy voice gateway so /firmware/bin endpoint goes live
cd ~/Development/agentshroud
docker-compose -f docker/docker-compose.yml -p agentshroud up -d voice-gateway

# 5. Smoke-test the endpoint (substitute your actual token)
TOKEN=$(cat docker/secrets/voice_gateway_token.txt)
curl -sI "http://localhost:8765/firmware/bin?token=$TOKEN"
# Expect: HTTP/1.1 200 OK  +  ETag: "sha256hex..."
curl -sI "http://localhost:8765/firmware/bin"
# Expect: HTTP/1.1 401 Unauthorized  (token required)

# 6. Find the USB port (BOX-3 must be powered on and connected)
ls /dev/cu.usbmodem*
# Typical: /dev/cu.usbmodem3101  or  /dev/cu.usbmodem5101

# 7. Flash and watch the first boot
cd firmware/voice-terminal
idf.py flash monitor -p /dev/cu.usbmodem3101
# (replace port with the one found in step 6)
```

**Expected first-boot serial output:**
```
I (vt_ota) OTA HEAD → https://marvin.tail240ea8.ts.net/firmware/bin
I (vt_ota) Remote ETag: "a3f7c..."
I (vt_ota) ETag mismatch — starting OTA download     ← first boot: NVS is empty
I (vt_ota) Downloaded 1892352 bytes
I (vt_ota) OTA complete — rebooting into new firmware
... (reboots into ota_1) ...
I (vt_ota) Remote ETag: "a3f7c..."
I (vt_ota) Firmware current                           ← ETag now in NVS, matches
I (vt)     Ready. Voice terminal active → agent: Hermes
```

> **Why two downloads on first boot?** After a USB flash, NVS is empty — no stored
> ETag — so the first boot downloads the same binary into `ota_1`. After that reboot,
> the ETag is in NVS and subsequent boots skip the download.

Press `Ctrl-]` to exit the monitor. The device is now OTA-capable.

### Ongoing update workflow (no USB ever again)

```bash
# After any code change in firmware/voice-terminal/main/:
cd ~/Development/agentshroud

# 1. Build
cd firmware/voice-terminal && idf.py build

# 2. Redeploy gateway (re-mounts new binary → new SHA-256 ETag)
cd ~/Development/agentshroud
docker-compose -f docker/docker-compose.yml -p agentshroud up -d voice-gateway

# 3. Trigger update — either:
#    a. Power-cycle the BOX-3 (unplug/replug USB-C or remove batteries)
#    b. Press the physical reset button on the back of the BOX-3
# The device will detect the ETag mismatch and self-update.
```

Watch the serial monitor (if connected) or just wait ~30 s — the BOX-3 will show its
face disappear briefly, reboot, and come back online with the new firmware.

### Troubleshooting OTA

| Symptom | Cause | Fix |
|---------|-------|-----|
| `/firmware/bin` returns 404 | Build not mounted | Run `idf.py build` first, then redeploy gateway |
| `/firmware/bin` returns 401 | Wrong or missing token | Check `?token=` matches `docker/secrets/voice_gateway_token.txt` |
| `OTA HEAD failed: err=… http=0` | No network / Funnel down | Check WiFi, Tailscale, `curl https://marvin.tail240ea8.ts.net/health` |
| Boot loop after OTA update | Bad firmware (no mark_valid) | Bootloader auto-reverts to previous slot after 2nd failed boot |
| NVS ETag stale after flash erase | `idf.py erase-flash` clears NVS | Normal — first boot re-downloads; resolves itself |
| `OTA: no update partition` in log | Old single-slot partition table | Must USB-flash the new partitions.csv (one-time bootstrap, §12 above) |

---

## Quick-reference commands

```bash
# Activate build environment (run once per shell)
conda activate gsdl && . ~/esp/esp-idf/export.sh

# Build only
idf.py build

# Build + flash + monitor (USB required; replaces OTA for partition table changes)
idf.py build flash monitor -p /dev/cu.usbmodem3101

# Reconfigure (pick up new sdkconfig.defaults keys — always run after git pull)
idf.py reconfigure

# Erase flash (clean slate — also clears NVS OTA ETag; first boot will re-download)
idf.py erase-flash -p /dev/cu.usbmodem3101

# Serial monitor only (device already flashed)
idf.py monitor -p /dev/cu.usbmodem3101

# Monitor firmware size
idf.py size-components

# ── OTA update (no USB) ───────────────────────────────────────────────────────
# Make code changes, then:
idf.py build
docker-compose -f ~/Development/agentshroud/docker/docker-compose.yml \
    -p agentshroud up -d voice-gateway
# Power-cycle BOX-3 — it will detect ETag mismatch and self-update (~30 s)

# Smoke-test the firmware endpoint on marvin
TOKEN=$(cat ~/Development/agentshroud/docker/secrets/voice_gateway_token.txt)
curl -sI "http://localhost:8765/firmware/bin?token=$TOKEN"   # 200 + ETag
curl -sI "https://marvin.tail240ea8.ts.net/firmware/bin?token=$TOKEN"   # Funnel path
```

---

*AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. — federal registration pending.*
