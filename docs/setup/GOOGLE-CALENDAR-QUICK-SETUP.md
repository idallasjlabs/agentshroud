# Google Calendar & Contacts - Quick Setup

**Status**: ✅ Google APIs Node.js packages installed
**Date**: 2026-02-16

---

## 🎯 Two Options

### Option A: Simple (App Password + CalDAV) - RECOMMENDED FOR NOW
No OAuth setup needed, works immediately

### Option B: Full (OAuth2 + Google APIs) - Better for production
Requires one-time browser consent, then full API access

---

## 🚀 Option A: Simple Setup (5 minutes)

Since the OpenClaw container doesn't have Python pip or the gog CLI easily available, let's use a **lightweight Node.js approach** with CalDAV:

### Install Node CalDAV Client

```bash
docker exec openclaw-bot sh -c "cd /home/node && npm install caldav-client"
```

### Create Test Script

Create `/home/node/test-google-calendar.js`:

```javascript
const fetch = require('node-fetch');

async function testGoogleCalendar() {
    const username = 'therealidallasj@gmail.com';
    const password = 'nkcy luwd cwou zimj'; // App password from 1Password

    // Google CalDAV endpoint
    const caldavUrl = 'https://apidata.googleusercontent.com/caldav/v2/';

    // Basic auth
    const auth = 'Basic ' + Buffer.from(username + ':' + password).toString('base64');

    try {
        // PROPFIND request to list calendars
        const response = await fetch(caldavUrl, {
            method: 'PROPFIND',
            headers: {
                'Authorization': auth,
                'Content-Type': 'application/xml',
                'Depth': '1'
            },
            body: `<?xml version="1.0" encoding="utf-8" ?>
                <D:propfind xmlns:D="DAV:" xmlns:C="urn:ietf:params:xml:ns:caldav">
                    <D:prop>
                        <D:displayname/>
                        <D:resourcetype/>
                    </D:prop>
                </D:propfind>`
        });

        console.log('Status:', response.status);
        const text = await response.text();
        console.log('Response:', text.substring(0, 500));

        if (response.status === 207) {
            console.log('\n✓ Connected to Google Calendar successfully!');
        }
    } catch (error) {
        console.error('✗ Error:', error.message);
    }
}

testGoogleCalendar();
```

### Run Test

```bash
docker exec openclaw-bot node /home/node/test-google-calendar.js
```

---

## 🎮 Option B: Using Google APIs (Better but requires OAuth)

The Google APIs we installed (googleapis) are more powerful but need OAuth setup.

### Step 1: Create Google Cloud Project

1. Go to https://console.cloud.google.com
2. Create project: "SecureClaw Bot"
3. Enable APIs:
   - Google Calendar API
   - Google People API (Contacts)

### Step 2: Create OAuth Credentials

1. Go to APIs & Services → Credentials
2. Create Credentials → OAuth Client ID
3. Application type: **Desktop app**
4. Name: "SecureClaw Bot"
5. Download JSON → Save as `credentials.json`

### Step 3: Get OAuth Token (One-Time)

Create `/home/node/get-google-token.js`:

```javascript
const {google} = require('googleapis');
const fs = require('fs');
const readline = require('readline');

const SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/contacts'
];

async function getToken() {
    // Load client secrets
    const credentials = JSON.parse(fs.readFileSync('credentials.json'));
    const {client_secret, client_id, redirect_uris} = credentials.installed;

    const oAuth2Client = new google.auth.OAuth2(
        client_id,
        client_secret,
        redirect_uris[0]
    );

    // Generate auth URL
    const authUrl = oAuth2Client.generateAuthUrl({
        access_type: 'offline',
        scope: SCOPES,
    });

    console.log('Authorize this app by visiting this url:', authUrl);
    console.log('\nPaste the code from that page here:');

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    });

    rl.question('', async (code) => {
        rl.close();
        try {
            const {tokens} = await oAuth2Client.getToken(code);
            console.log('\nTokens received!');
            console.log('Store this refresh_token in 1Password:');
            console.log(tokens.refresh_token);

            // Save tokens
            fs.writeFileSync('token.json', JSON.stringify(tokens));
            console.log('\n✓ Token saved to token.json');
        } catch (err) {
            console.error('Error retrieving access token', err);
        }
    });
}

getToken();
```

### Step 4: Use Google Calendar

Create `/home/node/use-google-calendar.js`:

