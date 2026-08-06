// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
//
// Unit tests for the AgentShroud browser-extension forwarder pure logic.
// Uses a mocked fetch — NO real network. Verifies payload construction,
// URL/selection extraction cleanup, config validation, and error handling
// when the gateway is unreachable or the token is missing.

const F = require("./forwarder");

/** Build a jest mock fetch that resolves with the given status/body. */
function mockFetchOk(status, body) {
  return jest.fn().mockResolvedValue({
    ok: status >= 200 && status < 300,
    status,
    json: jest.fn().mockResolvedValue(body),
  });
}

const GOOD_CONFIG = { gatewayUrl: "https://gw.tailnet.ts.net:8080", token: "secret-token-123" };

describe("normalizeGatewayUrl", () => {
  test("strips trailing slash and keeps origin+path", () => {
    expect(F.normalizeGatewayUrl("https://gw.example:8080/")).toBe("https://gw.example:8080");
    expect(F.normalizeGatewayUrl("http://127.0.0.1:8080/api/")).toBe("http://127.0.0.1:8080/api");
  });
  test("rejects blank url", () => {
    expect(() => F.normalizeGatewayUrl("")).toThrow(/not configured/);
    expect(() => F.normalizeGatewayUrl("   ")).toThrow(/not configured/);
  });
  test("rejects non-http(s) schemes", () => {
    expect(() => F.normalizeGatewayUrl("ftp://gw.example")).toThrow(/http or https/);
    expect(() => F.normalizeGatewayUrl("javascript:alert(1)")).toThrow();
  });
  test("rejects malformed url", () => {
    expect(() => F.normalizeGatewayUrl("not a url")).toThrow(/invalid/);
  });
});

describe("validateConfig", () => {
  test("returns normalized url and trimmed token", () => {
    const out = F.validateConfig({ gatewayUrl: "https://gw.example:8080/", token: "  tok  " });
    expect(out).toEqual({ gatewayUrl: "https://gw.example:8080", token: "tok" });
  });
  test("throws when token missing", () => {
    expect(() => F.validateConfig({ gatewayUrl: "https://gw.example" })).toThrow(/token is not configured/);
    expect(() => F.validateConfig({ gatewayUrl: "https://gw.example", token: "   " })).toThrow(
      /token is not configured/
    );
  });
  test("throws when url missing", () => {
    expect(() => F.validateConfig({ token: "tok" })).toThrow(/not configured/);
  });
});

describe("cleanExtractedText", () => {
  test("collapses whitespace and caps blank runs", () => {
    const raw = "  Hello   world \r\n\r\n\r\n\r\n  next  paragraph  \t ";
    expect(F.cleanExtractedText(raw)).toBe("Hello world\n\nnext paragraph");
  });
  test("handles non-string", () => {
    expect(F.cleanExtractedText(undefined)).toBe("");
    expect(F.cleanExtractedText(null)).toBe("");
  });
});

describe("truncateContent", () => {
  test("returns short content unchanged", () => {
    expect(F.truncateContent("short")).toBe("short");
  });
  test("truncates oversized content with marker", () => {
    const big = "x".repeat(F.MAX_CONTENT_CHARS + 500);
    const out = F.truncateContent(big);
    expect(out.length).toBeLessThan(big.length);
    expect(out).toMatch(/\[truncated by AgentShroud extension\]$/);
    expect(out.startsWith("x".repeat(F.MAX_CONTENT_CHARS))).toBe(true);
  });
});

describe("buildUrlPayload", () => {
  test("builds a url ForwardRequest with title + kind in metadata", () => {
    const body = F.buildUrlPayload({ url: "  https://news.example/story  ", title: "Big Story" });
    expect(body).toEqual({
      content: "https://news.example/story",
      source: "browser_extension",
      content_type: "url",
      metadata: {
        title: "Big Story",
        url: "https://news.example/story",
        kind: "url_forward",
      },
    });
  });
  test("includes instruction when provided", () => {
    const body = F.buildUrlPayload({ url: "https://x.example", instruction: "summarize this" });
    expect(body.metadata.instruction).toBe("summarize this");
  });
  test("throws when url is empty", () => {
    expect(() => F.buildUrlPayload({ url: "   " })).toThrow(/No URL/);
    expect(() => F.buildUrlPayload({})).toThrow(/No URL/);
  });
});

describe("buildClipPayload", () => {
  test("builds a text ForwardRequest from cleaned page text", () => {
    const body = F.buildClipPayload({
      url: "https://blog.example/post",
      title: "My Post",
      text: "Line one   \n\n\n\n Line two",
      selection: false,
    });
    expect(body.content).toBe("Line one\n\nLine two");
    expect(body.source).toBe("browser_extension");
    expect(body.content_type).toBe("text");
    expect(body.metadata).toEqual({
      title: "My Post",
      url: "https://blog.example/post",
      kind: "page_clip",
      selection: false,
    });
  });
  test("marks selection true and truncates oversized clips", () => {
    const body = F.buildClipPayload({
      url: "https://x.example",
      text: "y".repeat(F.MAX_CONTENT_CHARS + 100),
      selection: true,
    });
    expect(body.metadata.selection).toBe(true);
    expect(body.content).toMatch(/\[truncated by AgentShroud extension\]$/);
  });
  test("includes instruction when provided", () => {
    const body = F.buildClipPayload({
      url: "https://x.example",
      text: "some readable body text",
      instruction: "extract the action items",
    });
    expect(body.metadata.instruction).toBe("extract the action items");
  });
  test("throws when no content to clip", () => {
    expect(() => F.buildClipPayload({ url: "https://x.example", text: "   \n\n " })).toThrow(/No page content/);
  });
});

