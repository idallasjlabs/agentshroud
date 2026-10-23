---
type: community
cohesion: 0.33
members: 6
---

# AgentShroud Dev Environment — Raspberry Pi 4 (8GB) Setup Checklist (5)

**Cohesion:** 0.33 - loosely connected
**Members:** 6 nodes

## Members
- [[SubagentMonitor._log_event]] - code - gateway/security/subagent_monitor.py
- [[SubagentMonitor.check_tool_usage]] - code - gateway/security/subagent_monitor.py
- [[SubagentMonitor.deregister]] - code - gateway/security/subagent_monitor.py
- [[SubagentMonitor.kill_agent]] - code - gateway/security/subagent_monitor.py
- [[SubagentMonitor.kill_all]] - code - gateway/security/subagent_monitor.py
- [[SubagentMonitor.register_spawn]] - code - gateway/security/subagent_monitor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_Dev_Environment__Raspberry_Pi_4_8GB_Setup_Checklist_5
SORT file.name ASC
```