```javascript
const {google} = require('googleapis');
const fs = require('fs');

async function listCalendarEvents() {
    // Load credentials and token
    const credentials = JSON.parse(fs.readFileSync('credentials.json'));
    const token = JSON.parse(fs.readFileSync('token.json'));

    const {client_secret, client_id, redirect_uris} = credentials.installed;
    const oAuth2Client = new google.auth.OAuth2(
        client_id,
        client_secret,
        redirect_uris[0]
    );

    oAuth2Client.setCredentials(token);

    // Create calendar API client
    const calendar = google.calendar({version: 'v3', auth: oAuth2Client});

    try {
        // List events
        const res = await calendar.events.list({
            calendarId: 'primary',
            timeMin: (new Date()).toISOString(),
            maxResults: 10,
            singleEvents: true,
            orderBy: 'startTime',
        });

        const events = res.data.items;
        if (events.length) {
            console.log('Upcoming events:');
            events.forEach((event, i) => {
                const start = event.start.dateTime || event.start.date;
                console.log(`${i+1}. ${start} - ${event.summary}`);
            });
        } else {
            console.log('No upcoming events found.');
        }

        // Create event
        const event = {
            summary: 'Test Event from SecureClaw',
            start: {
                dateTime: '2026-02-20T10:00:00-08:00',
                timeZone: 'America/Los_Angeles',
            },
            end: {
                dateTime: '2026-02-20T11:00:00-08:00',
                timeZone: 'America/Los_Angeles',
            },
        };

        const createRes = await calendar.events.insert({
            calendarId: 'primary',
            resource: event,
        });

        console.log('\n✓ Event created:', createRes.data.htmlLink);

    } catch (error) {
        console.error('Error:', error.message);
    }
}

listCalendarEvents();
```

---

## 📊 Comparison

| Feature | Option A (CalDAV) | Option B (Google APIs) |
|---------|-------------------|----------------------|
| Setup time | 5 min | 30 min (OAuth) |
| Browser needed | No | Yes (one-time) |
| Authentication | App password | OAuth tokens |
| API features | Basic | Full |
| Complexity | Low | Medium |
| **Best for** | **Quick start** | **Production** |

---

## 🎯 My Recommendation

**Start with Option A** (CalDAV via Node.js):
1. Simple, works now
2. No OAuth complexity
3. Uses existing app password
4. Good enough for basic calendar/contact operations

**Upgrade to Option B later** if you need:
- Advanced features
- Better performance
- More control

---

## ⚡ Fastest Path Forward

Since you want to **use calendar and contacts now with your bot**, let's create a simple Node.js script:

```bash
# Create simple calendar helper
cat > /tmp/google-calendar-helper.js << 'EOF'
#!/usr/bin/env node
const https = require('https');

const username = 'therealidallasj@gmail.com';
const password = 'nkcy luwd cwou zimj';
const auth = 'Basic ' + Buffer.from(username + ':' + password).toString('base64');

function makeCalDAVRequest(method, path, body = '') {
    return new Promise((resolve, reject) => {
        const options = {
            hostname: 'apidata.googleusercontent.com',
            port: 443,
            path: '/caldav/v2/' + path,
            method: method,
            headers: {
                'Authorization': auth,
                'Content-Type': 'application/xml; charset=utf-8',
                'Content-Length': Buffer.byteLength(body),
                'Depth': '1'
            }
        };

        const req = https.request(options, (res) => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => resolve({status: res.statusCode, data}));
        });

        req.on('error', reject);
        if (body) req.write(body);
        req.end();
    });
}

async function listCalendars() {
    const body = `<?xml version="1.0" encoding="utf-8" ?>
        <D:propfind xmlns:D="DAV:">
            <D:prop><D:displayname/></D:prop>
        </D:propfind>`;

    const result = await makeCalDAVRequest('PROPFIND', '', body);
    console.log('Calendars:', result.status === 207 ? '✓ Found' : '✗ Error');
    if (result.status === 207) {
        console.log(result.data);
    }
}

const command = process.argv[2];
if (command === 'list') {
    listCalendars().catch(console.error);
} else {
    console.log('Usage: google-calendar-helper.js list');
}
EOF

# Copy to container
docker cp /tmp/google-calendar-helper.js openclaw-bot:/home/node/google-calendar-helper.js
docker exec openclaw-bot chmod +x /home/node/google-calendar-helper.js

# Test it
docker exec openclaw-bot node /home/node/google-calendar-helper.js list
```

---

## ✅ Next Steps

**Right now** (to unblock you):
1. Run the script above to test calendar access
2. If it works, we can extend it for:
   - Creating events
   - Listing events
   - Updating events
   - Managing contacts

**Later** (for production):
1. Set up OAuth2 properly
2. Create a proper OpenClaw skill
3. Integrate with SecureClaw gateway

**Want me to run the test script now?**
