import os

def create_lockup(symbol_content, concept_id, symbol_width=180, symbol_x=36):
    # Lockup canvas: viewBox="0 0 880 256" width="880" height="256"
    # Symbol placed on the left, scaled & centered vertically around y=128.
    # Text on the right:
    # "BÁNH LỌC NHÀ JUN"
    # Subtitle: "ĐẶC SẢN GIA TRUYỀN QUẢNG BÌNH"
    scale = symbol_width / 256.0
    y_offset = (256 - 256 * scale) / 2
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 256" width="880" height="256" role="img" aria-labelledby="titleLockup{concept_id}">
  <title id="titleLockup{concept_id}">Logo Bánh Lọc Nhà Jun — Concept {concept_id} Lockup</title>
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&amp;family=Inter:wght@600;700&amp;display=swap');
      .brand-title {{
        font-family: 'Playfair Display', Georgia, serif;
        font-weight: 900;
        font-size: 52px;
        fill: #1A4329;
        letter-spacing: -0.5px;
      }}
      .brand-accent {{
        fill: #9E2A1C;
      }}
      .brand-sub {{
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
        font-weight: 700;
        font-size: 16px;
        fill: #635445;
        letter-spacing: 4px;
        text-transform: uppercase;
      }}
    </style>
  </defs>

  <!-- Biểu Tượng (Symbol) -->
  <g transform="translate({symbol_x}, {y_offset}) scale({scale})">
    {symbol_content}
  </g>

  <!-- Tên Thương Hiệu (Wordmark Lockup) -->
  <g id="wordmark">
    <text x="250" y="124" class="brand-title">BÁNH LỌC <tspan class="brand-accent">NHÀ JUN</tspan></text>
    <circle cx="254" cy="162" r="3" fill="#D9822B"/>
    <text x="268" y="167" class="brand-sub">ĐẶC SẢN GIA TRUYỀN QUẢNG BÌNH</text>
  </g>
</svg>'''
    return svg

def extract_symbol_inner(path):
    with open(path, encoding='utf-8') as f:
        content = f.read()
    start = content.find('<g id="symbol">')
    end = content.find('</svg>')
    if start != -1 and end != -1:
        return content[start:end]
    return ''

for cid in ['a', 'b', 'c']:
    sym_path = f'banh-loc-nha-jun/logo/concept-{cid}.svg'
    inner = extract_symbol_inner(sym_path)
    lockup_svg = create_lockup(inner, cid.upper())
    out_path = f'banh-loc-nha-jun/logo/concept-{cid}-lockup.svg'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(lockup_svg)
    print(f"Generated {out_path}")
