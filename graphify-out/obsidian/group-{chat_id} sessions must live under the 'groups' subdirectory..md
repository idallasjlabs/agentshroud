---
source_file: "gateway/tests/test_group_isolation.py"
type: "rationale"
community: "TestGroupMemoryNamespaceIsolation"
location: "L134"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/TestGroupMemoryNamespaceIsolation
---

# group-{chat_id} sessions must live under the 'groups' subdirectory.

## Connections
- [[.test_group_id_uses_group_prefix_namespace()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/TestGroupMemoryNamespaceIsolation