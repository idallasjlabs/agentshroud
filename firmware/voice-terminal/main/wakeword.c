// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
// AgentShroud™ USPTO Serial No. 99728633 · Patent Pending No. 64/018,744
#include "wakeword.h"
#include <string.h>
#include "audio.h"
#include "remote_log.h"
#include "bsp/esp-bsp.h"
#include "iot_button.h"
#include "esp_log.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

/* esp-sr AFE + WakeNet.
 * The esp-sr component exposes its public headers via the esp32s3 include path.
 * model_path.h (in src/include, pulled in by esp_afe_config.h) provides
 * esp_srmodel_init / esp_srmodel_filter / srmodel_list_t. */
#if __has_include("esp_afe_sr_iface.h")
#  include "esp_afe_sr_iface.h"    /* esp_afe_sr_data_t, afe_fetch_result_t */
#  include "esp_afe_sr_models.h"   /* esp_afe_handle_from_config              */
#  include "esp_afe_config.h"      /* afe_config_t, afe_config_init/alloc/free */
#  include "esp_wn_iface.h"        /* wakenet_state_t, WAKENET_DETECTED       */
#  include "esp_wn_models.h"       /* ESP_WN_PREFIX                           */
#  include "model_path.h"          /* srmodel_list_t, esp_srmodel_init/filter */
#  define HAVE_ESP_SR 1
#else
#  define HAVE_ESP_SR 0
#endif

static const char *TAG = "wakeword";

/* ── Shared state ──────────────────────────────────────────────────────────── */
static volatile bool s_triggered   = false;
static volatile bool s_ended       = false;
static volatile bool s_ptt_held    = false;
/* Set while TTS is playing so speaker echo cannot retrigger the mic pipeline. */
static volatile bool s_tts_playing = false;
/* Set when the user taps/presses during SPEAKING to interrupt TTS immediately. */
static volatile bool s_tts_stop_requested = false;

/* Hard cap on utterance length — safety net, NOT the normal end path.
 * Normal end: tap-to-stop, long-press release, or VAD silence endpointing. */
#define VAD_TIMEOUT_MS 8000
static TickType_t s_trigger_tick = 0;

/* ── VAD silence endpointing ──────────────────────────────────────────────── *
 * Ends an utterance ~VT_VAD_END_SILENCE_MS after the user stops speaking,
 * instead of waiting for the 8 s cap (which forced up to 8 s of dead air
 * before THINKING).  Requires ≥ VT_VAD_MIN_SPEECH_MS of detected speech first
 * so an accidental tap with no speech still waits for the cap rather than
 * ending instantly on ambient silence.  Counters advance only while the AFE
 * is being fed (i.e. not during TTS playback) and only for hands-free
 * utterances — while the physical button is HELD, release ends the utterance,
 * not silence. */
#define VT_VAD_MIN_SPEECH_MS   300
#define VT_VAD_END_SILENCE_MS  800
static uint32_t s_vad_speech_ms  = 0;
static uint32_t s_vad_silence_ms = 0;

/* ── Agent-toggle state ────────────────────────────────────────────────────── */
/* Agent index cycles through the list in app_main.c on each button press.
 * s_agent_switch_pending signals voice_task to reconnect with the new agent. */
static volatile int  s_agent_index          = 0;
static volatile bool s_agent_switch_pending = false;

/* ── Physical button PTT (BSP_BUTTON_MAIN — top button on BOX-3) ─────────── */
static button_handle_t s_bsp_buttons[BSP_BUTTON_NUM];
static int             s_bsp_btn_cnt = 0;

/* Shared PTT logic — called from physical button callbacks and from the
 * LVGL touch overlay in ui_face.c (wakeword_ptt_press / wakeword_ptt_release). */
