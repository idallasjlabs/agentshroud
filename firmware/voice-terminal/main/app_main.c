#include <stdlib.h>
#include <string.h>
#include <stdarg.h>
#include "wifi_credentials.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/event_groups.h"
#include "freertos/stream_buffer.h"
#include "esp_heap_caps.h"
#include "esp_log.h"
#include "esp_wifi.h"
#include "esp_event.h"
#include "nvs_flash.h"
#include "esp_ota_ops.h"
#include "bsp/esp-bsp.h"
#include "lvgl.h"
/* Private header needed for disp->flushing field used in flush_wait_cb below.
 * LVGL's cmake adds both ${LVGL_ROOT_DIR} and ${LVGL_ROOT_DIR}/src to INCLUDE_DIRS,
 * so "display/lv_display_private.h" resolves correctly in the IDF build. */
#include "display/lv_display_private.h"

#include "audio.h"
#include "wakeword.h"
#include "ws_client.h"
#include "ui_face.h"
#include "ota.h"
#include "remote_log.h"
#include "playback_logic.h"

static const char *TAG = "vt";

/* ── Agent table ──────────────────────────────────────────────────────────── *
 * Defines the ordered list of agents the user can cycle through with the
 * agent-toggle button (BSP_BUTTON_MUTE).  The slug is passed as ?agent=<slug>
 * in the WebSocket URL; the gateway resolves it via the agentshroud.yaml bots:
 * registry.  Index 0 is the default (matches VOICE_DEFAULT_AGENT on the server).
 *
 * To add a future agent: add an entry here, update agentshroud.yaml bots:,
 * and reflash the firmware.  No server code change needed.
 */
typedef struct {
    const char *slug;    /* AgentShroud bot key (agentshroud.yaml bots: section) */
    const char *display; /* Human-readable name shown on screen */
} vt_agent_t;

static const vt_agent_t VT_AGENTS[] = {
    /* Local model (gateway direct fast-path) first = boot default (owner
     * directive 2026-08-07, supersedes the 2026-07-06 Hermes-first
     * directive below): Hermes's agentic-loop latency is highly variable
     * (6-60+s observed live) and was making the device "nearly unusable"
     * as a boot default; the fast local path answers in 1-6s. Middle
     * button cycles to Hermes for full agentic control (email, systems,
     * browsing) or say "tell Hermes"/"ask Hermes" from any state — spoken
     * switches are sticky for the server-side session but do not survive
     * a device reboot, hence changing the boot default itself here.
     * Display label is deliberately model-agnostic ("Local"): the actual
     * model behind "direct" is the voice-gateway's VOICE_MODEL env
     * (docker-compose.yml) and has already changed twice (qwen3-14b →
     * gemma-4-12B-it-4bit, 2026-08-27) — a hardcoded model name here goes
     * stale on every server-side swap, which is exactly how the screen
     * ended up claiming "Qwen3" while gemma answered.
     * Historical context (2026-07-06): "the ESP32 is the owner's ADMIN
     * VOICE ACCESS to Hermes, not a generic chat box" — still true, just no
     * longer the boot default; Hermes is one voice command away. */
    { "direct",  "Local"    },   /* Low-latency gateway LLM proxy — no agentic tools          */
    { "hermes",  "Hermes"   },   /* Hermes agentic assistant — synchronous OpenAI-compat reply */
    { "openclaw","OpenClaw" },   /* OpenClaw — async Telegram bot; replies on Telegram         */
};
#define VT_AGENT_COUNT ((int)(sizeof(VT_AGENTS) / sizeof(VT_AGENTS[0])))

/* Called by wakeword.c via the forward declaration. */
int vt_agent_count(void) { return VT_AGENT_COUNT; }

/* Build the full WebSocket URL with ?token= and &agent= query params.
 * buf must be at least 512 bytes.  Returns the length written (excl. NUL). */
static int _build_ws_url(char *buf, size_t bufsz, int agent_idx)
{
    const char *slug = (agent_idx >= 0 && agent_idx < VT_AGENT_COUNT)
                       ? VT_AGENTS[agent_idx].slug
                       : VT_AGENTS[0].slug;
    return snprintf(buf, bufsz,
                    "%s?token=%s&agent=%s",
                    CONFIG_VT_VG_WS_URL, CONFIG_VT_VG_WS_TOKEN, slug);
}

/* ── WiFi ─────────────────────────────────────────────────────────────────── */

#define WIFI_CONNECTED_BIT BIT0
#define WIFI_FAIL_BIT      BIT1

static EventGroupHandle_t s_wifi_eg;
static int                s_retry = 0;
static char               s_ip[20];

typedef struct { const char *ssid; const char *pass; } wifi_net_t;
static const wifi_net_t NETWORKS[] = {
    { CONFIG_VT_WIFI_SSID,   CONFIG_VT_WIFI_PASSWORD   },
    { CONFIG_VT_WIFI_SSID_2, CONFIG_VT_WIFI_PASSWORD_2 },
};
#define NETWORK_COUNT (sizeof(NETWORKS) / sizeof(NETWORKS[0]))
static int s_net_idx = 0;

/* ── LVGL flush-wait shim ─────────────────────────────────────────────────── *
 * esp_lvgl_port never sets lv_display_set_flush_wait_cb(), so LVGL falls back
 * to a bare busy-wait ("while(disp->flushing);") inside wait_for_flushing().
 * When the SPI DMA ISR is slow to call lv_disp_flush_ready(), taskLVGL spins
 * continuously, starving IDLE0 → WDT fires after 5 s.
 *
 * Fix: yield in 1 ms slices while waiting, with a 200 ms hard timeout.
 * 200 ms covers worst-case: multiple dirty regions flushed per animation tick,
 * or I2S DMA contention slowing SPI ISR scheduling.  LVGL forces
 * disp->flushing = 0 after the callback returns, so we cannot create a true
 * livelock — worst case we skip one frame and the DMA transaction eventually
 * drains.
 */
static void _lvgl_flush_wait_yield(lv_display_t *disp)
{
    uint32_t start = xTaskGetTickCount();
    while (disp->flushing && (xTaskGetTickCount() - start) < pdMS_TO_TICKS(200)) {
        vTaskDelay(pdMS_TO_TICKS(1));
    }
}

/* ── LVGL UI ──────────────────────────────────────────────────────────────── */

typedef enum {
    UI_WIFI_CONNECTING,
    UI_WIFI_CONNECTED,
    UI_READY,
} ui_state_t;

static lv_obj_t  *s_label      = NULL;
static lv_obj_t  *s_sub_label  = NULL;
static ui_state_t s_ui_state   = UI_WIFI_CONNECTING;

