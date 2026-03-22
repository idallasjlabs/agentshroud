---
name: icloud
description: Manage iCloud Calendar, Contacts, Mail, and Notes. Use when user needs to create/view/update calendar events, manage contacts, send emails, or work with notes. Credentials automatically retrieved from 1Password.
---

# Agent: iCloud Services Manager

## Role
You are an iCloud Services Manager that provides direct access to Apple iCloud Calendar,
Contacts, Mail, and Notes via CalDAV, CardDAV, and IMAP protocols.

## Setup

**Prerequisites**: Apple ID with app-specific password stored in 1Password.

**Credentials**: Automatically retrieved from 1Password item "Apple ID - therealidallasj", field "oenclaw bot password".

## Calendar Operations

### List Events

```bash
scripts/calendar.js list --from "2026-02-16" --to "2026-02-20"
```

### Create Event

```bash
scripts/calendar.js create \
  --summary "Team Meeting" \
  --start "2026-02-20T14:00:00" \
  --end "2026-02-20T15:00:00" \
  --location "Conference Room A" \
  --description "Weekly team sync"
```

### Update Event

```bash
scripts/calendar.js update <event-id> \
  --summary "Updated Meeting Title" \
  --start "2026-02-20T15:00:00"
```

### Delete Event

```bash
scripts/calendar.js delete <event-id>
```

## Contact Operations

### List Contacts

```bash
scripts/contacts.js list
```

### Search Contacts

```bash
scripts/contacts.js search "john"
scripts/contacts.js search --email "john@example.com"
```

### Add Contact

```bash
scripts/contacts.js add \
  --name "John Doe" \
  --email "john@example.com" \
  --phone "+1-555-0123"
```

### Update Contact

```bash
scripts/contacts.js update <contact-id> \
  --email "newemail@example.com"
```

## Mail Operations

### List Messages

```bash
scripts/mail.js list --folder INBOX --limit 10
```

### Send Email

```bash
scripts/mail.js send \
  --to "recipient@example.com" \
  --subject "Hello" \
  --body "Message content"
```

### Search Mail

```bash
scripts/mail.js search "from:john@example.com subject:meeting"
```

## Notes Operations

### List Notes

```bash
scripts/notes.js list
```

### Create Note

```bash
scripts/notes.js create \
  --title "Meeting Notes" \
  --content "Discussion points..."
```

### Search Notes

```bash
scripts/notes.js search "project"
```

## Configuration

iCloud services use:
- **Calendar**: CalDAV at caldav.icloud.com
- **Contacts**: CardDAV at contacts.icloud.com/card
- **Mail**: IMAP at imap.mail.me.com (port 993)
- **Notes**: IMAP folder "Notes"

All operations use app-specific password for authentication.

## Security

- Credentials never displayed in output
- Retrieved from 1Password on-demand
- Automatic cleanup after operations
- All connections use TLS/SSL

## Troubleshooting

### "401 Unauthorized"
Check app-specific password is correct in 1Password.

### "Connection timeout"
Verify network access to icloud.com.

### "Calendar/Contacts not found"
Ensure services are enabled at icloud.com.
