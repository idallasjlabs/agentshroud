// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
// AgentShroud™ USPTO Serial No. 99728633 · Patent Pending No. 64/018,744
//
// Host-native unit tests for the wakeword PTT state machine.
//
// Compiled with stub headers (no ESP-IDF, no FreeRTOS, no hardware):
//   cc -std=c11 -DHAVE_ESP_SR=0 -I stubs -I ../../main wakeword_src.c test_ptt_state.c
//
// The four assertions below are the exact regression guard for the
// "stuck in listening" bug introduced by the LVGL-9 face update:
//   1. Tap in IDLE  → wakeword_triggered() true  (LISTEN would be sent)
//   2. Tap in LISTENING via wakeword_ptt_finish() → wakeword_ended() true (END would be sent)
//   3. After wakeword_clear(), fresh tap triggers again (proves lockout cannot recur)
//   4. While triggered, wakeword_push_frame() suppresses the AFE feed path
//      (no crash on HAVE_ESP_SR=0, but the early-return guard is exercised)

#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>

/* Tick counter controlled by the test harness. */
volatile uint32_t g_test_tick_ms = 0;

/* Pull in the wakeword implementation with all ESP-IDF headers stubbed out.
 * The Makefile compiles wakeword.c (via the wakeword_src.c alias) separately
 * so this file only needs the public header. */
#include "wakeword.h"

/* vt_agent_count() is declared extern in wakeword.c; provide a stub. */
int vt_agent_count(void) { return 0; }

/* wakeword.c mirrors diagnostics via vt_remote_log() (remote_log.h) — added
 * after this test was first written.  The host build has no WebSocket to write
 * to, so swallow the call to keep the link resolved. */
#include <stdarg.h>
void vt_remote_log(const char *fmt, ...) { (void)fmt; }

/* ── Minimal test framework ───────────────────────────────────────────────── */

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

/* ── Helpers ──────────────────────────────────────────────────────────────── */

/* Simulate a short tap: press then immediate release (<1 s). */
static void do_tap(void)
{
    wakeword_ptt_press();
    /* No tick advance: elapsed < 1000 ms → short tap, s_ended stays false. */
    wakeword_ptt_release();
}

/* ── Tests ────────────────────────────────────────────────────────────────── */

static void test_tap_in_idle_starts_listen(void)
{
    puts("test_tap_in_idle_starts_listen");
    wakeword_clear();
    g_test_tick_ms = 0;

    do_tap();

    ASSERT(wakeword_triggered(),
           "After tap in IDLE, wakeword_triggered() must be true (voice_task sends LISTEN)");
    ASSERT(!wakeword_ended(),
           "After short tap, wakeword_ended() must be false (utterance still open)");
}

static void test_ptt_finish_ends_listening(void)
{
    puts("test_ptt_finish_ends_listening");
    wakeword_clear();
    g_test_tick_ms = 0;

    /* Enter LISTENING state (tap to start). */
    do_tap();
    ASSERT(wakeword_triggered(), "Pre-condition: triggered after tap");
    ASSERT(!wakeword_ended(),    "Pre-condition: not yet ended after short tap");

    /* User taps again → tap-to-stop → wakeword_ptt_finish() (the core fix). */
    wakeword_ptt_finish();

    ASSERT(wakeword_ended(),
           "After wakeword_ptt_finish(), wakeword_ended() must be true (voice_task sends END)");
    ASSERT(wakeword_triggered(),
           "s_triggered stays true until wakeword_clear() — voice_task clears after END");
}

static void test_clear_allows_fresh_tap(void)
{
    puts("test_clear_allows_fresh_tap");
    wakeword_clear();
    g_test_tick_ms = 0;

    /* Simulate a complete utterance cycle: tap → finish → clear. */
    do_tap();
    wakeword_ptt_finish();
    ASSERT(wakeword_ended(), "Pre-condition: utterance ended");

    /* voice_task calls wakeword_clear() after sending END. */
    wakeword_clear();

    ASSERT(!wakeword_triggered(), "After wakeword_clear(), triggered must be false");
    ASSERT(!wakeword_ended(),     "After wakeword_clear(), ended must be false");

    /* Fresh tap must work — this is the lockout regression assertion. */
    do_tap();

    ASSERT(wakeword_triggered(),
           "After clear(), a fresh tap must set triggered again "
           "(proves the s_triggered lockout cannot recur)");
    ASSERT(!wakeword_ended(),
           "Fresh tap after clear must not immediately end (utterance is open)");
}

static void test_vad_timeout_fires_without_audio(void)
{
    puts("test_vad_timeout_fires_without_audio");
    wakeword_clear();
    g_test_tick_ms = 0;

    /* Start a triggered utterance. */
    do_tap();
    ASSERT(wakeword_triggered(), "Pre-condition: triggered");
    ASSERT(!wakeword_ended(),    "Pre-condition: not ended");

    /* Advance the tick to just before the VAD timeout. */
    g_test_tick_ms = 7999;   /* 7999 ms < VAD_TIMEOUT_MS (8000 ms) */
    wakeword_tick();
    ASSERT(!wakeword_ended(), "At 7999 ms, VAD timeout must not yet have fired");

    /* One more ms — past the timeout. */
    g_test_tick_ms = 8001;
    wakeword_tick();
    ASSERT(wakeword_ended(),
           "At 8001 ms, wakeword_tick() must fire the VAD timeout and set ended=true");
}

static void test_ptt_finish_noop_when_idle(void)
{
    puts("test_ptt_finish_noop_when_idle");
    wakeword_clear();
    g_test_tick_ms = 0;

    /* Calling finish with no active utterance must be a no-op. */
    wakeword_ptt_finish();

    ASSERT(!wakeword_triggered(), "finish() on IDLE state must not set triggered");
    ASSERT(!wakeword_ended(),     "finish() on IDLE state must not set ended");
}

static void test_push_frame_suppressed_while_triggered(void)
{
    puts("test_push_frame_suppressed_while_triggered (HAVE_ESP_SR=0, no crash)");
    wakeword_clear();
    g_test_tick_ms = 0;

    do_tap();
    ASSERT(wakeword_triggered(), "Pre-condition: triggered");

    /* Feeding a frame while triggered must not crash and must not clear triggered.
     * With HAVE_ESP_SR=0 the AFE path is compiled out; the function returns early
     * after the timeout check (which does not fire at t=0). */
    uint8_t silence[512] = {0};
    wakeword_push_frame(silence, sizeof(silence));

    ASSERT(wakeword_triggered(),
           "push_frame() while triggered must not clear triggered flag");
    ASSERT(!wakeword_ended(),
           "push_frame() at t=0 must not fire timeout (elapsed < 8000 ms)");
}

/* ── Main ─────────────────────────────────────────────────────────────────── */

int main(void)
{
    puts("=== wakeword PTT state machine tests ===");
    test_tap_in_idle_starts_listen();
    test_ptt_finish_ends_listening();
    test_clear_allows_fresh_tap();
    test_vad_timeout_fires_without_audio();
    test_ptt_finish_noop_when_idle();
    test_push_frame_suppressed_while_triggered();

    printf("\n=== Results: %d passed, %d failed ===\n", s_pass, s_fail);
    return s_fail > 0 ? 1 : 0;
}
