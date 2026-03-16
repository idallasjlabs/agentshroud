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
.tag-fail { display:inline-block; background:#ffcdd2; color:#b71c1c; padding:1px 6px; border-radius:10px; font-size:6.5pt; font-weight:600; }
.tag-warn { display:inline-block; background:#fff3e0; color:#e65100; padding:1px 6px; border-radius:10px; font-size:6.5pt; font-weight:600; }

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


def data_row_html(cells: list[str]) -> str:
    probe = html_escape(cells[0]) if len(cells) > 0 else ""
    sent  = html_escape(cells[1]) if len(cells) > 1 else ""
    owner = format_owner_cell(cells[2]) if len(cells) > 2 else ""
    collab = format_collab_cell(cells[3]) if len(cells) > 3 else ""
    evaltd = format_eval_cell(cells[4]) if len(cells) > 4 else ""
    return (
        f"<tr>"
        f"<td>{probe}</td>"
        f"<td>{sent}</td>"
        f"<td>{owner}</td>"
        f"<td>{collab}</td>"
        f"<td>{evaltd}</td>"
        f"</tr>"
    )


def build_html(report_path: Path) -> str:
    content = report_path.read_text(encoding="utf-8")
    lines = content.split("\n")

    # Extract report date from title
    title_match = re.search(r"Security Assessment - (\S+ \S+)", content)
    report_date = title_match.group(1) if title_match else "Unknown Date"

    # Count stats
    bt_content = content[content.find("## Blue Team"):content.find("## Red Team")] if "## Red Team" in content else ""
    rt_content = content[content.find("## Red Team"):] if "## Red Team" in content else content
    
    def count_section(s):
        return {
            "pass": s.count("PASS"),
            "fail": s.count("FAIL"),
            "warn": s.count("WARN"),
            "total": s.count("PASS") + s.count("FAIL") + s.count("WARN"),
        }
    
    bt = count_section(bt_content)
    rt = count_section(rt_content)
    total_pass = bt["pass"] + rt["pass"]
    total_fail = bt["fail"] + rt["fail"]
    total_warn = bt["warn"] + rt["warn"]
    total = total_pass + total_fail + total_warn

    verdict_cls = "strong-pass" if total_fail <= 2 else "partial"
    pass_rate = round((total_pass / total) * 100) if total else 0
    verdict_title = f"Security Posture: Strong ({pass_rate}% Pass Rate)" if total_fail <= 2 else f"Security Posture: Partial ({pass_rate}% Pass Rate)"
    verdict_body = (
        f"AgentShroud v0.8.0 passed {total_pass} of {total} probes across Blue Team and Red Team assessments. "
        f"Owner and collaborator trust levels function as distinct security boundaries. "
        f"Owner responses contain full operational detail; collaborator responses are consistently safe-mode gated. "
        f"Sensitive content in this document has been redacted per the redaction policy below."
    )

    # Build table sections
    table_html_parts: dict[str, list[str]] = {}
    current_section = ""
    in_table = False

    for line in lines:
        if line.startswith("## "):
            current_section = line[3:].strip()
            table_html_parts[current_section] = []
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

        if is_section_header(cells):
            table_html_parts[current_section].append(section_header_html(cells))
        else:
            table_html_parts[current_section].append(data_row_html(cells))

    def section_page(title: str, key: str, stats: dict) -> str:
        rows = "".join(table_html_parts.get(key, []))
        if not rows:
            return ""
        return f"""
<div class="content-page">
  <h2>{title}</h2>
  <div class="redaction-note">
    <strong>Redaction policy:</strong> Owner responses are shown with sensitive identifiers removed.
    Redacted values appear as <code>[TELEGRAM_ID]</code>, <code>[ENV_VAR]</code>, <code>[SECRET_PATH]</code>, etc.
    Collaborator responses are shown verbatim — they already contain only safe-mode gated content.
  </div>
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

{section_page("Blue Team Validation", "Blue Team Validation", bt)}
{section_page("Red Team Adversarial Testing", "Red Team Adversarial Testing", rt)}

</body>
</html>
"""


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    report = Path(sys.argv[1]) if len(sys.argv) > 1 else latest_report()
    out_pdf = Path(sys.argv[2]) if len(sys.argv) > 2 else report.with_suffix(".redacted.pdf")

    print(f"Report: {report}")
    print(f"Output: {out_pdf}")

    html_content = build_html(report)
    html_path = report.with_suffix(".redacted.html")
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
