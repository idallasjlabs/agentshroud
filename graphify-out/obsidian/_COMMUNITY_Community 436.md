---
type: community
members: 22
---

# Community 436

**Members:** 22 nodes

## Members
- [[.test_multipart_fails_closed_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_multipart_markdown_exfil_link_scrubbed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_multipart_outbound_pipeline_called()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_multipart_overlength_caption_blocked_for_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_multipart_owner_exempt_from_fail_closed()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_multipart_pipeline_block_non_owner()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_multipart_sanitized_caption_applied_binary_intact()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_multipart_sanitizer_fallback_redacts_pii()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_multipart_text_field_scanned_when_no_caption()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[.test_multipart_without_text_part_passes_through()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[A multipart 'text' field (sendMessage via multipart) is scanned too.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Build a multipartform-data body with text fields and an optional binary part.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[If the pipeline crashes on a multipart body, non-owner captions are blocked.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Markdown exfil links are stripped from multipart captions (parity).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Multipart bodies with no captiontext part are forwarded unchanged.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Over-length multipart captions to non-owners are blocked like JSONform.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Owner multipart messages still pass through on pipeline crash (parity).]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Pipeline-blocked captions to non-owners are replaced with a safe notice.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Redacted caption replaces the original; binary part stays byte-identical.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[Without a pipeline, the sanitizer fallback still redacts caption PII.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py
- [[_make_multipart_body()]] - code - gateway/tests/test_telegram_proxy_outbound.py
- [[process_outbound must run on multipart caption text.]] - rationale - gateway/tests/test_telegram_proxy_outbound.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_436
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_Community 99]]
- 10 edges to [[_COMMUNITY_Community 626]]
- 10 edges to [[_COMMUNITY_Community 845]]
- 1 edge to [[_COMMUNITY_Community 1130]]

## Top bridge nodes
- [[.test_multipart_pipeline_block_non_owner()]] - degree 6, connects to 4 communities
- [[.test_multipart_outbound_pipeline_called()]] - degree 5, connects to 3 communities
- [[.test_multipart_sanitized_caption_applied_binary_intact()]] - degree 5, connects to 3 communities
- [[.test_multipart_fails_closed_for_non_owner()]] - degree 5, connects to 3 communities
- [[.test_multipart_owner_exempt_from_fail_closed()]] - degree 5, connects to 3 communities