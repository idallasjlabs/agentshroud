#pragma once
/* Animated face for the BOX-3 320×240 display.
 *
 * Draws a minimal LVGL face using circles and arcs:
 *   IDLE       — neutral expression, eyes normal
 *   LISTENING  — wide eyes, subtle pulse animation
 *   THINKING   — eyes looking up/sideways, ellipsis dots
 *   SPEAKING   — mouth animated (open/close cycle)
 */

#include "ws_client.h"  /* for ws_vg_state_t */

/**
 * @brief Create the face widget on the active LVGL screen.
 *
 * Must be called inside a bsp_display_lock()/bsp_display_unlock() pair,
 * after the status labels are set up in ui_init().
 */
void ui_face_init(void);

/**
 * @brief Transition the face to reflect the given Voice Gateway state.
 *
 * Safe to call from any task; acquires the display lock internally.
 */
void ui_face_set_state(ws_vg_state_t state);
