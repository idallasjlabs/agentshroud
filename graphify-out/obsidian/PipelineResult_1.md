---
source_file: "gateway/tests/test_telegram_pipeline.py"
type: "code"
community: "falco_monitor.py"
location: "L22"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/falco_monitorpy
---

# PipelineResult

## Connections
- [[PipelineAction]] - `uses` [INFERRED]
- [[PipelineResult]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[_make_pipeline_result()]] - `references` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/falco_monitorpy