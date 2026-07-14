# iOS / macOS Shortcuts — Relay to AgentShroud

> **AgentShroud™** — USPTO Serial No. 99728633 · Patent Pending No. 64/018,744

Native Apple Shortcuts that forward content (share-sheet text/URL/photo, Siri
voice capture, screenshots, clipboard) to the AgentShroud gateway `/forward`
ingest endpoint — the **same endpoint** the browser extension uses. Nothing is
granted standing access: each Shortcut builds one HTTPS `POST` with a Bearer
token and hands the payload to the gateway, which runs it through the full
security pipeline (PII redaction, prompt-guard, audit hash-chain, egress policy)
before any agent sees it.

> **Why a recipe and not a `.shortcut` file?** `.shortcut` files are opaque,
> signed binary property lists. A committed binary cannot be reviewed, diffed,
> or trusted in a security product, and Apple re-signs them per-account on
> import anyway. This document is the **reproducible recipe** — every action,
> in order, plus the exact request contract — so you can build each Shortcut by
> hand in the Shortcuts app in a few minutes and know precisely what it sends.

---

## The `/forward` contract (authoritative)

All Shortcuts POST to the gateway's ingest endpoint. The contract below is taken
directly from the gateway source; cited so it stays honest.

| Item | Value | Source of truth |
|------|-------|-----------------|
| Method / path | `POST <gateway>/forward` | `gateway/ingest_api/routes/forward.py:326` |
| Auth | `Authorization: Bearer <token>` (constant-time compared) | `gateway/ingest_api/auth.py:120-146` |
| Content type | `Content-Type: application/json` | — |
| Success status | `201 Created` (`202` if queued for approval) | `forward.py:326`, `forward.py:435-442` |

### Request body — `ForwardRequest`

Defined in `gateway/ingest_api/models.py:20-68`.

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `content` | string, ≤ 100 000 chars, non-empty | ✅ | The text/data being forwarded (`models.py:26`, `models.py:47-52`) |
| `source` | string, allowlisted | ✅ | **Must be `"shortcut"`** for these recipes (`models.py:54-68`) |
| `content_type` | `"text" \| "url" \| "photo" \| "file"` | — (default `"text"`) | Closed set (`models.py:32-34`) |
| `metadata` | object | — | Free-form routing hints/context (`models.py:35-37`) |
| `route_to` | string | — | Optional explicit target agent (`models.py:38-40`) |

**Source allowlist** (`models.py:57-65`) — the accepted values are:
`shortcut`, `browser_extension`, `script`, `api`, `telegram`, `chat-console`,
`control-center`. **Apple Shortcuts use `shortcut`** (there is no separate
`ios_shortcut` value — do not invent one; the gateway will reject it).

### Response body — `ForwardResponse`

Defined in `gateway/ingest_api/models.py:100-117`. Fields you may want to surface
in a Shortcut confirmation toast:

| Field | Meaning |
|-------|---------|
| `id` | Ledger entry UUID |
| `forwarded_to` | Target agent name (e.g. `openclaw`, `hermes`) |
| `sanitized` / `redaction_count` | Whether/how much PII was redacted by the gateway |
| `agent_response` | The agent's reply, if one was produced |

### Canonical request (copy-paste `curl` to validate before building Shortcuts)

Replace `<gateway>` (e.g. `https://marvin.tailnet.ts.net:8080`) and `<TOKEN>`
with your real values. **Never commit a real token.**

```bash
curl -sS -X POST "<gateway>/forward" \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
        "content": "hello from my iPhone",
        "source": "shortcut",
        "content_type": "text",
        "metadata": {"kind": "share_sheet", "app": "Notes"}
      }'
```

A `201` with a JSON body containing `"forwarded_to"` means the whole path
(auth → pipeline → routing → ledger) worked.

---

## One-time setup (do this first)

1. **Get your gateway URL.** The gateway binds to loopback and is reached over
   Tailscale (see the project README). Use the Tailscale MagicDNS name and port,
   e.g. `https://marvin.tailnet.ts.net:8080`. HTTPS is strongly recommended so
   the Bearer token never crosses the wire in clear text.
2. **Get your Bearer token.** This is the gateway `auth_token`
   (`gateway/ingest_api/config.py`, set from your gateway secret). Treat it like
   a password.
3. **Store both once, reuse everywhere.** In the Shortcuts app create a
   dedicated shortcut named **"AS Config"** with two **Text** actions feeding a
   **Dictionary**, or simpler: store the token in an iCloud Keychain / a
   Shortcuts *Text* action inside each shortcut. For a shared secret across
   shortcuts, use the **"Get Value for Key"** pattern against a single
   Dictionary shortcut you call. The recipes below inline the two values for
   clarity — factor them out if you prefer.

