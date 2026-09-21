# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Validate that init-config.sh cron jobs and jobs.yaml stay in sync.

Prevents accidental drift between the native hermes cron create invocations
(which write to Hermes' internal DB) and the YAML reference file (which is
seeded for documentation and backup purposes).
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml

REPO = Path(__file__).parent.parent.parent
INIT_CONFIG = REPO / "docker" / "bots" / "hermes" / "init-config.sh"
JOBS_YAML = REPO / "docker" / "config" / "hermes" / "cron" / "jobs.yaml"
CREDENTIAL_INJECTOR = REPO / "gateway" / "security" / "credential_injector.py"


def _injectable_providers() -> set[str]:
    """Provider names the gateway can actually inject a credential for.

    Derived from credential_injector.py rather than hardcoded, so adding an
    upstream there automatically permits it here and this test cannot drift
    out of step with the thing it is guarding.
    """
    text = CREDENTIAL_INJECTOR.read_text(encoding="utf-8")
    providers: set[str] = set()
    for domain in re.findall(r'domain="([^"]+)"', text):
        # api.anthropic.com -> anthropic, api.openai.com -> openai
        parts = [p for p in domain.split(".") if p not in ("api", "com", "ai", "*")]
        if parts:
            providers.add(parts[0])
    return providers


_INJECTABLE_PROVIDERS = _injectable_providers()

# init-config.sh native cron jobs: 5 original + 3 (stability, landscape, email)
# + 1 SCRUM-81 (jira-weekly-review)
_EXPECTED_SH_JOB_COUNT = 9
# jobs.yaml includes 2 extra jobs that are YAML-only (AI Security Standards Tracker,
# Agentic AI CVE Watch) plus the 9 from init-config.sh
_EXPECTED_YAML_JOB_COUNT = 11


def _parse_cron_names_from_sh() -> list[str]:
    text = INIT_CONFIG.read_text(encoding="utf-8")
    # Jobs are seeded via: _seed_cron "Job Name" "deliver" "schedule" "prompt"
    return re.findall(r'^_seed_cron\s+"([^"]+)"', text, re.MULTILINE)


def _parse_job_names_from_yaml() -> list[str]:
    data = yaml.safe_load(JOBS_YAML.read_text(encoding="utf-8"))
    return [job["name"] for job in data.get("jobs", [])]


def test_init_config_has_expected_cron_job_count():
    names = _parse_cron_names_from_sh()
    assert len(names) == _EXPECTED_SH_JOB_COUNT, (
        f"Expected {_EXPECTED_SH_JOB_COUNT} 'hermes cron create' jobs in init-config.sh, "
        f"got {len(names)}: {names}"
    )


def test_jobs_yaml_has_expected_job_count():
    names = _parse_job_names_from_yaml()
    assert (
        len(names) == _EXPECTED_YAML_JOB_COUNT
    ), f"Expected {_EXPECTED_YAML_JOB_COUNT} jobs in jobs.yaml, got {len(names)}: {names}"


def test_cron_seed_is_stampless_and_idempotent():
    """Stamp-file gating (v1/v2/v3) caused job triplication on every version bump.

    The seeder must instead delete any same-named job before creating it, and the
    old stamp mechanism must not return.
    """
    text = INIT_CONFIG.read_text(encoding="utf-8")
    assert "hermes-cron-seeded" not in text, (
        "Stamp-file gating must stay removed — it caused cron job triplication "
        "on every version bump (see PR #148)"
    )
    assert "_seed_cron" in text, "Idempotent _seed_cron helper missing from init-config.sh"
    assert "cron delete" in text, "_seed_cron must delete same-named jobs before re-creating"


def test_stability_report_job_present():
    sh_names = _parse_cron_names_from_sh()
    assert any(
        "Stability" in n for n in sh_names
    ), "Weekly Stability Report job missing from init-config.sh"

    yaml_names = _parse_job_names_from_yaml()
    assert any(
        "Stability" in n for n in yaml_names
    ), "Weekly Stability Report job missing from jobs.yaml"


