# Secrets Configuration

This directory contains sensitive credentials for the SecureClaw stack.

## Setup

### 1. Anthropic API Key (Required)

Create a file `anthropic_api_key.txt` with your Anthropic API key:

```bash
echo "sk-ant-api03-..." > docker/secrets/anthropic_api_key.txt
chmod 600 docker/secrets/anthropic_api_key.txt
```

**IMPORTANT**: Never commit `anthropic_api_key.txt` to git. It's in `.gitignore`.

### 2. Verify Setup

```bash
# Check file exists and has correct permissions
ls -la docker/secrets/anthropic_api_key.txt
# Should show: -rw------- (600 permissions)

# Verify content (should show your API key)
cat docker/secrets/anthropic_api_key.txt
```

## Security Notes

- API keys are mounted as Docker secrets at `/run/secrets/anthropic_api_key`
- Never pass API keys via environment variables in `docker-compose.yml`
- Keys are never logged or exposed in container output
- File permissions: 600 (owner read/write only)

## Troubleshooting

**Error: "secret not found"**
- Ensure `anthropic_api_key.txt` exists in `docker/secrets/`
- Check file permissions (600)
- Verify docker-compose.yml references correct path

**Error: "permission denied"**
- Run: `chmod 600 docker/secrets/anthropic_api_key.txt`
