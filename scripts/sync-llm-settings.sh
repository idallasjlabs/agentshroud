#!/usr/bin/env bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# scripts/sync-llm-settings.sh — Sync skills/agents/MCP from ~/.llm_settings into both bots.
#
# SINGLE SOURCE OF TRUTH: ~/.llm_settings/
#   skills/    — skill definition files (SKILL.md, references/, etc.)
#   mcp/       — MCP server configs (no tokens — only structural definitions)
#   agents/    — bot persona / instruction files
#
# DESTINATIONS:
#   docker/config/openclaw/   — OpenClaw bot config directory
#   docker/config/hermes/     — Hermes bot config directory
#
# MANIFEST: A manifest.json is written to each destination recording the SHA-256
# hash of every synced file. Used by validate-skills-manifest.sh as a CI gate.
#
# IDEMPOTENCY: Files are only overwritten when their hash has changed.
# Running twice against the same source produces the same result.
#
# USAGE:
#   bash scripts/sync-llm-settings.sh [--source DIR] [--dry-run]
#
#   --source DIR    Override source (default: ~/.llm_settings)
#   --dry-run       Print what would change without writing anything
#
# EXIT CODES:
#   0 — success (including "nothing to sync" when already in sync)
#   1 — ~/.llm_settings is missing or empty
#   2 — argument error

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$SCRIPT_DIR/.." && pwd)"

# ── Defaults ─────────────────────────────────────────────────────────────────
SOURCE="${HOME}/.llm_settings"
DRY_RUN=0

# ── Argument parsing ─────────────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
  case "$1" in
    --source)
      SOURCE="$2"; shift 2 ;;
    --dry-run)
      DRY_RUN=1; shift ;;
    *)
      echo "ERROR: Unknown argument: $1" >&2
      echo "Usage: $0 [--source DIR] [--dry-run]" >&2
      exit 2 ;;
  esac
done

# ── SHA-256 helper (macOS + Linux) ────────────────────────────────────────────
_sha256() {
  local file="$1"
  if command -v sha256sum &>/dev/null; then
    sha256sum "$file" | awk '{print $1}'
  else
    shasum -a 256 "$file" | awk '{print $1}'
  fi
}

# ── Write manifest.json (JSON via python3 for correctness) ───────────────────
_write_manifest() {
  local src="$1" out="$2"
  local ts
  ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

  entries_json=""
  first=1
  for subdir in skills mcp agents; do
    src_subdir="${src}/${subdir}"
    [[ -d "$src_subdir" ]] || continue
    while IFS= read -r -d '' f; do
      rel="${f#${src}/}"
      hash="$(_sha256 "$f")"
      size="$(wc -c < "$f" | tr -d ' ')"
      entry="{\"name\":\"${rel}\",\"hash\":\"${hash}\",\"size\":${size}}"
      if [[ $first -eq 1 ]]; then
        entries_json="${entry}"
        first=0
      else
        entries_json="${entries_json},${entry}"
      fi
    done < <(find "$src_subdir" -type f -print0 2>/dev/null | sort -z)
  done

  python3 - "$entries_json" "$ts" > "$out" <<'PYEOF'
import json, sys
entries_raw = sys.argv[1].strip()
ts = sys.argv[2]
entries = json.loads('[' + entries_raw + ']') if entries_raw else []
manifest = {'version': '1', 'generated_at': ts, 'entries': entries}
print(json.dumps(manifest, indent=2))
PYEOF
}

# ── Validate source ──────────────────────────────────────────────────────────
if [[ ! -d "$SOURCE" ]]; then
  echo "ERROR: Source directory not found: ${SOURCE}" >&2
  echo "Create ~/.llm_settings/ with skills/, mcp/, and agents/ subdirectories." >&2
  exit 1
fi

# Count eligible files (skills/ mcp/ agents/ subtrees only)
file_count=0
for subdir in skills mcp agents; do
  if [[ -d "${SOURCE}/${subdir}" ]]; then
    while IFS= read -r -d '' _f; do
      (( file_count++ )) || true
    done < <(find "${SOURCE}/${subdir}" -type f -print0 2>/dev/null)
  fi
done

if [[ "$file_count" -eq 0 ]]; then
  echo "ERROR: Source directory is empty — no eligible files found in ${SOURCE}" >&2
  echo "Expected subdirectories: skills/, mcp/, agents/" >&2
  exit 1
fi

# ── Destinations ─────────────────────────────────────────────────────────────
declare -a DESTINATIONS=(
  "${REPO}/docker/config/openclaw"
  "${REPO}/docker/config/hermes"
)

# ── Header ───────────────────────────────────────────────────────────────────
copied=0
skipped=0

echo ""
echo "╔══════════════════════════════════════════════════════╗"
echo "║  AgentShroud™ — Skills Manifest Sync                 ║"
echo "╚══════════════════════════════════════════════════════╝"
echo ""
echo "  Source      : ${SOURCE}"
echo "  Destinations: ${#DESTINATIONS[@]}"
echo "  Dry run     : $([ "$DRY_RUN" -eq 1 ] && echo yes || echo no)"
echo ""

# ── Per-destination sync ─────────────────────────────────────────────────────
for dest in "${DESTINATIONS[@]}"; do
  echo "── Syncing → ${dest}"
  mkdir -p "$dest"

  for subdir in skills mcp agents; do
    src_subdir="${SOURCE}/${subdir}"
    [[ -d "$src_subdir" ]] || continue

    while IFS= read -r -d '' src_file; do
      rel="${src_file#${SOURCE}/}"
      dst_file="${dest}/${rel}"

      # Idempotency gate: skip if hash already matches
      if [[ -f "$dst_file" ]]; then
        src_hash="$(_sha256 "$src_file")"
        dst_hash="$(_sha256 "$dst_file")"
        if [[ "$src_hash" == "$dst_hash" ]]; then
          (( skipped++ )) || true
          continue
        fi
      fi

      if [[ "$DRY_RUN" -eq 1 ]]; then
        echo "    [DRY-RUN] would copy: ${rel}"
      else
        mkdir -p "$(dirname "$dst_file")"
        cp "$src_file" "$dst_file"
        echo "    copied: ${rel}"
      fi
      (( copied++ )) || true
    done < <(find "$src_subdir" -type f -print0 2>/dev/null)
  done

  # Write manifest.json to destination
  if [[ "$DRY_RUN" -eq 0 ]]; then
    _write_manifest "$SOURCE" "${dest}/manifest.json"
    echo "    wrote: manifest.json"
  fi
  echo ""
done

# ── Summary ──────────────────────────────────────────────────────────────────
echo "══════════════════════════════════════════════════════"
echo "  Files copied : ${copied}"
echo "  Files skipped: ${skipped} (already in sync)"
echo "══════════════════════════════════════════════════════"
echo ""

if [[ "$DRY_RUN" -eq 0 ]]; then
  echo "Sync complete."
else
  echo "Dry-run complete — no files written."
fi
