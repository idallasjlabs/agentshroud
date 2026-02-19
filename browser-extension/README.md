# Browser Extension

Forward web content to AgentShroud without exposing cookies, session tokens, or trackers.

## Structure (to be implemented in Week 3-4)

```
browser-extension/
├── manifest.json       # Manifest V3 configuration
├── popup.html          # Extension popup UI
├── content.js          # Page content extraction
├── background.js       # Background service worker
├── icons/              # Extension icons
└── safari/             # Safari Web Extension wrapper
```

## Features

### 1. URL Forwarder
- Toolbar button + right-click menu
- Sends: current URL, title, selected text, user instruction
- Does NOT send: cookies, session tokens, DOM

### 2. Page Clipper
- Select region of page
- Readability-style extraction (strips ads/trackers)
- Sends sanitized content

### 3. Form Fill Request (Reverse Flow)
- Send form field names to agent
- Agent returns suggested values
- Review/approve in extension popup
- Fill fields on approval

### 4. Tab Session Exporter
- Export open tabs (URLs + titles only)
- PII filter on titles
- Send to agent for categorization

### 5. Reading List Queue
- One-click "Read Later with AI"
- Agent processes async
- Results in dashboard

## Privacy Features

- Manifest V3 (minimal permissions)
- Permissions: `tabs`, `activeTab` only
- No cookie access
- No session token access
- Readability mode (strips trackers)

## Browser Support

- Chrome/Chromium
- Firefox
- Safari (via Web Extension wrapper)
- Edge

## Implementation Status

🚧 **Not yet implemented** - Scheduled for Week 3-4, Days 22-23