static void ui_update(ui_state_t state, const char *detail)
{
    if (!s_label) return;
    bsp_display_lock(0);
    s_ui_state = state;
    switch (state) {
        case UI_WIFI_CONNECTING:
            lv_label_set_text(s_label, "Connecting to WiFi...");
            lv_label_set_text(s_sub_label, detail ? detail : "");
            break;
        case UI_WIFI_CONNECTED:
            lv_label_set_text(s_label, "WiFi connected");
            lv_label_set_text(s_sub_label, detail ? detail : "");
            break;
        case UI_READY:
            /* Hand off display to ui_face; hide the WiFi status labels. */
            lv_obj_add_flag(s_label,     LV_OBJ_FLAG_HIDDEN);
            lv_obj_add_flag(s_sub_label, LV_OBJ_FLAG_HIDDEN);
            break;
    }
    bsp_display_unlock();
}

static void ui_init(void)
{
    bsp_display_cfg_t cfg = {
        .lvgl_port_cfg = ESP_LVGL_PORT_INIT_CONFIG(),
        .buffer_size   = BSP_LCD_H_RES * BSP_LCD_V_RES / 4,
        .flags = {
            .buff_dma = true,   /* must be DMA-capable; non-DMA buffer fails spi_device_queue_trans */
        },
    };
    bsp_display_start_with_config(&cfg);
    bsp_display_backlight_on();

    bsp_display_lock(0);
    /* Replace the default busy-wait with a yielding wait so taskLVGL doesn't
     * starve IDLE0 when a SPI DMA flush takes longer than usual. */
    lv_display_t *disp = lv_display_get_default();
    if (disp) {
        lv_display_set_flush_wait_cb(disp, _lvgl_flush_wait_yield);
    }

    lv_obj_t *scr = lv_screen_active();
    lv_obj_set_style_bg_color(scr, lv_color_hex(0x1a1a2e), LV_PART_MAIN);

    s_label = lv_label_create(scr);
    lv_obj_set_style_text_color(s_label, lv_color_hex(0xffffff), LV_PART_MAIN);
    lv_obj_set_style_text_font(s_label, &lv_font_montserrat_28, LV_PART_MAIN);
    lv_obj_align(s_label, LV_ALIGN_CENTER, 0, -28);
    lv_label_set_text(s_label, "Starting...");

    s_sub_label = lv_label_create(scr);
    lv_obj_set_style_text_color(s_sub_label, lv_color_hex(0xcccccc), LV_PART_MAIN);
    lv_obj_set_style_text_font(s_sub_label, &lv_font_montserrat_28, LV_PART_MAIN);
    lv_obj_align(s_sub_label, LV_ALIGN_CENTER, 0, 28);
    lv_label_set_text(s_sub_label, "");

    bsp_display_unlock();
}

/* ── WiFi event handler ───────────────────────────────────────────────────── */

static void wifi_event_handler(void *arg, esp_event_base_t base,
                               int32_t id, void *data)
{
    if (base == WIFI_EVENT && id == WIFI_EVENT_STA_START) {
        esp_wifi_connect();

    } else if (base == WIFI_EVENT && id == WIFI_EVENT_STA_DISCONNECTED) {
        wifi_event_sta_disconnected_t *ev = (wifi_event_sta_disconnected_t *)data;
        s_retry++;
        ESP_LOGW(TAG, "WiFi disconnected from '%s' reason=%d (attempt %d/%d)",
                 NETWORKS[s_net_idx].ssid, ev->reason, s_retry, CONFIG_VT_WIFI_MAX_RETRY);
        /* Queued; flushes after the link recovers.  The reason code is the
         * only remote evidence of a WiFi-layer drop (vs TCP/TLS-layer). */
        vt_remote_log("WiFi DROP reason=%d (attempt %d)", (int)ev->reason, s_retry);

        if (s_retry >= CONFIG_VT_WIFI_MAX_RETRY) {
            s_retry = 0;
            s_net_idx = (s_net_idx + 1) % NETWORK_COUNT;
            if (strlen(NETWORKS[s_net_idx].ssid) == 0) {
                s_net_idx = 0;
            }
            ESP_LOGI(TAG, "Switching to network '%s'", NETWORKS[s_net_idx].ssid);

            wifi_config_t cfg = {};
            strlcpy((char *)cfg.sta.ssid,     NETWORKS[s_net_idx].ssid, 32);
            strlcpy((char *)cfg.sta.password, NETWORKS[s_net_idx].pass, 64);
            esp_wifi_set_config(WIFI_IF_STA, &cfg);
            ui_update(UI_WIFI_CONNECTING, NETWORKS[s_net_idx].ssid);
        }
        esp_wifi_connect();

    } else if (base == IP_EVENT && id == IP_EVENT_STA_GOT_IP) {
        ip_event_got_ip_t *ev = (ip_event_got_ip_t *)data;
        snprintf(s_ip, sizeof(s_ip), IPSTR, IP2STR(&ev->ip_info.ip));
        ESP_LOGI(TAG, "Got IP: %s", s_ip);
        vt_remote_log("WiFi UP ip=%s", s_ip);
        s_retry = 0;
        xEventGroupSetBits(s_wifi_eg, WIFI_CONNECTED_BIT);
        ui_update(UI_WIFI_CONNECTED, s_ip);
    }
}

static void wifi_init(void)
{
    s_wifi_eg = xEventGroupCreate();
    esp_netif_create_default_wifi_sta();

    wifi_init_config_t init = WIFI_INIT_CONFIG_DEFAULT();
    ESP_ERROR_CHECK(esp_wifi_init(&init));

    ESP_ERROR_CHECK(esp_event_handler_instance_register(
        WIFI_EVENT, ESP_EVENT_ANY_ID, &wifi_event_handler, NULL, NULL));
    ESP_ERROR_CHECK(esp_event_handler_instance_register(
        IP_EVENT, IP_EVENT_STA_GOT_IP, &wifi_event_handler, NULL, NULL));

    wifi_config_t cfg = {};
    strlcpy((char *)cfg.sta.ssid,     NETWORKS[0].ssid, 32);
    strlcpy((char *)cfg.sta.password, NETWORKS[0].pass, 64);
    cfg.sta.threshold.authmode = WIFI_AUTH_OPEN;

    ESP_ERROR_CHECK(esp_wifi_set_mode(WIFI_MODE_STA));
    ESP_ERROR_CHECK(esp_wifi_set_config(WIFI_IF_STA, &cfg));
    ESP_ERROR_CHECK(esp_wifi_start());
    /* Disable modem power-save.  Default WIFI_PS_MIN_MODEM ("pm start, type: 1"
     * in the boot log) sleeps the radio between DTIM beacons; a sudden PCM
     * uplink burst on an iPhone hotspot then reliably drops the link ~0.3-1 s
     * after streaming starts — the "reconnects every time I speak" bug.  The
     * device is mains-powered, so the power cost is irrelevant. */
    ESP_ERROR_CHECK(esp_wifi_set_ps(WIFI_PS_NONE));

    ESP_LOGI(TAG, "Connecting to '%s'...", NETWORKS[0].ssid);
    ui_update(UI_WIFI_CONNECTING, NETWORKS[0].ssid);
}

