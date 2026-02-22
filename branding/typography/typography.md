# AgentShroud Typography Guidelines

## Font Families

### Primary Typeface
**Inter** — Finalized

- **Rationale:** Exceptional screen legibility, neutral technical voice, variable font support, and active maintenance. Used across all web and documentation surfaces since v0.5.0.
- **License:** SIL Open Font License 1.1 — free for commercial use
- **Source:** [rsms.me/inter](https://rsms.me/inter) · Google Fonts
- **CSS stack:**
  ```css
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
  ```

**Alternatives considered:** IBM Plex Sans (too corporate), Space Grotesk (too stylized for body text), Montserrat (better for display/marketing than UI)

### Monospace (Code/Technical)
**JetBrains Mono** — Finalized

- **Rationale:** Developer-native, optimized for code readability, ligature support, and high x-height for terminal contexts. Pairs naturally with Inter.
- **License:** SIL Open Font License 1.1 — free for commercial use
- **Source:** [jetbrains.com/lp/mono](https://www.jetbrains.com/lp/mono) · Google Fonts
- **CSS stack:**
  ```css
  --font-mono: 'JetBrains Mono', 'SF Mono', 'Cascadia Code', 'Fira Code', Consolas, monospace;
  ```

**Alternatives considered:** Fira Code (good ligatures but lower x-height), IBM Plex Mono (pairs with Plex Sans, not Inter), Source Code Pro (less distinctive in dark UI)

## Type Scale

### Headings
- **H1:** 48px / 3rem - Page titles
- **H2:** 36px / 2.25rem - Section headers
- **H3:** 28px / 1.75rem - Subsection headers
- **H4:** 24px / 1.5rem - Component headers
- **H5:** 20px / 1.25rem - Small headers
- **H6:** 18px / 1.125rem - Smallest headers

### Body Text
- **Large:** 18px / 1.125rem - Intro text, emphasis
- **Base:** 16px / 1rem - Body copy, default
- **Small:** 14px / 0.875rem - Secondary text
- **Tiny:** 12px / 0.75rem - Captions, labels

### Code/Monospace
- **Large:** 16px / 1rem - Code blocks
- **Base:** 14px / 0.875rem - Inline code
- **Small:** 12px / 0.75rem - Technical labels

## Font Weights

- **Light:** 300 - Rarely used, large displays only
- **Regular:** 400 - Body text
- **Medium:** 500 - Emphasis, UI elements
- **Semibold:** 600 - Subheadings, strong emphasis
- **Bold:** 700 - Headings, CTAs

## Line Heights

- **Tight:** 1.2 - Headlines, large text
- **Normal:** 1.5 - Body copy
- **Relaxed:** 1.75 - Long-form content

## Letter Spacing

- **Tight:** -0.02em - Large headlines
- **Normal:** 0 - Body text
- **Wide:** 0.05em - Uppercase labels

## Usage Guidelines

### Do's
- Use consistent type scale across all materials
- Maintain proper line height for readability
- Limit to 2-3 font weights per design
- Use monospace for code, technical terms

### Don'ts
- Don't use more than 2 font families
- Don't use decorative fonts for body text
- Don't stack multiple font weights
- Don't use all caps for long text

## Platform-Specific

### Web
- Use web-safe fallbacks
- Include variable fonts when supported
- Optimize font loading (FOUT/FOIT)

### Print
- Ensure fonts have commercial print licenses
- Embed fonts in PDFs
- Test at actual print sizes

### Mobile
- Increase base size to 16px minimum
- Use larger touch targets (44px+)
- Test on actual devices

---

**Last Updated:** 2026-02-22
