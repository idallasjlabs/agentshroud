---
type: community
cohesion: 0.33
members: 6
---

# Subagent Monitor (security)

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
TABLE source_file, type FROM #community/Subagent_Monitor_security
SORT file.name ASC
```
