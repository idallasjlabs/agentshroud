# Google Services Setup - Calendar, Contacts, Keep

**Date**: 2026-02-16
**Account**: therealidallasj@gmail.com
**Purpose**: Shared Google services for AgentShroud bot

---

## 📧 Gmail Already Working

✅ Credentials stored in 1Password
✅ IMAP/SMTP access configured
✅ App password available

---

## 📅 Google Calendar (CalDAV)

### Server Settings

**CalDAV URL**: `https://apidata.googleusercontent.com/caldav/v2/`

**Authentication**:
- Username: `therealidallasj@gmail.com`
- Password: [App password from 1Password]

### Python Integration

```python
import caldav
from datetime import datetime

# Retrieve credentials from 1Password
username = "therealidallasj@gmail.com"
password = get_credential("gmail-app-password")

# Connect to Google Calendar via CalDAV
client = caldav.DAVClient(
    url="https://apidata.googleusercontent.com/caldav/v2/",
    username=username,
    password=password
)

# Get calendars
principal = client.principal()
calendars = principal.calendars()

# Create event
calendar = calendars[0]
event = calendar.save_event(
    dtstart=datetime(2026, 2, 20, 10, 0),
    dtend=datetime(2026, 2, 20, 11, 0),
    summary="Meeting with Bot",
    description="Automated event creation test"
)
print(f"Event created: {event.url}")
```

### CLI Tool: gcalcli

```bash
# Install
pip3 install gcalcli

# Setup (one-time OAuth)
gcalcli init

# List events
gcalcli agenda

# Add event
gcalcli add "Meeting tomorrow at 2pm"

# Quick add (natural language)
gcalcli quick "Lunch with team next Monday at noon"
```

---

## 📞 Google Contacts (CardDAV)

### Server Settings

**CardDAV URL**: `https://www.googleapis.com/carddav/v1/principals/therealidallasj@gmail.com/lists/default/`

**Authentication**:
- Username: `therealidallasj@gmail.com`
- Password: [App password from 1Password]

### Python Integration

```python
import vobject
import requests
from requests.auth import HTTPBasicAuth

username = "therealidallasj@gmail.com"
password = get_credential("gmail-app-password")

# CardDAV endpoint
carddav_url = f"https://www.googleapis.com/carddav/v1/principals/{username}/lists/default/"

# Get contacts
response = requests.request(
    'PROPFIND',
    carddav_url,
    auth=HTTPBasicAuth(username, password),
    headers={'Depth': '1'}
)

# Parse contacts
# (vCard format)
```

### Alternative: Google People API

**Better option** - Use Google People API with OAuth:

```python
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# After OAuth setup
service = build('people', 'v1', credentials=creds)

# List contacts
results = service.people().connections().list(
    resourceName='people/me',
    personFields='names,emailAddresses,phoneNumbers'
).execute()

contacts = results.get('connections', [])
for person in contacts:
    names = person.get('names', [])
    if names:
        print(names[0].get('displayName'))
```

---

## 📝 Google Keep (Notes)

### Problem: No Public API

Google Keep has **no official public API**.

### Workarounds:

**Option 1: Unofficial gkeepapi** (Python library)
```bash
pip3 install gkeepapi
```

```python
import gkeepapi

keep = gkeepapi.Keep()
success = keep.login('therealidallasj@gmail.com', 'password')

# Create note
note = keep.createNote('My Title', 'My note content')
keep.sync()

# List notes
gnotes = keep.all()
for note in gnotes:
    print(note.title)
```

**Security Warning**: This uses internal Google APIs that could break at any time. Not recommended for production.

**Option 2: Use Google Docs Instead**

Google Docs has a proper API:

```python
from googleapiclient.discovery import build

service = build('docs', 'v1', credentials=creds)

# Create document
document = service.documents().create(body={
    'title': 'My Note'
}).execute()

# Add content
requests = [{
    'insertText': {
        'location': {'index': 1},
        'text': 'Note content here'
    }
}]
service.documents().batchUpdate(
    documentId=document['documentId'],
    body={'requests': requests}
).execute()
```

**Option 3: Use Different Notes App**

Consider switching to a notes app with a proper API:
- **Notion** (excellent API)
- **Obsidian** (local markdown files)
- **Apple Notes** (if you get Apple ID working)
- **Standard Notes** (encrypted, has API)

---

## 🔐 Setup Steps

### Step 1: Enable App Password (Gmail)

You already have this in 1Password: `nkcy luwd cwou zimj`

### Step 2: Enable CalDAV/CardDAV Access

Should be enabled by default for Google accounts. No action needed.

### Step 3: Test Calendar Access

