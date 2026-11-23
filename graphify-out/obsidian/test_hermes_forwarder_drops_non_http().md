---
source_file: "gateway/tests/test_telegram_executor.py"
type: "code"
community: "test_hermes_forwarder_drops_non_http"
location: "L45"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_hermes_forwarder_drops_non_http
---

# test_hermes_forwarder_drops_non_http()

## Connections
- [[Non-HTTP bytes (e.g. TLS ClientHello) must be dropped without proxying.]] - `rationale_for` [EXTRACTED]
- [[__init__()_24]] - `contains` [EXTRACTED]
- [[_fake_open_connection()]] - `contains` [EXTRACTED]
- [[_fake_reader_factory()]] - `contains` [EXTRACTED]
- [[asyncio_84]] - `references` [EXTRACTED]
- [[close()_4]] - `contains` [EXTRACTED]
- [[drain()]] - `contains` [EXTRACTED]
- [[get_extra_info()]] - `contains` [EXTRACTED]
- [[test_telegram_executor.py]] - `contains` [EXTRACTED]
- [[write()_2]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/test_hermes_forwarder_drops_non_http
