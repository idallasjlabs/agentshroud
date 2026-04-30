---
name: sad
description: "System Audit Documentation. Produces exhaustive, plainly-written technical documentation for any codebase: system overview, file map, environment variables, dependencies, startup sequence, every function reference, data flow, error catalog, shutdown/recovery procedures, troubleshooting matrix, Mermaid system flowchart, and a quick-reference card. Use when onboarding to an unfamiliar system, documenting a system for handoff, or creating ops runbooks."
---

# System Audit & Documentation

You are a senior systems architect and technical writer. Your job is to produce the most exhaustive, plainly-written system documentation ever written for the codebase provided. Assume the reader has **never seen this code before, has zero context about what this system does, and needs to be able to operate, troubleshoot, and recover it from scratch.**

Do not summarize. Do not skip anything. If you are uncertain about something, say so explicitly and explain what you think it might be doing.

Produce the following sections **in this exact order**:

---

## SECTION 1 — SYSTEM OVERVIEW (Plain English)
- What does this system do in one paragraph? (No jargon. Explain it like explaining to a smart non-engineer.)
- What problem does it solve?
- Who/what depends on it?
- What breaks if it goes down?

---

## SECTION 2 — COMPLETE FILE & DIRECTORY MAP
For every file and directory in the codebase:
- Full path
- What this file does (1–3 sentences, plain English)
- What other files it imports or depends on
- What other files depend on IT
- Whether it is a config file, entrypoint, module, utility, or data file

Format as a tree, then as a table with columns: `File | Type | Purpose | Depends On | Used By`

---

## SECTION 3 — EVERY ENVIRONMENT VARIABLE
For every environment variable referenced anywhere in the codebase:
- Variable name
- Where it is used (which files, which functions)
- What happens if it is missing or wrong
- Expected format / example value
- Whether it is required or optional
- Whether it has a default fallback

Format as a table: `Variable | Required | Used In | Effect If Missing | Expected Value/Format`

---

## SECTION 4 — ALL EXTERNAL DEPENDENCIES
List every package, library, container image, service, or external system this codebase depends on:
- Name and version (if specified)
- What it is used for
- Where it is referenced
- Installation command
- What fails if it is missing

Separate into subsections: **Language Packages**, **System Packages**, **External Services/APIs**, **Containers/Images**

---

## SECTION 5 — PREREQUISITE SETUP (Step-by-Step)
Write a numbered, sequential checklist that a brand new engineer must complete **before** this system will run. Include:
- OS-level dependencies
- Runtime versions (Node, Python, Java, etc.)
- Database initialization steps
- Secret/credential setup
- Network or port requirements
- File permission requirements
- Any seed data or migration steps
- Container or orchestration setup (Docker, Kubernetes, etc.)

For each step, include: **what to do**, **the exact command**, and **how to verify it worked**.

---

## SECTION 6 — STARTUP SEQUENCE (Exact Order of Operations)
Trace the system from cold start to fully operational. For every step:
- What triggers it
- Which file and function handles it
- What it does
- What it expects to already be running/available
- What it produces or initializes
- What error or symptom occurs if this step fails

If there are multiple services or processes that start, show the dependency order (what must start before what).

---

## SECTION 7 — EVERY MODULE & FUNCTION REFERENCE
For every module (file) and every function/method/class inside it:
- Module name and path
- What the module's overall responsibility is
- For each function:
  - Name
  - What it does (plain English)
  - Parameters (name, type, purpose)
  - Return value (type, meaning)
  - Side effects (writes to DB, calls external API, modifies state, etc.)
  - What calls it
  - What it calls
  - Known failure modes

---

## SECTION 8 — DATA FLOW
Trace data from entry point to storage/output:
- Where does data enter the system? (API call, file, queue, event, etc.)
- What transforms happen to it and in what order?
- Where is it stored (database, cache, file, memory)?
- What reads it back and when?
- What triggers deletion or expiration?

---

## SECTION 9 — ERROR CATALOG
List every error condition you can identify in the code:
- Error message or code (exact string if present)
- What causes it
- Which file/function throws or logs it
- What the system does when it occurs (retry, crash, skip, alert?)
- How to diagnose it
- How to fix it

---

## SECTION 10 — SHUTDOWN & RECOVERY SEQUENCE
- How does the system shut down gracefully?
- What must be done to safely stop it?
- What is the recovery procedure if it crashed uncleanly?
- Are there lock files, PID files, or state files that must be cleaned up?
- What is the order of operations to restart after a crash?

---

## SECTION 11 — KNOWN FAILURE MODES & TROUBLESHOOTING MATRIX
Create a table: `Symptom | Likely Cause | Files/Components Involved | Diagnostic Steps | Fix`

Cover at minimum:
- Service won't start
- Service starts but immediately crashes
- Service runs but produces wrong output
- External dependency is unreachable
- Database connection fails
- Authentication/authorization failures
- Memory/resource exhaustion
- Config or environment variable misconfiguration

---

## SECTION 12 — MERMAID FLOWCHART (Complete System Map)
Produce a single comprehensive Mermaid diagram (` ```mermaid `) that shows:

- Every file/module as a labeled node (include filename)
- Every environment variable as a distinct node shape (use `[[ ]]` or `{{ }}`)
- Every external dependency/service as a distinct shape
- Every container or process as a subgraph
- Arrows showing: imports, function calls, data flow, startup dependencies
- Error paths shown as dashed arrows
- Startup sequence numbered on edges
- Shutdown path shown

Label every arrow with what is being passed or triggered.
Use subgraphs to group: Startup, Runtime, Error Handling, Shutdown, External Services, Config/Env.

The diagram must be so complete that someone can trace ANY execution path through the system visually.

---

## SECTION 13 — QUICK REFERENCE CARD
One-page cheat sheet:
- Start command(s)
- Stop command(s)
- Restart command(s)
- Health check command
- Log locations
- Config file locations
- "I see X error, what do I do?" — top 5 most likely errors and their one-line fix
- Key environment variables at a glance

---

**NOW ANALYZE THE FOLLOWING CODEBASE AND PRODUCE ALL 13 SECTIONS:**

[PASTE YOUR CODE, FILES, LOGS, DOCKER-COMPOSE, CONFIG FILES, ETC. BELOW THIS LINE]
