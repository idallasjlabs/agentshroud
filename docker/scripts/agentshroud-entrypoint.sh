#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
# AgentShroud entrypoint wrapper
# Exports API keys from Docker secrets before starting AgentShroud

# Export OpenAI API key from secret file
if [ -f "$OPENAI_API_KEY_FILE" ]; then
    export OPENAI_API_KEY=$(cat "$OPENAI_API_KEY_FILE")
    echo "[entrypoint] Loaded OpenAI API key from secret"
fi

# Export Anthropic API key from secret file
if [ -f "$ANTHROPIC_API_KEY_FILE" ]; then
    export ANTHROPIC_API_KEY=$(cat "$ANTHROPIC_API_KEY_FILE")
    echo "[entrypoint] Loaded Anthropic API key from secret"
fi

# Execute the original entrypoint
exec docker-entrypoint.sh "$@"
