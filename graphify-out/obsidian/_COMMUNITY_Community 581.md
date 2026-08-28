---
type: community
cohesion: 0.13
members: 16
---

# Community 581

**Cohesion:** 0.13 - loosely connected
**Members:** 16 nodes

## Members
- [[.get_document_tag()]] - code - gateway/security/metadata_guard.py
- [[.guard()_1]] - code - gateway/tests/test_metadata_guard.py
- [[.tag_document()]] - code - gateway/security/metadata_guard.py
- [[.test_document_tag_creation()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_document_tag_lookup_by_hash()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_document_tag_untrusted_source()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_get_document_tag_unknown_hash_returns_none()]] - code - gateway/tests/test_metadata_guard.py
- [[.test_tag_document_different_content_different_hash()]] - code - gateway/tests/test_metadata_guard.py
- [[Create and store a provenance tag for a document.]] - rationale - gateway/security/metadata_guard.py
- [[DocumentTag]] - code - gateway/security/metadata_guard.py
- [[Look up a document tag by its SHA-256 content hash.]] - rationale - gateway/security/metadata_guard.py
- [[Numbered security control catalog (C8, C9, C18, C47, ...)]] - concept - gateway/tests/test_prompt_guard.py
- [[Provenance record for a document ingested into the agent context.]] - rationale - gateway/security/metadata_guard.py
- [[TestDocumentTagging]] - code - gateway/tests/test_metadata_guard.py
- [[metadata_guard.py]] - code - gateway/security/metadata_guard.py
- [[test_metadata_guard.py]] - code - gateway/tests/test_metadata_guard.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_581
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Security Audit & Drift Detection]]
- 2 edges to [[_COMMUNITY_Community 350]]
- 1 edge to [[_COMMUNITY_Community 30]]
- 1 edge to [[_COMMUNITY_Community 1132]]

## Top bridge nodes
- [[test_metadata_guard.py]] - degree 5, connects to 2 communities
- [[Numbered security control catalog (C8, C9, C18, C47, ...)]] - degree 3, connects to 2 communities
- [[TestDocumentTagging]] - degree 9, connects to 1 community
- [[DocumentTag]] - degree 7, connects to 1 community
- [[.get_document_tag()]] - degree 3, connects to 1 community