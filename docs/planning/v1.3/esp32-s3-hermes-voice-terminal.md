# ESP32-S3-BOX-3 Voice Terminal for Hermes (behind AgentShroud)

**Status:** Draft (2026-06-18) · planning + device setup guide · branch `feat/esp32-s3-hermes-voice`
**Device:** Espressif ESP32-S3-BOX-3 (Mouser 356-ESP32-S3-BOX-3) — ESP32-S3, 16 MB flash, 16 MB octal PSRAM, 2.4" 320×240 touch, dual mic, speaker, USB-C
**Server / tailnet host:** `marvin` (`marvin.tail240ea8.ts.net`) — the host already running Hermes behind the AgentShroud gateway
**Wake word target:** "hey buddy" (custom WakeNet model — see §9)

---

## 1. Why this differs from a generic ESP32+Hermes build

Hermes here is **not** a standalone agent — it runs in Docker on `agentshroud-isolated`,
reachable only through the AgentShroud gateway. Every governed inbound message and every
outbound action is policy-enforced. The voice terminal must respect that, so the design is:

```
[BOX-3: mic + 320×240 screen + speaker]
   └─ MicroLink (native Tailscale client on-device; uses the 16MB PSRAM for TLS)
        │  plain internet (iPhone/iPad hotspot · home/hotel WiFi)
   ─── Tailscale encrypted tunnel ───
        │
[marvin  (tailnet 100.x, tailscale serve)]
   ├─ Voice Gateway container        ← BOX-3 WebSocket terminates here
   │     • STT (faster-whisper, local)   • TTS (Piper, local)
   │     • posts TEXT to the GOVERNED gateway endpoint, reads the reply
   │
   └─ AgentShroud gateway :8080
        • POST /forward {route_to: "hermes"}  → PromptGuard + PII + approval queue
        → Hermes (agentshroud-isolated, OpenAI-compatible API :8642)
```

Two settled decisions and the AgentShroud-specific reasons:

- **The tunnel runs on the BOX-3, not the phone.** An iPhone/iPad hotspot does not route its
  clients through the phone's VPN, so encryption must terminate on-device. The BOX-3's octal
  PSRAM makes MicroLink's TLS feasible. The BOX-3 becomes its own tailnet node and reaches
  `marvin` over the tailnet from any network.
- **The BOX-3 talks to a Voice Gateway, never raw to Hermes.** Hermes has no audio endpoint,
  and we want voice commands to pass through governance. The Voice Gateway owns the WebSocket,
  does STT/TTS, and submits **text** to the governed `POST /forward` path so PromptGuard, PII
  redaction, and the approval queue all apply.

---

## 2. Server-side work this branch must implement

These are the code/config tasks that live on `feat/esp32-s3-hermes-voice`. The device setup
(§6–§11) assumes they are done.

### 2.1 New `voice_gateway/` service
- New top-level service dir `voice_gateway/` (own `Dockerfile` from `python:3.13-slim`, non-root
  UID 1000, start script in `docker/scripts/`), mirroring the `gateway/` Dockerfile pattern.
  Code style follows existing `gateway/proxy/*` WebSocket services (`slack_socket_client.py`,
  `canvas_proxy.py`).
- Responsibilities:
  - Accept the BOX-3 WebSocket (default `:8765`, path `/voice`).
  - Receive 16-bit PCM, mono, 16 kHz frames while the device button is held; end-of-utterance on release.
  - **STT** locally with `faster-whisper` (CPU-friendly; GPU optional).
  - **Submit text to the governed pipeline:** `POST http://gateway:8080/forward`
    with `{"content": "<transcript>", "source": "api", "content_type": "text",
    "route_to": "hermes"}` and the gateway `Authorization` token. Read `agent_response`
    from the `ForwardResponse` (`gateway/ingest_api/routes/models.py:100`).
  - **TTS** the reply locally with Piper; stream PCM back down the WebSocket.
  - Emit state events (`state`, `transcript`, `tts`) for the screen state machine (§6.5).

### 2.2 Close the governed-path schema gap for Hermes  ⚠️ required
- `POST /forward` with `route_to: hermes` routes via `MultiAgentRouter.forward_to_agent`
  (`gateway/proxy/router.py:155`), which POSTs AgentShroud's generic
  `{content, ledger_id, source, content_type, metadata}` to the target's `chat_path`.
