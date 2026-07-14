# Browser Extension

Forward web content to AgentShroud without exposing cookies, session tokens, or trackers.

## Structure

```
browser-extension/
├── manifest.json         # Manifest V3 configuration
├── background.js         # Service worker: context menus, tab query, script injection, transport
├── lib/forwarder.js      # Pure logic: payload construction + gateway POST (unit-tested)
├── lib/forwarder.test.js # Jest tests (mocked fetch, no network)
├── popup.html / popup.js # Toolbar popup UI (Forward URL / Clip page)
├── options.html / .js    # Gateway URL + token settings (chrome.storage.sync)
├── icons/                # Extension icons
└── package.json          # Jest test harness
```

### Gateway wiring

Both actions POST a `ForwardRequest` to `<gatewayUrl>/forward`
(`gateway/ingest_api/routes/forward.py:326`) with an
`Authorization: Bearer <token>` header:

| Action | `content` | `content_type` | `metadata.kind` |
|--------|-----------|----------------|-----------------|
| Forward URL | the tab URL | `url` | `url_forward` |
| Clip page | readable text / selection | `text` | `page_clip` |

Configure the gateway URL and token in the extension's options page — no token
is ever hardcoded.

### Tests

```bash
cd browser-extension
npm install
npm test              # jest, mocked fetch, no network
npm run test:coverage
```

### Safari

Safari uses the same MV3 sources wrapped with Xcode's
`xcrun safari-web-extension-converter .` — no separate JavaScript is required.

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

✅ **URL forwarder + page clipper implemented** (MV3, Chrome/Firefox; Safari via
converter). Features 3–5 (form fill, tab exporter, reading list) remain planned.
