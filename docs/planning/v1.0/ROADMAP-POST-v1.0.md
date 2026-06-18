# AgentShroud Post-v1.0.0 Roadmap

Ideas and features planned for after v1.0.0 stable release. Not prioritized yet.

---

## Apple Platform Integration

### Control Center Widget (iPhone + macOS)
- **iPhone Widget**: AgentShroud status at a glance — gateway health, recent alerts, pending approvals
- **macOS Widget**: Same data on the Mac desktop/Notification Center
- **WidgetKit**: Use SwiftUI WidgetKit for both platforms (shared code)
- **Data source**: Poll gateway /status and /approve/pending endpoints via REST API
- **Auth**: Widget authenticates with gateway token stored in Keychain (shared via App Group)

### Apple Watch Support
- Receive push notifications for:
  - Pending approval requests (with approve/deny actions on the watch)
  - Security alerts (critical/high findings)
  - Daily digest summaries
- Complication showing gateway status (healthy/degraded/down)

### Push Notifications (iPhone + Mac + Apple Watch)
- **APNs integration**: Gateway sends push notifications via Apple Push Notification service
- **Notification categories**:
  - `APPROVAL_REQUEST` — actionable (approve/deny buttons)
  - `SECURITY_ALERT` — critical findings, blocked requests
  - `DAILY_DIGEST` — morning summary of overnight activity
  - `STATUS_CHANGE` — gateway mode changes, container restarts
- **Delivery**: All three surfaces (iPhone, Mac, Apple Watch) via APNs
- **Fallback**: If APNs unavailable, fall back to Telegram notifications (current behavior)

### Implementation Notes
- Requires an Apple Developer account and APNs certificate/key
- Native Swift app (even minimal) needed to register for push and host widgets
- Could start with a simple "AgentShroud Monitor" app that just shows status + receives pushes
- Widget timeline provider can refresh every 15-30 minutes (WidgetKit limitation)
- Watch app can use WatchConnectivity or independent URLSession for data

---

*Added: 2026-03-05 by Isaiah Jefferson*
