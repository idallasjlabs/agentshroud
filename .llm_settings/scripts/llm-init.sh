#!/bin/bash
# llm-init.sh
#
# Deploy LLM AI tool configurations to a repository
# This sets up Claude Code (PRIMARY), Gemini CLI (SECONDARY),
# Codex CLI (TERTIARY), and GitHub Copilot CLI (QUATERNARY)
# Plus comprehensive security infrastructure
#
# Usage:
#   source llm-init.sh              # Load function into shell
#   llm-init                        # Deploy to current directory
#   llm-init /path/to/repo          # Deploy to specific directory
#   llm-init --dry-run              # Preview without making changes
#   llm-init -n /path/to/repo       # Dry run to specific directory
#   llm-init --jira fluenceenergy . # Pin repo to a specific Atlassian tenant
#   llm-init --jira all .           # Register all three Atlassian tenants

# zsh compatibility: avoid alias expansion conflict on function name
unalias llm-init 2>/dev/null || true

# ─────────────────────────────────────────────────────────────────────────────
# _llm_init_render_mcp [--dry-run]
#
# Reads .llm_settings/repo-tenants (in the current directory) and filters the
# three agent MCP registry files to retain only the selected atlassian-* entries.
# Non-atlassian entries (github, aws-api, xmind, etc.) are always preserved.
#
# Requires: jq (for .mcp.json / .gemini/settings.json); awk for .codex/config.toml.
# If jq is absent, JSON files are left unfiltered with a warning.
# ─────────────────────────────────────────────────────────────────────────────
_llm_init_render_mcp() {
    local _dry_run="${1:-false}"
    local _marker=".llm_settings/repo-tenants"

    # ── Resolve active MCP keys from marker file ─────────────────────
    local -a _active_keys=()
    if [ -f "$_marker" ]; then
        while IFS= read -r _line; do
            _line="${_line%%#*}"             # strip inline comments
            _line="${_line//[[:space:]]/}"   # strip whitespace
            [ -z "$_line" ] && continue
            case "$_line" in
                fluenceenergy)   _active_keys+=("atlassian-fluence") ;;
                therealidallasj) _active_keys+=("atlassian-idallasj") ;;
                agentshroudai)   _active_keys+=("atlassian-agentshroud") ;;
                *) echo "   ⚠️  [render-mcp] Unknown tenant '$_line' in $_marker — skipping" >&2 ;;
            esac
        done < "$_marker"
    fi
    [ ${#_active_keys[@]} -eq 0 ] && _active_keys=("atlassian-fluence")  # safe default

    local _keys_str="${_active_keys[*]}"

    if [ "$_dry_run" = "true" ]; then
        echo "   ℹ️  [dry-run] Would render MCP configs for: ${_keys_str}"
        return 0
    fi

    echo "   🎛️  Rendering MCP configs — active tenant(s): ${_keys_str}"

    # ── Filter JSON files with jq ─────────────────────────────────────
    if command -v jq >/dev/null 2>&1; then
        # Build a JSON array of the active atlassian-* keys for the jq filter
        local _keys_json
        _keys_json="$(printf '"%s",' "${_active_keys[@]}")"
        _keys_json="[${_keys_json%,}]"
        local _jq_filter
        _jq_filter='.mcpServers |= with_entries(select(
            (.key | startswith("atlassian-") | not) or
            (.key as $k | $keep | any(. == $k))
        ))'
        local _jf _tmp
        for _jf in ".mcp.json" ".gemini/settings.json"; do
            if [ -f "$_jf" ]; then
                _tmp="${_jf}.rnd.$$"
                if jq --argjson keep "$_keys_json" "$_jq_filter" "$_jf" > "$_tmp" 2>/dev/null; then
                    mv "$_tmp" "$_jf"
                    echo "      ✅ $_jf"
                else
                    rm -f "$_tmp"
                    echo "   ⚠️  [render-mcp] jq filter failed for $_jf — file unchanged" >&2
                fi
            fi
        done
    else
        echo "   ⚠️  [render-mcp] jq not found — .mcp.json and .gemini/settings.json unfiltered" >&2
        echo "   ⚠️              Install jq for full per-tenant filtering" >&2
    fi

    # ── Filter TOML file with awk (POSIX, always available) ──────────
    local _tf=".codex/config.toml"
    if [ -f "$_tf" ]; then
        local _tmp
        _tmp="${_tf}.rnd.$$"
        awk -v keep="$_keys_str" '
            BEGIN {
                n = split(keep, arr, " ")
                for (i = 1; i <= n; i++) keep_set[arr[i]] = 1
                in_skip = 0
            }
            /^\[mcp_servers\.atlassian-[A-Za-z_-]+\]/ {
                key = $0
                sub(/^\[mcp_servers\./, "", key)
                sub(/\].*$/, "", key)
                in_skip = (key in keep_set) ? 0 : 1
                if (!in_skip) print
                next
            }
            /^\[/ {
                in_skip = 0
                print
                next
            }
            !in_skip { print }
        ' "$_tf" > "$_tmp" && mv "$_tmp" "$_tf" && echo "      ✅ $_tf" || {
            rm -f "$_tmp"
            echo "   ⚠️  [render-mcp] awk filter failed for $_tf — file unchanged" >&2
        }
    fi
}

