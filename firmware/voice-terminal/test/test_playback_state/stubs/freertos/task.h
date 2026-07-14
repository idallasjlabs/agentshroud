/* Host-native stub: replaces freertos/task.h for wakeword PTT state tests. */
#pragma once
#include "FreeRTOS.h"

static inline void vTaskDelay(TickType_t ticks) { (void)ticks; }