- Hermes's `chat_path` is `/v1/chat/completions` (`agentshroud.yaml:137`) — the **OpenAI** body
  shape. So the generic payload does not match what Hermes expects on that path.
- **Fix (pick one, implement + test):**
  - (a) Teach the router to translate the generic payload → OpenAI `messages[]` shape when the
    target is an OpenAI-compatible bot (detectable from `chat_path`), and parse the
    `choices[0].message.content` back into `agent_response`; **or**
  - (b) Add a thin `/chat` shim to the Hermes container that accepts the generic payload and
    proxies to its own `:8642/v1/chat/completions`, then set Hermes `chat_path: /chat`.
- This is the single most important integration task — without it the governed path returns
  malformed replies for Hermes (it works today only for OpenClaw's `/chat`). Do **not** paper
  over it by falling back to the bypass path (§2.4).

### 2.3 Compose + tailnet exposure
- Add a `voice-gateway` service to `docker/docker-compose.yml` mirroring the `hermes` block:
  on `agentshroud-isolated`, `HTTP(S)_PROXY=http://gateway:8181`, `depends_on gateway healthy`,
  `mem_limit`, healthcheck on `/health`. STT/TTS models baked into the image or mounted via a
  named volume.
- Publish the WebSocket to the host loopback through the gateway forwarder pattern
  (`127.0.0.1:8765`), then expose on the tailnet by adding port `8765` to
  `scripts/tailscale-serve.sh` (it already serves 8080/18789/9119/8642).

### 2.4 Egress & governance — what does NOT change
- **No new egress allowlist entries** for local STT/TTS — the Voice Gateway only talks to
  `gateway:8080` internally and to local model files.
- Tailscale tunnel traffic from the BOX-3 terminates at the host `tailscaled`, **not** through
  the AgentShroud HTTP proxy, so `gateway/security/egress_config.py` needs no Tailscale domains.
- If you ever switch to **cloud** STT/TTS: `api.openai.com` is already allowlisted
  (`gateway/security/egress_config.py:33`); add others to `PERMANENT_EGRESS_DOMAINS` the same
  way PRs #154/#190 did.
- **Approval queue is automatic on the governed path:** a voice command whose detected action is
  `execute_command`/`delete_file`/`admin_action`/`install_package` routes to human approval at
  `gateway/proxy/pipeline.py:716`; tool-tier `critical`/`high` actions gate via
  `gateway/approval_queue/enhanced_queue.py:111`. Plain conversation forwards. This means
  "delete that file" spoken to the box will page you for approval — by design.

### 2.5 Tests (CLAUDE.md §4, coverage gate `fail_under=84`)
- `gateway/tests/test_voice_gateway.py` — STT stub → `/forward` POST shape → TTS frame emission,
  using deterministic fixtures (no real audio models, no network — mock the gateway HTTP call).
- A regression test asserting the §2.2 translation produces a valid OpenAI body for Hermes and
  parses the reply.

---

## 3. Tailscale changes

1. Use your existing tailnet (free tier is fine). `marvin` is already a node.
2. Generate a **reusable, pre-approved** auth key for the device:
   Admin console → Settings → Keys → Generate auth key → enable **Reusable** + **Pre-approved**,
   tag it `tag:iot`. Copy the `tskey-auth-…` string (treat as a password) — it goes into the
   firmware, not into a server-side Docker secret (the device authenticates itself).
3. **ACL lock-down (recommended):** restrict `tag:iot` to only `marvin:8765` (the Voice Gateway
   serve port) — nothing else on the tailnet.
4. Confirm `marvin` serves the WS port: `scripts/tailscale-serve.sh` includes `8765`, and
   `scripts/tailscale-check.sh` shows it. Device target becomes
   `wss://marvin.tail240ea8.ts.net/voice` (tailscale serve terminates TLS).

## 4. iPhone & iPad (just hotspots — they do NOT tunnel the box)

- iPhone: Settings → Personal Hotspot → "Allow Others to Join". Note SSID + password; give it a
  simple stable name.
- iPad (cellular): same; note its own SSID + password.
- Add both SSIDs to the firmware network list (§6.2) so whichever is on works.
- First-join quirk: keep the Personal Hotspot screen open during the BOX-3's first connect — iOS
  naps the hotspot radio until a non-Apple client completes the handshake.
- Installing Tailscale on the phone is fine for your own use but does **not** route the BOX-3.

---

## 5. Hardware prep
- Peel the screen protector — it covers the mic ports and muffles them.
- Use a **data** USB-C cable for flashing (not charge-only).
- Anker 733 for untethered use; if it idle-cuts on battery, it's the low-current cutoff.
- Only the main unit is used; dock/sensor/RGB/breadboard parts are future-proofing.

## 6. Firmware

### 6.1 Toolchain + board support
- Install ESP-IDF v5.x; `idf.py set-target esp32s3`.
- Base on the **esp-box BSP** (`github.com/espressif/esp-box`) — brings up screen (LVGL), the
  ES8311 speaker / ES7210 dual-mic codec, and buttons; no manual pin wiring.
- `idf.py menuconfig`: enable **SPIRAM/PSRAM in octal mode** (MicroLink's TLS handshake fails
  without it).
- Sanity check: flash a BSP display example + mic→speaker loopback before adding networking.

### 6.2 Roaming WiFi (join first reachable, skip captive portals)
```c
typedef struct { const char* ssid; const char* pass; } wifi_net_t;
static const wifi_net_t KNOWN_NETS[] = {
    { "My iPhone", "hotspot-pw-1" },
    { "My iPad",   "hotspot-pw-2" },
    { "HomeWiFi",  "home-pw" },
    // travel networks ONLY if they have no captive portal
};
```
- Never add the corporate SSID (you want cellular at the office).
- After associating, run a connectivity probe (reach `marvin`'s tailnet host / fetch a tiny known
  URL); on failure drop that net and try the next — captive portals "connect" but go nowhere.
- Disconnect handler: on link loss, re-walk the list and re-establish tunnel + WebSocket.

### 6.3 Join the tailnet (MicroLink)
- Clone MicroLink (`CamM2325/microlink`) into `components/`. Pin a known-good commit.
```c
#include "microlink.h"
void init_tailscale(void) {
    microlink_config_t ts = {
        .auth_key     = "tskey-auth-XXXXXXXX",  // reusable key from §3
        .hostname     = "hermes-box3",
        .enable_psram = true,
    };
    microlink_init(&ts);
}
```
- Expect tuning on S3 hardware: raise STUN/peer-discovery timeout (~3s → ~6s); bind DISCO to a
  port separate from WireGuard's 51820 (e.g. 51821); suppress the aggressive heartbeat that
  otherwise drops the link. Check the component's Kconfig for current option names.
- Success: `hermes-box3` appears in the Tailscale admin console.

### 6.4 Connect to the Voice Gateway
```c
#include <WebSocketsClient.h>
WebSocketsClient ws;
// tailscale serve terminates TLS; connect to marvin's serve endpoint
void net_setup() {
    ws.beginSSL("marvin.tail240ea8.ts.net", 443, "/voice");
    ws.onEvent(onWsEvent);
    ws.setReconnectInterval(2000);   // mobile links flap
}
```

### 6.5 Audio + display state machine
- Audio via BSP codec API in its own FreeRTOS task; queue network sends so I²S never blocks on WiFi.
- LVGL screen driven by gateway events:

| State | Trigger | Screen |
|-------|---------|--------|
| Joining network | boot / link lost | "Connecting…" (show SSID) |
| Tunneling | WiFi up, MicroLink handshaking | "Securing link…" |
| Ready | WebSocket open | "Hermes online — say 'hey buddy'" |
| Listening | wake word / button held | "Listening…" + level meter |
| Thinking | `state: thinking` | "Hermes is thinking…" |
| Result | `transcript` / `tts` | transcript text, then reply |
| Awaiting approval | `state: approval` | "Waiting for owner approval…" |
| Error | tunnel/WS dropped | "Reconnecting…" |

Add an **"Awaiting approval"** state — when a spoken command hits the AgentShroud approval queue
(§2.4), the Voice Gateway should emit `{"type":"state","value":"approval"}` so the screen reflects
it instead of looking hung.

## 7. Bring-up order (one cause per failure)
1. Display example renders.
2. Local mic → speaker loopback works.
3. WiFi walks the list, joins one, passes the connectivity probe.
4. MicroLink registers — `hermes-box3` in the admin console.
5. BOX-3 reaches `marvin` over the tailnet.
6. Voice Gateway WebSocket connects and echoes a test message.
7. Governed round-trip: Voice Gateway `POST /forward {route_to: hermes}` returns a real `agent_response`.
8. Full loop: wake word → speak → transcript on screen → spoken reply.
9. Approval path: speak a high-risk command ("delete that file") → screen shows "Awaiting approval" → approve in AgentShroud → reply plays.
10. Roam test: kill the active network mid-session; confirm it falls back, re-tunnels, and the WebSocket returns with no reboot.

## 8. Gotchas (incl. AgentShroud-specific)
- Screen protector covers the mics — remove first.
- Data USB-C cable, not charge-only.
- PSRAM must be **enabled** in menuconfig, not just present.
- MicroLink is young — pin a commit, budget an afternoon for the discovery/heartbeat tuning.
- Captive portals silently break travel WiFi — the probe + hotspot fallback handles it.
- Office = cellular; on restrictive carrier NAT MicroLink may fall back to a DERP relay (works, slightly higher latency).
- **Use the governed `/forward` path, not the `:8642` forwarder** — the forwarder bypasses inbound PromptGuard/PII (`gateway/runtime/lifespan.py:1966`).
- High-risk spoken commands **will** pause for owner approval (§2.4) — that's the product working, not a bug.

## 9. "hey buddy" wake word — honest status

ESP-SR's WakeNet ships a fixed set of built-in wake words (e.g. "Hi ESP", "Alexa", "Hi Lexin",
"Computer"). **"hey buddy" is not built in.** Two real options:

