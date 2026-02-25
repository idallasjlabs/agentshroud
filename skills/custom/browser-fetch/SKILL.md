# Browser Fetch Skill

Securely fetch content from JavaScript-heavy websites using headless browser automation.

## Features

- 🔐 Full approval queue integration - every fetch requires explicit approval
- 📝 Complete audit trail - all URLs and actions logged
- 🎭 Playwright-powered - handles modern JavaScript applications
- 🛡️ Sandboxed execution - runs in isolated container environment

## Use Cases

- Fetch 1Password share links (requires JavaScript decryption)
- Access dynamic web applications
- Scrape content from SPA (Single Page Applications)
- Automate browser interactions with full logging

## Security

All browser fetch operations:
1. Require explicit approval via approval queue
2. Log URL, timestamp, and requester to audit ledger
3. Run in sandboxed container with no network access to LAN
4. Cannot access local filesystem outside container

## Usage

Via Telegram:
```
Fetch content from https://share.1password.com/...
```

The bot will:
1. Request approval to open the URL
2. Launch headless browser after approval
3. Wait for page to fully load and decrypt
4. Extract and return the content
5. Log the operation to audit ledger
