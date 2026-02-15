# Secrets Configuration

This directory contains sensitive credentials for the SecureClaw stack.

---

## Setup

### 1. OpenAI API Key

Create a file `openai_api_key.txt` with your OpenAI API key:

```bash
echo "sk-proj-..." > docker/secrets/openai_api_key.txt
chmod 600 docker/secrets/openai_api_key.txt
```

### 2. Anthropic API Key

Create a file `anthropic_api_key.txt` with your Anthropic API key:

```bash
echo "sk-ant-api03-..." > docker/secrets/anthropic_api_key.txt
chmod 600 docker/secrets/anthropic_api_key.txt
```

**IMPORTANT**: Never commit these files to git. They're in `.gitignore`.

### 3. Verify Setup

```bash
# Check files exist and have correct permissions
ls -la docker/secrets/*.txt
# Should show: -rw------- (600 permissions) for both files

# Verify content
cat docker/secrets/openai_api_key.txt
cat docker/secrets/anthropic_api_key.txt
```

---

## Security Notes

- API keys are mounted as Docker secrets at:
  - `/run/secrets/openai_api_key`
  - `/run/secrets/anthropic_api_key`
- Never pass API keys via environment variables in `docker-compose.yml`
- Keys are never logged or exposed in container output
- File permissions: 600 (owner read/write only)
- These files are ignored by git (see `.gitignore`)

---

## Troubleshooting

**Error: "secret not found"**
- Ensure both `.txt` files exist in `docker/secrets/`
- Check file permissions (should be 600)
- Verify docker-compose.yml references correct paths

**Error: "permission denied"**
```bash
chmod 600 docker/secrets/openai_api_key.txt
chmod 600 docker/secrets/anthropic_api_key.txt
```

**Need to update a key**
```bash
# Edit the file directly
nano docker/secrets/openai_api_key.txt
# or
nano docker/secrets/anthropic_api_key.txt

# Then restart the container
docker compose -f docker/docker-compose.yml restart openclaw
```

---

## Quick Setup Script

```bash
#!/bin/bash
# Run from project root: /Users/ijefferson.admin/Development/oneclaw

# Set your API keys here
OPENAI_KEY="sk-proj-YOUR_KEY_HERE"
ANTHROPIC_KEY="sk-ant-api03-YOUR_KEY_HERE"

# Create secret files
echo "$OPENAI_KEY" > docker/secrets/openai_api_key.txt
echo "$ANTHROPIC_KEY" > docker/secrets/anthropic_api_key.txt

# Set permissions
chmod 600 docker/secrets/openai_api_key.txt
chmod 600 docker/secrets/anthropic_api_key.txt

echo "✅ API keys configured"
ls -la docker/secrets/*.txt
```
