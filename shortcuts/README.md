# iOS/macOS Shortcuts

Native OS integration for forwarding content to AgentShroud without granting direct access.

## Shortcuts (to be implemented in Week 3)

1. **universal-share.shortcut** - Universal Share Sheet integration
   - Appears in Share menu (any app)
   - Accepts: text, URLs, photos, files, contacts
   - Strips EXIF/GPS from photos
   - POST to `/forward` endpoint

2. **voice-capture.shortcut** - Voice command integration
   - "Hey Siri, send to AgentShroud"
   - Records and transcribes locally (Apple Speech framework)
   - Sends transcript only (audio never leaves device)

3. **screenshot-to-agent.shortcut** - Screenshot forwarding
   - Triggered by screenshot gesture
   - On-device OCR
   - Crops status bar (PII)
   - Sends image + extracted text

4. **clipboard-relay.shortcut** - Clipboard forwarding (macOS)
   - Menu bar shortcut
   - Opt-in clipboard monitoring
   - Hotkey to send current clipboard

5. **photo-forwarder.shortcut** - Batch photo forwarding
   - Select multiple photos
   - Strips all EXIF/GPS
   - Optional downsize
   - Sends to proxy Gmail as attachments

6. **calendar-proxy.shortcut** - Calendar event forwarding
   - Select calendar event
   - Strips attendee emails & location
   - Sends sanitized summary

7. **contact-forwarder.shortcut** - Contact sharing
   - Select contact
   - Choose fields (name only, name+phone, etc.)
   - Sends sanitized vCard

## Installation

Each shortcut will be distributed via iCloud link during setup.

## Security Features

- All processing on-device
- EXIF/GPS stripping before transmission
- PII filtering
- Confirmation toasts
- No standing access to data

## Implementation Status

🚧 **Not yet implemented** - Scheduled for Week 3
