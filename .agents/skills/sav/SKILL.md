---
name: sav
description: "System Audit Vault. Analyzes a codebase and produces a complete Obsidian vault — a set of interconnected markdown notes forming a living, navigable knowledge base. Generates: Home, System Overview, Quick Reference, Architecture, Startup Sequence, Shutdown & Recovery, Data Flow, one note per source module, one note per config file, one note per environment variable, one note per dependency, one note per container, error catalog and troubleshooting matrix, runbooks (setup, restart, crash recovery), and comprehensive Mermaid diagrams. Use when creating a knowledge base for a codebase from scratch."
---

# System Audit Vault (Obsidian)

You are a senior systems architect and technical knowledge engineer. Your job is to analyze the codebase provided and produce a **complete Obsidian vault** — a set of interconnected markdown notes that collectively form a living, navigable knowledge base for this system.

The vault must be so complete that someone who has **never seen this code, never used this system, and has no prior context** can open it in Obsidian, browse the graph view, and fully understand, operate, and troubleshoot the system.

---

## OBSIDIAN VAULT RULES (Follow These Exactly)

### Linking
- Use `[[Note Name]]` for every reference to another note in the vault
- Use `[[Note Name#Section]]` to link to a specific heading within a note
- Use `[[Note Name^blockid]]` only when referencing a specific paragraph
- Use `![[Note Name]]` to embed content from another note (use sparingly for quick-reference cards)
- **Every note must link to at least 2–3 other notes** — no orphaned notes

### Tags
- Apply tags consistently across all notes
- Required tag taxonomy:
  - `#type/module` — source code files/modules
  - `#type/config` — configuration files
  - `#type/env-var` — environment variables
  - `#type/dependency` — external packages/services
  - `#type/container` — Docker/K8s containers
  - `#type/error` — error conditions
  - `#type/process` — startup/shutdown/runtime processes
  - `#type/index` — index/hub notes
  - `#status/critical` — things that will break the system if wrong
  - `#status/optional` — optional/non-breaking
  - `#status/unknown` — uncertain behavior, needs investigation

### YAML Frontmatter
Every note must begin with YAML properties:
```yaml
---
title: Note Title
type: module | config | env-var | dependency | container | error | process | index
tags: [#type/x, #status/x]
related: ["[[Note 1]]", "[[Note 2]]"]
file_path: /actual/path/to/file  # for code modules
status: active | deprecated | unknown
last_reviewed: YYYY-MM-DD
---
```

### Folder Structure
Output notes organized into these folders (use `📁 FolderName/NoteName.md` format):

```
📁 00 - START HERE/
   🏠 Home.md                  ← Master index, start here
   🗺️ System Overview.md
   ⚡ Quick Reference.md        ← Cheat sheet, embeds key sections

📁 01 - Architecture/
   📐 Architecture Overview.md
   🔄 Startup Sequence.md
   🔄 Shutdown & Recovery.md
   🌊 Data Flow.md

📁 02 - Modules/
   (one note per source file/module)

📁 03 - Configuration/
   (one note per config file)
   📋 All Environment Variables.md   ← Master env var index

📁 04 - Environment Variables/
   (one note per environment variable)

📁 05 - Dependencies/
   📦 All Dependencies.md            ← Master dependency index
   (one note per major dependency)

📁 06 - Containers & Services/
   (one note per container/service)

📁 07 - Errors & Troubleshooting/
   🚨 Error Index.md                 ← Master error catalog
   (one note per error type or error category)
   🔧 Troubleshooting Matrix.md

📁 08 - Runbooks/
   🚀 First Time Setup.md
   🔁 Restart Procedure.md
   💀 Crash Recovery.md
   🩺 Health Checks.md

📁 09 - Diagrams/
   🗺️ Full System Flowchart.md       ← Mermaid diagram
   🌐 Dependency Graph.md
   🔄 Startup Flow Diagram.md
```

---

## REQUIRED NOTES — PRODUCE EVERY ONE OF THESE

### `00 - START HERE/Home.md`
The master index. Must include:
- What this system does (2 sentences, plain English)
- Callout block: `> [!WARNING] System is currently DOWN — last known issue: [describe]`
- Links to every major section using `[[Note]]` format
- An embedded quick reference: `![[Quick Reference]]`
- Table of contents for the entire vault

---

### `00 - START HERE/System Overview.md`
- What this system does and why it exists
- Who depends on it
- What breaks downstream if it goes down
- Architecture summary in plain English
- Links to `[[Architecture Overview]]`, `[[Startup Sequence]]`, `[[Data Flow]]`

---