- **Ship now with push-to-talk** (hold the BOX-3 button to speak). Zero extra work; use this for §7 bring-up.
- **Add "hey buddy" via a custom WakeNet model:** generate one through Espressif's custom
  wake-word service (submit the phrase "hey buddy", receive a model blob), drop it into the
  `model/` partition, and select it in `menuconfig` under ESP-SR → WakeNet. Far-field dual mics
  make on-device, always-listening wake detection viable. The wake event simply replaces the
  button-hold trigger that starts streaming to the Voice Gateway.

Recommended order: bring the whole chain up on push-to-talk (§7 steps 1–10), then swap in the
custom "hey buddy" model as the final step so wake-word issues never block tunnel/STT debugging.

## 10. Alternatives (only if needed)
- **WireGuard bridge instead of MicroLink** (`pierrejay/esp32-tailbridge` or a WG server on
  `marvin`) — lighter firmware, but you maintain a reachable WG endpoint. Audio/display/Voice
  Gateway halves unchanged.
- **Native Hermes adapter instead of a separate STT/TTS** — a custom Hermes gateway platform
  adapter reusing Hermes' own transcription/TTS. Upside: reuse built-ins; downside: couples to
  Hermes internals and **loses the governed `/forward` enforcement** unless you re-add it. Not
  recommended for a security product.

## 11. Open decisions (confirm before server-side coding)
1. **STT/TTS:** local (faster-whisper + Piper, default — zero new egress) vs cloud (api.openai.com, already allowlisted). Default = local.
2. **§2.2 governed-path fix:** router translation (a) vs Hermes `/chat` shim (b). Default = (a), keeps the change inside the gateway.
3. **Wake word timing:** push-to-talk for v1, "hey buddy" custom model as the closing step (default), or block on the custom model first.

## Sources
- MicroLink: `github.com/CamM2325/microlink`
- esp-box BSP: `github.com/espressif/esp-box`
- esp32-tailbridge: `github.com/pierrejay/esp32-tailbridge`
- Hermes Agent: `NousResearch/hermes-agent`
- Tailscale auth keys: `tailscale.com/kb`
- AgentShroud governed ingest: `gateway/ingest_api/routes/forward.py:330`; egress allowlist: `gateway/security/egress_config.py:23`; approval routing: `gateway/proxy/pipeline.py:716`; tailnet exposure: `scripts/tailscale-serve.sh`
