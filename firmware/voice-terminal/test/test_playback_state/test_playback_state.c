// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
// AgentShroud™ USPTO Serial No. 99728633 · Patent Pending No. 64/018,744
//
// Host-native unit tests for the TTS playback END-gate and utterance-delivery
// resume math shipped in the 'playdrive-0707m' build (SCRUM-59).
//
// Compiled with stub headers (no ESP-IDF, no FreeRTOS, no LVGL, no hardware):
//   cc -std=c11 -DHAVE_ESP_SR=0 -I stubs -I ../../main wakeword.c test_playback_state.c
//
// Two logic families are covered:
//
//   1. Pure decision helpers extracted from app_main.c into playback_logic.h
//      (same arithmetic, new home — see the SAFE-EXTRACTION NOTE in that file):
//        - playback_gate_should_open(): reply-complete / 768 KB cap / 20 s age
//        - delivery_resume_offset():    8 KB rewind clamp
//        - delivery_track_sent_ok():    monotonic high-water mark
//
//   2. The playback-driven state machine.  tts_task() (app_main.c) drives the
//      speaking state from PLAYBACK, not server frames:
//        gate-open  → wakeword_set_tts_playing(true)  + face SPEAKING
//        drain      → wakeword_set_tts_playing(false) + face IDLE (if not
//                     re-triggered) + wakeword_tts_stop_clear()
//      We reproduce that exact call sequence here using the REAL wakeword.c
//      flag functions (compiled in) plus a captured face-state stub, mirroring
//      how test_ptt_state.c isolates the wakeword flags.

#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>

/* Tick counter required by the FreeRTOS stub that wakeword.c pulls in. */
volatile uint32_t g_test_tick_ms = 0;

#include "wakeword.h"          /* real flag API from wakeword.c            */
#include "playback_logic.h"    /* pure END-gate + resume helpers under test */

/* vt_agent_count() is declared extern in wakeword.c; provide a stub. */
int vt_agent_count(void) { return 0; }

/* wakeword.c mirrors diagnostics via vt_remote_log() (remote_log.h).  On the
 * host it has no WebSocket to write to — swallow the call. */
#include <stdarg.h>
void vt_remote_log(const char *fmt, ...) { (void)fmt; }

/* ── Face-state capture stub ──────────────────────────────────────────────────
 * app_main.c calls ui_face_set_state() at the gate-open and drain boundaries.
 * The real implementation drives LVGL; here we only record the last state so
 * the transition sequence can be asserted.  We mirror the ws_vg_state_t values
 * used by the playback path (IDLE and SPEAKING) without pulling ws_client.h. */
typedef enum {
    FACE_IDLE = 0,
    FACE_LISTENING,
    FACE_THINKING,
    FACE_SPEAKING,
} face_state_t;

static face_state_t s_face = FACE_IDLE;
static void face_set_state(face_state_t st) { s_face = st; }

/* ── Playback state-machine step ──────────────────────────────────────────────
 * A faithful, side-effect-equivalent reproduction of the gate-open and drain
 * branches of tts_task() (app_main.c), calling the SAME functions in the SAME
 * order.  It does not touch audio_play()/the stream buffer — those are the I/O
 * the host build deliberately omits — but the STATE it mutates (tts_playing,
 * face, stop-clear) is exactly what the on-device task mutates.
 *
 * @param gate_open      [in/out] current gate state (persists across steps).
 * @param reply_complete server END landed.
 * @param avail_bytes    bytes banked in the TTS buffer.
 * @param gate_age_ms    ms since first byte of this reply.
 * @param drained        true when the buffer has emptied (xStreamBufferReceive
 *                       returned 0) — the drain trigger.
 */
static void playback_step(bool *gate_open, bool reply_complete,
                          size_t avail_bytes, uint32_t gate_age_ms,
                          bool drained)
{
    if (!*gate_open && avail_bytes > 0) {
        if (playback_gate_should_open(reply_complete, avail_bytes, gate_age_ms)) {
            *gate_open = true;
            /* app_main.c tts_task: playback drives the speaking state. */
            wakeword_set_tts_playing(true);
            face_set_state(FACE_SPEAKING);
        }
    }

    if (*gate_open && drained) {
        /* app_main.c tts_task: reply drained — re-gate for the next. */
        *gate_open = false;
        wakeword_set_tts_playing(false);
        wakeword_tts_stop_clear();
        if (!wakeword_triggered()) {
            face_set_state(FACE_IDLE);
        }
    }
}

/* Reset all wakeword state to IDLE.  wakeword_clear() intentionally does NOT
 * touch s_tts_playing (only wakeword_set_tts_playing(false) does), so a full
 * reset between tests must clear tts_playing explicitly — mirroring how the
 * device leaves that flag owned solely by the playback path. */
static void reset_all(void)
{
    wakeword_set_tts_playing(false);   /* clears tts_playing + stale trigger  */
    wakeword_tts_stop_clear();
    wakeword_clear();
    g_test_tick_ms = 0;
    s_face = FACE_IDLE;
}

/* ── Minimal test framework (matches test_ptt_state.c) ────────────────────── */

