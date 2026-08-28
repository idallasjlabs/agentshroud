---
type: community
cohesion: 0.08
members: 38
---

# Community 179

**Cohesion:** 0.08 - loosely connected
**Members:** 38 nodes

## Members
- [[A HERMES_MAIN_MODEL naming the anchor model directly (not via the     'qwen3-14b]] - rationale - gateway/tests/test_hermes_model_resolver.py
- [[An unrecognized mode value is treated conservatively as cloud.]] - rationale - gateway/tests/test_hermes_model_resolver.py
- [[Mode comparison tolerates case and surrounding whitespace from env files.]] - rationale - gateway/tests/test_hermes_model_resolver.py
- [[No arg → emit the model (start.sh convenience).]] - rationale - gateway/tests/test_hermes_model_resolver.py
- [[Resolve (model, provider) for Hermes from the container environment.      Preced]] - rationale - docker/bots/hermes/resolve_model.py
- [[_apply_stale_alias_correction()]] - code - docker/bots/hermes/resolve_model.py
- [[_load_resolver()]] - code - gateway/tests/test_hermes_model_resolver.py
- [[cloud mode with a Claude HERMES_MAIN_MODEL → that model + anthropic provider.]] - rationale - gateway/tests/test_hermes_model_resolver.py
- [[cloud mode with an OpenAI HERMES_MAIN_MODEL → openai provider.]] - rationale - gateway/tests/test_hermes_model_resolver.py
- [[cloud mode with everything unset → safe Anthropic default, never empty.]] - rationale - gateway/tests/test_hermes_model_resolver.py
- [[cloud mode, HERMES_MAIN_MODEL empty → use AGENTSHROUD_CLOUD_MODEL_REF.]] - rationale - gateway/tests/test_hermes_model_resolver.py
- [[local mode must not use a stale cloud HERMES_MAIN_MODEL.      Guards against the]] - rationale - gateway/tests/test_hermes_model_resolver.py
- [[local mode requested but neither HERMES_MAIN_MODEL nor local ref is local.]] - rationale - gateway/tests/test_hermes_model_resolver.py
- [[local mode with HERMES_MAIN_MODEL set → bare local model + ollama provider.]] - rationale - gateway/tests/test_hermes_model_resolver.py
- [[local mode, HERMES_MAIN_MODEL empty → use AGENTSHROUD_LOCAL_MODEL_REF.]] - rationale - gateway/tests/test_hermes_model_resolver.py
- [[local-multi mode LM Studio dash-style anchor model → ollama provider.]] - rationale - gateway/tests/test_hermes_model_resolver.py
- [[resolve_model()]] - code - docker/bots/hermes/resolve_model.py
- [[test_cli_default_key_is_model()]] - code - gateway/tests/test_hermes_model_resolver.py
- [[test_cli_emits_model_line()]] - code - gateway/tests/test_hermes_model_resolver.py
- [[test_cli_emits_provider_line()]] - code - gateway/tests/test_hermes_model_resolver.py
- [[test_cli_unknown_key_returns_nonzero()]] - code - gateway/tests/test_hermes_model_resolver.py
- [[test_cloud_mode_falls_back_to_cloud_ref_when_main_unset()]] - code - gateway/tests/test_hermes_model_resolver.py
- [[test_cloud_mode_no_refs_returns_safe_default()]] - code - gateway/tests/test_hermes_model_resolver.py
- [[test_cloud_mode_openai_model()]] - code - gateway/tests/test_hermes_model_resolver.py
- [[test_cloud_mode_uses_hermes_main_model_when_claude()]] - code - gateway/tests/test_hermes_model_resolver.py
- [[test_hermes_model_resolver.py]] - code - gateway/tests/test_hermes_model_resolver.py
- [[test_local_mode_empty_local_ref_falls_back_to_default_local_model()]] - code - gateway/tests/test_hermes_model_resolver.py
- [[test_local_mode_falls_back_to_local_ref_when_main_unset()]] - code - gateway/tests/test_hermes_model_resolver.py
- [[test_local_mode_ignores_stale_cloud_main_model()]] - code - gateway/tests/test_hermes_model_resolver.py
- [[test_local_mode_recognizes_nemotron_as_local()]] - code - gateway/tests/test_hermes_model_resolver.py
- [[test_local_mode_uses_hermes_main_model()]] - code - gateway/tests/test_hermes_model_resolver.py
- [[test_local_multi_mode_uses_lmstudio_dash_model()]] - code - gateway/tests/test_hermes_model_resolver.py
- [[test_mode_case_insensitive_and_whitespace_tolerant()]] - code - gateway/tests/test_hermes_model_resolver.py
- [[test_resolve_model_corrects_stale_alias_from_hermes_main_model()]] - code - gateway/tests/test_hermes_model_resolver.py
- [[test_resolve_model_corrects_stale_alias_from_local_model_ref()]] - code - gateway/tests/test_hermes_model_resolver.py
- [[test_stale_qwen3_rapid_alias_corrected_to_nemotron()]] - code - gateway/tests/test_hermes_model_resolver.py
- [[test_unknown_mode_treated_as_cloud()]] - code - gateway/tests/test_hermes_model_resolver.py
- [[test_unrelated_model_names_pass_through_uncorrected()]] - code - gateway/tests/test_hermes_model_resolver.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_179
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Community 852]]
- 1 edge to [[_COMMUNITY_Community 860]]

## Top bridge nodes
- [[test_hermes_model_resolver.py]] - degree 24, connects to 2 communities
- [[resolve_model()]] - degree 20, connects to 1 community
- [[_apply_stale_alias_correction()]] - degree 4, connects to 1 community