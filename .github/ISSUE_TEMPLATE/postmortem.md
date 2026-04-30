---
name: Postmortem
about: Document an incident, its root cause, and the test added to prevent recurrence
title: "[POSTMORTEM] "
labels: postmortem
assignees: idallasj
---

## Incident Summary

<!-- One sentence: what failed, when, and for how long? -->

## Timeline

<!-- UTC timestamps. Start from first symptom, end at full recovery. -->

| Time (UTC) | Event |
|-----------|-------|
| | First symptom observed |
| | Investigation started |
| | Root cause identified |
| | Fix applied |
| | Service fully recovered |

## Root Cause

<!-- Precise technical description. Not "human error" — what specific code,
     config, or process allowed this to happen? -->

## Contributing Factors

<!-- What made this worse or harder to detect? -->

-
-

## Remediation

<!-- What was done to restore service? Include commands run. -->

## Test Added to Prevent Recurrence (MANDATORY)

<!-- This field is required. Every postmortem must produce a test.
     Paste the test file path and the specific assertion added. -->

**Test file:** `<!-- e.g. tests/startup_smoke/test_bot_boot_static.sh -->`

**Assertion added:**
```bash
# Paste the new check() or assert() call here
```

**Why this assertion catches the failure:**
<!-- Explain how this test would have caught the bug before it hit production. -->

## Follow-Up Actions

<!-- Optional: GSD issues opened, MEMORY.md updates, doc changes. -->

- [ ]
