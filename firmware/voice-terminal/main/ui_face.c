// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
#include "ui_face.h"
#include "ws_client.h"
#include "wakeword.h"
#include "remote_log.h"
#include "lvgl_kawaii_face.h"
#include "bsp/esp-bsp.h"
#include "lvgl.h"
#include "esp_log.h"
#include "esp_heap_caps.h"
#include "esp_memory_utils.h"   /* esp_ptr_external_ram */
#include <string.h>             /* memcpy */

static const char *TAG = "ui_face";

/* SCRUM-58 experiment #1 — kawaii canvas heap placement.
 *
 * The kawaii face renders into an LVGL canvas whose backing pixel buffer is
 * allocated inside the lvgl_kawaii_face component.  On the ESP32-S3-BOX-3 the
 * default allocator lands large buffers in PSRAM (external SPI RAM).  A canvas
 * in PSRAM is a problem here: every face redraw READS the whole buffer over the
 * same SPI/octal bus that audio (I2S DMA) and TLS traffic contend for, and that
 * bus contention is the mechanism behind the render-stalls-WiFi drops the file
 * already documents (see _apply_state_cb).  Moving the canvas into internal DRAM
 * takes those reads off the shared bus.
 *
 * This experiment (a) LOGS whether the canvas buffer is in PSRAM or internal
 * DRAM so the placement is visible in the device log, and (b) if it is in PSRAM
 * AND a same-sized internal-DRAM buffer will fit, re-points the canvas at a DRAM
 * copy via the public lv_canvas API.  It is deliberately confined to the LVGL
 * canvas buffer — it does NOT touch BSP I2S DMA descriptor sizing (OFF-LIMITS,
 * boot-brick risk, 2026-07-07).
 *
 * Experiment #2 (animate-the-face-during-SPEAKING) is a SEPARATE follow-up and
 * is intentionally NOT implemented here.
 */

/* Depth-first search for the first lv_canvas descendant of `root`. The kawaii
 * component owns the canvas; we locate it by class rather than by reaching into
 * component internals, so this stays valid across kawaii-face versions. */
static lv_obj_t *_find_canvas(lv_obj_t *root)
{
    if (root == NULL) return NULL;
    if (lv_obj_check_type(root, &lv_canvas_class)) return root;
    uint32_t n = lv_obj_get_child_count(root);
    for (uint32_t i = 0; i < n; i++) {
        lv_obj_t *hit = _find_canvas(lv_obj_get_child(root, i));
        if (hit) return hit;
    }
    return NULL;
}

/* Report the canvas buffer's heap placement and, when it sits in PSRAM and a
 * same-sized internal-DRAM buffer will fit, relocate it into internal DRAM.
 * Best-effort and fully guarded: any missing canvas / buffer / OOM leaves the
 * original (working) PSRAM buffer untouched — we only ever log in that case. */
