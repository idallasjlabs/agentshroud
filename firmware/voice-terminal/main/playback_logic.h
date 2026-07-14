// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
// AgentShroud™ USPTO Serial No. 99728633 · Patent Pending No. 64/018,744
//
// Pure decision helpers for the TTS playback END-gate and utterance delivery
// resume math.  Extracted verbatim from app_main.c so the same arithmetic can
// be exercised by host-native unit tests (test/test_wakeword_state) WITHOUT
// pulling in FreeRTOS, LVGL, the audio codec, or the WebSocket stack.
//
// These functions are `static inline` and side-effect-free: app_main.c calls
// them at the exact points the inline expressions used to live, so on-device
// behavior is byte-for-byte identical — only the expression's *home* moved.
//
// SAFE-EXTRACTION NOTE (SCRUM-59): the END-gate condition and the delivery
// resume offset were previously inline expressions inside tts_task() and
// _deliver_utterance().  They were not host-testable because those functions
// depend on hardware/RTOS singletons.  Lifting the pure arithmetic here is the
// minimal change that makes the logic testable; no thresholds or ordering
// changed.

#pragma once

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

/* ── END-gate caps (mirror the comments in tts_task) ──────────────────────────
 * The playback gate opens when ANY of these is true:
 *   - the server's END frame landed (reply_complete): the whole reply is
 *     buffered strictly after the last PCM byte — the primary, correct trigger;
 *   - the banked byte cap is hit (1 MB TTS buffer overflow guard); or
 *   - the fill-age cap is hit (synthesis-wedge guard: END never arrived).
 */
#define PLAYBACK_GATE_BYTE_CAP    (768u * 1024u)  /* 768 KB banked  (~24 s)      */
#define PLAYBACK_GATE_AGE_CAP_MS  20000u          /* 20 s fill age               */

/* Rewind applied to the resume offset so a mid-flight loss at the drop point is
 * re-sent rather than skipped.  Matches _deliver_utterance()'s 8 KB rewind. */
#define DELIVERY_RESUME_REWIND    8192u

/**
 * @brief END-gate open decision.
 *
 * Pure form of the condition in tts_task():
 *     s_reply_complete
 *     || avail >= (768 * 1024)
 *     || (now - gate_start) * portTICK_PERIOD_MS > 20000
 *
 * @param reply_complete  server END frame has landed (whole reply buffered).
 * @param avail_bytes     bytes currently banked in the TTS stream buffer.
 * @param gate_age_ms     ms elapsed since the first byte of this reply arrived.
 * @return true when playback should start (gate opens).
 */
static inline bool
playback_gate_should_open(bool reply_complete, size_t avail_bytes,
                          uint32_t gate_age_ms)
{
    return reply_complete
        || avail_bytes >= PLAYBACK_GATE_BYTE_CAP
        || gate_age_ms > PLAYBACK_GATE_AGE_CAP_MS;
}

/**
 * @brief Delivery resume offset with rewind clamp.
 *
 * Pure form of _deliver_utterance()'s:
 *     size_t start_off = (sent_ok > 8192) ? sent_ok - 8192 : 0;
 *
 * Attempt 1 (sent_ok == 0) yields 0 → plain LISTEN.  Once more than one rewind
 * window has been confirmed, resume 8 KB behind the high-water mark so the
 * bytes that may have been lost in flight are re-sent, never skipped.
 *
 * @param sent_ok  high-water mark of bytes confirmed sent across attempts.
 * @return byte offset to resume the LISTEN upload from (clamped at 0).
 */
static inline size_t
delivery_resume_offset(size_t sent_ok)
{
    return (sent_ok > DELIVERY_RESUME_REWIND)
             ? sent_ok - DELIVERY_RESUME_REWIND
             : 0;
}

/**
 * @brief Update the sent-so-far high-water mark after a chunk lands.
 *
 * Pure form of _deliver_utterance()'s:
 *     if (off > sent_ok) sent_ok = off;
 *
 * Monotonic: a later attempt that resumed from a rewound offset must not lower
 * the mark below what an earlier attempt already confirmed.
 *
 * @param sent_ok  current high-water mark.
 * @param off      byte offset reached by the current chunk.
 * @return the new high-water mark (max of the two).
 */
static inline size_t
delivery_track_sent_ok(size_t sent_ok, size_t off)
{
    return (off > sent_ok) ? off : sent_ok;
}
