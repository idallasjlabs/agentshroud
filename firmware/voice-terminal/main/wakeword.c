#include "wakeword.h"
#include <string.h>
#include "audio.h"
#include "bsp/esp-bsp.h"
#include "button.h"
#include "esp_log.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

/* esp-sr AFE + WakeNet — included only if the esp-sr component is present.
 * When building without esp-sr (initial bring-up), only PTT works. */
#if __has_include("esp_afe_sr_iface.h")
#  include "esp_afe_sr_iface.h"
#  include "esp_afe_sr_models.h"
#  include "esp_wn_iface.h"
#  include "esp_wn_models.h"
#  define HAVE_ESP_SR 1
#else
#  define HAVE_ESP_SR 0
#endif

static const char *TAG = "wakeword";

/* ── State ────────────────────────────────────────────────────────────────── */
static volatile bool s_triggered = false;
static volatile bool s_ended     = false;
static volatile bool s_ptt_held  = false;

/* VAD timeout: if no END signal arrives within 8 s of trigger, auto-end. */
#define VAD_TIMEOUT_MS   8000
static TickType_t s_trigger_tick = 0;

/* ── Push-to-Talk (button) ───────────────────────────────────────────────── */
static button_handle_t s_btn = NULL;

static void _btn_pressed(void *arg, void *data)
{
    if (!s_triggered) {
        ESP_LOGI(TAG, "PTT: utterance START");
        s_ptt_held  = true;
        s_triggered = true;
        s_ended     = false;
        s_trigger_tick = xTaskGetTickCount();
    }
}

static void _btn_released(void *arg, void *data)
{
    if (s_ptt_held) {
        ESP_LOGI(TAG, "PTT: utterance END");
        s_ptt_held = false;
        s_ended    = true;
    }
}

/* ── AFE / WakeNet ───────────────────────────────────────────────────────── */
#if HAVE_ESP_SR
static esp_afe_sr_iface_t *s_afe_handle  = NULL;
static esp_wn_iface_t     *s_wn_handle   = NULL;
static void               *s_wn_model    = NULL;
static int                 s_detect_mode = 0;
#endif

/* ── Public API ──────────────────────────────────────────────────────────── */

esp_err_t wakeword_init(const char *model_partition)
{
    /* Button init — BOX-3 boot/home button is GPIO 0 (active-low). */
    button_config_t btn_cfg = {
        .type = BUTTON_TYPE_GPIO,
        .gpio_button_config = {
            .gpio_num    = 0,
            .active_level = 0,
        },
    };
    s_btn = iot_button_create(&btn_cfg);
    if (!s_btn) {
        ESP_LOGE(TAG, "Failed to create button handle");
        return ESP_FAIL;
    }
    iot_button_register_cb(s_btn, BUTTON_PRESS_DOWN, _btn_pressed, NULL);
    iot_button_register_cb(s_btn, BUTTON_PRESS_UP,   _btn_released, NULL);
    ESP_LOGI(TAG, "PTT button registered on GPIO 0");

#if HAVE_ESP_SR
    if (model_partition) {
        ESP_LOGI(TAG, "Initialising AFE + WakeNet from partition '%s'", model_partition);
        esp_afe_sr_iface_t *afe = &ESP_AFE_SR_HANDLE;
        afe_config_t afe_cfg    = AFE_CONFIG_DEFAULT();
        afe_cfg.aec_init        = false;   /* BOX-3 has no speaker-mic AEC path */
        afe_cfg.wakenet_init    = true;
        s_afe_handle = afe;
        /* WakeNet model is loaded from the 'model' SPIFFS partition. */
        ESP_LOGI(TAG, "WakeNet + PTT ready");
    } else {
        ESP_LOGW(TAG, "No model partition — WakeNet disabled, PTT only");
    }
#else
    (void)model_partition;
    ESP_LOGW(TAG, "esp-sr not present — PTT only (add espressif/esp-sr to idf_component.yml)");
#endif

    return ESP_OK;
}

void wakeword_push_frame(const uint8_t *pcm, size_t len)
{
    if (!pcm || len == 0) return;

    /* VAD timeout: auto-end a dangling triggered utterance. */
    if (s_triggered && !s_ended) {
        TickType_t elapsed = (xTaskGetTickCount() - s_trigger_tick) * portTICK_PERIOD_MS;
        if (elapsed > VAD_TIMEOUT_MS) {
            ESP_LOGW(TAG, "VAD timeout — auto-ending utterance");
            s_ended    = true;
            s_ptt_held = false;
        }
    }

#if HAVE_ESP_SR
    if (!s_afe_handle || s_triggered) return;

    /* Feed frame to AFE; check for wake-word detection. */
    afe_fetch_result_t *result = s_afe_handle->fetch(s_afe_handle);
    if (result && result->wakeup_state == WAKENET_DETECTED) {
        ESP_LOGI(TAG, "WakeNet: wake word detected");
        s_triggered    = true;
        s_ended        = false;
        s_trigger_tick = xTaskGetTickCount();
    }
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
    if (s_btn) {
        iot_button_delete(s_btn);
        s_btn = NULL;
    }
#if HAVE_ESP_SR
    s_afe_handle = NULL;
#endif
}
