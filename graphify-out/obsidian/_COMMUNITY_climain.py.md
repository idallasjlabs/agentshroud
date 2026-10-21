---
type: community
members: 56
---

# cli/main.py

**Members:** 56 nodes

## Members
- [[Build a minimal SecurityPipeline with passthrough PII + optional clamav.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[ClamAV scan_bytes returns error → fail-open CRITICAL log, FORWARD.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Clean base64 payload → FORWARD.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Cosign signature verification of container images (fail-closed on missing binarytimeoutbad signature)]] - rationale - gateway/tests/test_image_verifier.py
- [[Malware-infected base64 payload → BLOCK with signature in block_reason.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[No clamav_scanner configured → step skipped, no error.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Short base64 (64 groups of 4) skips ClamAV scan.]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[Stream bytes to clamdscan for inline malware scanning. Uses ``clamdscan…]] - rationale - gateway/security/clamav_scanner.py
- [[Test replacement for asyncio.wait_for — awaits coroutine directly.]] - rationale - gateway/tests/test_image_verifier.py
- [[Test replacement for asyncio.wait_for — raises TimeoutError.      Closes the un-]] - rationale - gateway/tests/test_image_verifier.py
- [[Tests for ClamAV inline pipeline integration. Covers - scan_bytes() happy…]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[True if clamd accepts connections on its socket. Connects rather than testing…]] - rationale - gateway/security/clamav_scanner.py
- [[Verify an image signature using cosign keyless OIDC verification.      Args]] - rationale - gateway/security/image_verifier.py
- [[Verify multiple image signatures concurrently.      Returns         Dict mappin]] - rationale - gateway/security/image_verifier.py
- [[Wrap bytes in a long-enough base64 chunk to trigger the scan (= 64 groups of…]] - rationale - gateway/tests/test_clamav_pipeline.py
- [[_b64_payload()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_instant_wait_for()_1]] - code - gateway/tests/test_image_verifier.py
- [[_make_pipeline()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_passthrough()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_run_capture()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_timeout_wait_for()]] - code - gateway/tests/test_clamav_pipeline.py
- [[_timeout_wait_for()_1]] - code - gateway/tests/test_image_verifier.py
- [[clamd_available()]] - code - gateway/security/clamav_scanner.py
- [[clamdscan' when the resident clamd can take the scan, else 'clamscan'.]] - rationale - gateway/security/clamav_scanner.py
- [[fake_run()]] - code - gateway/tests/test_clamav_pipeline.py
- [[image_verifier.py]] - code - gateway/security/image_verifier.py
- [[preferred_scan_binary()]] - code - gateway/security/clamav_scanner.py
- [[scan_bytes()]] - code - gateway/security/clamav_scanner.py
- [[test_clamav_pipeline.py]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_clamd_available_false_for_stale_socket_left_by_killed_daemon()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_clamd_available_false_when_socket_missing()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_clamd_available_true_when_daemon_listening()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_clamd_socket_constant_matches_both_images_clamd_conf()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_cosign_fails_bad_signature()]] - code - gateway/tests/test_image_verifier.py
- [[test_cosign_not_found()]] - code - gateway/tests/test_image_verifier.py
- [[test_cosign_success()]] - code - gateway/tests/test_image_verifier.py
- [[test_cosign_timeout()]] - code - gateway/tests/test_image_verifier.py
- [[test_image_verifier.py]] - code - gateway/tests/test_image_verifier.py
- [[test_pipeline_clamav_clean_payload()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_pipeline_clamav_error_fail_open()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_pipeline_clamav_malware_blocked()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_pipeline_clamav_not_configured()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_pipeline_short_base64_not_scanned()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_preferred_scan_binary_falls_back_when_daemon_dead()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_preferred_scan_binary_uses_daemon_when_listening()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_run_clamscan_clamdscan_command_has_no_clamscan_only_flags()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_run_clamscan_clamscan_command_unchanged()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_scan_bytes_binary_not_found()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_scan_bytes_empty_input()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_scan_bytes_timeout()]] - code - gateway/tests/test_clamav_pipeline.py
- [[test_verify_images_exception_handled()]] - code - gateway/tests/test_image_verifier.py
- [[test_verify_images_mixed()]] - code - gateway/tests/test_image_verifier.py
- [[verify_image()]] - code - gateway/security/image_verifier.py
- [[verify_images()]] - code - gateway/security/image_verifier.py
- [[verify_images exception from one task is caught, others continue.]] - rationale - gateway/tests/test_image_verifier.py
- [[verify_images one succeeds, one fails → results keyed by ref.]] - rationale - gateway/tests/test_image_verifier.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/cli/mainpy
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_ApprovalQueueConfig (2) (2)]]
- 7 edges to [[_COMMUNITY_Common Queries]]
- 2 edges to [[_COMMUNITY_api.py (2)]]
- 2 edges to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_TrustConfig]]
- 1 edge to [[_COMMUNITY_create_auth_dependency]]
- 1 edge to [[_COMMUNITY_AgentTarget]]

## Top bridge nodes
- [[test_clamav_pipeline.py]] - degree 29, connects to 4 communities
- [[scan_bytes()]] - degree 11, connects to 3 communities
- [[preferred_scan_binary()]] - degree 7, connects to 3 communities
- [[clamd_available()]] - degree 6, connects to 1 community
- [[_run_capture()]] - degree 5, connects to 1 community
