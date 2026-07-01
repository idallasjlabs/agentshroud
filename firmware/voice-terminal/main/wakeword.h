#pragma once
/* Wake-word and push-to-talk trigger for the BOX-3 voice terminal.
 *
 * Two trigger modes run concurrently:
 *   PTT  — tap-and-hold the touchscreen (BSP_BUTTON_MAIN)
 *   WW   — say "Hi, ESP" (esp-sr WakeNet WN9, stock keyword — no training required)
 *
 * The caller feeds mic frames one at a time via wakeword_push_frame().
 * Frame size MUST equal wakeword_feed_bytes() (the AFE's required chunk size).
 * wakeword_triggered() returns true when a trigger fires; wakeword_clear()
 * resets it.  This is intentionally simple/polling — the audio task drives
 * the loop at wakeword_feed_bytes() / (AUDIO_SAMPLE_RATE * 2) intervals.
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
 * @brief Returns the required number of bytes per audio frame for wakeword_push_frame().
 *
 * This is the AFE's feed chunk size in bytes (samples × 2).  After wakeword_init()
 * returns, call this once and allocate your frame buffer accordingly.
 * If esp-sr is not compiled in, returns a safe default (512 bytes).
 */
int wakeword_feed_bytes(void);

/**
 * @brief Feed one capture frame to the AFE + WakeNet pipeline.
 *
 * @param pcm  Raw S16LE 16 kHz mono frame; length must equal wakeword_feed_bytes().
 * @param len  Frame length in bytes.
 */
void wakeword_push_frame(const uint8_t *pcm, size_t len);

/**
 * @brief Advance internal timers (VAD timeout, PTT release) without audio data.
 *
 * Call from the voice_task loop when audio_capture_frame() returns 0 bytes so
 * that a triggered-but-stuck streaming state can still time out and send END.
 * wakeword_push_frame() calls this automatically when len > 0.
 */
void wakeword_tick(void);

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
 * @brief Programmatically start a PTT utterance (e.g. from an LVGL touch handler).
 *        Equivalent to pressing the physical button.  No-op if already triggered or
 *        if TTS is currently playing (prevents triggering on speaker echo).
 */
void wakeword_ptt_press(void);

/**
 * @brief Programmatically end a PTT utterance (e.g. on touch release / PRESS_LOST).
 *        Equivalent to releasing the physical button.  No-op if not holding PTT.
 */
void wakeword_ptt_release(void);

/**
 * @brief Signal that TTS playback is starting or ending.
 *
 * While TTS is playing (playing=true) both PTT and WakeNet are suppressed so
 * the speaker output cannot accidentally trigger a new utterance.  The Voice
 * Gateway state machine clears this flag when it transitions to IDLE (i.e.
 * after the server's "END" frame is received), re-enabling triggers.
 *
 * @param playing  true when the gateway enters SPEAKING state;
 *                 false when the gateway returns to IDLE.
 */
void wakeword_set_tts_playing(bool playing);

/**
 * @brief Free all AFE/WakeNet resources (called at shutdown).
 */
void wakeword_deinit(void);

/**
 * @brief Advance to the next agent in the compiled-in agent list.
 *
 * Called from the agent-select button (BSP_BUTTON_MUTE or BSP_BUTTON_CONFIG).
 * The agent list and display names are defined in app_main.c.
 * Thread-safe (increments an atomic index).
 */
void wakeword_next_agent(void);

/**
 * @brief Returns true if a pending agent switch has been requested
 *        (wakeword_next_agent() was called since the last wakeword_agent_ack()).
 */
bool wakeword_agent_switch_pending(void);

/**
 * @brief Acknowledge an agent switch (clear the pending flag).
 *        Call after the voice task has processed the switch and reconnected.
 */
void wakeword_agent_switch_ack(void);

/**
 * @brief Returns the current agent index (0-based, into the app_main agent table).
 */
int wakeword_agent_index(void);

/**
 * @brief Request an immediate stop of TTS playback.
 *
 * Called when the user taps the screen or presses the physical button while
 * TTS is playing.  Sets an internal flag that causes the PCM callback in
 * app_main.c to discard incoming audio chunks until the server sends "END".
 * No-op if TTS is not currently playing.
 */
void wakeword_tts_stop_request(void);

/**
 * @brief Returns true if a TTS stop has been requested by the user.
 *        Checked in the PCM callback to drop incoming audio chunks.
 */
bool wakeword_tts_stop_requested(void);

/**
 * @brief Clear the TTS stop request flag.
 *        Called in _on_vg_state when IDLE is received after a SPEAKING state.
 */
void wakeword_tts_stop_clear(void);