static void _report_and_place_canvas(lv_obj_t *face_root)
{
    lv_obj_t *canvas = _find_canvas(face_root);
    if (canvas == NULL) {
        ESP_LOGW(TAG, "canvas-placement: no lv_canvas found under face panel — skipping");
        vt_remote_log("canvas-placement: no canvas found");
        return;
    }

    lv_image_dsc_t *dsc = lv_canvas_get_image(canvas);
    if (dsc == NULL || dsc->data == NULL || dsc->data_size == 0) {
        ESP_LOGW(TAG, "canvas-placement: canvas has no buffer yet — skipping");
        vt_remote_log("canvas-placement: no buffer");
        return;
    }
    const void *buf = dsc->data;
    size_t buf_bytes = dsc->data_size;

    bool in_psram = esp_ptr_external_ram(buf);
    ESP_LOGI(TAG,
             "canvas-placement: buf=%p bytes=%u region=%s (%ux%u cf=%d)",
             buf, (unsigned)buf_bytes, in_psram ? "PSRAM" : "INTERNAL-DRAM",
             (unsigned)dsc->header.w, (unsigned)dsc->header.h, (int)dsc->header.cf);
    vt_remote_log("canvas-placement: %s %u bytes",
                  in_psram ? "PSRAM" : "DRAM", (unsigned)buf_bytes);

    if (!in_psram) {
        return;   /* already internal — nothing to do */
    }

    /* Only relocate if a same-sized internal-DRAM block will fit with margin.
     * Reads on the WiFi/TLS path are the reason for the move; we never want the
     * move itself to exhaust internal DRAM and starve the stacks. */
    size_t dram_free = heap_caps_get_free_size(MALLOC_CAP_INTERNAL | MALLOC_CAP_8BIT);
    const size_t DRAM_MARGIN = 24 * 1024;   /* leave headroom for stacks/TLS */
    if (buf_bytes + DRAM_MARGIN > dram_free) {
        ESP_LOGW(TAG,
                 "canvas-placement: canvas in PSRAM but internal DRAM too tight "
                 "(need %u, free %u) — leaving in PSRAM",
                 (unsigned)buf_bytes, (unsigned)dram_free);
        vt_remote_log("canvas-placement: DRAM tight, staying PSRAM");
        return;
    }

    void *dram_buf = heap_caps_malloc(buf_bytes, MALLOC_CAP_INTERNAL | MALLOC_CAP_8BIT);
    if (dram_buf == NULL) {
        ESP_LOGW(TAG, "canvas-placement: internal-DRAM alloc failed — leaving in PSRAM");
        vt_remote_log("canvas-placement: DRAM alloc failed");
        return;
    }
    memcpy(dram_buf, buf, buf_bytes);
    lv_canvas_set_buffer(canvas, dram_buf, dsc->header.w, dsc->header.h,
                         (lv_color_format_t)dsc->header.cf);
    /* NOTE: the original PSRAM buffer is owned by the kawaii component and is
     * freed when the component tears the canvas down; we intentionally do not
     * free it here.  This leaks the PSRAM copy for the life of the canvas — an
     * acceptable one-time cost (PSRAM has MBs free) to keep the hot redraw path
     * in internal DRAM. */
    ESP_LOGI(TAG, "canvas-placement: relocated canvas buffer PSRAM → internal DRAM (%p)", dram_buf);
    vt_remote_log("canvas-placement: moved to DRAM %p", dram_buf);
}

/* DIAGNOSTIC BUILD FLAG — set to 1 to disable ALL kawaii face rendering.
 * The 2026-07-02 A/B test with this flag CONVICTED the face redraw: with
 * rendering off, streaming survived full utterances and completed the first
 * end-to-end voice→Hermes→TTS loop; with it on, the relay FIN'd every
 * utterance within 0.3–9 s.  The production mitigation is
 * face_animation_pause(true) while LISTENING (see _apply_state_cb). */
#define VT_DIAG_NO_FACE 0   /* face restored — store-and-forward delivery makes
                             * the transport drop-tolerant, and the freeze-during-
                             * interaction below keeps renders out of the (now
                             * short, retried) delivery bursts */

static lv_obj_t      *s_status        = NULL;
static lv_obj_t      *s_agent_label   = NULL;
static lv_obj_t      *s_touch         = NULL;
static ws_vg_state_t  s_current_state = WS_VG_STATE_IDLE;

static face_emotion_t _state_to_emotion(ws_vg_state_t state)
{
    switch (state) {
        case WS_VG_STATE_IDLE:         return FACE_NEUTRAL;
        case WS_VG_STATE_LISTENING:    return FACE_SURPRISED;
        case WS_VG_STATE_THINKING:     return FACE_WORKING_HARD;
        case WS_VG_STATE_SPEAKING:     return FACE_HAPPY;
        case WS_VG_STATE_DISCONNECTED: return FACE_WORRIED;
        default:                       return FACE_NEUTRAL;
    }
}

/* Fallback handler registered on LV_EVENT_SHORT_CLICKED (fires on release).
 * ONLY starts an utterance from IDLE — never calls wakeword_ptt_finish() so
 * that it cannot cancel an utterance that LV_EVENT_PRESSED already started. */
