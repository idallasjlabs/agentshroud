#!/usr/bin/env bash
set -euo pipefail

REPO="$(git rev-parse --show-toplevel)"
VAULT="$REPO/.obsidian-vaults/code-architecture"
SRC="$REPO/src"
DATE=$(date +%Y-%m-%d)

mkdir -p "$VAULT/modules" "$VAULT/git-log" "$VAULT/adr"

find "$SRC" -name "*.py" | while read -r f; do
  rel="${f#$SRC/}"
  slug="${rel//\//__}"
  note="$VAULT/modules/${slug%.py}.md"
  imports=$(grep -E "^(import|from)" "$f" 2>/dev/null | head -20 || true)
  cat > "$note" << MDEOF
---
tags: [module, auto-generated]
source: src/${rel}
updated: ${DATE}
---
# [[src/${rel}]]

## Imports
\`\`\`
${imports}
\`\`\`
MDEOF
done

git -C "$REPO" log --oneline -20 \
  --format="- %h %s (%ad)" --date=short \
  > "$VAULT/git-log/recent-commits.md"

# Symlink ADRs if they exist
if [[ -d "$REPO/docs/adr" ]]; then
  ln -sf "$REPO/docs/adr"/*.md "$VAULT/adr/" 2>/dev/null || true
fi

echo "Code graph updated → $VAULT"
