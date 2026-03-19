---
title: health_report.py
type: module
file_path: gateway/security/health_report.py
tags: [security, health, scoring, reporting, sqlite, aggregation]
related: [[falco_monitor.py]], [[trivy_report.py]], [[wazuh_client.py]]
status: documented
---

# health_report.py

## Purpose
Aggregates security findings from all integrated tools (Trivy, ClamAV, Falco, Wazuh, gateway), calculates a weighted composite security score (0–100) with a letter grade, persists historical scores in SQLite, and generates both machine-readable and human-readable security health reports.

## Threat Model
Provides centralized visibility across the full security tool stack. Tracks posture trends to detect gradual degradation that might be missed by looking at individual point-in-time alerts. Serves as the single source of truth for the gateway's security grade.

## Responsibilities
- Calculate per-tool scores from severity counts using configurable deduction weights
- Compute a weighted composite score across all tool summaries
- Convert numeric scores to letter grades (A–F)
- Initialize and manage a SQLite database for historical score tracking
- Save each report snapshot to the history database
- Retrieve rolling trend data (configurable lookback, default 7 days)
- Generate a full structured report dict with recommendations
- Format the report as a human-readable string with emoji status indicators

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `calculate_tool_score` | Function | Scores a single tool (0–100) by deducting points per finding severity |
| `calculate_overall_score` | Function | Produces a weighted composite score across all tools |
| `score_to_grade` | Function | Maps a numeric score to a letter grade A–F |
| `init_db` | Function | Creates the SQLite `health_history` table if it does not exist |
| `save_to_history` | Function | Inserts a report snapshot (score, grade, full JSON) into the DB |
| `get_trend` | Function | Retrieves recent score/grade history rows from the DB |
| `generate_report` | Function | Orchestrates scoring, trend retrieval, recommendations, and optionally persists |
| `format_report` | Function | Renders a report dict as a human-readable multi-line string |
| `WEIGHTS` | Constant | Per-tool scoring weights (must sum to 1.0) |
| `SEVERITY_DEDUCTIONS` | Constant | Points deducted per finding at each severity level |
| `GRADE_THRESHOLDS` | Constant | Score thresholds for letter grades |

## Function Details

### calculate_tool_score(summary)
**Purpose:** Deducts points from 100 based on critical (−20), high (−10), medium (−3), and low (−1) finding counts; clamps result to [0, 100]. Returns 50.0 for error status (unknown).
**Parameters:** `summary` — tool summary dict with `critical`, `high`, `medium`, `low` keys
**Returns:** `float` in [0, 100]

### calculate_overall_score(summaries)
**Purpose:** Applies per-tool weights to produce a single composite score. Only includes tools present in the summaries dict; normalizes by actual total weight.
**Parameters:** `summaries` — `dict[tool_name, summary_dict]`
**Returns:** `float` in [0, 100]; returns 100.0 if no tools present

### score_to_grade(score)
**Purpose:** Maps the composite score to a letter grade using fixed thresholds (A≥90, B≥80, C≥70, D≥60, F<60).
**Parameters:** `score` — `float`
**Returns:** `str` — one of "A", "B", "C", "D", "F"

### init_db(db_path)
**Purpose:** Connects to the SQLite database and creates the `health_history` table (id, timestamp, score, grade, details JSON). Creates parent directories as needed.
**Parameters:** `db_path` — `Path`, defaults to `/var/log/security/health_history.db`
**Returns:** `sqlite3.Connection`

### save_to_history(score, grade, details, db_path)
**Purpose:** Inserts a timestamped health report snapshot into the history table; closes the connection in a `finally` block.
**Parameters:** `score`, `grade`, `details` (full report dict), `db_path`
**Returns:** `None`

### get_trend(days, db_path)
**Purpose:** Queries the last N days of history rows for score trending dashboards.
**Parameters:** `days` — int (default 7), `db_path`
**Returns:** `list[dict]` with keys `timestamp`, `score`, `grade`

### generate_report(summaries, db_path, save_history)
**Purpose:** Main entry point. Calculates overall score and grade, builds per-tool score breakdowns, fetches 7-day trend, generates recommendations for any critical/high findings, optionally persists to history.
**Parameters:** `summaries`, `db_path`, `save_history` (bool, default `True`)
**Returns:** Full report `dict` with `timestamp`, `overall_score`, `grade`, `tool_scores`, `trend`, `recommendations`, `total_findings`, `total_critical`, `total_high`

### format_report(report)
**Purpose:** Renders a report dict as a human-readable string including per-tool summary table with status icons, 7-day trend, and prioritized recommendations.
**Parameters:** `report` — dict from `generate_report()`
**Returns:** `str`

## Configuration / Environment Variables
- Database path: `DEFAULT_DB_PATH = /var/log/security/health_history.db`
- Scoring weights: `trivy=0.25`, `clamav=0.20`, `falco=0.25`, `wazuh=0.15`, `gateway=0.15`
- Severity deductions: `CRITICAL=20`, `HIGH=10`, `MEDIUM=3`, `LOW=1`

## Related
- [[falco_monitor.py]]
- [[trivy_report.py]]
- [[wazuh_client.py]]
