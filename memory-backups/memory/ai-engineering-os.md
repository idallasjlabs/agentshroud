# AI Engineering Operating System

Imported 2026-03-08 from Isaiah's files.

## Concept

A full lifecycle AI-augmented development system with specialized agents for each phase.

## Lifecycle Phases
1. Product Discovery → product-agent
2. Architecture Design → architecture-agent
3. Development → tdd-engineer
4. Testing → qa-agent
5. Security → security-reviewer
6. CI/CD → ci-agent
7. Deployment → release-agent
8. Operations → sre-agent
9. Continuous Improvement → kaizen-agent

## Agent Selection Rules

| Trigger | Agent Chain |
|---------|------------|
| Feature development | product-agent → architect-agent → tdd-engineer |
| Bug investigation | debugging-agent → qa-agent → security-agent |
| Production incidents | incident-commander → sre-agent → observability-agent |
| Releases | release-engineer → ci-agent → deploy-agent |
| Architecture changes | architect-agent → security-agent → performance-agent |
| Podcast pipeline | research-agent → script-writer → podcast-producer |

## Autonomous Workflows

### Feature Delivery
product-agent → architecture-agent → tdd-engineer → qa-agent → security-reviewer → ci-agent → release-engineer

### Production Incident
incident-commander → diagnostics-agent → sre-agent → observability-agent → postmortem-agent

### Self-Healing CI/CD
ci-agent detects failures → diagnostics-agent → fix-suggestion-agent → test-agent → re-run pipeline

### Continuous Improvement
kaizen-agent analyzes: incident reports, DORA metrics, deployment stats

## How This Maps to AgentShroud's Current Setup

Our current peer review loop (WORKFLOW.md) implements a subset of this:
- security-reviewer = security-reviewer agent
- testrunner = qa-agent
- fixer-critical = tdd-engineer
- blue-team-probes = security-agent (offensive)
- test-coverage = qa-agent (coverage mode)

The AI Engineering OS extends this to the full product lifecycle. As AgentShroud matures, we should implement more of these agent chains.

## Full Package Extracted

Extracted `ai_engineering_operating_system.tgz` to `workspace/ai_engineering_os/`.

Contents:
- **55 agent definitions** in `agents/` (scaffolded — roles defined, responsibilities are placeholder)
- **16 skills** in `skills/` (scaffolded — titles defined, descriptions are placeholder)
- **Orchestrator** in `.claude/ORCHESTRATOR.md` (agent chaining rules)
- **Scripts** in `scripts/` (placeholder shells)
- **Pipeline dirs** for ci-cd, sre, podcast

## Current State

The AI Engineering OS is a **framework/scaffold**. The orchestrator and workflow files define the architecture clearly, but individual agent definitions and skills are placeholder stubs ("Execute specialized tasks within the AI engineering OS."). 

The AgentShroud repo's `.claude/skills/` directory has **37 fully-fleshed-out skills** with detailed procedures. Those are the production versions. This OS provides the overarching framework that organizes them.

## Integration Plan

1. The AgentShroud `.claude/skills/` are the **detailed implementations**
2. The AI Engineering OS provides the **orchestration layer** — which agent chains to which
3. As we flesh out the agent stubs, they should reference the existing skills
4. The ORCHESTRATOR.md should be merged into AgentShroud's workflow

## Source Files
- ORCHESTRATOR-ai-engineering-os.md — agent collaboration rules
- WORKFLOW-ai-engineering-os.md — lifecycle overview  
- ai_engineering_operating_system.tgz — extracted to workspace/ai_engineering_os/
