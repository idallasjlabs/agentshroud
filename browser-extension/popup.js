// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
//
// Popup UI controller. Delegates the actual forward/clip work to the service
// worker (background.js) via chrome.runtime.sendMessage so all transport and
// token handling stays in one place.

/* global chrome */

const statusEl = document.getElementById("status");

function setStatus(text) {
  statusEl.textContent = text;
}

async function send(action, label) {
  setStatus(label + "…");
  try {
    await chrome.runtime.sendMessage({ action });
    setStatus("Request sent. Check the notification for the result.");
  } catch (e) {
    setStatus("Failed: " + (e && e.message ? e.message : "unknown error"));
  }
}

document.getElementById("forwardUrl").addEventListener("click", () => {
  send("forwardUrl", "Forwarding URL");
});

document.getElementById("clipPage").addEventListener("click", () => {
  send("clipPage", "Clipping page");
});

document.getElementById("openOptions").addEventListener("click", (e) => {
  e.preventDefault();
  chrome.runtime.openOptionsPage();
});
