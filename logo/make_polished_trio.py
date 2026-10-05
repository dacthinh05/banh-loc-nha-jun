import math
import subprocess

def create_polished_concept_a():
    # Concept A: "Chữ j Nếp Bánh" (Folded j Monogram)
    # Perfectly centered on 256x256 canvas.
    # Total width of mark = 134. Left margin = 61, Right margin = 61.
    # Shifted x by +24 compared to previous version.
    # Dot of j at (176, 46).
    # Clean 90-degree verticals and clean arcs, zero near-miss angles.
    # Colors: #1A4329 (Deep Leaf Green), #9E2A1C (Shrimp Crimson), #D9822B (Golden Amber).
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleA">
  <title id="titleA">Logo Bánh Lọc Nhà Jun — Concept A: Chữ j Nếp Bánh Gia Truyền</title>
  <g id="symbol">
    <!-- Dấu Chấm Chữ j: Hạt Ngọc Tôm Rim Đỏ Son (Crimson Shrimp Dot) -->
    <circle cx="176" cy="46" r="18" fill="#9E2A1C"/>
    <!-- Điểm nhấn mỡ hành vàng óng (Golden spice accent) -->
    <circle cx="182" cy="40" r="4.5" fill="#D9822B"/>

    <!-- Thân Chữ j Bánh Lọc với Nếp Gấp Mí Bo Tròn Mềm Mại (Pleated j Dumpling) -->
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
    return svg

def create_polished_concept_b():
    # Concept B: "Cánh Bánh Bán Nguyệt & Tôm Rim" (Artisanal Dumpling Silhouette)
    # Perfectly centered on 256x256.
    # Total width ≈ 216 (margins L20, R20).
    # Colors: exactly 3: #1A4329, #9E2A1C, #D9822B.
    # Dumpling uses real negative space (fill-rule="evenodd") for the translucent window!
    # No fake white, no strokes.
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleB">
  <title id="titleB">Logo Bánh Lọc Nhà Jun — Concept B: Cánh Bánh Bán Nguyệt &amp; Tôm Rim</title>
  <g id="symbol">
    <!-- Phiến Lá Chuối Nâng Đỡ Đáy Bánh (Banana Leaf Base) -->
    <path fill="#1A4329" d="M20 176
      C64 198 126 202 188 186
      C218 178 234 166 242 156
      C220 168 180 180 130 180
      C76 180 38 172 20 176 Z"/>

    <!-- Vỏ Bánh Lọc Bán Nguyệt với 4 Nếp Gấp Mí và Cửa Sổ Bột Trong (Pleated Dumpling Shell) -->
    <path fill="#1A4329" fill-rule="evenodd" d="M38 164
      C42 130 60 88 88 78
      C100 74 110 78 112 88
      C124 82 136 88 138 98
      C150 94 162 102 162 114
      C174 114 184 126 182 138
      C190 144 194 156 190 166
      C144 174 90 172 38 164 Z
      M58 158
      C66 128 88 108 120 108
      C150 108 168 130 172 158
      C136 164 94 164 58 158 Z"/>

    <!-- Chú Tôm Rim Đỏ Son Uốn Lượn Trong Bánh (Braised Shrimp Filling) -->
    <path fill="#9E2A1C" d="M88 150
      C94 132 114 122 132 126
      C140 128 146 134 142 142
      C138 148 130 148 122 146
      C112 144 104 148 100 154
      C96 158 92 156 88 150 Z"/>
    <path fill="#9E2A1C" d="M132 126 C138 118 148 118 152 122 C152 126 148 132 142 132 Z"/>

    <!-- Điểm Nhấn Mỡ Hành Vàng Hổ Phách (Golden Scallion Oil) -->
    <circle cx="116" cy="138" r="4.5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

def create_polished_concept_c():
    # Concept C: "Xửng Hấp Bếp Nhà Jun" (The Heritage Steamer Pot)
    # Perfectly centered, 3 colors, zero strokes, clean filled vector shapes.
    # Width = 184 (L36, R36). Height balanced.
    # Colors: #1A4329 (Bamboo Green), #9E2A1C (Shrimp Crimson), #D9822B (Golden Amber).
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleC">
  <title id="titleC">Logo Bánh Lọc Nhà Jun — Concept C: Xửng Hấp Bánh Gia Truyền</title>
  <g id="symbol">
    <!-- Làn Khói Thơm Nghi Ngút Từ Nồi Hấp (Rising Aromatic Steam) -->
    <path fill="#D9822B" d="M116 36
      C112 48 120 58 116 70
      C114 72 112 72 110 70
      C108 58 116 48 112 36
      C113 34 115 34 116 36 Z"/>
    <path fill="#D9822B" d="M140 36
      C144 48 136 58 140 70
      C142 72 144 72 146 70
      C148 58 140 48 144 36
      C143 34 141 34 140 36 Z"/>

    <!-- Núm Nắp Xửng Tre (Steamer Lid Handle) -->
    <rect x="114" y="68" width="28" height="10" rx="5" fill="#1A4329"/>

    <!-- Nắp Xửng Tre Bo Vòm (Steamer Lid Arch) -->
    <path fill="#1A4329" d="M42 120
      C48 90 84 80 128 80
      C172 80 208 90 214 120
      Z"/>
    <!-- Vành Nẹp Nắp Tre (Lid Rim Band) -->
    <rect x="36" y="118" width="184" height="12" rx="4" fill="#1A4329"/>

    <!-- Thân Xửng Tre Hấp Bánh (Steamer Basket Body) -->
    <path fill="#1A4329" d="M44 134
      L212 134
      L202 208
      C200 216 192 222 184 222
      L72 222
      C64 222 56 216 54 208
      Z"/>

    <!-- Đường Rãnh Nan Nứa Đan Thân Xửng (Bamboo Slat Groove) -->
    <rect x="52" y="172" width="152" height="4" rx="2" fill="#D9822B"/>

    <!-- Biểu Tượng Chữ J & Tôm Rim Đỏ Trên Thân Xửng (J Monogram & Red Shrimp on Pot) -->
    <!-- Khoảng âm bản hình chữ J -->
    <path fill="#D9822B" d="M120 148
      L134 148
      L134 186
      C134 196 124 204 112 204
      C100 204 92 196 92 188
      C92 184 96 180 100 180
      C104 180 108 184 108 188
      C108 192 112 194 116 194
      C120 194 124 190 124 186
      Z"/>
    <!-- Hạt Ngọc Tôm Rim Đỏ (Crimson Shrimp Accent Dot) -->
    <circle cx="148" cy="166" r="9" fill="#9E2A1C"/>
  </g>
</svg>'''
    return svg

with open('banh-loc-nha-jun/logo/concept-a.svg', 'w', encoding='utf-8') as f:
    f.write(create_polished_concept_a())

with open('banh-loc-nha-jun/logo/concept-b.svg', 'w', encoding='utf-8') as f:
    f.write(create_polished_concept_b())

with open('banh-loc-nha-jun/logo/concept-c.svg', 'w', encoding='utf-8') as f:
    f.write(create_polished_concept_c())

print("Written polished trio")
