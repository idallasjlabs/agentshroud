---
type: community
cohesion: 0.07
members: 30
---

# Community 267

**Cohesion:** 0.07 - loosely connected
**Members:** 30 nodes

## Members
- [[A garbage WHISPER_MODEL_SIZE env value does not break startup.]] - rationale - gateway/tests/test_voice_stt_model_ab.py
- [[A valid requested value overrides the default (the AB knob).]] - rationale - gateway/tests/test_voice_stt_model_ab.py
- [[An unknown model size does NOT crash — it falls back to the default.]] - rationale - gateway/tests/test_voice_stt_model_ab.py
- [[Duration is rounded for stable, log-friendly records.]] - rationale - gateway/tests/test_voice_stt_model_ab.py
- [[No requested value → the default is used (behaviour unchanged).]] - rationale - gateway/tests/test_voice_stt_model_ab.py
- [[Operator-friendly trims + lowercases before matching.]] - rationale - gateway/tests/test_voice_stt_model_ab.py
- [[Setting WHISPER_MODEL_SIZE=base.en flips the resolved model (AB).]] - rationale - gateway/tests/test_voice_stt_model_ab.py
- [[The AB measurement fires on the real transcribe path (model mocked).      Prove]] - rationale - gateway/tests/test_voice_stt_model_ab.py
- [[The documented AB knob values are all accepted.]] - rationale - gateway/tests/test_voice_stt_model_ab.py
- [[The fallback is visible to operators (WARNING, not silent).]] - rationale - gateway/tests/test_voice_stt_model_ab.py
- [[The helper returns a record tagged with model size + duration.]] - rationale - gateway/tests/test_voice_stt_model_ab.py
- [[The record is emitted through the module logger for AB comparison.]] - rationale - gateway/tests/test_voice_stt_model_ab.py
- [[With WHISPER_MODEL_SIZE unset, the resolved size stays small.en.]] - rationale - gateway/tests/test_voice_stt_model_ab.py
- [[Zero  unknown audio length → rtf is None (no divide-by-zero).]] - rationale - gateway/tests/test_voice_stt_model_ab.py
- [[test_module_model_size_defaults_to_small_en()]] - code - gateway/tests/test_voice_stt_model_ab.py
- [[test_module_model_size_env_override()]] - code - gateway/tests/test_voice_stt_model_ab.py
- [[test_module_model_size_invalid_env_falls_back()]] - code - gateway/tests/test_voice_stt_model_ab.py
- [[test_record_transcription_latency_handles_zero_audio()]] - code - gateway/tests/test_voice_stt_model_ab.py
- [[test_record_transcription_latency_logs_info()]] - code - gateway/tests/test_voice_stt_model_ab.py
- [[test_record_transcription_latency_returns_structured_record()]] - code - gateway/tests/test_voice_stt_model_ab.py
- [[test_record_transcription_latency_rounds_duration()]] - code - gateway/tests/test_voice_stt_model_ab.py
- [[test_select_model_size_default_when_unset()]] - code - gateway/tests/test_voice_stt_model_ab.py
- [[test_select_model_size_env_override_selects_configured_model()]] - code - gateway/tests/test_voice_stt_model_ab.py
- [[test_select_model_size_invalid_falls_back_to_default()]] - code - gateway/tests/test_voice_stt_model_ab.py
- [[test_select_model_size_invalid_logs_warning()]] - code - gateway/tests/test_voice_stt_model_ab.py
- [[test_select_model_size_is_case_and_whitespace_insensitive()]] - code - gateway/tests/test_voice_stt_model_ab.py
- [[test_transcribe_emits_latency_record()]] - code - gateway/tests/test_voice_stt_model_ab.py
- [[test_valid_model_sizes_contains_documented_ab_set()]] - code - gateway/tests/test_voice_stt_model_ab.py
- [[test_voice_stt_model_ab.py]] - code - gateway/tests/test_voice_stt_model_ab.py
- [[voice_gatewaystt.py]] - code - voice_gateway/stt.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_267
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Community 737]]

## Top bridge nodes
- [[test_voice_stt_model_ab.py]] - degree 16, connects to 1 community