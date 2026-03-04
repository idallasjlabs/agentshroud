---
title: Egress Filter Errors
type: troubleshooting
tags: [egress, networking, errors]
related: [Security Modules/egress_filter.py, Configuration/agentshroud.yaml, Errors & Troubleshooting/Error Index]
status: documented
---

# Egress Filter Errors

## HTTP 403 — Egress Blocked

The egress filter rejected an outbound request because the destination domain or IP was not in the allowlist.

### Diagnosis

```bash
# Look for blocked domain in logs
docker logs agentshroud-gateway | grep "Egress blocked"
# Output: "Egress blocked: domain not in allowlist: example.com"
```

### Fix: Add Domain to Allowlist

1. Edit `agentshroud.yaml`:
```yaml
proxy:
  allowed_domains:
    - api.openai.com
    - api.anthropic.com
    - your-new-domain.com    # Add here
    - "*.your-wildcard.com"  # Wildcard (must be quoted)
```

2. Restart gateway:
```bash
docker compose restart agentshroud-gateway
```

### Common Missing Domains

| Service | Domain to Add |
|---------|--------------|
| Brave Search | `api.search.brave.com` |
| iCloud IMAP | `imap.mail.me.com` |
| iCloud SMTP | `smtp.mail.me.com` |
| Google OAuth | `oauth2.googleapis.com` |
| Google APIs | `www.googleapis.com`, `gmail.googleapis.com` |
| npm registry | `registry.npmjs.org` |
| GitHub | `*.github.com`, `*.githubusercontent.com` |

---

## RFC1918 Blocked

**Error:** `RFC1918 address blocked: 192.168.x.x`

**Cause:** Attempt to reach a private network address. This is intentional security behavior.

**If you need to reach a local service:**
- Use Tailscale to give the service a public IP
- Or run the service inside the `agentshroud-isolated` Docker network

---

## Egress Filter Not Initialized

**Error (500):** `Egress filter not initialized`

**Cause:** Gateway started without loading the egress filter (module initialization failed)

**Fix:**
```bash
docker logs agentshroud-gateway | grep -i "egress"
docker compose restart agentshroud-gateway
```

---

## Monitor Mode — Egress Not Enforced

**Symptom:** Blocked domains are getting through

**Cause:** `AGENTSHROUD_MODE=monitor` is set

**Fix:**
```bash
# Verify current mode
docker exec agentshroud-gateway env | grep AGENTSHROUD_MODE

# Remove monitor mode
docker compose stop agentshroud-gateway
# Edit docker-compose.yml to remove AGENTSHROUD_MODE=monitor
docker compose up -d agentshroud-gateway
```

---

## Related Notes

- [[Security Modules/egress_filter.py|egress_filter.py]] — Egress filter implementation
- [[Configuration/agentshroud.yaml]] — `proxy.allowed_domains` config
- [[Environment Variables/HTTP_PROXY]] — Network-layer egress (future)
- [[Errors & Troubleshooting/Error Index]] — Full error index