```bash
docker exec openclaw-bot pip3 install caldav

docker exec openclaw-bot python3 << 'PYTHON'
import caldav

client = caldav.DAVClient(
    url="https://apidata.googleusercontent.com/caldav/v2/",
    username="therealidallasj@gmail.com",
    password="nkcy luwd cwou zimj"
)

try:
    principal = client.principal()
    calendars = principal.calendars()
    print(f"✓ Connected! Found {len(calendars)} calendars:")
    for cal in calendars:
        print(f"  - {cal.name}")
except Exception as e:
    print(f"✗ Error: {e}")
PYTHON
```

### Step 4: Test Contacts Access

```bash
docker exec openclaw-bot pip3 install vobject requests

# Test CardDAV access
docker exec openclaw-bot python3 << 'PYTHON'
import requests
from requests.auth import HTTPBasicAuth

username = "therealidallasj@gmail.com"
password = "nkcy luwd cwou zimj"

url = f"https://www.googleapis.com/carddav/v1/principals/{username}/lists/default/"

try:
    response = requests.request(
        'PROPFIND',
        url,
        auth=HTTPBasicAuth(username, password),
        headers={'Depth': '0'}
    )
    print(f"✓ CardDAV Status: {response.status_code}")
    if response.status_code == 207:
        print("✓ Connected successfully!")
    else:
        print(f"Response: {response.text}")
except Exception as e:
    print(f"✗ Error: {e}")
PYTHON
```

---

## 🚀 Recommended Approach

### For Immediate Use: CalDAV/CardDAV

**Pros**:
- ✅ No OAuth setup needed
- ✅ Uses existing app password
- ✅ Works immediately
- ✅ Simple authentication

**Cons**:
- ❌ Less features than full API
- ❌ Slower than REST APIs
- ❌ Limited query capabilities

**Best for**: Basic calendar/contact operations

### For Production: OAuth2 + Google APIs

**Pros**:
- ✅ Full API features
- ✅ Better performance
- ✅ More control
- ✅ Official Google support

**Cons**:
- ❌ Requires OAuth setup
- ❌ Need Google Cloud project
- ❌ One-time browser consent

**Best for**: Advanced features, high volume

---

## 🛠️ OAuth2 Setup (If Needed)

### Step 1: Create Google Cloud Project

1. Go to https://console.cloud.google.com
2. Create new project: "AgentShroud Bot"
3. Enable APIs:
   - Google Calendar API
   - Google People API (Contacts)
   - Google Docs API (if using for notes)

### Step 2: Create OAuth Credentials

1. Go to Credentials → Create Credentials → OAuth Client ID
2. Application type: Desktop app
3. Name: "AgentShroud Bot"
4. Download JSON credentials

### Step 3: Store Credentials

```bash
# Add to 1Password
docker exec openclaw-bot 1password-skill create-item \
  --vault "AgentShroud Bot Credentials" \
  --title "Google OAuth Client" \
  --type "login" \
  --field "client_id" "[from JSON]" \
  --field "client_secret" "[from JSON]"
```

### Step 4: Get Refresh Token

```python
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/contacts'
]

flow = InstalledAppFlow.from_client_secrets_file(
    'credentials.json',
    scopes=SCOPES
)

# This opens browser for consent
creds = flow.run_local_server(port=0)

# Save refresh token to 1Password
print(f"Refresh token: {creds.refresh_token}")
```

---

## 📊 Comparison: CalDAV vs OAuth2

| Feature | CalDAV/CardDAV | OAuth2 + API |
|---------|----------------|--------------|
| Setup time | 5 minutes | 30 minutes |
| Authentication | App password | OAuth tokens |
| Features | Basic | Full |
| Performance | Slower | Faster |
| Complexity | Simple | Complex |
| Official support | Yes | Yes |
| **Recommendation** | **Start here** | Upgrade later |

---

## ✅ Quick Start Command

```bash
# Install dependencies
docker exec openclaw-bot pip3 install caldav vobject requests google-api-python-client google-auth-oauthlib

# Test calendar access
docker exec openclaw-bot python3 -c "
import caldav
client = caldav.DAVClient(
    url='https://apidata.googleusercontent.com/caldav/v2/',
    username='therealidallasj@gmail.com',
    password='nkcy luwd cwou zimj'
)
print('Calendars:', [c.name for c in client.principal().calendars()])
"
```

---

## 🎯 Next Steps

### Option A: Quick CalDAV Setup (Recommended)
1. Run test commands above
2. Verify calendar/contact access works
3. Start using basic features immediately

### Option B: Full OAuth Setup
1. Create Google Cloud project
2. Set up OAuth credentials
3. Get refresh token
4. Use full Google APIs

### Option C: Alternative Notes Solution
1. Skip Google Keep (no API)
2. Use Notion, Obsidian, or Google Docs
3. All have proper APIs

---

**Which approach would you like to take?**
