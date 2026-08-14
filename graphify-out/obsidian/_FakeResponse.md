---
source_file: "gateway/tests/test_soc_services_coverage.py"
type: "code"
community: "Security Docs"
location: "L33"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Security_Docs
---

# _FakeResponse

## Connections
- [[.__init__()_183]] - `method` [EXTRACTED]
- [[.read()_2]] - `method` [EXTRACTED]
- [[.test_200_returns_parsed_json()]] - `calls` [EXTRACTED]
- [[.test_404_returns_empty_dict()]] - `calls` [EXTRACTED]
- [[.test_500_returns_none()]] - `calls` [EXTRACTED]
- [[.test_exception_returns_empty()]] - `calls` [EXTRACTED]
- [[.test_exception_returns_none()]] - `calls` [EXTRACTED]
- [[.test_forward_file_download_aborts_at_size_limit()]] - `calls` [INFERRED]
- [[.test_non_200_returns_empty()]] - `calls` [EXTRACTED]
- [[.test_parses_multiplexed_frames()]] - `calls` [EXTRACTED]
- [[.test_tail_limit_applied()]] - `calls` [EXTRACTED]
- [[ServiceManager]] - `uses` [INFERRED]
- [[test_soc_services_coverage.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Security_Docs