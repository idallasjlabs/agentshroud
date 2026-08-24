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
# Per-job-type model routing (2026-08-23) — see the long comment above
# _seed_cron() in init-config.sh for the evidence: one-shot testing on real
# job content showed the prior universal default (nemotron-3.5-lightning-rapid)
# consistently fails to complete a structured deliverable under realistic
# token budgets, while gemma-4-26b-a4b-it succeeds faithfully. Every
# content-generating job is pinned to gemma-4-26b-a4b-it EXCEPT
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


def test_content_generating_jobs_pinned_to_evidence_backed_model():
    calls = _parse_seed_cron_calls_from_sh()
    for name in _PINNED_JOB_NAMES:
        assert name in calls, f"{name} not found in init-config.sh"
        assert '"gemma-4-26b-a4b-it" "custom"' in calls[name], (
            f"{name} must be pinned to gemma-4-26b-a4b-it/custom — see the "
            "evidence in the comment above _seed_cron() in init-config.sh. "
            "Provider is 'custom', not 'ollama': confirmed via `hermes doctor` "
            "2026-08-24 that 'ollama' was never a valid provider name in this "
            "Hermes version (0.20.1) -- every job using it was silently broken."
        )


def test_jira_weekly_review_not_pinned_to_a_model():
    """jira-weekly-review is pure script execution (near-zero free-form
    generation) — it must keep following cron.model/model.default rather
    than being pinned, since the model-quality evidence doesn't cover this
    job shape."""
    calls = _parse_seed_cron_calls_from_sh()
    assert "jira-weekly-review" in calls
    assert '"gemma-4-26b-a4b-it"' not in calls["jira-weekly-review"]


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
