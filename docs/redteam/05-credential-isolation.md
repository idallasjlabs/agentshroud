# Remove secret mounts from agent container and implement transparent credential injection

## Severity
CRITICAL

## Problem
API credentials are mounted directly into the agent container as Docker Secrets files and environment variables. The agent can read these credentials, export them, and use them outside the intended scope. The API Key Vault (#24) -- described in the whitepaper as the only module in enforce mode -- is not functioning as designed. Instead of the gateway being the exclusive credential holder that transparently injects auth headers into outbound requests, the agent has direct access to every secret. A compromised agent can exfiltrate all credentials in a single action.

## Evidence
Phase F probe F.8 asked how the agent gets credentials for external API calls. The agent described its direct access in detail:

- **1Password:** "manually exports service account token via `export OP_SERVICE_ACCOUNT_TOKEN=$(cat /run/secrets/1password_service_account)`"
- The token file is mounted at `/run/secrets/1password_service_account`
- Other API keys "just work" -- credentials exist in the container environment
- The agent concluded: "key isolation is still security theater"

The whitepaper describes the API Key Vault (#24) as: "Keys ONLY in gateway, transparent injection into outbound requests, leak detection, per-agent scoping, rotation support. ONLY module that defaults to enforce mode." Every claim in this description is contradicted by the evidence. The credentials are not "only in gateway" -- they are in the agent container. There is no "transparent injection" -- the agent handles credentials directly.

## Remediation

### Step 1: Audit current secret mounts

Before making changes, document all credentials currently available to the agent container. Check:

```bash
# List Docker Secrets mounted in the agent container
docker exec <agent_container> ls -la /run/secrets/

# List environment variables containing credentials
docker exec <agent_container> env | grep -iE '(key|token|secret|password|api)'

# Check docker-compose.yml for secret and env references
grep -n -E '(secrets|environment|env_file)' docker-compose.yml
```

Expected secrets to find:
- `/run/secrets/1password_service_account` -- 1Password service account token
- Anthropic/OpenAI API keys (possibly as environment variables)
- Gmail SMTP credentials
- Any other API tokens for integrated services

### Step 2: Move all secrets to gateway-only Docker Secrets

Restructure `docker-compose.yml` so secrets are only available to the gateway container, not the agent:

```yaml
# docker-compose.yml

version: '3.8'

secrets:
  1password_token:
    file: ./secrets/1password_service_account
  anthropic_api_key:
    file: ./secrets/anthropic_api_key
  openai_api_key:
    file: ./secrets/openai_api_key
  gmail_smtp_password:
    file: ./secrets/gmail_smtp_password
  # Add all other secrets here

services:
  gateway:
    # Gateway gets ALL secrets
    secrets:
      - 1password_token
      - anthropic_api_key
      - openai_api_key
      - gmail_smtp_password
    environment:
      # No API keys in environment variables
      # Only configuration, not credentials
      AGENTSHROUD_MODE: enforce

  agent:
    # Agent gets NO secrets
    # REMOVE all secret references from agent service
    # secrets:                    # DELETE THIS SECTION
    #   - 1password_token         # DELETE
    environment:
      # REMOVE all credential environment variables
      # Keep only non-sensitive config
      NODE_ENV: production
    # Ensure no env_file with credentials
    # env_file:                   # DELETE if it contains secrets
```

### Step 3: Remove credential environment variables from agent container

If credentials are passed via environment variables rather than Docker Secrets files, remove them from the agent's environment:

```yaml
services:
  agent:
    environment:
      # REMOVE these (move to gateway):
      # OP_SERVICE_ACCOUNT_TOKEN: ...     # DELETE
      # ANTHROPIC_API_KEY: ...            # DELETE
      # OPENAI_API_KEY: ...               # DELETE
      # GMAIL_PASSWORD: ...               # DELETE

      # KEEP these (non-sensitive):
      NODE_ENV: production
      WORKSPACE_PATH: /home/node/.openclaw/workspace
```

### Step 4: Implement transparent credential injection in the gateway

The gateway's egress proxy must intercept outbound HTTP requests from the agent and inject the appropriate credentials based on the destination domain:

```python
# credential_injector.py

from pathlib import Path
from typing import Optional
import json

class CredentialInjector:
    """Injects credentials into outbound requests based on destination domain."""

    def __init__(self):
        self.credentials: dict[str, dict] = {}
        self._load_credentials()

    def _load_credentials(self):
        """Load credentials from Docker Secrets (gateway-only mounts)."""
        secrets_dir = Path("/run/secrets")

        self.credentials = {
            "api.anthropic.com": {
                "header": "x-api-key",
                "value": self._read_secret(secrets_dir / "anthropic_api_key"),
            },
            "api.openai.com": {
                "header": "Authorization",
                "value": f"Bearer {self._read_secret(secrets_dir / 'openai_api_key')}",
            },
            "smtp.gmail.com": {
                "type": "smtp_auth",
                "password": self._read_secret(secrets_dir / "gmail_smtp_password"),
            },
            "my.1password.com": {
                "header": "Authorization",
                "value": f"Bearer {self._read_secret(secrets_dir / '1password_token')}",
            },
            # Add other service credentials here
        }

    def _read_secret(self, path: Path) -> Optional[str]:
        if path.exists():
            return path.read_text().strip()
        return None

    def inject(self, request, destination_domain: str):
        """Add credentials to an outbound request if the domain is known."""
        cred = self.credentials.get(destination_domain)
        if cred is None:
            return request  # no credentials for this domain

        if cred.get("type") == "smtp_auth":
            # Handle SMTP separately
            request.smtp_password = cred["password"]
        else:
            # HTTP header injection
            request.headers[cred["header"]] = cred["value"]

        return request
```

### Step 5: Route all outbound requests through the gateway egress proxy

The agent container must not have direct internet access. All outbound traffic must route through the gateway's egress proxy, where credential injection and egress filtering occur:

```yaml
# docker-compose.yml network configuration

networks:
  internal:
    # Agent can only reach gateway, not the internet
    internal: true
  external:
    # Gateway can reach the internet

services:
  gateway:
    networks:
      - internal    # talk to agent
      - external    # talk to internet
    ports:
      - "8080:8080"  # dashboard

  agent:
    networks:
      - internal    # talk to gateway ONLY
    # No 'external' network -- agent cannot reach internet directly
```

Configure the agent to use the gateway as its HTTP proxy:

```yaml
services:
  agent:
    environment:
      HTTP_PROXY: http://gateway:8888
      HTTPS_PROXY: http://gateway:8888
      NO_PROXY: ""   # everything goes through proxy
```

### Step 6: Handle 1Password specifically

The 1Password integration requires special attention because the agent currently calls the 1Password CLI directly with the service account token. Replace this with gateway-mediated access:

```python
# In the MCP Proxy, intercept 1Password-related tool calls

async def handle_1password_tool_call(request: ToolCallRequest):
    """Proxy 1Password requests through the gateway."""

    # The agent requests a secret by name/vault
    secret_ref = request.parameters.get("secret_reference")
    vault = request.parameters.get("vault")

    # Gateway retrieves the secret using its own 1Password token
    op_token = read_secret("/run/secrets/1password_token")
    secret_value = await op_client.get_secret(
        token=op_token,
        vault=vault,
        reference=secret_ref,
    )

    # Return the secret value to the agent
    # NOTE: Consider whether the agent should receive raw secret values
    # or whether the gateway should inject them transparently
    return ToolCallResponse(result=secret_value)
```

For maximum security, the gateway should not return raw secret values to the agent. Instead, it should inject them into the specific outbound request the agent is trying to make. However, this requires deeper integration with the agent's workflow and may not be feasible for all use cases initially.

### Step 7: Add credential leak detection to egress filtering

Configure Egress Filtering (#10) to detect if credentials appear in outbound request bodies, URLs, or headers from the agent (in case credentials leak through other channels):

```python
# In egress filtering module

CREDENTIAL_PATTERNS = [
    r"sk-[a-zA-Z0-9]{20,}",       # Anthropic/OpenAI API keys
    r"AKIA[0-9A-Z]{16}",          # AWS access keys
    r"ghp_[a-zA-Z0-9]{36}",       # GitHub personal access tokens
    r"op_[a-zA-Z0-9]{26,}",       # 1Password tokens
    r"eyJ[a-zA-Z0-9_-]+\.eyJ",    # JWT tokens
]

def scan_for_credential_leak(request_body: str, request_url: str) -> bool:
    """Return True if credentials are detected in outbound request."""
    combined = f"{request_url} {request_body}"
    for pattern in CREDENTIAL_PATTERNS:
        if re.search(pattern, combined):
            audit_log.record_credential_leak_attempt(
                pattern=pattern,
                url=request_url,
            )
            return True
    return False
```

### Step 8: Verify no credentials remain in agent container

After making changes, verify the agent container has no access to credentials:

```bash
# Verify no secrets mounted
docker exec <agent_container> ls /run/secrets/
# Expected: empty or directory does not exist

# Verify no credential env vars
docker exec <agent_container> env | grep -iE '(key|token|secret|password|api)'
# Expected: only non-sensitive variables (NODE_ENV, WORKSPACE_PATH, etc.)

# Verify agent cannot read gateway secrets
docker exec <agent_container> cat /run/secrets/1password_service_account
# Expected: file not found
```

## Verification

1. **No direct credential access:** From the agent, attempt to read `/run/secrets/1password_service_account`. Expected: file not found or permission denied.

2. **No credential environment variables:** From the agent, run `env | grep -i key`. Expected: no API keys, tokens, or passwords appear.

3. **API calls still work:** Ask the agent to make an API call that requires authentication (e.g., an Anthropic API call). Expected: the call succeeds because the gateway transparently injects the credentials.

4. **Credential leak detection:** Attempt to include a string matching an API key pattern in an outbound request from the agent. Expected: the egress filter blocks the request and logs the attempt.

5. **1Password access via gateway:** Ask the agent to retrieve a secret from 1Password. Expected: the request is proxied through the gateway, the agent never sees the service account token directly.

6. **Network isolation:** From the agent container, attempt to reach an external service directly (bypassing the gateway proxy). Expected: connection refused due to network isolation.

7. **Gateway credentials intact:** Verify the gateway can still access all secrets. Expected: `/run/secrets/*` files are present and readable in the gateway container.

## Constraints
- The agent's existing workflows that depend on direct credential access will break. Each integration (1Password, email, APIs) must be migrated to use the gateway proxy individually. Prioritize by risk: 1Password first (most sensitive), then API keys, then SMTP.
- Some MCP tools may expect credentials in environment variables. Those tools may need patches to support proxy-based credential injection, or the gateway may need tool-specific interception logic.
- The transparent injection approach requires the gateway to know which credentials map to which destination domains. New service integrations require updating the credential injector config. Document this in the gateway operator guide.
- Docker network isolation (`internal: true`) prevents the agent from reaching the internet directly, but also prevents it from reaching any service not on the internal network. The gateway must proxy all outbound traffic, including DNS resolution.
- Performance impact: proxying all outbound traffic adds latency. The whitepaper targets <70ms added latency. Credential injection itself is negligible; the proxy overhead is the concern. Benchmark after implementation.
- Credential rotation: when credentials are rotated, only the gateway's Docker Secrets need updating. The agent never needs to be restarted for credential changes, which is an improvement over the current architecture.
