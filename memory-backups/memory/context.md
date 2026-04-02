## Active Projects
- v0.9.0 "Sentinel" — SOC Team Collaboration, branch `feat/v0.9.0-soc-team-collab`
- 44 SOC Command Center UI fixes committed (CC-01 through CC-44)
- 3500 tests passing

## Pending Tasks
- v0.9.0 PR to main
- Recreate docker/secrets/telegram_bot_token_marvin.txt (lost in volume reset)
- Upgrade openclaw from 2026.3.8 (critical pairing token fix in 2026.3.11; latest 2026.3.13)

## Key Facts
- SSH access: marvin (primary dev, max_session=1800s), raspberrypi (daily check-in), trillian (Linux server)
- All SSH routes through gateway:8181 CONNECT proxy
- Use `dev` helper script on marvin for Docker operations
- Model: anthropic/claude-opus-4-6 (cloud mode)
- Slack integration working end-to-end via Socket Mode
- Per-collaborator agent isolation: collab-{telegram_uid}
- NPM_CONFIG_PREFIX=/home/node/.npm-global on openclaw-runtime volume (enables Update Now button)
