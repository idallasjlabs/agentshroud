---
type: community
members: 14
---

# Community 20

**Members:** 14 nodes

## Members
- [[.test_fail_closed_replaces_caption_payload()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_markdown_exfil_link_scrubbed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_owner_id_redaction_continues_to_pipeline_scan()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_form_unknown_tool_call_quarantined()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_json_caption_pipeline_block_replaces_caption()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_json_caption_sanitized_in_place()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Fail-closed substitution must target the resolved text field.          Regressio]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Markdown exfil links are stripped from form bodies (parity with JSON).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Owner-ID-redacted form text must still reach the pipeline scan.          Regress]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pipeline-blocked caption payloads must have the caption replaced.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pipeline-sanitized sendPhoto captions must replace the caption itself.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Regression tests for the JSONformmultipart scan unification.      Each test pi]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[TestOutboundScanUnification]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[Unknown raw tool-call JSON in form bodies is quarantined for audit.          Tig]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_20
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_Community 3]]
- 1 edge to [[_COMMUNITY_Community 1]]
- 1 edge to [[_COMMUNITY_Community 870]]
- 1 edge to [[_COMMUNITY_Community 4]]
- 1 edge to [[_COMMUNITY_Community 42]]
- 1 edge to [[_COMMUNITY_Community 874]]
- 1 edge to [[_COMMUNITY_Community 265]]
- 1 edge to [[_COMMUNITY_Community 346]]

## Top bridge nodes
- [[TestOutboundScanUnification]] - degree 13, connects to 6 communities
- [[.test_json_caption_pipeline_block_replaces_caption()]] - degree 5, connects to 2 communities
- [[.test_json_caption_sanitized_in_place()]] - degree 4, connects to 1 community
- [[.test_form_owner_id_redaction_continues_to_pipeline_scan()]] - degree 4, connects to 1 community
- [[.test_form_unknown_tool_call_quarantined()]] - degree 4, connects to 1 community