describe("postForward", () => {
  test("posts to <gatewayUrl>/forward with Bearer token and JSON body", async () => {
    const fetchImpl = mockFetchOk(201, { id: "abc", forwarded_to: "openclaw" });
    const payload = F.buildUrlPayload({ url: "https://x.example", title: "T" });

    const res = await F.postForward(payload, GOOD_CONFIG, fetchImpl);

    expect(res.ok).toBe(true);
    expect(res.status).toBe(201);
    expect(res.data).toEqual({ id: "abc", forwarded_to: "openclaw" });

    expect(fetchImpl).toHaveBeenCalledTimes(1);
    const [url, opts] = fetchImpl.mock.calls[0];
    expect(url).toBe("https://gw.tailnet.ts.net:8080/forward");
    expect(opts.method).toBe("POST");
    expect(opts.headers.Authorization).toBe("Bearer secret-token-123");
    expect(opts.headers["Content-Type"]).toBe("application/json");
    expect(JSON.parse(opts.body)).toEqual(payload);
  });

  test("returns error result when token missing (does not call fetch)", async () => {
    const fetchImpl = jest.fn();
    await expect(
      F.postForward({ content: "x" }, { gatewayUrl: "https://gw.example" }, fetchImpl)
    ).rejects.toThrow(/token is not configured/);
    expect(fetchImpl).not.toHaveBeenCalled();
  });

  test("handles gateway unreachable (fetch throws)", async () => {
    const fetchImpl = jest.fn().mockRejectedValue(new Error("Failed to fetch"));
    const res = await F.postForward(F.buildUrlPayload({ url: "https://x.example" }), GOOD_CONFIG, fetchImpl);
    expect(res.ok).toBe(false);
    expect(res.status).toBe(0);
    expect(res.error).toMatch(/Gateway unreachable/);
    expect(res.error).toMatch(/Failed to fetch/);
  });

  test("surfaces gateway 401 detail", async () => {
    const fetchImpl = mockFetchOk(401, { detail: "Invalid authentication token" });
    const res = await F.postForward(F.buildUrlPayload({ url: "https://x.example" }), GOOD_CONFIG, fetchImpl);
    expect(res.ok).toBe(false);
    expect(res.status).toBe(401);
    expect(res.error).toMatch(/Invalid authentication token/);
  });

  test("handles non-JSON error body", async () => {
    const fetchImpl = jest.fn().mockResolvedValue({
      ok: false,
      status: 502,
      json: jest.fn().mockRejectedValue(new Error("not json")),
    });
    const res = await F.postForward(F.buildUrlPayload({ url: "https://x.example" }), GOOD_CONFIG, fetchImpl);
    expect(res.ok).toBe(false);
    expect(res.status).toBe(502);
    expect(res.error).toBe("Gateway returned HTTP 502");
  });

  test("succeeds even when a 201 body is not JSON (data undefined)", async () => {
    const fetchImpl = jest.fn().mockResolvedValue({
      ok: true,
      status: 201,
      json: jest.fn().mockRejectedValue(new Error("empty body")),
    });
    const res = await F.postForward(F.buildUrlPayload({ url: "https://x.example" }), GOOD_CONFIG, fetchImpl);
    expect(res.ok).toBe(true);
    expect(res.status).toBe(201);
    expect(res.data).toBeUndefined();
  });

  test("never leaks the token into the error string on failure", async () => {
    const fetchImpl = jest.fn().mockRejectedValue(new Error("boom"));
    const res = await F.postForward(F.buildUrlPayload({ url: "https://x.example" }), GOOD_CONFIG, fetchImpl);
    expect(res.error).not.toContain(GOOD_CONFIG.token);
  });
});

// --- SCRUM-108: HTTP credential protection ---

test("validateConfig rejects plain HTTP for non-localhost URLs", () => {
  expect(() =>
    F.validateConfig({ gatewayUrl: "http://remote-host.example.com:8080", token: "secret" })
  ).toThrow(/Refusing to send credentials over plain HTTP/);
});

test("validateConfig allows plain HTTP for localhost", () => {
  const cfg = F.validateConfig({ gatewayUrl: "http://localhost:8080", token: "secret" });
  expect(cfg.gatewayUrl).toBe("http://localhost:8080");
});

test("validateConfig allows plain HTTP for 127.0.0.1", () => {
  const cfg = F.validateConfig({ gatewayUrl: "http://127.0.0.1:8080", token: "secret" });
  expect(cfg.gatewayUrl).toBe("http://127.0.0.1:8080");
});

test("validateConfig allows HTTPS for remote URLs", () => {
  const cfg = F.validateConfig({ gatewayUrl: "https://gateway.example.com", token: "secret" });
  expect(cfg.gatewayUrl).toBe("https://gateway.example.com");
});

// --- SCRUM-108: iframe selection must target the frame the selection is
// actually in, not silently fall back to the top-level frame. ---

describe("buildClipTarget", () => {
  test("targets the specific frame when a context-menu frameId is known", () => {
    // e.g. user right-clicked a selection inside an <iframe> (frameId 7)
    expect(F.buildClipTarget(42, 7)).toEqual({ tabId: 42, frameIds: [7] });
  });

  test("targets frameId 0 (top frame) when frameId is 0 itself", () => {
    expect(F.buildClipTarget(42, 0)).toEqual({ tabId: 42, frameIds: [0] });
  });

  test("falls back to the top-level frame when no frameId is known (toolbar/popup invocation)", () => {
    expect(F.buildClipTarget(42, undefined)).toEqual({ tabId: 42, frameIds: [0] });
    expect(F.buildClipTarget(42, null)).toEqual({ tabId: 42, frameIds: [0] });
    expect(F.buildClipTarget(42)).toEqual({ tabId: 42, frameIds: [0] });
  });
});
