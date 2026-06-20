#pragma once
/* WebSocket client for streaming PCM to and from the Voice Gateway.
 *
 * Bring-up strategy:
 *   Phase 1 — plain ws:// over the local WiFi network (no TLS, dev only).
 *             Set WS_CLIENT_URL to ws://<marvin-LAN-IP>:8765/voice
 *   Phase 2 — wss:// through MicroLink once it's verified.
 *             Set WS_CLIENT_URL to wss://marvin.tail240ea8.ts.net:8765/voice
 */

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>
#include "esp_err.h"

/* Voice Gateway WebSocket URL.  Override via sdkconfig:
 *   CONFIG_VT_VG_WS_URL in Kconfig.projbuild */
#ifndef CONFIG_VT_VG_WS_URL
#  define CONFIG_VT_VG_WS_URL "ws://192.168.0.1:8765/voice"
#endif

/** Opaque client state returned by ws_client_create(). */
typedef struct ws_client *ws_client_handle_t;

/** State event sent by the Voice Gateway as a JSON text frame. */
typedef enum {
    WS_VG_STATE_IDLE = 0,
    WS_VG_STATE_LISTENING,
    WS_VG_STATE_THINKING,
    WS_VG_STATE_SPEAKING,
    WS_VG_STATE_UNKNOWN,
} ws_vg_state_t;

/** Callback types registered by the caller. */
typedef void (*ws_state_cb_t)(ws_vg_state_t state, void *user_ctx);
typedef void (*ws_pcm_cb_t)(const uint8_t *pcm, size_t len, void *user_ctx);

/**
 * @brief Initialise the WebSocket client and connect to the Voice Gateway.
 *
 * @param url        Full WebSocket URL (ws:// or wss://).
 * @param state_cb   Called when a state-change JSON frame arrives.
 * @param pcm_cb     Called for each binary TTS PCM frame received.
 * @param user_ctx   Forwarded to callbacks unchanged.
 * @return Handle on success, NULL on failure.
 */
ws_client_handle_t ws_client_create(const char *url,
                                    ws_state_cb_t state_cb,
                                    ws_pcm_cb_t   pcm_cb,
                                    void         *user_ctx);

/**
 * @brief Send raw PCM mic data to the Voice Gateway.
 *
 * @param c    Client handle.
 * @param buf  S16LE PCM bytes.
 * @param len  Number of bytes to send.
 * @return ESP_OK on success.
 */
esp_err_t ws_client_send_pcm(ws_client_handle_t c, const uint8_t *buf, size_t len);

/**
 * @brief Send the utterance-start marker ("LISTEN") to the Voice Gateway.
 */
esp_err_t ws_client_send_listen(ws_client_handle_t c);

/**
 * @brief Send the utterance-end marker ("END") to the Voice Gateway.
 */
esp_err_t ws_client_send_end(ws_client_handle_t c);

/**
 * @brief Returns true if the WebSocket connection is currently open.
 */
bool ws_client_connected(ws_client_handle_t c);

/**
 * @brief Destroy the client and free all resources.
 */
void ws_client_destroy(ws_client_handle_t c);
