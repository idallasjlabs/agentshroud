---
title: trivy_report.py
type: module
file_path: gateway/security/trivy_report.py
tags: [security, vulnerability-scanning, trivy, cve, container-security, sbom]
related: [[health_report.py]], [[wazuh_client.py]], [[falco_monitor.py]]
status: documented
---

# trivy_report.py

## Purpose
Integrates with the Trivy open-source vulnerability scanner by invoking the local `trivy` binary, parsing its JSON output, and producing structured vulnerability summaries for consumption by the health reporting pipeline.

## Threat Model
Defends against unpatched vulnerabilities in OS packages and application dependencies within the gateway container and the filesystem it monitors. Regular Trivy scans provide a continuous inventory of known CVEs (Common Vulnerabilities and Exposures), enabling prioritized patching before exploitation occurs.

## Responsibilities
- Execute Trivy as a local subprocess (filesystem, image, or repo scan)
- Handle timeout, binary-not-found, and JSON parse errors gracefully
- Parse raw Trivy JSON output into a normalized vulnerability summary
- Count vulnerabilities by severity (CRITICAL, HIGH, MEDIUM, LOW, UNKNOWN)
- Identify the top 20 CVEs by severity rank
- Track affected package names
- Persist timestamped scan reports to a log directory
- Generate a health-report-compatible summary dict

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `run_trivy_scan` | Function | Invokes the `trivy` binary as a subprocess; returns parsed results |
| `parse_trivy_output` | Function | Normalizes raw Trivy JSON into a structured summary dict |
| `save_report` | Function | Writes a JSON report to `DEFAULT_LOG_DIR` with a timestamp filename |
| `generate_summary` | Function | Produces a health-report-compatible summary dict from a parsed report |

## Function Details

### run_trivy_scan(target, scan_type, severity, timeout, trivy_bin)
**Purpose:** Builds and executes the Trivy command with JSON output format. Returns `{"error": "timeout"}` on timeout and `{"error": "binary_not_found"}` if the binary is missing. Trivy exit code 1 (vulnerabilities found) is treated as normal. Non-zero, non-1 exit codes are logged as warnings.
**Parameters:**
- `target` — scan target path or image name (default `/`)
- `scan_type` — `"fs"` | `"image"` | `"rootfs"` | `"repo"` (default `"fs"`)
- `severity` — comma-separated severity filter (default `"CRITICAL,HIGH,MEDIUM,LOW"`)
- `timeout` — command timeout in seconds (default 600)
- `trivy_bin` — path to trivy binary (default `"trivy"`)
**Returns:** Parsed results dict from `parse_trivy_output`, or an error dict

### parse_trivy_output(raw)
**Purpose:** Iterates over all `Results` entries in the Trivy JSON. Counts vulnerabilities by severity, collects affected package names, and builds a sorted top-20 CVE list by severity rank.
**Parameters:** `raw` — raw JSON dict from Trivy
**Returns:** `dict` with keys `scanner`, `timestamp`, `total_vulnerabilities`, `by_severity`, `top_cves`, `affected_packages`, `affected_package_count`, `error`

### save_report(report, log_dir)
**Purpose:** Creates the log directory if needed, writes the report as formatted JSON to a timestamped file (`trivy-YYYYMMDD-HHMMSS.json`), and returns the file path.
**Parameters:** `report` (dict), `log_dir` (Path, default `/var/log/security/trivy`)
**Returns:** `Path`

### generate_summary(report)
**Purpose:** Converts a parsed Trivy report into the standard health-report summary dict. Returns an error summary if the report contains an error. Status is `"critical"` if any CRITICAL findings exist, `"warning"` if only HIGH, otherwise `"clean"`.
**Parameters:** `report` — dict from `parse_trivy_output`
**Returns:** `dict` with keys `tool`, `status`, `findings`, `critical`, `high`, `medium`, `low`, `affected_packages`, `top_cves`, `timestamp`

## Configuration / Environment Variables
- `DEFAULT_LOG_DIR = /var/log/security/trivy` — report output directory; created automatically
- `trivy_bin` — Trivy binary location; defaults to `trivy` (must be on `PATH` or specified explicitly)
- No environment variables; all configuration passed as function arguments

## Severity Order (for ranking)

`CRITICAL > HIGH > MEDIUM > LOW > UNKNOWN`

## Related
- [[health_report.py]]
- [[wazuh_client.py]]
- [[falco_monitor.py]]
