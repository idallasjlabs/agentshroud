# AgentShroud™ — OpenClaw Local-Model Tool-Use Instructions

<!-- Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved. -->
<!-- AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633) -->
<!-- Patent Pending — U.S. Provisional Application No. 64/018,744 -->

> **Purpose:** Local LLMs (Qwen3, qwen2.5-coder, deepseek-r1) do NOT reliably read
> tool-use rules in SOUL.md or system-prompt-only blocks. These instructions MUST live
> in AGENTS.md with concrete examples. Copy these rules verbatim into the system prompt
> for any local-model conversation that expects tool calling.

---

## Tool Invocation Format

You have access to tools. When you need to call a tool, you MUST use this EXACT format
with no deviation. Do NOT describe the action in prose — invoke the tool directly.

```json
{"tool": "TOOL_NAME", "args": {"arg1": "value1", "arg2": "value2"}}
```

- `tool`: the exact tool name (case-sensitive, underscore-separated)
- `args`: a JSON object with the required arguments

After calling a tool you will receive a result. Use the result to continue your response.

---

## Approved Tools and Their Arguments

### web_search
Search the web for current information.

```json
{"tool": "web_search", "args": {"query": "your search query here"}}
```

Example:
```json
{"tool": "web_search", "args": {"query": "AgentShroud latest security module updates 2026"}}
```

### file_read
Read the contents of a file.

```json
{"tool": "file_read", "args": {"path": "/path/to/file"}}
```

Example:
```json
{"tool": "file_read", "args": {"path": "/data/gateway/config.yaml"}}
```

### file_write
Write content to a file (requires approval for paths outside /tmp).

```json
{"tool": "file_write", "args": {"path": "/path/to/file", "content": "file content here"}}
```

Example:
```json
{"tool": "file_write", "args": {"path": "/tmp/report.md", "content": "# Report\n\nContent here."}}
```

### bash
Run a shell command (always requires approval).

```json
{"tool": "bash", "args": {"command": "your command here"}}
```

Example:
```json
{"tool": "bash", "args": {"command": "docker ps --format '{{.Names}}'"}}
```

### send_message
Send a Telegram message to the owner.

```json
{"tool": "send_message", "args": {"chat_id": "OWNER_CHAT_ID", "text": "message text"}}
```

Example:
```json
{"tool": "send_message", "args": {"chat_id": "8096968754", "text": "Task complete: daily report attached."}}
```

---

## Critical Rules for Local Models

1. **NEVER describe tool calls in prose.** Wrong: "I will search the web for X." Correct: invoke the tool directly with the JSON format above.

2. **NEVER invent tool names.** Only call tools from the approved list above. If you need a capability not listed, say so explicitly.

3. **ALWAYS include the full `args` object.** Missing arguments cause the tool to fail silently.

4. **ONE tool call per response turn.** Do not chain multiple tool invocations in one reply. Wait for the result, then decide on the next step.

5. **Tool results are injected automatically.** After your tool call, the result will appear in the next message. Do not fabricate results.

6. **Respect AgentShroud approval gates.** Actions tagged `[APPROVAL REQUIRED]` will pause until the owner approves. Do not retry automatically.

---

## Example: Multi-Step Tool Use

**User:** Find out what the latest AgentShroud version is and write a summary.

**Step 1 — search:**
```json
{"tool": "web_search", "args": {"query": "AgentShroud latest version changelog 2026"}}
```

*(result is injected)*

**Step 2 — write summary:**
```json
{"tool": "file_write", "args": {"path": "/tmp/agentshroud-summary.md", "content": "# AgentShroud Version Summary\n\nLatest version: v1.2.0 ...\n"}}
```

**Step 3 — confirm:**
Summary written to `/tmp/agentshroud-summary.md`.

---

## Failover Behaviour (Local Mode)

When running on a local model, the gateway may switch to a secondary model if the primary is unavailable (OOM or timeout). Your tool-use format must be identical regardless of which local model is active — these rules apply to all local backends:

- Qwen3 family (qwen3-14b, qwen3.8-27b-mlx, qwen3-coder-30b)
- qwen2.5-coder (qwen2.5-coder:32b)
- DeepSeek-R1 via mlx_lm (reasoning tasks — no tool calling on this backend)

If you are running on deepseek-r1, you do NOT have tool-calling capability. State explicitly when a task requires tools and you cannot perform it.
