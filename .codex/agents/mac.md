---
name: mac-app-discovery
description: >
  Discover and catalog ALL applications installed on a macOS system regardless of
  installation method (direct .pkg, compiled from source, Homebrew, Mac App Store,
  Setapp, manual drag-and-drop, system built-in, etc.). Produces a structured
  JSON manifest and a human-readable Markdown catalog with categories,
  descriptions, and top alternatives sourced from the web.
---

# Mac App Discovery Skill

Comprehensive macOS application inventory agent. Scans every known installation
vector, deduplicates results, enriches each entry with metadata, and outputs a
structured catalog ready for sharing and collaboration.

---

## When to Use This Skill

- User wants a full inventory of installed Mac applications
- User wants to catalog, categorize, or document their Mac setup
- User is building a "must-have apps" list or onboarding guide
- User wants to compare their toolset against alternatives

---

## Discovery Strategy

The agent MUST run **all** of the following discovery methods in order.
Each method catches apps the others miss. **Do not skip any step.**

### Phase 1 — Raw Collection

Run each command and capture output. All commands target macOS and must be
executed on the user's Mac (or against files exported from it).

#### 1. System Profiler (most comprehensive single source)

```bash
system_profiler SPApplicationsDataType -json > /tmp/mac_apps_system_profiler.json
```

Returns every `.app` bundle the OS knows about, including:
- Path, version, architecture (Apple Silicon / Intel / Universal)
- Source ("Mac App Store", "Identified Developer", "Apple")
- Last modified date
- Signing authority

**Parse this first** — it is the authoritative baseline.

#### 2. Applications Folders (catch drag-and-drop installs)

```bash
# Global apps
find /Applications -maxdepth 3 -name "*.app" -print0 | xargs -0 \
  mdls -name kMDItemCFBundleIdentifier -name kMDItemDisplayName \
       -name kMDItemVersion -name kMDItemAppStoreCategory 2>/dev/null

# User-level apps
find ~/Applications -maxdepth 3 -name "*.app" -print0 | xargs -0 \
  mdls -name kMDItemCFBundleIdentifier -name kMDItemDisplayName \
       -name kMDItemVersion -name kMDItemAppStoreCategory 2>/dev/null

# System apps (read-only, for reference)
find /System/Applications -maxdepth 2 -name "*.app" -print0 | xargs -0 \
  mdls -name kMDItemCFBundleIdentifier -name kMDItemDisplayName \
       -name kMDItemVersion 2>/dev/null
```

#### 3. Homebrew (formulae + casks)

```bash
# Check if Homebrew is installed
if command -v brew &>/dev/null; then
  echo "=== BREW FORMULAE ==="
  brew list --formula --versions
  echo "=== BREW CASKS ==="
  brew list --cask --versions
  echo "=== BREW TAPS ==="
  brew tap
else
  echo "Homebrew not installed"
fi
```

#### 4. Mac App Store (via `mas` CLI)

```bash
# Install mas if missing
if ! command -v mas &>/dev/null; then
  brew install mas 2>/dev/null || echo "mas not available"
fi

if command -v mas &>/dev/null; then
  mas list   # outputs: <app_id>  <app_name> (<version>)
fi
```

#### 5. Setapp Detection

Setapp apps live in `/Applications/Setapp` or are symlinked from
`~/Library/Application Support/Setapp/`. They also contain a
`SetappMetadata.plist` inside the bundle.

```bash
# Setapp folder
if [ -d "/Applications/Setapp" ]; then
  ls -1 /Applications/Setapp/
fi

# Setapp metadata in any app bundle
find /Applications -maxdepth 3 -name "SetappMetadata.plist" 2>/dev/null
```

#### 6. Package Receipts (direct .pkg installs)

```bash
pkgutil --pkgs | sort
```

Cross-reference with `pkgutil --pkg-info <package_id>` for install date and
version. Many CLI tools, drivers, and system extensions install via .pkg only.

#### 7. CLI Tools & Utilities (non-.app installs)

