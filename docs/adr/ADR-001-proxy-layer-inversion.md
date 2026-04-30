---
tags: [adr]
status: accepted
date: 2026-04-13
---
# ADR-001: Proxy-layer inversion model

## Decision
AgentShroud wraps any existing agent runtime rather than replacing it.

## Rationale
Practical advantage over approaches that require stack switching.

## Alternatives rejected
- Fork agent runtimes directly
- Require agents to use AgentShroud SDK
