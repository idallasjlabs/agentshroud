#include "audio.h"
#include <string.h>
#include "bsp/esp-bsp.h"
#include "esp_codec_dev.h"
#include "esp_log.h"

static const char *TAG = "audio";

static esp_codec_dev_handle_t s_mic    = NULL;
static esp_codec_dev_handle_t s_spk    = NULL;
static bool                   s_ready  = false;

/* The ES8311/NS4150 output stage distorts audibly above ~85 codec volume
 * regardless of digital headroom (owner-verified 2026-07-07: clean at 75-80,
 * crackle at 90-100 even with -4.5 dB digital scaling).  Map the user's
 * 0-100% onto the clean 0-85 codec range so "100%" = loudest clean output
 * and the distortion zone is unreachable. */
#define AUDIO_CODEC_VOL_MAX 85

/* Zipper-free volume state — see audio_set_volume()/audio_volume_tick(). */
static volatile int  s_vol_target_pct = -1;   /* -1 = uninitialised */
static volatile int  s_vol_actual     = -1;   /* codec units */
static volatile bool s_vol_dirty      = false;

/* Shared I2S config: 16 kHz mono 16-bit, BOX-3 GPIO pins.
 * Used by both audio_preinit() and audio_init() so the config is defined once. */
static const i2s_std_config_t s_i2s_cfg = {
    .clk_cfg  = I2S_STD_CLK_DEFAULT_CONFIG(AUDIO_SAMPLE_RATE),
    .slot_cfg = I2S_STD_PHILIP_SLOT_DEFAULT_CONFIG(I2S_DATA_BIT_WIDTH_16BIT,
                                                   I2S_SLOT_MODE_MONO),
    .gpio_cfg = {
        .mclk = BSP_I2S_MCLK,
        .bclk = BSP_I2S_SCLK,
        .ws   = BSP_I2S_LCLK,
        .dout = BSP_I2S_DOUT,
        .din  = BSP_I2S_DSIN,
        .invert_flags = { .mclk_inv = false, .bclk_inv = false, .ws_inv = false },
    },
};

esp_err_t audio_preinit(void)
{
    /* bsp_audio_init has an early-return guard: if i2s_tx_chan and i2s_rx_chan
     * are already set it returns ESP_OK immediately.  Calling audio_preinit()
     * BEFORE bsp_display_start*() means we claim I2S at 16 kHz first; the
     * display's internal bsp_audio_init(NULL) then hits the guard and cannot
     * override the clock with its 22050 Hz default. */
    esp_err_t ret = bsp_audio_init(&s_i2s_cfg);
    if (ret != ESP_OK) {
        ESP_LOGE(TAG, "audio_preinit bsp_audio_init failed: %s", esp_err_to_name(ret));
    } else {
        ESP_LOGI(TAG, "I2S pre-claimed at %d Hz (before display init)", AUDIO_SAMPLE_RATE);
    }
    return ret;
}

esp_err_t audio_init(void)
{
    /* bsp_audio_init is a no-op here — audio_preinit() already ran.
     * Call it defensively in case preinit was skipped, but expect early-return. */
    esp_err_t ret = bsp_audio_init(&s_i2s_cfg);
    if (ret != ESP_OK) {
        ESP_LOGE(TAG, "bsp_audio_init failed: %s", esp_err_to_name(ret));
        return ret;
    }

    /* Microphone — ES7210 ADC */
    s_mic = bsp_audio_codec_microphone_init();
    if (!s_mic) {
        ESP_LOGE(TAG, "bsp_audio_codec_microphone_init failed");
        return ESP_FAIL;
    }

    esp_codec_dev_sample_info_t mic_info = {
        .bits_per_sample = AUDIO_BITS,
        .channel         = AUDIO_CHANNELS,
        .sample_rate     = AUDIO_SAMPLE_RATE,
    };
    ret = esp_codec_dev_open(s_mic, &mic_info);
    if (ret != ESP_OK) {
        ESP_LOGE(TAG, "esp_codec_dev_open(mic) failed: %s", esp_err_to_name(ret));
        return ret;
    }
    esp_codec_dev_set_in_gain(s_mic, 37.5f);   /* typical BOX-3 mic gain */

    /* Speaker — ES8311 DAC */
    s_spk = bsp_audio_codec_speaker_init();
    if (!s_spk) {
        ESP_LOGE(TAG, "bsp_audio_codec_speaker_init failed");
        return ESP_FAIL;
    }

    esp_codec_dev_sample_info_t spk_info = {
        .bits_per_sample = AUDIO_BITS,
        .channel         = AUDIO_CHANNELS,
        .sample_rate     = AUDIO_SAMPLE_RATE,
    };
    ret = esp_codec_dev_open(s_spk, &spk_info);
    if (ret != ESP_OK) {
        ESP_LOGE(TAG, "esp_codec_dev_open(spk) failed: %s", esp_err_to_name(ret));
        return ret;
    }
    /* Volume: NVS-persisted user percent (spoken "set volume X%" command),
     * mapped onto the clean codec range — see audio_set_volume(). */
    s_ready = true;
    {
        int _boot_pct = audio_get_saved_volume();
        s_vol_target_pct = _boot_pct;
        s_vol_actual     = (_boot_pct * AUDIO_CODEC_VOL_MAX) / 100;
        esp_codec_dev_set_out_vol(s_spk, s_vol_actual);   /* pre-playback: no ramp needed */
    }

    s_ready = true;
    ESP_LOGI(TAG, "Audio ready: mic + speaker at %d Hz %d-bit mono",
             AUDIO_SAMPLE_RATE, AUDIO_BITS);
    return ESP_OK;
}