static void _ptt_start(void)
{
    if (!s_triggered && !s_tts_playing) {
        ESP_LOGI(TAG, "PTT: START");
        vt_remote_log("PTT START");
        s_ptt_held     = true;
        s_triggered    = true;
        s_ended        = false;
        s_trigger_tick = xTaskGetTickCount();
        s_vad_speech_ms  = 0;
        s_vad_silence_ms = 0;
    } else {
        /* DIAGNOSTIC: the guard rejected this press.  Without this line a tap that
         * lands while s_triggered is already latched (or during TTS) is a totally
         * silent no-op — the #1 cause of "tap does nothing".  Now the trace says so. */
        ESP_LOGW(TAG, "PTT: START ignored — triggered=%d tts_playing=%d",
                 (int)s_triggered, (int)s_tts_playing);
        vt_remote_log("PTT START ignored — triggered=%d tts=%d",
                      (int)s_triggered, (int)s_tts_playing);
    }
}

static void _ptt_end(void)
{
    if (s_ptt_held) {
        s_ptt_held = false;
        TickType_t elapsed_ms = (xTaskGetTickCount() - s_trigger_tick)
                                * portTICK_PERIOD_MS;
        if (elapsed_ms >= 1000) {
            /* Long press — end immediately on release. */
            ESP_LOGI(TAG, "PTT: END (held %ums)", (unsigned)elapsed_ms);
            s_ended = true;
        } else {
            /* Short tap (<1 s): stay triggered so the user can speak after
             * lifting their finger.  VAD timeout (8 s) will end the utterance. */
            ESP_LOGI(TAG, "PTT: tap (%ums) — VAD will end", (unsigned)elapsed_ms);
        }
    }
}

static void _btn_pressed(void *arg, void *data)
{
    if (s_tts_playing) {
        /* Physical button pressed during TTS — interrupt playback. */
        ESP_LOGI(TAG, "Physical button: TTS interrupt");
        s_tts_stop_requested = true;
    } else {
        _ptt_start();
    }
}

static void _btn_released(void *arg, void *data)
{
    /* Only end PTT if we started one; a stop-press has no PTT to end. */
    if (!s_tts_stop_requested) {
        _ptt_end();
    }
}

/* Agent-toggle button: advance to the next agent on press.
 * Declared extern here; the table is defined in app_main.c. */
extern int  vt_agent_count(void);   /* returns the length of the agent table */

static void _agent_btn_pressed(void *arg, void *data)
{
    int count = vt_agent_count();
    if (count < 1) return;
    /* Atomic-ish under FreeRTOS single-core critical section (portENTER_CRITICAL
     * is too heavy in a callback; use __atomic or accept the race on a single
     * assignment — either s_agent_index update or the switch flag is acceptable
     * to miss by one; the physical button press repeats easily). */
    int next = ((int)s_agent_index + 1) % count;
    s_agent_index = next;
    s_agent_switch_pending = true;
    ESP_LOGI(TAG, "Agent toggle → index %d", next);
}

/* ── AFE / WakeNet ─────────────────────────────────────────────────────────── */
#if HAVE_ESP_SR
static const esp_afe_sr_iface_t *s_afe_iface = NULL;  /* vtable */
static esp_afe_sr_data_t        *s_afe_data  = NULL;  /* instance */
static srmodel_list_t           *s_models    = NULL;
static afe_config_t             *s_afe_cfg   = NULL;
static int                       s_feed_bytes = 0;    /* bytes per feed() call */
#endif

/* ── Public API ─────────────────────────────────────────────────────────────── */

