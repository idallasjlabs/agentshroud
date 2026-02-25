#!/usr/bin/env node

// Use browsers from /home/node/.cache (copied from root)
process.env.PLAYWRIGHT_BROWSERS_PATH = "/home/node/.cache/ms-playwright";
const { chromium } = require("/usr/local/lib/node_modules/playwright");

const fs = require("fs");
const path = require("path");

async function browserFetch(url, options = {}) {
  const {
    waitForSelector = "body",
    timeout = 30000,
    screenshot = false,
    logPath = "/home/node/.openclaw/logs/browser-fetch.log"
  } = options;

  // Audit log entry
  const logEntry = {
    timestamp: new Date().toISOString(),
    url,
    action: "browser_fetch",
    user: process.env.USER || "unknown"
  };

  console.log(`[browser-fetch] Starting fetch: ${url}`);
  
  let browser;
  try {
    // Launch headless Chromium
    browser = await chromium.launch({
      headless: true,
      args: [
        "--no-sandbox",
        "--disable-setuid-sandbox",
        "--disable-dev-shm-usage",
        "--disable-gpu"
      ]
    });

    const context = await browser.newContext({
      userAgent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    });

    const page = await context.newPage();

    // Navigate to URL
    console.log(`[browser-fetch] Navigating to ${url}`);
    await page.goto(url, { waitUntil: "networkidle", timeout });

    // Wait for specific selector if provided
    if (waitForSelector) {
      console.log(`[browser-fetch] Waiting for selector: ${waitForSelector}`);
      await page.waitForSelector(waitForSelector, { timeout });
    }

    // Give extra time for JavaScript decryption
    await page.waitForTimeout(2000);

    // Extract page content
    const content = await page.evaluate(() => {
      // Try to find 1Password share content
      const shareContent = document.querySelector("[data-testid=\"share-content\"]");
      if (shareContent) {
        return shareContent.innerText;
      }

      // Fallback to body text
      return document.body.innerText;
    });

    await browser.close();

    // Log success
    logEntry.status = "success";
    logEntry.contentLength = content.length;
    appendLog(logPath, logEntry);

    return {
      success: true,
      content,
      url,
      timestamp: logEntry.timestamp
    };

  } catch (error) {
    if (browser) {
      await browser.close();
    }

    // Log failure
    logEntry.status = "error";
    logEntry.error = error.message;
    appendLog(logPath, logEntry);

    return {
      success: false,
      error: error.message,
      url,
      timestamp: logEntry.timestamp
    };
  }
}

function appendLog(logPath, entry) {
  try {
    const logDir = path.dirname(logPath);
    if (!fs.existsSync(logDir)) {
      fs.mkdirSync(logDir, { recursive: true });
    }
    fs.appendFileSync(logPath, JSON.stringify(entry) + "\\n");
  } catch (err) {
    console.error(`[browser-fetch] Failed to write log: ${err.message}`);
  }
}

// CLI mode
if (require.main === module) {
  const url = process.argv[2];
  if (!url) {
    console.error("Usage: browser-fetch.js <url>");
    process.exit(1);
  }

  browserFetch(url)
    .then(result => {
      if (result.success) {
        console.log("\\n=== CONTENT ===");
        console.log(result.content);
        console.log("\\n=== END ===");
        process.exit(0);
      } else {
        console.error(`Error: ${result.error}`);
        process.exit(1);
      }
    });
}

module.exports = { browserFetch };
