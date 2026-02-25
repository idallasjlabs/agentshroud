---
name: securebrowser
description: Enterprise-grade secure browser automation with Playwright. Use for web tasks requiring browser interaction (form filling, screenshots, page navigation, data extraction) with built-in security controls including URL allowlisting, approval queue integration, audit logging, and sandboxed contexts. Designed for "One Claw Tied Behind Your Back" philosophy - maximum capability with maximum security. Use when user needs automated web interactions, Apple ID creation, form submissions, or any browser-based task that requires security guarantees.
---

# SecureBrowser - Enterprise Secure Browser Automation

Secure, audited browser automation using Playwright with enterprise-grade security controls.

## Core Security Principles

**"One Claw Tied Behind Your Back"** - The bot can perform powerful browser actions, but only within strict security boundaries:

1. **URL Allowlisting**: Only approved domains accessible
2. **Approval Queue**: High-risk actions require explicit approval  
3. **Audit Logging**: Every action logged to ledger
4. **Sandboxed Contexts**: Isolated browser contexts per task
5. **No Credential Extraction**: Cannot extract passwords/tokens from pages
6. **Rate Limiting**: Prevents abuse
7. **Session Isolation**: Each task uses fresh context

## Security Architecture

```
User Request
    ↓
SecureBrowser Skill
    ↓
┌──────────────────────────────────────┐
│  Security Layer                      │
│  • URL Validation (allowlist)        │
│  • Action Classification (risk level)│
│  • Approval Check (if high-risk)     │
│  • Rate Limit Check                  │
└───────────┬──────────────────────────┘
            ↓
┌──────────────────────────────────────┐
│  Playwright Execution                │
│  • Headless Chromium                 │
│  • Isolated Context                  │
│  • No persistent storage             │
│  • Limited permissions               │
└───────────┬──────────────────────────┘
            ↓
┌──────────────────────────────────────┐
│  Audit Layer                         │
│  • Log all URLs visited              │
│  • Log all actions taken             │
│  • Log all data extracted            │
│  • Store screenshots (optional)      │
└──────────────────────────────────────┘
```

## Usage

### Navigate to URL
```bash
scripts/browse.py navigate --url "https://example.com" --screenshot
```

###Fill Form
```bash
scripts/browse.py fill-form \
  --url "https://example.com/signup" \
  --fields '{"email":"user@example.com","name":"John"}' \
  --submit
```

### Extract Data
```bash
scripts/browse.py extract \
  --url "https://example.com" \
  --selector ".price" \
  --attribute "textContent"
```

### Click Element
```bash
scripts/browse.py click \
  --url "https://example.com" \
  --selector "#submit-button" \
  --wait-for "navigation"
```

### Take Screenshot
```bash
scripts/browse.py screenshot \
  --url "https://example.com" \
  --output "/tmp/screenshot.png" \
  --full-page
```

## Security Configuration

Configuration stored in `/home/node/.openclaw/skills/securebrowser/config.yaml`:

```yaml
security:
  url_allowlist:
    - "apple.com"
    - "icloud.com"
    - "account.apple.com"
    - "appleid.apple.com"
    # Add more trusted domains as needed
  
  url_blocklist:
    - "*.onion"
    - "*.torproject.org"
    # Explicitly blocked domains
  
  approval_required:
    - action: "fill_form"
      patterns: ["password", "credit_card", "ssn"]
    - action: "click"
      patterns: ["delete", "remove", "cancel_subscription"]
    - action: "execute_javascript"
      always: true
  
  rate_limits:
    requests_per_minute: 30
    requests_per_hour: 500
  
  audit:
    log_all_actions: true
    save_screenshots: true
    screenshot_dir: "/home/node/.openclaw/audit/screenshots"
  
  browser:
    headless: true
    timeout: 30000
    user_agent: "SecureClaw/1.0 (Enterprise Browser Automation)"
    block_third_party_cookies: true
    block_ads: true
    javascript_enabled: true
```

## Risk Levels

Actions are automatically classified:

**LOW RISK** (Auto-execute):
- Navigate to allowlisted URL
- Take screenshot
- Extract text content
- Read page title/meta

**MEDIUM RISK** (Log + Execute):
- Click non-destructive buttons
- Fill non-sensitive form fields
- Scroll/zoom/resize

**HIGH RISK** (Require Approval):
- Fill password/credit card fields
- Click destructive actions (delete, cancel, etc.)
- Execute arbitrary JavaScript
- Navigate to new domains

## Approval Integration

High-risk actions integrate with SecureClaw approval queue:

```python
from gateway.approval_queue import ApprovalQueue

approval = await ApprovalQueue.request(
    action="fill_password_field",
    url="https://account.apple.com",
    details={"field": "password", "value": "[REDACTED]"},
    risk_level="HIGH"
)

if approval.approved:
    # Execute action
else:
    raise SecurityError("Action denied by approval queue")
```