/* ── TTS ring buffer ──────────────────────────────────────────────────────── *
 * PCM frames from the gateway arrive in the websocket_task context (CPU 0).
 * Calling audio_play() there blocks i2s_channel_write() for ~93 ms per 4 KB
 * chunk, which stalls the WebSocket receive loop and eventually causes a dirty
 * close (transport detects no progress).
 *
 * Fix: _on_tts_pcm pushes PCM into a stream buffer (non-blocking).  A
 * dedicated tts_task on CPU 1 drains it and calls audio_play(), leaving the
 * websocket_task free to keep reading frames.  If the buffer fills (gateway
 * sending faster than real-time playback), we drop the excess — a momentary
 * audio gap is better than a connection crash.
 *
 * The backing store is placed in PSRAM explicitly (heap_caps_malloc +
 * xStreamBufferCreateStatic) so we get a large buffer without needing
 * CONFIG_SPIRAM_USE_MALLOC to redirect pvPortMalloc to PSRAM.
 */
#define TTS_STREAM_BUF_BYTES   (1024 * 1024) /* ~32 s at 16000 Hz 16-bit mono.
                                              * The server BURSTS the whole reply
                                              * (drop-tolerant on the hotspot), so
                                              * the buffer must hold the longest
                                              * plausible reply: at 256 KB (~8 s),
                                              * anything longer overflowed and
                                              * _on_tts_pcm dropped whole chunks —
                                              * the "ends of words cut off"
                                              * user report.  PSRAM has MBs free. */
static StreamBufferHandle_t  s_tts_buf      = NULL;
static StaticStreamBuffer_t  s_tts_sbuf_ctrl;     /* control struct — internal DRAM (BSS) */
static uint8_t              *s_tts_sbuf_mem = NULL; /* backing store — PSRAM */

/* Set when the server's END frame lands (strictly after the last PCM byte of
 * a reply) — the ONLY reliable "reply fully received" signal.  The playback
 * gate waits for it: the server pipelines synthesis, so the whole reply
 * streams in while sentence 1 would otherwise be playing, and that
 * concurrent TLS receive was tearing sentence 1 into static on every build
 * that gated on quiet-windows or byte counts (inter-sentence synthesis gaps
 * are indistinguishable from reply-complete on the wire). */
static volatile bool s_reply_complete = false;

/* Pop-free playback: the speaker stream NEVER stops.  Every start/stop of
 * the I2S/DAC stream pops the ES8311/NS4150 audibly; three build iterations
 * of pre-buffer tuning (1.5 s → 4 s → burst-end trigger) moved the clicks
 * around instead of removing them because each drain/refill boundary was
 * itself the click.  Design now: feed continuous zeros whenever no reply
 * audio is queued — the DAC clocks silence forever and there is no boundary
 * to pop.  A small initial gate (1 s banked or 300 ms of stream-quiet)
 * absorbs network jitter at reply start; mid-reply gaps become silent
 * stretches instead of pops.  Mains-powered device: the always-on amp is
 * irrelevant. */

static void tts_task(void *arg)
{
    static uint8_t play_chunk[4096];
    bool   gate_open   = false;   /* replies pass only after the END-gate */
    while (1) {
        size_t avail = xStreamBufferBytesAvailable(s_tts_buf);

        if (!gate_open && avail > 0) {
            /* END-GATE: play only once the WHOLE reply is buffered (the
             * server's END frame sets s_reply_complete strictly after the
             * last PCM byte).  Playback then never overlaps TLS receive —
             * the root cause of first-sentence static that survived every
             * quiet-window/byte-count gate.  Caps: 768 KB banked (~24 s;
             * 1 MB buffer overflow guard) or 20 s fill age (synthesis
             * wedge guard) start playback anyway. */
            static TickType_t s_gate_start = 0;
            if (s_gate_start == 0) s_gate_start = xTaskGetTickCount();
            uint32_t gate_age_ms =
                (xTaskGetTickCount() - s_gate_start) * portTICK_PERIOD_MS;
            if (playback_gate_should_open(s_reply_complete, avail, gate_age_ms)) {
                gate_open        = true;
                s_reply_complete = false;
                s_gate_start     = 0;
                /* PLAYBACK drives the speaking-state machine, not server
                 * frames: under the END-gate the server's idle arrives
                 * BEFORE playback starts, and keying tts_playing to it
                 * released every hold (rlog flush, beacon, WakeNet feed)
                 * exactly at playback start — the surviving first-words
                 * static.  Set it here, clear it when the buffer drains. */
                wakeword_set_tts_playing(true);
                ui_face_set_state(WS_VG_STATE_SPEAKING);
            }
        }

        size_t got = 0;
        if (gate_open) {
            got = xStreamBufferReceive(s_tts_buf, play_chunk, sizeof(play_chunk), 0);
            if (got == 0) {
                gate_open = false;     /* reply drained — re-gate for the next */
                wakeword_set_tts_playing(false);
                wakeword_tts_stop_clear();
                if (!wakeword_triggered()) {
                    ui_face_set_state(WS_VG_STATE_IDLE);
                }
            } else if (wakeword_tts_stop_requested()) {
                got = 0;               /* discard; fall through to silence */
            }
        }
        if (got == 0) {
            /* No reply audio → feed silence.  The stream never stops. */
            memset(play_chunk, 0, sizeof(play_chunk));
            got = sizeof(play_chunk);
        }
        audio_play(play_chunk, got);   /* blocks ~128 ms per 4 KB — paces the loop */
        audio_volume_tick();           /* zipper-free volume ramp + deferred NVS */
    }
}

/* ── Voice Gateway callbacks ──────────────────────────────────────────────── */

static ws_vg_state_t s_prev_vg_state = WS_VG_STATE_DISCONNECTED;

/* Runs in websocket_task context — every call below is non-blocking:
 * wakeword_* are flag writes, vt_remote_log is a queue post, and
 * ui_face_set_state/set_agent are lv_async_call posts into the LVGL thread.
 * (History: this logic first ran heavy LVGL work inline → deadlock; then on
 * a dedicated vg_state_task → wedged on cross-task display locks after WiFi
 * drops, beacon-evidenced by stateq pinned at 3.  lv_async_call removes the
 * cross-task locking class entirely.) */
/* Set for the whole capture→delivery window (voice_task).  While an utterance
 * is being captured or delivered, the delivery loop owns the face — WS drops
 * and reconnects are EXPECTED on the hotspot (retries handle them), and the
 * DISCONNECTED/"Reconnecting" + reconnect-IDLE flashes they caused were the
 * owner's #1 cosmetic complaint.  Suppress both while active. */
