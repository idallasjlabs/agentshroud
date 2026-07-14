/* Host-native stub: replaces iot_button.h for wakeword PTT state tests. */
#pragma once
#include "bsp/esp-bsp.h"

typedef void (*button_cb_t)(void *arg, void *data);
typedef int   button_event_t;

#define BUTTON_PRESS_DOWN  0
#define BUTTON_PRESS_UP    1

static inline int
iot_button_register_cb(button_handle_t btn, button_event_t event,
                       void *cfg, button_cb_t cb, void *arg)
{
    (void)btn; (void)event; (void)cfg; (void)cb; (void)arg;
    return 0;
}

static inline int iot_button_delete(button_handle_t btn)
{
    (void)btn;
    return 0;
}
