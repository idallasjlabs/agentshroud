# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
AgentShroud Branding Asset Generator
=====================================
Generates all required branding assets from source logo PNGs using Pillow.

Usage:
    python3 scripts/generate_branding_assets.py

Outputs written to ./branding/ subdirectories.
"""

import os
import struct
import zlib
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# ─── Paths ────────────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).parent.parent
BRANDING = REPO_ROOT / "branding"
LOGOS = BRANDING / "logos" / "png"
SOURCE_LOGO = LOGOS / "logo-transparent.png"   # 1024×1024 RGBA transparent
SOURCE_DARK  = LOGOS / "logo.png"              # 1024×1024 on dark bg

# ─── Brand Colours ────────────────────────────────────────────────────────────
BRAND_BLUE  = (21, 131, 240)          # #1583f0  sampled from logo centre
DARK_BG     = (19, 20, 22)            # #131416  logo canvas dark
MID_BG      = (51, 51, 51)            # #333333  secondary dark
WHITE       = (255, 255, 255)
BLACK       = (0, 0, 0)
BRAND_BLUE_HEX = "#1583f0"
DARK_BG_HEX    = "#131416"
WHITE_HEX      = "#ffffff"

# ─── Typography ───────────────────────────────────────────────────────────────
FONT_PATHS = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/System/Library/Fonts/SFNSDisplay-Bold.otf",
]

def get_font(size: int, bold: bool = True) -> ImageFont.FreeTypeFont:
    for fp in FONT_PATHS:
        if Path(fp).exists():
            try:
                return ImageFont.truetype(fp, size)
            except Exception:
                continue
    return ImageFont.load_default()


# ─── Helpers ──────────────────────────────────────────────────────────────────
def ensure(path: Path):
    path.mkdir(parents=True, exist_ok=True)
    return path


def save(img: Image.Image, path: Path, *, optimize=True):
    ensure(path.parent)
    if path.suffix.lower() in (".jpg", ".jpeg"):
        img = img.convert("RGB")
        img.save(path, "JPEG", quality=92, optimize=optimize)
    else:
        img.save(path, "PNG", optimize=optimize)
    print(f"  ✓  {path.relative_to(REPO_ROOT)}")


def load_logo(size: int | tuple[int, int] | None = None, bg: str = "transparent") -> Image.Image:
    """Load source logo, optionally resize and composite onto bg."""
    if bg == "transparent":
        src = Image.open(SOURCE_LOGO).convert("RGBA")
    else:
        src = Image.open(SOURCE_DARK).convert("RGBA")

    if size is None:
        return src
    if isinstance(size, int):
        size = (size, size)
    return src.resize(size, Image.LANCZOS)


def icon_on_canvas(canvas_size: tuple[int,int], icon_frac: float = 0.8,
                   bg_color=DARK_BG, src=None) -> Image.Image:
    """Paste transparent logo centred on a solid-colour canvas."""
    if src is None:
        src = Image.open(SOURCE_LOGO).convert("RGBA")
    icon_w = int(canvas_size[0] * icon_frac)
    icon_h = int(canvas_size[1] * icon_frac)
    icon = src.resize((icon_w, icon_h), Image.LANCZOS)
    canvas = Image.new("RGBA", canvas_size, (*bg_color, 255))
    x = (canvas_size[0] - icon_w) // 2
    y = (canvas_size[1] - icon_h) // 2
    canvas.paste(icon, (x, y), icon)
    return canvas


# ─── 1. Favicons ──────────────────────────────────────────────────────────────
def generate_favicons():
    print("\n[1] Favicons")
    out = ensure(BRANDING / "favicons")
    src = Image.open(SOURCE_LOGO).convert("RGBA")

    sizes = [16, 32, 48, 64, 96, 128, 192, 256, 512]
    frames = []
    for s in [16, 32, 48]:
        img = icon_on_canvas((s, s), icon_frac=0.88)
        frames.append(img.convert("RGBA"))

    # Multi-size .ico
    ico_path = out / "favicon.ico"
    ico_imgs = []
    for s in [16, 32, 48]:
        img = icon_on_canvas((s, s), icon_frac=0.88)
        ico_imgs.append(img.convert("RGBA"))
    ico_imgs[0].save(
        ico_path, format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48)],
        append_images=ico_imgs[1:]
    )
    print(f"  ✓  {ico_path.relative_to(REPO_ROOT)}")

    # Individual PNGs
    for s in sizes:
        img = icon_on_canvas((s, s), icon_frac=0.88)
        save(img.convert("RGB") if s < 32 else img, out / f"favicon-{s}x{s}.png")

    # Apple touch icon
    apple = icon_on_canvas((180, 180), icon_frac=0.80)
    save(apple, out / "apple-touch-icon.png")

    # PWA icons
    for s in [192, 512]:
        img = icon_on_canvas((s, s), icon_frac=0.82)
        save(img, out / f"icon-{s}x{s}.png")


# ─── 2. Social Media ──────────────────────────────────────────────────────────
def generate_social():
    print("\n[2] Social Media")
    out = ensure(BRANDING / "social")
    src = Image.open(SOURCE_LOGO).convert("RGBA")

    def branded_banner(size: tuple[int,int], title: str, subtitle: str = "",
                       icon_frac: float = 0.25) -> Image.Image:
        """Dark banner with centred logo + text."""
        w, h = size
        canvas = Image.new("RGBA", size, (*DARK_BG, 255))

        # Subtle gradient overlay on left half
        grad = Image.new("RGBA", (w // 2, h), (0, 0, 0, 0))
        draw_g = ImageDraw.Draw(grad)
        for i in range(w // 2):
            alpha = int(60 * (1 - i / (w // 2)))
            draw_g.line([(i, 0), (i, h)], fill=(*BRAND_BLUE, alpha))
        canvas.paste(grad, (0, 0), grad)

        # Blue accent bar at top (6px)
        draw = ImageDraw.Draw(canvas)
        draw.rectangle([(0, 0), (w, 5)], fill=(*BRAND_BLUE, 255))

        # Icon placement: left side
        icon_h = int(h * icon_frac * 1.6)
        icon_w = icon_h
        icon = src.resize((icon_w, icon_h), Image.LANCZOS)
        ix = int(w * 0.06)
        iy = (h - icon_h) // 2
        canvas.paste(icon, (ix, iy), icon)

        # Text: right of icon
        tx = ix + icon_w + int(w * 0.04)
        font_title = get_font(max(28, h // 8))
        font_sub   = get_font(max(16, h // 16), bold=False)

        # Title
        draw.text((tx, h // 2 - int(h * 0.18)), title,
                  font=font_title, fill=WHITE)
        # Subtitle
        if subtitle:
            draw.text((tx, h // 2 + int(h * 0.04)), subtitle,
                      font=font_sub, fill=(*BRAND_BLUE, 220))

        return canvas

    # Twitter / X profile (400×400)
    twp = icon_on_canvas((400, 400), icon_frac=0.82, src=src)
    save(twp, out / "twitter-profile-400x400.png")

    # Twitter / X header (1500×500)
    twh = branded_banner((1500, 500), "AgentShroud™",
                         "Enterprise Governance Proxy for AI Agents", icon_frac=0.35)
    save(twh, out / "twitter-header-1500x500.png")

    # LinkedIn profile (400×400)
    lip = icon_on_canvas((400, 400), icon_frac=0.82, src=src)
    save(lip, out / "linkedin-profile-400x400.png")

    # LinkedIn banner (1584×396)
    lib = branded_banner((1584, 396), "AgentShroud™",
                         "Built by AI Agents · Governed by Design", icon_frac=0.32)
    save(lib, out / "linkedin-banner-1584x396.png")

    # GitHub social preview (1280×640)
    ghp = branded_banner((1280, 640), "AgentShroud™",
                         "Enterprise Governance Proxy for Autonomous AI Agents",
                         icon_frac=0.38)
    save(ghp, out / "github-social-preview-1280x640.png")

    # Telegram bot avatar (512×512)
    tg = icon_on_canvas((512, 512), icon_frac=0.84, src=src)
    save(tg, out / "telegram-avatar-512x512.png")

    # Open Graph / meta image (1200×630)
    og = branded_banner((1200, 630), "AgentShroud™",
                        "You decide what the agent sees · agentshroud.ai",
                        icon_frac=0.36)
    save(og, out / "open-graph-1200x630.png")


# ─── 3. Feature Icons ─────────────────────────────────────────────────────────

MODULES = [
    ("pii-sanitizer",    "PII\nSanitizer",    "🛡"),
    ("approval-queue",   "Approval\nQueue",   "✋"),
    ("audit-ledger",     "Audit\nLedger",     "📋"),
    ("prompt-guard",     "Prompt\nGuard",     "🔒"),
    ("egress-filter",    "Egress\nFilter",    "🌐"),
    ("trust-manager",    "Trust\nManager",    "🔑"),
    ("drift-detector",   "Drift\nDetector",   "📡"),
    ("encrypted-store",  "Encrypted\nStore",  "🗄"),
    ("ssh-proxy",        "SSH\nProxy",        "💻"),
    ("kill-switch",      "Kill\nSwitch",      "⚡"),
    ("agent-isolation",  "Agent\nIsolation",  "📦"),
    ("live-dashboard",   "Live\nDashboard",   "📊"),
    ("http-proxy",       "HTTP\nProxy",       "🔀"),
    ("credential-iso",   "Credential\nIso.",  "🔐"),
]


def generate_feature_icons():
    print("\n[3] Feature Icons (14 modules)")
    out = ensure(BRANDING / "icons" / "modules")
    SIZE = 256
    src = Image.open(SOURCE_LOGO).convert("RGBA")

    for slug, label, emoji in MODULES:
        canvas = Image.new("RGBA", (SIZE, SIZE), (*DARK_BG, 255))
        draw = ImageDraw.Draw(canvas)

        # Blue rounded-rect background
        margin = 12
        draw.rounded_rectangle(
            [(margin, margin), (SIZE - margin, SIZE - margin)],
            radius=24,
            fill=(*BRAND_BLUE, 40)
        )

        # Blue border
        draw.rounded_rectangle(
            [(margin, margin), (SIZE - margin, SIZE - margin)],
            radius=24,
            outline=(*BRAND_BLUE, 200),
            width=3
        )

        # Logo icon (top 55%)
        icon_size = int(SIZE * 0.42)
        icon = src.resize((icon_size, icon_size), Image.LANCZOS)
        ix = (SIZE - icon_size) // 2
        iy = int(SIZE * 0.08)
        canvas.paste(icon, (ix, iy), icon)

        # Label text (bottom area)
        lines = label.split("\n")
        font = get_font(max(18, SIZE // 14))
        y_start = int(SIZE * 0.60)
        for i, line in enumerate(lines):
            bbox = draw.textbbox((0, 0), line, font=font)
            tw = bbox[2] - bbox[0]
            tx = (SIZE - tw) // 2
            draw.text((tx, y_start + i * int(SIZE * 0.165)), line,
                      font=font, fill=WHITE)

        save(canvas, out / f"{slug}-256x256.png")


# ─── 4. Email Banner & Signature ─────────────────────────────────────────────
def generate_email():
    print("\n[4] Email Assets")
    out = ensure(BRANDING / "email")
    src = Image.open(SOURCE_LOGO).convert("RGBA")

    # Email banner (600×150)
    W, H = 600, 150
    banner = Image.new("RGBA", (W, H), (*DARK_BG, 255))
    draw = ImageDraw.Draw(banner)

    # Bottom blue accent line
    draw.rectangle([(0, H - 4), (W, H)], fill=(*BRAND_BLUE, 255))

    # Logo
    icon_h = int(H * 0.68)
    icon_w = icon_h
    icon = src.resize((icon_w, icon_h), Image.LANCZOS)
    banner.paste(icon, (20, (H - icon_h) // 2), icon)

    # Wordmark
    font_big = get_font(32)
    font_sm  = get_font(13, bold=False)
    tx = 20 + icon_w + 16
    draw.text((tx, H // 2 - 24), "AgentShroud™", font=font_big, fill=WHITE)
    draw.text((tx, H // 2 + 12), "Enterprise AI Governance Gateway",
              font=font_sm, fill=(*BRAND_BLUE, 220))

    save(banner, out / "email-banner-600x150.png")

    # HTML email signature template
    sig_html = f"""\
