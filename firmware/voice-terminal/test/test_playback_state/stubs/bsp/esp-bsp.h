/* Host-native stub: replaces bsp/esp-bsp.h for wakeword PTT state tests.
 * Only the symbols referenced by wakeword.c's button-init path are provided;
 * the BSP display/audio/audio_preinit APIs are not needed for PTT state tests. */
#pragma once
#include <stdint.h>

typedef void *button_handle_t;
typedef int   esp_err_t;
#define ESP_OK    0
#define ESP_FAIL  (-1)

/* wakeword.c declares s_bsp_buttons[BSP_BUTTON_NUM] — must be a compile-time constant. */
#define BSP_BUTTON_NUM   4
#define BSP_BUTTON_MAIN  0
#define BSP_BUTTON_MUTE  1

static inline esp_err_t
bsp_iot_button_create(button_handle_t *handles, int *count, int num)
{
    for (int i = 0; i < num; i++) handles[i] = NULL;
    *count = 0;   /* all handles NULL → button-init path exits early */
    return ESP_OK;
}