esp_err_t wakeword_init(const char *model_partition)
{
    /* ── Physical button PTT (BSP_BUTTON_MAIN) ──────────────────────────── *
     * bsp_display_start_with_config() ran in ui_init() before this call, so
     * the BSP button registry is populated. BSP_BUTTON_MAIN is the top button
     * on the BOX-3 (NOT the touchscreen — touchscreen PTT is handled separately
     * via the LVGL overlay in ui_face.c calling wakeword_ptt_press/release). */
    esp_err_t ret = bsp_iot_button_create(s_bsp_buttons, &s_bsp_btn_cnt,
                                          BSP_BUTTON_NUM);
    if (ret != ESP_OK) {
        ESP_LOGE(TAG, "bsp_iot_button_create: %s", esp_err_to_name(ret));
        return ret;
    }
    button_handle_t main_btn = s_bsp_buttons[BSP_BUTTON_MAIN];
    if (!main_btn) {
        ESP_LOGE(TAG, "BSP_BUTTON_MAIN handle is NULL");
        return ESP_FAIL;
    }
    iot_button_register_cb(main_btn, BUTTON_PRESS_DOWN, NULL, _btn_pressed, NULL);
    iot_button_register_cb(main_btn, BUTTON_PRESS_UP,   NULL, _btn_released, NULL);
    ESP_LOGI(TAG, "Physical button PTT registered (BSP_BUTTON_MAIN)");

    /* Agent-toggle button — BSP_BUTTON_MUTE (GPIO1) on the BOX-3.
     * The button is created by bsp_iot_button_create() above; we only need to
     * register our callback.  If the handle is NULL (board variant without the
     * button), skip silently — agent selection works only via ?agent= URL param. */
    if (s_bsp_btn_cnt > BSP_BUTTON_MUTE) {
        button_handle_t mute_btn = s_bsp_buttons[BSP_BUTTON_MUTE];
        if (mute_btn) {
            iot_button_register_cb(mute_btn, BUTTON_PRESS_DOWN, NULL, _agent_btn_pressed, NULL);
            ESP_LOGI(TAG, "Agent-toggle button registered (BSP_BUTTON_MUTE)");
        } else {
            ESP_LOGW(TAG, "BSP_BUTTON_MUTE handle NULL — agent toggle via button disabled");
        }
    } else {
        ESP_LOGW(TAG, "BSP_BUTTON_MUTE index %d >= bsp_btn_cnt %d — skipped",
                 BSP_BUTTON_MUTE, s_bsp_btn_cnt);
    }

#if HAVE_ESP_SR
    if (!model_partition) {
        ESP_LOGW(TAG, "No model partition — WakeNet disabled, touch-PTT only");
        return ESP_OK;
    }

    /* 1. Load models from 'model' SPIFFS partition. */
    s_models = esp_srmodel_init(model_partition);
    if (!s_models) {
        ESP_LOGE(TAG, "esp_srmodel_init('%s') failed", model_partition);
        return ESP_OK;   /* degrade to touch-PTT only */
    }

    /* 2. Find the Hi,ESP WakeNet model. */
    char *wn_name = esp_srmodel_filter(s_models, ESP_WN_PREFIX, NULL);
    if (!wn_name) {
        ESP_LOGE(TAG, "No WakeNet model in partition '%s'", model_partition);
        return ESP_OK;
    }
    ESP_LOGI(TAG, "WakeNet model: %s", wn_name);

    /* 3. Build AFE config — single mic ("M"), SR mode, low-cost. */
    s_afe_cfg = afe_config_init("M", s_models, AFE_TYPE_SR, AFE_MODE_LOW_COST);
    if (!s_afe_cfg) {
        ESP_LOGE(TAG, "afe_config_init failed");
        return ESP_OK;
    }
    s_afe_cfg->wakenet_init        = true;
    s_afe_cfg->wakenet_model_name  = wn_name;
    s_afe_cfg->wakenet_model_name_2 = NULL;
    s_afe_cfg->wakenet_mode        = DET_MODE_90;
    s_afe_cfg->vad_init            = true;
    /* Most aggressive silence classification: office ambience (HVAC/chatter)
     * pinned the default WebRTC VAD at VAD_SPEECH for entire utterances
     * (vad: trace showed sil=0ms for 8 s straight, 2026-07-06), so the
     * silence endpointing never fired outside quiet rooms. */
    s_afe_cfg->vad_mode            = VAD_MODE_4;
    s_afe_cfg->aec_init            = false;   /* BOX-3: no echo path */
    s_afe_cfg->se_init             = false;
    s_afe_cfg->afe_perferred_core  = 1;
    s_afe_cfg->afe_perferred_priority = 5;
    s_afe_cfg->afe_ringbuf_size    = 50;
    s_afe_cfg->memory_alloc_mode   = AFE_MEMORY_ALLOC_MORE_PSRAM;
    s_afe_cfg->debug_init          = false;
    /* pcm_config — afe_config_init("M",...) already sets 1 mic + 16 kHz;
     * confirm sample_rate in case the default differs. */
    s_afe_cfg->pcm_config.sample_rate = AUDIO_SAMPLE_RATE;

    /* 4. Get the iface vtable from the config and create the AFE instance. */
    s_afe_iface = esp_afe_handle_from_config(s_afe_cfg);
    if (!s_afe_iface) {
        ESP_LOGE(TAG, "esp_afe_handle_from_config failed");
        afe_config_free(s_afe_cfg);
        s_afe_cfg = NULL;
        return ESP_OK;
    }
    s_afe_data = s_afe_iface->create_from_config(s_afe_cfg);
    if (!s_afe_data) {
        ESP_LOGE(TAG, "afe create_from_config failed");
        afe_config_free(s_afe_cfg);
        s_afe_cfg = NULL;
        s_afe_iface = NULL;
        return ESP_OK;
    }

    /* 5. Determine required feed chunk size. */
    int feed_samples = s_afe_iface->get_feed_chunksize(s_afe_data);
    s_feed_bytes = feed_samples * (int)sizeof(int16_t);
    ESP_LOGI(TAG, "AFE feed chunk: %d samples = %d bytes", feed_samples, s_feed_bytes);
    ESP_LOGI(TAG, "WakeNet + PTT ready — say 'Hi, ESP' or tap the screen");
#else
    (void)model_partition;
    ESP_LOGW(TAG, "esp-sr not compiled in — touch-PTT only");
#endif

    return ESP_OK;
}