```bash
# Binaries in common paths not managed by brew
for dir in /usr/local/bin /opt/homebrew/bin ~/.local/bin ~/bin; do
  if [ -d "$dir" ]; then
    echo "=== $dir ==="
    ls -1 "$dir" 2>/dev/null
  fi
done

# pip-installed tools
pip3 list --format=json 2>/dev/null

# npm global packages
npm list -g --depth=0 --json 2>/dev/null

# cargo-installed tools
if [ -d ~/.cargo/bin ]; then
  ls -1 ~/.cargo/bin
fi

# go-installed tools
if [ -d ~/go/bin ]; then
  ls -1 ~/go/bin
fi
```

#### 8. Launch Agents & Daemons (background services)

```bash
# User launch agents
ls ~/Library/LaunchAgents/ 2>/dev/null

# System launch agents & daemons
ls /Library/LaunchAgents/ 2>/dev/null
ls /Library/LaunchDaemons/ 2>/dev/null
```

#### 9. Browser Extensions (optional but useful)

```bash
# Chrome extensions
find ~/Library/Application\ Support/Google/Chrome -name "manifest.json" \
  -path "*/Extensions/*" -exec grep -l '"name"' {} \; 2>/dev/null

# Safari extensions
pluginkit -mDA -p com.apple.Safari.web-extension 2>/dev/null
```

#### 10. Spotlight Catch-All

```bash
mdfind "kMDItemContentType == 'com.apple.application-bundle'" | sort
```

This may find apps in unusual locations (e.g., inside `~/Downloads`,
`/opt`, developer tool chains, etc.).

---

### Phase 2 — Deduplication & Normalization

After collecting from all sources, build a unified record per application:

```
Dedup Key = lowercase(bundle_identifier) || lowercase(app_name)
```

For each unique app, merge data into this schema:

```json
{
  "name": "string — Display name",
  "bundle_id": "string — e.g. com.example.app (null if CLI tool)",
  "version": "string",
  "install_source": "enum: app_store | homebrew_formula | homebrew_cask | setapp | pkg_installer | drag_and_drop | system_builtin | pip | npm | cargo | go | source_compiled | unknown",
  "path": "string — filesystem path",
  "arch": "enum: apple_silicon | intel | universal | unknown",
  "signing": "string — signing authority",
  "last_modified": "ISO date",
  "category": "string — assigned in Phase 3",
  "description": "string — 1-2 sentence summary",
  "alternatives": ["string — top 3 alternatives"],
  "website": "string — official URL",
  "is_cli": "boolean",
  "is_system": "boolean"
}
```

**Install Source Heuristics:**

| Signal | Source |
|--------|--------|
| `mas list` output | `app_store` |
| `brew list --cask` output | `homebrew_cask` |
| `brew list --formula` output | `homebrew_formula` |
| Contains `SetappMetadata.plist` | `setapp` |
| In `pkgutil --pkgs` but not brew/mas/setapp | `pkg_installer` |
| In `/Applications` but no receipt | `drag_and_drop` |
| In `/System/Applications` | `system_builtin` |
| Source field says "Apple" in system_profiler | `system_builtin` |
| In `pip3 list` | `pip` |
| In `npm list -g` | `npm` |
| In `~/.cargo/bin` | `cargo` |
| In `~/go/bin` | `go` |

---

### Phase 3 — Categorization

Assign each app to ONE primary category. Use these standard categories
(add new ones only if nothing fits):

| Category | Examples |
|----------|----------|
| **Productivity & Office** | Microsoft Office, Notion, Obsidian, Things 3 |
| **Development & Engineering** | VS Code, Xcode, Docker, iTerm2, Git |
| **DevOps & Infrastructure** | AWS CLI, Terraform, kubectl, Ansible |
| **Data & Analytics** | Tableau, DBeaver, Jupyter, Excel |
| **Design & Creative** | Figma, Photoshop, Sketch, Canva |
| **Communication & Collaboration** | Slack, Teams, Zoom, Discord |
| **Email & Calendar** | Outlook, Spark, Fantastical, Calendly |
| **Web Browsers** | Chrome, Firefox, Safari, Arc, Brave |
| **Security & Privacy** | 1Password, Little Snitch, Wireshark, VPN clients |
| **System Utilities** | CleanMyMac, Alfred, Raycast, BetterTouchTool |
| **Window Management** | Magnet, Rectangle, Amethyst, Moom |
| **Backup & Storage** | Time Machine, Backblaze, Dropbox, Google Drive |
| **Media & Entertainment** | Spotify, VLC, IINA, Plex |
| **Writing & Documentation** | Bear, Ulysses, Typora, Scrivener |
| **AI & Machine Learning** | ChatGPT, Claude, Ollama, Stable Diffusion |
| **Networking & Remote Access** | Royal TSX, Tailscale, WireGuard, Transmit |
| **Virtualization & Containers** | Docker, Parallels, UTM, VMware Fusion |
| **Terminal & Shell** | iTerm2, Warp, Alacritty, Hyper |
| **Package Managers & Toolchains** | Homebrew, nvm, pyenv, rustup |
| **System (Apple Built-in)** | Finder, Safari, Mail, Calendar, Preview |
| **Drivers & Hardware** | printer drivers, audio interfaces, etc. |
| **Other** | Anything that doesn't fit above |

