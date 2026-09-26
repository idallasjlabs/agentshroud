---
source_file: "gateway/tests/test_audit_export.py"
type: "rationale"
community: "load_config()"
location: "L347"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/load_config
---

# Opening a pre-migration DB (no bot_id column) should auto-migrate.

## Connections
- [[.test_migration_adds_bot_id_column()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/load_config