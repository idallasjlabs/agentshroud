
# AI Agent Orchestrator

This file defines how agents collaborate.

## Agent Selection Rules

Use the following logic:

- Feature development → product-agent → architect-agent → tdd-engineer
- UI/UX feature → ux-agent (/ux) → ui-agent (/ui) → tdd-engineer → qa-agent
- Bug investigation → debugging-agent → qa-agent → security-agent
- Production incidents → incident-commander → sre-agent → observability-agent
- Releases → release-engineer → ci-agent → deploy-agent
- Architecture changes → architect-agent → security-agent → performance-agent
- Podcast pipeline → research-agent → script-writer → podcast-producer
- Knowledge mapping → mm-agent (/mm) → atlas-agent (/atlas)

## Autonomous Workflows

### Feature Delivery

product-agent
→ architecture-agent
→ tdd-engineer
→ qa-agent
→ security-reviewer
→ ci-agent
→ release-engineer

### Feature Delivery (UI/UX)

ux-agent (/ux)       — information architecture, user flows, usability audit
→ ui-agent (/ui)     — component design, CSS architecture, responsive layout, accessibility
→ tdd-engineer       — component unit tests, interaction tests
→ qa-agent           — visual regression, keyboard navigation, screen reader check
→ security-reviewer  — XSS, CSRF, input validation review
→ ci-agent
→ release-engineer

### Production Incident

incident-commander
→ diagnostics-agent
→ sre-agent
→ observability-agent
→ postmortem-agent

### AI Podcast Generation

research-agent
→ outline-agent
→ script-agent
→ voice-generation-agent
→ podcast-publisher

## Self Healing CI/CD

ci-agent detects pipeline failures

then:

diagnostics-agent
→ fix-suggestion-agent
→ test-agent
→ re-run pipeline

## Continuous Improvement

kaizen-agent analyzes:

- incident reports
- DORA metrics
- deployment stats
