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
 * @brief Initialise mic (ES7210) and speaker (ES8311) codecs.
 *
 * Must be called once after bsp_display_start_with_config() has run.
 * Configures I2S at AUDIO_SAMPLE_RATE / AUDIO_BITS / AUDIO_CHANNELS.
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