# ─────────────────────────────────────────────────────────────────────────────
# _llm_init_merge_claude_md <src> <tgt> <dry_run>
#
# Smart CLAUDE.md deployment:
#   - No target       → deploy full template (as before)
#   - Has markers     → replace only the llm-init block, preserve repo sections
#   - No markers      → preserve entirely (repo owns its own CLAUDE.md)
# ─────────────────────────────────────────────────────────────────────────────
_llm_init_merge_claude_md() {
    local _src="$1"
    local _tgt="$2"
    local _dry_run="${3:-false}"

    local _start_marker="## LLM OPERATING CONTEXT (llm-init)"
    local _end_marker="END OF LLM OPERATING CONTEXT (llm-init)"

    # Case 1: No target — deploy full template
    if [ ! -f "$_tgt" ]; then
        if $_dry_run; then
            echo "   ℹ️  [dry-run] Would deploy CLAUDE.md (new)"
        else
            cp "$_src" "$_tgt"
            echo "   ✅ CLAUDE.md deployed (new)"
        fi
        return 0
    fi

    # Case 2: Target exists WITHOUT markers — preserve entirely
    if ! grep -q "$_start_marker" "$_tgt"; then
        echo "   ✅ CLAUDE.md preserved (no llm-init markers; repo-specific file kept as-is)"
        return 0
    fi

    # Case 3: Target exists WITH markers — replace only the llm-init block
    if ! grep -q "$_start_marker" "$_src"; then
        echo "   ⚠️  Source CLAUDE.md missing llm-init markers; skipping merge"
        return 1
    fi

    if $_dry_run; then
        echo "   ℹ️  [dry-run] Would update llm-init block in existing CLAUDE.md (repo sections preserved)"
        return 0
    fi

    # Line-number-based extraction (portable: macOS + Linux)
    local _tgt_start _tgt_end _src_start _src_end
    _tgt_start=$(grep -n "$_start_marker" "$_tgt" | head -1 | cut -d: -f1)
    _tgt_end=$(grep -n "$_end_marker"   "$_tgt" | head -1 | cut -d: -f1)
    _src_start=$(grep -n "$_start_marker" "$_src" | head -1 | cut -d: -f1)
    _src_end=$(grep -n "$_end_marker"   "$_src" | head -1 | cut -d: -f1)

    # The ── ruler line before start marker and after end marker belong to the block
    local _tgt_block_start=$(( _tgt_start - 1 ))
    local _tgt_block_end=$(( _tgt_end + 1 ))
    local _src_block_start=$(( _src_start - 1 ))
    local _src_block_end=$(( _src_end + 1 ))

    local _tmpfile
    _tmpfile="$(mktemp "${_tgt}.merge.XXXXXX")"

    {
        head -n $(( _tgt_block_start - 1 )) "$_tgt"
        sed -n "${_src_block_start},${_src_block_end}p" "$_src"
        tail -n +$(( _tgt_block_end + 1 )) "$_tgt"
    } > "$_tmpfile"

    mv "$_tmpfile" "$_tgt"
    echo "   ✅ CLAUDE.md updated (llm-init block refreshed, repo-specific sections preserved)"
}

