---
source_file: "firmware/voice-terminal/main/ota.c"
type: "code"
community: "ota_check"
location: "L76"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/ota_check
---

# ota_check()

## Connections
- [[_nvs_get_etag()]] - `calls` [EXTRACTED]
- [[_nvs_set_etag()]] - `calls` [EXTRACTED]
- [[_ws_to_https_base()]] - `calls` [EXTRACTED]
- [[app_main()_1]] - `calls` [INFERRED]
- [[esp_err_t]] - `references` [EXTRACTED]
- [[ota.c]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/ota_check
