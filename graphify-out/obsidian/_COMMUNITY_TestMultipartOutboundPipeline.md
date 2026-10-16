---
type: community
cohesion: 0.06
members: 38
---

# TestMultipartOutboundPipeline

**Cohesion:** 0.06 - loosely connected
**Members:** 38 nodes

## Members
- [[dot-test_fail_closed_replaces_caption_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_form_markdown_exfil_link_scrubbed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_form_owner_id_redaction_continues_to_pipeline_scan()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_form_unknown_tool_call_quarantined()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_json_caption_pipeline_block_replaces_caption()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_json_caption_sanitized_in_place()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_multipart_fails_closed_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_multipart_markdown_exfil_link_scrubbed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_multipart_outbound_pipeline_called()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_multipart_overlength_caption_blocked_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_multipart_owner_exempt_from_fail_closed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_multipart_pipeline_block_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_multipart_sanitized_caption_applied_binary_intact()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_multipart_sanitizer_fallback_redacts_pii()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_multipart_text_field_scanned_when_no_caption()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_multipart_without_text_part_passes_through()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[A multipart 'text' field (sendMessage via multipart) is scanned too.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Build a multipartform-data body with text fields and an optional binary part.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Fail-closed substitution must target the resolved text field.          Regressio]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[If the pipeline crashes on a multipart body, non-owner captions are blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Markdown exfil links are stripped from form bodies (parity with JSON).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Markdown exfil links are stripped from multipart captions (parity).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Multipart bodies with no captiontext part are forwarded unchanged.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Multipart captions must get the full pipeline scan, not just the XML filter.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Over-length multipart captions to non-owners are blocked like JSONform.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Owner multipart messages still pass through on pipeline crash (parity).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Owner-ID-redacted form text must still reach the pipeline scan.          Regress]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pipeline-blocked caption payloads must have the caption replaced.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pipeline-blocked captions to non-owners are replaced with a safe notice.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pipeline-sanitized sendPhoto captions must replace the caption itself.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Redacted caption replaces the original; binary part stays byte-identical.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Regression tests for the JSONformmultipart scan unification.      Each test pi]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestMultipartOutboundPipeline]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOutboundScanUnification]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Unknown raw tool-call JSON in form bodies is quarantined for audit.          Tig]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Without a pipeline, the sanitizer fallback still redacts caption PII.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_make_multipart_body()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[process_outbound must run on multipart caption text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestMultipartOutboundPipeline
SORT file.name ASC
```

## Connections to other communities
- 32 edges to [[_COMMUNITY_TelegramAPIProxy]]
- 4 edges to [[_COMMUNITY_PIIConfig]]
- 3 edges to [[_COMMUNITY_test_telegram_proxy_outbound.py]]
- 2 edges to [[_COMMUNITY_TelegramAPIProxy_2]]
- 2 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 2 edges to [[_COMMUNITY_BlockingPipeline]]

## Top bridge nodes
- [[TestMultipartOutboundPipeline]] - degree 15, connects to 4 communities
- [[TestOutboundScanUnification]] - degree 13, connects to 4 communities
- [[dot-test_multipart_pipeline_block_non_owner()]] - degree 6, connects to 2 communities
- [[dot-test_json_caption_pipeline_block_replaces_caption()]] - degree 5, connects to 2 communities
- [[_make_multipart_body()]] - degree 12, connects to 1 community