static int s_pass = 0;
static int s_fail = 0;

#define ASSERT(cond, msg)                                           \
    do {                                                            \
        if (cond) {                                                 \
            printf("  PASS  %s\n", msg);                           \
            s_pass++;                                               \
        } else {                                                    \
            printf("  FAIL  %s  (line %d)\n", msg, __LINE__);      \
            s_fail++;                                               \
        }                                                           \
    } while (0)

/* ── END-gate open-condition tests ────────────────────────────────────────── */

static void test_gate_stays_closed_before_any_cap(void)
{
    puts("test_gate_stays_closed_before_any_cap");
    /* Not complete, under the byte cap, under the age cap → gate stays shut. */
    ASSERT(!playback_gate_should_open(false, 4096, 0),
           "Small partial reply, no END, young gate → gate must stay closed");
    ASSERT(!playback_gate_should_open(false, PLAYBACK_GATE_BYTE_CAP - 1,
                                      PLAYBACK_GATE_AGE_CAP_MS),
           "Just under BOTH caps (byte cap-1, age == cap not >) → still closed");
}

static void test_gate_opens_on_reply_complete(void)
{
    puts("test_gate_opens_on_reply_complete");
    /* The primary, correct trigger: server END frame landed. */
    ASSERT(playback_gate_should_open(true, 1, 0),
           "reply_complete=true opens the gate even with 1 byte banked");
    ASSERT(playback_gate_should_open(true, 0, 0),
           "reply_complete=true dominates regardless of avail/age");
}

static void test_gate_opens_on_768kb_cap(void)
{
    puts("test_gate_opens_on_768kb_cap");
    ASSERT(PLAYBACK_GATE_BYTE_CAP == 768u * 1024u,
           "Byte cap constant must be exactly 768 KB (1 MB buffer overflow guard)");
    ASSERT(!playback_gate_should_open(false, PLAYBACK_GATE_BYTE_CAP - 1, 0),
           "One byte below the 768 KB cap → gate closed");
    ASSERT(playback_gate_should_open(false, PLAYBACK_GATE_BYTE_CAP, 0),
           "Exactly 768 KB banked → gate opens (>= cap)");
    ASSERT(playback_gate_should_open(false, PLAYBACK_GATE_BYTE_CAP + 4096, 0),
           "Above the 768 KB cap → gate opens");
}

static void test_gate_opens_on_20s_age(void)
{
    puts("test_gate_opens_on_20s_age");
    ASSERT(PLAYBACK_GATE_AGE_CAP_MS == 20000u,
           "Age cap constant must be exactly 20 s (synthesis-wedge guard)");
    ASSERT(!playback_gate_should_open(false, 4096, PLAYBACK_GATE_AGE_CAP_MS),
           "Exactly 20000 ms → gate closed (condition is strictly > 20000)");
    ASSERT(playback_gate_should_open(false, 4096, PLAYBACK_GATE_AGE_CAP_MS + 1),
           "20001 ms fill age → gate opens (synthesis wedged, no END)");
}

/* ── Delivery resume offset math tests ────────────────────────────────────── */

static void test_resume_offset_first_attempt_is_zero(void)
{
    puts("test_resume_offset_first_attempt_is_zero");
    ASSERT(delivery_resume_offset(0) == 0,
           "Attempt 1 (sent_ok == 0) → offset 0 → plain LISTEN");
    ASSERT(delivery_resume_offset(DELIVERY_RESUME_REWIND) == 0,
           "sent_ok == 8192 (== rewind, not >) → offset clamped to 0");
    ASSERT(delivery_resume_offset(1) == 0,
           "Tiny progress below the rewind window → offset clamped to 0");
}

static void test_resume_offset_rewinds_8kb(void)
{
    puts("test_resume_offset_rewinds_8kb");
    ASSERT(delivery_resume_offset(DELIVERY_RESUME_REWIND + 1) == 1,
           "One byte past the rewind window → resume from 1 (8 KB rewound)");
    ASSERT(delivery_resume_offset(151 * 1024) == 151 * 1024 - DELIVERY_RESUME_REWIND,
           "151 KB confirmed → resume 8 KB behind the high-water mark");
    ASSERT(DELIVERY_RESUME_REWIND == 8192u,
           "Rewind window must be exactly 8 KB (matches in-flight loss guard)");
}

static void test_track_sent_ok_is_monotonic(void)
{
    puts("test_track_sent_ok_is_monotonic");
    ASSERT(delivery_track_sent_ok(0, 4096) == 4096,
           "First chunk advances the high-water mark from 0 to 4096");
    ASSERT(delivery_track_sent_ok(151 * 1024, 160 * 1024) == 160 * 1024,
           "A larger offset raises the mark");
    /* A resumed attempt re-sends rewound bytes; off can be BELOW sent_ok and
     * must NOT lower the mark (else the next resume would rewind too far). */
    ASSERT(delivery_track_sent_ok(151 * 1024, 145 * 1024) == 151 * 1024,
           "Resumed (rewound) chunk below the mark must NOT lower it");
    ASSERT(delivery_track_sent_ok(4096, 4096) == 4096,
           "Equal offset leaves the mark unchanged");
}

