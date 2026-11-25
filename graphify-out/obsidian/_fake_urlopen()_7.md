---
source_file: "gateway/tests/test_sync_cve_registry_ghsa.py"
type: "code"
community: ".test_fetch_paginates_via_link_cursor"
location: "L408"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/test_fetch_paginates_via_link_cursor
---

# _fake_urlopen()

## Connections
- [[dot-_page()]] - `calls` [EXTRACTED]
- [[dot-test_403_without_token_still_raises()]] - `indirect_call` [INFERRED]
- [[dot-test_fetch_paginates_via_link_cursor()]] - `indirect_call` [INFERRED]
- [[dot-test_other_http_errors_are_not_retried()]] - `indirect_call` [INFERRED]
- [[dot-test_persistent_failure_exits_non_zero()]] - `indirect_call` [INFERRED]
- [[dot-test_token_refused_retries_public_endpoint_without_token()]] - `indirect_call` [INFERRED]
- [[dot-test_transient_read_timeout_is_retried()]] - `indirect_call` [INFERRED]

#graphify/code #graphify/INFERRED #community/test_fetch_paginates_via_link_cursor