static volatile bool s_delivery_active = false;

static void _on_vg_state(ws_vg_state_t state, void *ctx)
{
    (void)ctx;

    if (s_delivery_active &&
        (state == WS_VG_STATE_DISCONNECTED || state == WS_VG_STATE_IDLE ||
         state == WS_VG_STATE_LISTENING)) {
        /* LISTENING here is the server echoing our delivery-retry LISTEN
         * frames — the user is NOT being recorded.  Owner report 2026-07-07:
         * "still listening long after I stop speaking" = this echo. */
        /* Keep the LISTENING/THINKING face steady through delivery retries.
         * The delivery loop sets the final state itself (IDLE on failure;
         * on success the server drives THINKING→SPEAKING→IDLE). */
        s_prev_vg_state = state;
        return;
    }

    if (state == WS_VG_STATE_SPEAKING) {
        /* Reply download starting.  tts_playing + the SPEAKING face are set
         * by tts_task when PLAYBACK actually begins (END-gate) — not here. */
        s_reply_complete = false;

    } else if (state == WS_VG_STATE_IDLE) {
        bool post_tts    = (s_prev_vg_state == WS_VG_STATE_SPEAKING);
        bool interrupted = wakeword_tts_stop_requested();
        if (post_tts) s_reply_complete = true;   /* END landed — reply fully buffered */
        if (interrupted && s_tts_buf) {
            /* User tapped stop: flush the undelivered remainder so nothing
             * blares after the tap.  tts_task clears the stop request when
             * its drain completes. */
            xStreamBufferReset(s_tts_buf);
        }

        if (post_tts && !interrupted) {
            /* Reply fully buffered; playback (tts_task) owns the face from
             * here — SPEAKING when audio starts, IDLE when the buffer
             * drains.  (Auto-listen remains disabled: no AEC.) */
        } else if (!wakeword_triggered() && !wakeword_tts_playing()) {
            /* Interrupted or normal idle.  ui_face may already show IDLE if
             * the user tapped (touch callback updated it); set_state() has an
             * early-return guard so the redundant call is harmless. */
            ui_face_set_state(WS_VG_STATE_IDLE);
        }

    } else {
        ui_face_set_state(state);
    }

    s_prev_vg_state = state;
}

static void _on_tts_pcm(const uint8_t *pcm, size_t len, void *ctx)
{
    /* Non-blocking push: if the buffer is full, drop rather than stall
     * websocket_task.  CRITICAL: drop the WHOLE chunk or nothing —
     * xStreamBufferSend with 0 timeout does PARTIAL writes, and a partial
     * ending on an odd byte shifts every subsequent 16-bit sample by one
     * byte = full-scale white noise ("loud static louder than the speech",
     * user-reported).  Whole even-sized chunks keep S16LE alignment. */
    if (s_tts_buf && !wakeword_tts_stop_requested()) {
        size_t even_len = len & ~(size_t)1;
        if (even_len > 0 &&
            xStreamBufferSpacesAvailable(s_tts_buf) >= even_len) {
            xStreamBufferSend(s_tts_buf, pcm, even_len, 0);
        }
        /* else: chunk dropped whole — a brief gap, never corruption */
    }
}

/* Holds the display label for a server-side spoken model/agent switch
 * ("use Claude" / "tell Hermes" — voice_gateway/server.py's
 * _parse_model_switch_command). ui_face_set_agent()'s contract requires a
 * pointer that "stays valid forever" (it's queued through lv_async_call and
 * read later on the LVGL task) — VT_AGENTS entries satisfy that by being
 * static const; this buffer satisfies it by being static and outliving any
 * single _on_ws_ctrl call, unlike the cJSON-parsed string it's copied from
 * (freed immediately after this callback returns). */
static char s_spoken_agent_label[32];

/* Server control frames — spoken commands intercepted server-side.
 * Runs in websocket_task context; audio_set_volume's NVS commit is a few ms
 * (the TTS pre-buffer absorbs far more), everything else is non-blocking. */
static void _on_ws_ctrl(const char *cmd, int value, const char *str_value, void *ctx)
{
    (void)ctx;
    if (strcmp(cmd, "set_volume") == 0) {
        audio_set_volume(value);
        vt_remote_log("volume set to %d%% (spoken command)", value);
    } else if (strcmp(cmd, "set_agent_label") == 0 && str_value) {
        snprintf(s_spoken_agent_label, sizeof(s_spoken_agent_label), "%s", str_value);
        ui_face_set_agent(s_spoken_agent_label);
        vt_remote_log("agent label → %s (spoken command)", s_spoken_agent_label);
    } else {
        vt_remote_log("unknown ctrl cmd %.24s (value=%d) — ignored", cmd, value);
    }
}

/* ── Voice task ───────────────────────────────────────────────────────────── */

/* Shared WS handle — written by app_main, read/written by voice_task on switch. */
static volatile ws_client_handle_t s_ws = NULL;

/* ── Remote diagnostic log (see remote_log.h) ─────────────────────────────── */

/* Callers (LVGL task, voice_task, button callbacks) must NEVER block on the
 * ws-client lock — vt_remote_log only formats and enqueues (0-tick timeout);
 * rlog_task owns the actual sends.  Queue-full → drop, by design. */
#define RLOG_LINE_MAX 160
static QueueHandle_t s_rlog_q = NULL;
/* Task handle for the liveness status beacon (stack HWM + run state). */
static TaskHandle_t s_rlog_task_h = NULL;

void vt_remote_log(const char *fmt, ...)
{
    if (!s_rlog_q) return;

    char line[RLOG_LINE_MAX];
    va_list ap;
    va_start(ap, fmt);
    vsnprintf(line, sizeof(line), fmt, ap);
    va_end(ap);

    xQueueSend(s_rlog_q, line, 0);         /* never blocks the caller */
}

/* Liveness status beacon — sent DIRECTLY from voice_task (bypasses rlog_task)
 * so it keeps flowing even if rlog_task itself is the casualty.  Queue depths
 * + stack high-water marks pinpoint a dead/wedged worker task remotely. */
