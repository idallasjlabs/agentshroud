#!/usr/bin/env bash
# session-prompt-setup.sh
#
# Inject or remove a project-specific SESSION_PROMPT.md into all three LLM
# context files (CLAUDE.md, .gemini/GEMINI.md, .codex/AGENTS.md).
#
# Usage:
#   session-prompt-setup.sh [OPTIONS] [PROMPT_FILE]
#
# Options:
#   --remove        Strip injected session prompt from all target files
#   --dry-run, -n   Preview changes without modifying files
#   --help,    -h   Show this help and exit
#
# Prompt file resolution (first match wins):
#   1. CLI argument
#   2. $SESSION_PROMPT_FILE env var
#   3. SESSION_PROMPT.md in repo root (cwd)
#   4. .llm_settings/SESSION_PROMPT.md in repo root (cwd)
#
# Idempotent: safe to run multiple times. Uses HTML comment sentinels to
# delimit the injected block, stripping any prior block before re-injecting.
#
# Targets (relative to repo root / cwd):
#   Claude  → CLAUDE.md
#   Gemini  → .gemini/GEMINI.md
#   Codex   → .codex/AGENTS.md

set -euo pipefail

# ── Sentinels ──────────────────────────────────────────────────────────────────
readonly SENTINEL_BEGIN="<!-- ── SESSION PROMPT BEGIN ── -->"
readonly SENTINEL_END="<!-- ── SESSION PROMPT END ── -->"

# ── Target files (relative paths from repo root) ────────────────────────────
readonly TARGETS=(
    "CLAUDE.md"
    ".gemini/GEMINI.md"
    ".codex/AGENTS.md"
)

# ── State ──────────────────────────────────────────────────────────────────────
DRY_RUN=false
REMOVE=false
PROMPT_FILE_ARG=""

# ── Output helpers ─────────────────────────────────────────────────────────────
_ok()   { echo "   ✅ $*"; }
_warn() { echo "   ⚠️  $*"; }
_info() { echo "   ℹ️  $*"; }
_fail() { echo "❌ $*"; }
_hdr()  { echo "$*"; }

# ── Usage ──────────────────────────────────────────────────────────────────────
_usage() {
    cat <<'EOF'
Usage: session-prompt-setup.sh [OPTIONS] [PROMPT_FILE]

Inject a project-specific session prompt into all three LLM context files.

Options:
  --remove        Strip injected session prompt from all target files
  --dry-run, -n   Preview changes without modifying files
  --help,    -h   Show this help message

Arguments:
  PROMPT_FILE     Path to the session prompt Markdown file (optional)

Prompt file resolution order:
  1. CLI argument (PROMPT_FILE)
  2. SESSION_PROMPT_FILE environment variable
  3. SESSION_PROMPT.md in current directory (repo root)
  4. .llm_settings/SESSION_PROMPT.md in current directory

Target files (must already exist — llm-init creates them):
  CLAUDE.md
  .gemini/GEMINI.md
  .codex/AGENTS.md

Workflow:
  cd ~/repos/my-project
  llm-init                                     # Deploy LLM configs first
  # Create SESSION_PROMPT.md with project rules
  session-prompt-setup.sh                      # Inject into all 3 LLMs
  session-prompt-setup.sh --remove             # Strip session prompt
  session-prompt-setup.sh --dry-run            # Preview without modifying
EOF
}

# ── Argument parsing ────────────────────────────────────────────────────────────
_parse_args() {
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --remove)     REMOVE=true; shift ;;
            --dry-run|-n) DRY_RUN=true; shift ;;
            --help|-h)    _usage; exit 0 ;;
            -*)
                _fail "Unknown option: $1"
                echo "   Run with --help for usage."
                exit 1
                ;;
            *)
                if [[ -n "$PROMPT_FILE_ARG" ]]; then
                    _fail "Multiple positional arguments given. Expected at most one PROMPT_FILE."
                    exit 1
                fi
                PROMPT_FILE_ARG="$1"
                shift
                ;;
        esac
    done
}

# ── Prompt file resolution ──────────────────────────────────────────────────────
_resolve_prompt_file() {
    local repo_root="$1"

    # 1. CLI argument
    if [[ -n "$PROMPT_FILE_ARG" ]]; then
        if [[ -f "$PROMPT_FILE_ARG" ]]; then
            echo "$PROMPT_FILE_ARG"
            return 0
        else
            _fail "Prompt file not found: $PROMPT_FILE_ARG"
            exit 1
        fi
    fi

    # 2. Environment variable
    if [[ -n "${SESSION_PROMPT_FILE:-}" ]]; then
        if [[ -f "$SESSION_PROMPT_FILE" ]]; then
            echo "$SESSION_PROMPT_FILE"
            return 0
        else
            _fail "SESSION_PROMPT_FILE is set but file not found: $SESSION_PROMPT_FILE"
            exit 1
        fi
    fi

    # 3. Convention: SESSION_PROMPT.md in repo root
    if [[ -f "$repo_root/SESSION_PROMPT.md" ]]; then
        echo "$repo_root/SESSION_PROMPT.md"
        return 0
    fi

    # 4. Convention: .llm_settings/SESSION_PROMPT.md
    if [[ -f "$repo_root/.llm_settings/SESSION_PROMPT.md" ]]; then
        echo "$repo_root/.llm_settings/SESSION_PROMPT.md"
        return 0
    fi

    # Not found
    return 1
}

