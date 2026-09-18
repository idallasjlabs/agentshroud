---
source_file: ".llm_settings/scripts/llm-init.sh"
type: "code"
community: ".claude/settings.json (hook + permission wiring)"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/claude/settingsjson_hook__permission_wiring
---

# llm-init() (main deployment function)

## Connections
- [[_install_hint() (nested helper)]] - `defines` [EXTRACTED]
- [[_llm_init_convert_for_gemini()]] - `calls` [EXTRACTED]
- [[_llm_init_ensure_production_gate_marker()]] - `calls` [EXTRACTED]
- [[_llm_init_merge_claude_md()]] - `calls` [EXTRACTED]
- [[_llm_init_render_mcp()]] - `calls` [EXTRACTED]
- [[_llm_init_skill_allowed()]] - `calls` [EXTRACTED]
- [[llm-init.sh]] - `defines` [EXTRACTED]
- [[llm-init.sh script]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/claude/settingsjson_hook__permission_wiring