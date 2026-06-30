// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
#pragma once
#include "esp_err.h"

/**
 * Check the voice gateway for a firmware update.
 *
 * Derives the HTTPS base from ws_url (wss://host/path → https://host) then
 * HEAD-requests /firmware/bin?token=<token>.  If the ETag matches the value
 * persisted in NVS the firmware is current and this function returns.
 *
 * On an ETag mismatch the binary is streamed via GET into the inactive OTA
 * partition, the boot partition is switched, and the device restarts.  This
 * function does NOT return when an update is applied.
 *
 * Any network or HTTP error is logged at WARNING and the function returns
 * ESP_OK — a failed OTA check never blocks normal boot.
 */
esp_err_t ota_check(const char *ws_url, const char *token);