static void _send_status_beacon(ws_client_handle_t ws, bool streaming)
{
    /* WiFi RSSI: link quality to the hotspot — weak signal explains idle
     * drops that TCP-level evidence can't. */
    wifi_ap_record_t ap = {0};
    int rssi = (esp_wifi_sta_get_ap_info(&ap) == ESP_OK) ? ap.rssi : 0;

    /* Internal-RAM-specific free/min-ever, alongside the existing combined
     * (internal+PSRAM) figure. esp_get_free_heap_size() alone looks healthy
     * (several MB, PSRAM-dominated) even when internal RAM specifically —
     * the pool AES/TLS/WiFi actually draw from — is critically low or
     * fragmented; that's exactly why the 2026-08-26/27 esp-aes allocation
     * failures were invisible in this status line the whole time. Minimum-
     * ever (not just current) catches transient dips between beacons, not
     * just snapshots. */
    char line[RLOG_LINE_MAX];
    snprintf(line, sizeof(line),
             "status: stream=%d trig=%d rssi=%d rlogq=%u rlog_st=%d rlog_hwm=%u heap=%u "
             "int_free=%u int_min=%u",
             (int)streaming, (int)wakeword_triggered(), rssi,
             s_rlog_q      ? (unsigned)uxQueueMessagesWaiting(s_rlog_q)           : 0u,
             s_rlog_task_h ? (int)eTaskGetState(s_rlog_task_h)                    : -1,
             s_rlog_task_h ? (unsigned)uxTaskGetStackHighWaterMark(s_rlog_task_h) : 0u,
             (unsigned)esp_get_free_heap_size(),
             (unsigned)heap_caps_get_free_size(MALLOC_CAP_INTERNAL),
             (unsigned)heap_caps_get_minimum_free_size(MALLOC_CAP_INTERNAL));
    ws_client_send_log(ws, line);
}

static void rlog_task(void *arg)
{
    (void)arg;
    char line[RLOG_LINE_MAX];
    for (;;) {
        if (xQueueReceive(s_rlog_q, line, portMAX_DELAY) != pdTRUE) continue;
        /* HOLD the line while disconnected (drop-window diagnostics are the
         * ones that matter), but do NOT let one undeliverable line dam the
         * queue: while CONNECTED, give it ~3 s of send attempts then drop it
         * and move on.  The previous 60 s cap head-of-line-blocked the whole
         * queue during streaming (PCM writes monopolise the tx lock), which
         * blacked out diagnostics exactly when the link was failing. */
        int connected_tries = 0;
        for (int waited_ms = 0; waited_ms < 30000; waited_ms += 250) {
            ws_client_handle_t ws = s_ws;  /* local copy; avoids torn reads */
            if (wakeword_tts_playing() || s_reply_complete) {
                /* Hold diagnostics while a reply plays OR is about to (fully
                 * buffered, gate opening) — each send is TLS work that can
                 * tear the audio.  Queue drains right after. */
                vTaskDelay(pdMS_TO_TICKS(250));
                continue;
            }
            if (ws && ws_client_connected(ws)) {
                if (ws_client_send_log(ws, line) == ESP_OK) break;  /* delivered */
                if (++connected_tries >= 4) break;                  /* ~1 s: drop it */
            }
            vTaskDelay(pdMS_TO_TICKS(250));
        }
    }
}

typedef struct {
    /* intentionally empty — voice_task reads s_ws and wakeword state directly */
    int unused;
} voice_task_args_t;

/* ── Store-and-forward utterance delivery ─────────────────────────────────
 *
 * The iPhone-hotspot/cellular leg FINs long-lived upstream streams
 * unpredictably (0.3–9 s into live PCM, in time-clustered phases) — proven
 * by a day of remote-diag traces while the Funnel+gateway legs tested clean.
 * Live-streaming the mic can therefore never be reliable on this deployment.
 *
 * Instead: RECORD the whole utterance to PSRAM during capture (no network
 * dependency at all), then DELIVER it afterwards as a paced burst with up to
 * 3 attempts across reconnects.  A connection drop costs seconds of delay,
 * never the query. */
#define UTT_BUF_MAX     (256 * 1024)   /* 8 s @ 16 kHz S16LE — matches VAD cap  */
#define UTT_CHUNK       4096           /* burst chunk size                       */
#define UTT_CHUNK_DELAY 64             /* ms between chunks ≈ 2× realtime.  20 ms
                                        * (6×) overran the hotspot uplink — live
                                        * 2026-07-05: all 5 attempts dropped
                                        * mid-burst at random offsets.  64 ms is
                                        * the empirically-clean rate. */
#define UTT_ATTEMPTS    5              /* delivery attempts — live 2026-07-04 trace
                                        * showed steady progress per retry (4→49→
                                        * 151 KB); 3 gave up just short of landing */

static bool _deliver_utterance(const uint8_t *buf, size_t len)
{
    size_t sent_ok = 0;   /* bytes successfully sent across attempts (resume) */
    /* CRITICAL: never hand PSRAM pointers to the TLS stack.  utt_buf lives in
     * PSRAM; mbedTLS on the S3 fails the SSL write instantly when the
     * plaintext is external RAM (serial-caught 2026-07-04:
     * "esp_transport_write() returned -1, ESP_ERR_MBEDTLS_SSL_WRITE_FAILED"
     * 9 ms into the first chunk), which closes the connection and made every
     * delivery die at 0/N bytes.  LISTEN/END (flash strings) always went
     * through — only the PSRAM payload failed.  Bounce each chunk through
     * internal DRAM (static → BSS) before it reaches TLS. */
    static uint8_t bounce[UTT_CHUNK];

    for (int attempt = 1; attempt <= UTT_ATTEMPTS; attempt++) {
        /* Wait for a live connection — the WS client auto-reconnects every
         * ~5 s, and post-drop recovery has measured at ~8 s. */
        for (int waited = 0; waited < 20000 && !ws_client_connected(s_ws); waited += 250) {
            vTaskDelay(pdMS_TO_TICKS(250));
        }
        ws_client_handle_t ws = s_ws;
        if (!ws_client_connected(ws)) {
            vt_remote_log("delivery %d/%d: no connection", attempt, UTT_ATTEMPTS);
            continue;
        }

        /* Resume from where earlier attempts got to (rewound 8 KB for
         * in-flight loss) — a drop at 90%% now costs a tail send, not a full
         * restart.  Attempt 1 (sent_ok == 0) uses the plain LISTEN. */
        size_t start_off = delivery_resume_offset(sent_ok);
        esp_err_t lr = ESP_FAIL;
        for (int a = 0; a < 3 && lr != ESP_OK; a++) {
            lr = (start_off > 0)
                     ? ws_client_send_listen_resume(ws, start_off)
                     : ws_client_send_listen(ws);
            if (lr != ESP_OK) vTaskDelay(pdMS_TO_TICKS(20));
        }
        if (lr != ESP_OK) {
            vt_remote_log("delivery %d/%d: LISTEN send failed", attempt, UTT_ATTEMPTS);
            continue;
        }

        /* Paced burst: full 8 s utterance delivers in ≤4 s — inside the
         * server's 15 s LISTEN window and 640 KB PCM cap.  The server treats
         * every LISTEN as a fresh utterance, so retrying the whole buffer
         * after a mid-burst drop is idempotent. */
        size_t off = start_off;
        bool   dropped = false;
        /* Adaptive pacing: if earlier attempts dropped mid-burst, the uplink
         * can't sustain the base rate — slow down instead of failing the same
         * way five times (live 2026-07-05: weak-signal location dropped every
         * attempt at 4-196 KB).  Cap at 3× (192 ms/chunk ≈ 21 KB/s): a full
         * 8 s utterance still delivers in ~12 s, inside the server's 15 s
         * LISTEN window. */
        int chunk_delay = UTT_CHUNK_DELAY * (attempt < 3 ? attempt : 3);
        while (off < len) {
            size_t n = (len - off > UTT_CHUNK) ? UTT_CHUNK : (len - off);
            memcpy(bounce, buf + off, n);   /* PSRAM → internal DRAM, see above */
            if (!ws_client_connected(ws) ||
                ws_client_send_pcm(ws, bounce, n) != ESP_OK) {
                dropped = true;
                break;
            }
            off += n;
            sent_ok = delivery_track_sent_ok(sent_ok, off);
            vTaskDelay(pdMS_TO_TICKS(chunk_delay));
        }
        if (dropped) {
            vt_remote_log("delivery %d/%d: dropped at %u/%u bytes — retrying",
                          attempt, UTT_ATTEMPTS, (unsigned)off, (unsigned)len);
            continue;
        }

        esp_err_t er = ESP_FAIL;
        for (int a = 0; a < 3 && er != ESP_OK; a++) {
            er = ws_client_send_end(ws);
            if (er != ESP_OK) vTaskDelay(pdMS_TO_TICKS(20));
        }
        if (er != ESP_OK) {
            vt_remote_log("delivery %d/%d: END send failed", attempt, UTT_ATTEMPTS);
            continue;
        }

        ESP_LOGI(TAG, "Utterance delivered: %u bytes (attempt %d)", (unsigned)len, attempt);
        vt_remote_log("utterance DELIVERED: %u bytes (attempt %d)", (unsigned)len, attempt);
        return true;
    }

    ESP_LOGW(TAG, "Utterance delivery failed after %d attempts (%u bytes)", UTT_ATTEMPTS, (unsigned)len);
    vt_remote_log("utterance delivery FAILED after %d attempts (%u bytes)", UTT_ATTEMPTS, (unsigned)len);
    return false;
}

