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
static lv_obj_t *s_status   = NULL;  /* small status label (bottom) */
static lv_obj_t *s_agent    = NULL;  /* agent name label (top-left) */
static lv_obj_t *s_touch    = NULL;  /* full-screen transparent touch overlay */
static lv_anim_t   s_mouth_anim;
static lv_anim_t   s_pupil_anim;          /* THINKING pupil-scan animation */
static lv_timer_t *s_blink_timer = NULL;  /* periodic eye-blink (IDLE only) */

static ws_vg_state_t s_current_state = WS_VG_STATE_IDLE;

/* ── Helpers ─────────────────────────────────────────────────────────────── */

static lv_obj_t *_make_circle(lv_obj_t *parent, int32_t x, int32_t y,
                               int32_t r, lv_color_t color)
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
    lv_obj_set_height((lv_obj_t *)obj, (int32_t)v);
}

static void _start_mouth_anim(void)
{
    lv_anim_init(&s_mouth_anim);
    lv_anim_set_var(&s_mouth_anim, s_mouth);
    lv_anim_set_exec_cb(&s_mouth_anim, _mouth_anim_cb);
    lv_anim_set_values(&s_mouth_anim, MOUTH_H / 4, MOUTH_H);
    lv_anim_set_duration(&s_mouth_anim, 400);
    lv_anim_set_playback_duration(&s_mouth_anim, 300);
    lv_anim_set_repeat_count(&s_mouth_anim, LV_ANIM_REPEAT_INFINITE);
    lv_anim_start(&s_mouth_anim);
}

/* ── Eye blink (IDLE only) ───────────────────────────────────────────────── */

static void _blink_restore_cb(lv_timer_t *t)
{
    (void)t;
    lv_obj_set_height(s_eye_l, EYE_RADIUS * 2);
    lv_obj_set_height(s_eye_r, EYE_RADIUS * 2);
}

static void _blink_cb(lv_timer_t *t)
{
    (void)t;
    if (s_current_state != WS_VG_STATE_IDLE) return;
    lv_obj_set_height(s_eye_l, 2);
    lv_obj_set_height(s_eye_r, 2);
    lv_timer_t *restore = lv_timer_create(_blink_restore_cb, 150, NULL);
    lv_timer_set_repeat_count(restore, 1);
}

/* ── Pupil scan (THINKING) ───────────────────────────────────────────────── */

static void _pupil_x_anim_cb(void *var, int32_t v)
{
    (void)var;
    lv_obj_set_x(s_pupil_l, (FACE_CX - EYE_SPACING) - PUPIL_RADIUS + v);
    lv_obj_set_x(s_pupil_r, (FACE_CX + EYE_SPACING) - PUPIL_RADIUS + v);
}

static void _start_pupil_scan(void)
{
    lv_anim_init(&s_pupil_anim);
    lv_anim_set_var(&s_pupil_anim, s_pupil_l);
    lv_anim_set_exec_cb(&s_pupil_anim, _pupil_x_anim_cb);
    lv_anim_set_values(&s_pupil_anim, -14, 14);
    lv_anim_set_duration(&s_pupil_anim, 600);
    lv_anim_set_playback_duration(&s_pupil_anim, 600);
    lv_anim_set_repeat_count(&s_pupil_anim, LV_ANIM_REPEAT_INFINITE);
    lv_anim_start(&s_pupil_anim);
}

static void _stop_pupil_scan(void)
{
    lv_anim_del(s_pupil_l, _pupil_x_anim_cb);
    /* re-centre pupils */
    lv_obj_set_x(s_pupil_l, (FACE_CX - EYE_SPACING) - PUPIL_RADIUS);
    lv_obj_set_x(s_pupil_r, (FACE_CX + EYE_SPACING) - PUPIL_RADIUS);
}

/* ── Touch-to-talk overlay callbacks ─────────────────────────────────────── */