void wakeword_push_frame(const uint8_t *pcm, size_t len)
{
    /* VAD timeout: auto-end a dangling triggered utterance.
     * Runs BEFORE the pcm/len guard so that the 8-second safety net fires
     * even when audio capture returns 0 bytes (codec not ready, I2S underrun,
     * etc.).  Without this, a stuck streaming state can never self-recover. */
    if (s_triggered && !s_ended) {
        TickType_t elapsed_ms = (xTaskGetTickCount() - s_trigger_tick)
                                * portTICK_PERIOD_MS;
        if (elapsed_ms > VAD_TIMEOUT_MS) {
            ESP_LOGW(TAG, "VAD timeout — auto-ending utterance");
            vt_remote_log("VAD timeout (8s) — auto-ending utterance");
            s_ended    = true;
            s_ptt_held = false;
        }
    }

    if (!pcm || len == 0) return;

#if HAVE_ESP_SR
    if (!s_afe_iface || !s_afe_data) {
        /* DIAGNOSTIC (one-shot): AFE never initialised → WakeNet is permanently
         * deaf.  Latch so we warn once instead of every 16 ms frame. */
        static bool s_afe_warned = false;
        if (!s_afe_warned) {
            s_afe_warned = true;
            ESP_LOGW(TAG, "WakeNet feed skipped — AFE not initialised (wake word disabled)");
            vt_remote_log("WakeNet DISABLED: AFE not initialised");
        }
        return;
    }
    /* Skip AFE feed ONLY during TTS playback: speaker echo would retrigger
     * WakeNet and pollute the VAD.  During a triggered utterance the feed
     * KEEPS RUNNING so the AFE's WebRTC VAD can endpoint it — the old code
     * skipped feeding while triggered, which made the VAD_SILENCE branch dead
     * code and left the 8 s cap as the only hands-free end path (up to 8 s of
     * dead air after the user stopped speaking). */
    bool skip_feed = s_tts_playing;
    /* DIAGNOSTIC (transition-edge): log only when the skip state flips so we can
     * see the AFE going deaf/live in the trace without per-frame spam. */
    static int s_last_skip = -1;
    if ((int)skip_feed != s_last_skip) {
        s_last_skip = (int)skip_feed;
        ESP_LOGW(TAG, "AFE feed %s (ptt=%d triggered=%d tts=%d)",
                 skip_feed ? "OFF" : "ON",
                 (int)s_ptt_held, (int)s_triggered, (int)s_tts_playing);
        vt_remote_log("AFE feed %s (ptt=%d triggered=%d tts=%d)",
                      skip_feed ? "OFF" : "ON",
                      (int)s_ptt_held, (int)s_triggered, (int)s_tts_playing);
    }
    if (skip_feed) return;

    /* Feed the mic frame into the AFE pipeline. */
    int rc = s_afe_iface->feed(s_afe_data, (const int16_t *)pcm);
    if (rc < 0) {
        ESP_LOGD(TAG, "AFE feed returned %d (queue full, skip)", rc);
        return;
    }

    /* Fetch processed result — may return NULL if not ready yet. */
    afe_fetch_result_t *result = s_afe_iface->fetch(s_afe_data);
    if (!result) return;

    if (result->wakeup_state == WAKENET_DETECTED) {
        if (!s_triggered) {
            ESP_LOGI(TAG, "WakeNet: 'Hi, ESP' detected");
            vt_remote_log("WakeNet DETECTED 'Hi, ESP'");
            s_triggered      = true;
            s_ended          = false;
            s_trigger_tick   = xTaskGetTickCount();
            s_vad_speech_ms  = 0;
            s_vad_silence_ms = 0;
        }
        /* else: detection during an active capture (e.g. the user says the
         * wake word again mid-utterance) — ignore, capture continues. */
    }

    /* Silence endpointing — hands-free utterances only (tap or wake word).
     * While the physical button is HELD, its release ends the utterance. */
    if (s_triggered && !s_ended && !s_ptt_held) {
        /* One AFE feed chunk = len/2 samples at 16 kHz. */
        uint32_t frame_ms = (uint32_t)(len / 2) * 1000u / 16000u;
        if (result->vad_state == VAD_SILENCE) {
            s_vad_silence_ms += frame_ms;
        } else {
            s_vad_speech_ms += frame_ms;
            s_vad_silence_ms = 0;
        }
        /* DIAGNOSTIC (1 Hz): the counters are the only remote evidence of what
         * the WebRTC VAD is reporting.  Live 2026-07-05: first field test hit
         * the 8 s cap with no endpoint — this trace shows whether vad_state
         * was pinned at SPEECH (noise/sensitivity) or silence never summed. */
        static uint32_t s_vad_dbg_ms = 0;
        s_vad_dbg_ms += frame_ms;
        if (s_vad_dbg_ms >= 1000) {
            s_vad_dbg_ms = 0;
            vt_remote_log("vad: speech=%ums sil=%ums state=%d",
                          (unsigned)s_vad_speech_ms, (unsigned)s_vad_silence_ms,
                          (int)result->vad_state);
        }
        if (s_vad_speech_ms >= VT_VAD_MIN_SPEECH_MS &&
            s_vad_silence_ms >= VT_VAD_END_SILENCE_MS) {
            ESP_LOGI(TAG, "VAD endpoint: speech=%ums silence=%ums — ending utterance",
                     (unsigned)s_vad_speech_ms, (unsigned)s_vad_silence_ms);
            vt_remote_log("VAD endpoint: speech=%ums silence=%ums — ending",
                          (unsigned)s_vad_speech_ms, (unsigned)s_vad_silence_ms);
            s_ended = true;
        }
    }
#endif
}

