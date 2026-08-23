---
type: community
cohesion: 0.12
members: 26
---

# Clamav Pipeline

**Cohesion:** 0.12 - loosely connected
**Members:** 26 nodes

## Members
- [[Build a minimal SecurityPipeline with passthrough PII + optional clamav.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[ClamAV scan_bytes returns error → fail-open CRITICAL log, FORWARD.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Clean base64 payload → FORWARD.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Malware-infected base64 payload → BLOCK with signature in block_reason.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[No clamav_scanner configured → step skipped, no error.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Short base64 (64 groups of 4) skips ClamAV scan.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Stream bytes to clamdscan for inline malware scanning.      Uses ``clamdscan --s]] - rationale - gateway/security/clamav_scanner.py
- [[Test replacement for asyncio.wait_for — awaits coroutine directly.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Test replacement for asyncio.wait_for — raises TimeoutError.      Closes the un-]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Wrap bytes in a long-enough base64 chunk to trigger the scan (= 64 groups of 4)]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[_b64_payload()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_instant_wait_for()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_make_pipeline()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_timeout_wait_for()]] - code - gateway/tests/test_clamav_pipeline.py
- [[scan_bytes()]] - code - gateway/security/clamav_scanner.py
- [[test_clamav_pipeline.py]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_pipeline_clamav_clean_payload()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_pipeline_clamav_error_fail_open()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_pipeline_clamav_malware_blocked()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_pipeline_clamav_not_configured()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_pipeline_short_base64_not_scanned()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_scan_bytes_binary_not_found()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_scan_bytes_clean()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_scan_bytes_empty_input()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_scan_bytes_infected()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_scan_bytes_timeout()]] - code - gateway/tests/test_clamav_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Clamav_Pipeline
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Slack Proxy Coverage]]
- 5 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 2 edges to [[_COMMUNITY_Security Toolchain]]
- 1 edge to [[_COMMUNITY_Tool Chain & CVE Triage]]

## Top bridge nodes
- [[scan_bytes()]] - degree 11, connects to 3 communities
- [[test_clamav_pipeline.py]] - degree 18, connects to 1 community
- [[_make_pipeline()]] - degree 8, connects to 1 community
- [[test_pipeline_clamav_clean_payload()]] - degree 5, connects to 1 community
- [[test_pipeline_clamav_error_fail_open()]] - degree 5, connects to 1 community