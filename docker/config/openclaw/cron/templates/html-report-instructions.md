# Report Delivery Format Instructions

Every report has **two delivery surfaces**, and they use different formats:

| Surface  | Format                        | Why |
|----------|-------------------------------|-----|
| **Email**    | Branded HTML (template below) | Mail clients render HTML natively — brand colors, tables, callouts, badges all display inline. |
| **Telegram** | Markdown / plain text         | Telegram does not render HTML inline — attached `.html` files show as raw source. Markdown is readable in-chat. |

**Rule of thumb:** Save every report as both `.html` (for email) and `.md` (for Telegram). Never paste raw HTML source into a Telegram message.

---

## Canonical storage

Save reports to `/home/node/.openclaw/workspace/reports/` using this naming:

- `competitive-report-YYYY-MM-DD.html` — branded HTML for email
- `competitive-report-YYYY-MM-DD.md` — markdown version for Telegram and archival

The HTML is the "showcase" artifact; the markdown is the working copy. Both should carry the same facts.

---

## HTML version (for email)

Use the AgentShroud branded HTML template at `/home/node/.openclaw/workspace/templates/report-template.html`.

### How to build it

1. Read the template from `/home/node/.openclaw/workspace/templates/report-template.html`
2. Replace `{{REPORT_TITLE}}` with the report title
3. Replace `{{REPORT_TYPE}}` with the report type (e.g., "Competitive Intelligence", "Collaborator Report")
4. Replace `{{REPORT_DATE}}` with today's date in "Month Day, Year" format
5. Replace `{{REPORT_CONTENT}}` with the report body using proper HTML tags:
   - `<h2>` for section headers
   - `<h3>` for subsection headers
   - `<p>` for paragraphs
   - `<ul><li>` for bullet lists
   - `<table><thead><tr><th>` for tables
   - `<div class="callout">` for callouts (add `-warning`, `-danger`, `-success` variants)
   - `<span class="badge badge-success">` (or `-warning`, `-danger`, `-info`) for status badges
   - `<div class="divider"></div>` for section separators
6. Save the complete HTML file to `/home/node/.openclaw/workspace/reports/`

### Sending via email

When delivering the report by email, paste the **full HTML file contents** as the email body with content type `text/html` (e.g., `html: true` on the mail tool). Never attach the HTML as a file unless the user explicitly asks — inline rendering is the whole point.

### Brand colors reference
- Primary: `#1583f0` (blue)
- Secondary: `#0d4f8f` (dark blue)
- Accent: `#4da6ff` (light blue)
- Background: `#000000` (black — do not use any blue/purple tint for the body background)
- Text: `#e8e8e8` (near-white, for readability on black)
- Success: `#28a745` / Warning: `#ffc107` / Danger: `#dc3545`

---

## Markdown version (for Telegram + archival)

Write the same report as a `.md` file using standard markdown:

- `#`, `##`, `###` for headers
- `- ` for bullets, `1.` for numbered lists
- `| a | b |` tables (ok for archival; Telegram will show them as plain text)
- `> ` blockquotes for callouts
- `**bold**` / `*italic*` for emphasis
- `---` for section dividers

### Telegram delivery rules (from AGENTS.md)

- **No markdown tables** in Telegram messages — convert to bullet lists before sending
- **No raw HTML** — Telegram will display it as source
- Prefer **short summary + key bullets** in the chat message; link or attach the full `.md` file if the report is long
- If the report is too long for a single message, send a 5–8 bullet executive summary and offer the full file on request

---

## Source Verification Policy (MANDATORY)

Every factual claim in a report MUST have a clickable source URL. No exceptions.

### Rules

1. **GitHub competitor data:** Always link to the specific release page (`https://github.com/org/repo/releases/tag/vX.Y.Z`) or releases list.
2. **Ecosystem signals / articles:** Must include the actual article URL. Fetch the URL and confirm it returns 200 before including.
3. **If a source URL cannot be verified (404, no results, cannot find):** DO NOT include the claim. Omit it entirely.
4. **Never cite an article by name without a working URL.** "TechCrunch reported X" without a link is not acceptable.
5. **In the HTML report:** Every competitor name links to its GitHub repo. Every ecosystem signal links to its source article.
6. **In the Markdown report:** Use inline `[text](url)` links for every source.
7. **In competitive-analysis.md:** Every entry in Ecosystem Signals must have a URL in parentheses or brackets.

### Verification checklist (run before saving any report)

- [ ] Every competitor version links to the GitHub releases page
- [ ] Every article/blog reference has a fetched-and-confirmed URL
- [ ] No claim exists without a first-party source
- [ ] Claims that failed URL verification have been REMOVED, not left in with a note

---

## Quick checklist

Before calling a report "delivered":

- [ ] **Source verification policy above is satisfied** — every claim has a working URL
- [ ] `.html` version saved to `/reports/` and sent via **email** (inline HTML body, not attachment)
- [ ] `.md` version saved to `/reports/`
- [ ] Telegram message is **markdown / plain text** with an exec summary, not raw HTML source
- [ ] `competitive-analysis.md` updated with verified latest state (if competitive report)
- [ ] `reports/trend-log.md` appended (if competitive report)
