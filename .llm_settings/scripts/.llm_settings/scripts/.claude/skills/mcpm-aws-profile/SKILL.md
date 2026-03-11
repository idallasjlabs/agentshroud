# Skill: MCP AWS Profile Configuration (MCPM-AWS-PROFILE)

## Role
You are an AWS configuration specialist for MCP (Model Context Protocol) servers. Help developers configure and switch AWS profiles for MCP operations.

## When to Invoke
Use this skill when:
- Switching between AWS accounts/profiles
- Configuring AWS MCP for the first time
- Setting up multi-account AWS access
- Troubleshooting AWS credential issues
- Using AWS SSO profiles

## AWS Profile Basics

### What is an AWS Profile?
AWS profiles store credential sets in `~/.aws/credentials` and configuration in `~/.aws/config`. This allows managing multiple AWS accounts/roles.

### Default Profile vs Named Profiles
- **Default:** Used when no profile is specified
- **Named:** Requires explicit selection (e.g., `--profile production`)

---

## List Available Profiles

### View Configured Profiles
```bash
# List all profiles from ~/.aws/credentials
grep '^\[' ~/.aws/credentials

# List all profiles from ~/.aws/config
grep '^\[profile' ~/.aws/config

# Show all profiles with details
aws configure list-profiles 2>/dev/null || {
  echo "Profiles in ~/.aws/credentials:"
  grep '^\[' ~/.aws/credentials 2>/dev/null | tr -d '[]'
  echo ""
  echo "Profiles in ~/.aws/config:"
  grep '^\[profile' ~/.aws/config 2>/dev/null | sed 's/\[profile //' | tr -d ']'
}
```

### Check Current Profile
```bash
# Show which profile is active
echo "Current profile: ${AWS_PROFILE:-default}"

# Verify credentials work
aws sts get-caller-identity

# Expected output:
# {
#   "UserId": "AIDAI...",
#   "Account": "123456789012",
#   "Arn": "arn:aws:iam::123456789012:user/your-name"
# }
```

---

## Configure New Profile

### Option 1: Interactive Configuration
```bash
# Configure default profile
aws configure

# Configure named profile
aws configure --profile your-profile-name
```

You'll be prompted for:
1. AWS Access Key ID
2. AWS Secret Access Key
3. Default region (e.g., `us-east-1`)
4. Default output format (e.g., `json`)

### Option 2: Manual Configuration

**Edit `~/.aws/credentials`:**
```ini
[default]
aws_access_key_id = AKIAIOSFODNN7EXAMPLE
aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

[production]
aws_access_key_id = AKIAI44QH8DHBEXAMPLE
aws_secret_access_key = je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY

[development]
aws_access_key_id = AKIAI44QH8DHBEXAMPLE
aws_secret_access_key = je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY
```

**Edit `~/.aws/config`:**
```ini
[default]
region = us-east-1
output = json

[profile production]
region = us-east-1
output = json
role_arn = arn:aws:iam::123456789012:role/ProductionRole
source_profile = default

[profile development]
region = us-west-2
output = json
```

---

## Switch AWS Profile for MCP

### Method 1: Set Environment Variable (Session)
```bash
# Set for current shell session
export AWS_PROFILE=production

# Verify
echo $AWS_PROFILE
aws sts get-caller-identity
```

### Method 2: Set Permanently (Shell Config)
```bash
# Add to ~/.zshrc or ~/.bashrc
echo 'export AWS_PROFILE=production' >> ~/.zshrc
source ~/.zshrc

# Verify
echo $AWS_PROFILE
```

### Method 3: Configure in .mcp.json
Update `.mcp.json` to set profile for MCP server:
```json
{
  "mcpServers": {
    "awslabs.aws-api-mcp-server": {
      "command": "/opt/homebrew/bin/uvx",
      "args": [
        "awslabs.aws-api-mcp-server@latest",
        "--readonly"
      ],
      "env": {
        "AWS_PROFILE": "production"
      }
    }
  }
}
```

**Restart Claude Code** after modifying `.mcp.json`.

---

## AWS SSO Configuration

AWS SSO provides temporary credentials that auto-expire (more secure).