/* ── Playback-driven state-machine transition tests ───────────────────────── */

static void test_gate_open_sets_speaking_and_tts_playing(void)
{
    puts("test_gate_open_sets_speaking_and_tts_playing");
    reset_all();
    bool gate_open = false;

    /* Reply fully buffered (END landed) with audio banked → gate opens. */
    playback_step(&gate_open, /*reply_complete=*/true, /*avail=*/8192,
                  /*age_ms=*/0, /*drained=*/false);

    ASSERT(gate_open, "gate must be open after reply_complete with audio banked");
    ASSERT(wakeword_tts_playing(),
           "gate-open must set tts_playing (playback drives the state, not server)");
    ASSERT(s_face == FACE_SPEAKING,
           "gate-open must drive the face to SPEAKING");
}

static void test_gate_stays_closed_leaves_state_idle(void)
{
    puts("test_gate_stays_closed_leaves_state_idle");
    reset_all();
    bool gate_open = false;

    /* Partial reply, no END, young gate → gate must NOT open, no SPEAKING. */
    playback_step(&gate_open, /*reply_complete=*/false, /*avail=*/4096,
                  /*age_ms=*/100, /*drained=*/false);

    ASSERT(!gate_open, "gate must stay closed on a partial, incomplete reply");
    ASSERT(!wakeword_tts_playing(),
           "no gate-open → tts_playing stays false");
    ASSERT(s_face == FACE_IDLE, "face stays IDLE while the gate is closed");
}

static void test_drain_clears_playing_and_returns_idle(void)
{
    puts("test_drain_clears_playing_and_returns_idle");
    reset_all();
    bool gate_open = false;

    /* Open the gate first. */
    playback_step(&gate_open, /*reply_complete=*/true, /*avail=*/8192,
                  /*age_ms=*/0, /*drained=*/false);
    ASSERT(gate_open && wakeword_tts_playing() && s_face == FACE_SPEAKING,
           "Pre-condition: gate open, tts_playing, face SPEAKING");

    /* Buffer drains (xStreamBufferReceive returns 0). */
    playback_step(&gate_open, /*reply_complete=*/false, /*avail=*/0,
                  /*age_ms=*/0, /*drained=*/true);

    ASSERT(!gate_open, "drain must re-gate for the next reply (gate closed)");
    ASSERT(!wakeword_tts_playing(),
           "drain must clear tts_playing when the buffer empties");
    ASSERT(!wakeword_tts_stop_requested(),
           "drain must clear any pending TTS stop request");
    ASSERT(s_face == FACE_IDLE,
           "drain with no active trigger must return the face to IDLE");
}

static void test_drain_keeps_face_off_idle_when_retriggered(void)
{
    puts("test_drain_keeps_face_off_idle_when_retriggered");
    reset_all();
    bool gate_open = false;

    /* User is holding PTT (a fresh utterance) BEFORE the previous reply's
     * playback drains — s_ptt_held + s_triggered latch while tts_playing is
     * still false (the guard in _ptt_start rejects presses during TTS). */
    wakeword_ptt_press();
    ASSERT(wakeword_triggered(), "Pre-condition: held PTT set triggered");

    /* The tail of the previous reply opens the gate and plays out. */
    playback_step(&gate_open, /*reply_complete=*/true, /*avail=*/8192,
                  /*age_ms=*/0, /*drained=*/false);
    ASSERT(s_face == FACE_SPEAKING, "Pre-condition: face SPEAKING");

    /* Now the buffer drains.  wakeword_set_tts_playing(false) preserves the
     * trigger because s_ptt_held is set, so the drain branch's
     * `if (!wakeword_triggered())` guard must SKIP forcing the face to IDLE —
     * otherwise the new utterance's LISTENING face would be stomped. */
    playback_step(&gate_open, /*reply_complete=*/false, /*avail=*/0,
                  /*age_ms=*/0, /*drained=*/true);

    ASSERT(!wakeword_tts_playing(), "drain still clears tts_playing");
    ASSERT(wakeword_triggered(),
           "held-PTT trigger survives set_tts_playing(false) (s_ptt_held set)");
    ASSERT(s_face == FACE_SPEAKING,
           "drain must NOT force IDLE while a new utterance is triggered");
}

/* ── Main ─────────────────────────────────────────────────────────────────── */

int main(void)
{
    puts("=== TTS playback END-gate + state-machine tests ===");
    test_gate_stays_closed_before_any_cap();
    test_gate_opens_on_reply_complete();
    test_gate_opens_on_768kb_cap();
    test_gate_opens_on_20s_age();
    test_resume_offset_first_attempt_is_zero();
    test_resume_offset_rewinds_8kb();
    test_track_sent_ok_is_monotonic();
    test_gate_open_sets_speaking_and_tts_playing();
    test_gate_stays_closed_leaves_state_idle();
    test_drain_clears_playing_and_returns_idle();
    test_drain_keeps_face_off_idle_when_retriggered();

    printf("\n=== Results: %d passed, %d failed ===\n", s_pass, s_fail);
    return s_fail > 0 ? 1 : 0;
}
