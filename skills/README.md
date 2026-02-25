# AgentShroud Skills Library

Skills imported from OpenClaw Claude Code for reference and customization.

## Directory Structure

- `openclaw/` — 52 built-in OpenClaw skills (from `/usr/local/lib/node_modules/openclaw/skills/`)
- `custom/` — 5 custom AgentShroud skills (from `~/.openclaw/skills/`)

## Custom Skills

| Skill | Description |
|-------|-------------|
| `agentshroud-blueteam` | Blue team security auditing |
| `agentshroud-redteam` | Red team attack simulation |
| `browser-fetch` | Browser-based web fetching |
| `icloud` | iCloud Calendar, Contacts, Mail, Notes |
| `securebrowser` | Enterprise secure browser automation |

## OpenClaw Built-in Skills

52 skills covering: 1Password, Apple Notes/Reminders, Bear Notes, Camsnap, Canvas, Discord, GitHub, Gmail (himalaya), iMessage, Notion, Obsidian, OpenAI (image gen, whisper), Slack, Sonos, Spotify, Things, Trello, Weather, and more.

## Usage

Skills are loaded by the agent runtime based on `SKILL.md` descriptions. Each skill directory contains a `SKILL.md` with instructions and optionally helper scripts.

---
*Imported: 2026-02-25*
