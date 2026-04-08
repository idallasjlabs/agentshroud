#!/bin/bash
echo "======================================"
echo "  AgentShroud Infrastructure Check"
echo "======================================"

# MLX Server
echo "--- MLX (localhost:8234) ---"
MLX=$(curl -s --max-time 5 http://localhost:8234/v1/models)
if [ -z "$MLX" ]; then
  echo "  ❌ Not running"
else
  echo "  ✅ Running"
  echo "$MLX" | python3 -c "
import sys,json
d=json.load(sys.stdin)
for m in d.get('data',[]): print(f'     • {m[\"id\"]}')
"
  echo "--- MLX Inference Test (may take 30-60s) ---"
  RESULT=$(curl -s --max-time 120 http://localhost:8234/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{"model":"mlx-community/Qwen2.5-Coder-32B-Instruct-4bit",
         "messages":[{"role":"user","content":"Reply with only the word: OK"}],
         "stream":false,"max_tokens":10}')
  CONTENT=$(echo "$RESULT" | python3 -c "
import sys,json
d=json.load(sys.stdin)
print(d['choices'][0]['message']['content'].strip())
" 2>/dev/null)
  [ -n "$CONTENT" ] && echo "  ✅ Inference working: '$CONTENT'" || echo "  ❌ Inference failed"
fi

# Ollama
echo "--- Ollama (localhost:11434) ---"
OLLAMA=$(curl -s --max-time 5 http://localhost:11434/api/tags)
if [ -z "$OLLAMA" ]; then
  echo "  ❌ Not running"
else
  echo "  ✅ Running"
  echo "$OLLAMA" | python3 -c "
import sys,json
d=json.load(sys.stdin)
for m in d.get('models',[]): print(f'     • {m[\"name\"]}')
"
  echo "--- Ollama Inference Test (may take 30-60s) ---"
  ORESULT=$(curl -s --max-time 120 http://localhost:11434/api/chat \
    -d '{"model":"qwen2.5-coder:32b",
         "messages":[{"role":"user","content":"Reply with only the word: OK"}],
         "stream":false}')
  OCONTENT=$(echo "$ORESULT" | python3 -c "
import sys,json
d=json.load(sys.stdin)
print(d['message']['content'].strip())
" 2>/dev/null)
  [ -n "$OCONTENT" ] && echo "  ✅ Inference working: '$OCONTENT'" || echo "  ❌ Inference failed"
fi

# OpenWebUI
echo "--- OpenWebUI (localhost:8082) ---"
OWUI=$(curl -s --max-time 5 -o /dev/null -w "%{http_code}" http://localhost:8082/health)
[ "$OWUI" = "200" ] && echo "  ✅ Running" || echo "  ❌ Not running (HTTP $OWUI)"

echo "======================================"
echo "  Done"
echo "======================================"