def test_competitive_landscape_job_present():
    sh_names = _parse_cron_names_from_sh()
    assert any(
        "Competitive Landscape" in n for n in sh_names
    ), "Competitive Landscape job missing from init-config.sh"

    yaml_names = _parse_job_names_from_yaml()
    assert any(
        "Competitive Landscape" in n for n in yaml_names
    ), "Competitive Landscape job missing from jobs.yaml"


def test_competitive_email_job_present():
    sh_names = _parse_cron_names_from_sh()
    assert any(
        "Competitive Intelligence Email" in n for n in sh_names
    ), "Competitive Intelligence Email job missing from init-config.sh"

    yaml_names = _parse_job_names_from_yaml()
    assert any(
        "Competitive Intelligence Email" in n for n in yaml_names
    ), "Competitive Intelligence Email job missing from jobs.yaml"


def test_jira_weekly_review_job_present():
    """SCRUM-81: weekly Jira review cron must exist in both sh and yaml, Sun 09:00."""
    sh_names = _parse_cron_names_from_sh()
    assert any(
        "jira-weekly-review" in n for n in sh_names
    ), "jira-weekly-review job missing from init-config.sh"

    yaml_names = _parse_job_names_from_yaml()
    assert any(
        "jira-weekly-review" in n for n in yaml_names
    ), "jira-weekly-review job missing from jobs.yaml"


def test_jira_weekly_review_schedule_is_sunday_9am():
    """The schedule must be '0 9 * * 0' (Sunday 09:00) in both files."""
    sh_text = INIT_CONFIG.read_text(encoding="utf-8")
    assert (
        '"jira-weekly-review" "local" "0 9 * * 0"' in sh_text
    ), "jira-weekly-review must be seeded with schedule '0 9 * * 0' in init-config.sh"

    data = yaml.safe_load(JOBS_YAML.read_text(encoding="utf-8"))
    job = next(j for j in data["jobs"] if j["name"] == "jira-weekly-review")
    assert job["schedule"] == "0 9 * * 0", "jobs.yaml schedule must be Sunday 09:00"


# ---------------------------------------------------------------------------
# Per-job-type model routing (2026-08-23; serving history 2026-08-27) —
# see the long comment above _seed_cron() in init-config.sh for the full
# evidence trail: one-shot testing on real job content showed the prior
# universal default (nemotron-3.5-lightning-rapid) consistently fails to
# complete a structured deliverable under realistic token budgets, while
# the gemma-4-26b weights succeed faithfully. Serving history for those
# weights, all same-day 2026-08-27: briefly re-pointed to mlx_gemma
# (:8237) to escape Turbo Fieldflare's single-slot queueing, then
# REVERTED to Fieldflare (:8238, since reconfigured to 64K ctx) after
# mlx_gemma's 16GB resident footprint triggered a host-wide RAM pressure
# spiral and its default promotion was withdrawn on the local-llms side.
# mlx_gemma (or oMLX's own copy of the weights,
# "mlx-community--gemma-4-26b-a4b-it-4bit") remains the future re-point
# candidate but requires coordinated RAM budgeting first — do not re-point
# unilaterally; both alternate IDs stay registered in
# gateway/proxy/llm_proxy.py's LOCAL_MODEL_ROUTES ready for that switch.
# Every content-generating job is pinned to this model EXCEPT
# jira-weekly-review, whose payload is pure script execution with no
# meaningful free-form generation.
# ---------------------------------------------------------------------------

# Every _seed_cron call site except jira-weekly-review.
_PINNED_JOB_NAMES = [
    "AgentShroud Daily Check-in",
    "AgentShroud Weekly Summary",
    "Weekly Kaizen Review",
    "Monthly Chaos Engineering Drill",
    "Daily Memory Journal",
    "Weekly Hermes Stability Report",
    "Hermes Competitive Landscape Update (AM/PM)",
    "Hermes Competitive Intelligence Email (AM/PM)",
]


