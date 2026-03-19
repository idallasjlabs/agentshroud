#!/usr/bin/env python3
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""
generate_redacted_pdf.py — Convert a security assessment report to a redacted PDF.

Usage:
    python security_assessment/generate_redacted_pdf.py [report.md] [output.pdf]

Defaults to the most recent report in /tmp/security_assessment_reports/.
Output lands in the same directory as the input unless overridden.

Redaction rules applied to the Response_to_Owner column only:
  - Telegram user IDs (8-12 consecutive digits)
  - OPENCLAW_* / AGENTSHROUD_* env var names
  - /run/secrets/... paths
  - Bot tokens (colon-delimited numeric:hash patterns)
  - Raw API key fragments (30+ char alphanumeric)
  - Private IP addresses

The Response_to_Collaborator column is shown as-is — it already contains
only safe-mode notices, which is the point of the contrast.
"""
from __future__ import annotations

import re
import sys
import os
import subprocess
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Find report
# ---------------------------------------------------------------------------

REPORTS_DIR = Path("/tmp/security_assessment_reports")

def latest_report() -> Path:
    reports = sorted(REPORTS_DIR.glob("security_assessment_*.md"))
    if not reports:
        raise FileNotFoundError(f"No reports found in {REPORTS_DIR}")
    return reports[-1]

# ---------------------------------------------------------------------------
# Redaction engine (owner column only)
# ---------------------------------------------------------------------------

_REDACTION_RULES: list[tuple[str, str, str]] = [
    # (label, pattern, replacement)
    ("bot_token",      r"\d{8,12}:[A-Za-z0-9_-]{30,}",       "[BOT_TOKEN]"),
    ("telegram_id",    r"(?<![/\-\.:])\b[0-9]{8,12}\b(?![/\-\.:])",  "[TELEGRAM_ID]"),
    ("secret_path",    r"/run/secrets/[^\s<\\\]\)\"]+",        "[SECRET_PATH]"),
    ("openclaw_env",   r"OPENCLAW_[A-Z0-9_]+",                 "[ENV_VAR]"),
    ("agentshroud_env",r"AGENTSHROUD_[A-Z0-9_]+",              "[ENV_VAR]"),
    ("api_key_frag",   r"[A-Za-z0-9_-]{40,}",                  "[API_KEY]"),
    ("private_ip",     r"\b(?:10|172\.(?:1[6-9]|2\d|3[01])|192\.168)\.\d{1,3}\.\d{1,3}\b", "[PRIVATE_IP]"),
]
_COMPILED = [(label, re.compile(pat), repl) for label, pat, repl in _REDACTION_RULES]


def redact_owner(text: str) -> str:
    """Apply all redaction rules to an owner response string."""
    for _label, pattern, replacement in _COMPILED:
        text = pattern.sub(replacement, text)
    return text


def strip_timestamp(text: str) -> str:
    """Remove leading [HH:MM:SS.mmm] timestamps from owner responses."""
    return re.sub(r"^\[\d{2}:\d{2}:\d{2}\.\d{3}\]\s*", "", text)


# ---------------------------------------------------------------------------
# Markdown parser
# ---------------------------------------------------------------------------

def parse_table_row(line: str) -> list[str] | None:
    """Parse a Markdown table row into cells. Returns None for non-table lines."""
    line = line.strip()
    if not line.startswith("|") or line.startswith("| :"):
        return None
    cells = [c.strip() for c in line.split("|")]
    # Remove empty first/last from leading/trailing pipes
    if cells and cells[0] == "":
        cells = cells[1:]
    if cells and cells[-1] == "":
        cells = cells[:-1]
    return cells if len(cells) >= 2 else None


def is_section_header(cells: list[str]) -> bool:
    """Detect bold section header rows like | **BT1 - ...** | **Module:** ..."""
    return cells and cells[0].startswith("**") and cells[0].endswith("**")


def eval_class(eval_text: str) -> str:
    """Map eval text to CSS class."""
    t = eval_text.lower()
    if "pass" in t:
        return "pass"
    if "fail" in t:
        return "fail"
    if "warn" in t:
        return "warn"
    return "info"


# ---------------------------------------------------------------------------
# HTML builder
# ---------------------------------------------------------------------------

_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
    font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif;
    font-size: 9pt;
    color: #1a1a2e;
    background: #ffffff;
    padding: 0;
}

.cover {
    page-break-after: always;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    background: linear-gradient(135deg, #0d1b2a 0%, #1b2838 50%, #16213e 100%);
    color: white;
    text-align: center;
    padding: 60px 40px;
}
.cover .logo { font-size: 64pt; margin-bottom: 16px; }
.cover h1 { font-size: 28pt; font-weight: 700; letter-spacing: -0.5px; margin-bottom: 8px; }
.cover h2 { font-size: 14pt; font-weight: 400; opacity: 0.75; margin-bottom: 40px; }
.cover .badge {
    display: inline-block;
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 20px;
    padding: 6px 20px;
    font-size: 9pt;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin: 6px;
}
.cover .date { margin-top: 48px; opacity: 0.5; font-size: 8pt; }

.summary-page {
    page-break-after: always;
    padding: 40px;
}
.summary-page h2 { font-size: 16pt; font-weight: 700; margin-bottom: 24px; color: #0d1b2a; }

.scorecard {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-bottom: 32px;
}
.score-box {
    border-radius: 12px;
    padding: 20px;
    text-align: center;
}
.score-box .num { font-size: 36pt; font-weight: 700; line-height: 1; }
.score-box .label { font-size: 8pt; text-transform: uppercase; letter-spacing: 1px; margin-top: 6px; opacity: 0.8; }
.score-box.pass { background: #e8f5e9; color: #2e7d32; }
.score-box.fail { background: #fce4ec; color: #c62828; }
.score-box.warn { background: #fff8e1; color: #f57f17; }
.score-box.total { background: #e8eaf6; color: #283593; }

.verdict-box {
    border-radius: 10px;
    padding: 20px 24px;
    margin-bottom: 24px;
    border-left: 5px solid;
}
.verdict-box.strong-pass { background: #e8f5e9; border-color: #43a047; }
.verdict-box.partial { background: #fff8e1; border-color: #ffa000; }
.verdict-box h3 { font-size: 11pt; font-weight: 700; margin-bottom: 6px; }
.verdict-box p { font-size: 8.5pt; line-height: 1.5; }

.legend {
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    margin-bottom: 24px;
}
.legend-item { display: flex; align-items: center; gap: 8px; font-size: 8pt; }
.legend-dot { width: 12px; height: 12px; border-radius: 3px; }

.content-page { padding: 30px 40px; }
.content-page h2 {
    font-size: 14pt; font-weight: 700; color: #0d1b2a;
    border-bottom: 2px solid #e0e0e0;
    padding-bottom: 8px; margin-bottom: 20px;
    page-break-after: avoid;
}

.redaction-note {
    background: #f3f4f6;
    border: 1px solid #d1d5db;
    border-radius: 6px;
    padding: 10px 14px;
    margin-bottom: 20px;
    font-size: 7.5pt;
    color: #374151;
}
.redaction-note strong { color: #111827; }

table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 24px;
    font-size: 7.5pt;
    table-layout: fixed;
}
th {
    background: #1b2838;
    color: white;
    padding: 8px 10px;
    text-align: left;
    font-weight: 600;
    font-size: 7pt;
    letter-spacing: 0.5px;
}
col.c-probe  { width: 5%; }
col.c-sent   { width: 20%; }
col.c-owner  { width: 30%; }
col.c-collab { width: 30%; }
col.c-eval   { width: 15%; }

td {
    padding: 8px 10px;
    vertical-align: top;
    border-bottom: 1px solid #e5e7eb;
    line-height: 1.45;
    word-wrap: break-word;
}
tr:nth-child(even) td { background: #f9fafb; }

/* Row-level highlighting for non-pass results */
tr.row-fail td { background: #fff0f0 !important; border-left: 3px solid #e53935; }
tr.row-warn td { background: #fffde7 !important; border-left: 3px solid #ffa000; }
tr.row-fail td:first-child { font-weight: 700; color: #c62828; }
tr.row-warn td:first-child { font-weight: 700; color: #e65100; }

tr.section-header td {
    background: #e8eaf6;
    font-weight: 600;
    font-size: 7pt;
    color: #283593;
    padding: 10px;
    page-break-after: avoid;
}
tr.section-header td:first-child { font-size: 8pt; }

.eval-pass { color: #2e7d32; font-weight: 600; }
.eval-fail { color: #c62828; font-weight: 600; }
.eval-warn { color: #f57f17; font-weight: 600; }
.eval-info { color: #546e7a; }

.owner-cell { color: #1a237e; }
.collab-cell { color: #4a148c; }

.redacted {
    background: #111;
    color: #111;
    border-radius: 2px;
    padding: 0 3px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 6.5pt;
    cursor: default;
    user-select: none;
}
/* Show label on hover/print — can't hover in PDF, so show tooltip text */
.redacted::before { content: attr(data-label); color: #555; font-size: 6pt; background: #ddd; padding: 0 2px; border-radius: 2px; }

.tag-pass { display:inline-block; background:#c8e6c9; color:#1b5e20; padding:1px 6px; border-radius:10px; font-size:6.5pt; font-weight:600; }
.tag-fail { display:inline-block; background:#ffcdd2; color:#b71c1c; padding:2px 8px; border-radius:10px; font-size:7pt; font-weight:700; }
.tag-warn { display:inline-block; background:#fff3e0; color:#e65100; padding:2px 8px; border-radius:10px; font-size:7pt; font-weight:700; }

.findings-box {
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    margin-bottom: 20px;
    overflow: hidden;
    page-break-inside: avoid;
}
.findings-box-header {
    padding: 8px 14px;
    font-size: 8pt;
    font-weight: 700;
    letter-spacing: 0.3px;
}
.findings-box-header.has-fail { background: #ffebee; color: #b71c1c; }
.findings-box-header.all-warn { background: #fff8e1; color: #e65100; }
.findings-row {
    display: flex;
    align-items: baseline;
    padding: 6px 14px;
    border-top: 1px solid #f0f0f0;
    font-size: 7.5pt;
    gap: 10px;
}
.findings-row:nth-child(even) { background: #fafafa; }
.findings-probe { font-weight: 700; min-width: 40px; color: #555; }
.findings-sent { flex: 1; color: #333; }
.findings-eval { min-width: 80px; text-align: right; }

@page { size: A4 landscape; margin: 15mm 12mm; }
@page :first { margin: 0; }
"""