<!DOCTYPE html>
<!--
  AgentShroud™ Email Signature Template
  © 2026 Isaiah Dallas Jefferson, Jr. All rights reserved.
-->
<html>
<body style="margin:0;padding:0;font-family:Arial,Helvetica,sans-serif;">
<table cellpadding="0" cellspacing="0" border="0" style="width:500px;">
  <tr>
    <td style="padding:16px 0 8px;">
      <img src="https://raw.githubusercontent.com/idallasjlabs/agentshroud/main/branding/email/email-banner-600x150.png"
           alt="AgentShroud™" width="500" style="display:block;border:0;" />
    </td>
  </tr>
  <tr>
    <td style="padding:8px 0 4px;border-top:2px solid {BRAND_BLUE_HEX};">
      <span style="font-size:15px;font-weight:bold;color:{DARK_BG_HEX};">Isaiah Dallas Jefferson, Jr.</span><br/>
      <span style="font-size:13px;color:#555555;">Chief Innovation Engineer &amp; Creator, AgentShroud™</span>
    </td>
  </tr>
  <tr>
    <td style="padding:4px 0 8px;">
      <a href="mailto:agentshroud.ai@gmail.com"
         style="font-size:12px;color:{BRAND_BLUE_HEX};text-decoration:none;">agentshroud.ai@gmail.com</a>
      &nbsp;&bull;&nbsp;
      <a href="https://github.com/idallasjlabs/agentshroud"
         style="font-size:12px;color:{BRAND_BLUE_HEX};text-decoration:none;">github.com/idallasjlabs/agentshroud</a>
    </td>
  </tr>
  <tr>
    <td style="padding:8px 0 0;border-top:1px solid #e0e0e0;">
      <span style="font-size:10px;color:#888888;">
        <em>AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
        Protected by common law trademark rights. Federal trademark registration pending.
        Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.</em><br/>
        © 2026 Isaiah Dallas Jefferson, Jr. All rights reserved.
      </span>
    </td>
  </tr>
