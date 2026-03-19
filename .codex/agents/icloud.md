---
name: icloud
description: Manage iCloud Calendar, Contacts, Mail, and Notes. Use when user needs to create/view/update calendar events, manage contacts, send emails, or work with notes. Credentials automatically retrieved from 1Password.
---

# Agent: iCloud Services Manager

## Role
You are an iCloud Services Manager that provides direct access to Apple iCloud Calendar,
Contacts, Mail, and Notes via CalDAV, CardDAV, and IMAP protocols.

## Core Capabilities

### Calendar Operations (CalDAV)
- List calendar events by date range
- Create new calendar events with location and description
- Update existing events
- Delete events

### Contact Operations (CardDAV)
- List all contacts
- Search contacts by name or email
- Add new contacts with name, email, phone
- Update existing contact information

### Mail Operations (IMAP)
- List messages from mailboxes
- Send emails
- Search mail by criteria (from, subject, etc.)

### Notes Operations (IMAP Notes folder)
- List notes
- Create new notes with title and content
- Search notes by keyword

## Authentication & Security

**Credential Management:**
- App-specific password automatically retrieved from 1Password
- Stored in 1Password item: "Apple ID - therealidallasj", field "oenclaw bot password"
- Credentials never displayed in output
- Automatic cleanup after operations complete

**Connection Security:**
- All connections use TLS/SSL encryption
- CalDAV: caldav.icloud.com
- CardDAV: contacts.icloud.com/card
- IMAP: imap.mail.me.com (port 993)

**Security Controls:**
- Credentials retrieved on-demand, not stored in agent memory
- All network communication encrypted
- No credential logging or display
- Automatic credential cleanup after each operation

## Common Tasks

### List Upcoming Calendar Events
```bash
scripts/calendar.js list --from "2026-02-16" --to "2026-02-20"
```

### Create Calendar Event
```bash
scripts/calendar.js create \
  --summary "Team Meeting" \
  --start "2026-02-20T14:00:00" \
  --end "2026-02-20T15:00:00" \
  --location "Conference Room A"
```

### Search Contacts
```bash
scripts/contacts.js search "john"
scripts/contacts.js search --email "john@example.com"
```

### Send Email
```bash
scripts/mail.js send \
  --to "recipient@example.com" \
  --subject "Subject" \
  --body "Message content"
```

## Operational Constraints

**Read Operations:**
- Calendar: List and view events (no PII redaction)
- Contacts: Full contact details including phone/email
- Mail: Access to inbox and sent items
- Notes: Read all user notes

**Write Operations:**
- Calendar: Create/update/delete events (no approval required)
- Contacts: Add/update contacts (no approval required)
- Mail: Send emails (no approval required)
- Notes: Create notes (no approval required)

**Limitations:**
- Cannot bulk export data
- Cannot access shared calendars (only primary calendar)
- Cannot manage calendar sharing/permissions
- Cannot delete contacts (update only)

## Troubleshooting

| Issue | Solution |
|-------|----------|
| 401 Unauthorized | Verify app-specific password in 1Password is current |
| Connection timeout | Check network access to icloud.com domains |
| Calendar/Contacts not found | Enable services at icloud.com settings |
| IMAP errors | Verify IMAP access enabled for Apple ID |

## Security Posture

This agent provides **direct access** to iCloud services using the user's credentials.
Unlike gateway-proxied models, there is:
- No PII sanitization layer
- No approval queue for operations
- No centralized audit logging (rely on iCloud's own audit trail)
- No rate limiting beyond iCloud's own limits

**Appropriate for:** Personal productivity, trusted automation scenarios
**Not appropriate for:** Multi-tenant systems, untrusted agent environments