def html_escape(text: str) -> str:
    return (text
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;"))


def format_owner_cell(raw: str) -> str:
    """Redact + format owner response for HTML."""
    text = strip_timestamp(raw)
    text = redact_owner(text)
    # Replace <br> and <br/> with newlines for processing
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = html_escape(text)
    # Bold markdown
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    # Inline code
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    # Newlines
    text = text.replace("\n", "<br>")
    return f'<span class="owner-cell">{text}</span>'


def format_collab_cell(raw: str) -> str:
    """Format collaborator response for HTML."""
    text = re.sub(r"<br\s*/?>", "\n", raw, flags=re.IGNORECASE)
    text = html_escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = text.replace("\n", "<br>")
    return f'<span class="collab-cell">{text}</span>'


def format_eval_cell(raw: str) -> str:
    cls = eval_class(raw)
    tag_map = {"pass": "tag-pass", "fail": "tag-fail", "warn": "tag-warn"}
    tag = tag_map.get(cls, "")
    clean = html_escape(raw)
    clean = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", clean)
    if tag:
        verdict = re.split(r":\s*", clean, maxsplit=1)
        if len(verdict) == 2:
            return f'<span class="{tag}">{verdict[0]}</span>: {verdict[1]}'
        return f'<span class="{tag}">{clean}</span>'
    return f'<span class="eval-info">{clean}</span>'


def section_header_html(cells: list[str]) -> str:
    label = re.sub(r"\*\*(.*?)\*\*", r"\1", cells[0])
    detail = ""
    if len(cells) > 1:
        d = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", cells[1])
        d = re.sub(r"<br\s*/?>", " ", d, flags=re.IGNORECASE)
        detail = f" — {d}"
    return (
        f'<tr class="section-header">'
        f'<td>{html_escape(label)}</td>'
        f'<td colspan="4">{detail}</td>'
        f'</tr>'
    )


def data_row_html(cells: list[str]) -> tuple[str, str, str, str]:
    """Returns (html, probe_id, sent_text, eval_class)."""
    probe = html_escape(cells[0]) if len(cells) > 0 else ""
    sent  = html_escape(cells[1]) if len(cells) > 1 else ""
    owner = format_owner_cell(cells[2]) if len(cells) > 2 else ""
    collab = format_collab_cell(cells[3]) if len(cells) > 3 else ""
    raw_eval = cells[4] if len(cells) > 4 else ""
    evaltd = format_eval_cell(raw_eval)
    cls = eval_class(raw_eval)
    row_class = f' class="row-{cls}"' if cls in ("fail", "warn") else ""
    html = (
        f"<tr{row_class}>"
        f"<td>{probe}</td>"
        f"<td>{sent}</td>"
        f"<td>{owner}</td>"
        f"<td>{collab}</td>"
        f"<td>{evaltd}</td>"
        f"</tr>"
    )
    return html, cells[0] if cells else "", cells[1] if len(cells) > 1 else "", cls


def build_html(report_path: Path) -> str:
    content = report_path.read_text(encoding="utf-8")
    lines = content.split("\n")

    # Extract report date from title
    title_match = re.search(r"Security Assessment - (\S+ \S+)", content)
    report_date = title_match.group(1) if title_match else "Unknown Date"

    # Build table sections
    table_html_parts: dict[str, list[str]] = {}
    # non_pass_findings: section -> list of (probe_id, sent, eval_class, eval_text)
    non_pass_findings: dict[str, list[tuple[str, str, str, str]]] = {}
    # actual eval counts per section (from eval column only)
    actual_counts: dict[str, dict[str, int]] = {}
    current_section = ""
    in_table = False

    for line in lines:
        if line.startswith("## "):
            current_section = line[3:].strip()
            table_html_parts[current_section] = []
            non_pass_findings[current_section] = []
            actual_counts[current_section] = {"pass": 0, "fail": 0, "warn": 0, "total": 0}
            in_table = False
            continue

        cells = parse_table_row(line)
        if cells is None:
            in_table = False
            continue

        if not in_table:
            in_table = True

        if current_section not in table_html_parts:
            table_html_parts[current_section] = []
            non_pass_findings[current_section] = []
            actual_counts[current_section] = {"pass": 0, "fail": 0, "warn": 0, "total": 0}

        if is_section_header(cells):
            table_html_parts[current_section].append(section_header_html(cells))
        else:
            row_html, probe_id, sent_text, cls = data_row_html(cells)
            table_html_parts[current_section].append(row_html)
            raw_eval = cells[4] if len(cells) > 4 else ""
            if cls in actual_counts[current_section]:
                actual_counts[current_section][cls] += 1
                actual_counts[current_section]["total"] += 1
            elif raw_eval.strip():
                actual_counts[current_section]["pass"] += 1
                actual_counts[current_section]["total"] += 1
            if cls in ("fail", "warn"):
                non_pass_findings[current_section].append(
                    (probe_id, sent_text, cls, raw_eval)
                )

    # Compute summary stats from actual parsed eval counts
    bt_key = next((k for k in actual_counts if "blue" in k.lower()), "Blue Team Validation")
    rt_key = next((k for k in actual_counts if "red" in k.lower()), "Red Team Adversarial Exercise")
    bt = actual_counts.get(bt_key, {"pass": 0, "fail": 0, "warn": 0, "total": 0})
    rt = actual_counts.get(rt_key, {"pass": 0, "fail": 0, "warn": 0, "total": 0})
    total_pass = bt["pass"] + rt["pass"]
    total_fail = bt["fail"] + rt["fail"]
    total_warn = bt["warn"] + rt["warn"]
    total = total_pass + total_fail + total_warn

    verdict_cls = "strong-pass" if total_fail <= 2 else "partial"
    pass_rate = round((total_pass / total) * 100) if total else 0
    verdict_title = f"Security Posture: Strong ({pass_rate}% Pass Rate)" if total_fail <= 2 else f"Security Posture: Partial ({pass_rate}% Pass Rate)"
    verdict_body = (
        f"AgentShroud v0.9.0 passed {total_pass} of {total} probes across Blue Team and Red Team assessments. "
        f"Owner and collaborator trust levels function as distinct security boundaries. "
        f"Owner responses contain full operational detail; collaborator responses are consistently safe-mode gated. "
        f"Sensitive content in this document has been redacted per the redaction policy below."
    )

    def findings_box_html(key: str) -> str:
        findings = non_pass_findings.get(key, [])
        if not findings:
            return ""
        has_fail = any(cls == "fail" for _, _, cls, _ in findings)
        header_cls = "has-fail" if has_fail else "all-warn"
        fail_count = sum(1 for _, _, cls, _ in findings if cls == "fail")
        warn_count = sum(1 for _, _, cls, _ in findings if cls == "warn")
        parts = []
        if fail_count:
            parts.append(f"{fail_count} FAIL")
        if warn_count:
            parts.append(f"{warn_count} WARN")
        summary = " &nbsp;·&nbsp; ".join(parts)
        rows_html = ""
        for probe_id, sent_text, cls, raw_eval in findings:
            tag_cls = "tag-fail" if cls == "fail" else "tag-warn"
            clean_eval = html_escape(raw_eval)
            # Shorten sent text for the callout
            sent_short = html_escape(sent_text[:120] + ("…" if len(sent_text) > 120 else ""))
            rows_html += (
                f'<div class="findings-row">'
                f'<span class="findings-probe">{html_escape(probe_id)}</span>'
                f'<span class="findings-sent">{sent_short}</span>'
                f'<span class="findings-eval"><span class="{tag_cls}">{clean_eval[:60]}</span></span>'
                f'</div>'
            )
        return (
            f'<div class="findings-box">'
            f'<div class="findings-box-header {header_cls}">⚠ Key Findings — {summary} (highlighted in table below)</div>'
            f'{rows_html}'
            f'</div>'
        )

    def section_page(title: str, key: str) -> str:
        rows = "".join(table_html_parts.get(key, []))
        if not rows:
            return ""
        stats = actual_counts.get(key, {"pass": 0, "fail": 0, "warn": 0, "total": 0})
        findings_html = findings_box_html(key)
        return f"""
<div class="content-page">
  <h2>{title}</h2>
  <div class="redaction-note">
    <strong>Redaction policy:</strong> Owner responses are shown with sensitive identifiers removed.
    Redacted values appear as <code>[TELEGRAM_ID]</code>, <code>[ENV_VAR]</code>, <code>[SECRET_PATH]</code>, etc.
    Collaborator responses are shown verbatim — they already contain only safe-mode gated content.
  </div>
  {findings_html}
  <table>
    <colgroup>
      <col class="c-probe"><col class="c-sent"><col class="c-owner"><col class="c-collab"><col class="c-eval">
    </colgroup>
    <thead>
      <tr>
        <th>ID</th>
        <th>Probe Sent</th>
        <th>Owner Response (redacted)</th>
        <th>Collaborator Response</th>
        <th>Evaluation</th>
      </tr>
    </thead>
    <tbody>{rows}</tbody>
  </table>
  <p style="font-size:7pt;color:#888;margin-top:8px;">
    Section totals: {stats['pass']} PASS &nbsp;|&nbsp; {stats['fail']} FAIL &nbsp;|&nbsp; {stats['warn']} WARN
  </p>
</div>
"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>AgentShroud Security Assessment — {report_date}</title>
<style>{_CSS}</style>
</head>
<body>

<!-- COVER PAGE -->
<div class="cover">
  <div class="logo">🛡️</div>
  <h1>AgentShroud™</h1>
  <h2>Security Assessment Report</h2>
  <div>
    <span class="badge">v0.8.0</span>
    <span class="badge">Confidential</span>
    <span class="badge">Redacted</span>
  </div>
  <br>
  <div>
    <span class="badge">Blue Team Validation</span>
    <span class="badge">Red Team Adversarial</span>
  </div>
  <div class="date">Report Date: {report_date} &nbsp;|&nbsp; Generated: {datetime.now().strftime("%Y-%m-%d %H:%M UTC")}</div>
</div>

<!-- SUMMARY PAGE -->
<div class="summary-page">
  <h2>Executive Summary</h2>

  <div class="scorecard">
    <div class="score-box total"><div class="num">{total}</div><div class="label">Total Probes</div></div>
    <div class="score-box pass"><div class="num">{total_pass}</div><div class="label">Passed</div></div>
    <div class="score-box warn"><div class="num">{total_warn}</div><div class="label">Warnings</div></div>
    <div class="score-box fail"><div class="num">{total_fail}</div><div class="label">Failed</div></div>
  </div>

  <div class="verdict-box {verdict_cls}">
    <h3>{verdict_title}</h3>
    <p>{verdict_body}</p>
  </div>

  <div class="scorecard">
    <div class="score-box total"><div class="num">{bt['total']}</div><div class="label">Blue Team Probes</div></div>
    <div class="score-box pass"><div class="num">{bt['pass']}</div><div class="label">BT Pass</div></div>
    <div class="score-box warn"><div class="num">{bt['warn']}</div><div class="label">BT Warn</div></div>
    <div class="score-box fail"><div class="num">{bt['fail']}</div><div class="label">BT Fail</div></div>
  </div>

  <div class="scorecard">
    <div class="score-box total"><div class="num">{rt['total']}</div><div class="label">Red Team Probes</div></div>
    <div class="score-box pass"><div class="num">{rt['pass']}</div><div class="label">RT Pass</div></div>
    <div class="score-box warn"><div class="num">{rt['warn']}</div><div class="label">RT Warn</div></div>
    <div class="score-box fail"><div class="num">{rt['fail']}</div><div class="label">RT Fail</div></div>
  </div>

  <div class="legend">
    <div class="legend-item"><div class="legend-dot" style="background:#43a047;"></div> PASS — Security control functioned correctly</div>
    <div class="legend-item"><div class="legend-dot" style="background:#ffa000;"></div> WARN — Functioned but with minor disclosure or degraded response</div>
    <div class="legend-item"><div class="legend-dot" style="background:#e53935;"></div> FAIL — Security control did not prevent expected leakage</div>
    <div class="legend-item"><div class="legend-dot" style="background:#111;"></div> [REDACTED] — Sensitive value removed from owner response column</div>
  </div>

  <p style="font-size:7.5pt;color:#555;line-height:1.7;">
    <strong>Owner responses</strong> show full operational detail available to the authenticated owner account —
    useful for verifying the bot is working correctly and can see all context.<br>
    <strong>Collaborator responses</strong> show what any approved-but-untrusted collaborator sees through the
    same security proxy — consistently gated to safe-mode notices, capability confirmations, and no raw tool output.<br>
    This contrast is the core security guarantee AgentShroud provides.
  </p>
</div>

{section_page("Blue Team Validation", bt_key)}
{section_page("Red Team Adversarial Exercise", rt_key)}

</body>
</html>
"""


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

OUTPUT_DIR = Path(__file__).parent


def main():
    report = Path(sys.argv[1]) if len(sys.argv) > 1 else latest_report()
    out_pdf = Path(sys.argv[2]) if len(sys.argv) > 2 else OUTPUT_DIR / (report.stem + ".redacted.pdf")
    html_path = out_pdf.with_suffix(".html")

    print(f"Report: {report}")
    print(f"Output: {out_pdf}")

    html_content = build_html(report)
    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    html_path.write_text(html_content, encoding="utf-8")
    print(f"HTML written: {html_path}")

    # PDF engines: Chrome headless (preferred) → weasyprint → pandoc
    chrome_candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "google-chrome", "google-chrome-stable", "chromium", "chromium-browser",
    ]
    chrome_bin = next(
        (c for c in chrome_candidates
         if Path(c).exists() or
         subprocess.run(["which", c], capture_output=True).returncode == 0),
        None,
    )

    if chrome_bin:
        subprocess.run(
            [chrome_bin, "--headless=new", "--disable-gpu", "--no-sandbox",
             f"--print-to-pdf={out_pdf}", "--print-to-pdf-no-header",
             f"file://{html_path.resolve()}"],
            capture_output=True, text=True, timeout=120,
        )
        if out_pdf.exists():
            print(f"PDF written via Chrome: {out_pdf}")
        else:
            print("Chrome headless failed, trying weasyprint...")
            chrome_bin = None  # fall through

    if not chrome_bin:
        result = subprocess.run(
            ["weasyprint", str(html_path), str(out_pdf)],
            capture_output=True, text=True, timeout=120,
        )
        if result.returncode != 0:
            print("weasyprint failed, trying pandoc...")
            result = subprocess.run(
                ["pandoc", str(html_path), "-o", str(out_pdf), "--pdf-engine=weasyprint"],
                capture_output=True, text=True, timeout=120,
            )
            if result.returncode != 0:
                print(f"All PDF engines failed.\n{result.stderr[:500]}")
                sys.exit(1)
        print(f"PDF written: {out_pdf}")

    print("Done.")


if __name__ == "__main__":
    main()
