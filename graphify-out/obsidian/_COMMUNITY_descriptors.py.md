---
type: community
members: 19
---

# descriptors.py

**Members:** 19 nodes

## Members
- [[A correctly signed manifest in a temp dir, wired in place of the committed one.]] - rationale - gateway/tests/test_edge_service_routes.py
- [[Any_72]] - code
- [[Canonical JSON sorted keys, no insignificant whitespace, UTF-8.]] - rationale - gateway/inbound_edge/descriptors.py
- [[DescriptorIntegrityError]] - code - gateway/inbound_edge/descriptors.py
- [[Ed25519PublicKey]] - code
- [[RuntimeError_1]] - code
- [[The served descriptors do not match the signed manifest. Refuse to start.]] - rationale - gateway/inbound_edge/descriptors.py
- [[Verify the manifest signature, then that ``descriptors`` match it exactly.…]] - rationale - gateway/inbound_edge/descriptors.py
- [[_load_public_key()]] - code - gateway/inbound_edge/descriptors.py
- [[build_manifest()]] - code - gateway/inbound_edge/descriptors.py
- [[canonical_bytes()]] - code - gateway/inbound_edge/descriptors.py
- [[descriptor_hash()]] - code - gateway/inbound_edge/descriptors.py
- [[descriptors.py]] - code - gateway/inbound_edge/descriptors.py
- [[fixture_120]] - code
- [[main()_32]] - code - gateway/inbound_edge/descriptors.py
- [[secrets_dir()_1]] - code - gateway/tests/test_edge_service_routes.py
- [[signed_descriptors()]] - code - gateway/tests/test_edge_service_routes.py
- [[test_unreadable_public_key_refuses()]] - code - gateway/tests/test_edge_service_routes.py
- [[verify_descriptors()]] - code - gateway/inbound_edge/descriptors.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/descriptorspy
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_test_edge_service_routes.py]]
- 7 edges to [[_COMMUNITY_test_edge_pipeline.py]]
- 2 edges to [[_COMMUNITY_TestManifest]]
- 1 edge to [[_COMMUNITY_test_edge_e2e_sdk.py]]
- 1 edge to [[_COMMUNITY_test_soc_edge.py]]
- 1 edge to [[_COMMUNITY_service.py]]
- 1 edge to [[_COMMUNITY_test_edge_fuzz.py]]

## Top bridge nodes
- [[descriptors.py]] - degree 16, connects to 6 communities
- [[canonical_bytes()]] - degree 12, connects to 2 communities
- [[secrets_dir()_1]] - degree 3, connects to 2 communities
- [[verify_descriptors()]] - degree 10, connects to 1 community
- [[DescriptorIntegrityError]] - degree 6, connects to 1 community
