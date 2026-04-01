## Summary

<!-- What changed and why? Link the related issue if applicable (e.g. Closes #123). -->

## Type of Change

- [ ] Bug fix (non-breaking change that resolves a defect)
- [ ] New feature (non-breaking change that adds capability)
- [ ] Breaking change (fix or feature that changes existing behavior)
- [ ] Documentation update
- [ ] Security module change (must include IEC 62443 FR reference below)

## IEC 62443 Reference

<!-- Required if "Security module change" is checked above. -->
<!-- Identify the Foundational Requirement(s) addressed or affected. -->
<!-- Example: FR3 — System Integrity (SL3): strengthens Cosign signature verification path. -->

FR(s) affected: <!-- e.g. FR2, FR3, FR4 -->
Impact: <!-- Strengthens / Neutral / Requires review -->

## Checklist

- [ ] Tests pass locally — `pytest -q`
- [ ] Test coverage is ≥ 94% — `pytest --cov=gateway --cov-report=term-missing`
- [ ] Version bumped in `gateway/__init__.py` (if this is a releasable change)
- [ ] `CHANGELOG.md` updated with a concise entry under the correct version heading
- [ ] No secrets or PII in diff — `git grep -i 'sk-ant-\|xoxb-\|password\|secret'`
- [ ] Semgrep passes — `pre-commit run semgrep`
- [ ] No new module stubs — every security module is fully wired in the pipeline
- [ ] Approval queue routing preserved for `email_sending`, `file_deletion`, `external_api_calls`, `skill_installation`
- [ ] PII redaction threshold not lowered (presidio confidence minimum remains 0.9)
- [ ] AgentShroud™ trademark notices intact (not removed or altered)
