#include <stdlib.h>
#include <string.h>
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
    { "hermes",  "Hermes"   },   /* Hermes agentic assistant — synchronous OpenAI-compat reply */
    { "direct",  "Fast LLM" },   /* Low-latency gateway LLM proxy — no agentic tools          */
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
#define TTS_STREAM_BUF_BYTES   (64 * 1024)   /* ~2 s at 16000 Hz 16-bit mono */
static StreamBufferHandle_t  s_tts_buf      = NULL;
static StaticStreamBuffer_t  s_tts_sbuf_ctrl;     /* control struct — internal DRAM (BSS) */
static uint8_t              *s_tts_sbuf_mem = NULL; /* backing store — PSRAM */

static void tts_task(void *arg)
{
    static uint8_t play_chunk[4096];
    while (1) {
        size_t got = xStreamBufferReceive(s_tts_buf, play_chunk, sizeof(play_chunk),
                                          pdMS_TO_TICKS(100));
        if (got > 0 && !wakeword_tts_stop_requested()) {
            audio_play(play_chunk, got);
        }
    }
}

/* ── Voice Gateway callbacks ──────────────────────────────────────────────── */

static ws_vg_state_t s_prev_vg_state = WS_VG_STATE_DISCONNECTED;

static void _on_vg_state(ws_vg_state_t state, void *ctx)
{
    if (state == WS_VG_STATE_SPEAKING) {
        wakeword_set_tts_playing(true);
        ui_face_set_state(state);

    } else if (state == WS_VG_STATE_IDLE) {
        bool post_tts    = (s_prev_vg_state == WS_VG_STATE_SPEAKING);
        bool interrupted = wakeword_tts_stop_requested();
        wakeword_set_tts_playing(false);
        wakeword_tts_stop_clear();

        if (post_tts && !interrupted) {
            /* TTS finished naturally — auto-listen so the user can ask a
             * follow-up without saying "Hi, ESP" again.  VAD timeout (8 s of
             * silence) will send END and return to idle if no follow-up. */
            wakeword_ptt_press();
            ui_face_set_state(WS_VG_STATE_LISTENING);
        } else if (!wakeword_triggered()) {
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
    /* Non-blocking push: if the buffer is full, drop this chunk rather than
     * stalling websocket_task (which would corrupt the WS receive loop). */
    if (s_tts_buf && !wakeword_tts_stop_requested()) {
        xStreamBufferSend(s_tts_buf, pcm, len, 0);
    }
}

/* ── Voice task ───────────────────────────────────────────────────────────── */

/* Shared WS handle — written by app_main, read/written by voice_task on switch. */
static volatile ws_client_handle_t s_ws = NULL;

typedef struct {
    /* intentionally empty — voice_task reads s_ws and wakeword state directly */
    int unused;
} voice_task_args_t;

static void voice_task(void *arg)
{
    (void)arg;

    /* Frame size is determined by the AFE at init time — must match afe->get_feed_chunksize(). */
    const int frame_bytes = wakeword_feed_bytes();
    uint8_t  *frame_buf   = (uint8_t *)malloc(frame_bytes);
    if (!frame_buf) {
        ESP_LOGE(TAG, "voice_task: frame_buf alloc failed (%d bytes)", frame_bytes);
        vTaskDelete(NULL);
        return;
    }

    bool streaming = false;
    ESP_LOGI(TAG, "Voice task running (frame=%d bytes)", frame_bytes);

    while (1) {
        /* ── Agent switch ── */
        if (!streaming && wakeword_agent_switch_pending()) {
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

        /* Capture one AFE-sized mic frame */
        size_t got = audio_capture_frame(frame_buf, (size_t)frame_bytes);
        if (got == 0) {
            vTaskDelay(pdMS_TO_TICKS(10));
            continue;
        }

        /* Feed frame to the trigger detector */
        wakeword_push_frame(frame_buf, got);

        if (!streaming && wakeword_triggered()) {
            /* New utterance: signal gateway and start streaming */
            if (ws_client_connected(ws)) {
                ws_client_send_listen(ws);
                streaming = true;
                ESP_LOGI(TAG, "Utterance started");
            } else {
                /* WS is down — clear the trigger so the next tap/wake-word works
                 * once the connection recovers.  Without this, s_triggered stays
                 * true and all future activations are silently dropped. */
                wakeword_clear();
                ESP_LOGW(TAG, "Trigger while disconnected — cleared");
            }
        }

        if (streaming) {
            /* Stream PCM to gateway */
            ws_client_send_pcm(ws, frame_buf, got);

            if (wakeword_ended()) {
                /* Utterance complete */
                ws_client_send_end(ws);
                streaming = false;
                wakeword_clear();
                ESP_LOGI(TAG, "Utterance ended");
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
    xTaskCreatePinnedToCore(tts_task, "tts_play", 4096, NULL, 4, NULL, 1);

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

    /* Build the initial WS URL with the default agent (index 0 = Hermes). */
    char ws_url[512];
    _build_ws_url(ws_url, sizeof(ws_url), 0);
    ESP_LOGI(TAG, "Connecting to voice gateway: %.*s…",
             /* truncate to avoid logging the full token */
             (int)(strstr(ws_url, "?token=") ? strstr(ws_url, "?token=") - ws_url + 7 : 80),
             ws_url);

    while (!s_ws) {
        s_ws = ws_client_create(ws_url, _on_vg_state, _on_tts_pcm, NULL);
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

    static voice_task_args_t voice_args;
    xTaskCreatePinnedToCore(voice_task, "voice", 8192, &voice_args,
                            5, NULL, 1);  /* pin to core 1, away from WiFi */

    /* Main task idles; voice_task owns the audio loop */
    while (1) {
        vTaskDelay(pdMS_TO_TICKS(10000));
    }
}
