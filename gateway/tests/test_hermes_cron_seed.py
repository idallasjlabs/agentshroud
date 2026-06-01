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

# init-config.sh native cron jobs: 5 original + 3 added (stability, landscape, email)
_EXPECTED_SH_JOB_COUNT = 8
# jobs.yaml includes 2 extra jobs that are YAML-only (AI Security Standards Tracker,
# Agentic AI CVE Watch) plus the 8 from init-config.sh
_EXPECTED_YAML_JOB_COUNT = 10


def _parse_cron_names_from_sh() -> list[str]:
    text = INIT_CONFIG.read_text(encoding="utf-8")
    # Match lines like: --name "Some Job Name"
    return re.findall(r'--name\s+"([^"]+)"', text)


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
    assert len(names) == _EXPECTED_YAML_JOB_COUNT, (
        f"Expected {_EXPECTED_YAML_JOB_COUNT} jobs in jobs.yaml, got {len(names)}: {names}"
    )


def test_cron_stamp_is_v2():
    text = INIT_CONFIG.read_text(encoding="utf-8")
    assert ".hermes-cron-seeded-v2" in text, (
        "Cron stamp must be '.hermes-cron-seeded-v2' to trigger re-seed on existing deploys"
    )


def test_stability_report_job_present():
    sh_names = _parse_cron_names_from_sh()
    assert any("Stability" in n for n in sh_names), \
        "Weekly Stability Report job missing from init-config.sh"

    yaml_names = _parse_job_names_from_yaml()
    assert any("Stability" in n for n in yaml_names), \
        "Weekly Stability Report job missing from jobs.yaml"


def test_competitive_landscape_job_present():
    sh_names = _parse_cron_names_from_sh()
    assert any("Competitive Landscape" in n for n in sh_names), \
        "Competitive Landscape job missing from init-config.sh"

    yaml_names = _parse_job_names_from_yaml()
    assert any("Competitive Landscape" in n for n in yaml_names), \
        "Competitive Landscape job missing from jobs.yaml"


def test_competitive_email_job_present():
    sh_names = _parse_cron_names_from_sh()
    assert any("Competitive Intelligence Email" in n for n in sh_names), \
        "Competitive Intelligence Email job missing from init-config.sh"

    yaml_names = _parse_job_names_from_yaml()
    assert any("Competitive Intelligence Email" in n for n in yaml_names), \
        "Competitive Intelligence Email job missing from jobs.yaml"
