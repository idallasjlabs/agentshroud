#pragma once
/* Audio capture (ES7210 mic) and playback (ES8311 speaker) for BOX-3. */

#include <stddef.h>
#include <stdint.h>
#include "esp_err.h"

/* PCM config used for both capture and playback.
 * 16 kHz is required by the esp-sr WakeNet AFE pipeline.
 * faster-whisper also works natively at 16 kHz (no resampling needed). */
#define AUDIO_SAMPLE_RATE    16000
#define AUDIO_BITS           16
#define AUDIO_CHANNELS       1

/* AFE feed chunk size is determined at runtime via afe->get_feed_chunksize().
 * Typically 256 samples (512 bytes) for WN9 at 16 kHz mono.
 * AUDIO_FRAME_BYTES_MAX is the worst-case buffer size for a single feed call. */
#define AUDIO_FRAME_BYTES_MAX  1024   /* 512 samples × 2 bytes — safe upper bound */

/* Maximum PCM buffered for one push-to-talk utterance (5 s). */
#define AUDIO_UTTERANCE_MAX  (AUDIO_SAMPLE_RATE * AUDIO_BITS / 8 * 5)

/**
 * @brief Pre-initialize I2S at AUDIO_SAMPLE_RATE BEFORE bsp_display_start*().
 *
 * bsp_display_new() internally calls bsp_audio_init(NULL) which locks I2S to
 * 22050 Hz (BSP default).  bsp_audio_init has an early-return guard that
 * ignores any subsequent call if I2S is already initialized, so audio_init()
 * cannot override the 22050 Hz clock.
 *
 * Call audio_preinit() first to claim I2S at 16000 Hz; the display's
 * bsp_audio_init(NULL) will then hit the early-return guard and leave
 * the clock unchanged.
 *
 * @return ESP_OK or propagated I2S error.
 */
esp_err_t audio_preinit(void);

/**
 * @brief Initialise mic (ES7210) and speaker (ES8311) codecs.
 *
 * Must be called once after bsp_display_start_with_config() has run
 * AND after audio_preinit() has been called.
 * Configures codecs at AUDIO_SAMPLE_RATE / AUDIO_BITS / AUDIO_CHANNELS.
 *
 * @return ESP_OK or propagated codec error.
 */
esp_err_t audio_init(void);

/**
 * @brief Read exactly *nbytes* from the microphone into *buf*.
 *
 * Blocking call; returns nbytes on success or 0 on codec error.
 * The caller supplies nbytes — typically afe->get_feed_chunksize() * 2 (bytes).
 *
 * @param buf    Output buffer; must be at least nbytes bytes.
 * @param nbytes Bytes to capture; must be a multiple of 2 (16-bit samples).
 * @return Number of bytes written into buf, or 0 on error.
 */
size_t audio_capture_frame(uint8_t *buf, size_t nbytes);

/**
 * @brief Play raw S16LE PCM from *buf* through the speaker.
 *
 * @param buf  PCM data.
 * @param len  Number of bytes to play.
 * @return ESP_OK or propagated codec error.
 */
esp_err_t audio_play(const uint8_t *buf, size_t len);

/**
 * @brief Set speaker volume 0-100%% and persist it to NVS ("audio"/"out_vol").
 *
 * Driven by the spoken "set volume X%%" command (server sends a
 * {"cmd":"set_volume","value":N} control frame).  Clamped to [0,100].
 */
esp_err_t audio_set_volume(int pct);

/**
 * @brief Volume loaded from NVS, or the built-in default on first boot.
 */
int audio_get_saved_volume(void);

/**
 * @brief Step the codec volume toward the spoken target (zipper-free ramp)
 *        and persist to NVS once settled.  Call periodically (~100-150 ms)
 *        from the playback task.
 */
void audio_volume_tick(void);
