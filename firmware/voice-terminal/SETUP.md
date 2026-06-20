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

## 6. Tailscale — secure ESP→Hermes link ⏳ PENDING (Phase 5)

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

### 6c. Add MicroLink to the firmware ⏳

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

### 6d. Expose the Voice Gateway on marvin ⏳

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

## 7. Voice Gateway — server-side ⏳ PENDING (Phase 5)

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

## 8. Connect to Hermes (governed path) ⏳ PENDING

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

## 11. Current status

| Feature | Status | Notes |
|---------|--------|-------|
| Toolchain (ESP-IDF v5.4 + conda) | ✅ Done | `~/.espressif/python_env/idf5.4_py3.11_env` |
| 3× IDF v5.4 compat patches | ✅ Done | Auto-apply on every build via `CMakeLists.txt` |
| WiFi — roaming list + state machine | ✅ Done | Up to 2 SSIDs; retry + network-swap |
| Display — LVGL 28pt status + IP | ✅ Done | Montserrat 28, 320×240, legible |
| PSRAM — 16 MB octal | ✅ Done | 15424 KB available at runtime |
| Tailscale on-device (MicroLink) | ⏳ Pending | Phase 5 |
| Voice Gateway container on marvin | ⏳ Pending | Phase 5 |
| STT (faster-whisper) | ⏳ Pending | Phase 5 |
| TTS (Piper) | ⏳ Pending | Phase 5 |
| Governed-path schema fix (§2.2) | ⏳ Pending | `gateway/proxy/router.py` |
| Animated face reacting to states | ⏳ Pending | Phase 5 (LVGL state machine) |
| "hey buddy" WakeNet model | ⏳ Pending | After Phase 5; push-to-talk in interim |

---

## Quick-reference commands

```bash
# Activate build environment (run once per shell)
conda activate gsdl && . ~/esp/esp-idf/export.sh

# Build only
idf.py build

# Build + flash + monitor
idf.py build flash monitor -p /dev/cu.usbmodem5101

# Reconfigure (pick up new sdkconfig.defaults keys)
idf.py reconfigure

# Erase flash (clean slate)
idf.py erase-flash -p /dev/cu.usbmodem5101

# Serial monitor only (device already flashed)
idf.py monitor -p /dev/cu.usbmodem5101

# Monitor firmware size
idf.py size-components
```

---

*AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. — federal registration pending.*
