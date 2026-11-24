---
type: community
members: 11
---

# ManifestEntry

**Members:** 11 nodes

## Members
- [[dot-by_name()]] - code - gateway/skills/manifest.py
- [[dot-from_file()]] - code - gateway/skills/manifest.py
- [[dot-test_hash_changes_when_content_changes()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_hash_is_sha256_of_content()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-test_serialise_roundtrip()]] - code - gateway/tests/test_skills_manifest_sync.py
- [[dot-to_dict()_7]] - code - gateway/skills/manifest.py
- [[A single item in the skills manifest.]] - rationale - gateway/skills/manifest.py
- [[Build a ManifestEntry by reading path from disk.]] - rationale - gateway/skills/manifest.py
- [[ManifestEntry]] - code - gateway/skills/manifest.py
- [[TestManifestEntry]] - code - gateway/tests/test_skills_manifest_sync.py
- [[_sha256()]] - code - gateway/tests/test_skills_manifest_sync.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ManifestEntry
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_dot-from_source]]

## Top bridge nodes
- [[ManifestEntry]] - degree 7, connects to 1 community
- [[dot-from_file()]] - degree 7, connects to 1 community
- [[TestManifestEntry]] - degree 5, connects to 1 community
- [[_sha256()]] - degree 4, connects to 1 community
- [[dot-test_hash_is_sha256_of_content()]] - degree 4, connects to 1 community
