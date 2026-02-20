# AgentShroud Brand Quick Reference

## Logo Files

```
branding/logos/png/
├── logo.png              # Primary logo with background
├── logo-transparent.png  # Transparent background (use this most often)
└── logo-mockup.png       # Presentation/showcase version
```

## Primary Brand Color

```css
/* AgentShroud Blue */
--brand-primary: #8bf0fb;
--brand-primary-rgb: rgb(139, 240, 251);
--brand-primary-hsl: hsl(184, 93%, 76%);
```

## Quick Color Palette

```css
/* Primary */
--brand-blue: #8bf0fb;
--brand-blue-light: #c5f7fd;
--brand-blue-dark: #51e9f9;

/* Semantic Colors */
--success: #00ff88;
--warning: #ffb800;
--error: #ff4444;

/* Neutrals */
--charcoal: #1a1a1a;
--slate: #4a4a4a;
--silver: #a0a0a0;
--ghost: #e0e0e0;
--white: #ffffff;
```

## Typography

```css
/* Recommended Font Stacks */
--font-sans: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
--font-mono: "JetBrains Mono", "Fira Code", Consolas, monospace;

/* Type Scale */
--text-xs: 0.75rem;   /* 12px */
--text-sm: 0.875rem;  /* 14px */
--text-base: 1rem;    /* 16px */
--text-lg: 1.125rem;  /* 18px */
--text-xl: 1.25rem;   /* 20px */
--text-2xl: 1.5rem;   /* 24px */
--text-3xl: 1.75rem;  /* 28px */
--text-4xl: 2.25rem;  /* 36px */
--text-5xl: 3rem;     /* 48px */
```

## Logo Usage Rules

### ✅ Do
- Use transparent version for most applications
- Maintain 50% logo height clear space
- Minimum 120px width (digital) / 1 inch (print)
- Ensure 4.5:1 contrast ratio

### ❌ Don't
- Stretch or distort
- Change colors
- Add effects or shadows
- Use on busy backgrounds

## File Locations

```
branding/
├── logos/           # All logo formats
├── colors/          # Color palettes
├── typography/      # Font guidelines
└── guidelines/      # Detailed brand guidelines
```

## Common Use Cases

### Website Header
```html
<img src="branding/logos/png/logo-transparent.png"
     alt="AgentShroud"
     width="150"
     height="auto">
```

### Favicon
```html
<!-- Use a smaller, simplified version -->
<link rel="icon" type="image/png" href="/favicon-32.png">
```

### CSS Variables
```css
:root {
  --brand-primary: #8bf0fb;
  --font-sans: Inter, system-ui, sans-serif;
}

.cta-button {
  background: var(--brand-primary);
  color: var(--charcoal);
}
```

### Dark Mode
```css
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #1a1a1a;
    --text: #e0e0e0;
    --accent: #8bf0fb;
  }
}
```

## Accessibility Checklist

- [ ] Text contrast ≥ 4.5:1 (normal) or 3:1 (large)
- [ ] Interactive elements ≥ 3:1 contrast
- [ ] Logo visible on all backgrounds
- [ ] Touch targets ≥ 44px (mobile)
- [ ] Alt text for all images
- [ ] Color not sole indicator of meaning

## Need More Details?

See `branding/README.md` for full documentation.

---

**Quick Start:** Use `logo-transparent.png` + `#8bf0fb` color + Inter font
