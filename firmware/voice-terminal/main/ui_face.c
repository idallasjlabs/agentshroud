// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
#include "ui_face.h"
#include "ws_client.h"
#include "wakeword.h"
#include "remote_log.h"
#include "lvgl_kawaii_face.h"
#include "bsp/esp-bsp.h"
#include "lvgl.h"
#include "esp_log.h"

static const char *TAG = "ui_face";

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
    /* Tap-to-toggle state machine:
     *   SPEAKING    → interrupt TTS playback (unchanged)
     *   LISTENING   → end utterance now (NEW: tap-to-stop)
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

    if (state == WS_VG_STATE_LISTENING ||
        state == WS_VG_STATE_THINKING  ||
        state == WS_VG_STATE_SPEAKING) {
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
