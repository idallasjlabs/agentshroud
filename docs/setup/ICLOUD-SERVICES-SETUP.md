# iCloud Services Setup - Complete Guide

**Date**: 2026-02-16
**Apple ID**: agentshroud.ai@gmail.com
**Status**: ✅ Apple ID created, ready for service setup

---

## 🔐 Important: App-Specific Passwords

Since your Apple ID likely has Two-Factor Authentication enabled, you'll need to generate **app-specific passwords** for:
- Mail (IMAP/SMTP)
- Calendar (CalDAV)
- Contacts (CardDAV)

### Generate App-Specific Password

1. Go to https://appleid.apple.com
2. Sign in with: agentshroud.ai@gmail.com
3. Go to **Security** section
4. Click **App-Specific Passwords**
5. Click **Generate an app-specific password**
6. Label it: "OpenClaw Bot - Mail & Calendar"
7. Copy the password (format: xxxx-xxxx-xxxx-xxxx)
8. Store in 1Password

**Or we can try with main password first** - if it fails with 401/403, we'll need the app-specific password.

---

## 📧 iCloud Mail (IMAP/SMTP)

### Server Settings

**IMAP (Incoming Mail)**:
```
Server: imap.mail.me.com
Port: 993
Security: SSL/TLS
Username: agentshroud.ai@gmail.com
Password: [App-specific password or main password]
```

**SMTP (Outgoing Mail)**:
```
Server: smtp.mail.me.com
Port: 587
Security: STARTTLS
Username: agentshroud.ai@gmail.com
Password: [Same as IMAP]
```

### Test IMAP Connection

```javascript
const Imap = require('node-imap');

const imap = new Imap({
    user: 'agentshroud.ai@gmail.com',
    password: '[password from 1Password]',
    host: 'imap.mail.me.com',
    port: 993,
    tls: true
});

imap.once('ready', () => {
    console.log('✓ Connected to iCloud Mail!');
    imap.end();
});

imap.once('error', (err) => {
    console.error('✗ Connection failed:', err.message);
});

imap.connect();
```

---

## 📅 iCloud Calendar (CalDAV)

### Server Settings

**CalDAV URL**: `https://caldav.icloud.com/`

**Authentication**:
- Username: agentshroud.ai@gmail.com
- Password: [App-specific password]

### Discovery Process

1. Initial PROPFIND to discover principal URL
2. Get calendar home URL
3. List calendars
4. Access individual calendars

### Test CalDAV Connection

```javascript
const https = require('https');

function testCalDAV(username, password) {
    const auth = 'Basic ' + Buffer.from(username + ':' + password).toString('base64');

    const options = {
        hostname: 'caldav.icloud.com',
        port: 443,
        path: '/',
        method: 'PROPFIND',
        headers: {
            'Authorization': auth,
            'Content-Type': 'application/xml; charset=utf-8',
            'Depth': '0'
        }
    };

    const req = https.request(options, (res) => {
        console.log(`CalDAV Status: ${res.statusCode}`);

        if (res.statusCode === 207) {
            console.log('✓ Connected to iCloud Calendar!');
        } else if (res.statusCode === 401) {
            console.log('✗ Authentication failed - need app-specific password');
        }

        let data = '';
        res.on('data', chunk => data += chunk);
        res.on('end', () => {
            if (res.statusCode !== 207) {
                console.log('Response:', data.substring(0, 300));
            }
        });
    });

    req.on('error', (e) => {
        console.error('✗ Error:', e.message);
    });

    req.end();
}

// Test with credentials from 1Password
testCalDAV('agentshroud.ai@gmail.com', '[password]');
```

---

## 📞 iCloud Contacts (CardDAV)

### Server Settings

**CardDAV URL**: `https://contacts.icloud.com/`

**Authentication**:
- Username: agentshroud.ai@gmail.com
- Password: [App-specific password]

### Discovery Process

Similar to CalDAV:
1. PROPFIND to discover principal
2. Get addressbook home
3. List addressbooks
4. Access contacts

### Test CardDAV Connection

```javascript
const https = require('https');

function testCardDAV(username, password) {
    const auth = 'Basic ' + Buffer.from(username + ':' + password).toString('base64');

    const options = {
        hostname: 'contacts.icloud.com',
        port: 443,
        path: '/',
        method: 'PROPFIND',
        headers: {
            'Authorization': auth,
            'Content-Type': 'application/xml; charset=utf-8',
            'Depth': '0'
        }
    };

    const req = https.request(options, (res) => {
        console.log(`CardDAV Status: ${res.statusCode}`);

        if (res.statusCode === 207) {
            console.log('✓ Connected to iCloud Contacts!');
        } else if (res.statusCode === 401) {
            console.log('✗ Authentication failed - need app-specific password');
        }
    });

    req.on('error', (e) => {
        console.error('✗ Error:', e.message);
    });

    req.end();
}

testCardDAV('agentshroud.ai@gmail.com', '[password]');
```

---

## 📝 iCloud Notes

### Challenge

Apple Notes doesn't have a public API. Options:

**Option 1: AppleScript (macOS only)**
```applescript
tell application "Notes"
    make new note at folder "Notes" with properties {name:"Title", body:"Content"}
end tell
```

**Option 2: CloudKit API**
- Apple's cloud database
- Notes might be accessible via CloudKit
- Requires Apple Developer account
- Complex setup

**Option 3: IMAP Access**
- Notes are actually stored in a special IMAP folder
- Can be accessed via IMAP connection
- Folder: "Notes"

### Access Notes via IMAP

