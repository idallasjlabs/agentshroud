// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
#include "ui_face.h"
#include "ws_client.h"
#include "wakeword.h"
#include "lvgl_kawaii_face.h"
#include "bsp/esp-bsp.h"
#include "lvgl.h"
#include "esp_log.h"

static const char *TAG = "ui_face";

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

static void _touch_pressed(lv_event_t *e)
{
    /* Tap-to-toggle state machine:
     *   SPEAKING    → interrupt TTS playback (unchanged)
     *   LISTENING   → end utterance now (NEW: tap-to-stop)
     *   THINKING    → no-op (query already in flight; tapping _ptt_start here
     *                  would latch s_triggered and permanently block the next tap)
     *   IDLE / DISC → start a new utterance
     *
     * The touchscreen overlay is PRESSED-only: LV_EVENT_RELEASED is NOT registered
     * (removed with this change) so wakeword_ptt_release() is never called from
     * touch — the physical BSP_BUTTON_MAIN retains its hold-to-talk behaviour. */
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
             * Silently ignore: calling _ptt_start here would latch s_triggered and
             * block all subsequent taps until the next wakeword_clear(). */
            break;

        default:
            /* IDLE or DISCONNECTED: start a new utterance. */
            wakeword_ptt_press();
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
    // PRESSED only — tap-to-toggle model.  LV_EVENT_RELEASED is intentionally
    // omitted: wakeword_ptt_release() must NOT be called from touch because the
    // touch overlay uses tap-to-stop (wakeword_ptt_finish) rather than hold-to-talk.
    // The physical BSP_BUTTON_MAIN still uses hold-to-talk via _btn_released.
    lv_obj_add_event_cb(s_touch, _touch_pressed,  LV_EVENT_PRESSED,    NULL);

    bsp_display_unlock();

    ESP_LOGI(TAG, "kawaii face initialised");
}

void ui_face_set_state(ws_vg_state_t state)
{
    if (state == s_current_state) return;
    s_current_state = state;

    // face_set_emotion acquires lvgl_port lock internally — no outer lock needed.
    face_set_emotion(_state_to_emotion(state), false);

    const char *status_text;
    switch (state) {
        case WS_VG_STATE_IDLE:         status_text = "Say 'Hi, ESP' or tap to talk"; break;
        case WS_VG_STATE_LISTENING:    status_text = "Listening...";                  break;
        case WS_VG_STATE_THINKING:     status_text = "Thinking...";                   break;
        case WS_VG_STATE_SPEAKING:     status_text = "Speaking...";                   break;
        case WS_VG_STATE_DISCONNECTED: status_text = "Reconnecting...";               break;
        default:                       status_text = "";                               break;
    }

    bsp_display_lock(0);
    lv_label_set_text(s_status, status_text);
    bsp_display_unlock();
}

void ui_face_set_agent(const char *name)
{
    if (!s_agent_label || !name) return;
    bsp_display_lock(0);
    lv_label_set_text(s_agent_label, name);
    bsp_display_unlock();
    ESP_LOGI(TAG, "agent → %s", name);
}