static void _touch_start_only(lv_event_t *e)
{
    (void)e;
    /* Gate on !wakeword_triggered(): PRESSED already started the utterance
     * ~200 ms before this fires (finger release), and the local UI state may
     * still read IDLE because the server's LISTENING frame hasn't landed yet.
     * Without the gate this double-fires into the PTT ignore guard (noise). */
    if ((s_current_state == WS_VG_STATE_IDLE      ||
         s_current_state == WS_VG_STATE_DISCONNECTED ||
         s_current_state == WS_VG_STATE_UNKNOWN) && !wakeword_triggered()) {
        ESP_LOGI(TAG, "touch fallback (SHORT_CLICKED): starting PTT");
        vt_remote_log("touch SHORT_CLICKED fallback: starting PTT");
        face_animation_pause(true);   /* synchronous freeze — see _touch_pressed */
        wakeword_ptt_press();
        /* A tap is press+release: without the release, s_ptt_held stays
         * latched (the touch overlay has no RELEASED handler) and VAD
         * endpointing is skipped as "button held" — every touch utterance
         * ran to the 8 s cap (live 2026-07-06, zero vad: trace lines). */
        wakeword_ptt_release();
    }
}

static void _touch_pressed(lv_event_t *e)
{
    ESP_LOGI(TAG, "touch: state=%d", (int)s_current_state);
    vt_remote_log("touch PRESSED state=%d", (int)s_current_state);

    /* Tap-to-stop, keyed on the firmware's OWN capture state rather than
     * s_current_state: s_current_state only updates once the server's
     * LISTENING frame round-trips back (~300 ms, longer under network/host
     * load — see 2026-08-26 trace, WS drops mid-utterance made this worse).
     * A second tap landing in that window fell through to the `default`
     * case below, called wakeword_ptt_press() while already triggered, hit
     * _ptt_start()'s guard, and silently no-op'd — leaving no way to escape
     * the VAD/8s-cap wait once a tap had started capture but the state sync
     * hadn't landed yet. wakeword_triggered()/wakeword_ended() are local and
     * immediate, so this fires the instant the user taps again regardless of
     * what the server has (or hasn't) confirmed. wakeword_ptt_finish() is
     * already a safe no-op when nothing is triggered. */
    if (wakeword_triggered() && !wakeword_ended()) {
        wakeword_ptt_finish();
        return;
    }

    /* Tap-to-toggle state machine:
     *   SPEAKING    → interrupt TTS playback (unchanged)
     *   LISTENING   → end utterance now (redundant with the check above,
     *                  kept as a documented, explicit path)
     *   THINKING    → no-op (query already in flight; tapping _ptt_start here
     *                  would latch s_triggered and permanently block the next tap)
     *   IDLE / DISC → start a new utterance */
    switch (s_current_state) {
        case WS_VG_STATE_SPEAKING:
            wakeword_tts_stop_request();
            s_current_state = WS_VG_STATE_IDLE;
            // smooth=true: lock-free flag write — safe inside LVGL event callback.
            face_set_emotion(FACE_NEUTRAL, true);
            bsp_display_lock(0);
            lv_label_set_text(s_status, "Say 'Hi, ESP' or tap to talk");
            bsp_display_unlock();
            break;

        case WS_VG_STATE_LISTENING:
            /* Tap-to-stop: force-end the current utterance so voice_task sends END
             * on its next iteration.  Without this, the user had to wait the full
             * 8-second VAD timeout — the root cause of the "stuck in listening" bug. */
            wakeword_ptt_finish();
            break;

        case WS_VG_STATE_THINKING:
            /* Query already dispatched — nothing we can do from the client side.
             * Ignore: calling _ptt_start here would latch s_triggered and block
             * all subsequent taps until the next wakeword_clear().  DIAGNOSTIC log
             * so a tap during THINKING is visible in the trace rather than silent. */
            ESP_LOGI(TAG, "touch: THINKING — ignored (query in flight)");
            vt_remote_log("touch ignored: THINKING (query in flight)");
            break;

        default:
            /* IDLE or DISCONNECTED: start a new utterance.
             * Freeze the face SYNCHRONOUSLY, before the first PCM byte
             * streams — we're in the LVGL task here, so this stops the very
             * next animation frame.  Waiting for the server's LISTENING state
             * to pause (~300 ms round trip) let 3-4 idle frames render into
             * the streaming window, which was enough to stall WiFi and get
             * the connection FIN'd (drops observed at 0.46 s). */
            face_animation_pause(true);
            wakeword_ptt_press();
            /* Tap = press+release — see _touch_start_only.  Clears s_ptt_held
             * (<1 s → short-tap path keeps the utterance triggered) so the
             * VAD silence endpointing governs the end of the utterance. */
            wakeword_ptt_release();
            break;
    }
}

