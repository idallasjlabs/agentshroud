// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
//
// AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
// Patent Pending — U.S. Provisional Application No. 64/018,744
//
// MV3 service worker for the AgentShroud browser extension.
//
// Wires two user actions to the gateway `/forward` ingest endpoint:
//   1. URL forwarder  — sends the active tab's URL + title.
//   2. Page clipper   — sends the active tab's readable text (or selection).
//
// All request construction and transport lives in lib/forwarder.js (pure,
// unit-tested). This worker only handles browser plumbing: config load,
// context menus, tab querying, script injection, and user notifications.
// It NEVER hardcodes a token; the token is read from chrome.storage.sync.

/* global chrome, importScripts, AgentShroudForwarder */

importScripts("lib/forwarder.js");

const CTX_FORWARD_URL = "agentshroud-forward-url";
const CTX_CLIP_PAGE = "agentshroud-clip-page";
const CTX_CLIP_SELECTION = "agentshroud-clip-selection";

// --- config -----------------------------------------------------------------

/** Read {gatewayUrl, token} from sync storage (falls back to local). */
async function loadConfig() {
  const keys = { gatewayUrl: "", token: "" };
  const sync = await chrome.storage.sync.get(keys);
  if (sync.gatewayUrl || sync.token) {
    return sync;
  }
  return chrome.storage.local.get(keys);
}

// --- notifications -----------------------------------------------------------

function notify(title, message) {
  try {
    chrome.notifications.create({
      type: "basic",
      iconUrl: "icons/icon128.png",
      title,
      message,
    });
  } catch (e) {
    // Notifications are best-effort; never let a UI failure break forwarding.
    console.warn("AgentShroud: notification failed", e && e.message);
  }
}

/** Interpret a postForward() result and surface it to the user. */
function reportResult(kind, result) {
  if (result.ok) {
    const to = result.data && result.data.forwarded_to ? result.data.forwarded_to : "gateway";
    notify("AgentShroud", kind + " forwarded to " + to + ".");
  } else {
    notify("AgentShroud — failed", result.error || "Unknown error");
  }
}

// --- page content extraction (injected into the page) ------------------------

// Runs in the page context via chrome.scripting.executeScript. Returns the
// user's current selection if any, otherwise a readable text approximation of
// the main content. NO cookies, storage, or DOM nodes are returned — only text.
function extractPageContent() {
  const selection = window.getSelection ? String(window.getSelection()) : "";
  if (selection && selection.trim() !== "") {
    return { text: selection, selection: true, title: document.title, url: location.href };
  }
  // Prefer semantic main content when present; fall back to body.
  const root =
    document.querySelector("main") ||
    document.querySelector("article") ||
    document.body;
  const text = root ? root.innerText || root.textContent || "" : "";
  return { text, selection: false, title: document.title, url: location.href };
}

// --- actions -----------------------------------------------------------------

async function forwardUrl(tab) {
  if (!tab || !tab.url) {
    notify("AgentShroud — failed", "No active tab URL to forward.");
    return;
  }
  let config;
  try {
    config = await loadConfig();
    AgentShroudForwarder.validateConfig(config);
  } catch (e) {
    notify("AgentShroud — not configured", e.message + " Open the extension options.");
    return;
  }
  const payload = AgentShroudForwarder.buildUrlPayload({ url: tab.url, title: tab.title });
  const result = await AgentShroudForwarder.postForward(payload, config, fetch);
  reportResult("URL", result);
}

async function clipPage(tab) {
  if (!tab || tab.id == null) {
    notify("AgentShroud — failed", "No active tab to clip.");
    return;
  }
  let config;
  try {
    config = await loadConfig();
    AgentShroudForwarder.validateConfig(config);
  } catch (e) {
    notify("AgentShroud — not configured", e.message + " Open the extension options.");
    return;
  }

  let extracted;
  try {
    const injection = await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: extractPageContent,
    });
    extracted = injection && injection[0] ? injection[0].result : null;
  } catch (e) {
    notify("AgentShroud — failed", "Could not read page content: " + (e && e.message));
    return;
  }
  if (!extracted) {
    notify("AgentShroud — failed", "No page content found.");
    return;
  }

  let payload;
  try {
    payload = AgentShroudForwarder.buildClipPayload({
      url: extracted.url,
      title: extracted.title,
      text: extracted.text,
      selection: extracted.selection,
    });
  } catch (e) {
    notify("AgentShroud — nothing to clip", e.message);
    return;
  }
  const result = await AgentShroudForwarder.postForward(payload, config, fetch);
  reportResult(extracted.selection ? "Selection" : "Page clip", result);
}

// --- browser wiring ----------------------------------------------------------

async function getActiveTab() {
  const tabs = await chrome.tabs.query({ active: true, currentWindow: true });
  return tabs && tabs[0] ? tabs[0] : null;
}

chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.removeAll(() => {
    chrome.contextMenus.create({
      id: CTX_FORWARD_URL,
      title: "AgentShroud: forward this URL",
      contexts: ["page", "action"],
    });
    chrome.contextMenus.create({
      id: CTX_CLIP_PAGE,
      title: "AgentShroud: clip this page",
      contexts: ["page", "action"],
    });
    chrome.contextMenus.create({
      id: CTX_CLIP_SELECTION,
      title: "AgentShroud: clip selection",
      contexts: ["selection"],
    });
  });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
  if (info.menuItemId === CTX_FORWARD_URL) {
    forwardUrl(tab);
  } else if (info.menuItemId === CTX_CLIP_PAGE || info.menuItemId === CTX_CLIP_SELECTION) {
    clipPage(tab);
  }
});

// Toolbar click (only fires when no default_popup is set; kept as a fallback
// so the extension still works if the popup is removed).
chrome.action.onClicked.addListener((tab) => {
  forwardUrl(tab);
});

// Messages from the popup UI.
chrome.runtime.onMessage.addListener((msg, _sender, sendResponse) => {
  (async () => {
    const tab = await getActiveTab();
    if (msg && msg.action === "forwardUrl") {
      await forwardUrl(tab);
    } else if (msg && msg.action === "clipPage") {
      await clipPage(tab);
    }
    sendResponse({ done: true });
  })();
  return true; // keep the message channel open for the async response
});
