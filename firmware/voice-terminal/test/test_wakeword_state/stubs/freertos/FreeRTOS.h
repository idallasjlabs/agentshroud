/* Host-native stub: replaces FreeRTOS/FreeRTOS.h for wakeword PTT state tests. */
#pragma once
#include <stdint.h>
#include <stdbool.h>

typedef uint32_t TickType_t;
typedef uint32_t UBaseType_t;

#define portTICK_PERIOD_MS  1u

/* Controlled tick counter — advanced by the test harness. */
extern volatile uint32_t g_test_tick_ms;
static inline TickType_t xTaskGetTickCount(void) { return g_test_tick_ms; }