void ui_face_init(void)
{
    // Create background, face panel container, and overlay labels inside the lock.
    bsp_display_lock(0);

    lv_obj_t *scr = lv_screen_active();
    lv_obj_set_style_bg_color(scr, lv_color_hex(0x1a1a2e), LV_PART_MAIN);

    lv_obj_t *face_panel = lv_obj_create(scr);
    lv_obj_set_size(face_panel, 220, 220);
    lv_obj_align(face_panel, LV_ALIGN_CENTER, 0, -10);
    lv_obj_set_style_bg_opa(face_panel, LV_OPA_TRANSP, LV_PART_MAIN);
    lv_obj_set_style_border_width(face_panel, 0, LV_PART_MAIN);
    lv_obj_set_style_pad_all(face_panel, 0, LV_PART_MAIN);
    lv_obj_remove_flag(face_panel, LV_OBJ_FLAG_SCROLLABLE);

    s_status = lv_label_create(scr);
    lv_obj_set_style_text_color(s_status, lv_color_hex(0x888888), LV_PART_MAIN);
    lv_obj_set_style_text_font(s_status, &lv_font_montserrat_20, LV_PART_MAIN);
    lv_obj_align(s_status, LV_ALIGN_BOTTOM_MID, 0, -8);
    lv_label_set_text(s_status, "Say 'Hi, ESP' or tap to talk");

    s_agent_label = lv_label_create(scr);
    lv_obj_set_style_text_color(s_agent_label, lv_color_hex(0x4fc3f7), LV_PART_MAIN);
    lv_obj_set_style_text_font(s_agent_label, &lv_font_montserrat_14, LV_PART_MAIN);
    lv_obj_set_pos(s_agent_label, 6, 6);
    lv_label_set_text(s_agent_label, "");

    bsp_display_unlock();

#if VT_DIAG_NO_FACE
    ESP_LOGW(TAG, "DIAGNOSTIC: kawaii face rendering DISABLED (labels only)");
    (void)face_panel;
#else
    // face_lock() inside face_animation_init is a no-op (no lock fns registered).
    // Hold the display lock here so LVGL object creation doesn't race taskLVGL.
    bsp_display_lock(0);
    face_config_t cfg = {
        .parent          = face_panel,
        .animation_speed = 100,  /* 10 fps — keeps SPI queue clear under I2S load */
        .blink_interval  = 4000,
        .auto_blink      = true,
        .bg_color        = lv_color_hex(0x1a1a2e),
    };
    ESP_ERROR_CHECK(face_animation_init(&cfg));
    face_set_emotion(FACE_NEUTRAL, false);
    /* SCRUM-58 exp #1: log the canvas buffer's heap placement and, if it landed
     * in PSRAM, relocate it into internal DRAM (keeps redraw reads off the
     * SPI/octal bus that audio + TLS share).  Runs under the display lock so the
     * lv_canvas_* calls don't race taskLVGL.  DMA descriptor config untouched. */
    _report_and_place_canvas(face_panel);
    bsp_display_unlock();
#endif

    // Touch overlay — created last so it sits at the highest z-order.
    bsp_display_lock(0);

    s_touch = lv_obj_create(scr);
    lv_obj_set_size(s_touch,
                    lv_display_get_horizontal_resolution(NULL),
                    lv_display_get_vertical_resolution(NULL));
    lv_obj_set_pos(s_touch, 0, 0);
    lv_obj_set_style_bg_opa(s_touch, LV_OPA_TRANSP, LV_PART_MAIN);
    lv_obj_set_style_border_width(s_touch, 0, LV_PART_MAIN);
    lv_obj_remove_flag(s_touch, LV_OBJ_FLAG_SCROLLABLE);
    /* Explicitly set CLICKABLE — default for lv_obj_create, but set it
     * defensively to guard against BSP or LVGL 9 theme overrides that
     * might clear it.  Without this, a transparent overlay may silently
     * receive no LV_EVENT_PRESSED events in LVGL 9.x. */
    lv_obj_add_flag(s_touch, LV_OBJ_FLAG_CLICKABLE);
    /* PRIMARY: PRESSED fires on touch-down.  Register on the overlay. */
    lv_obj_add_event_cb(s_touch, _touch_pressed, LV_EVENT_PRESSED, NULL);
    /* FALLBACK: SHORT_CLICKED fires on quick release — catches the case
     * where LVGL 9 / BSP 3.2.0 does not deliver PRESSED to a transparent
     * overlay.  Guard: only IDLE/DISC → start; do NOT call ptt_finish from
     * the fallback path to avoid immediately stopping what PRESSED started. */
    lv_obj_add_event_cb(s_touch, _touch_start_only, LV_EVENT_SHORT_CLICKED, NULL);
    lv_obj_move_foreground(s_touch);

    bsp_display_unlock();

    ESP_LOGI(TAG, "kawaii face initialised");
}