int wakeword_feed_bytes(void)
{
#if HAVE_ESP_SR
    return (s_feed_bytes > 0) ? s_feed_bytes : (AUDIO_FRAME_BYTES_MAX / 2);
#else
    return AUDIO_FRAME_BYTES_MAX / 2;   /* 512 bytes default */
#endif
}

bool wakeword_triggered(void) { return s_triggered; }
bool wakeword_ended(void)     { return s_ended; }

void wakeword_tick(void)
{
    /* Advance the VAD timeout even when no audio frame is available.
     * Mirrors the timeout block at the top of wakeword_push_frame(). */
    if (s_triggered && !s_ended) {
        TickType_t elapsed_ms = (xTaskGetTickCount() - s_trigger_tick)
                                * portTICK_PERIOD_MS;
        if (elapsed_ms > VAD_TIMEOUT_MS) {
            ESP_LOGW(TAG, "VAD timeout (no audio) — auto-ending utterance");
            vt_remote_log("VAD timeout (no audio) — auto-ending utterance");
            s_ended    = true;
            s_ptt_held = false;
        }
    }
}

void wakeword_clear(void)
{
    s_triggered      = false;
    s_ended          = false;
    s_ptt_held       = false;
    s_vad_speech_ms  = 0;
    s_vad_silence_ms = 0;
}

