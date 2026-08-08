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
    WS_VG_STATE_DISCONNECTED,
    WS_VG_STATE_UNKNOWN,
} ws_vg_state_t;

/** Callback types registered by the caller. */
typedef void (*ws_state_cb_t)(ws_vg_state_t state, void *user_ctx);
typedef void (*ws_pcm_cb_t)(const uint8_t *pcm, size_t len, void *user_ctx);
/** Server control frame {"cmd":"<name>","value":N|"str"} (e.g. spoken volume
 *  — numeric value, str_value NULL; spoken model/agent switch — str_value
 *  set, value 0). str_value points into a JSON parse buffer that is freed
 *  immediately after this callback returns — copy it if the callback needs
 *  it beyond the call. */
typedef void (*ws_ctrl_cb_t)(const char *cmd, int value, const char *str_value, void *user_ctx);

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
 * @brief Resume an interrupted utterance upload: sends "LISTEN <offset>".
 *
 * The server seeds its buffer from its cross-connection cache up to
 * <offset>; the device then sends only the remainder.  Turns a mid-upload
 * drop from a full resend into a seconds-long tail delivery.
 */
esp_err_t ws_client_send_listen_resume(ws_client_handle_t c, size_t offset);

/**
 * @brief Send the utterance-end marker ("END") to the Voice Gateway.
 */
esp_err_t ws_client_send_end(ws_client_handle_t c);

/**
 * @brief Send the TTS-abort marker ("STOP") to the Voice Gateway.
 *
 * Sent when the user taps during SPEAKING.  The gateway aborts the in-flight
 * TTS stream and returns the session to idle immediately; without it the
 * server keeps streaming the full reply (8-30 s) while the device discards
 * it, deaf to new utterances.
 */
esp_err_t ws_client_send_stop(ws_client_handle_t c);

/**
 * @brief Send a keepalive text frame to the Voice Gateway.
 *
 * Sends {"ping":1} to keep NAT and Tailscale relay state alive when no audio
 * is flowing.  Call every ~30 s from the voice_task idle path.
 * No-op if the connection is not currently open.
 */
esp_err_t ws_client_send_keepalive(ws_client_handle_t c);

/**
 * @brief Ship a diagnostic log line to the Voice Gateway as {"log":"..."}.
 *
 * Remote-diagnosis channel: with no USB serial available, key firmware
 * diagnostics are mirrored to the gateway, which prints them into its own
 * log ("[device <addr>] ...").  Best-effort: silently no-ops when the
 * connection is down; uses a short send timeout so it can never stall the
 * audio path.  Message is truncated and quote-stripped for JSON safety.
 */
esp_err_t ws_client_send_log(ws_client_handle_t c, const char *msg);

/**
 * @brief Register a handler for server control frames ({"cmd":...}).
 *
 * Optional; unregistered commands are ignored.  The callback runs in
 * websocket_task context — it must not block (same contract as state_cb).
 */
void ws_client_set_ctrl_cb(ws_client_handle_t c, ws_ctrl_cb_t cb);

/**
 * @brief Returns true if the WebSocket connection is currently open.
 */
bool ws_client_connected(ws_client_handle_t c);

/**
 * @brief Destroy the client and free all resources.
 */
void ws_client_destroy(ws_client_handle_t c);
