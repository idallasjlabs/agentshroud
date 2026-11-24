---
type: community
members: 20
---

# TestOutboundScanUnification

**Members:** 20 nodes

## Members
- [[dot-test_fail_closed_replaces_caption_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_form_markdown_exfil_link_scrubbed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_form_owner_id_redaction_continues_to_pipeline_scan()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_form_unknown_tool_call_quarantined()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_json_caption_pipeline_block_replaces_caption()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_json_caption_sanitized_in_place()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[dot-test_multipart_markdown_exfil_link_scrubbed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Fail-closed substitution must target the resolved text field. Regression the…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Markdown exfil links are stripped from form bodies (parity with JSON).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Markdown exfil links are stripped from multipart captions (parity).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Owner-ID-redacted form text must still reach the pipeline scan. Regression the…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pipeline-blocked caption payloads must have the caption replaced.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pipeline-sanitized sendPhoto captions must replace the caption itself.…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Regression tests for the JSONformmultipart scan unification. Each test pins a…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOutboundScanUnification]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Unknown raw tool-call JSON in form bodies is quarantined for audit. Tightening…]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[process_outbound()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[process_outbound()_1]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[process_outbound()_2]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[process_outbound()_3]] - code - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/TestOutboundScanUnification
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY__make_sanitizer]]
- 7 edges to [[_COMMUNITY_asyncio_5]]
- 1 edge to [[_COMMUNITY_lifespan.py]]
- 1 edge to [[_COMMUNITY_TelegramAPIProxy]]
- 1 edge to [[_COMMUNITY_BlockingPipeline]]
- 1 edge to [[_COMMUNITY__make_multipart_body]]

## Top bridge nodes
- [[dot-test_json_caption_pipeline_block_replaces_caption()]] - degree 6, connects to 3 communities
- [[dot-test_multipart_markdown_exfil_link_scrubbed()]] - degree 5, connects to 3 communities
- [[TestOutboundScanUnification]] - degree 10, connects to 2 communities
- [[dot-test_fail_closed_replaces_caption_payload()]] - degree 5, connects to 2 communities
- [[dot-test_form_owner_id_redaction_continues_to_pipeline_scan()]] - degree 5, connects to 2 communities
