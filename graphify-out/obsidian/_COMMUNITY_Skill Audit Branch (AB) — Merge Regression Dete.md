---
type: community
cohesion: 0.17
members: 15
---

# Skill: Audit Branch (AB) — Merge Regression Dete

**Cohesion:** 0.17 - loosely connected
**Members:** 15 nodes

## Members
- [[Any_82]] - code - voice_gateway/tts.py
- [[Frequencies well below the Nyquist (≤3 kHz) must pass through with minimal     a]] - rationale - gateway/tests/test_voice_gateway.py
- [[Kaiser-windowed sinc anti-aliasing filter suppresses content above the output]] - rationale - gateway/tests/test_voice_gateway.py
- [[Resample raw S16LE mono PCM from src_rate Hz to dst_rate Hz.      For downsa]] - rationale - voice_gateway/tts.py
- [[Return text suitable for TTS synthesis on the ESP32 voice interface.      Two]] - rationale - voice_gateway/tts.py
- [[Split an agent reply into ordered sentence-sized TTS chunks.      Applies normal]] - rationale - voice_gateway/tts.py
- [[Synthesize text to raw S16LE PCM mono audio bytes at TARGET_SAMPLE_RATE.]] - rationale - voice_gateway/tts.py
- [[_get_pipeline()]] - code - voice_gateway/tts.py
- [[_resample_s16le_mono()]] - code - voice_gateway/tts.py
- [[normalize_for_speech()]] - code - voice_gateway/tts.py
- [[split_for_speech()]] - code - voice_gateway/tts.py
- [[synthesize()]] - code - voice_gateway/tts.py
- [[test_resample_antialias_attenuates_above_nyquist()]] - code - gateway/tests/test_voice_gateway.py
- [[test_resample_passband_preserved()]] - code - gateway/tests/test_voice_gateway.py
- [[tts.py]] - code - voice_gateway/tts.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Skill_Audit_Branch_AB__Merge_Regression_Dete
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_CollaboratorActivityTracker]]
- 1 edge to [[_COMMUNITY_auto_remediate_cves.py]]
- 1 edge to [[_COMMUNITY_TestWebSocketHandshakeAuth]]
- 1 edge to [[_COMMUNITY_test_a2a_policy.py]]

## Top bridge nodes
- [[tts.py]] - degree 7, connects to 2 communities
- [[normalize_for_speech()]] - degree 6, connects to 2 communities
- [[split_for_speech()]] - degree 5, connects to 2 communities
- [[_resample_s16le_mono()]] - degree 6, connects to 1 community
- [[test_resample_antialias_attenuates_above_nyquist()]] - degree 3, connects to 1 community