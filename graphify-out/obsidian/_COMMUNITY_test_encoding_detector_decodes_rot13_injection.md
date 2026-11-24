---
type: community
members: 4
---

# test_encoding_detector_decodes_rot13_injection

**Members:** 4 nodes

## Members
- [[Empty inbound text is handled without error.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[rot13 layer is surfaced when the decoded text reveals injection language.]] - rationale - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_encoding_detector_decodes_rot13_injection()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py
- [[test_encoding_detector_rot13_empty_text()]] - code - gateway/tests/test_ws_e_rt2_inbound_encoding.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_encoding_detector_decodes_rot13_injection
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_EncodingDetector]]
- 2 edges to [[_COMMUNITY_test_ws_e_rt2_inbound_encoding.py]]

## Top bridge nodes
- [[test_encoding_detector_decodes_rot13_injection()]] - degree 3, connects to 2 communities
- [[test_encoding_detector_rot13_empty_text()]] - degree 3, connects to 2 communities
