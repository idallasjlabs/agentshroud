# SecureBrowser Skill

**Version**: 1.0.0  
**Author**: SecureClaw Project  
**License**: MIT  
**Security Level**: Enterprise-Grade

---

## Overview

SecureBrowser is an enterprise-grade browser automation skill for OpenClaw that embodies the "One Claw Tied Behind Your Back" philosophy. It provides powerful browser automation capabilities while maintaining strict security controls.

## Key Features

✅ **Security-First Design**:
- URL allowlisting (only approved domains accessible)
- Risk-based approval workflows
- Comprehensive audit logging
- Isolated browser contexts
- No credential extraction from DOM

✅ **Browser Capabilities**:
- Navigate to web pages
- Fill forms (with security checks)
- Click elements (with destructive action protection)
- Take screenshots
- Extract data (with sensitive data blocking)
- Detect CAPTCHAs

✅ **Enterprise Controls**:
- Configurable security policies
- Rate limiting
- Approval queue integration
- Immutable audit trail
- Screenshot retention for forensics

## Quick Start

### 1. Verify Installation

```bash
docker exec openclaw-bot openclaw skills list | grep securebrowser
```

Should show:
```
✓ ready   │ 🌐 securebrowser  │ Enterprise-grade secure browser automation...
```

### 2. Configure Allowlist

Edit `/home/node/.openclaw/skills/securebrowser/config.yaml`:

```yaml
security:
  url_allowlist:
    - "apple.com"
    - "icloud.com"
    - "yoursite.com"  # Add your trusted domains
```

### 3. Test Navigation

```bash
docker exec openclaw-bot python3 /home/node/.openclaw/skills/securebrowser/scripts/browse.py \
  navigate --url "https://www.apple.com" --screenshot
```

## Usage Examples

### Example 1: Simple Navigation

```python
# Via OpenClaw bot
"Navigate to Apple's website and take a screenshot"
```

Bot will:
1. Validate apple.com is in allowlist
2. Navigate to https://www.apple.com
3. Take screenshot
4. Log action to audit trail

### Example 2: Fill Form (Non-Sensitive)

```python
"Go to the contact form and fill in my email"
```

Bot will:
1. Navigate to form page
2. Fill email field (LOW risk - auto-execute)
3. Log action
4. Return success

### Example 3: Fill Password (Sensitive)

```python
"Fill in the password field for Apple ID creation"
```

Bot will:
1. Navigate to signup page
2. Classify as HIGH risk (password field)
3. Request approval via Control UI
4. Wait for approval
5. Fill field if approved
6. Log action with redacted value

### Example 4: Handle CAPTCHA

```python
"Create an Apple ID account"
```

Bot will:
1. Navigate to signup
2. Fill email/name (auto)
3. Detect CAPTCHA
4. Return: "CAPTCHA detected. Please complete manually at: [URL]"
5. User completes CAPTCHA
6. Bot continues with approval-required steps

## Security Model

### URL Access Control

**Allowlist-Based**:
- Only explicitly approved domains are accessible
- Wildcards supported: `*.apple.com`
- Blocklist overrides allowlist

**Default Allowlist**:
- apple.com
- icloud.com
- account.apple.com
- appleid.apple.com

**To add domains**:
Edit `config.yaml` and add to `url_allowlist`

### Risk Classification

| Action | Default Risk | Approval Required? |
|--------|--------------|-------------------|
| Navigate to allowlisted URL | LOW | No |
| Take screenshot | LOW | No |
| Extract public text | LOW | No |
| Fill text field | LOW | No |
| Fill password field | HIGH | Yes |
| Click delete button | HIGH | Yes |
| Execute JavaScript | CRITICAL | Yes |

### Approval Workflow

High-risk actions trigger approval request:

```
[SecureBrowser] Approval Required
Action: Fill password field
URL: https://account.apple.com/signup
Risk: HIGH
Selector: #password
Value: [REDACTED]

Approve? [Yes/No]
```

User approves via Control UI → Action executes → Logged

### Audit Trail

Every action creates immutable audit entry:

```json
{
  "timestamp": "2026-02-16T10:30:00Z",
  "action": "navigate",
  "url": "https://account.apple.com",
  "risk_level": "LOW",
  "result": "success",
  "screenshot": "/audit/screenshots/20260216_103000.png"
}
```

Audit logs stored at:
- Actions: `/home/node/.openclaw/audit/browser_audit.jsonl`
- Screenshots: `/home/node/.openclaw/audit/screenshots/`

## Configuration

### Full Configuration Example

