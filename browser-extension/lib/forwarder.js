// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
//
// AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
// Patent Pending — U.S. Provisional Application No. 64/018,744
//
// Pure, side-effect-free logic for the AgentShroud browser extension.
//
// These functions build the request that is POSTed to the gateway `/forward`
// ingest endpoint and interpret its response. They take `config` and `fetch`
// as explicit arguments so they can be unit-tested with a mocked `fetch` and
// never touch the network or the `chrome.*` APIs during tests.
//
// The module is authored as a UMD-ish shim so the SAME file loads in:
//   - the MV3 service worker (via `importScripts('lib/forwarder.js')`)  -> attaches to `self.AgentShroudForwarder`
//   - Node/Jest (via `require('./lib/forwarder')`)                      -> `module.exports`

(function (root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) {
    module.exports = api; // Node / Jest
  }
  // Expose on the global (service worker `self`, window, or Node `global`)
  if (root) {
    root.AgentShroudForwarder = api;
  }
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  const SOURCE = "browser_extension";
  const FORWARD_PATH = "/forward";

  // Content sent to the gateway is capped to keep the request well under the
  // gateway's ForwardRequest 100_000-char ceiling (gateway/ingest_api/models.py:26)
  // and to avoid shipping an entire heavy DOM. Clipped page text is truncated
  // client-side so the transport stays predictable.
  const MAX_CONTENT_CHARS = 90000;

  /**
   * Normalize a user-supplied gateway base URL into an absolute origin+path
   * with no trailing slash. Throws on anything that is not http(s).
   * @param {string} rawUrl
   * @returns {string}
   */
  function normalizeGatewayUrl(rawUrl) {
    if (typeof rawUrl !== "string" || rawUrl.trim() === "") {
      throw new Error("Gateway URL is not configured");
    }
    let parsed;
    try {
      parsed = new URL(rawUrl.trim());
    } catch (e) {
      throw new Error("Gateway URL is invalid: " + rawUrl);
    }
    if (parsed.protocol !== "http:" && parsed.protocol !== "https:") {
      throw new Error("Gateway URL must be http or https");
    }
    // Strip trailing slash from the path (keep origin), so joining is deterministic.
    const path = parsed.pathname.replace(/\/+$/, "");
    return parsed.origin + path;
  }

  /**
   * Validate configuration read from extension storage.
   * @param {{gatewayUrl?: string, token?: string}} config
   * @returns {{gatewayUrl: string, token: string}}
   * @throws {Error} when the URL or token is missing/blank.
   */
  function validateConfig(config) {
    const cfg = config || {};
    const gatewayUrl = normalizeGatewayUrl(cfg.gatewayUrl);
    const token = typeof cfg.token === "string" ? cfg.token.trim() : "";
    if (token === "") {
      throw new Error("Gateway token is not configured");
    }
    // Security: refuse to send Bearer token over plain HTTP (credential leak)
    // Exception: localhost/127.0.0.1 for local development
    if (gatewayUrl.startsWith("http:")) {
      try {
        var parsed = new URL(gatewayUrl);
        var host = parsed.hostname;
        if (host !== "localhost" && host !== "127.0.0.1" && host !== "[::1]") {
          throw new Error(
            "Refusing to send credentials over plain HTTP. " +
            "Use HTTPS for non-localhost gateway URLs."
          );
        }
      } catch (e) {
        if (e.message.indexOf("Refusing") !== -1) throw e;
        // URL parse failed — normalizeGatewayUrl already validated, shouldn't happen
      }
    }
    return { gatewayUrl, token };
  }

  /**
   * Truncate text to the client-side content ceiling. Returns the original
   * string when already short enough.
   * @param {string} text
   * @returns {string}
   */
  function truncateContent(text) {
    const s = typeof text === "string" ? text : "";
    if (s.length <= MAX_CONTENT_CHARS) {
      return s;
    }
    return s.slice(0, MAX_CONTENT_CHARS) + "\n\n[truncated by AgentShroud extension]";
  }

  /**
   * Collapse whitespace in extracted page text without destroying paragraph
   * structure. Runs of blank lines become a single blank line; trailing
   * spaces are trimmed. Pure string transform — no DOM.
   * @param {string} text
   * @returns {string}
   */
  function cleanExtractedText(text) {
    const s = typeof text === "string" ? text : "";
    return s
      .replace(/\r\n?/g, "\n") // normalize newlines
      .replace(/[ \t]+/g, " ") // collapse horizontal whitespace
      .replace(/ *\n */g, "\n") // trim around newlines
      .replace(/\n{3,}/g, "\n\n") // cap blank runs
      .trim();
  }

  /**
   * Build the ForwardRequest body for a "forward this URL" action.
   *
   * Mirrors gateway ForwardRequest: {content, source, content_type, metadata}.
   * The URL itself is the content (content_type "url"); title and any user
   * instruction ride in metadata. NO cookies, tokens, or DOM are included.
   *
   * @param {{url: string, title?: string, instruction?: string}} tab
   * @returns {object} JSON-serializable request body
   */
  function buildUrlPayload(tab) {
    const t = tab || {};
    const url = typeof t.url === "string" ? t.url.trim() : "";
    if (url === "") {
      throw new Error("No URL to forward");
    }
    const metadata = {
      title: typeof t.title === "string" ? t.title : "",
      url: url,
      kind: "url_forward",
    };
    if (typeof t.instruction === "string" && t.instruction.trim() !== "") {
      metadata.instruction = t.instruction.trim();
    }
    return {
      content: url,
      source: SOURCE,
      content_type: "url",
      metadata: metadata,
    };
  }

  /**
   * Build the ForwardRequest body for a "clip this page" action.
   *
   * The readable text (or the user's selection) becomes the content
   * (content_type "text"); the origin URL and title ride in metadata so the
   * agent can attribute the clip. Content is cleaned and truncated client-side.
   *
   * @param {{url: string, title?: string, text: string, selection?: boolean, instruction?: string}} page
   * @returns {object} JSON-serializable request body
   */
  function buildClipPayload(page) {
    const p = page || {};
    const cleaned = cleanExtractedText(p.text);
    if (cleaned === "") {
      throw new Error("No page content to clip");
    }
    const metadata = {
      title: typeof p.title === "string" ? p.title : "",
      url: typeof p.url === "string" ? p.url.trim() : "",
      kind: "page_clip",
      selection: p.selection === true,
    };
    if (typeof p.instruction === "string" && p.instruction.trim() !== "") {
      metadata.instruction = p.instruction.trim();
    }
    return {
      content: truncateContent(cleaned),
      source: SOURCE,
      content_type: "text",
      metadata: metadata,
    };
  }

  /**
   * POST a pre-built ForwardRequest body to the gateway and interpret the
   * result. Uses the injected `fetchImpl` so tests can mock it; NEVER logs the
   * token and only sends it in the Authorization header.
   *
   * @param {object} payload  body from buildUrlPayload/buildClipPayload
   * @param {{gatewayUrl: string, token: string}} config validated config
   * @param {typeof fetch} fetchImpl fetch implementation (injected)
   * @returns {Promise<{ok: boolean, status: number, data?: object, error?: string}>}
   */
  async function postForward(payload, config, fetchImpl) {
    const { gatewayUrl, token } = validateConfig(config);
    const endpoint = gatewayUrl + FORWARD_PATH;

    let response;
    try {
      response = await fetchImpl(endpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + token,
        },
        body: JSON.stringify(payload),
      });
    } catch (networkErr) {
      // Gateway unreachable (Tailscale down, wrong URL, DNS, offline, ...).
      return {
        ok: false,
        status: 0,
        error: "Gateway unreachable: " + (networkErr && networkErr.message ? networkErr.message : "network error"),
      };
    }

    let data;
    try {
      data = await response.json();
    } catch (e) {
      data = undefined;
    }

    if (!response.ok) {
      const detail = data && (data.detail || data.error);
      return {
        ok: false,
        status: response.status,
        error: detail
          ? "Gateway rejected request (" + response.status + "): " + detail
          : "Gateway returned HTTP " + response.status,
        data: data,
      };
    }

    return { ok: true, status: response.status, data: data };
  }

  return {
    SOURCE,
    FORWARD_PATH,
    MAX_CONTENT_CHARS,
    normalizeGatewayUrl,
    validateConfig,
    truncateContent,
    cleanExtractedText,
    buildUrlPayload,
    buildClipPayload,
    postForward,
  };
});
