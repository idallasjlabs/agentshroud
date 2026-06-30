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
 * @brief Create the kawaii face widget on the active LVGL screen.
 *
 * Manages its own bsp_display_lock/unlock internally. Must NOT be called
 * while the caller holds the display lock (would deadlock on lvgl_port_lock).
 * Call after status labels are hidden via ui_update(UI_READY).
 */
void ui_face_init(void);

/**
 * @brief Transition the face to reflect the given Voice Gateway state.
 *
 * Safe to call from any task; acquires the display lock internally.
 */
void ui_face_set_state(ws_vg_state_t state);

/**
 * @brief Update the agent name label shown in the top-left corner of the face.
 *
 * @param name  Display name of the active agent (e.g. "Hermes", "Fast LLM").
 *              Must be a null-terminated string that remains valid until the
 *              next call (LVGL copies the text internally via lv_label_set_text).
 *
 * Safe to call from any task; acquires the display lock internally.
 */
void ui_face_set_agent(const char *name);
