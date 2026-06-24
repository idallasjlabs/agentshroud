#!/usr/bin/env python3
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Markdown → HTML email renderer (Python stdlib only, no pip installs).

Pre-installed at /usr/local/lib/agentshroud/render_md_email.py inside the Hermes
Docker image.  Used by the competitive-intelligence email cron job.

Usage:
    python3 render_md_email.py <input.md> [output.html]

Default output path: /tmp/competitive-email.html
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

_CSS = """
  body{font-family:-apple-system,Arial,sans-serif;background:#ffffff;color:#111111;
       max-width:700px;margin:0 auto;padding:24px 16px;line-height:1.6}
  h1,h2,h3,h4,h5,h6{color:#111111;border-bottom:1px solid #e0e0e0;
                     padding-bottom:6px;margin-top:24px}
  a{color:#1a73e8}
  code{background:#f6f8fa;border:1px solid #d0d7de;border-radius:3px;
       padding:2px 5px;font-family:monospace;font-size:.9em}
  pre{background:#f6f8fa;border:1px solid #d0d7de;border-radius:6px;
      padding:12px 16px;overflow-x:auto}
  pre code{background:none;border:none;padding:0}
  table{border-collapse:collapse;width:100%;margin:16px 0}
  th{background:#f6f8fa;text-align:left;padding:8px 12px;
     border:1px solid #d0d7de;font-weight:600}
  td{padding:8px 12px;border:1px solid #d0d7de;vertical-align:top}
  blockquote{margin:8px 0 8px 16px;padding-left:12px;
             border-left:4px solid #d0d7de;color:#555}
  hr{border:none;border-top:1px solid #e0e0e0;margin:20px 0}
  ul,ol{padding-left:24px}
  li{margin:4px 0}
"""

_FENCED_RE = re.compile(r"^```([^\n]*)\n(.*?)^```", re.MULTILINE | re.DOTALL)
_HR_RE = re.compile(r"^[ \t]*(?:-{3,}|={3,}|\*{3,})[ \t]*$")
_ATX_RE = re.compile(r"^(#{1,6})\s+(.*?)(?:\s+#+)?\s*$")


def _esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _inline(text: str) -> str:
    """Apply inline Markdown spans to plain text (no recursive nesting)."""
    # Images before links (! prefix distinguishes them)
    text = re.sub(
        r"!\[([^\]]*)\]\(([^)]+)\)",
        lambda m: f'<img alt="{_esc(m[1])}" src="{_esc(m[2])}" style="max-width:100%">',
        text,
    )
    # Hyperlinks
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{_esc(m[2])}">{_esc(m[1])}</a>',
        text,
    )
    # Inline code (before bold/italic to avoid false delimiter matches)
    text = re.sub(r"`([^`]+)`", lambda m: f"<code>{_esc(m[1])}</code>", text)
    # Bold (**text** or __text__)
    text = re.sub(
        r"\*\*(.+?)\*\*|__(.+?)__",
        lambda m: f"<strong>{_esc(m[1] or m[2])}</strong>",
        text,
    )
    # Italic (*text* or _text_) — single delimiters only
    text = re.sub(
        r"\*([^*\s][^*]*?)\*|_([^_\s][^_]*?)_",
        lambda m: f"<em>{_esc(m[1] or m[2])}</em>",
        text,
    )
    return text


def _render_table(rows: list[str]) -> str:
    out = ["<table>"]
    header_emitted = False
    for row in rows:
        if re.match(r"^[\s|:-]+$", row):
            header_emitted = True
            continue
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        tag = "th" if not header_emitted else "td"
        out.append(
            "<tr>" + "".join(f"<{tag}>{_inline(c)}</{tag}>" for c in cells) + "</tr>"
        )
        if not header_emitted:
            header_emitted = True
    out.append("</table>")
    return "\n".join(out)