size_t audio_capture_frame(uint8_t *buf, size_t nbytes)
{
    if (!s_ready || !buf || nbytes == 0) return 0;
    esp_err_t ret = esp_codec_dev_read(s_mic, buf, (int)nbytes);
    if (ret != ESP_OK) {
        ESP_LOGW(TAG, "esp_codec_dev_read failed: %s", esp_err_to_name(ret));
        return 0;
    }
    return nbytes;
}

esp_err_t audio_play(const uint8_t *buf, size_t len)
{
    if (!s_ready || !buf || len == 0) return ESP_OK;
    esp_err_t ret = esp_codec_dev_write(s_spk, (void *)buf, (int)len);
    if (ret != ESP_OK) {
        ESP_LOGW(TAG, "esp_codec_dev_write failed: %s", esp_err_to_name(ret));
    }
    return ret;
}

/* ── Speaker volume (spoken "set volume X%" command) ─────────────────────── */

#include "nvs_flash.h"
#include "nvs.h"

#define AUDIO_DEFAULT_VOL 92

int audio_get_saved_volume(void)
{
    nvs_handle_t h;
    int32_t vol = AUDIO_DEFAULT_VOL;
    if (nvs_open("audio", NVS_READONLY, &h) == ESP_OK) {
        nvs_get_i32(h, "out_vol", &vol);
        nvs_close(h);
    }
    if (vol < 0)   vol = 0;
    if (vol > 100) vol = 100;
    return (int)vol;
}

/* Zipper-free volume: a single large ES8311 gain step pops audibly right as
 * the confirmation reply starts (owner-isolated 2026-07-07: volume-change
 * turns click, plain turns clean — on a clean power supply).  audio_set_volume
 * only stores the target; audio_volume_tick() (called from the tts_task loop,
 * ~every 128 ms) walks the codec toward it in ≤4-unit steps and persists to
 * NVS once, after the ramp settles (flash commits stall the cache — keep them
 * away from the moment playback starts).
 * State + AUDIO_CODEC_VOL_MAX are declared near the top (audio_init uses them). */
esp_err_t audio_set_volume(int pct)
{
    if (pct < 0)   pct = 0;
    if (pct > 100) pct = 100;
    s_vol_target_pct = pct;
    s_vol_dirty      = true;
    ESP_LOGI(TAG, "Speaker volume target %d%% (ramped by audio_volume_tick)", pct);
    return ESP_OK;
}

void audio_volume_tick(void)
{
    if (s_vol_target_pct < 0 || !s_spk) return;
    int target = (s_vol_target_pct * AUDIO_CODEC_VOL_MAX) / 100;
    int actual = s_vol_actual;
    if (actual < 0) actual = target;          /* first call: jump silently */
    if (actual != target) {
        int step = (target > actual) ? 4 : -4;
        actual += step;
        if ((step > 0 && actual > target) || (step < 0 && actual < target)) {
            actual = target;
        }
        s_vol_actual = actual;
        esp_codec_dev_set_out_vol(s_spk, actual);
        return;                               /* persist only once settled */
    }
    if (s_vol_dirty) {
        s_vol_dirty = false;
        nvs_handle_t h;
        if (nvs_open("audio", NVS_READWRITE, &h) == ESP_OK) {
            nvs_set_i32(h, "out_vol", (int32_t)s_vol_target_pct);
            nvs_commit(h);
            nvs_close(h);
        }
        ESP_LOGI(TAG, "Speaker volume %d%% persisted", (int)s_vol_target_pct);
    }
}
