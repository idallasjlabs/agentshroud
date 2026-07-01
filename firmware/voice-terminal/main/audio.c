#include "audio.h"
#include <string.h>
#include "bsp/esp-bsp.h"
#include "esp_codec_dev.h"
#include "esp_log.h"

static const char *TAG = "audio";

static esp_codec_dev_handle_t s_mic    = NULL;
static esp_codec_dev_handle_t s_spk    = NULL;
static bool                   s_ready  = false;

esp_err_t audio_init(void)
{
    /* Init I2S at the project's native sample rate instead of the BSP default.
     * Passing NULL uses BSP_I2S_DUPLEX_MONO_CFG(22050) which then mismatches
     * the 16000 Hz passed to esp_codec_dev_open below, causing
     * esp_codec_dev_read to fail and audio_capture_frame to return 0. */
    i2s_std_config_t i2s_cfg = {
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
    esp_err_t ret = bsp_audio_init(&i2s_cfg);
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
    esp_codec_dev_set_out_vol(s_spk, 75);   /* 75 % volume */

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