> **Security note:** anyone who can read the Shortcut can read the token. Keep
> these shortcuts on a personal, passcode-locked device. Rotate the gateway
> token if a device is lost.

---

## Recipe A — Share Sheet: text / URL

Sends selected text or a shared link from any app's Share menu.

**Shortcut settings**
- In the shortcut's settings (ⓘ), enable **Show in Share Sheet**.
- **Accepted Types:** *Text*, *URLs*, *Safari web pages*, *Articles*.

**Actions (in order):**
1. **Receive** *Text* and *URLs* input from *Share Sheet*.
   - (Shortcut input) → variable **ShortcutInput**.
2. **Text** action → `<TOKEN>` → name it **Token**.
3. **Text** action → `<gateway>` → name it **Gateway**.
4. **If** *Shortcut Input* is a **URL** → set **CType** = `url`, otherwise
   **CType** = `text`. (Simplest: use *Get Type* + an *If*.) When in doubt,
   `text` is always valid.
5. **Dictionary** action, keys:
   - `content` → **Shortcut Input** (the shared text or URL).
   - `source` → `shortcut`
   - `content_type` → **CType** variable (`text` or `url`).
   - `metadata` → **Dictionary**: `{ "kind": "share_sheet" }`
6. **Get Contents of URL** action:
   - **URL:** `Gateway` + `/forward` (use the *Gateway* text variable, append `/forward`).
   - **Method:** `POST`
   - **Headers:**
     - `Authorization` → `Bearer ` + **Token**
     - `Content-Type` → `application/json`
   - **Request Body:** **JSON** → the **Dictionary** from step 5.
7. **Get Dictionary from Input** (parse the JSON response) → **Get Value for Key**
   `forwarded_to`.
8. **Show Notification** → `Sent to [forwarded_to]`.

Body actually sent:

```json
{ "content": "<shared text or URL>", "source": "shortcut",
  "content_type": "url", "metadata": { "kind": "share_sheet" } }
```

---

## Recipe B — Siri voice capture ("Hey Siri, send to AgentShroud")

Speak a message; only the **transcript** leaves the device (audio never does).

**Shortcut settings**
- Rename the shortcut to a Siri-friendly phrase, e.g. **"Send to AgentShroud"**.
  Invoke with *"Hey Siri, Send to AgentShroud"*.

**Actions (in order):**
1. **Dictate Text** (language of your choice). On-device Apple Speech produces a
   transcript → variable **Dictated**.
2. **If** *Dictated* *has any value* — otherwise **Stop and Show** "Nothing heard".
3. **Text** `<TOKEN>` → **Token**; **Text** `<gateway>` → **Gateway**.
4. **Dictionary**:
   - `content` → **Dictated**
   - `source` → `shortcut`
   - `content_type` → `text`
   - `metadata` → `{ "kind": "voice_capture" }`
5. **Get Contents of URL** → `POST` `Gateway/forward`, headers as in Recipe A,
   **Request Body: JSON** = the Dictionary.
