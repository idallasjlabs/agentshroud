#pragma once
/* Wake-word and push-to-talk trigger for the BOX-3 voice terminal.
 *
 * Two trigger modes run concurrently:
 *   PTT  — BOX-3 boot/home button: hold = start, release = END
 *   WW   — esp-sr WakeNet (stock keyword) detected via the AFE pipeline
 *
 * The caller feeds mic frames one at a time via wakeword_push_frame().
 * wakeword_triggered() returns true when a trigger fires; wakeword_clear()
 * resets it.  This is intentionally simple/polling — the audio task drives
 * the loop at AUDIO_FRAME_BYTES / (16000 * 2) ≈ 10 ms intervals.
 */

#include <stdbool.h>
#include <stdint.h>
#include <stddef.h>
#include "esp_err.h"

/**
 * @brief Initialise the AFE pipeline and button trigger.
 *
 * @param model_partition  SPIFFS label of the partition holding the WakeNet
 *                         model data (e.g. "model").  NULL disables WakeNet;
 *                         only PTT will work.
 * @return ESP_OK on success.
 */
esp_err_t wakeword_init(const char *model_partition);

/**
 * @brief Feed one capture frame to the AFE + WakeNet pipeline.
 *
 * @param pcm  Raw S16LE 16 kHz mono frame (AUDIO_FRAME_BYTES bytes).
 * @param len  Frame length in bytes.
 */
void wakeword_push_frame(const uint8_t *pcm, size_t len);

/**
 * @brief Returns true if a trigger (PTT press or WakeNet detection) fired.
 *        The caller should drain the ring buffer and start streaming.
 */
bool wakeword_triggered(void);

/**
 * @brief Returns true if the trigger has ended (PTT button released or VAD timeout).
 *        The caller should send "END" to the Voice Gateway.
 */
bool wakeword_ended(void);

/** @brief Reset trigger state (call after processing each utterance). */
void wakeword_clear(void);

/**
 * @brief Free all AFE/WakeNet resources (called at shutdown).
 */
void wakeword_deinit(void);
