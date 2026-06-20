#pragma once
/* Audio capture (ES7210 mic) and playback (ES8311 speaker) for BOX-3. */

#include <stddef.h>
#include <stdint.h>
#include "esp_err.h"

/* PCM config used for both capture and playback. */
#define AUDIO_SAMPLE_RATE    16000
#define AUDIO_BITS           16
#define AUDIO_CHANNELS       1

/* Size of one capture frame fed to the wake-word AFE pipeline (10 ms @ 16 kHz). */
#define AUDIO_FRAME_BYTES    320   /* 160 samples × 2 bytes */

/* Maximum PCM buffered for one push-to-talk utterance (5 s). */
#define AUDIO_UTTERANCE_MAX  (AUDIO_SAMPLE_RATE * AUDIO_BITS / 8 * 5)

/**
 * @brief Initialise mic (ES7210) and speaker (ES8311) codecs.
 *
 * Must be called once after bsp_display_start_with_config() has run.
 * Configures I2S at AUDIO_SAMPLE_RATE / AUDIO_BITS / AUDIO_CHANNELS.
 *
 * @return ESP_OK or propagated codec error.
 */
esp_err_t audio_init(void);

/**
 * @brief Read one capture frame from the microphone into *buf*.
 *
 * Blocking call; returns AUDIO_FRAME_BYTES on success or 0 on codec error.
 *
 * @param buf   Output buffer; must be at least AUDIO_FRAME_BYTES bytes.
 * @return Number of bytes written into buf.
 */
size_t audio_capture_frame(uint8_t *buf);

/**
 * @brief Play raw S16LE PCM from *buf* through the speaker.
 *
 * @param buf  PCM data.
 * @param len  Number of bytes to play.
 * @return ESP_OK or propagated codec error.
 */
esp_err_t audio_play(const uint8_t *buf, size_t len);