### `00 - START HERE/Quick Reference.md`
One-page cheat sheet:
- Start / stop / restart commands (code blocks)
- Log file locations
- Config file locations
- Health check commands
- Top 5 "I see X, do Y" emergency fixes with links to `[[Error Index]]`
- Key env vars table linking to `[[04 - Environment Variables/VAR_NAME]]`

---

### `01 - Architecture/Architecture Overview.md`
- System component map (Mermaid diagram — simplified, high level)
- Every major component with a `[[link]]` to its module note
- How components communicate (REST, queue, socket, shared memory, etc.)
- Data stores and where state lives
- Network topology (ports, hosts, internal vs external)

---

### `01 - Architecture/Startup Sequence.md`
Numbered, step-by-step startup from cold boot to fully operational:
- Each step is a callout block: `> [!NOTE] Step 3: Initialize database connection`
- Inside each step: what triggers it, which `[[Module]]` handles it, what it needs, what it produces
- Dependency arrows: "Step 4 cannot run until Step 2 and Step 3 complete"
- Link to each module note inline
- Failure callout: `> [!DANGER] If this step fails: symptom → see [[Error Note]]`

---

### `01 - Architecture/Shutdown & Recovery.md`
- Graceful shutdown sequence (numbered steps)
- What files/locks/PIDs to clean up
- Crash recovery procedure
- Data integrity checks post-recovery
- Links to `[[Crash Recovery]]` runbook

---

### `01 - Architecture/Data Flow.md`
- Where data enters the system
- Step-by-step transformation pipeline with `[[Module]]` links at each stage
- Where data is stored, cached, or queued
- What reads it back and when
- Deletion/expiration logic
- Mermaid flowchart of data movement

---

### `02 - Modules/[FileName].md` — ONE PER SOURCE FILE
For every source code file, produce a note with:

```yaml
---
title: filename.ext
type: module
file_path: /full/path/to/filename.ext
tags: [#type/module, #status/active]
related: ["[[depends-on-module]]", "[[used-by-module]]"]
---
```

Body must include:
- **Purpose**: What this module does (plain English, 2–4 sentences)
- **Responsibilities**: Bullet list of everything this file is responsible for
- **Imports / Depends On**: Table — `Module | Why it's needed | [[Link]]`
- **Exported by / Used By**: Table — `Module | How it uses this | [[Link]]`
- **Functions / Classes / Methods**: For each one:
  - Name (as a `##` heading)
  - What it does
  - Parameters table: `Name | Type | Required | Description`
  - Returns: type and meaning
  - Side effects: DB writes, API calls, state changes
  - Calls: `[[other modules]]` it invokes
  - Called by: what invokes it
  - Failure modes: what breaks and what error appears
- **Environment Variables Used**: inline links to `[[04 - Environment Variables/VAR_NAME]]`
- **Config Files Read**: inline links to `[[03 - Configuration/filename]]`
- **Known Issues / Unknowns**: callout block `> [!WARNING]`

---

### `03 - Configuration/[ConfigFile].md` — ONE PER CONFIG FILE
- What this file configures
- Full annotated breakdown of every key/section
- Which `[[Modules]]` read this file
- What happens if it's missing or malformed
- Example of a valid configuration (code block)
- Links to related `[[env-var]]` notes

---

### `04 - Environment Variables/[VAR_NAME].md` — ONE PER ENV VAR
```yaml
---
title: VAR_NAME
type: env-var
tags: [#type/env-var, #status/critical]  # or #status/optional
required: true | false
default: "value or none"
---
```

Body:
- **What it controls** (plain English)
- **Expected format**: `string | integer | boolean | URL | path | JSON`
- **Example value**: (code block)
- **Effect if missing**: exact behavior — crash? fallback? silent failure?
- **Effect if wrong format**: exact behavior
- **Used in**: table linking to every `[[Module]]` that reads it
- **Set in**: which `.env` file, docker-compose, K8s secret, etc.
- Callout: `> [!DANGER] Critical — system will not start without this` or `> [!TIP] Optional — has safe default`

---

### `05 - Dependencies/[PackageName].md` — ONE PER MAJOR DEPENDENCY
- What it is and what it does
- Version in use
- Installation command
- Where it's used (links to `[[Modules]]`)
- What breaks if it's missing or wrong version
- Known version conflicts or gotchas
- Official docs link

---

### `05 - Dependencies/All Dependencies.md`
Master index table:
`Package | Version | Type | Used For | Required By | Install Command | [[Link]]`

---

