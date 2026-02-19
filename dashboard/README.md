# AgentShroud Dashboard

Real-time observability and control interface for AgentShroud.

## Components (to be implemented in Week 2)

```
dashboard/
├── src/
│   ├── ActionFeed.jsx         # Live action stream
│   ├── DataLedger.jsx         # Forwarded content viewer
│   ├── MemoryViewer.jsx       # MEMORY.md browser
│   ├── NetworkInspector.jsx   # Outbound requests
│   └── KillSwitch.jsx         # Emergency halt
├── public/
├── package.json
└── README.md
```

## Features

### Action Feed
- WebSocket connection to OpenClaw gateway logs
- Live stream of skills invoked, commands run, API calls
- Color-coded by risk (green/yellow/red)
- "Halt this action" button

### Data Ledger Viewer
- Searchable table of all forwarded content
- Columns: timestamp, source, type, size, sanitized
- "Forget this" button for secure deletion

### Memory Browser
- Renders MEMORY.md in categorized format
- Highlights PII, credentials, suspicious directives
- Manual edit and automated scrub options

### Network Inspector
- Shows all outbound requests (domain, size, method)
- Unknown domains auto-blocked + flagged
- Real-time whitelist/blacklist

### Kill Switch
- Big red button: halt all agent activity
- Freezes container, preserves state
- Logs incident for forensics

## Tech Stack

- React 18
- Tailwind CSS
- WebSocket (live updates)
- Recharts (graphs)

## Implementation Status

🚧 **Not yet implemented** - Scheduled for Week 2
