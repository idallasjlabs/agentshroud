---
type: community
cohesion: 0.23
members: 17
---

# TestStartupScannerKeying

**Cohesion:** 0.23 - loosely connected
**Members:** 17 nodes

## Members
- [[._clean_report()]] - code - gateway/tests/test_security_toolchain.py
- [[._make_app_state()]] - code - gateway/tests/test_security_toolchain.py
- [[._make_store_result_fn()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_fs_compound_key_stored()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_history_accumulates_all_entries()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_image_key_summary_severity_computed()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_image_keys_do_not_overwrite_each_other()]] - code - gateway/tests/test_security_toolchain.py
- [[.test_legacy_trivy_key_present()]] - code - gateway/tests/test_security_toolchain.py
- [[Each _store_result call appends an entry to scanner_result_history.]] - rationale - gateway/tests/test_security_toolchain.py
- [[Per-image compound keys are independent — last image doesn't clobber first.]] - rationale - gateway/tests/test_security_toolchain.py
- [[Reproduce the _store_result closure from lifespan.py.]] - rationale - gateway/tests/test_security_toolchain.py
- [[Simulate the _store_result keying logic from lifespan._startup_scanner. The…]] - rationale - gateway/tests/test_security_toolchain.py
- [[Summary status is derived correctly for compound 'trivyimage...' keys.]] - rationale - gateway/tests/test_security_toolchain.py
- [[TestStartupScannerKeying]] - code - gateway/tests/test_security_toolchain.py
- [[_store_result()]] - code - gateway/tests/test_security_toolchain.py
- [[trivy' key is always stored for backward compat (SOC scanners endpoint).]] - rationale - gateway/tests/test_security_toolchain.py
- [[trivyfsapp' key is stored for per-target access.]] - rationale - gateway/tests/test_security_toolchain.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestStartupScannerKeying
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_test_security_toolchain.py]]

## Top bridge nodes
- [[TestStartupScannerKeying]] - degree 10, connects to 1 community