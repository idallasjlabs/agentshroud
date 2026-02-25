#!/bin/bash
# Wrapper to run browser-fetch as root (browsers are owned by root)
exec su -c "node /home/node/.openclaw/skills/browser-fetch/browser-fetch.js \"\$@\"" root -- "$@"
