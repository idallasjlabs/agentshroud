#!/bin/sh
# Patch Anthropic SDK to ALWAYS route through ANTHROPIC_BASE_URL
#
# SECURITY: this is the only thing keeping LLM API calls routed through the
# gateway's egress filtering. If the vendor SDK is refactored and our patch
# target strings no longer match, this must fail the build loudly rather than
# silently ship an image where LLM egress bypasses the gateway.
set -e

# Resolve the openclaw install actually in use (respects PATH, so it
# naturally picks .npm-global's fresh seed when present, or falls back to
# the image-bundled copy when the seed failed) — npm root -g instead reports
# the CONFIGURED prefix regardless of whether anything was actually
# installed there, so it silently pointed at an empty/nonexistent directory
# whenever the npm registry seed step failed (e.g. a transient 502 from
# registry.npmjs.org), which made this whole check a no-op: SDK_PATH never
# existed, so the "not found" branch fired every time and was logged as a
# non-fatal warning by the caller instead of blocking — letting an
# unpatched, gateway-bypassing SDK ship undetected. Incident: 2026-09-07.
OPENCLAW_BIN="$(command -v openclaw)" || {
    echo "ERROR: openclaw binary not found on PATH — cannot locate SDK to patch." >&2
    exit 1
}
OPENCLAW_ROOT="$(dirname "$(dirname "$(readlink -f "$OPENCLAW_BIN")")")"
SDK_PATH="$OPENCLAW_ROOT/openclaw/node_modules/@anthropic-ai/sdk/client.js"
if [ ! -f "$SDK_PATH" ]; then
    echo "ERROR: Anthropic SDK not found at $SDK_PATH — LLM egress would bypass the gateway." >&2
    echo "Vendor package layout may have changed; update patch-anthropic-sdk.sh." >&2
    exit 1
fi

node -e "
const fs = require('fs');
const p = process.argv[1];
let c = fs.readFileSync(p, 'utf8');
const marker = 'process.env.ANTHROPIC_BASE_URL';

// Patch 1: Force env var to always override in constructor default
const old1 = 'baseURL: baseURL || \`https://api.anthropic.com\`';
const new1 = 'baseURL: process.env.ANTHROPIC_BASE_URL || baseURL || \`https://api.anthropic.com\`';
let patched1 = false;
if (c.includes(old1)) {
    c = c.replace(old1, new1);
    patched1 = true;
    console.log('Patch 1 applied: constructor default');
}

// Patch 2: Override in the actual URL builder method (belt and suspenders)
const old2 = 'const baseURL = (!tslib_1.__classPrivateFieldGet(this, _BaseAnthropic_instances, \"m\", _BaseAnthropic_baseURLOverridden).call(this) && defaultBaseURL) || this.baseURL;';
const new2 = 'const baseURL = process.env.ANTHROPIC_BASE_URL || ((!tslib_1.__classPrivateFieldGet(this, _BaseAnthropic_instances, \"m\", _BaseAnthropic_baseURLOverridden).call(this) && defaultBaseURL) || this.baseURL);';
let patched2 = false;
if (c.includes(old2)) {
    c = c.replace(old2, new2);
    patched2 = true;
    console.log('Patch 2 applied: URL builder override');
}

// Patch 1 is the primary routing guarantee. If it didn't apply this run AND
// the file doesn't already carry the marker from a prior run, the vendor
// source has drifted out from under us — that's a real proxy-bypass risk,
// not a harmless no-op. Patch 2 stays best-effort (belt and suspenders).
if (!patched1 && !c.includes(marker)) {
    console.error('ERROR: Anthropic SDK patch target not found and no existing ANTHROPIC_BASE_URL marker.');
    console.error('LLM egress would bypass the gateway. Vendor SDK source likely changed; update patch-anthropic-sdk.sh.');
    process.exit(1);
}

// Skip the write when nothing changed — e.g. the image-build-time patched
// copy (read-only rootfs) re-checked here on every boot via
// init-openclaw-config.sh's unconditional 'Always ensure ... SDK patches'
// pass. Writing unconditionally would EROFS on that already-correct file
// for no reason (harmless, but a noisy failure on every boot when the npm
// reseed step falls back to the bundled copy).
if (patched1 || patched2) {
    fs.writeFileSync(p, c);
    console.log('Anthropic SDK patched successfully');
} else {
    console.log('Anthropic SDK already patched — no changes needed');
}
" "$SDK_PATH"
