---
type: community
cohesion: 0.31
members: 9
---

# Turbo Fieldfare (MLX inference backend)

**Cohesion:** 0.31 - loosely connected
**Members:** 9 nodes

## Members
- [[MoE (Mixture-of-Experts) Streaming Inference]] - concept - docker/config/hermes/cron/prompts/newsletter-moe-streaming-ssd-offload.txt
- [[Newsletter Local Inference Engines]] - document - docker/config/hermes/cron/prompts/newsletter-local-inference-engines.txt
- [[Newsletter MoE Streaming  SSD Offload]] - document - docker/config/hermes/cron/prompts/newsletter-moe-streaming-ssd-offload.txt
- [[Today in AI (Daily Newsletter)]] - document - docker/config/hermes/cron/prompts/today-in-ai.txt
- [[Turbo Fieldfare (MLX inference backend)]] - concept - docker/config/hermes/cron/prompts/turbo-fieldfare-fix-watch.txt
- [[Turbo Fieldfare Fix Watch]] - document - docker/config/hermes/cron/prompts/turbo-fieldfare-fix-watch.txt
- [[Turbo Fieldfare GitHub Issue 84 (decoder_consume bug)]] - concept - docker/config/hermes/cron/prompts/turbo-fieldfare-fix-watch.txt
- [[oMLX (local model backend)]] - concept - docker/config/hermes/cron/prompts/omlx-moe-streaming-health-check.txt
- [[oMLX MoE Streaming Health Check]] - document - docker/config/hermes/cron/prompts/omlx-moe-streaming-health-check.txt

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Turbo_Fieldfare_MLX_inference_backend
SORT file.name ASC
```
