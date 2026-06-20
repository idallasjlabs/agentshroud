// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
// AgentShroud™ USPTO Serial No. 99728633 · Patent Pending No. 64/018,744
#include "wakeword.h"
#include <string.h>
#include "audio.h"
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
static volatile bool s_triggered = false;
static volatile bool s_ended     = false;
static volatile bool s_ptt_held  = false;

#define VAD_TIMEOUT_MS 8000
static TickType_t s_trigger_tick = 0;

/* ── Touchscreen PTT (BSP_BUTTON_MAIN) ──────────────────────────────────── */
static button_handle_t s_bsp_buttons[BSP_BUTTON_NUM];
static int             s_bsp_btn_cnt = 0;

static void _btn_pressed(void *arg, void *data)
{
    if (!s_triggered) {
        ESP_LOGI(TAG, "Touch PTT: START");
        s_ptt_held     = true;
        s_triggered    = true;
        s_ended        = false;
        s_trigger_tick = xTaskGetTickCount();
    }
}

static void _btn_released(void *arg, void *data)
{
    if (s_ptt_held) {
        ESP_LOGI(TAG, "Touch PTT: END");
        s_ptt_held = false;
        s_ended    = true;
    }
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
    /* ── Touchscreen PTT ─────────────────────────────────────────────────── *
     * bsp_display_start_with_config() ran in ui_init() before this call, so
     * BSP_BUTTON_MAIN (touch panel) is available via bsp_iot_button_create(). */
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
    iot_button_register_cb(main_btn, BUTTON_PRESS_DOWN, _btn_pressed, NULL);
    iot_button_register_cb(main_btn, BUTTON_PRESS_UP,   _btn_released, NULL);
    ESP_LOGI(TAG, "Touch PTT registered (BSP_BUTTON_MAIN)");

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
    ESP_LOGI(TAG, "WakeNet + Touch-PTT ready — say 'Hi, ESP' or tap the screen");
#else
    (void)model_partition;
    ESP_LOGW(TAG, "esp-sr not compiled in — touch-PTT only");
#endif

    return ESP_OK;
}

void wakeword_push_frame(const uint8_t *pcm, size_t len)
{
    if (!pcm || len == 0) return;

    /* VAD timeout: auto-end a dangling triggered utterance. */
    if (s_triggered && !s_ended) {
        TickType_t elapsed_ms = (xTaskGetTickCount() - s_trigger_tick)
                                * portTICK_PERIOD_MS;
        if (elapsed_ms > VAD_TIMEOUT_MS) {
            ESP_LOGW(TAG, "VAD timeout — auto-ending utterance");
            s_ended    = true;
            s_ptt_held = false;
        }
    }

#if HAVE_ESP_SR
    if (!s_afe_iface || !s_afe_data) return;
    /* Only run AFE when idle (PTT-triggered utterances skip the AFE feed path). */
    if (s_ptt_held || (s_triggered && s_ended == false && !s_ptt_held == false)) return;
    if (s_triggered) return;

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
        ESP_LOGI(TAG, "WakeNet: 'Hi, ESP' detected");
        s_triggered    = true;
        s_ended        = false;
        s_trigger_tick = xTaskGetTickCount();
    } else if (s_triggered && result->vad_state == VAD_SILENCE) {
        /* VAD detected end of speech in a wake-word triggered utterance. */
        ESP_LOGI(TAG, "VAD: silence — utterance end");
        s_ended = true;
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

void wakeword_clear(void)
{
    s_triggered = false;
    s_ended     = false;
    s_ptt_held  = false;
}

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
