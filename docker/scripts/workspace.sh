#!/bin/bash
set -euo pipefail

# Helper script for working with OpenClaw workspace (Docker volume)

CONTAINER="openclaw-bot"
WORKSPACE="/home/node/openclaw/workspace"

usage() {
    cat <<EOF
OpenClaw Workspace Helper

Usage:
  $0 ls [path]              List files in workspace
  $0 cp-to <file> [path]    Copy file from Mac to workspace
  $0 cp-from <file> [dest]  Copy file from workspace to Mac
  $0 cat <file>             View file contents
  $0 rm <file>              Delete file from workspace
  $0 mkdir <dir>            Create directory in workspace
  $0 shell                  Open shell in workspace
  $0 tree                   Show workspace tree (if tree installed)

Examples:
  $0 ls                     # List workspace root
  $0 ls screenshots         # List screenshots folder
  $0 cp-to report.pdf       # Copy report.pdf to workspace root
  $0 cp-to data.csv data/   # Copy to workspace/data/
  $0 cp-from report.pdf ~/Downloads/
  $0 cat notes.txt
  $0 shell

EOF
    exit 1
}

check_container() {
    if ! docker ps --format '{{.Names}}' | grep -q "^${CONTAINER}$"; then
        echo "Error: Container '${CONTAINER}' is not running"
        echo "Start it with: docker-compose -f docker/docker-compose.yml up -d"
        exit 1
    fi
}

cmd_ls() {
    check_container
    local path="${1:-.}"
    docker exec "$CONTAINER" ls -lAh "${WORKSPACE}/${path}"
}

cmd_cp_to() {
    check_container
    local src="$1"
    local dest="${2:-.}"

    if [ ! -e "$src" ]; then
        echo "Error: File '$src' not found on Mac"
        exit 1
    fi

    echo "Copying $src → workspace/$dest"
    docker cp "$src" "${CONTAINER}:${WORKSPACE}/${dest}"
    echo "✓ Copied successfully"
}

cmd_cp_from() {
    check_container
    local src="$1"
    local dest="${2:-.}"

    echo "Copying workspace/$src → $dest"
    docker cp "${CONTAINER}:${WORKSPACE}/${src}" "$dest"
    echo "✓ Copied successfully"
}

cmd_cat() {
    check_container
    local file="$1"
    docker exec "$CONTAINER" cat "${WORKSPACE}/${file}"
}

cmd_rm() {
    check_container
    local file="$1"

    read -p "Delete workspace/$file? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        docker exec "$CONTAINER" rm -rf "${WORKSPACE}/${file}"
        echo "✓ Deleted $file"
    else
        echo "Cancelled"
    fi
}

cmd_mkdir() {
    check_container
    local dir="$1"
    docker exec "$CONTAINER" mkdir -p "${WORKSPACE}/${dir}"
    echo "✓ Created workspace/$dir"
}

cmd_shell() {
    check_container
    echo "Opening shell in workspace..."
    echo "Type 'exit' to return to Mac terminal"
    echo ""
    docker exec -it "$CONTAINER" bash -c "cd ${WORKSPACE} && exec bash"
}

cmd_tree() {
    check_container
    if docker exec "$CONTAINER" which tree >/dev/null 2>&1; then
        docker exec "$CONTAINER" tree "${WORKSPACE}"
    else
        echo "Tree view (using find):"
        docker exec "$CONTAINER" find "${WORKSPACE}" -type d -o -type f | sed 's|[^/]*/| |g'
    fi
}

# Main command dispatcher
COMMAND="${1:-}"

case "$COMMAND" in
    ls)
        shift
        cmd_ls "$@"
        ;;
    cp-to)
        shift
        if [ $# -lt 1 ]; then
            echo "Error: Missing source file"
            usage
        fi
        cmd_cp_to "$@"
        ;;
    cp-from)
        shift
        if [ $# -lt 1 ]; then
            echo "Error: Missing source file"
            usage
        fi
        cmd_cp_from "$@"
        ;;
    cat)
        shift
        if [ $# -lt 1 ]; then
            echo "Error: Missing file name"
            usage
        fi
        cmd_cat "$@"
        ;;
    rm)
        shift
        if [ $# -lt 1 ]; then
            echo "Error: Missing file name"
            usage
        fi
        cmd_rm "$@"
        ;;
    mkdir)
        shift
        if [ $# -lt 1 ]; then
            echo "Error: Missing directory name"
            usage
        fi
        cmd_mkdir "$@"
        ;;
    shell)
        cmd_shell
        ;;
    tree)
        cmd_tree
        ;;
    *)
        usage
        ;;
esac