```javascript
const Imap = require('node-imap');

const imap = new Imap({
    user: 'agentshroud.ai@gmail.com',
    password: '[app-specific password]',
    host: 'imap.mail.me.com',
    port: 993,
    tls: true
});

function openNotesFolder() {
    imap.once('ready', () => {
        imap.openBox('Notes', false, (err, box) => {
            if (err) {
                console.error('Error opening Notes folder:', err);
                return;
            }

            console.log('✓ Opened Notes folder');
            console.log('Total notes:', box.messages.total);

            // Fetch notes
            const fetch = imap.seq.fetch('1:*', {
                bodies: 'HEADER.FIELDS (SUBJECT)',
                struct: true
            });

            fetch.on('message', (msg, seqno) => {
                msg.on('body', (stream, info) => {
                    let buffer = '';
                    stream.on('data', chunk => buffer += chunk.toString('utf8'));
                    stream.once('end', () => {
                        console.log(`Note ${seqno}:`, buffer);
                    });
                });
            });

            fetch.once('end', () => {
                imap.end();
            });
        });
    });

    imap.connect();
}

openNotesFolder();
```

---

## 🚀 Complete Setup Script

Let me create a comprehensive test script that tries all services:

```javascript
#!/usr/bin/env node
const https = require('https');

const CREDENTIALS = {
    username: 'agentshroud.ai@gmail.com',
    password: null // Will be loaded from 1Password
};

async function getCredentialFromOnePassword() {
    // This would use 1password-skill to retrieve password
    // For now, placeholder
    return 'password-from-1password';
}

function testService(service, hostname, path = '/') {
    return new Promise((resolve) => {
        const auth = 'Basic ' + Buffer.from(
            `${CREDENTIALS.username}:${CREDENTIALS.password}`
        ).toString('base64');

        const options = {
            hostname,
            port: 443,
            path,
            method: 'PROPFIND',
            headers: {
                'Authorization': auth,
                'Content-Type': 'application/xml; charset=utf-8',
                'Depth': '0'
            }
        };

        const req = https.request(options, (res) => {
            const success = res.statusCode === 207;
            resolve({
                service,
                success,
                statusCode: res.statusCode,
                needsAppPassword: res.statusCode === 401
            });
        });

        req.on('error', () => {
            resolve({ service, success: false, error: true });
        });

        req.end();
    });
}

async function testAllServices() {
    console.log('Testing iCloud Services...\n');

    // Load password from 1Password
    CREDENTIALS.password = await getCredentialFromOnePassword();

    const services = [
        { name: 'Mail (IMAP)', host: 'imap.mail.me.com' },
        { name: 'Calendar (CalDAV)', host: 'caldav.icloud.com' },
        { name: 'Contacts (CardDAV)', host: 'contacts.icloud.com' }
    ];

    const results = await Promise.all(
        services.map(s => testService(s.name, s.host))
    );

    console.log('Results:\n');
    results.forEach(r => {
        const status = r.success ? '✓' : '✗';
        const message = r.needsAppPassword
            ? '(needs app-specific password)'
            : r.success ? 'Connected!' : 'Failed';

        console.log(`${status} ${r.service}: ${message}`);
    });

    const allSuccess = results.every(r => r.success);
    if (allSuccess) {
        console.log('\n✓ All services ready!');
    } else if (results.some(r => r.needsAppPassword)) {
        console.log('\n⚠ Generate app-specific password at https://appleid.apple.com');
    }
}

testAllServices();
```

---

## 📦 Required Node.js Packages

```bash
# Install email and DAV packages
docker exec openclaw-bot sh -c "cd /home/node && npm install node-imap mailcomposer dav"
```

---

## ✅ Setup Checklist

### Step 1: Generate App-Specific Password
- [ ] Go to https://appleid.apple.com
- [ ] Sign in with agentshroud.ai@gmail.com
- [ ] Security → App-Specific Passwords
- [ ] Generate password (label: "OpenClaw Bot")
- [ ] Store in 1Password as "icloud app password"

### Step 2: Install Dependencies
```bash
docker exec openclaw-bot sh -c "cd /home/node && npm install node-imap mailcomposer dav"
```

### Step 3: Test Services
```bash
# Test Calendar
docker exec openclaw-bot node /home/node/test-icloud-calendar.js

# Test Contacts
docker exec openclaw-bot node /home/node/test-icloud-contacts.js

# Test Mail
docker exec openclaw-bot node /home/node/test-icloud-mail.js
```

### Step 4: Verify All Working
- [ ] ✓ Can connect to iCloud Mail
- [ ] ✓ Can list calendars
- [ ] ✓ Can access contacts
- [ ] ✓ Can read notes (via IMAP)

---

## 🎯 Next Steps After Setup

Once all services are working:

1. **Create OpenClaw skill** for iCloud services
2. **Integrate with AgentShroud gateway**
3. **Add to bot capabilities**
4. **Test via Telegram**

---

## 🔍 Troubleshooting

### "401 Unauthorized"
**Problem**: Wrong password or 2FA enabled
**Solution**: Generate app-specific password at appleid.apple.com

### "403 Forbidden"
**Problem**: Service not enabled in iCloud settings
**Solution**: Go to iCloud.com → Settings → Enable Mail, Calendar, Contacts

### "Connection timeout"
**Problem**: Network/firewall issues
**Solution**: Check container network access

### "Notes folder not found"
**Problem**: Notes not synced to IMAP
**Solution**: Open Notes app on Mac/iOS, wait for sync

---

**Ready to test? Let me know when you've generated the app-specific password!**
