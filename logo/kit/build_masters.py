import os
import subprocess

KIT_DIR = "banh-loc-nha-jun/logo/kit"
os.makedirs(KIT_DIR, exist_ok=True)

# 1. Master Symbol (Color)
symbol_color = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleSymbolColor">
  <title id="titleSymbolColor">Logo Bánh Lọc Nhà Jun — Biểu Tượng Master</title>
  <g id="symbol">
    <!-- Dấu Chấm Chữ j: Hạt Ngọc Tôm Rim Đỏ Son (Crimson Shrimp Dot) -->
    <circle cx="176" cy="46" r="18" fill="#9E2A1C"/>
    <!-- Điểm nhấn mỡ hành vàng óng (Golden spice accent) -->
    <circle cx="182" cy="40" r="4.5" fill="#D9822B"/>

    <!-- Thân Chữ j Bánh Lọc với Nếp Gấp Mí Bo Tròn Mềm Mại (Pleated j Dumpling Body) -->
    <path fill="#1A4329" d="M160 82
      L192 82
      L192 152
      C192 188 162 214 126 214
      C116 214 106 218 96 214
      C86 210 78 200 76 190
      C66 188 60 178 60 168
      C60 156 68 148 78 144
      C78 130 92 120 108 120
      C124 120 134 132 134 148
      C134 160 126 170 114 174
      C118 180 126 184 134 184
      C150 184 162 172 162 152
      L162 82
      Z"/>
  </g>
</svg>'''

# 2. Master Symbol Small-Size Cut (Optimized for 16-24px favicon / app icon)
# Thicker stems, merged dot, exaggerated pleat silhouettes so details don't blur at 16px
symbol_small = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleSymbolSmall">
  <title id="titleSymbolSmall">Logo Bánh Lọc Nhà Jun — Biểu Tượng Cỡ Nhỏ (16-24px)</title>
  <g id="symbol">
    <!-- Dấu Chấm Chữ j Đỏ Son Phóng Đại Nhẹ (High contrast crimson dot) -->
    <circle cx="174" cy="48" r="22" fill="#9E2A1C"/>
    <circle cx="180" cy="42" r="6" fill="#D9822B"/>

    <!-- Thân Chữ j Đậm Nét (Bold robust stem & pleats) -->
    <path fill="#1A4329" d="M154 82
      L196 82
      L196 150
      C196 190 164 218 124 218
      C112 218 102 222 92 216
      C80 210 72 198 70 186
      C58 184 52 172 52 160
      C52 146 62 138 74 134
      C74 122 88 114 104 114
      C122 114 136 126 136 144
      C136 154 130 162 120 166
      C124 172 130 174 138 174
      C152 174 162 164 162 148
      L162 82
      Z"/>
  </g>
</svg>'''

# 3. Horizontal Lockup (880x256)
lockup_horizontal = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 256" width="880" height="256" role="img" aria-labelledby="titleLockupH">
  <title id="titleLockupH">Logo Bánh Lọc Nhà Jun — Lockup Ngang</title>
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&amp;family=Inter:wght@600;700&amp;display=swap');
      .brand-title {
        font-family: 'Playfair Display', Georgia, serif;
        font-weight: 900;
        font-size: 52px;
        fill: #1A4329;
        letter-spacing: -0.5px;
      }
      .brand-accent {
        fill: #9E2A1C;
      }
      .brand-sub {
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
        font-weight: 700;
        font-size: 16px;
        fill: #635445;
        letter-spacing: 4px;
        text-transform: uppercase;
      }
    </style>
  </defs>

  <!-- Biểu tượng (Symbol) -->
  <g transform="translate(36, 38) scale(0.703)">
    <!-- Dấu Chấm Chữ j -->
    <circle cx="176" cy="46" r="18" fill="#9E2A1C"/>
    <circle cx="182" cy="40" r="4.5" fill="#D9822B"/>

    <!-- Thân Chữ j Bánh Lọc -->
    <path fill="#1A4329" d="M160 82 L192 82 L192 152 C192 188 162 214 126 214 C116 214 106 218 96 214 C86 210 78 200 76 190 C66 188 60 178 60 168 C60 156 68 148 78 144 C78 130 92 120 108 120 C124 120 134 132 134 148 C134 160 126 170 114 174 C118 180 126 184 134 184 C150 184 162 172 162 152 L162 82 Z"/>
  </g>

  <!-- Tên thương hiệu (Wordmark) -->
  <g id="wordmark">
    <text x="240" y="124" class="brand-title">BÁNH LỌC <tspan class="brand-accent">NHÀ JUN</tspan></text>
    <circle cx="244" cy="162" r="3" fill="#D9822B"/>
    <text x="258" y="167" class="brand-sub">ĐẶC SẢN GIA TRUYỀN QUẢNG BÌNH</text>
  </g>
</svg>'''

# 4. Stacked Lockup (Vertical / Square 400x480)
lockup_stacked = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 480" width="400" height="480" role="img" aria-labelledby="titleLockupS">
  <title id="titleLockupS">Logo Bánh Lọc Nhà Jun — Lockup Dọc</title>
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&amp;family=Inter:wght@600;700&amp;display=swap');
      .brand-title-s {
        font-family: 'Playfair Display', Georgia, serif;
        font-weight: 900;
        font-size: 38px;
        fill: #1A4329;
        text-anchor: middle;
        letter-spacing: -0.5px;
      }
      .brand-accent-s {
        fill: #9E2A1C;
      }
      .brand-sub-s {
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
        font-weight: 700;
        font-size: 13px;
        fill: #635445;
        letter-spacing: 3.5px;
        text-transform: uppercase;
        text-anchor: middle;
      }
    </style>
  </defs>

  <!-- Biểu tượng căn giữa ở trên (Symbol centered at top) -->
  <g transform="translate(100, 24) scale(0.78)">
    <circle cx="176" cy="46" r="18" fill="#9E2A1C"/>
    <circle cx="182" cy="40" r="4.5" fill="#D9822B"/>
    <path fill="#1A4329" d="M160 82 L192 82 L192 152 C192 188 162 214 126 214 C116 214 106 218 96 214 C86 210 78 200 76 190 C66 188 60 178 60 168 C60 156 68 148 78 144 C78 130 92 120 108 120 C124 120 134 132 134 148 C134 160 126 170 114 174 C118 180 126 184 134 184 C150 184 162 172 162 152 L162 82 Z"/>
  </g>

  <!-- Tên thương hiệu căn giữa ở dưới (Wordmark centered at bottom) -->
  <g id="wordmark">
    <text x="200" y="300" class="brand-title-s">BÁNH LỌC</text>
    <text x="200" y="348" class="brand-title-s brand-accent-s">NHÀ JUN</text>
    <circle cx="200" cy="382" r="3" fill="#D9822B"/>
    <text x="200" y="414" class="brand-sub-s">ĐẶC SẢN QUẢNG BÌNH</text>
  </g>
</svg>'''

files = {
    "symbol-color.svg": symbol_color,
    "symbol-small.svg": symbol_small,
    "lockup-horizontal.svg": lockup_horizontal,
    "lockup-stacked.svg": lockup_stacked,
}

for name, content in files.items():
    p = os.path.join(KIT_DIR, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {p}")

# Run audit on symbol SVGs
for s in ["symbol-color.svg", "symbol-small.svg"]:
    sp = os.path.join(KIT_DIR, s)
    res = subprocess.run(["python", "C:/Users/dacth/.omp/agent/skills/ak-logo-design/scripts/svg_audit.py", sp], capture_output=True, text=True)
    print(f"--- Audit {s} ---")
    print(res.stdout)
