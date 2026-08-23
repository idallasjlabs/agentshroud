---
type: community
cohesion: 0.07
members: 46
---

# Switch Model Idempotent

**Cohesion:** 0.07 - loosely connected
**Members:** 46 nodes

## Members
- [[--verify flag causes switch_model.sh to check both bots are healthy.]] - rationale - gateway/tests/test_switch_model_idempotent.py
- [[._run_and_read()_1]] - code - gateway/tests/test_switch_model_idempotent.py
- [[._run_and_read()]] - code - gateway/tests/test_switch_model_idempotent.py
- [[._run_twice()]] - code - gateway/tests/test_switch_model_idempotent.py
- [[.test_anthropic_sets_cloud_mode()]] - code - gateway/tests/test_switch_model_idempotent.py
- [[.test_cloud_anthropic_idempotent()]] - code - gateway/tests/test_switch_model_idempotent.py
- [[.test_cloud_switch_writes_hermes_main_model()]] - code - gateway/tests/test_switch_model_idempotent.py
- [[.test_local_anchor_idempotent()]] - code - gateway/tests/test_switch_model_idempotent.py
- [[.test_local_coder_idempotent()]] - code - gateway/tests/test_switch_model_idempotent.py
- [[.test_local_coder_sets_local_multi_mode()]] - code - gateway/tests/test_switch_model_idempotent.py
- [[.test_local_coder_switch_both_bots()]] - code - gateway/tests/test_switch_model_idempotent.py
- [[.test_local_default_idempotent()]] - code - gateway/tests/test_switch_model_idempotent.py
- [[.test_local_model_mode_is_local()]] - code - gateway/tests/test_switch_model_idempotent.py
- [[.test_local_multi_writes_anchor_coding_reasoning()]] - code - gateway/tests/test_switch_model_idempotent.py
- [[.test_local_sets_required_keys()]] - code - gateway/tests/test_switch_model_idempotent.py
- [[.test_local_switch_hermes_and_openclaw_models_match()]] - code - gateway/tests/test_switch_model_idempotent.py
- [[.test_local_switch_writes_hermes_main_model()]] - code - gateway/tests/test_switch_model_idempotent.py
- [[.test_local_with_explicit_model_idempotent()]] - code - gateway/tests/test_switch_model_idempotent.py
- [[.test_local_with_model_ref_sets_correct_model()]] - code - gateway/tests/test_switch_model_idempotent.py
- [[.test_verify_flag_accepted_without_error()]] - code - gateway/tests/test_switch_model_idempotent.py
- [[.test_verify_flag_with_model_ref()]] - code - gateway/tests/test_switch_model_idempotent.py
- [[After cloud switch, HERMES_MAIN_MODEL is written for Hermes too.]] - rationale - gateway/tests/test_switch_model_idempotent.py
- [[After local switch, HERMES_MAIN_MODEL is written to .env.]] - rationale - gateway/tests/test_switch_model_idempotent.py
- [[CompletedProcess_4]] - code - gateway/tests/test_switch_model_idempotent.py
- [[Expected keys are present in docker.env after a switch.]] - rationale - gateway/tests/test_switch_model_idempotent.py
- [[HERMES_MAIN_MODEL and OPENCLAW_MAIN_MODEL must reference the same model.]] - rationale - gateway/tests/test_switch_model_idempotent.py
- [[Parse a docker.env file into a dict.]] - rationale - gateway/tests/test_switch_model_idempotent.py
- [[Path_40]] - code - gateway/tests/test_switch_model_idempotent.py
- [[Returns (env_after_first_run, env_after_second_run).]] - rationale - gateway/tests/test_switch_model_idempotent.py
- [[Run switch_model.sh with mocked external commands.]] - rationale - gateway/tests/test_switch_model_idempotent.py
- [[TestSwitchModelBothBots]] - code - gateway/tests/test_switch_model_idempotent.py
- [[TestSwitchModelEnvKeys]] - code - gateway/tests/test_switch_model_idempotent.py
- [[TestSwitchModelIdempotent]] - code - gateway/tests/test_switch_model_idempotent.py
- [[TestSwitchModelVerifyFlag]] - code - gateway/tests/test_switch_model_idempotent.py
- [[_read_env()]] - code - gateway/tests/test_switch_model_idempotent.py
- [[_run_switch()]] - code - gateway/tests/test_switch_model_idempotent.py
- [[anthropic target second run leaves env identical.]] - rationale - gateway/tests/test_switch_model_idempotent.py
- [[local qwen314b second run leaves env identical.]] - rationale - gateway/tests/test_switch_model_idempotent.py
- [[local target second run leaves env identical.]] - rationale - gateway/tests/test_switch_model_idempotent.py
- [[local-coder switch writes matching HERMES_MAIN_MODEL.]] - rationale - gateway/tests/test_switch_model_idempotent.py
- [[local-coder target second run leaves env identical.]] - rationale - gateway/tests/test_switch_model_idempotent.py
- [[switch_model.sh local --verify exits 0 (mocked health checks).]] - rationale - gateway/tests/test_switch_model_idempotent.py
- [[switch_model.sh local m twice must leave docker.env unchanged on second run.]] - rationale - gateway/tests/test_switch_model_idempotent.py
- [[switch_model.sh local qwen314b --verify exits 0.]] - rationale - gateway/tests/test_switch_model_idempotent.py
- [[switch_model.sh must write model config for both OpenClaw and Hermes.]] - rationale - gateway/tests/test_switch_model_idempotent.py
- [[test_switch_model_idempotent.py]] - code - gateway/tests/test_switch_model_idempotent.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Switch_Model_Idempotent
SORT file.name ASC
```
