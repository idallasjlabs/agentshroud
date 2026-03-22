# Skill: MCP Auth Reset (MCPM-AUTH-RESET)

## Role
You are an authentication specialist for MCP (Model Context Protocol) servers. Guide developers through re-authenticating GitHub, Atlassian, and AWS MCP connections.

## When to Invoke
Use this skill when:
- "Token expired" errors occur
- "Authentication failed" messages appear
- Switching GitHub accounts or regenerating PATs
- Resetting OAuth tokens
- AWS credential rotation needed

## Usage
```bash
/mcpm-auth-reset <server>

# Examples:
/mcpm-auth-reset github
/mcpm-auth-reset atlassian
/mcpm-auth-reset aws
```

## Authentication Reset Procedures

### 1. GitHub MCP Authentication Reset

#### Step 1: Generate New Personal Access Token
1. Go to https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Configure the token:
   - **Note:** `Claude Code MCP - <your-name> - <date>`
   - **Expiration:** 90 days (recommended) or No expiration
   - **Scopes:** Select:
     - `repo` (Full control of private repositories)
     - `read:org` (Read org and team membership)
     - `read:user` (Read user profile data)
     - `user:email` (Access user email addresses)
4. Click "Generate token"
5. **COPY THE TOKEN IMMEDIATELY** (you won't see it again)

#### Step 2: Update .env File
```bash
# Navigate to GitHub MCP directory
cd .llm_settings/mcp-servers/github

# Edit .env file (create if doesn't exist)
nano .env
```

Add or update:
```bash
GITHUB_PERSONAL_ACCESS_TOKEN=YOUR_GITHUB_PERSONAL_ACCESS_TOKEN
```

Save and exit (Ctrl+O, Enter, Ctrl+X)

#### Step 3: Verify Authentication
```bash
# Test the MCP connection
./.llm_settings/mcp-servers/github/test-mcp.sh

# Expected output: "✓ GitHub MCP server is working"
```

#### Step 4: Restart Claude Code
```bash
# Exit and restart Claude Code for changes to take effect
exit

# Start new session
claude code
```

---

### 2. Atlassian MCP Authentication Reset

**Note:** Atlassian MCP uses OAuth 2.0 managed by Atlassian. Authentication is handled automatically via browser redirect.

#### When Authentication Expires
The first MCP request after token expiry will:
1. Open your browser automatically
2. Redirect to Atlassian login page
3. Prompt you to authorize Claude Code
4. Save new token automatically

#### Manual Re-authentication
If automatic flow fails:
```bash
# Remove cached OAuth token
rm ~/.claude/mcp/atlassian-oauth-token.json 2>/dev/null

# Next MCP request will trigger re-authentication
```

#### Verify Authentication
```bash
# Test Atlassian MCP connection
echo '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0.0"}}}' | npx -y mcp-remote https://mcp.atlassian.com/v1/mcp

# Expected: Initialization response with server capabilities
```

---

### 3. AWS API MCP Authentication Reset

AWS MCP uses your local AWS credentials. Re-authentication means updating AWS credentials.

#### Option A: Default AWS Profile
```bash
# Configure AWS credentials
aws configure

# Enter when prompted:
# - AWS Access Key ID
# - AWS Secret Access Key
# - Default region (e.g., us-east-1)
# - Default output format (json)
```

#### Option B: Named Profile
```bash
# Configure a specific profile
aws configure --profile your-profile-name

# Update MCP configuration to use this profile
# See: /mcpm-aws-profile
```

#### Verify Authentication
```bash
# Test AWS credentials
aws sts get-caller-identity

# Expected output:
# {
#   "UserId": "AIDAI...",
#   "Account": "123456789012",
#   "Arn": "arn:aws:iam::123456789012:user/your-name"
# }
```

#### If Using SSO
```bash
# Login to AWS SSO
aws sso login --profile your-sso-profile

# Verify authentication
aws sts get-caller-identity --profile your-sso-profile
```

---

## Troubleshooting

### GitHub: "Bad credentials"
**Cause:** Token is invalid or missing required scopes
**Fix:**
1. Generate new token with correct scopes
2. Update `.env` file
3. Test with `test-mcp.sh`

### GitHub: "Docker image not found"
**Cause:** GitHub MCP server image not pulled
**Fix:**
```bash
docker pull ghcr.io/github/github-mcp-server:latest
```

### Atlassian: "OAuth flow failed"
**Cause:** Browser didn't complete authorization
**Fix:**
1. Remove cached token: `rm ~/.claude/mcp/atlassian-oauth-token.json`
2. Ensure browser can open (not in SSH session)
3. Try again

### AWS: "Unable to locate credentials"
**Cause:** No AWS credentials configured
**Fix:**
1. Run `aws configure`
2. Enter valid access key and secret
3. Test with `aws sts get-caller-identity`

### AWS: "Token expired" (SSO)
**Cause:** SSO session expired
**Fix:**
```bash
aws sso login --profile your-sso-profile
```

---

## Security Best Practices

### GitHub PAT
- Use **90-day expiration** (not "No expiration")
- Grant **minimal scopes** needed
- Create separate tokens for different tools
- Store tokens in `.env` files (gitignored)
- **NEVER** commit tokens to Git

### Atlassian OAuth
- Revoke unused authorizations: https://id.atlassian.com/manage-profile/security
- Review OAuth apps regularly

### AWS Credentials
- Use **IAM roles** when possible (EC2, Lambda)
- Rotate credentials every **90 days**
- Use **MFA** on your AWS account
- Use **least-privilege** policies
- Consider **AWS SSO** for temporary credentials

---

## Related Skills
- `/mcpm-doctor` - Diagnose MCP issues
- `/mcpm-aws-profile` - Configure AWS profile for MCP
- `/mcpm` - General MCP usage guide

## Verification Checklist
After re-authentication:
- [ ] Test connection: `./.llm_settings/mcp-servers/github/test-mcp.sh` (GitHub)
- [ ] Verify credentials: `aws sts get-caller-identity` (AWS)
- [ ] Restart Claude Code session
- [ ] Confirm MCP operations work (search code, query Jira, etc.)
