---
type: community
cohesion: 0.08
members: 35
---

# AuditStore

**Cohesion:** 0.08 - loosely connected
**Members:** 35 nodes

## Members
- [[.__init__()_140]] - code - gateway/security/audit_store.py
- [[.__init__()_39]] - code - gateway/security/audit_store.py
- [[._generate_event_id()]] - code - gateway/security/audit_store.py
- [[._get_latest_hash()]] - code - gateway/security/audit_store.py
- [[.close()_3]] - code - gateway/security/audit_store.py
- [[.compute_content_hash()]] - code - gateway/security/audit_store.py
- [[.compute_entry_hash()]] - code - gateway/security/audit_store.py
- [[.get_recent_entries()]] - code - gateway/security/audit_store.py
- [[.get_stats()_4]] - code - gateway/security/audit_store.py
- [[.initialize()]] - code - gateway/security/audit_store.py
- [[.log_event()_2]] - code - gateway/security/audit_store.py
- [[.query_events()]] - code - gateway/security/audit_store.py
- [[.to_dict()_11]] - code - gateway/security/audit_store.py
- [[.verify_hash_chain()]] - code - gateway/security/audit_store.py
- [[AuditEvent]] - code - gateway/security/audit_store.py
- [[AuditStore]] - code - gateway/security/audit_export.py
- [[AuditStore_1]] - code - gateway/security/audit_store.py
- [[Close the database connection.]] - rationale - gateway/security/audit_store.py
- [[Compute SHA-256 hash of event content (excluding hashes).]] - rationale - gateway/security/audit_store.py
- [[Compute entry hash including previous hash (chain).]] - rationale - gateway/security/audit_store.py
- [[Convert to dictionary representation.]] - rationale - gateway/security/audit_store.py
- [[Generate a unique event ID based on timestamp + random.]] - rationale - gateway/security/audit_store.py
- [[Get audit store statistics.]] - rationale - gateway/security/audit_store.py
- [[Get the entry_hash of the most recent event for chain continuation.]] - rationale - gateway/security/audit_store.py
- [[Log a new audit event with hash chain integrity.          Args             bot_]] - rationale - gateway/security/audit_store.py
- [[Open the database, create the schema, and run column migrations.          Initia]] - rationale - gateway/security/audit_store.py
- [[Path_1]] - code - gateway/security/audit_store.py
- [[Query audit events with optional filters.          Args             bot_id Whe]] - rationale - gateway/security/audit_store.py
- [[Represents a single audit event.      The ``bot_id`` field identifies which bot]] - rationale - gateway/security/audit_store.py
- [[Return the most recent audit entries (alias for query_events with limit).]] - rationale - gateway/security/audit_store.py
- [[SQLite-backed audit event store with tamper-evident hash chain.]] - rationale - gateway/security/audit_store.py
- [[TextIO]] - code - gateway/security/audit_export.py
- [[Verify the integrity of the hash chain.          Args             start_id Sta]] - rationale - gateway/security/audit_store.py
- [[audit_export.py]] - code - gateway/security/audit_export.py
- [[audit_store.py]] - code - gateway/security/audit_store.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AuditStore
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_AuditExporter]]
- 4 edges to [[_COMMUNITY_AuditExportConfig]]
- 4 edges to [[_COMMUNITY_ApprovalRequest]]
- 4 edges to [[_COMMUNITY_TestAuditStoreBotId]]
- 3 edges to [[_COMMUNITY_AuditEvent]]
- 3 edges to [[_COMMUNITY_TestAuditStore]]
- 2 edges to [[_COMMUNITY_lifespan.py]]
- 2 edges to [[_COMMUNITY_TrustManager]]
- 1 edge to [[_COMMUNITY_test_redteam_probes.py]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL]]
- 1 edge to [[_COMMUNITY_Restart Procedure]]
- 1 edge to [[_COMMUNITY_AgentShroud macOS App Icon (1024x1024, Rounded S]]
- 1 edge to [[_COMMUNITY_IEC 62443 Compliance Matrix — AgentShroud]]
- 1 edge to [[_COMMUNITY_archive_old_events()]]

## Top bridge nodes
- [[AuditStore_1]] - degree 36, connects to 9 communities
- [[AuditEvent]] - degree 25, connects to 5 communities
- [[audit_export.py]] - degree 7, connects to 4 communities
- [[audit_store.py]] - degree 6, connects to 3 communities
- [[AuditStore]] - degree 3, connects to 1 community