#include "ui_face.h"
#include "bsp/esp-bsp.h"
#include "lvgl.h"
#include "ws_client.h"
#include "wakeword.h"
#include "esp_log.h"

static const char *TAG = "ui_face";

/* ── Layout constants (320 × 240) ────────────────────────────────────────── */
#define FACE_CX      160   /* horizontal centre */
#define FACE_CY      120   /* vertical centre */
#define EYE_RADIUS    18
#define PUPIL_RADIUS   8
#define EYE_SPACING   55   /* half-distance between eye centres */
#define EYE_Y        100   /* eye vertical position */
#define MOUTH_W       70   /* mouth width */
#define MOUTH_H       20   /* mouth height (arc) */
#define MOUTH_Y      150   /* mouth vertical position */

/* ── Widget handles ─────────────────────────────────────────────────────── */
static lv_obj_t *s_eye_l    = NULL;  /* left eye white */
static lv_obj_t *s_eye_r    = NULL;  /* right eye white */
static lv_obj_t *s_pupil_l  = NULL;
static lv_obj_t *s_pupil_r  = NULL;
static lv_obj_t *s_mouth    = NULL;  /* rounded-rect mouth */
static lv_obj_t *s_status   = NULL;  /* small status label */
static lv_obj_t *s_touch    = NULL;  /* full-screen transparent touch overlay */
static lv_anim_t s_mouth_anim;

static ws_vg_state_t s_current_state = WS_VG_STATE_IDLE;

/* ── Helpers ─────────────────────────────────────────────────────────────── */

static lv_obj_t *_make_circle(lv_obj_t *parent, lv_coord_t x, lv_coord_t y,
                               lv_coord_t r, lv_color_t color)
{
    lv_obj_t *obj = lv_obj_create(parent);
    lv_obj_set_size(obj, r * 2, r * 2);
    lv_obj_set_style_radius(obj, LV_RADIUS_CIRCLE, LV_PART_MAIN);
    lv_obj_set_style_bg_color(obj, color, LV_PART_MAIN);
    lv_obj_set_style_border_width(obj, 0, LV_PART_MAIN);
    lv_obj_set_pos(obj, x - r, y - r);
    return obj;
}

static void _mouth_anim_cb(void *obj, int32_t v)
{
    if (!obj) return;
    lv_obj_set_height((lv_obj_t *)obj, (lv_coord_t)v);
}

static void _start_mouth_anim(void)
{
    lv_anim_init(&s_mouth_anim);
    lv_anim_set_var(&s_mouth_anim, s_mouth);
    lv_anim_set_exec_cb(&s_mouth_anim, _mouth_anim_cb);
    lv_anim_set_values(&s_mouth_anim, MOUTH_H / 4, MOUTH_H);
    lv_anim_set_time(&s_mouth_anim, 400);
    lv_anim_set_playback_time(&s_mouth_anim, 300);
    lv_anim_set_repeat_count(&s_mouth_anim, LV_ANIM_REPEAT_INFINITE);
    lv_anim_start(&s_mouth_anim);
}

/* ── Touch-to-talk overlay callbacks ─────────────────────────────────────── */

static void _touch_pressed(lv_event_t *e)
{
    (void)e;
    wakeword_ptt_press();
}

static void _touch_released(lv_event_t *e)
{
    (void)e;
    wakeword_ptt_release();
}

/* ── Public API ─────────────────────────────────────────────────────────── */