static void voice_task(void *arg)
{
    (void)arg;
    ESP_LOGI(TAG, "voice_task started on core %d", (int)xPortGetCoreID());

    /* Frame size is determined by the AFE at init time — must match afe->get_feed_chunksize(). */
    const int frame_bytes = wakeword_feed_bytes();
    uint8_t  *frame_buf   = (uint8_t *)malloc(frame_bytes);
    /* Utterance record buffer — PSRAM (256 KB won't fit internal DRAM). */
    uint8_t *utt_buf = (uint8_t *)heap_caps_malloc(UTT_BUF_MAX,
                                                   MALLOC_CAP_SPIRAM | MALLOC_CAP_8BIT);
    size_t   utt_len = 0;
    if (!frame_buf || !utt_buf) {
        ESP_LOGE(TAG, "voice_task: buffer alloc failed (frame=%p utt=%p)",
                 (void *)frame_buf, (void *)utt_buf);
        vTaskDelete(NULL);
        return;
    }

    bool capturing = false;
    /* Keepalive: send {"ping":1} every 30 s when idle so the office NAT and
     * Tailscale DERP relay see bidirectional traffic and don't drop the TCP
     * connection.  frame_bytes is ~512 bytes at 16kHz; ~62 frames/s → counter
     * of 1860 ≈ 30 s. */
    int keepalive_frames = 0;
    const int KEEPALIVE_INTERVAL = 1860;
    ESP_LOGI(TAG, "Voice task running (frame=%d bytes)", frame_bytes);

    while (1) {
        /* ── Agent switch ── */
        if (!capturing && wakeword_agent_switch_pending()) {
            int idx = wakeword_agent_index();
            ESP_LOGI(TAG, "Agent switch → [%d] %s (%s)",
                     idx, VT_AGENTS[idx].display, VT_AGENTS[idx].slug);

            ws_client_handle_t old_ws = s_ws;
            char url[512];
            _build_ws_url(url, sizeof(url), idx);

            /* Reconnect with the new agent slug in the query string. */
            ws_client_handle_t new_ws = NULL;
            int attempts = 0;
            while (!new_ws && attempts < 5) {
                new_ws = ws_client_create(url, _on_vg_state, _on_tts_pcm, NULL);
                if (new_ws) ws_client_set_ctrl_cb(new_ws, _on_ws_ctrl);
                if (!new_ws) {
                    ESP_LOGW(TAG, "Agent switch WS connect failed (attempt %d/5)", attempts + 1);
                    vTaskDelay(pdMS_TO_TICKS(3000));
                }
                attempts++;
            }

            if (new_ws) {
                s_ws = new_ws;
                if (old_ws) ws_client_destroy(old_ws);
                wakeword_agent_switch_ack();
                /* Update the on-screen agent label */
                ui_face_set_agent(VT_AGENTS[idx].display);
                ESP_LOGI(TAG, "Agent switch complete → %s", VT_AGENTS[idx].display);
            } else {
                ESP_LOGE(TAG, "Agent switch failed — keeping previous connection");
                wakeword_agent_switch_ack();   /* clear pending to avoid retry storm */
            }
        }

        ws_client_handle_t ws = s_ws;  /* local copy; avoids torn reads */

        /* STOP protocol: on the rising edge of a TTS stop request (tap or
         * physical button during SPEAKING), tell the SERVER to abort the TTS
         * stream.  Locally the request only discards incoming PCM; without
         * this frame the server keeps streaming the full reply (8-30 s) and
         * the device stays deaf until state:idle finally arrives.  Sent from
         * voice_task (not the LVGL/button callbacks) so UI paths never touch
         * the ws-client lock. */
        static bool s_stop_sent = false;
        if (wakeword_tts_stop_requested()) {
            if (!s_stop_sent) {
                s_stop_sent = true;
                esp_err_t sr = ws_client_send_stop(ws);
                ESP_LOGI(TAG, "TTS stop → STOP frame to server (%s)",
                         esp_err_to_name(sr));
                vt_remote_log("STOP sent to server (%s)", esp_err_to_name(sr));
            }
        } else {
            s_stop_sent = false;   /* re-arm once the request is cleared */
        }

        /* One-shot boot marker on the remote-diag channel: confirms in the
         * gateway log which firmware the device is actually running, and the
         * reset reason (poweron/software/panic/brownout/task-wdt…) so crash
         * reboots are distinguishable from clean power cycles remotely. */
        static bool s_boot_logged = false;
        if (!s_boot_logged && ws_client_connected(ws)) {
            s_boot_logged = true;
            /* tts_buf identifies the build unambiguously: esp_app_desc's
             * compiled date/time can go stale when the version file isn't
             * regenerated, which made "which firmware is actually running?"
             * unanswerable remotely (observed: fresh flash, Jul 2 stamp). */
            /* VT_BUILD_TAG: bump on EVERY behavioural firmware change — the
             * only reliable remote build identifier (esp_app_desc stamps go
             * stale, and config-derived values collide across builds). */
            #define VT_BUILD_TAG "playdrive-0707m"
            vt_remote_log("boot: tag=" VT_BUILD_TAG " fw=%s reset=%d tts_buf=%u (remote-diag online)",
                          esp_app_get_description()->version,
                          (int)esp_reset_reason(),
                          (unsigned)TTS_STREAM_BUF_BYTES);
        }

        /* Capture one AFE-sized mic frame */
        size_t got = audio_capture_frame(frame_buf, (size_t)frame_bytes);

        /* Start CAPTURE on tap/wake-word — checked BEFORE the audio-failure
         * guard so a tap registers even on a transient mic failure.
         *
         * NOTE: capture has NO network dependency.  Recording starts
         * immediately whether or not the WS is up; connectivity only matters
         * at delivery time (which waits/retries across reconnects).  This is
         * the store-and-forward core: the hotspot can drop whenever it likes
         * without costing the user their query. */
        if (!capturing && wakeword_triggered()) {
            capturing = true;
            s_delivery_active = true;   /* face owned by us until delivery resolves */
            utt_len   = 0;
            ui_face_set_state(WS_VG_STATE_LISTENING);   /* local, immediate */
            ESP_LOGI(TAG, "Capture started");
            vt_remote_log("capture started");
        }

        if (got == 0) {
            /* No audio data — advance timers so a triggered utterance can still
             * time out and send END even when the codec is unavailable. */
            wakeword_tick();

            /* DIAGNOSTIC: a chronically dead mic (codec never ready, I2S underrun)
             * makes got==0 every loop, which is indistinguishable from idle and
             * silently kills the wake-word path.  Warn ~every 2 s so the trace
             * shows the mic is starved rather than the device being quiet. */
            static int s_zero_streak = 0;
            if (++s_zero_streak >= 200) {   /* ~200 × 10 ms delay ≈ 2 s */
                s_zero_streak = 0;
                ESP_LOGW(TAG, "audio_capture_frame returning 0 (mic not producing frames)");
                vt_remote_log("mic DEAD: audio_capture_frame returning 0");
            }

            /* Check utterance-end and keepalive before looping */
            if (capturing && wakeword_ended()) {
                capturing = false;
                ui_face_set_state(WS_VG_STATE_THINKING);
                bool ok = _deliver_utterance(utt_buf, utt_len);
                s_delivery_active = false;
                wakeword_clear();
                keepalive_frames = 0;
                if (!ok) ui_face_set_state(WS_VG_STATE_IDLE);
                /* On success the server drives THINKING→SPEAKING→IDLE. */
            } else if (!capturing) {
                if (++keepalive_frames >= KEEPALIVE_INTERVAL) {
                    keepalive_frames = 0;
                    ws_client_send_keepalive(ws);
                    if (!wakeword_tts_playing()) _send_status_beacon(ws, capturing);
                }
            }
            vTaskDelay(pdMS_TO_TICKS(10));
            continue;
        }

        /* Feed frame to the trigger detector.
         * Yield 1 ms after the AFE/WakeNet call so IDLE1 on CPU 1 can reset
         * the Task WDT.  Without this yield, wakeword_push_frame (esp-sr AFE
         * + WakeNet inference) runs back-to-back without blocking, starving
         * IDLE1 and triggering the 5 s TWDT — which panics and reboots the
         * device every ~5 minutes.  The 1 ms overhead per 16 ms audio frame
         * (~6 % CPU) is acceptable for the real-time audio loop. */
        wakeword_push_frame(frame_buf, got);
        vTaskDelay(pdMS_TO_TICKS(1));

        if (capturing) {
            /* RECORD to PSRAM — zero network dependency during capture. */
            if (utt_len + got <= UTT_BUF_MAX) {
                memcpy(utt_buf + utt_len, frame_buf, got);
                utt_len += got;
            } else {
                /* Buffer full (8 s) — force the utterance to end now. */
                wakeword_ptt_finish();
            }

            if (wakeword_ended()) {
                capturing = false;
                ESP_LOGI(TAG, "Capture ended: %u bytes — delivering", (unsigned)utt_len);
                ui_face_set_state(WS_VG_STATE_THINKING);
                bool ok = _deliver_utterance(utt_buf, utt_len);
                s_delivery_active = false;
                wakeword_clear();
                keepalive_frames = 0;   /* reset so we don't ping immediately after */
                if (!ok) ui_face_set_state(WS_VG_STATE_IDLE);
                /* On success the server drives THINKING→SPEAKING→IDLE. */
            }
        } else {
            /* Idle path: periodic keepalive to prevent NAT/relay dropping the
             * connection.  The server's own heartbeat goes server→device; this
             * goes device→server so the NAT table sees traffic in both directions. */
            if (++keepalive_frames >= KEEPALIVE_INTERVAL) {
                keepalive_frames = 0;
                ws_client_send_keepalive(ws);
                /* No beacon while TTS plays: a periodic TLS send overlapping
                 * a reply = occasional mid-reply click. */
                if (!wakeword_tts_playing()) _send_status_beacon(ws, capturing);
            }
        }
    }
}