static void _touch_pressed(lv_event_t *e)
{
    (void)e;
    if (s_current_state == WS_VG_STATE_SPEAKING) {
        /* Interrupt TTS — already in the LVGL timer task so widget writes are
         * safe without re-acquiring the display lock.  Stop the mouth animation
         * and reset visuals immediately; the PCM callback will discard remaining
         * audio chunks until the server's "END" frame clears the stop flag. */
        wakeword_tts_stop_request();
        s_current_state = WS_VG_STATE_IDLE;
        lv_anim_del(s_mouth, _mouth_anim_cb);
        lv_obj_set_height(s_mouth, MOUTH_H / 3);
        lv_obj_set_style_bg_color(s_pupil_l, lv_color_hex(0x1a1a2e), LV_PART_MAIN);
        lv_obj_set_style_bg_color(s_pupil_r, lv_color_hex(0x1a1a2e), LV_PART_MAIN);
        lv_label_set_text(s_status, "Say 'Hi, ESP' or tap to talk");
    } else {
        wakeword_ptt_press();
    }
}

static void _touch_released(lv_event_t *e)
{
    (void)e;
    wakeword_ptt_release();
}

/* ── Public API ─────────────────────────────────────────────────────────── */

void ui_face_init(void)
{
    lv_obj_t *scr = lv_screen_active();

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

    /* Status text (bottom-centre) */
    s_status = lv_label_create(scr);
    lv_obj_set_style_text_color(s_status, lv_color_hex(0x888888), LV_PART_MAIN);
    lv_obj_set_style_text_font(s_status, &lv_font_montserrat_20, LV_PART_MAIN);
    lv_obj_align(s_status, LV_ALIGN_BOTTOM_MID, 0, -10);
    lv_label_set_text(s_status, "Say 'Hi, ESP' or tap to talk");

    /* Agent name label (top-left corner) — updated by ui_face_set_agent().
     * Shows the currently active proxied agent so the user always knows who
     * they are talking to.  Font is small so it doesn't crowd the face. */
    s_agent = lv_label_create(scr);
    lv_obj_set_style_text_color(s_agent, lv_color_hex(0x4fc3f7), LV_PART_MAIN);
    lv_obj_set_style_text_font(s_agent, &lv_font_montserrat_14, LV_PART_MAIN);
    lv_obj_set_pos(s_agent, 6, 6);
    lv_label_set_text(s_agent, "");

    /* Touchscreen PTT overlay — full-screen transparent object on top of the
     * face widgets so any screen tap triggers PTT.  The physical button
     * (BSP_BUTTON_MAIN) is registered separately in wakeword.c and still works. */
    s_touch = lv_obj_create(scr);
    lv_obj_set_size(s_touch, lv_display_get_horizontal_resolution(NULL), lv_display_get_vertical_resolution(NULL));
    lv_obj_set_pos(s_touch, 0, 0);
    lv_obj_set_style_bg_opa(s_touch, LV_OPA_TRANSP, LV_PART_MAIN);
    lv_obj_set_style_border_width(s_touch, 0, LV_PART_MAIN);
    lv_obj_remove_flag(s_touch, LV_OBJ_FLAG_SCROLLABLE);
    lv_obj_add_event_cb(s_touch, _touch_pressed,  LV_EVENT_PRESSED,    NULL);
    lv_obj_add_event_cb(s_touch, _touch_released, LV_EVENT_RELEASED,   NULL);
    lv_obj_add_event_cb(s_touch, _touch_released, LV_EVENT_PRESS_LOST, NULL);

    /* Periodic blink timer — fires every 4 s; callback is a no-op outside IDLE */
    s_blink_timer = lv_timer_create(_blink_cb, 4000, NULL);

    ESP_LOGI(TAG, "Face initialised (touchscreen PTT active)");
}

