import os
import shutil
import subprocess

KIT_DIR = "banh-loc-nha-jun/logo/kit"
VARIANTS_DIR = os.path.join(KIT_DIR, "variants")

# 1. Create a circular badge SVG with Concept A on warm cream #FAF7F2
badge_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <!-- Nền tròn kem gốm mộc -->
  <circle cx="256" cy="256" r="256" fill="#FAF7F2"/>
  
  <!-- Viền vành tre mạ vàng nhạt tinh tế -->
  <circle cx="256" cy="256" r="248" fill="none" stroke="#D9822B" stroke-width="4" stroke-opacity="0.3"/>

  <!-- Logo Concept A Chữ j Nếp Bánh căn giữa quang học -->
  <g transform="translate(76, 76) scale(1.406)">
    <!-- Dấu Chấm Chữ j: Hạt Ngọc Tôm Rim Đỏ Son -->
    <circle cx="176" cy="46" r="18" fill="#9E2A1C"/>
    <circle cx="182" cy="40" r="4.5" fill="#D9822B"/>

    <!-- Thân Chữ j Bánh Lọc Nếp Gấp -->
    <path fill="#1A4329" d="M160 82 L192 82 L192 152 C192 188 162 214 126 214 C116 214 106 218 96 214 C86 210 78 200 76 190 C66 188 60 178 60 168 C60 156 68 148 78 144 C78 130 92 120 108 120 C124 120 134 132 134 148 C134 160 126 170 114 174 C118 180 126 184 134 184 C150 184 162 172 162 152 L162 82 Z"/>
  </g>
</svg>'''

badge_path = os.path.join(KIT_DIR, "logo-badge.svg")
with open(badge_path, "w", encoding="utf-8") as f:
    f.write(badge_svg)

# Render badge to PNG 512x512
badge_png_path = os.path.join(KIT_DIR, "logo-badge.png")
subprocess.run([
    "python", "C:/Users/dacth/.omp/agent/skills/ak-logo-design/scripts/render_png.py",
    badge_path, "--out-dir", KIT_DIR, "--size", "512"
], check=True)

# Destinations to update
dest_dirs = [
    "banh-loc-nha-jun/assets",
    "public/showcase/banh-loc-nha-jun/assets",
    "public/images/banh-loc"
]

files_to_copy = [
    (os.path.join(KIT_DIR, "logo-badge.png"), "hero-basket.png"),
    (os.path.join(VARIANTS_DIR, "favicon.ico"), "favicon.ico"),
    (os.path.join(VARIANTS_DIR, "favicon.svg"), "favicon.svg"),
    (os.path.join(VARIANTS_DIR, "apple-touch-icon.png"), "apple-touch-icon.png"),
    (os.path.join(VARIANTS_DIR, "site.webmanifest"), "site.webmanifest"),
    (os.path.join(KIT_DIR, "symbol-color.svg"), "logo-symbol.svg"),
    (os.path.join(KIT_DIR, "lockup-horizontal.svg"), "logo-lockup.svg")
]

for d in dest_dirs:
    os.makedirs(d, exist_ok=True)
    for src, dst_name in files_to_copy:
        if os.path.exists(src):
            dst = os.path.join(d, dst_name)
            shutil.copy2(src, dst)
            print(f"Copied {src} -> {dst}")

print("Asset sync complete!")