# ── Strip sentinel block from a file (cross-platform sed) ─────────────────────
# Removes everything from SENTINEL_BEGIN through SENTINEL_END (inclusive).
# If no sentinel block exists, file is unchanged.
_strip_block() {
    local file="$1"

    # Check whether the sentinel is actually present
    if ! grep -qF "$SENTINEL_BEGIN" "$file" 2>/dev/null; then
        return 0  # Nothing to strip
    fi

    local os_type
    os_type="$(uname -s)"

    if [[ "$DRY_RUN" == "true" ]]; then
        _info "Would strip session prompt block from: $file"
        return 0
    fi

    # sed -i behaves differently on macOS vs Linux:
    #   macOS (BSD sed): -i '' requires empty string arg
    #   Linux (GNU sed): -i alone is sufficient
    if [[ "$os_type" == "Darwin" ]]; then
        sed -i '' "/${SENTINEL_BEGIN}/,/${SENTINEL_END}/d" "$file"
    else
        sed -i "/${SENTINEL_BEGIN}/,/${SENTINEL_END}/d" "$file"
    fi
}

# ── Inject sentinel block into a file ─────────────────────────────────────────
# Algorithm: strip any existing block → append fresh block.
# A trailing newline is added before the sentinel block for clean separation.
_inject_block() {
    local file="$1"
    local prompt_content="$2"

    # Strip any prior block first (idempotency)
    _strip_block "$file"

    if [[ "$DRY_RUN" == "true" ]]; then
        _info "Would inject session prompt into: $file"
        _info "  (${#prompt_content} bytes of prompt content)"
        return 0
    fi

    # Append sentinel-wrapped block
    {
        printf '\n'
        printf '%s\n' "$SENTINEL_BEGIN"
        printf '%s\n' "$prompt_content"
        printf '%s\n' "$SENTINEL_END"
    } >> "$file"
}

# ── Remove session prompt from all targets ─────────────────────────────────────
_remove_all() {
    local repo_root="$1"
    local stripped=0

    _hdr "🧹 Removing session prompt from all LLM context files..."
    echo ""

    for rel in "${TARGETS[@]}"; do
        local target="$repo_root/$rel"

        if [[ ! -f "$target" ]]; then
            _warn "Target not found, skipping: $rel"
            continue
        fi

        if ! grep -qF "$SENTINEL_BEGIN" "$target" 2>/dev/null; then
            _info "No session prompt block found in: $rel"
            continue
        fi

        _strip_block "$target"

        if [[ "$DRY_RUN" == "true" ]]; then
            : # already messaged in _strip_block
        else
            _ok "Removed session prompt from: $rel"
            (( stripped++ )) || true
        fi
    done

    echo ""
    if [[ "$DRY_RUN" == "true" ]]; then
        _info "Dry run complete. No files modified."
    else
        _ok "Done. Removed from $stripped target(s)."
    fi
}

# ── Inject session prompt into all targets ─────────────────────────────────────
_inject_all() {
    local repo_root="$1"
    local prompt_file="$2"
    local prompt_content
    prompt_content="$(cat "$prompt_file")"
    local injected=0 skipped=0

    _hdr "💉 Injecting session prompt into all LLM context files..."
    _info "Prompt file: $prompt_file"
    echo ""

    for rel in "${TARGETS[@]}"; do
        local target="$repo_root/$rel"

        if [[ ! -f "$target" ]]; then
            _warn "Target not found, skipping: $rel"
            _warn "  (Run llm-init first to create LLM context files)"
            (( skipped++ )) || true
            continue
        fi

        _inject_block "$target" "$prompt_content"

        if [[ "$DRY_RUN" != "true" ]]; then
            _ok "Session prompt injected into: $rel"
            (( injected++ )) || true
        fi
    done

    echo ""
    if [[ "$DRY_RUN" == "true" ]]; then
        _info "Dry run complete. No files modified."
    else
        _ok "Done. Injected into $injected target(s). Skipped: $skipped."
    fi
}

# ── Main ───────────────────────────────────────────────────────────────────────
main() {
    _parse_args "$@"

    local repo_root
    repo_root="$(pwd)"

    if [[ "$DRY_RUN" == "true" ]]; then
        echo "⚠️  DRY RUN MODE — no files will be modified"
        echo ""
    fi

    # ── Remove mode ──
    if [[ "$REMOVE" == "true" ]]; then
        _remove_all "$repo_root"
        return 0
    fi

    # ── Inject mode ──
    _hdr "🔍 Resolving session prompt file..."
    echo ""

    local prompt_file=""
    if ! prompt_file="$(_resolve_prompt_file "$repo_root")"; then
        _warn "No session prompt file found. Checked:"
        [[ -n "$PROMPT_FILE_ARG" ]]          || _info "  CLI arg:               (none)"
        [[ -n "${SESSION_PROMPT_FILE:-}" ]]   || _info "  \$SESSION_PROMPT_FILE: (not set)"
        _info "  $repo_root/SESSION_PROMPT.md"
        _info "  $repo_root/.llm_settings/SESSION_PROMPT.md"
        echo ""
        _warn "Create a SESSION_PROMPT.md in your repo root and re-run."
        return 0
    fi

    _ok "Found: $prompt_file"

    # Guard: empty prompt file
    local prompt_content
    prompt_content="$(cat "$prompt_file")"
    if [[ -z "${prompt_content// /}" ]]; then
        _warn "Session prompt file is empty: $prompt_file"
        _warn "Add content and re-run."
        return 0
    fi

    echo ""
    _inject_all "$repo_root" "$prompt_file"
}

main "$@"
