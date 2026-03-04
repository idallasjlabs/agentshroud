---
title: clamav_scanner.py
type: module
file_path: gateway/security/clamav_scanner.py
tags: [security, antivirus, clamav, malware-detection, file-scanning]
related: ["[[Security Modules/alert_dispatcher.py|alert_dispatcher.py]]", "[[Security Modules/drift_detector.py|drift_detector.py]]", "[[Data Flow]]"]
status: documented
---

# clamav_scanner.py

## Purpose
Integrates with the local ClamAV installation to scan files and directories for malware, parse scan output into structured results, and generate summaries compatible with the AgentShroud health report format.

## Threat Model
Malicious file upload or creation — an agent or external input introducing malware, ransomware, or otherwise malicious binaries into the container filesystem or agent-accessible directories before they can be executed or exfiltrated.

## Responsibilities
- Update the ClamAV virus signature database via `freshclam`
- Run `clamscan` against a target path (file or directory), with optional recursion and exclude patterns
- Parse raw `clamscan` stdout into a structured dict (infected files, signatures, scan counts, errors)
- Classify scan results as `clean` or `critical` (any infected file = critical)
- Save timestamped JSON reports to `/var/log/security/clamav/`
- Produce a normalized summary dict compatible with the gateway health report aggregator

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `update_virus_db()` | Function | Run `freshclam` to update virus signatures |
| `run_clamscan()` | Function | Execute `clamscan` and return parsed results |
| `parse_clamscan_output()` | Function | Parse raw stdout/returncode into structured dict |
| `save_report()` | Function | Write JSON report to timestamped file in log dir |
| `generate_summary()` | Function | Produce health-report-compatible summary dict |

## Function Details

### update_virus_db(freshclam_bin, timeout)
**Purpose:** Invoke `freshclam --no-warnings` to update the ClamAV database.
**Parameters:**
- `freshclam_bin` (str, default `"freshclam"`) — path to freshclam binary
- `timeout` (int, default 300) — subprocess timeout in seconds
**Returns:** dict with keys: `status` (`"ok"` / `"warning"` / `"error"`), `output` (first 1000 chars of stdout), `returncode`
**Side effects:** Network I/O to ClamAV mirror servers; modifies local virus DB files.

### run_clamscan(target, recursive, timeout, clamscan_bin, exclude_patterns)
**Purpose:** Run clamscan against a target path and return parsed results.
**Parameters:**
- `target` (str, default `"/home"`) — path to scan
- `recursive` (bool, default True) — scan directories recursively (`-r` flag)
- `timeout` (int, default 600) — subprocess timeout
- `clamscan_bin` (str, default `"clamscan"`) — path to clamscan binary
- `exclude_patterns` (list[str] | None) — regex patterns passed as `--exclude` arguments
**Returns:** Parsed results dict from `parse_clamscan_output()`
**Side effects:** Spawns subprocess; I/O intensive on large directories.

### parse_clamscan_output(output, returncode)
**Purpose:** Parse clamscan line-by-line output. Detects infected lines via the `FOUND` suffix regex, counts OK lines as scanned files, and counts ERROR/WARNING lines.
**Parameters:**
- `output` (str) — raw stdout from clamscan (with `--no-summary` flag)
- `returncode` (int) — process exit code (0 = clean, 1 = infected found)
**Returns:** dict with keys:
  - `scanner`: `"clamav"`
  - `timestamp`: ISO 8601 UTC
  - `scanned_files`: int
  - `infected_files`: list of `{file, signature}` dicts
  - `infected_count`: int
  - `errors`: int
  - `returncode`: int
  - `error`: None (or `"timeout"` / `"binary_not_found"` if set upstream)

### save_report(report, log_dir)
**Purpose:** Write the parsed report as a prettified JSON file. Filename format: `clamav-YYYYMMDD-HHMMSS.json`.
**Parameters:** `report` (dict), `log_dir` (Path, default `/var/log/security/clamav`)
**Returns:** Path to written file.
**Side effects:** Creates `log_dir` if absent; writes file.

### generate_summary(report)
**Purpose:** Translate a parsed ClamAV report into the normalized summary format used by the gateway health report aggregator.
**Returns:** dict with keys: `tool`, `status`, `findings`, `critical`, `high`, `medium`, `low`, `scanned_files`, `infected_files`, `signatures`, `timestamp`.
Severity mapping: all infected files are `critical`.

## Configuration

| Parameter | Default | Description |
|-----------|---------|-------------|
| Default log dir | `/var/log/security/clamav` | JSON report output directory |
| `clamscan_bin` | `"clamscan"` | Override with full path if not on $PATH |
| `freshclam_bin` | `"freshclam"` | Override with full path if not on $PATH |

## Mode: Enforce vs Monitor
No mode toggle in this module. `run_clamscan()` is always read-only (no `--remove` or `--move` flags are applied). Quarantine or deletion decisions are left to the caller.

## Environment Variables
None. Binary paths and log directory are passed as function parameters.

## Error Handling

| Condition | Returned |
|-----------|----------|
| `clamscan` binary not found | `{"error": "binary_not_found", "scanner": "clamav"}` |
| Subprocess timeout | `{"error": "timeout", "scanner": "clamav"}` |
| Log write failure | Logged via `logger.error`; no exception raised |

## Related
- [[Data Flow]]
- [[Security Modules/alert_dispatcher.py|alert_dispatcher.py]]
- [[Security Modules/drift_detector.py|drift_detector.py]]
