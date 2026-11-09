# Inbound MCP Edge — Runbook

All commands run on marvin from the repo root. Dev uses the `agentshroud-bot` compose project and host port 9443; prod uses 8443. Nothing here exposes anything publicly until step 5 of §1.

## 1. First-time enablement (dev first, then prod on the owner's word)

### 1. Sign the tool descriptors (owner only, interactive terminal)

```bash
python -m gateway.inbound_edge.descriptors keygen | keyring set agentshroud-edge descriptors
python -m gateway.inbound_edge.descriptors manifest
keyring get agentshroud-edge descriptors | python -m gateway.inbound_edge.descriptors sign
python -m gateway.inbound_edge.descriptors verify          # → verify: OK
```

Commit `config/inbound-edge/descriptors.{manifest.json,manifest.sig,pub.pem}`. The private key exists only in your keychain (or use `op` in place of `keyring`).

### 2. Create the edge secrets

```bash
docker/setup-secrets.sh            # creates edge_signing_key (EC P-256) and edge_gateway_token
```

The script never echoes them. `asb` writes them into the runtime secrets.

### 3. Turn the edge on

Set `AGENTSHROUD_INBOUND_EDGE=1` and `AGENTSHROUD_EDGE_PUBLIC_URL=https://<node>.ts.net:8443` in the environment `asb` uses. Optionally set:
- `AGENTSHROUD_EDGE_PKE_FEEDS=https://…/feed.xml,…` to enable `pke_status`;
- `AGENTSHROUD_EDGE_DELEGATE=1` to seed the Hermes `edge-delegate` profile and expose `delegate_to_hermes`.

Then run `asb up`.

**Check it started:**
- The gateway log shows `Inbound MCP Edge ready: issuer=… tools=[…] vendors_enabled=[]`.
- The Command Center → Inbound Edge tab shows *enabled*.

### 4. Enable one vendor

Set `enabled: true` in `config/inbound-edge/vendors/<vendor>.yaml`, restart the gateway, then confirm in the Agents tab.

### 5. Expose publicly

**Owner approval required.** First review what would be exposed:

```bash
sudo scripts/tailscale-serve.sh edge-funnel plan     # prints exactly what would be exposed
```

Then turn it on:

```bash
sudo scripts/tailscale-serve.sh edge-funnel on --yes-expose-publicly
```

### 6. Link the vendor

```bash
asb edge enroll --vendor claude-duet               # prints a one-time code, valid 10 minutes
```

In the vendor's UI, add the custom connector `https://<node>.ts.net:8443/mcp`. When your browser reaches the consent page, enter the code. Telegram then confirms the link.

## 2. Killswitch

| Scope | Command | Effect |
|---|---|---|
| One token | `asb edge kill --jti <jti> --reason "…"` | Next request refused |
| One client | `asb edge kill --client <client_id> --reason "…"` | Next request refused; its refresh fails |
| Whole vendor | `asb edge kill --vendor <vendor> --reason "…"` | Every client of that vendor is refused |
| Everything public | `sudo scripts/tailscale-serve.sh edge-funnel off` | Port 8443 is no longer reachable from the internet |
| All agents | Command Center killswitch (freeze / shutdown / disconnect) | Also stops the edge container |

Kills are checked on every call from the database, with no cache, so they apply on the next request (`test_kill_takes_effect_within_one_second`). To restore, run `asb edge unkill …` with the same scope.

## 3. Rotating keys

### Token signing key (`edge_signing_key`)
1. Replace the secret and restart the gateway.
2. Every access token becomes invalid immediately, because signatures no longer verify.
3. Refresh tokens are unaffected but now mint under the new key.
4. Sealed client secrets become unreadable (the seal key is derived from the signing key), so affected clients must re-register. Re-enroll every linked vendor.

### Service token (`edge_gateway_token`)
Replace it, then restart the gateway and edge together.

### Descriptor signing key
Run `keygen` again, commit the new `descriptors.pub.pem`, then `sign`.

## 4. Reading the audit trail

- Every call writes an `edge_call` event to the gateway audit chain (`$AGENTSHROUD_DATA_DIR/audit.db`). Its `details` holds request id, vendor, client, jti, tool, args SHA-256, schema result, P0 score, approval, target, Hermes session id, response SHA-256, DLP counts, canary hits, latency and outcome.
- Escalations are written as `edge_lockdown` events.
- Verify the chain from the Command Center (Security → audit verify), or call `AuditStore.verify_hash_chain(start_id=…)`. Verification from a mid-chain anchor is supported.

## 5. Backout

1. `sudo scripts/tailscale-serve.sh edge-funnel off` — public exposure ends immediately.
2. `asb edge kill --vendor <each enabled vendor>`.
3. Set `AGENTSHROUD_INBOUND_EDGE=0` and run `asb up`. The gateway runs exactly as before; the edge container idles and serves 503.
4. Optionally stop the edge container. Rollback images are tagged by the Sunday upgrade job like every other service.

## 6. Troubleshooting

| Symptom | Likely cause |
|---|---|
| `Inbound MCP Edge refused to start: descriptor …` | The manifest is unsigned, stale or tampered. Run `verify`, re-sign if the change was intended. |
| `NOT started: edge_signing_key, edge_gateway_token …` | Secrets missing, or no `https` public URL. |
| Vendor registration returns 400 `registration is closed` | No open enrollment window. Run `asb edge enroll`. |
| Registration returns `invalid_redirect_uri` | The vendor's callback isn't in its profile's `redirect_uris`. |
| Calls return `denied: revoked: …` | Killed or lockdown-suspended. Check the Inbound Edge tab. |
| Write calls stay `awaiting_human_approval` | Approve in Telegram or the Approvals tab. With no decision, the request expires after 10 minutes. |