void ui_face_init(void)
{
    lv_obj_t *scr = lv_scr_act();

    /* Eyes */
    s_eye_l   = _make_circle(scr, FACE_CX - EYE_SPACING, EYE_Y,
                              EYE_RADIUS, lv_color_hex(0xffffff));
    s_eye_r   = _make_circle(scr, FACE_CX + EYE_SPACING, EYE_Y,
                              EYE_RADIUS, lv_color_hex(0xffffff));
    s_pupil_l = _make_circle(scr, FACE_CX - EYE_SPACING, EYE_Y,
                              PUPIL_RADIUS, lv_color_hex(0x1a1a2e));
    s_pupil_r = _make_circle(scr, FACE_CX + EYE_SPACING, EYE_Y,
                              PUPIL_RADIUS, lv_color_hex(0x1a1a2e));

    /* Mouth — a wide rounded rectangle; height animated when speaking */
    s_mouth = lv_obj_create(scr);
    lv_obj_set_size(s_mouth, MOUTH_W, MOUTH_H);
    lv_obj_set_style_radius(s_mouth, 10, LV_PART_MAIN);
    lv_obj_set_style_bg_color(s_mouth, lv_color_hex(0xffffff), LV_PART_MAIN);
    lv_obj_set_style_border_width(s_mouth, 0, LV_PART_MAIN);
    lv_obj_set_pos(s_mouth, FACE_CX - MOUTH_W / 2, MOUTH_Y);

    /* Status text */
    s_status = lv_label_create(scr);
    lv_obj_set_style_text_color(s_status, lv_color_hex(0x888888), LV_PART_MAIN);
    lv_obj_set_style_text_font(s_status, &lv_font_montserrat_20, LV_PART_MAIN);
    lv_obj_align(s_status, LV_ALIGN_BOTTOM_MID, 0, -10);
    lv_label_set_text(s_status, "Say 'Hi, ESP' or tap to talk");

    /* Touchscreen PTT overlay — full-screen transparent object on top of the
     * face widgets so any screen tap triggers PTT.  The physical button
     * (BSP_BUTTON_MAIN) is registered separately in wakeword.c and still works. */
    s_touch = lv_obj_create(scr);
    lv_obj_set_size(s_touch, LV_HOR_RES, LV_VER_RES);
    lv_obj_set_pos(s_touch, 0, 0);
    lv_obj_set_style_bg_opa(s_touch, LV_OPA_TRANSP, LV_PART_MAIN);
    lv_obj_set_style_border_width(s_touch, 0, LV_PART_MAIN);
    lv_obj_clear_flag(s_touch, LV_OBJ_FLAG_SCROLLABLE);
    lv_obj_add_event_cb(s_touch, _touch_pressed,  LV_EVENT_PRESSED,    NULL);
    lv_obj_add_event_cb(s_touch, _touch_released, LV_EVENT_RELEASED,   NULL);
    lv_obj_add_event_cb(s_touch, _touch_released, LV_EVENT_PRESS_LOST, NULL);

    ESP_LOGI(TAG, "Face initialised (touchscreen PTT active)");
}

void ui_face_set_state(ws_vg_state_t state)
{
    if (state == s_current_state) return;
    s_current_state = state;

    /* portMAX_DELAY: wait for the LVGL timer task to release the mutex before
     * modifying any LVGL objects.  The previous timeout of 0 (non-blocking)
     * silently skipped the lock and mutated LVGL state from a foreign task,
     * which could corrupt the touch overlay's event callback list and prevent
     * subsequent taps from firing. */
    bsp_display_lock(portMAX_DELAY);

    switch (state) {
    case WS_VG_STATE_IDLE:
        /* Normal eyes, static mouth */
        lv_obj_set_size(s_eye_l, EYE_RADIUS * 2, EYE_RADIUS * 2);
        lv_obj_set_size(s_eye_r, EYE_RADIUS * 2, EYE_RADIUS * 2);
        lv_anim_del(s_mouth, _mouth_anim_cb);
        lv_obj_set_height(s_mouth, MOUTH_H / 3);
        lv_label_set_text(s_status, "Say 'Hi, ESP' or tap to talk");
        break;

    case WS_VG_STATE_LISTENING:
        /* Wide eyes */
        lv_obj_set_size(s_eye_l, EYE_RADIUS * 2 + 8, EYE_RADIUS * 2 + 8);
        lv_obj_set_size(s_eye_r, EYE_RADIUS * 2 + 8, EYE_RADIUS * 2 + 8);
        lv_anim_del(s_mouth, _mouth_anim_cb);
        lv_obj_set_height(s_mouth, MOUTH_H / 4);
        lv_label_set_text(s_status, "Listening...");
        break;

    case WS_VG_STATE_THINKING:
        /* Normal eyes, no mouth anim */
        lv_obj_set_size(s_eye_l, EYE_RADIUS * 2, EYE_RADIUS * 2);
        lv_obj_set_size(s_eye_r, EYE_RADIUS * 2, EYE_RADIUS * 2);
        lv_anim_del(s_mouth, _mouth_anim_cb);
        lv_obj_set_height(s_mouth, MOUTH_H / 6);
        lv_label_set_text(s_status, "Thinking...");
        break;

    case WS_VG_STATE_SPEAKING:
        /* Normal eyes, animated mouth */
        lv_obj_set_size(s_eye_l, EYE_RADIUS * 2, EYE_RADIUS * 2);
        lv_obj_set_size(s_eye_r, EYE_RADIUS * 2, EYE_RADIUS * 2);
        _start_mouth_anim();
        lv_label_set_text(s_status, "Speaking...");
        break;

    case WS_VG_STATE_DISCONNECTED:
        lv_obj_set_size(s_eye_l, EYE_RADIUS * 2, EYE_RADIUS * 2);
        lv_obj_set_size(s_eye_r, EYE_RADIUS * 2, EYE_RADIUS * 2);
        lv_anim_del(s_mouth, _mouth_anim_cb);
        lv_obj_set_height(s_mouth, MOUTH_H / 6);
        lv_label_set_text(s_status, "Reconnecting...");
        break;

    default:
        break;
    }

    bsp_display_unlock();
}