### `06 - Containers & Services/[ContainerName].md` — ONE PER CONTAINER/SERVICE
- Image name and version
- What this container does
- Port mappings
- Volume mounts (what's mounted, why)
- Environment variables it receives (links to `[[04 - Environment Variables/]]`)
- Depends on (other containers that must start first)
- Health check command
- Common failure modes
- How to inspect logs: exact command
- How to restart just this container: exact command

---

### `07 - Errors & Troubleshooting/Error Index.md`
Master table of all errors:
`Error Code/Message | Severity | Cause | Module | First Step | [[Detailed Note]]`

Organized by category:
- Startup Errors
- Runtime Errors
- Connection/Network Errors
- Auth/Permission Errors
- Data/Validation Errors
- Resource Exhaustion

---

### `07 - Errors & Troubleshooting/[ErrorName].md` — ONE PER ERROR CATEGORY
```yaml
---
title: "Error: Cannot connect to database"
type: error
tags: [#type/error, #status/critical]
severity: fatal | high | medium | low
---
```

Body:
- **Exact error message** (code block)
- **What it means** (plain English)
- **Root cause(s)**: numbered list
- **Which module throws it**: `[[Module]]`
- **Diagnostic steps**: numbered checklist with exact commands
- **Fix**: numbered steps with exact commands
- **Prevention**: what to do so this never happens again
- Links to related `[[env-var]]` and `[[module]]` notes

---

### `07 - Errors & Troubleshooting/Troubleshooting Matrix.md`
Callout-block format for each symptom:

```
> [!BUG] Symptom: Service starts then immediately exits
> **Likely causes**: Missing env var, port conflict, failed DB connection
> **Check first**: [[VAR_NAME]], [[Container]], [[Module]]
> **Diagnostic command**: `docker logs container_name --tail 50`
> **Most common fix**: See [[Error Note]]
```

Cover every symptom you can infer from the code.

---

### `08 - Runbooks/First Time Setup.md`
Numbered checklist. Every step has:
- What to do
- Exact command (code block)
- How to verify it worked
- What to do if it fails (link to error note)

---

### `08 - Runbooks/Restart Procedure.md`
- Safe restart (step by step, exact commands)
- When to use a rolling restart vs full restart
- What to verify after restart
- How long it should take — if it takes longer, something is wrong

---

### `08 - Runbooks/Crash Recovery.md`
- How to tell if the crash was clean or dirty
- Lock files, PID files, state files to check and clean
- Database integrity check commands
- Step-by-step recovery sequence
- How to verify recovery was successful

---

### `09 - Diagrams/Full System Flowchart.md`
A single, massive Mermaid diagram:
```mermaid
flowchart TD
    subgraph ENV["🔐 Environment Variables"]
        ...every env var as a node...
    end
    subgraph STARTUP["🚀 Startup Sequence"]
        ...numbered steps...
    end
    subgraph RUNTIME["⚙️ Runtime Modules"]
        ...every module...
    end
    subgraph EXTERNAL["🌐 External Services"]
        ...databases, APIs, queues...
    end
    subgraph ERRORS["🚨 Error Paths"]
        ...error conditions with dashed arrows...
    end
    subgraph SHUTDOWN["🛑 Shutdown"]
        ...shutdown sequence...
    end
```

Rules for the diagram:
- Every file = a node labeled with filename
- Every env var = a `[[double bracket]]` node
- Every external service = a `[(cylinder)]` or `>flag]` node
- Every container = a subgraph
- Startup edges labeled with step numbers: `-->|"3: reads config"|`
- Error edges as dashed: `-. "throws error" .->`
- Color code with `style NodeName fill:#color`
  - Green = healthy startup path
  - Red = error paths
  - Yellow = external dependencies
  - Blue = config/env

---

### `09 - Diagrams/Startup Flow Diagram.md`
Focused Mermaid diagram of startup only:
- Every step in order
- Which module handles it
- What it needs (env vars, other services)
- Success path vs failure path
- Exact error that appears on failure

---

## OUTPUT FORMAT

Output each note as a separate code block labeled with its full vault path:

````
📁 FILE: 00 - START HERE/Home.md
```markdown
[note content here]
```

📁 FILE: 02 - Modules/server.js.md
```markdown
[note content here]
```
````

Output all notes in folder order. Do not skip any file. If you are uncertain about something in the code, create the note anyway and add:
```
> [!WARNING] UNCERTAIN
> This section is based on inference. Verify against actual runtime behavior.
```

---

## NOW ANALYZE THE FOLLOWING CODEBASE AND PRODUCE THE COMPLETE OBSIDIAN VAULT:

> Paste ALL of the following below this line:
> - All source code files (with file paths)
> - docker-compose.yml / Dockerfile(s)
> - .env.example or any sample env files
> - package.json / requirements.txt / Cargo.toml / go.mod (any dependency manifests)
> - Any config files (nginx.conf, supervisord.conf, etc.)
> - Startup scripts or Makefile
> - Any recent error logs (VERY IMPORTANT — paste them in full)
> - README if one exists (even if outdated)

[PASTE EVERYTHING HERE]
