---
name: GSD — Get Shit Done
about: Lightweight approval gate for production-impacting changes
title: "[GSD] "
labels: gsd
assignees: idallasj
---

## Problem

<!-- What is broken, missing, or needs to change? One sentence. -->

## Outcome

<!-- What does "done" look like? Measurable acceptance criteria. -->

## Effort

<!-- S / M / L — S = <2h, M = 2h–1d, L = >1d -->

## Blast Radius

<!-- Which systems are affected? Check all that apply. -->

- [ ] `gateway/security/**` — security modules (IEC 62443)
- [ ] `docker/` or `docker-compose.yml` — container stack
- [ ] `docker/setup-secrets.sh` — secret storage
- [ ] `docker/config/openclaw/apply-patches.js` — bot config injection
- [ ] `.claude/settings.json` or hooks — harness enforcement
- [ ] CI/CD workflows
- [ ] None of the above — low blast radius

## Approval Required By

<!-- Per GSD_CADENCE.md: production-visible, secret-handling, or schema
     changes require the `approved:isaiah` label before merge.
     Set to N/A if blast radius is "None of the above". -->