</table>
</body>
</html>
"""
    sig_path = out / "signature-template.html"
    ensure(sig_path.parent)
    sig_path.write_text(sig_html)
    print(f"  ✓  {sig_path.relative_to(REPO_ROOT)}")


# ─── 5. Presentation Template Slide ──────────────────────────────────────────
def generate_presentation():
    print("\n[5] Presentation Assets")
    out = ensure(BRANDING / "presentation")
    src = Image.open(SOURCE_LOGO).convert("RGBA")

    # Title slide (1920×1080, 16:9)
    W, H = 1920, 1080
    canvas = Image.new("RGBA", (W, H), (*DARK_BG, 255))
    draw = ImageDraw.Draw(canvas)

    # Left blue column
    col_w = int(W * 0.08)
    for x in range(col_w):
        alpha = int(255 * (1 - x / col_w))
        draw.line([(x, 0), (x, H)], fill=(*BRAND_BLUE, alpha))

    # Top accent bar
    draw.rectangle([(0, 0), (W, 6)], fill=(*BRAND_BLUE, 255))
    # Bottom accent bar
    draw.rectangle([(0, H - 6), (W, H)], fill=(*BRAND_BLUE, 255))

    # Large logo left-centre
    icon_h = int(H * 0.50)
    icon = src.resize((icon_h, icon_h), Image.LANCZOS)
    ix = int(W * 0.10)
    iy = (H - icon_h) // 2
    canvas.paste(icon, (ix, iy), icon)

    # Title text right side
    tx = ix + icon_h + int(W * 0.05)
    font_title  = get_font(90)
    font_tag    = get_font(36, bold=False)
    font_sub    = get_font(26, bold=False)
    font_footer = get_font(18, bold=False)

    draw.text((tx, H // 2 - 130), "AgentShroud™",
              font=font_title, fill=WHITE)
    draw.text((tx, H // 2 + 10),
              "Enterprise Governance Proxy", font=font_tag,
              fill=(*BRAND_BLUE, 230))
    draw.text((tx, H // 2 + 70),
              "for Autonomous AI Agents", font=font_tag,
              fill=(*BRAND_BLUE, 230))
    draw.text((tx, H // 2 + 140),
              "Isaiah Dallas Jefferson, Jr.  ·  Chief Innovation Engineer",
              font=font_sub, fill=(180, 180, 180, 255))

    # Footer
    draw.text((col_w + 20, H - 44),
              "© 2026 Isaiah Dallas Jefferson, Jr.  ·  AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr.",
              font=font_footer, fill=(120, 120, 120, 255))

    save(canvas, out / "title-slide-1920x1080.png")

    # Content slide template (blank with header bar)
    content = Image.new("RGBA", (W, H), (245, 247, 250, 255))
    draw2 = ImageDraw.Draw(content)

    # Header bar
    draw2.rectangle([(0, 0), (W, 90)], fill=(*DARK_BG, 255))
    hicon = src.resize((60, 60), Image.LANCZOS)
    content.paste(hicon, (20, 15), hicon)
    draw2.text((90, 22), "AgentShroud™", font=get_font(38), fill=WHITE)
    draw2.text((90, 60), "Enterprise AI Governance Gateway",
               font=get_font(18, bold=False), fill=(*BRAND_BLUE, 220))

    # Blue bottom bar
    draw2.rectangle([(0, H - 40), (W, H)], fill=(*DARK_BG, 255))
    draw2.text((20, H - 30),
               "© 2026 Isaiah Dallas Jefferson, Jr.  ·  AgentShroud™",
               font=get_font(14, bold=False), fill=(150, 150, 150, 255))

    save(content, out / "content-slide-template-1920x1080.png")


# ─── 6. Additional Icon Sizes ─────────────────────────────────────────────────
def generate_icon_sizes():
    print("\n[6] Miscellaneous Icon Sizes")
    out = ensure(BRANDING / "icons" / "app")
    src = Image.open(SOURCE_LOGO).convert("RGBA")

    for s in [16, 24, 32, 48, 64, 96, 128, 256, 512, 1024]:
        img = icon_on_canvas((s, s), icon_frac=0.84, src=src)
        save(img, out / f"icon-{s}x{s}.png")

    # macOS-style rounded icon
    mac_s = 1024
    icon = icon_on_canvas((mac_s, mac_s), icon_frac=0.78, src=src)
    mask = Image.new("L", (mac_s, mac_s), 0)
    mask_draw = ImageDraw.Draw(mask)
    radius = int(mac_s * 0.22)
    mask_draw.rounded_rectangle([(0, 0), (mac_s, mac_s)], radius=radius, fill=255)
    icon.putalpha(mask)
    save(icon, out / "icon-macos-rounded-1024x1024.png")


# ─── 7. Variant Logos ─────────────────────────────────────────────────────────
def generate_variants():
    print("\n[7] Logo Variants")
    out = ensure(BRANDING / "logos" / "variants")
    src = Image.open(SOURCE_LOGO).convert("RGBA")

    # White background version
    light = Image.new("RGBA", src.size, (255, 255, 255, 255))
    light.paste(src, (0, 0), src)
    save(light, out / "logo-on-white-1024x1024.png")

    # Dark background version (re-export clean)
    dark = Image.new("RGBA", src.size, (*DARK_BG, 255))
    dark.paste(src, (0, 0), src)
    save(dark, out / "logo-on-dark-1024x1024.png")

    # Blue background version
    blue_bg = Image.new("RGBA", src.size, (*BRAND_BLUE, 255))
    blue_bg.paste(src, (0, 0), src)
    save(blue_bg, out / "logo-on-brand-blue-1024x1024.png")

    # Square badge (compact, for app store / profile)
    for s in [60, 120, 180]:
        badge = icon_on_canvas((s, s), icon_frac=0.75, src=src)
        save(badge, out / f"badge-{s}x{s}.png")


# ─── 8. SVG Logo Wrappers ─────────────────────────────────────────────────────
def generate_svg_logos():
    """Create SVG files that embed the logo PNGs as base64 data URIs.

    These are scalable SVG containers — not vector traces.  True vector
    re-creation of the hooded-figure + honeycomb design requires manual
    illustration work.  The SVG wrappers are standards-compliant and work in
    every SVG-capable context (browsers, Figma import, Inkscape, etc.).
    """
    import base64
    print("\n[8] SVG Logo Wrappers")
    out = ensure(BRANDING / "logos" / "svg")

    sources = [
        (SOURCE_DARK,        "logo.svg",             DARK_BG_HEX,  "#08090b"),
        (SOURCE_LOGO,        "logo-transparent.svg", "none",        "none"),
    ]

    for src_path, filename, bg_fill, bg_stroke in sources:
        raw = src_path.read_bytes()
        b64 = base64.b64encode(raw).decode()
        mime = "image/png"
        data_uri = f"data:{mime};base64,{b64}"

        # Read source to get natural dimensions
        with Image.open(src_path) as im:
            w, h = im.size

        svg = f"""\