/* Public PTT API — called from the LVGL touch overlay in ui_face.c. */
void wakeword_ptt_press(void)   { _ptt_start(); }
void wakeword_ptt_release(void) { _ptt_end(); }

void wakeword_ptt_finish(void)
{
    /* Force-end a triggered utterance (tap-to-stop UI model).
     * Sets s_ended so voice_task sends END on the next loop iteration.
     * Clears s_ptt_held so a trailing LV_EVENT_RELEASED cannot double-fire
     * _ptt_end() and flip s_ended back to false via a short-tap path. */
    if (s_triggered && !s_ended) {
        ESP_LOGI(TAG, "PTT: finish (user tap-to-stop)");
        vt_remote_log("PTT finish (tap-to-stop)");
        s_ended    = true;
        s_ptt_held = false;
    }
}

void wakeword_set_tts_playing(bool playing)
{
    s_tts_playing = playing;
    if (!playing) {
        /* When TTS ends, clear any stale trigger that may have latched during
         * the SPEAKING window (e.g. phantom wake-word on speaker echo). */
        if (!s_ptt_held) {
            s_triggered = false;
            s_ended     = false;
        }
    }
}

/* ── Agent-toggle public API ─────────────────────────────────────────────── */

void wakeword_next_agent(void)
{
    int count = vt_agent_count();
    if (count < 1) return;
    s_agent_index = ((int)s_agent_index + 1) % count;
    s_agent_switch_pending = true;
    ESP_LOGI(TAG, "wakeword_next_agent() → index %d", (int)s_agent_index);
}

bool wakeword_agent_switch_pending(void)
{
    return s_agent_switch_pending;
}

void wakeword_agent_switch_ack(void)
{
    s_agent_switch_pending = false;
}

int wakeword_agent_index(void)
{
    return (int)s_agent_index;
}

/* ── TTS interrupt public API ────────────────────────────────────────────── */

void wakeword_tts_stop_request(void)
{
    if (s_tts_playing) {
        ESP_LOGI(TAG, "TTS stop requested");
        s_tts_stop_requested = true;
    }
}

bool wakeword_tts_stop_requested(void) { return s_tts_stop_requested; }

void wakeword_tts_stop_clear(void)     { s_tts_stop_requested = false; }

void wakeword_deinit(void)
{
    for (int i = 0; i < s_bsp_btn_cnt; i++) {
        if (s_bsp_buttons[i]) {
            iot_button_delete(s_bsp_buttons[i]);
            s_bsp_buttons[i] = NULL;
        }
    }
    s_bsp_btn_cnt = 0;

#if HAVE_ESP_SR
    if (s_afe_iface && s_afe_data) {
        s_afe_iface->destroy(s_afe_data);
        s_afe_data  = NULL;
        s_afe_iface = NULL;
    }
    if (s_afe_cfg) {
        afe_config_free(s_afe_cfg);
        s_afe_cfg = NULL;
    }
    if (s_models) {
        esp_srmodel_deinit(s_models);
        s_models = NULL;
    }
    s_feed_bytes = 0;
#endif
}