### Initial SSO Setup
```bash
# Configure SSO profile
aws configure sso

# Follow prompts:
# 1. SSO start URL: https://your-company.awsapps.com/start
# 2. SSO region: us-east-1
# 3. Select account
# 4. Select role
# 5. CLI default region: us-east-1
# 6. CLI default output: json
# 7. Profile name: your-sso-profile
```

### Login to SSO
```bash
# Login (opens browser)
aws sso login --profile your-sso-profile

# Verify
aws sts get-caller-identity --profile your-sso-profile
```

### Use SSO Profile with MCP
```bash
# Set SSO profile as active
export AWS_PROFILE=your-sso-profile

# Login (required before each session)
aws sso login --profile your-sso-profile

# Verify MCP can use it
aws sts get-caller-identity
```

**Note:** SSO credentials expire (typically 12 hours). Re-run `aws sso login` when expired.

---

## Multi-Account AWS Access

### Scenario: Development → Production
```bash
# Development account
export AWS_PROFILE=development
aws sts get-caller-identity

# Switch to production
export AWS_PROFILE=production
aws sts get-caller-identity
```

### Using AssumeRole for Cross-Account Access

**Config (`~/.aws/config`):**
```ini
[profile dev]
region = us-east-1

[profile prod]
region = us-east-1
role_arn = arn:aws:iam::987654321098:role/ProdAccessRole
source_profile = dev
mfa_serial = arn:aws:iam::123456789012:mfa/your-name
```

**Usage:**
```bash
# Assume prod role (requires MFA)
export AWS_PROFILE=prod
aws sts get-caller-identity
# Prompts for MFA token
```

---

## Troubleshooting

### "Unable to locate credentials"
**Cause:** No credentials configured for the profile
**Fix:**
```bash
# Configure profile
aws configure --profile your-profile-name

# Or check credentials file
cat ~/.aws/credentials
```

### "Token expired" (SSO)
**Cause:** SSO session expired
**Fix:**
```bash
aws sso login --profile your-sso-profile
```

### "Access Denied"
**Cause:** Profile lacks permissions for operation
**Fix:**
```bash
# Check which identity you're using
aws sts get-caller-identity --profile your-profile-name

# Review IAM policies
aws iam list-attached-user-policies --user-name your-name

# Simulate policy
aws iam simulate-principal-policy \
  --policy-source-arn arn:aws:iam::ACCOUNT:user/your-name \
  --action-names s3:GetObject
```

### MCP Not Using Profile
**Cause:** Environment variable not set for MCP process
**Fix:**
```bash
# Option 1: Set in .mcp.json (recommended)
# Add "env": {"AWS_PROFILE": "your-profile"} to server config

# Option 2: Restart Claude Code with profile set
export AWS_PROFILE=your-profile
claude code
```

---

## Best Practices

### Security
- Use **IAM roles** when possible (EC2, Lambda, ECS)
- Enable **MFA** on AWS accounts
- Use **temporary credentials** (SSO) over long-term keys
- Rotate access keys every **90 days**
- Use **least-privilege** IAM policies

### Organization
- Name profiles clearly: `company-dev`, `company-prod`
- Use consistent region settings
- Document which profile accesses which account
- Keep `~/.aws/credentials` in version control `.gitignore`

### MCP-Specific
- Set `AWS_PROFILE` in `.mcp.json` for consistency
- Use `--readonly` flag for safe MCP operations
- Test profile before using with MCP: `aws sts get-caller-identity`
- Restart Claude Code after changing profiles

---

## Quick Reference

```bash
# List profiles
aws configure list-profiles

# Show current profile
echo $AWS_PROFILE

# Set profile (session)
export AWS_PROFILE=your-profile

# Set profile (permanent)
echo 'export AWS_PROFILE=your-profile' >> ~/.zshrc

# Verify credentials
aws sts get-caller-identity

# SSO login
aws sso login --profile your-sso-profile

# Configure new profile
aws configure --profile new-profile-name
```

---

## Related Skills
- `/mcpm-auth-reset aws` - Reset AWS credentials
- `/mcpm-doctor` - Diagnose MCP issues
- `/mcpm` - General MCP usage guide

## Configuration Files
- **Credentials:** `~/.aws/credentials`
- **Config:** `~/.aws/config`
- **MCP Config:** `.mcp.json`