def _parse_seed_cron_calls_from_sh() -> dict[str, str]:
    """Map job name -> the full '_seed_cron "Name" ...' call text (all lines,
    since prompts continue across '\\' line continuations)."""
    text = INIT_CONFIG.read_text(encoding="utf-8")
    calls: dict[str, str] = {}
    for name in _parse_cron_names_from_sh():
        # Find the call starting at '_seed_cron "Name"' and capture through the
        # next blank line (call sites are separated by a blank line).
        start = text.index(f'_seed_cron "{name}"')
        end = text.find("\n\n", start)
        calls[name] = text[start : end if end != -1 else None]
    return calls


def test_content_generating_jobs_pinned_to_injectable_upstream():
    """These jobs must target an upstream the gateway can inject credentials for.

    Superseded the 2026-08-23 hard pin to gemma-4-26b-a4b-it/custom (#394) on
    2026-09-21. That pin resolved through the OpenRouter registry to
    https://openrouter.ai/api/v1, and gateway/security/credential_injector.py
    knows exactly two upstreams — api.anthropic.com (anthropic_oauth_token) and
    api.openai.com (openai_api_key). There is no openrouter.ai rule and no
    OpenRouter secret on the gateway, so every one of these jobs failed with
    "HTTP 401: Missing Authentication header" on every scheduled run.

    Nothing was bypassing the proxy: the request reached the gateway correctly,
    the gateway simply had no credential to inject for that upstream. So the
    invariant worth testing is not WHICH model is pinned — that is a tuning
    decision the model evidence can revise — but that whatever is pinned
    resolves to a provider the injector actually supports. A pin the gateway
    cannot authenticate is broken no matter how good the weights are.
    """
    calls = _parse_seed_cron_calls_from_sh()
    for name in _PINNED_JOB_NAMES:
        assert name in calls, f"{name} not found in init-config.sh"
        assert '"$_HERMES_CRON_MODEL" "$_HERMES_CRON_PROVIDER"' in calls[name], (
            f"{name} must use the shared $_HERMES_CRON_MODEL/"
            "$_HERMES_CRON_PROVIDER pair rather than a literal pin, so the "
            "model can be moved without editing every call site."
        )

    text = INIT_CONFIG.read_text(encoding="utf-8")
    provider_default = re.search(
        r'_HERMES_CRON_PROVIDER="\$\{HERMES_CRON_PROVIDER:-([^}"]+)\}"', text
    )
    assert provider_default, "_HERMES_CRON_PROVIDER default not found"
    assert provider_default.group(1) in _INJECTABLE_PROVIDERS, (
        f"default provider {provider_default.group(1)!r} has no rule in "
        "gateway/security/credential_injector.py — the gateway would have no "
        "credential to inject and every job would 401, which is exactly the "
        "2026-09-21 outage this test exists to prevent recurring."
    )


def test_jira_weekly_review_not_pinned_to_a_model():
    """jira-weekly-review is pure script execution (near-zero free-form
    generation) — it must keep following cron.model/model.default rather
    than being pinned, since the model-quality evidence doesn't cover this
    job shape."""
    calls = _parse_seed_cron_calls_from_sh()
    assert "jira-weekly-review" in calls
    assert '"gemma-4-26b-a4b-it' not in calls["jira-weekly-review"]
    assert '"mlx-community/gemma-4-26b-a4b-it-4bit"' not in calls["jira-weekly-review"]


def test_seed_cron_supports_optional_model_and_provider_args():
    """_seed_cron must accept optional $5 (model) / $6 (provider) and forward
    them as `hermes cron create --model ... --provider ...` only when set."""
    sh_text = INIT_CONFIG.read_text(encoding="utf-8")
    assert (
        '_model="${5:-}" _provider="${6:-}"' in sh_text
    ), "_seed_cron must accept optional 5th (model) / 6th (provider) positional args"
    assert (
        '--model "$_model"' in sh_text and '--provider "${_provider:-custom}"' in sh_text
    ), "_seed_cron must forward --model/--provider to `hermes cron create` when set"