/* Applies a state change — ALWAYS runs in the LVGL task via lv_async_call.
 * No cross-task display locking: we're already in the LVGL thread, so direct
 * lv_* calls are safe by definition, and face_set_emotion(smooth=true) is a
 * lock-free flag write applied by the animation timer (same thread). */
static void _apply_state_cb(void *param)
{
    ws_vg_state_t state = (ws_vg_state_t)(intptr_t)param;
    if (state == s_current_state) return;
    s_current_state = state;

    if (state == WS_VG_STATE_THINKING  ||
        state == WS_VG_STATE_SPEAKING) {
        /* LISTENING now ANIMATES: capture is store-and-forward (no network
         * during recording), so the historical render-stalls-WiFi reason no
         * longer applies to it.  Delivery (THINKING) and TTS (SPEAKING)
         * stay frozen — those are the network-critical windows. */
        /* CRITICAL: freeze ALL face redraw for the entire interaction —
         * mic upstream (LISTENING), reply wait (THINKING), and TTS downlink
         * (SPEAKING).  The kawaii PSRAM canvas fills stall the WiFi stack
         * long enough that the relay drops the connection (proven by the
         * face-off A/B test: zero renders = zero drops + first full
         * end-to-end).  No emotion change either — a single redraw burst is
         * a risk.  The face resumes animating at IDLE. */
        face_animation_pause(true);
    } else {
        face_animation_pause(false);
        face_set_emotion(_state_to_emotion(state), true);
    }

    const char *status_text;
    switch (state) {
        case WS_VG_STATE_IDLE:         status_text = "Say 'Hi, ESP' or tap to talk"; break;
        case WS_VG_STATE_LISTENING:    status_text = "Listening...";                  break;
        case WS_VG_STATE_THINKING:     status_text = "Thinking...";                   break;
        case WS_VG_STATE_SPEAKING:     status_text = "Speaking...";                   break;
        case WS_VG_STATE_DISCONNECTED: status_text = "Reconnecting...";               break;
        default:                       status_text = "";                               break;
    }
    lv_label_set_text(s_status, status_text);
}

void ui_face_set_state(ws_vg_state_t state)
{
    /* Post into the LVGL thread and return immediately.  Callable from ANY
     * task (websocket_task included) with zero blocking: the previous design
     * ran face redraws + display-lock waits on a worker task and wedged —
     * beacon evidence: stateq pinned at 3 for minutes after a WiFi drop. */
    lv_async_call(_apply_state_cb, (void *)(intptr_t)state);
}

static void _apply_agent_cb(void *param)
{
    if (s_agent_label) lv_label_set_text(s_agent_label, (const char *)param);
}

void ui_face_set_agent(const char *name)
{
    if (!name) return;
    /* name points into the static VT_AGENTS table — stays valid forever, so
     * passing the pointer through the async queue is safe. */
    lv_async_call(_apply_agent_cb, (void *)name);
    ESP_LOGI(TAG, "agent → %s", name);
}
