---
type: community
cohesion: 0.12
members: 16
---

# TestMultipartOutboundPipeline

**Cohesion:** 0.12 - loosely connected
**Members:** 16 nodes

## Members
- [[dot-test_fail_closed_replaces_caption_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_form_markdown_exfil_link_scrubbed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_form_owner_id_redaction_continues_to_pipeline_scan()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_form_unknown_tool_call_quarantined()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_json_caption_pipeline_block_replaces_caption()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_json_caption_sanitized_in_place()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_multipart_markdown_exfil_link_scrubbed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Fail-closed substitution must target the resolved text field.          Regressio]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Markdown exfil links are stripped from form bodies (parity with JSON).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Markdown exfil links are stripped from multipart captions (parity).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Owner-ID-redacted form text must still reach the pipeline scan.          Regress]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pipeline-blocked caption payloads must have the caption replaced.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pipeline-sanitized sendPhoto captions must replace the caption itself.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Regression tests for the JSONformmultipart scan unification.      Each test pi]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOutboundScanUnification]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Unknown raw tool-call JSON in form bodies is quarantined for audit.          Tig]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestMultipartOutboundPipeline
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_TelegramAPIProxy_7]]
- 7 edges to [[_COMMUNITY_ApprovalQueueConfig_5]]
- 2 edges to [[_COMMUNITY_test_collaborator_tracker.py]]
- 1 edge to [[_COMMUNITY_PIIConfig]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy_2]]
- 1 edge to [[_COMMUNITY_ToolResultSanitizer]]
- 1 edge to [[_COMMUNITY_TestMultipartOutboundPipeline]]
- 1 edge to [[_COMMUNITY_BlockingPipeline]]

## Top bridge nodes
- [[TestOutboundScanUnification]] - degree 13, connects to 4 communities
- [[dot-test_json_caption_pipeline_block_replaces_caption()]] - degree 5, connects to 3 communities
- [[dot-test_multipart_markdown_exfil_link_scrubbed()]] - degree 5, connects to 3 communities
- [[dot-test_fail_closed_replaces_caption_payload()]] - degree 4, connects to 2 communities
- [[dot-test_form_markdown_exfil_link_scrubbed()]] - degree 4, connects to 2 communities
