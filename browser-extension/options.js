// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
//
// Options page controller. Persists {gatewayUrl, token} to chrome.storage.sync
// so the service worker can read them. The token is write-only from the UI's
// perspective (password field) and is never logged.

/* global chrome */

const urlEl = document.getElementById("gatewayUrl");
const tokenEl = document.getElementById("token");
const savedEl = document.getElementById("saved");

async function restore() {
  const cfg = await chrome.storage.sync.get({ gatewayUrl: "", token: "" });
  urlEl.value = cfg.gatewayUrl || "";
  tokenEl.value = cfg.token || "";
}

async function save() {
  await chrome.storage.sync.set({
    gatewayUrl: urlEl.value.trim(),
    token: tokenEl.value.trim(),
  });
  savedEl.textContent = "Saved.";
  setTimeout(() => {
    savedEl.textContent = "";
  }, 2000);
}

document.getElementById("save").addEventListener("click", save);
document.addEventListener("DOMContentLoaded", restore);
