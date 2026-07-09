"""
Generates the Limina favicon/PWA icon set as base64-encoded inline SVGs.

Icon concept: A3 V4 — a thin horizontal line (horizon) with a rising
semicircle (dawn/threshold), filled with a subtle glow. Represents "limen"
(Latin: threshold) — the liminal space between waking and dreaming.

Usage:
    python3 generate_favicon.py

Outputs base64 strings for each required size, ready to paste into
<link rel="icon" ...> or a web manifest as data:image/svg+xml;base64,...

To swap in a real image instead of this generated icon, replace the
data URIs in <head> with data:image/png;base64,<your-base64> and update
the manifest's "type" fields to "image/png" accordingly.
"""

import base64

BG_COLOR = "#0c0d0f"       # matches --bg in dark theme
ACCENT_COLOR = "#b4a5d2"  # matches --accent
GLOW_OPACITY = 0.13

SIZES = [16, 32, 180, 192, 512]


def make_svg(size: int) -> str:
    s = size
    cx = cy = s / 2
    r = s * 0.28          # arc radius
    line_w = max(s * 0.025, 0.4)
    line_ext = s * 0.10   # how far the line extends beyond the arc on each side

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{s}" height="{s}" '
        f'viewBox="0 0 {s} {s}">'
        f'<rect width="{s}" height="{s}" fill="{BG_COLOR}"/>'
        f'<g transform="translate({cx},{cy})">'
        f'<path d="M {-r:.2f} 0 A {r:.2f} {r:.2f} 0 0 1 {r:.2f} 0" '
        f'fill="{ACCENT_COLOR}" fill-opacity="{GLOW_OPACITY}" '
        f'stroke="{ACCENT_COLOR}" stroke-width="{line_w:.2f}" stroke-linecap="round"/>'
        f'<line x1="{-(r + line_ext):.2f}" y1="0" x2="{(r + line_ext):.2f}" y2="0" '
        f'stroke="{ACCENT_COLOR}" stroke-width="{line_w:.2f}" stroke-linecap="round"/>'
        f'</g></svg>'
    )


if __name__ == "__main__":
    for size in SIZES:
        svg = make_svg(size)
        b64 = base64.b64encode(svg.encode()).decode()
        print(f"\n# {size}x{size} ({len(b64)} chars base64)")
        print(f"data:image/svg+xml;base64,{b64}")
