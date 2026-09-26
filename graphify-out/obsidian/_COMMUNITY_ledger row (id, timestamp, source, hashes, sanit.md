---
type: community
cohesion: 0.17
members: 12
---

# ledger row (id, timestamp, source, hashes, sanit

**Cohesion:** 0.17 - loosely connected
**Members:** 12 nodes

## Members
- [[Access OpenClaw Dashboard Remotely]] - document - docs/reference/TAILSCALE_COMMANDS.md
- [[Current Status_6]] - document - docs/reference/TAILSCALE_COMMANDS.md
- [[Next Steps_4]] - document - docs/reference/TAILSCALE_COMMANDS.md
- [[Option 1 OpenClaw Control UI on Port 18790]] - document - docs/reference/TAILSCALE_COMMANDS.md
- [[Option 2 Gateway Dashboard on Port 8080]] - document - docs/reference/TAILSCALE_COMMANDS.md
- [[Option 3 Both Services]] - document - docs/reference/TAILSCALE_COMMANDS.md
- [[Security Tailscale ACLs]] - document - docs/reference/TAILSCALE_COMMANDS.md
- [[Stop Tailscale Serve]] - document - docs/reference/TAILSCALE_COMMANDS.md
- [[TAILSCALE_COMMANDS]] - document - docs/reference/TAILSCALE_COMMANDS.md
- [[Tailscale Remote Access (Pi)]] - concept - docs/operations/raspberry-pi.md
- [[Tailscale Remote Access Setup]] - document - docs/reference/TAILSCALE_COMMANDS.md
- [[Verify Tailscale Serve Status]] - document - docs/reference/TAILSCALE_COMMANDS.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ledger_row_id_timestamp_source_hashes_sanit
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Mode A — Single task]]
- 1 edge to [[_COMMUNITY_.from_dict()]]
- 1 edge to [[_COMMUNITY_test_clamav_pipeline.py]]

## Top bridge nodes
- [[TAILSCALE_COMMANDS]] - degree 4, connects to 2 communities
- [[Tailscale Remote Access (Pi)]] - degree 2, connects to 1 community