def render(md: str) -> str:
    # ── Protect fenced code blocks ──────────────────────────────────────────
    fenced: list[str] = []

    def _save_fence(m: re.Match) -> str:
        idx = len(fenced)
        lang = m[1].strip()
        inner = _esc(m[2])
        cls = f' class="language-{lang}"' if lang else ""
        fenced.append(f"<pre><code{cls}>{inner}</code></pre>")
        return f"\x00FEN{idx}\x00"

    md = _FENCED_RE.sub(_save_fence, md)

    # ── Line-by-line block rendering ────────────────────────────────────────
    lines = md.splitlines()
    out: list[str] = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Fenced code block placeholder (whole line)
        m = re.fullmatch(r"\x00FEN(\d+)\x00", line.strip())
        if m:
            out.append(fenced[int(m[1])])
            i += 1
            continue

        # Horizontal rule (must come before setext to catch bare ---)
        if _HR_RE.match(line):
            out.append("<hr>")
            i += 1
            continue

        # ATX heading
        m = _ATX_RE.match(line)
        if m:
            lvl = len(m[1])
            out.append(f"<h{lvl}>{_inline(m[2])}</h{lvl}>")
            i += 1
            continue

        # Setext heading (text line followed by === or ---)
        if i + 1 < len(lines) and line.strip():
            nxt = lines[i + 1].strip()
            if re.fullmatch(r"=+", nxt) and len(nxt) >= 2:
                out.append(f"<h1>{_inline(line.strip())}</h1>")
                i += 2
                continue
            if re.fullmatch(r"-+", nxt) and len(nxt) >= 2:
                out.append(f"<h2>{_inline(line.strip())}</h2>")
                i += 2
                continue

        # GFM table: current line contains | AND next line is a separator row
        if "|" in line and i + 1 < len(lines) and re.match(r"^[\s|:-]+$", lines[i + 1]):
            tbl: list[str] = [line]
            j = i + 1
            while j < len(lines) and (
                re.match(r"^[\s|:-]+$", lines[j]) or "|" in lines[j]
            ):
                tbl.append(lines[j])
                j += 1
            out.append(_render_table(tbl))
            i = j
            continue

        # Blockquote
        if line.startswith("> ") or line == ">":
            bq: list[str] = []
            while i < len(lines) and (
                lines[i].startswith("> ") or lines[i] == ">"
            ):
                bq.append(lines[i][2:] if lines[i].startswith("> ") else "")
                i += 1
            out.append(f"<blockquote>{_inline(' '.join(bq))}</blockquote>")
            continue

        # Unordered list
        if re.match(r"^[ \t]{0,3}[-*+] ", line):
            items: list[str] = []
            while i < len(lines) and re.match(r"^[ \t]{0,3}[-*+] ", lines[i]):
                items.append(_inline(re.sub(r"^[ \t]{0,3}[-*+] ", "", lines[i])))
                i += 1
            out.append("<ul>" + "".join(f"<li>{it}</li>" for it in items) + "</ul>")
            continue

        # Ordered list
        if re.match(r"^[ \t]{0,3}\d+[.)]\s", line):
            items = []
            while i < len(lines) and re.match(r"^[ \t]{0,3}\d+[.)]\s", lines[i]):
                items.append(
                    _inline(re.sub(r"^[ \t]{0,3}\d+[.)]\s+", "", lines[i]))
                )
                i += 1
            out.append("<ol>" + "".join(f"<li>{it}</li>" for it in items) + "</ol>")
            continue

        # Blank line
        if not line.strip():
            i += 1
            continue

        # Paragraph — accumulate until blank line or block-level element starts
        para: list[str] = []
        while i < len(lines):
            ln = lines[i]
            if not ln.strip():
                break
            if (
                re.fullmatch(r"\x00FEN\d+\x00", ln.strip())
                or _HR_RE.match(ln)
                or _ATX_RE.match(ln)
                or ln.startswith("> ")
                or re.match(r"^[ \t]{0,3}[-*+] ", ln)
                or re.match(r"^[ \t]{0,3}\d+[.)]\s", ln)
            ):
                break
            para.append(ln)
            i += 1
        if para:
            out.append(f"<p>{_inline(' '.join(para))}</p>")

    body = "\n".join(out)

    # Restore any fenced placeholders that ended up inside paragraphs
    body = re.sub(r"\x00FEN(\d+)\x00", lambda m: fenced[int(m[1])], body)

    return (
        "<!DOCTYPE html>\n"
        '<html lang="en">\n'
        "<head>\n"
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        f"<style>{_CSS}</style>\n"
        "</head>\n"
        "<body>\n"
        f"{body}\n"
        "</body>\n"
        "</html>"
    )


def main() -> None:
    argv = sys.argv[1:]
    if not argv:
        print(f"Usage: {sys.argv[0]} input.md [output.html]", file=sys.stderr)
        sys.exit(1)
    src = Path(argv[0])
    if not src.exists():
        print(f"Error: {src} does not exist", file=sys.stderr)
        sys.exit(1)
    dst = Path(argv[1]) if len(argv) > 1 else Path("/tmp/competitive-email.html")
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(render(src.read_text(encoding="utf-8")), encoding="utf-8")
    print(f"Rendered {src.name} → {dst} ({dst.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