6. **Get Value for Key** `agent_response` from the parsed response → **Speak Text**
   (so Siri reads the agent's reply back to you).

Body actually sent:

```json
{ "content": "<transcript>", "source": "shortcut",
  "content_type": "text", "metadata": { "kind": "voice_capture" } }
```

---

## Recipe C — Screenshot relay (OCR text)

Because `content` is a **text** field capped at 100 000 chars
(`models.py:26`), a full base64 screenshot usually will not fit. The reliable,
privacy-preserving pattern is **on-device OCR → send the extracted text** with
`content_type: "photo"` so the agent knows the origin was an image.

**Trigger:** run manually, or via an **Automation** (Personal Automation →
*Screenshot taken*).

**Actions (in order):**
1. **Get Latest Screenshots** (Count 1) → **Screenshot**.
   *(Or use the automation's provided screenshot input.)*
2. **Extract Text from Image** (**Screenshot**) → variable **OCRText**
   (100% on-device Vision OCR).
3. **If** **OCRText** *has any value* — otherwise stop.
4. **Text** `<TOKEN>` → **Token**; **Text** `<gateway>` → **Gateway**.
5. **Dictionary**:
   - `content` → **OCRText**
   - `source` → `shortcut`
   - `content_type` → `photo`
   - `metadata` → `{ "kind": "screenshot_ocr" }`
6. **Get Contents of URL** → `POST` `Gateway/forward`, headers as above,
   **Request Body: JSON** = the Dictionary.
7. **Show Notification** with `forwarded_to`.

Body actually sent:

```json
{ "content": "<OCR text from screenshot>", "source": "shortcut",
  "content_type": "photo", "metadata": { "kind": "screenshot_ocr" } }
```

> **Sending the actual image bytes?** If you truly need pixels (small images
> only), add a **Base64 Encode** action on the image and put the string in
> `content` with `content_type: "photo"`. Keep the encoded length under
> ~100 000 chars — **Resize Image** to a small dimension and use JPEG first, or
> the gateway will reject the body (`models.py:26`). OCR text is the recommended
> default.

---

## Recipe D — Clipboard relay (macOS menu bar / iOS)

Send whatever is on the clipboard right now.

**Shortcut settings (macOS):** enable **Pin in Menu Bar** for one-click access,
or assign a keyboard shortcut in the Shortcuts app.

**Actions (in order):**
1. **Get Clipboard** → **Clip**.
2. **If** **Clip** *has any value* — otherwise stop with "Clipboard empty".
3. **Text** `<TOKEN>` → **Token**; **Text** `<gateway>` → **Gateway**.
4. **Dictionary**:
   - `content` → **Clip**
   - `source` → `shortcut`
   - `content_type` → `text` (use `url` if the clipboard holds a single link)
   - `metadata` → `{ "kind": "clipboard" }`
5. **Get Contents of URL** → `POST` `Gateway/forward`, headers as above,
   **Request Body: JSON** = the Dictionary.
6. **Show Notification** with `forwarded_to`.

Body actually sent:

```json
{ "content": "<clipboard contents>", "source": "shortcut",
  "content_type": "text", "metadata": { "kind": "clipboard" } }
```

---

## Recipe E — Share Sheet: photo relay

For photos, the same 100 000-char ceiling applies. Two supported patterns:

1. **OCR text (recommended):** *Extract Text from Image* → send as
   `content_type: "photo"` (identical to Recipe C but sourced from the Share
   Sheet photo instead of a screenshot).
2. **Encoded thumbnail (small images):** *Resize Image* (e.g. longest side 512
   px) → *Convert Image* to JPEG → *Base64 Encode* → send the string as
   `content` with `content_type: "photo"`.

**Shortcut settings:** enable **Show in Share Sheet**, Accepted Types
**Images**.

Body actually sent (OCR variant):

```json
{ "content": "<OCR text or base64 thumbnail>", "source": "shortcut",
  "content_type": "photo", "metadata": { "kind": "photo_relay" } }
```

---

## Content-type quick reference

| Shortcut | `content` holds | `content_type` |
|----------|-----------------|----------------|
| Share text | the shared/selected text | `text` |
| Share URL | the link | `url` |
| Siri voice | on-device transcript | `text` |
| Screenshot | OCR text (or small base64) | `photo` |
| Clipboard | clipboard contents | `text` (or `url`) |
| Photo relay | OCR text (or small base64) | `photo` |
| Shared document | extracted/summarized text | `file` |

All use `source: "shortcut"`.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `401 Authentication required` | Missing/blank `Authorization` header | Header must be exactly `Bearer <token>` (`auth.py:120-135`) |
| `401 Invalid authentication token` | Wrong token | Match the gateway `auth_token` (`auth.py:140`) |
| `422 Unprocessable Entity`, "source must be one of" | Wrong `source` | Use `shortcut` (`models.py:57-67`) |
| `422`, "content must not be empty" | Empty/whitespace `content` | Guard with an *If has any value* action (`models.py:47-52`) |
| `422`, content_type error | Sent a type outside the closed set | Use `text`/`url`/`photo`/`file` (`models.py:32`) |
| Body rejected as too large | Content > 100 000 chars | Prefer OCR text; resize/encode smaller (`models.py:26`) |
| `429 Too Many Requests` | Rate limiter tripped | Back off; default 100 req/60 s per client (`auth.py:74`) |
| Network error / timeout | Not on the tailnet, or wrong URL/port | Confirm Tailscale is up and the `<gateway>` URL/port are correct |

---

## Contract verification (automated)

The exact contract these recipes rely on is asserted in the gateway test suite
so a regression fails CI rather than silently breaking the Shortcuts:

- `gateway/tests/test_security.py::test_shortcut_source_accepted`
- `gateway/tests/test_security.py::test_shortcut_content_types_accepted` (text/url/photo/file)
- `gateway/tests/test_security.py::test_shortcut_rejects_unknown_content_type`
- `gateway/tests/test_security.py::test_shortcut_empty_content_rejected`

Run them:

```bash
python -m pytest gateway/tests/test_security.py -o addopts="" -q -k shortcut
```

---

## Status

✅ **Reproducible recipes complete** — build each Shortcut by hand from the
actions above. The gateway side requires **no code changes**: `source="shortcut"`
and all four `content_type` values (`text`/`url`/`photo`/`file`) are already
accepted (`gateway/ingest_api/models.py:20-68`) and now contract-tested
(`gateway/tests/test_security.py`).
