#!/bin/bash
# sync-version.sh — Keep AgentShroud's own product version in sync everywhere
# it's mirrored, from the one place a human actually edits it.
#
# Source of truth: gateway/__init__.py's __version__.
#
# Mirrors kept in sync:
#   - gateway/pyproject.toml            ("version = ...")
#   - docker/versions.env               (AGENTSHROUD_VERSION=..., consumed as a
#                                         Docker build ARG for the version LABEL
#                                         on gateway/openclaw/hermes images, and
#                                         as a runtime env var so voice_gateway
#                                         and the SOC service list report the
#                                         real version instead of a stale label
#                                         or, for voice, an ungrounded guess)
#
# Usage:
#   scripts/sync-version.sh            Write the current __version__ into every
#                                       mirror. Safe to run any time; a no-op if
#                                       everything already matches.
#   scripts/sync-version.sh --check    Exit 1 if any mirror is out of sync,
#                                       without writing anything. Used by
#                                       .github/workflows/release.yml so a
#                                       release cannot ship with drifted
#                                       version strings.
#
# This script does NOT touch docker/.env — that file is gitignored/secrets-
# adjacent and out of scope here; docker/versions.env is the committed,
# reviewed mirror scripts/asb and docker-compose builds actually consume.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

INIT_PY="$REPO_ROOT/gateway/__init__.py"
PYPROJECT="$REPO_ROOT/gateway/pyproject.toml"
VERSIONS_ENV="$REPO_ROOT/docker/versions.env"

CHECK_ONLY=0
if [ "${1:-}" = "--check" ]; then
    CHECK_ONLY=1
fi

VERSION="$(sed -n 's/^__version__ = "\(.*\)"$/\1/p' "$INIT_PY")"
if [ -z "$VERSION" ]; then
    echo "ERROR: could not parse __version__ out of $INIT_PY" >&2
    exit 1
fi

echo "==> Source of truth: gateway/__init__.py __version__ = $VERSION"

drift=0

check_or_fix() {
    local label="$1" file="$2" pattern="$3" replacement="$4"
    if grep -qE "$pattern" "$file" 2>/dev/null; then
        # Already matches — nothing to do.
        return 0
    fi
    drift=1
    if [ "$CHECK_ONLY" -eq 1 ]; then
        echo "DRIFT: $label ($file) does not match $VERSION"
        return 0
    fi
    sed -i.bak "$replacement" "$file" && rm -f "$file.bak"
    echo "FIXED: $label ($file) -> $VERSION"
}

check_or_fix "gateway/pyproject.toml version" "$PYPROJECT" \
    "^version = \"$VERSION\"$" \
    "s/^version = \".*\"\$/version = \"$VERSION\"/"

check_or_fix "docker/versions.env AGENTSHROUD_VERSION" "$VERSIONS_ENV" \
    "^AGENTSHROUD_VERSION=$VERSION$" \
    "s/^AGENTSHROUD_VERSION=.*\$/AGENTSHROUD_VERSION=$VERSION/"

if [ "$CHECK_ONLY" -eq 1 ]; then
    if [ "$drift" -eq 1 ]; then
        echo ""
        echo "Version drift found. Run scripts/sync-version.sh (no --check) to fix,"
        echo "then commit the result before tagging a release."
        exit 1
    fi
    echo "OK: all mirrors match __version__ = $VERSION"
    exit 0
fi

if [ "$drift" -eq 1 ]; then
    echo ""
    echo "==> Mirrors updated. Review the diff and commit:"
    echo "    git diff -- gateway/pyproject.toml docker/versions.env"
else
    echo "OK: all mirrors already matched __version__ = $VERSION"
fi
