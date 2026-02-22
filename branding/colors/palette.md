# AgentShroud Color Palette

## Primary Colors

### AgentShroud Blue (Primary)
- **Hex:** `#1583f0`
- **RGB:** `rgb(21, 131, 240)`
- **HSL:** `hsl(211, 90%, 51%)`
- **Usage:** Primary brand color, logos, accents, CTAs

### Variations
- **Light:** `#4da2f4` (tint +20% toward white)
- **Dark:** `#0e69c0` (shade +20% toward black)

## Secondary Colors

Secondary colors are derived from the primary brand blue to maintain
visual coherence. They appear in supporting contexts — backgrounds,
decorative panels, illustrations, and data visualizations.

### Deep Navy
- **Hex:** `#0a2540`
- **RGB:** `rgb(10, 37, 64)`
- **HSL:** `hsl(211, 73%, 15%)`
- **Usage:** Dark accent panels, sidebar backgrounds, enterprise print materials

### Steel Blue
- **Hex:** `#3a7bd5`
- **RGB:** `rgb(58, 123, 213)`
- **HSL:** `hsl(213, 63%, 53%)`
- **Usage:** Secondary interactive elements, gradient mid-stop, data visualization

### Ice Blue
- **Hex:** `#b3d9ff`
- **RGB:** `rgb(179, 217, 255)`
- **HSL:** `hsl(211, 100%, 85%)`
- **Usage:** Light mode accents, highlight backgrounds, tint overlays

## Semantic Colors

Semantic colors match production code (`web/styles.css`) exactly.

**Success Green**
- **Hex:** `#22c55e`
- **RGB:** `rgb(34, 197, 94)`
- **Usage:** Success states, healthy indicators, approved actions

**Warning Amber**
- **Hex:** `#f59e0b`
- **RGB:** `rgb(245, 158, 11)`
- **Usage:** Warning states, caution indicators, pending review

**Alert Red**
- **Hex:** `#ef4444`
- **RGB:** `rgb(239, 68, 68)`
- **Usage:** Error states, critical alerts, rejected actions

**Info Purple**
- **Hex:** `#a78bfa`
- **RGB:** `rgb(167, 139, 250)`
- **Usage:** Informational highlights, AI-generated content markers

## Neutral Colors

Neutral values match the production dark theme (sourced from `web/styles.css`).

### Dark Surface Hierarchy
- **Void:** `#08090b` — Primary background (deepest)
- **Abyss:** `#0f1219` — Secondary surface
- **Cavern:** `#161c27` — Tertiary surface (cards, panels)
- **Chamber:** `#1e2535` — Quaternary surface (hover states)

### Text
- **Primary Text:** `#e2e8f0` — Headings, important labels
- **Secondary Text:** `#94a3b8` — Body text, descriptions
- **Muted Text:** `#546280` — Placeholders, timestamps

### Borders
- **Border:** `#232b3d` — Default borders
- **Border Bright:** `#2e3a50` — Focused / elevated borders

### Light Mode
- **White:** `#ffffff` — Pure white backgrounds
- **Ghost:** `#e0e0e0` — Light separators
- **Silver:** `#a0a0a0` — Disabled states

## Usage Guidelines

### Accessibility
- Ensure minimum contrast ratio of 4.5:1 for normal text
- Use 3:1 for large text (18pt+)
- Test colors with accessibility tools

### Applications
- **Web:** Use hex values
- **Design:** Use RGB for screens, CMYK for print
- **Code:** Define as CSS/SCSS variables for consistency

## Color Combinations

### Light Theme
- **Background:** `#ffffff`
- **Primary Text:** `#1a1a1a`
- **Accent:** `#1583f0`

### Dark Theme
- **Background:** `#08090b`
- **Primary Text:** `#e2e8f0`
- **Accent:** `#1583f0`

---

**Last Updated:** 2026-02-22