---

### Phase 4 — Enrichment

For each non-system app, use web search to gather:

1. **Description** — 1-2 sentence summary of what the app does.
   Pull from the app's official website or reputable source.
2. **Top 3 Alternatives** — Competing or similar apps. Prioritize:
   - Direct competitors (same core use case)
   - Open-source alternatives
   - Cross-platform alternatives
3. **Official Website URL**

Batch web searches efficiently. Group similar apps together:
- `"best alternatives to [AppName] mac 2025"`
- `"[AppName] vs competitors"`

For well-known apps (VS Code, Slack, Chrome, etc.), use existing knowledge
to avoid unnecessary web searches.

---

### Phase 5 — Output Generation

Produce TWO output files:

#### A. `mac_app_catalog.json` — Machine-readable manifest

Full JSON array of all app records using the schema from Phase 2.
Include a metadata header:

```json
{
  "generated_at": "ISO timestamp",
  "hostname": "machine name",
  "macos_version": "version string",
  "total_apps": 123,
  "categories": { "Development": 45, "Productivity": 22, ... },
  "apps": [ ... ]
}
```

#### B. `mac_app_catalog.md` — Human-readable catalog

Structure:

```markdown
# Must-Have Mac Apps Catalog
> Generated: [date] | Machine: [hostname] | macOS [version]
> Total: [N] applications across [M] categories

## Table of Contents
- [Category Name (count)](#category-name)
- ...

---

## Category Name (count)

### App Name
- **Version:** x.y.z | **Source:** Homebrew Cask | **Arch:** Universal
- **What it does:** Brief 1-2 sentence description.
- **Alternatives:** Alt1, Alt2, Alt3
- **Website:** https://...

### Next App Name
...
```

**Formatting Rules:**
- Sort categories alphabetically
- Within each category, sort apps alphabetically
- System built-in apps go in their own section at the end
- CLI-only tools get a `[CLI]` badge after their name
- Mark Setapp apps with a `[Setapp]` badge
- Mark App Store apps with a `[App Store]` badge

---

## Error Handling

- If a command fails (e.g., `brew` not installed), log it and continue.
  Never abort the full scan because one source is unavailable.
- If `mas` is not installed and cannot be installed, note that App Store
  apps will be detected via system_profiler but without App Store IDs.
- If running in a non-macOS environment, inform the user that this skill
  requires execution on macOS and offer to generate a template/script
  they can run locally.

---

## Performance Notes

- `system_profiler SPApplicationsDataType` can take 30-60 seconds on
  machines with many apps. Run it first and parse while other commands run.
- `mdfind` is fast but requires Spotlight indexing to be enabled.
- Enrichment (Phase 4) is the slowest phase due to web searches. For
  large catalogs (200+ apps), consider batching or limiting enrichment
  to non-system apps only.

---

## Future Extensions (for collaborative sharing)

This skill produces the baseline catalog. The following features are
planned for the sharing/collaboration phase:

- **Rating system** — colleagues rate apps 1-5 stars
- **Comments** — free-text notes per app
- **Suggest additions** — colleagues can nominate apps not on the list
- **Category voting** — community-driven recategorization
- **Export formats** — Notion database, Airtable, Google Sheets, web app
- **Diff mode** — compare two users' catalogs side-by-side