<?xml version="1.0" encoding="UTF-8"?>
<!--
  AgentShroud™ Logo — SVG wrapper with embedded PNG
  © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
  AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.

  NOTE: This SVG embeds the raster logo as a base64 data URI.
  For a true vector version, manual illustration work is required.
  This file scales cleanly at any size without quality loss.
-->
<svg xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="0 0 {w} {h}"
     width="{w}" height="{h}"
     role="img"
     aria-label="AgentShroud™ logo">
  <title>AgentShroud™</title>
  <desc>AgentShroud enterprise AI governance proxy logo</desc>
  {"" if bg_fill == "none" else f'<rect width="{w}" height="{h}" fill="{bg_fill}"/>'}
  <image href="{data_uri}"
         x="0" y="0" width="{w}" height="{h}"
         preserveAspectRatio="xMidYMid meet"/>
</svg>
"""
        svg_path = out / filename
        svg_path.write_text(svg, encoding="utf-8")
        print(f"  ✓  {svg_path.relative_to(REPO_ROOT)}")


# ─── Main ─────────────────────────────────────────────────────────────────────
def main():
    print("AgentShroud™ Branding Asset Generator")
    print("=" * 45)
    print(f"Source:  {SOURCE_LOGO.relative_to(REPO_ROOT)}")
    print(f"Output:  {BRANDING.relative_to(REPO_ROOT)}/")

    generate_favicons()
    generate_social()
    generate_feature_icons()
    generate_email()
    generate_presentation()
    generate_icon_sizes()
    generate_variants()
    generate_svg_logos()

    print("\n✅  All branding assets generated.")
    print(f"    See {BRANDING.relative_to(REPO_ROOT)}/ for outputs.")


if __name__ == "__main__":
    main()
