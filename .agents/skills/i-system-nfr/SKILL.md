---
name: i-system-nfr
description: "Playbook for the i-system-nfr agent: end-to-end, load, stress, soak, spike, resilience, DR, fuzz, concurrency, compatibility, accessibility (WCAG 2.2 AA), i18n, upgrade, configuration and visual regression on a release candidate in staging. Replaces the system half of the deprecated i-qa."
---
<!-- GENERATED — edit agents-src/ (render with scripts/render-agents.sh). Do not hand-edit. -->

# Skill: System and non-functional testing (Pre-release)

The `i-system-nfr` agent is the persona; this skill is the playbook. Follow the steps in order and show evidence (command and output) for each.

## Steps
1. Confirm the target environment is staging and the blast radius is documented.
2. Run end-to-end journeys, then load, stress, soak and spike tests against stated targets (no target = finding).
3. Resilience and DR: failover drill with `/i-chaos-engineering`; prove backup-restore by restoring.
4. Fuzz, negative and concurrency tests; compatibility matrix; install and upgrade paths; configuration combinations.
5. Accessibility (WCAG 2.2 AA), i18n and visual-regression review.

Output: per-type result vs target, DR evidence, accessibility findings.

## Owned testing types

See the `i-system-nfr` agent for the ranked checklist.
