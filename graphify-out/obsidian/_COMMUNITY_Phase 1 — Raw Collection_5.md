---
type: community
members: 24
---

# Phase 1 — Raw Collection

**Members:** 24 nodes

## Members
- [[dot-ompagentsmac-app-discovery]] - document - .omp/agents/mac-app-discovery.md
- [[1. System Profiler (most comprehensive single source)_6]] - document - .omp/agents/mac-app-discovery.md
- [[10. Spotlight Catch-All_6]] - document - .omp/agents/mac-app-discovery.md
- [[2. Applications Folders (catch drag-and-drop installs)_6]] - document - .omp/agents/mac-app-discovery.md
- [[3. Homebrew (formulae + casks)_6]] - document - .omp/agents/mac-app-discovery.md
- [[4. Mac App Store (via `mas` CLI)_6]] - document - .omp/agents/mac-app-discovery.md
- [[5. Setapp Detection_6]] - document - .omp/agents/mac-app-discovery.md
- [[6. Package Receipts (direct .pkg installs)_6]] - document - .omp/agents/mac-app-discovery.md
- [[7. CLI Tools & Utilities (non-.app installs)_6]] - document - .omp/agents/mac-app-discovery.md
- [[8. Launch Agents & Daemons (background services)_6]] - document - .omp/agents/mac-app-discovery.md
- [[9. Browser Extensions (optional but useful)_6]] - document - .omp/agents/mac-app-discovery.md
- [[A. `mac_app_catalog.json` — Machine-readable manifest_6]] - document - .omp/agents/mac-app-discovery.md
- [[B. `mac_app_catalog.md` — Human-readable catalog_6]] - document - .omp/agents/mac-app-discovery.md
- [[Discovery Strategy_6]] - document - .omp/agents/mac-app-discovery.md
- [[Error Handling_16]] - document - .omp/agents/mac-app-discovery.md
- [[Future Extensions (for collaborative sharing)_6]] - document - .omp/agents/mac-app-discovery.md
- [[Mac App Discovery Skill_6]] - document - .omp/agents/mac-app-discovery.md
- [[Performance Notes_6]] - document - .omp/agents/mac-app-discovery.md
- [[Phase 1 — Raw Collection_6]] - document - .omp/agents/mac-app-discovery.md
- [[Phase 2 — Deduplication & Normalization_6]] - document - .omp/agents/mac-app-discovery.md
- [[Phase 3 — Categorization_6]] - document - .omp/agents/mac-app-discovery.md
- [[Phase 4 — Enrichment_6]] - document - .omp/agents/mac-app-discovery.md
- [[Phase 5 — Output Generation_6]] - document - .omp/agents/mac-app-discovery.md
- [[When to Use This Skill_6]] - document - .omp/agents/mac-app-discovery.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Phase_1__Raw_Collection
SORT file.name ASC
```