void ui_face_set_state(ws_vg_state_t state)
{
    if (state == s_current_state) return;
    s_current_state = state;

    /* timeout_ms=0 maps to portMAX_DELAY inside lvgl_port_lock() — waits until
     * the LVGL timer task releases the mutex before touching any lv_obj. */
    bsp_display_lock(0);

    switch (state) {
    case WS_VG_STATE_IDLE:
        /* Normal eyes, static mouth, navy pupils, blink active */
        lv_obj_set_size(s_eye_l, EYE_RADIUS * 2, EYE_RADIUS * 2);
        lv_obj_set_size(s_eye_r, EYE_RADIUS * 2, EYE_RADIUS * 2);
        lv_anim_del(s_mouth, _mouth_anim_cb);
        lv_obj_set_height(s_mouth, MOUTH_H / 3);
        _stop_pupil_scan();
        lv_obj_set_style_bg_color(s_pupil_l, lv_color_hex(0x1a1a2e), LV_PART_MAIN);
        lv_obj_set_style_bg_color(s_pupil_r, lv_color_hex(0x1a1a2e), LV_PART_MAIN);
        lv_label_set_text(s_status, "Say 'Hi, ESP' or tap to talk");
        break;

    case WS_VG_STATE_LISTENING:
        /* Wide eyes, cyan pupils — alert, attentive */
        lv_obj_set_size(s_eye_l, EYE_RADIUS * 2 + 8, EYE_RADIUS * 2 + 8);
        lv_obj_set_size(s_eye_r, EYE_RADIUS * 2 + 8, EYE_RADIUS * 2 + 8);
        lv_anim_del(s_mouth, _mouth_anim_cb);
        lv_obj_set_height(s_mouth, MOUTH_H / 4);
        _stop_pupil_scan();
        lv_obj_set_style_bg_color(s_pupil_l, lv_color_hex(0x00bcd4), LV_PART_MAIN);
        lv_obj_set_style_bg_color(s_pupil_r, lv_color_hex(0x00bcd4), LV_PART_MAIN);
        lv_label_set_text(s_status, "Listening...");
        break;

    case WS_VG_STATE_THINKING:
        /* Normal eyes, amber pupils, scanning side-to-side */
        lv_obj_set_size(s_eye_l, EYE_RADIUS * 2, EYE_RADIUS * 2);
        lv_obj_set_size(s_eye_r, EYE_RADIUS * 2, EYE_RADIUS * 2);
        lv_anim_del(s_mouth, _mouth_anim_cb);
        lv_obj_set_height(s_mouth, MOUTH_H / 6);
        lv_obj_set_style_bg_color(s_pupil_l, lv_color_hex(0xffa726), LV_PART_MAIN);
        lv_obj_set_style_bg_color(s_pupil_r, lv_color_hex(0xffa726), LV_PART_MAIN);
        _start_pupil_scan();
        lv_label_set_text(s_status, "Thinking...");
        break;

    case WS_VG_STATE_SPEAKING:
        /* Normal eyes, green pupils, animated mouth */
        lv_obj_set_size(s_eye_l, EYE_RADIUS * 2, EYE_RADIUS * 2);
        lv_obj_set_size(s_eye_r, EYE_RADIUS * 2, EYE_RADIUS * 2);
        _stop_pupil_scan();
        lv_obj_set_style_bg_color(s_pupil_l, lv_color_hex(0x66bb6a), LV_PART_MAIN);
        lv_obj_set_style_bg_color(s_pupil_r, lv_color_hex(0x66bb6a), LV_PART_MAIN);
        _start_mouth_anim();
        lv_label_set_text(s_status, "Speaking...");
        break;

    case WS_VG_STATE_DISCONNECTED:
        lv_obj_set_size(s_eye_l, EYE_RADIUS * 2, EYE_RADIUS * 2);
        lv_obj_set_size(s_eye_r, EYE_RADIUS * 2, EYE_RADIUS * 2);
        lv_anim_del(s_mouth, _mouth_anim_cb);
        lv_obj_set_height(s_mouth, MOUTH_H / 6);
        _stop_pupil_scan();
        lv_obj_set_style_bg_color(s_pupil_l, lv_color_hex(0xef5350), LV_PART_MAIN);
        lv_obj_set_style_bg_color(s_pupil_r, lv_color_hex(0xef5350), LV_PART_MAIN);
        lv_label_set_text(s_status, "Reconnecting...");
        break;

    default:
        break;
    }

    bsp_display_unlock();
}

void ui_face_set_agent(const char *name)
{
    if (!s_agent || !name) return;
    bsp_display_lock(0);
    lv_label_set_text(s_agent, name);
    bsp_display_unlock();
    ESP_LOGI(TAG, "Agent label → %s", name);
}
