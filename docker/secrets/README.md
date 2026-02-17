# Docker Secrets

This directory stores secret files for Docker Compose services.

## Setup

```bash
# Create secrets directory with strict permissions
mkdir -p docker/secrets
chmod 700 docker/secrets

# Generate gateway password
python3 -c "import secrets; print(secrets.token_hex(32))" > docker/secrets/gateway_password.txt

# Add your API keys
echo "sk-..." > docker/secrets/openai_api_key.txt
echo "sk-ant-..." > docker/secrets/anthropic_api_key.txt

# Set strict file permissions
chmod 600 docker/secrets/*.txt
```

## Security

- **Never commit secret files** — they are in `.gitignore`
- File permissions must be 600 (owner read/write only)
- Directory permissions must be 700 (owner only)
- Use 1Password references where possible instead of files
