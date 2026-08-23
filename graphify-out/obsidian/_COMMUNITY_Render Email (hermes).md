---
type: community
cohesion: 0.24
members: 13
---

# Render Email (hermes)

**Cohesion:** 0.24 - loosely connected
**Members:** 13 nodes

## Members
- [[Apply inline Markdown spans to plain text (no recursive nesting).]] - rationale - docker/bots/hermes/render_md_email.py
- [[_esc()]] - code - docker/bots/hermes/render_md_email.py
- [[_inline()]] - code - docker/bots/hermes/render_md_email.py
- [[_render_table()]] - code - docker/bots/hermes/render_md_email.py
- [[_seed_cron()]] - code - docker/bots/hermes/init-config.sh
- [[_seed_cron() (idempotent native cron job seeding)]] - code - docker/bots/hermes/init-config.sh
- [[_write_soul()]] - code - docker/bots/hermes/init-config.sh
- [[_write_soul() (ownership-tolerant SOUL.md write)]] - code - docker/bots/hermes/init-config.sh
- [[init-config.sh]] - code - docker/bots/hermes/init-config.sh
- [[init-config.sh script]] - code - docker/bots/hermes/init-config.sh
- [[main()_4]] - code - docker/bots/hermes/render_md_email.py
- [[render()]] - code - docker/bots/hermes/render_md_email.py
- [[render_md_email.py]] - code - docker/bots/hermes/render_md_email.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Render_Email_hermes
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Container Runtime (smoke.d)]]

## Top bridge nodes
- [[init-config.sh]] - degree 7, connects to 1 community