```yaml
security:
  url_allowlist:
    - "apple.com"
    - "icloud.com"
    - "*.trusted-domain.com"
  
  url_blocklist:
    - "*.onion"
    - "malicious-site.com"
  
  approval_required:
    - action: "fill_form"
      patterns: ["password", "credit_card"]
    - action: "execute_javascript"
      always: true
  
  rate_limits:
    requests_per_minute: 30
    requests_per_hour: 500
  
  audit:
    log_all_actions: true
    save_screenshots: true
    screenshot_retention_days: 30
  
  browser:
    headless: true
    timeout: 30000
```

## CLI Reference

### Navigate

```bash
python3 browse.py navigate \
  --url "https://example.com" \
  --screenshot
```

### Fill Field

```bash
python3 browse.py fill-field \
  --selector "#email" \
  --value "user@example.com" \
  --risk MEDIUM
```

### Click

```bash
python3 browse.py click \
  --selector "#submit-button" \
  --wait-for navigation
```

### Extract

```bash
python3 browse.py extract \
  --selector ".price" \
  --attribute "textContent"
```

### Screenshot

```bash
python3 browse.py screenshot \
  --output "/tmp/screenshot.png" \
  --full-page
```

## Integration

### With SecureClaw Gateway

```python
# gateway/ingest_api/browser.py
from securebrowser import SecureBrowser

browser = SecureBrowser()
result = await browser.navigate("https://apple.com")
await ledger.record(result)
```

### With 1Password

```python
# Retrieve credentials securely
password = await get_credential("apple-password")

# Use in browser without displaying
await browser.fill_field("#password", password, risk_override="HIGH")
# Password never logged or displayed
```

## Troubleshooting

### "URL not in allowlist"

**Problem**: Trying to access unauthorized domain  
**Solution**: Add domain to `config.yaml` under `url_allowlist`

### "Approval required but none granted"

**Problem**: High-risk action needs approval  
**Solution**: Approve via Control UI or reduce risk level if appropriate

### "Browser timeout"

**Problem**: Page load exceeds timeout (default: 30s)  
**Solution**: Increase timeout in `config.yaml` under `browser.timeout`

### "CAPTCHA detected"

**Problem**: CAPTCHA blocking automated access  
**Solution**: Complete CAPTCHA manually, bot will continue after

### "Credential extraction blocked"

**Problem**: Trying to extract password from DOM  
**Solution**: This is intentional security control. Cannot be overridden.

## Security Guarantees

**What SecureBrowser WILL do**:
✅ Only access allowlisted URLs
✅ Require approval for high-risk actions
✅ Log all actions to immutable audit trail
✅ Isolate browser contexts (no cross-contamination)
✅ Block credential extraction from DOM
✅ Save screenshots for forensics
✅ Detect and report CAPTCHAs
✅ Enforce rate limits

**What SecureBrowser WON'T do**:
❌ Access URLs not in allowlist (even with approval)
❌ Extract credentials from page DOM
❌ Bypass approval queue for high-risk actions
❌ Modify audit logs (append-only)
❌ Reuse browser contexts across tasks
❌ Download files
❌ Execute arbitrary JavaScript without approval

## Limitations

**Cannot Fully Automate**:
- CAPTCHA solving (detection only)
- SMS/Email verification codes
- Biometric authentication
- Two-factor authentication (unless TOTP from 1Password)

**Security Restrictions**:
- No credential extraction (by design)
- No cross-domain navigation without approval
- No localStorage/cookie access
- No persistent browser state

## Publishing to ClawHub

### Step 1: Package Skill

```bash
docker exec openclaw-bot /usr/local/lib/node_modules/openclaw/skills/skill-creator/scripts/package_skill.py \
  /home/node/.openclaw/skills/securebrowser
```

Creates: `securebrowser.skill` file

### Step 2: Test Locally

```bash
docker exec openclaw-bot openclaw skills check securebrowser
```

### Step 3: Publish

```bash
# Install clawhub CLI
docker exec openclaw-bot npm install -g clawhub

# Login (creates account if needed)
docker exec openclaw-bot clawhub login --username therealidallasj

# Publish
docker exec openclaw-bot clawhub publish securebrowser.skill
```

## Support

**Documentation**:
- SKILL.md - Full skill documentation
- references/security-policies.md - Security policy details
- config.yaml - Configuration reference

**Issues**:
- GitHub: https://github.com/secureclaw/securebrowser
- Email: security@secureclaw.dev

## License

MIT License - See LICENSE file

---

**Built with "One Claw Tied Behind Your Back" Philosophy**

Maximum capability. Maximum security. No compromises.