llm-init() {
    # ── Argument Parsing ───────────────────────────────────────────
    local dry_run=false target_dir="."
    local -a jira_tenants=()
    while [[ $# -gt 0 ]]; do
        case "$1" in
            --dry-run|-n) dry_run=true; shift ;;
            --jira)
                shift
                case "${1:-}" in
                    fluenceenergy|therealidallasj|agentshroudai)
                        jira_tenants+=("$1") ;;
                    all)
                        jira_tenants+=("fluenceenergy" "therealidallasj" "agentshroudai") ;;
                    "")
                        echo "llm-init: --jira requires a value" >&2
                        echo "          valid: fluenceenergy | therealidallasj | agentshroudai | all" >&2
                        return 2 ;;
                    *)
                        echo "llm-init: unknown --jira value: '$1'" >&2
                        echo "          valid: fluenceenergy | therealidallasj | agentshroudai | all" >&2
                        return 2 ;;
                esac
                shift ;;
            --help|-h)
                echo "Usage: llm-init [--dry-run|-n] [--jira <tenant>]... [--help|-h] [target_directory]"
                echo ""
                echo "  --dry-run, -n          Preview changes without modifying anything"
                echo "  --jira <tenant>        Select Atlassian Jira tenant (repeatable):"
                echo "                           fluenceenergy   → fluenceenergy.atlassian.net (work)"
                echo "                           therealidallasj → idallasj.atlassian.net (personal)"
                echo "                           agentshroudai   → agentshroudai.atlassian.net (project)"
                echo "                           all             → register all three tenants"
                echo "                         Writes .llm_settings/repo-tenants (committed, per-repo)."
                echo "                         Omit to preserve existing selection; default: fluenceenergy."
                echo "  --help,    -h          Show this help message"
                echo "  target_directory       Directory to deploy to (default: .)"
                echo ""
                echo "  Note: filtering .mcp.json and .gemini/settings.json requires jq."
                return 0 ;;
            *) target_dir="$1"; shift ;;
        esac
    done

    local rsync_dry=""
    $dry_run && rsync_dry="--dry-run"
    $dry_run && echo "⚠️  DRY RUN MODE — no files will be modified" && echo ""

    # ── Platform Detection ─────────────────────────────────────────
    local os_type
    os_type="$(uname -s)"

    local pkg_manager="" pkg_install=""
    case "$os_type" in
        Darwin)
            command -v brew &>/dev/null && { pkg_manager="brew"; pkg_install="brew install"; } ;;
        Linux)
            if   command -v apt-get &>/dev/null; then pkg_manager="apt";    pkg_install="sudo apt-get install -y"
            elif command -v dnf     &>/dev/null; then pkg_manager="dnf";    pkg_install="sudo dnf install -y"
            elif command -v yum     &>/dev/null; then pkg_manager="yum";    pkg_install="sudo yum install -y"
            elif command -v pacman  &>/dev/null; then pkg_manager="pacman"; pkg_install="sudo pacman -S --noconfirm"
            elif command -v brew    &>/dev/null; then pkg_manager="brew";   pkg_install="brew install"
            fi ;;
    esac

    # ── Tool Path Resolution ───────────────────────────────────────
    local uvx_path="" npx_path=""
    command -v uvx &>/dev/null && uvx_path="$(command -v uvx)"
    command -v npx &>/dev/null && npx_path="$(command -v npx)"

    # Build platform-appropriate PATH for MCP env blocks
    local mcp_path="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    case "$os_type" in
        Darwin) [ -d "/opt/homebrew/bin" ] && mcp_path="/opt/homebrew/bin:$mcp_path" ;;
        Linux)
            [ -d "$HOME/.local/bin" ] && mcp_path="$HOME/.local/bin:$mcp_path"
            [ -d "$HOME/.cargo/bin" ] && mcp_path="$HOME/.cargo/bin:$mcp_path" ;;
    esac

    # ── Source Directory Resolution ────────────────────────────────
    local source_dir=""

    # 1. Explicit env var override
    if [ -n "${LLM_SETTINGS_DIR:-}" ] && [ -d "$LLM_SETTINGS_DIR" ]; then
        source_dir="$LLM_SETTINGS_DIR"
    fi

    # 2. Script self-location (resolve BASH_SOURCE[0] up two levels)
    if [ -z "$source_dir" ] && [ -n "${BASH_SOURCE[0]:-}" ]; then
        local _script="${BASH_SOURCE[0]}"
        # Resolve symlinks cross-platform
        if [ "$os_type" = "Darwin" ]; then
            # macOS: no readlink -f; manual loop
            local _link
            while [ -L "$_script" ]; do
                _link="$(readlink "$_script")"
                case "$_link" in
                    /*) _script="$_link" ;;
                    *)  _script="$(dirname "$_script")/$_link" ;;
                esac
            done
        else
            _script="$(readlink -f "$_script" 2>/dev/null || echo "$_script")"
        fi
        local _candidate
        _candidate="$(cd "$(dirname "$_script")/../.." 2>/dev/null && pwd)"
        # Guard: if the candidate equals the current working directory, it is likely
        # a deployed target repo (sourced via relative path), not the llm_settings
        # source.  Skip BASH_SOURCE resolution and fall through to well-known paths.
        local _cwd
        _cwd="$(pwd)"
        if [ "$_candidate" != "$_cwd" ] && \
           [ -d "${_candidate}/.claude" ] && \
           { [ -d "${_candidate}/.llm_settings" ] || [ -d "${_candidate}/llm_settings" ]; }; then
            source_dir="$_candidate"
        fi
    fi

    # 3. Well-known paths
    if [ -z "$source_dir" ]; then
        local _wk
        for _wk in \
            "$HOME/Development/llm_settings" \
            "$HOME/Development/LLM_Settings" \
            "$HOME/dev/llm_settings" \
            "$HOME/repos/llm_settings"; do
            if [ -d "${_wk}/.claude" ] && { [ -d "${_wk}/.llm_settings" ] || [ -d "${_wk}/llm_settings" ]; }; then
                source_dir="$_wk"
                break
            fi
        done
    fi

    # 4. Fail with clear message
    if [ -z "$source_dir" ]; then
        echo "❌ Error: Cannot locate llm_settings source directory."
        echo "   Set the LLM_SETTINGS_DIR environment variable to the repo root."
        echo "   Example: export LLM_SETTINGS_DIR=\$HOME/Development/llm_settings"
        return 1
    fi

    # Resolve canonical LLM settings source directory (.llm_settings preferred, llm_settings legacy fallback)
    local llm_settings_src=""
    if [ -d "$source_dir/.llm_settings" ]; then
        llm_settings_src="$source_dir/.llm_settings"
    elif [ -d "$source_dir/llm_settings" ]; then
        llm_settings_src="$source_dir/llm_settings"
    fi

    # ── Install Hint Helper ────────────────────────────────────────
    # Called from within llm-init(); sees $pkg_manager via bash dynamic scoping.
    _install_hint() {
        local tool="$1"
        case "$tool" in
            uv)
                case "$pkg_manager" in
                    brew) echo "brew install uv" ;;
                    *)    echo "curl -LsSf https://astral.sh/uv/install.sh | sh" ;;
                esac ;;
            gh)
                case "$pkg_manager" in
                    brew)    echo "brew install gh" ;;
                    apt)     echo "sudo apt install gh" ;;
                    dnf|yum) echo "sudo dnf install gh" ;;
                    *)       echo "https://cli.github.com" ;;
                esac ;;
            awscli)
                case "$pkg_manager" in
                    brew)    echo "brew install awscli" ;;
                    apt)     echo "sudo apt install awscli" ;;
                    dnf|yum) echo "sudo dnf install awscli" ;;
                    *)       echo "https://aws.amazon.com/cli/" ;;
                esac ;;
            gitleaks)
                case "$pkg_manager" in
                    brew) echo "brew install gitleaks" ;;
                    *)    echo "go install github.com/gitleaks/gitleaks/v8@latest  (or https://github.com/gitleaks/gitleaks#installing)" ;;
                esac ;;
            git-secrets)
                case "$pkg_manager" in
                    brew) echo "brew install git-secrets" ;;
                    *)    echo "https://github.com/awslabs/git-secrets#installing-git-secrets" ;;
                esac ;;
            direnv)
                case "$pkg_manager" in
                    brew)    echo "brew install direnv" ;;
                    apt)     echo "sudo apt install direnv" ;;
                    dnf|yum) echo "sudo dnf install direnv" ;;
                    *)       echo "https://direnv.net/docs/installation.html" ;;
                esac ;;
            rsync)
                case "$pkg_manager" in
                    brew)    echo "brew install rsync" ;;
                    apt)     echo "sudo apt-get install -y rsync" ;;
                    dnf|yum) echo "sudo dnf install rsync" ;;
                    pacman)  echo "sudo pacman -S --noconfirm rsync" ;;
                    *)       echo "install rsync via your system package manager" ;;
                esac ;;
        esac
    }

    echo "🚀 Deploying LLM AI tool configurations..."
    echo "   Platform: $os_type (${pkg_manager:-no package manager detected})"
    echo "   uvx:      ${uvx_path:-not found}"
    echo "   Source:   $source_dir"
    echo "   Target:   $target_dir"
    echo "   Mode:     Synchronize (add new, update existing, remove obsolete)"
    echo ""

    # Verify source directory exists
    if [ ! -d "$source_dir" ]; then
        echo "❌ Error: Source directory not found: $source_dir"
        return 1
    fi

    # Create target directory if it doesn't exist
    if [ ! -d "$target_dir" ]; then
        echo "❌ Error: Target directory not found: $target_dir"
        return 1
    fi

    # Check for rsync (required for synchronization)
    if ! command -v rsync &> /dev/null; then
        echo "❌ Error: rsync not found (required for synchronization)"
        echo "   Install with: $(_install_hint rsync)"
        return 1
    fi

    # Navigate to target directory
    cd "$target_dir" || return 1

    # Migration: Clean up old deployment structure
    echo "🧹 Checking for old deployment structure..."
    local cleaned=false

    # Old files/directories to remove
    local old_items=(
        "github-mcp-server"
        "AI_TOOLS_CONFIGURATION_GUIDE.md"
        "CONFIGURATION_SUMMARY.md"
        "MCP_README.md"
        "MCP_ADDITIONAL_SERVICES.md"
        "GEMINI.md"
        ".llm_env_example"
        "new-skills"
        "llm_settings"
        # Stale nested scope copies — created when llm-init was previously run
        # on the llm_settings repo itself. These must not exist in target repos.
        ".llm_settings/scripts/.claude"
        ".llm_settings/scripts/.gemini"
        ".llm_settings/scripts/.codex"
        ".llm_settings/scripts/.github"
        ".llm_settings/scripts/.mcp.json"
        ".llm_settings/scripts/.llm_settings"
    )

    for item in "${old_items[@]}"; do
        if [ -e "$item" ]; then
            if git ls-files --error-unmatch "$item" >/dev/null 2>&1; then
                echo "   🗑️  Removing tracked: $item"
                $dry_run || git rm -rf "$item" 2>/dev/null
                cleaned=true
            elif [ -d "$item" ]; then
                echo "   🗑️  Removing directory: $item"
                $dry_run || rm -rf "$item"
                cleaned=true
            elif [ -f "$item" ]; then
                echo "   🗑️  Removing file: $item"
                $dry_run || rm -f "$item"
                cleaned=true
            fi
        fi
    done

    # Glob-safe cleanup for new-skills-*.tgz — use find to avoid zsh "no matches found" error
    while IFS= read -r _tgz; do
        echo "   🗑️  Removing file: $_tgz"
        $dry_run || rm -f "$_tgz"
        cleaned=true
    done < <(find "$target_dir" -maxdepth 1 -name 'new-skills-*.tgz' -type f 2>/dev/null)

    if [ "$cleaned" = true ]; then
        echo "   ✅ Old deployment cleaned up"
    else
        echo "   ✅ No old deployment found (clean target)"
    fi
    echo ""

    # Check prerequisites
    echo "📋 Checking prerequisites..."
    echo ""

    # Check for uvx (required for AWS MCP)
    if [ -n "$uvx_path" ]; then
        echo "   ✅ uvx found at $uvx_path"
    else
        echo "   ⚠️  uvx not found - AWS MCP will not work"
        echo "      Install with: $(_install_hint uv)"
    fi

    # Check for gh CLI (helpful for GitHub MCP)
    if command -v gh &> /dev/null; then
        echo "   ✅ gh CLI found"
    else
        echo "   ⚠️  gh CLI not found - GitHub MCP token setup may be manual"
        echo "      Install with: $(_install_hint gh)"
    fi

    # Check for AWS CLI
    if command -v aws &> /dev/null; then
        echo "   ✅ aws CLI found"
    else
        echo "   ⚠️  aws CLI not found - AWS MCP requires AWS credentials"
        echo "      Install with: $(_install_hint awscli)"
    fi

    # Check for git security tools
    if command -v gitleaks &> /dev/null; then
        echo "   ✅ gitleaks found"
    else
        echo "   ⚠️  gitleaks not found"
        echo "      Install with: $(_install_hint gitleaks)"
    fi

    if command -v git-secrets &> /dev/null; then
        echo "   ✅ git-secrets found"
    else
        echo "   ⚠️  git-secrets not found"
        echo "      Install with: $(_install_hint git-secrets)"
    fi

    # Check for pre-commit framework
    if command -v pre-commit &> /dev/null; then
        echo "   ✅ pre-commit found"
    else
        echo "   ⚠️  pre-commit not found - Install with: pip install pre-commit"
        echo "      (Will fall back to manual git hooks)"
    fi

    # Check for direnv
    if command -v direnv &> /dev/null; then
        echo "   ✅ direnv found"
    else
        echo "   ⚠️  direnv not found"
        echo "      Install with: $(_install_hint direnv)"
        echo "      (Recommended for secure environment variables)"
    fi
    echo ""

    # ── Jira Tenant Marker File ────────────────────────────────────
    echo "🎯 Jira Tenant Selection"
    local _marker_file=".llm_settings/repo-tenants"
    if [ ${#jira_tenants[@]} -gt 0 ]; then
        # Deduplicate while preserving order
        local -a _deduped=()
        local _seen=""
        for _t in "${jira_tenants[@]}"; do
            if [[ "$_seen" != *"|${_t}|"* ]]; then
                _deduped+=("$_t")
                _seen="${_seen}|${_t}|"
            fi
        done
        if ! $dry_run; then
            mkdir -p .llm_settings
            {
                printf '# llm-init Jira tenant selection — generated %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
                printf '# Accepted values: fluenceenergy | therealidallasj | agentshroudai\n'
                printf '# Change with:  llm-init --jira <tenant> .\n'
                printf '%s\n' "${_deduped[@]}"
            } > "$_marker_file"
            echo "   📌 Set tenant(s): ${_deduped[*]} → $_marker_file"
        else
            echo "   ℹ️  [dry-run] Would write $_marker_file: ${_deduped[*]}"
        fi
    elif [ ! -f "$_marker_file" ]; then
        if ! $dry_run; then
            mkdir -p .llm_settings
            {
                printf '# llm-init Jira tenant selection (default: fluenceenergy)\n'
                printf '# Accepted values: fluenceenergy | therealidallasj | agentshroudai\n'
                printf '# Change with:  llm-init --jira <tenant> .\n'
                printf 'fluenceenergy\n'
            } > "$_marker_file"
            echo "   📌 No --jira flag and no marker found — defaulting to: fluenceenergy"
        else
            echo "   ℹ️  [dry-run] Would write $_marker_file: fluenceenergy (default)"
        fi
    else
        local _current_tenants
        _current_tenants="$(grep -v '^#' "$_marker_file" | tr -d '[:space:]' | tr '\n' ' ' | sed 's/ $//')"
        echo "   📌 Preserving existing selection: ${_current_tenants:-fluenceenergy}"
    fi
    echo ""

    echo "📦 Copying configurations..."
    echo ""

    # 1. Claude Code (PRIMARY Developer)
    echo "1️⃣  Claude Code (PRIMARY)"
    if [ -d "$source_dir/.claude" ]; then
        rsync -a $rsync_dry --delete \
            --exclude='settings.local.json' \
            --exclude='*.local.*' \
            --exclude='.cache/' \
            --exclude='tmp/' \
            --exclude='logs/' \
            --exclude='.credentials.json' \
            --exclude='history.jsonl' \
            --exclude='debug/' \
            --exclude='file-history/' \
            --exclude='paste-cache/' \
            --exclude='session-env/' \
            --exclude='shell-snapshots/' \
            --exclude='stats-cache.json' \
            --exclude='statsig/' \
            --exclude='todos/' \
            --exclude='agents/' \
            --exclude='skills/' \
            "$source_dir/.claude/" .claude/
        echo "   ✅ .claude/ synchronized (secrets preserved)"

        # Sync skills from canonical source (.llm_settings/skills/) into .claude/skills/
        if [ -d "$llm_settings_src/skills" ]; then
            local skill_count=0
            for skill_dir in "$llm_settings_src/skills"/*/; do
                local skill_name
                skill_name=$(basename "$skill_dir")
                if [ -f "$skill_dir/SKILL.md" ]; then
                    if ! $dry_run; then
                        mkdir -p ".claude/skills/$skill_name"
                        cp "$skill_dir/SKILL.md" ".claude/skills/$skill_name/SKILL.md"
                    fi
                    ((skill_count++))
                fi
            done
            echo "   ✅ .claude/skills/ synchronized ($skill_count skills from .llm_settings/skills/)"
        fi

        # Sync agents from canonical source (.llm_settings/agents/) into .claude/agents/
        if [ -d "$llm_settings_src/agents" ]; then
            $dry_run || mkdir -p .claude/agents
            local agent_count=0
            for agent_file in "$llm_settings_src/agents"/*.md; do
                [ -f "$agent_file" ] || continue
                $dry_run || cp "$agent_file" ".claude/agents/$(basename "$agent_file")"
                ((agent_count++))
            done
            echo "   ✅ .claude/agents/ synchronized ($agent_count agents from .llm_settings/agents/)"
        fi

        # Deploy ORCHESTRATOR.md
        if [ -f "$source_dir/.claude/ORCHESTRATOR.md" ]; then
            $dry_run || cp "$source_dir/.claude/ORCHESTRATOR.md" ".claude/ORCHESTRATOR.md"
            echo "   ✅ .claude/ORCHESTRATOR.md deployed"
        fi
    else
        echo "   ⚠️  .claude/ directory not found in source"
    fi

    if [ -f "$source_dir/CLAUDE.md" ]; then
        _llm_init_merge_claude_md "$source_dir/CLAUDE.md" "./CLAUDE.md" "$dry_run"
    else
        echo "   ⚠️  CLAUDE.md not found in source"
    fi

    echo ""

    # 2. Gemini CLI (SECONDARY Agent)
    echo "2️⃣  Gemini CLI (SECONDARY)"
    if [ -d "$source_dir/.gemini" ]; then
        rsync -a $rsync_dry --delete \
            --exclude='settings.local.json' \
            --exclude='*.local.*' \
            --exclude='.cache/' \
            --exclude='tmp/' \
            --exclude='logs/' \
            --exclude='agents/' \
            "$source_dir/.gemini/" .gemini/
        # Patch hardcoded macOS paths after sync (skip in dry-run)
        if ! $dry_run && [ -f ".gemini/settings.json" ] && [ -n "$uvx_path" ]; then
            sed -i.bak \
                -e "s|/opt/homebrew/bin/uvx|$uvx_path|g" \
                -e "s|/opt/homebrew/bin/npx|${npx_path:-/opt/homebrew/bin/npx}|g" \
                -e "s|/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin|$mcp_path|g" \
                .gemini/settings.json
            rm -f .gemini/settings.json.bak
        fi
        # Sync agents from canonical source (.llm_settings/skills/) into .gemini/agents/
        if [ -d "$llm_settings_src/skills" ]; then
            $dry_run || mkdir -p .gemini/agents
            local gemini_skill_count=0
            for skill_dir in "$llm_settings_src/skills"/*/; do
                local skill_name
                skill_name=$(basename "$skill_dir")
                if [ -f "$skill_dir/SKILL.md" ]; then
                    $dry_run || cp "$skill_dir/SKILL.md" ".gemini/agents/$skill_name.md"
                    ((gemini_skill_count++))
                fi
            done
            # Also sync agents from .llm_settings/agents/ into .gemini/agents/
            if [ -d "$llm_settings_src/agents" ]; then
                for agent_file in "$llm_settings_src/agents"/*.md; do
                    [ -f "$agent_file" ] || continue
                    $dry_run || cp "$agent_file" ".gemini/agents/$(basename "$agent_file")"
                done
            fi
            echo "   ✅ .gemini/ synchronized ($gemini_skill_count skills + agents from .llm_settings/, MCP configured)"
        else
            local gemini_agents
            gemini_agents=$(ls .gemini/agents/*.md 2>/dev/null | wc -l | tr -d ' ')
            echo "   ✅ .gemini/ synchronized ($gemini_agents agents, MCP configured)"
        fi
    else
        echo "   ⚠️  .gemini/ directory not found in source"
    fi
    echo ""

    # 3. Codex CLI (TERTIARY Agent)
    echo "3️⃣  Codex CLI (TERTIARY)"
    if [ -d "$source_dir/.codex" ]; then
        rsync -a $rsync_dry --delete \
            --exclude='config.local.toml' \
            --exclude='*.local.*' \
            --exclude='.cache/' \
            --exclude='tmp/' \
            --exclude='logs/' \
            --exclude='agents/' \
            "$source_dir/.codex/" .codex/
        # Patch hardcoded macOS paths after sync (skip in dry-run)
        if ! $dry_run && [ -f ".codex/config.toml" ] && [ -n "$uvx_path" ]; then
            sed -i.bak \
                -e "s|/opt/homebrew/bin/uvx|$uvx_path|g" \
                -e "s|/opt/homebrew/bin/npx|${npx_path:-/opt/homebrew/bin/npx}|g" \
                .codex/config.toml
            rm -f .codex/config.toml.bak
        fi
        # Sync agents from canonical source (.llm_settings/skills/) into .codex/agents/
        if [ -d "$llm_settings_src/skills" ]; then
            $dry_run || mkdir -p .codex/agents
            local codex_skill_count=0
            for skill_dir in "$llm_settings_src/skills"/*/; do
                local skill_name
                skill_name=$(basename "$skill_dir")
                if [ -f "$skill_dir/SKILL.md" ]; then
                    $dry_run || cp "$skill_dir/SKILL.md" ".codex/agents/$skill_name.md"
                    ((codex_skill_count++))
                fi
            done
            # Also sync agents from .llm_settings/agents/ into .codex/agents/
            if [ -d "$llm_settings_src/agents" ]; then
                for agent_file in "$llm_settings_src/agents"/*.md; do
                    [ -f "$agent_file" ] || continue
                    $dry_run || cp "$agent_file" ".codex/agents/$(basename "$agent_file")"
                done
            fi
            echo "   ✅ .codex/ synchronized ($codex_skill_count skills + agents from .llm_settings/, MCP configured)"
        else
            local codex_agents
            codex_agents=$(ls .codex/agents/*.md 2>/dev/null | wc -l | tr -d ' ')
            echo "   ✅ .codex/ synchronized ($codex_agents agents, MCP configured)"
        fi
    else
        echo "   ⚠️  .codex/ directory not found in source"
    fi

    if [ -f "$source_dir/AGENTS.md" ]; then
        rsync -a $rsync_dry "$source_dir/AGENTS.md" .
        echo "   ✅ AGENTS.md synchronized"
    else
        echo "   ⚠️  AGENTS.md not found in source"
    fi
    echo ""

    # 4. GitHub Copilot CLI (QUATERNARY Agent)
    echo "4️⃣  GitHub Copilot CLI (QUATERNARY)"
    if [ -d "$source_dir/.github" ]; then
        # Only sync .github/agents, COPILOT_CLI_SETUP.md, and copilot-config.json.example
        # (Avoid overwriting repo's own .github/workflows, CODEOWNERS, etc.)
        if [ -d "$source_dir/.github/agents" ]; then
            $dry_run || mkdir -p .github/agents
            rsync -a $rsync_dry --delete \
                "$source_dir/.github/agents/" .github/agents/
            echo "   ✅ .github/agents/ synchronized"
        fi

        if [ -f "$source_dir/.github/COPILOT_CLI_SETUP.md" ]; then
            rsync -a $rsync_dry "$source_dir/.github/COPILOT_CLI_SETUP.md" .github/
            echo "   ✅ .github/COPILOT_CLI_SETUP.md synchronized"
        fi

        if [ -f "$source_dir/.github/copilot-config.json.example" ]; then
            rsync -a $rsync_dry "$source_dir/.github/copilot-config.json.example" .github/
            echo "   ✅ .github/copilot-config.json.example synchronized"
        fi
    else
        echo "   ⚠️  .github/ directory not found in source"
    fi
    echo ""

    # 5. MCP Configuration
    echo "5️⃣  MCP Servers"
    if [ -f "$source_dir/.mcp.json" ]; then
        rsync -a $rsync_dry "$source_dir/.mcp.json" .
        # Patch hardcoded macOS paths after sync (skip in dry-run)
        if ! $dry_run && [ -f ".mcp.json" ] && [ -n "$uvx_path" ]; then
            sed -i.bak \
                -e "s|/opt/homebrew/bin/uvx|$uvx_path|g" \
                -e "s|/opt/homebrew/bin/npx|${npx_path:-/opt/homebrew/bin/npx}|g" \
                -e "s|/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin|$mcp_path|g" \
                .mcp.json
            rm -f .mcp.json.bak
        fi
        echo "   ✅ .mcp.json synchronized"
    else
        echo "   ⚠️  .mcp.json not found in source"
    fi
    echo ""

    # 6. LLM Settings (all subdirectories synchronized recursively)
    echo "6️⃣  LLM Settings Directory"
    if [ -n "$llm_settings_src" ] && [ -d "$llm_settings_src" ]; then
        $dry_run || mkdir -p .llm_settings

        # Synchronize llm_settings with secrets/local files excluded
        rsync -a $rsync_dry --delete \
            --filter='include .env.example' \
            --filter='include .env.*.example' \
            --filter='include .llm_env_example' \
            --filter='exclude .env' \
            --filter='exclude .env.*' \
            --filter='exclude .llm_env' \
            --filter='exclude *.local.*' \
            --filter='protect .env' \
            --filter='protect .env.*' \
            --filter='protect .llm_env' \
            --filter='protect *.local.*' \
            --filter='exclude repo-tenants' \
            --filter='protect repo-tenants' \
            --exclude='.DS_Store' \
            --exclude='.cache/' \
            --exclude='tmp/' \
            --exclude='logs/' \
            --exclude='*token*' \
            --exclude='*secret*' \
            --exclude='*credential*' \
            --exclude='*password*' \
            --exclude='*.pem' \
            --exclude='*.key' \
            --exclude='mcp-servers/*/.claude' \
            --exclude='scripts/.claude/' \
            --exclude='scripts/.gemini/' \
            --exclude='scripts/.codex/' \
            --exclude='scripts/.github/' \
            --exclude='scripts/.mcp.json' \
            --exclude='scripts/.llm_settings/' \
            "$llm_settings_src/" .llm_settings/

        # Make scripts executable
        if ! $dry_run; then
            find .llm_settings/scripts -type f -name '*.sh' -exec chmod +x {} \; 2>/dev/null || true
            find .llm_settings/git-hooks -type f -exec chmod +x {} \; 2>/dev/null || true
            find .llm_settings/mcp-servers -type f -name '*.sh' -exec chmod +x {} \; 2>/dev/null || true
        fi

        echo "   ✅ .llm_settings/ synchronized (secrets preserved, scripts executable)"

        # Render per-repo MCP configs based on .llm_settings/repo-tenants
        _llm_init_render_mcp "$dry_run"
    else
        echo "   ⚠️  .llm_settings/ directory not found in source"
    fi

    # Enforce legacy -> dot-directory migration in target repo
    # (handles edge cases where legacy folder survives cleanup)
    if [ -d "llm_settings" ]; then
        if [ -d ".llm_settings" ]; then
            if [ -f "llm_settings/scripts/llm-init.sh" ] || [ -d "llm_settings/skills" ] || [ -d "llm_settings/agents" ]; then
                echo "   🧹 Removing legacy llm_settings/ (migrated to .llm_settings/)"
                $dry_run || rm -rf "llm_settings"
            fi
        else
            echo "   🔁 Migrating legacy llm_settings/ -> .llm_settings/"
            if $dry_run; then
                echo "   ℹ️  [dry-run] Would move llm_settings to .llm_settings"
            else
                mv "llm_settings" ".llm_settings"
            fi
        fi
    fi
    echo ""

    # 7. Git Security Configuration
    echo "7️⃣  Git Security Configuration"

    # Deploy .gitignore (augment if exists)
    if [ -f "$llm_settings_src/templates/.gitignore" ]; then
        if [ -f ".gitignore" ]; then
            if $dry_run; then
                echo "   ℹ️  [dry-run] Would merge missing patterns into existing .gitignore"
            else
                cat "$llm_settings_src/templates/.gitignore" >> .gitignore
                awk '!seen[$0]++' .gitignore > .gitignore.tmp && mv .gitignore.tmp .gitignore
                echo "   ✅ .gitignore augmented with missing template patterns"
            fi
        else
            rsync -a $rsync_dry "$llm_settings_src/templates/.gitignore" .
            echo "   ✅ .gitignore deployed from template"
        fi
    else
        echo "   ⚠️  .gitignore template not found in source"
    fi

    # Deploy .pre-commit-config.yaml (preserve existing if present)
    if [ -f "$llm_settings_src/templates/.pre-commit-config.yaml" ]; then
        if [ -f ".pre-commit-config.yaml" ]; then
            echo "   ✅ .pre-commit-config.yaml preserved (existing repo config kept)"
        else
            rsync -a $rsync_dry "$llm_settings_src/templates/.pre-commit-config.yaml" .
            echo "   ✅ .pre-commit-config.yaml deployed"
        fi
    else
        echo "   ⚠️  .pre-commit-config.yaml template not found in source"
    fi

    # Deploy .gitallowed (always augment if exists)
    if [ -f "$llm_settings_src/templates/.gitallowed" ]; then
        if [ -f ".gitallowed" ]; then
            if $dry_run; then
                echo "   ℹ️  [dry-run] Would merge template patterns into existing .gitallowed"
            else
                # Append template patterns if not already present
                cat "$llm_settings_src/templates/.gitallowed" >> .gitallowed
                # Remove duplicates while preserving comments
                awk '!seen[$0]++' .gitallowed > .gitallowed.tmp && mv .gitallowed.tmp .gitallowed
                echo "   ✅ .gitallowed merged with template"
            fi
        else
            rsync -a $rsync_dry "$llm_settings_src/templates/.gitallowed" .
            echo "   ✅ .gitallowed deployed from template"
        fi
    else
        echo "   ⚠️  .gitallowed template not found in source"
    fi

    # Deploy gitleaks.toml (augment if existing)
    if [ -f "$llm_settings_src/git-hooks/gitleaks.toml" ]; then
        if [ -f "gitleaks.toml" ]; then
            if $dry_run; then
                echo "   ℹ️  [dry-run] Would augment existing gitleaks.toml (non-destructive)"
            else
                if grep -q "path = \".llm_settings/git-hooks/gitleaks.toml\"" gitleaks.toml 2>/dev/null || grep -q "regexes = \\['REDACTED'\\]" gitleaks.toml 2>/dev/null; then
                    echo "   ✅ gitleaks.toml preserved (already contains llm_settings rule)"
                elif grep -q "^\\[extend\\]" gitleaks.toml 2>/dev/null; then
                    echo "   ⚠️  gitleaks.toml has [extend] already; skipped auto-merge to avoid breaking existing config"
                    echo "      Add manually: path = \".llm_settings/git-hooks/gitleaks.toml\" under [extend]"
                else
                    {
                        echo ""
                        echo "# Added by llm-init: extend with llm_settings defaults"
                        echo "[extend]"
                        echo "path = \".llm_settings/git-hooks/gitleaks.toml\""
                    } >> gitleaks.toml
                    echo "   ✅ gitleaks.toml augmented via [extend] path to .llm_settings/git-hooks/gitleaks.toml"
                fi
            fi
        else
            rsync -a $rsync_dry "$llm_settings_src/git-hooks/gitleaks.toml" .
            echo "   ✅ gitleaks.toml deployed (custom gitleaks config)"
        fi
    else
        echo "   ⚠️  gitleaks.toml not found in source"
    fi

    # Check if this is a git repository (handles both normal repos and git worktrees)
    if git rev-parse --git-dir > /dev/null 2>&1; then
        # Install pre-commit hooks if pre-commit is available
        if command -v pre-commit &> /dev/null && [ -f ".pre-commit-config.yaml" ]; then
            echo "   🔒 Installing pre-commit hooks..."
            if $dry_run; then
                echo "   ℹ️  [dry-run] Would install pre-commit hooks"
            else
                pre-commit install --install-hooks 2>/dev/null || pre-commit install

                # Create secrets baseline if detect-secrets is configured
                if grep -q "detect-secrets" ".pre-commit-config.yaml" 2>/dev/null; then
                    if command -v detect-secrets &> /dev/null; then
                        if [ ! -f ".secrets.baseline" ]; then
                            echo "   📊 Creating secrets baseline..."
                            detect-secrets scan > .secrets.baseline 2>/dev/null || true
                            echo "   ✅ .secrets.baseline created"
                        fi
                    fi
                fi

                echo "   ✅ Pre-commit hooks installed"

                # Optional: Run once to verify
                read -p "   Run pre-commit on all files now? [y/N] " -n 1 -r
                echo
                if [[ $REPLY =~ ^[Yy]$ ]]; then
                    echo "   🔍 Running pre-commit checks..."
                    pre-commit run --all-files || true
                    echo ""
                fi
            fi
        else
            # Fall back to manual git hooks
            if [ -f ".llm_settings/git-hooks/install.sh" ]; then
                echo "   🔒 Installing fallback git hooks..."
                if $dry_run; then
                    echo "   ℹ️  [dry-run] Would install fallback git hooks"
                else
                    chmod +x .llm_settings/git-hooks/install.sh
                    .llm_settings/git-hooks/install.sh
                    echo "   ✅ Fallback git hooks installed"
                fi
            else
                echo "   ⚠️  Git hooks installer not found"
            fi

            if ! command -v pre-commit &> /dev/null; then
                echo "   💡 Tip: Install pre-commit for better security"
                echo "      pip install pre-commit"
            fi
        fi
    else
        echo "   ⚠️  Not a git repository - hooks not installed"
        echo "      Run 'pre-commit install' or '.llm_settings/git-hooks/install.sh' after git init"
    fi
    echo ""

    # 8. Security Scripts & Audit
    echo "8️⃣  Security Setup"
    if [ -d ".llm_settings/scripts/security" ]; then
        echo "   ✅ Security scripts available:"
        echo "      - setup-direnv.sh      (secure environment variables)"
        echo "      - setup-pgpass.sh      (PostgreSQL passwords)"
        echo "      - security-audit.sh    (scan for secrets in history)"
        echo "      - quick-setup.sh       (run all security setup)"

        # Optionally run security audit
        if git rev-parse --git-dir > /dev/null 2>&1; then
            if $dry_run; then
                echo "   ℹ️  [dry-run] Would prompt: Run security audit now?"
            else
                read -p "   Run security audit now? [y/N] " -n 1 -r
                echo
                if [[ $REPLY =~ ^[Yy]$ ]]; then
                    echo ""
                    .llm_settings/scripts/security/security-audit.sh
                    echo ""
                fi
            fi
        fi
    else
        echo "   ⚠️  Security scripts not found in source"
    fi
    echo ""

    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "✅ LLM AI tool configurations synchronized successfully!"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "🔄 Synchronization behavior:"
    echo "   ✅ Added new files from source"
    echo "   ✅ Updated existing files to match source"
    echo "   ✅ Removed obsolete files (no longer in source)"
    echo "   ✅ Preserved secrets (.env, *.local.*, credentials, tokens)"
    echo ""
    echo "📁 Files synchronized:"
    echo "   - .claude/                      (agents, skills, hooks, settings)"
    echo "   - .gemini/                      (agents, settings.json, GEMINI.md)"
    echo "   - .codex/                       (agents, config.toml)"
    echo "   - .github/agents/               (custom agent profiles)"
    echo "   - .mcp.json                     (MCP servers for Claude Code)"
    echo "   - .gitignore                    (comprehensive security template)"
    echo "   - .pre-commit-config.yaml       (secret detection framework)"
    echo "   - .gitallowed                   (false positive patterns)"
    if [ -f "$(git rev-parse --git-common-dir 2>/dev/null)/hooks/pre-commit" ]; then
        echo "   - .git/hooks/pre-commit         (secret scanning protection)"
    fi
    echo "   - CLAUDE.md                     (primary developer context)"
    echo "   - AGENTS.md                     (secondary/tertiary agent context)"
    echo "   - .llm_settings/                 (organized LLM configuration)"
    echo "     ├── agents/                   (52 flat agents — all CLIs)"
    echo "     ├── ci-cd/                    (CI/CD pipeline definitions)"
    echo "     ├── docs/                     (documentation files)"
    echo "     ├── env/                      (environment templates)"
    echo "     ├── git-hooks/                (fallback security hooks)"
    echo "     ├── mcp-servers/              (GitHub & Atlassian MCP servers)"
    echo "     ├── podcast/                  (podcast pipeline definitions)"
    echo "     ├── scripts/                  (deployment & security scripts)"
    echo "     │   ├── llm-init.sh"
    echo "     │   ├── ci_self_heal.sh"
    echo "     │   ├── run_agents.sh"
    echo "     │   └── security/             (direnv, pgpass, audit)"
    echo "     ├── skills/                   (54 skill definitions — all CLIs)"
    echo "     ├── sre/                      (SRE runbooks and definitions)"
    echo "     ├── templates/                (.gitignore, pre-commit, .gitallowed)"
    echo "     └── WORKFLOW.md               (multi-agent workflow guide)"
    echo ""
    echo "📝 Next steps:"
    echo "   1. 📖 Read: .llm_settings/docs/SECURITY_GUIDE.md"
    echo "   2. 📖 Read: .llm_settings/docs/CONFIGURATION_SUMMARY.md"
    echo "   3. 🔒 Security: .llm_settings/scripts/security/quick-setup.sh"
    echo "   4. 🔌 MCP GitHub: cp .llm_settings/mcp-servers/github/.env.example .env"
    echo "   5. 🔌 MCP User: .llm_settings/scripts/setup-mcp-user.sh (global config)"
    echo "   6. ☁️  AWS: export AWS_PROFILE=default AWS_REGION=us-east-1"
    echo "   7. 🤖 Test tools:"
    echo "      - claude      (PRIMARY developer)"
    echo "      - gemini      (SECONDARY agent)"
    echo "      - codex       (TERTIARY agent)"
    echo "      - copilot     (QUATERNARY agent)"
    echo ""
    echo "🔌 MCP Servers configured:"
    echo "   - GitHub          (.llm_settings/mcp-servers/github/)"
    echo "   - Atlassian       (.llm_settings/mcp-servers/atlassian/)"
    echo "   - AWS API         (via uvx awslabs.aws-api-mcp-server)"
    echo "   - XMind Generator (via npx xmind-generator-mcp)"
    echo ""
    echo "   📝 Project-level: .mcp.json (works in this repo only)"
    echo "   💡 User-level: Run setup-mcp-user.sh to enable 'claude mcp list'"
    echo ""

    # Offer to configure user-level MCP servers
    if [ -f ".llm_settings/scripts/setup-mcp-user.sh" ]; then
        if $dry_run; then
            echo "   ℹ️  [dry-run] Would prompt: Configure MCP servers globally?"
        else
            read -p "   Configure MCP servers globally (user-level)? [y/N] " -n 1 -r
            echo
            if [[ $REPLY =~ ^[Yy]$ ]]; then
                echo ""
                .llm_settings/scripts/setup-mcp-user.sh
                echo ""
            else
                echo "   ⏭️  Skipped user-level MCP setup"
                echo "      Run later with: .llm_settings/scripts/setup-mcp-user.sh"
                echo ""
            fi
        fi
    fi

    # Security status
    echo "🔒 Security features installed:"
    if command -v pre-commit &> /dev/null && [ -f ".pre-commit-config.yaml" ]; then
        echo "   ✅ Pre-commit framework (gitleaks + detect-secrets + validators)"
        echo "   ✅ Comprehensive .gitignore (200+ patterns)"
        echo "   ✅ .gitallowed (false positive patterns)"
        echo "   ✅ Secret scanning on every commit"
        echo ""
        echo "   💡 Pre-commit commands:"
        echo "      pre-commit run --all-files    # Run all hooks manually"
        echo "      pre-commit autoupdate         # Update hook versions"
        echo "      git commit --no-verify        # Skip hooks (emergency only)"
    elif [ -f "$(git rev-parse --git-common-dir 2>/dev/null)/hooks/pre-commit" ]; then
        echo "   ✅ Git hooks (gitleaks + git-secrets)"
        echo "   ✅ Comprehensive .gitignore (200+ patterns)"
        echo "   ✅ .gitallowed (false positive patterns)"
        echo "   ✅ Secret scanning on every commit"
        echo ""
        echo "   💡 Upgrade to pre-commit framework:"
        echo "      pip install pre-commit"
        echo "      pre-commit install"
    else
        echo "   ⚠️  No hooks installed (not a git repository)"
    fi
    echo ""

    echo "🧪 Test git security:"
    echo "   echo 'password=secret123' > test.txt"
    echo "   git add test.txt"
    echo "   git commit -m 'test'  # Should be blocked!"
    echo "   rm test.txt"
    echo ""
    echo "🔒 Security best practices:"
    echo "   ✅ Never commit .env files (use direnv instead)"
    echo "   ✅ Never commit API keys (use AWS Secrets Manager)"
    echo "   ✅ Never commit passwords (use ~/.pgpass for PostgreSQL)"
    echo "   ✅ Run security audit periodically"
    echo "   ✅ Review all files before committing"
    echo ""
    echo "📚 Documentation:"
    echo "   - Security Guide:     .llm_settings/docs/SECURITY_GUIDE.md"
    echo "   - AI Tools Guide:     .llm_settings/docs/AI_TOOLS_CONFIGURATION_GUIDE.md"
    echo "   - Quick Reference:    .llm_settings/docs/CONFIGURATION_SUMMARY.md"
    echo ""
}

# Export function if script is sourced
if [[ "${BASH_SOURCE[0]}" != "${0}" ]]; then
    export -f llm-init
    export -f _llm_init_render_mcp
    echo "✅ llm-init function loaded"
    echo "   Usage: llm-init [--dry-run] [--jira <tenant>] [target_directory]"
    echo "   Jira tenants: fluenceenergy | therealidallasj | agentshroudai | all"
fi

# If script is executed (not sourced), run the function
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    llm-init "$@"
fi