/* ── app_main ─────────────────────────────────────────────────────────────── */

void app_main(void)
{
    ESP_LOGI(TAG, "Voice terminal starting");

    /* NVS — required by WiFi */
    esp_err_t err = nvs_flash_init();
    if (err == ESP_ERR_NVS_NO_FREE_PAGES || err == ESP_ERR_NVS_NEW_VERSION_FOUND) {
        ESP_ERROR_CHECK(nvs_flash_erase());
        err = nvs_flash_init();
    }
    ESP_ERROR_CHECK(err);

    ESP_LOGI(TAG, "PSRAM: %u KB available",
             (unsigned)(heap_caps_get_total_size(MALLOC_CAP_SPIRAM) / 1024));

    /* Pre-claim I2S at 16 kHz BEFORE bsp_display_start*() runs.
     * bsp_display_new() calls bsp_audio_init(NULL) which locks I2S to the BSP
     * default of 22050 Hz.  bsp_audio_init has an early-return guard that
     * ignores any later call once I2S is initialized, so audio_init() could
     * not override it — the AFE and codecs would receive wrong-rate audio,
     * causing garbled wakeword, silent mic, and crashes when PCM started flowing.
     * audio_preinit() grabs I2S at 16 kHz first; the display's call then hits
     * the guard and leaves the clock unchanged. */
    ESP_ERROR_CHECK(audio_preinit());

    /* Display + touch */
    ui_init();
    ESP_LOGI(TAG, "Display initialised");

    /* WiFi */
    ESP_ERROR_CHECK(esp_netif_init());
    ESP_ERROR_CHECK(esp_event_loop_create_default());
    wifi_init();

    /* Wait for first connection */
    xEventGroupWaitBits(s_wifi_eg, WIFI_CONNECTED_BIT, pdFALSE, pdTRUE,
                        portMAX_DELAY);
    vTaskDelay(pdMS_TO_TICKS(1500));

    ota_check(CONFIG_VT_VG_WS_URL, CONFIG_VT_VG_WS_TOKEN);
    /* WiFi is up and gateway was reachable — this image can self-update.
     * No-op on normal boots; cancels bootloader rollback on first boot of a new OTA image. */
    esp_ota_mark_app_valid_cancel_rollback();

    /* WiFi labels no longer needed — bring up face UI.
     * ui_face_init() manages its own bsp_display_lock internally. */
    ui_face_init();

    /* Audio codecs */
    if (audio_init() != ESP_OK) {
        ESP_LOGE(TAG, "Audio init failed — voice features disabled");
        ui_update(UI_READY, NULL);
        while (1) vTaskDelay(pdMS_TO_TICKS(10000));
    }

    /* TTS playback task — drains s_tts_buf on CPU 1 so websocket_task is
     * never blocked by i2s_channel_write during TTS streaming.
     * Back the stream buffer with PSRAM so we don't eat internal DRAM. */
    s_tts_sbuf_mem = heap_caps_malloc(TTS_STREAM_BUF_BYTES + 1,
                                      MALLOC_CAP_SPIRAM | MALLOC_CAP_8BIT);
    configASSERT(s_tts_sbuf_mem);
    s_tts_buf = xStreamBufferCreateStatic(TTS_STREAM_BUF_BYTES, 1,
                                          s_tts_sbuf_mem, &s_tts_sbuf_ctrl);
    configASSERT(s_tts_buf);
    /* Priority 6 — ABOVE voice_task/AFE (5) and websocket_task (4).  The
     * speaker writer must never miss its ~128 ms per-chunk deadline: at
     * equal/lower priority it time-sliced against the websocket task while
     * the TTS burst was being received, and every missed slice was a DMA
     * underrun = one click per chunk ("click at the end of each word",
     * live 2026-07-06, persisted through the 1.5 s pre-buffer).  Its duty
     * cycle is tiny (blocks on DMA), so it cannot starve the others. */
    xTaskCreatePinnedToCore(tts_task, "tts_play", 4096, NULL, 6, NULL, 1);

    /* Wake-word + PTT trigger */
    wakeword_init("model");  /* NULL → PTT only, "model" → PTT + WakeNet */

    /* Voice Gateway WebSocket client.
     *
     * Phase 1 (bring-up): plain ws:// to the LAN IP of marvin.
     *   Set CONFIG_VT_VG_WS_URL = ws://192.168.x.y:8765/voice in menuconfig.
     * Phase 2: wss:// through MicroLink.
     *   Set CONFIG_VT_VG_WS_URL = wss://marvin.tail240ea8.ts.net:8765/voice
     */
    ui_update(UI_READY, NULL);

    /* Diagnostic queue + sender task MUST exist before ws_client_create —
     * every diagnostic point posts into s_rlog_q from the first event on.
     * UI state updates need no worker task: ui_face_set_state() posts into
     * the LVGL thread via lv_async_call (see _on_vg_state). */
    s_rlog_q = xQueueCreate(16, RLOG_LINE_MAX);
    /* rlog_task sends diagnostics (TLS write on its own stack) — lowest prio.
     * 6 KB: the mbedTLS record-write path runs on this stack. */
    xTaskCreatePinnedToCore(rlog_task, "rlog", 6144, NULL, 2, &s_rlog_task_h, 1);

    /* Build the initial WS URL with the default agent (index 0 = Hermes). */
    char ws_url[512];
    _build_ws_url(ws_url, sizeof(ws_url), 0);
    ESP_LOGI(TAG, "Connecting to voice gateway: %.*s…",
             /* truncate to avoid logging the full token */
             (int)(strstr(ws_url, "?token=") ? strstr(ws_url, "?token=") - ws_url + 7 : 80),
             ws_url);

    while (!s_ws) {
        s_ws = ws_client_create(ws_url, _on_vg_state, _on_tts_pcm, NULL);
        if (s_ws) ws_client_set_ctrl_cb(s_ws, _on_ws_ctrl);
        if (!s_ws) {
            ESP_LOGW(TAG, "WebSocket connection failed — retrying in 5 s");
            ui_face_set_state(WS_VG_STATE_DISCONNECTED);
            vTaskDelay(pdMS_TO_TICKS(5000));
        }
    }
    ui_face_set_state(WS_VG_STATE_IDLE);

    /* Show the active agent name immediately after connecting.
     * ui_face_set_agent() acquires the display lock internally. */
    ui_face_set_agent(VT_AGENTS[0].display);

    ESP_LOGI(TAG, "Ready. Voice terminal active → agent: %s", VT_AGENTS[0].display);

    /* voice_task stack must come from PSRAM — internal DRAM is too fragmented by
     * the time we reach this point (AFE, TLS, DMA buffers already allocated).
     * pvPortMalloc still routes to internal DRAM even for large requests due to
     * heap fragmentation; use xTaskCreateStaticPinnedToCore with an explicit
     * PSRAM allocation instead. */
    #define VOICE_STACK_WORDS 4096   /* 16 KB — covers esp-sr AFE + codec call depth */
    static StaticTask_t s_voice_tcb;
    static voice_task_args_t voice_args;
    StackType_t *voice_stack = heap_caps_malloc(
        VOICE_STACK_WORDS * sizeof(StackType_t),
        MALLOC_CAP_SPIRAM | MALLOC_CAP_8BIT);
    if (!voice_stack) {
        ESP_LOGE(TAG, "voice_task PSRAM stack alloc failed (need %u bytes, PSRAM free %u)",
                 (unsigned)(VOICE_STACK_WORDS * sizeof(StackType_t)),
                 (unsigned)heap_caps_get_free_size(MALLOC_CAP_SPIRAM));
    } else {
        xTaskCreateStaticPinnedToCore(voice_task, "voice",
                                      VOICE_STACK_WORDS, &voice_args,
                                      5, voice_stack, &s_voice_tcb, 1);
        ESP_LOGI(TAG, "voice_task started (PSRAM stack, %u KB)",
                 (unsigned)(VOICE_STACK_WORDS * sizeof(StackType_t) / 1024));
    }

    /* Main task idles; voice_task owns the audio loop */
    while (1) {
        vTaskDelay(pdMS_TO_TICKS(10000));
    }
}
