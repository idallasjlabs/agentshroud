#!/bin/bash
echo "=== OpenClaw Status ==="
echo ""
echo "Container:"
docker ps --filter "name=oneclaw_isaiah" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
echo ""
echo "Image:"
docker images oneclaw-secure:latest --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}\t{{.CreatedSince}}"
echo ""
echo "Personality Files:"
ls -lh workspace/{IDENTITY,SOUL.md,USER.md} 2>/dev/null | awk '{print $9, "-", $5}'
echo ""
echo "API Key Configured:"
if grep -q "^ANTHROPIC_API_KEY=.\+$" secrets/.env 2>/dev/null; then
    echo "✓ Anthropic"
elif grep -q "^OPENAI_API_KEY=.\+$" secrets/.env 2>/dev/null; then
    echo "✓ OpenAI"
else
    echo "✗ No API key found"
fi
echo ""
echo "Gateway Health:"
curl -s http://localhost:18789/health 2>/dev/null | jq . || echo "Not responding (container may be stopped)"
