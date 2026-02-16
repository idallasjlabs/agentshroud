# Apple Services Setup Guide

**Apple ID**: therealidallasj@gmail.com
**Purpose**: Shared Apple services for SecureClaw bot usage

---

## 📧 Apple Mail (IMAP/SMTP)

### IMAP Settings (Incoming Mail)
```
Server: imap.mail.me.com
Port: 993
Security: SSL/TLS
Username: therealidallasj@gmail.com
Password: [From 1Password: Apple ID - therealidallasj]
```

### SMTP Settings (Outgoing Mail)
```
Server: smtp.mail.me.com
Port: 587
Security: STARTTLS
Username: therealidallasj@gmail.com
Password: [From 1Password: Apple ID - therealidallasj]
```

**Note**: You may need to generate an app-specific password at https://appleid.apple.com if 2FA is enabled.

---

## 📅 Calendar (CalDAV)

### CalDAV Server
```
Server: caldav.icloud.com
Port: 443
Security: SSL
Username: therealidallasj@gmail.com
Password: [From 1Password: Apple ID - therealidallasj]
Path: /[your-calendar-id]/
```

**Discovery URL**: https://caldav.icloud.com/

---

## 📝 Notes

### Notes Access Options

1. **Via iCloud Web**: https://www.icloud.com/notes
2. **Via API**: No official public API (would require private access)
3. **Via Third-Party**: Some tools can sync iCloud Notes via WebDAV

**Note**: Apple doesn't provide an official Notes API. You may need to use:
- iCloud web interface
- Apple Script (macOS only)
- Third-party sync tools

---

## 📞 Contacts (CardDAV)

### CardDAV Server
```
Server: contacts.icloud.com
Port: 443
Security: SSL
Username: therealidallasj@gmail.com
Password: [From 1Password: Apple ID - therealidallasj]
Path: /[your-contacts-id]/
```

**Discovery URL**: https://contacts.icloud.com/

---

## 🔐 App-Specific Passwords

If you enable 2FA on the Apple ID (recommended), you'll need app-specific passwords for:
- Email clients (IMAP/SMTP access)
- Calendar apps (CalDAV access)
- Contact apps (CardDAV access)

**Generate at**: https://appleid.apple.com/account/manage
- Sign in
- Go to Security section
- Generate app-specific password
- Store in 1Password under "Apple ID - therealidallasj" with label "openclaw bot password"

---

## 🤖 Bot Integration Plan

### Phase 1: Email
```python
# Bot can send/receive email via Apple Mail SMTP/IMAP
import imaplib
import smtplib

# Retrieve credentials from 1Password
email = "therealidallasj@gmail.com"
password = get_credential("apple-app-password")

# Connect to IMAP
imap = imaplib.IMAP4_SSL("imap.mail.me.com", 993)
imap.login(email, password)

# Connect to SMTP
smtp = smtplib.SMTP("smtp.mail.me.com", 587)
smtp.starttls()
smtp.login(email, password)
```

### Phase 2: Calendar
```python
# Bot can read/write calendar events via CalDAV
import caldav

# Retrieve credentials from 1Password
username = "therealidallasj@gmail.com"
password = get_credential("apple-app-password")

# Connect to CalDAV
client = caldav.DAVClient(
    url="https://caldav.icloud.com",
    username=username,
    password=password
)
principal = client.principal()
calendars = principal.calendars()
```

### Phase 3: Contacts
```python
# Bot can read/write contacts via CardDAV
import vobject
import requests

# Retrieve credentials from 1Password
username = "therealidallasj@gmail.com"
password = get_credential("apple-app-password")

# CardDAV operations
# (Similar to CalDAV but for contacts)
```

---

## 📋 Setup Checklist

### Apple ID Creation
- [ ] Go to https://account.apple.com/account
- [ ] Click "Create Your Apple ID"
- [ ] Use email: therealidallasj@gmail.com
- [ ] Use password from 1Password
- [ ] Verify email (check Gmail)
- [ ] Set up security questions
- [ ] Enable 2FA (recommended)

### iCloud Services
- [ ] Sign in to https://www.icloud.com
- [ ] Enable Mail
- [ ] Enable Calendar
- [ ] Enable Notes
- [ ] Enable Contacts

### App-Specific Password (if 2FA enabled)
- [ ] Go to https://appleid.apple.com/account/manage
- [ ] Navigate to Security → App-Specific Passwords
- [ ] Generate password for "OpenClaw Bot"
- [ ] Store in 1Password as "openclaw bot password"

### Test Access
- [ ] Test IMAP connection
- [ ] Test SMTP sending
- [ ] Test CalDAV calendar access
- [ ] Test CardDAV contacts access

---

## 🚨 Security Notes

### Two-Factor Authentication
**Recommendation**: Enable 2FA for the Apple ID

**Impact**:
- More secure
- Requires app-specific passwords for API access
- Bot will need the app-specific password, not the main password

### Credential Storage
All Apple credentials stored in:
```
1Password: SecureClaw Bot Credentials vault
Item: Apple ID - therealidallasj
Fields:
  - username: therealidallasj@gmail.com
  - password: [main Apple ID password]
  - openclaw bot password: [app-specific password for bot]
```

### Access Pattern
- **Main password**: Only for signing in to Apple ID website
- **App-specific password**: For bot's API access (IMAP, CalDAV, etc.)

---

## 📚 Documentation Links

- **Apple ID**: https://appleid.apple.com
- **iCloud Settings**: https://www.icloud.com/settings
- **Mail Settings**: https://support.apple.com/en-us/HT202304
- **CalDAV Info**: https://developer.apple.com/documentation/
- **CardDAV Info**: https://developer.apple.com/documentation/

---

## 🎯 Next Steps

1. **Create Apple ID** (manual step)
   - Use the email and password from 1Password
   - Complete verification

2. **Enable iCloud services**
   - Sign in to iCloud.com
   - Turn on Mail, Calendar, Notes, Contacts

3. **Generate app-specific password** (if 2FA enabled)
   - Store in 1Password
   - Update this guide with the field name

4. **Test connections**
   - I can help write test scripts
   - Verify IMAP/SMTP work
   - Verify CalDAV/CardDAV work

5. **Integrate with bot**
   - Add email sending/receiving
   - Add calendar management
   - Add contact management

---

**Created**: 2026-02-16
**Status**: Waiting for Apple ID creation
