#!/usr/bin/env bash
# export-openapi.sh — Export AgentShroud OpenAPI spec from the live gateway
# Usage: ./scripts/export-openapi.sh [gateway_url]
# Default URL: http://localhost:8080
set -euo pipefail

URL="${1:-http://localhost:8080}"
OUT="docs/api/openapi.json"

echo "Fetching OpenAPI spec from $URL/openapi.json ..."
curl -sf "${URL}/openapi.json" | python3 -m json.tool > "$OUT"
echo "Written to $OUT"
echo "Spec summary:"
python3 -c "
import json, sys
s = json.load(open('$OUT'))
paths = s.get('paths', {})
print(f'  Title:   {s[\"info\"][\"title\"]}')
print(f'  Version: {s[\"info\"][\"version\"]}')
print(f'  Paths:   {len(paths)} endpoints')
"
