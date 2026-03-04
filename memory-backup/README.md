# Memory Backup

This directory is a host bind mount used by the AgentShroud Docker container
to persist bot memory across volume resets, upgrades, and fresh installs.

## How it works

1. **On startup**: If the workspace volume is empty (fresh install), memory
   files are restored from this backup directory.
2. **On every startup**: Current memory is backed up here.
3. **On shutdown**: Memory is backed up before the container stops.

## Files

- `MEMORY.md` — Long-term memory
- `memory/*.md` — Daily notes

## Important

- Actual memory content is in .gitignore (personal data)
- To migrate to a new machine: copy this directory
