---
type: community
members: 24
---

# Phase 1 — Raw Collection

**Members:** 24 nodes

## Members
- [[1. System Profiler (most comprehensive single source)_5]] - document - .github/agents/i-mac.agent.md
- [[10. Spotlight Catch-All_5]] - document - .github/agents/i-mac.agent.md
- [[2. Applications Folders (catch drag-and-drop installs)_5]] - document - .github/agents/i-mac.agent.md
- [[3. Homebrew (formulae + casks)_5]] - document - .github/agents/i-mac.agent.md
- [[4. Mac App Store (via `mas` CLI)_5]] - document - .github/agents/i-mac.agent.md
- [[5. Setapp Detection_5]] - document - .github/agents/i-mac.agent.md
- [[6. Package Receipts (direct .pkg installs)_5]] - document - .github/agents/i-mac.agent.md
- [[7. CLI Tools & Utilities (non-.app installs)_5]] - document - .github/agents/i-mac.agent.md
- [[8. Launch Agents & Daemons (background services)_5]] - document - .github/agents/i-mac.agent.md
- [[9. Browser Extensions (optional but useful)_5]] - document - .github/agents/i-mac.agent.md
- [[A. `mac_app_catalog.json` — Machine-readable manifest_5]] - document - .github/agents/i-mac.agent.md
- [[B. `mac_app_catalog.md` — Human-readable catalog_5]] - document - .github/agents/i-mac.agent.md
- [[Discovery Strategy_5]] - document - .github/agents/i-mac.agent.md
- [[Error Handling_15]] - document - .github/agents/i-mac.agent.md
- [[Future Extensions (for collaborative sharing)_5]] - document - .github/agents/i-mac.agent.md
- [[Mac App Discovery Skill_5]] - document - .github/agents/i-mac.agent.md
- [[Performance Notes_5]] - document - .github/agents/i-mac.agent.md
- [[Phase 1 — Raw Collection_5]] - document - .github/agents/i-mac.agent.md
- [[Phase 2 — Deduplication & Normalization_5]] - document - .github/agents/i-mac.agent.md
- [[Phase 3 — Categorization_5]] - document - .github/agents/i-mac.agent.md
- [[Phase 4 — Enrichment_5]] - document - .github/agents/i-mac.agent.md
- [[Phase 5 — Output Generation_5]] - document - .github/agents/i-mac.agent.md
- [[When to Use This Skill_5]] - document - .github/agents/i-mac.agent.md
- [[i-mac.agent]] - document - .github/agents/i-mac.agent.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Phase_1__Raw_Collection
SORT file.name ASC
```
