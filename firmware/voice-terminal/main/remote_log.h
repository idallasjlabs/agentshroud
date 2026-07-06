#pragma once
/* Remote diagnostic log — mirrors key firmware diagnostics to the Voice
 * Gateway over the existing WebSocket as {"log":"..."} text frames.
 *
 * Why: when the device is deployed remotely (no USB serial), the gateway log
 * is the only observable trace.  Call vt_remote_log() alongside the ESP_LOG
 * at each diagnostic point; the gateway prints it as "[device <addr>] ...".
 *
 * Best-effort by design: silently drops when the WS is down or the ws-client
 * lock is contended (200 ms send timeout).  NEVER call from an ISR.
 */

void vt_remote_log(const char *fmt, ...) __attribute__((format(printf, 1, 2)));
