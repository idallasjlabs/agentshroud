# HEARTBEAT.md

## v0.8.0 Overnight Work — Questions for Isaiah

1. **Observatory Mode**: Should `monitor` mode still log to the audit trail, or skip logging too? (I assume log everything but never block)
2. **Egress firewall**: Should the Telegram approval buttons be on the production bot or a separate admin bot?
3. **Cross-turn correlation**: How many turns back should we track? Plan says 20 — is that right or too aggressive?
4. **Output canary**: Should canary detection block the response entirely, or redact just the leaked portion?
5. **Production upgrade**: Old containers (60c3c8b5c3db, bc7b8ebc78f0) are stopped. Ready to run `./docker/upgrade.sh marvin-prod`?
6. **Chris Shelton**: His Telegram is deactivated. Should I email him? Need his email address.
7. **iCloud sharing**: Did you receive the calendar/reminder sharing invitations from agentshroud.ai@icloud.com?
8. **iMessage GUI login**: When can you Fast User Switch to agentshroud-bot on Marvin to sign into Messages.app?