## Audit Logging

Every action is logged to SecureClaw audit ledger:

```python
await ledger.record(
    source="securebrowser",
    content=f"Navigated to {url}",
    metadata={
        "action": "navigate",
        "url": url,
        "risk_level": "LOW",
        "timestamp": datetime.now().isoformat(),
        "screenshot_path": screenshot_path
    }
)
```

## Example: Apple ID Creation (Semi-Automated)

```python
# Step 1: Navigate to signup (LOW RISK - auto-execute)
await browse.navigate("https://appleid.apple.com/account")
await browse.screenshot("/tmp/signup_page.png")

# Step 2: Fill email (LOW RISK - auto-execute)
await browse.fill_field("#email", "user@example.com")

# Step 3: Fill password (HIGH RISK - require approval)
# Approval request sent to Control UI
await browse.fill_field("#password", password, risk="HIGH")

# Step 4: Handle CAPTCHA (MANUAL - notify user)
captcha_detected = await browse.detect_captcha()
if captcha_detected:
    return "CAPTCHA detected. Please complete manually at: [URL]"

# Step 5: Submit (MEDIUM RISK - log + execute)
await browse.click("#submit-button")

# Step 6: Handle verification (MANUAL - notify user)
return "Email verification required. Check inbox for link."
```

## Best Practices

### 1. Always Specify Risk Level
```python
# Bad
await browse.fill_field("#password", password)

# Good
await browse.fill_field("#password", password, risk="HIGH")
```

### 2. Use Allowlisting Liberally
```python
# Add domain before using
await browse.add_allowed_domain("newsite.com")
await browse.navigate("https://newsite.com")
```

### 3. Take Screenshots for Audit Trail
```python
await browse.screenshot(f"/tmp/before_{action}.png")
await browse.perform_action()
await browse.screenshot(f"/tmp/after_{action}.png")
```

### 4. Handle CAPTCHAs Gracefully
```python
if await browse.detect_captcha():
    return "Manual intervention required: CAPTCHA detected"
```

### 5. Never Extract Credentials
```python
# FORBIDDEN - Will be blocked
password = await browse.extract_field("#password")

# ALLOWED - Use credentials without extracting
await browse.fill_field("#password", get_credential("password"))
```

## Limitations

**Cannot Fully Automate**:
- CAPTCHAs (requires manual completion)
- SMS/Email verification (requires manual code entry)
- Biometric authentication (Touch ID, Face ID)
- Two-factor authentication (requires TOTP from 1Password)

**Security Restrictions**:
- Cannot extract password values from pages
- Cannot bypass allowlist (even with approval)
- Cannot disable audit logging
- Cannot access cookies/local storage from other sessions

## Integration with SecureClaw

### Gateway Integration
```python
# In gateway/ingest_api/main.py
@app.post("/browser/execute")
async def execute_browser_action(request: BrowserRequest):
    # Validate URL against allowlist
    if not await validate_url(request.url):
        raise SecurityError("URL not in allowlist")
    
    # Check risk level
    risk = classify_action(request.action)
    
    # Request approval if needed
    if risk == "HIGH":
        approved = await approval_queue.request(request)
        if not approved:
            raise SecurityError("Action denied")
    
    # Execute and log
    result = await securebrowser.execute(request)
    await ledger.record(result)
    
    return result
```

### 1Password Integration
```python
# Retrieve credentials securely
email = await get_credential("apple-username")
password = await get_credential("apple-password")

# Use in browser without displaying
await browse.fill_form({
    "email": email,
    "password": password
})
# Credentials never logged or displayed
```

## Troubleshooting

### "URL not in allowlist"
Add domain to config.yaml under `security.url_allowlist`

### "Action requires approval but none granted"
High-risk actions need manual approval via Control UI

### "Rate limit exceeded"
Wait or increase limits in config.yaml (if authorized)

### "Browser timeout"
Increase timeout in config.yaml or optimize page load

### "CAPTCHA detected"
Manual intervention required - user must complete CAPTCHA

## Security Guarantees

✅ **Enforced**:
- All URLs validated against allowlist
- All high-risk actions require approval
- All actions logged to audit ledger
- All browser contexts isolated (no cross-contamination)
- All screenshots stored for review
- All credential fields protected from extraction

❌ **Not Guaranteed**:
- Perfect CAPTCHA detection (may miss some)
- Protection against zero-day browser vulnerabilities
- Prevention of all forms of prompt injection (defense in depth)

## See Also

- `references/playwright-api.md` - Full Playwright API reference
- `references/security-policies.md` - Detailed security policy documentation
- `references/approval-workflows.md` - Approval queue integration guide
