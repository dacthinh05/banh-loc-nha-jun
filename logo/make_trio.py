import math
import subprocess

def create_concept_a():
    # Concept A: "Chữ J Nếp Bánh" (Folded J Monogram with Crimson Shrimp Dot)
    # The letter J (Jun) IS the folded dumpling!
    # - Stem is clean and architectural, x=136 to 168 (width 32), from y=80 down to y=156.
    # - At the bottom, the J sweeps in a smooth, majestic semicircle (outer radius 60, inner radius 28) up to x=48, y=140.
    # - 3 smooth, rounded convex scallops along the outer curve:
    #   Scallops are smooth arcs (nếp gấp gập mí tròn mượt mà).
    # - The "dot" of the J at (152, 44) is an elegant crimson circle r=18 with a warm amber dot r=4.5.
    # Centered on 256x256.
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleA">
  <title id="titleA">Logo Bánh Lọc Nhà Jun — Concept A: Chữ J Nếp Bánh Gia Truyền</title>
  <g id="symbol">
    <!-- Dấu Chấm Chữ J: Hạt Ngọc Tôm Rim Đỏ Son (Crimson Shrimp Dot) -->
    <circle cx="152" cy="46" r="18" fill="#9E2A1C"/>
    <!-- Điểm nhấn mỡ hành vàng óng (Golden spice accent) -->
    <circle cx="158" cy="40" r="4.5" fill="#D9822B"/>

    <!-- Thân Chữ J Bánh Lọc với 3 Nếp Gấp Mí Tròn Mượt Mà (Pleated J Dumpling) -->
    <path fill="#1A4329" d="M136 82
      L168 82
      L168 152
      C168 188 138 214 102 214
      C92 214 82 218 72 214
      C62 210 54 200 52 190
      C42 188 36 178 36 168
      C36 156 44 148 54 144
      C54 130 68 120 84 120
      C100 120 110 132 110 148
      C110 160 102 170 90 174
      C94 180 102 184 110 184
      C126 184 138 172 138 152
      Z"/>
  </g>
</svg>'''
    return svg

def create_concept_b():
    # Concept B: "Cánh Bánh Bán Nguyệt & Tôm Rim" (The Pure Artisanal Dumpling)
    # Classic, unmistakable silhouette of a handmade Vietnamese Bánh Bột Lọc:
    # 1. Base: A gently curved fresh green banana leaf (Lá chuối xanh) cradling the dumpling.
    # 2. Top: A classic rounded arch with 4 neat, smooth crimped pleats (nếp gập dập mí).
    # 3. Inside: A vibrant, curved red shrimp (#9E2A1C) with tail.
    # Symmetrical, appetizing, zero clam or eye look.
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleB">
  <title id="titleB">Logo Bánh Lọc Nhà Jun — Concept B: Cánh Bánh Bán Nguyệt &amp; Tôm Rim</title>
  <g id="symbol">
    <!-- Phiến Lá Chuối Nâng Đỡ Đáy Bánh (Banana Leaf Base) -->
    <path fill="#1A4329" d="M26 176
      C68 198 128 202 188 186
      C218 178 234 166 242 156
      C220 168 182 180 134 180
      C82 180 44 172 26 176 Z"/>

    <!-- Vỏ Bánh Lọc Bán Nguyệt Với 4 Nếp Gấp Mí Bo Tròn (4-Pleated Dumpling Arch) -->
    <path fill="#265C38" d="M42 164
      C46 130 64 88 92 78
      C104 74 114 78 116 88
      C128 82 140 88 142 98
      C154 94 166 102 166 114
      C178 114 188 126 186 138
      C194 144 198 156 194 166
      C148 174 94 172 42 164 Z"/>

    <!-- Khoảng Bột Trong Veo Ở Lòng Bánh (Translucent Dough Window) -->
    <path fill="#FAF7F2" d="M62 158
      C70 128 92 108 124 108
      C154 108 172 130 176 158
      C140 164 98 164 62 158 Z"/>

    <!-- Chú Tôm Rim Đỏ Son Nép Giữa Bột (Crimson Braised Shrimp) -->
    <path fill="#9E2A1C" d="M92 150
      C98 132 118 122 136 126
      C144 128 150 134 146 142
      C142 148 134 148 126 146
      C116 144 108 148 104 154
      C100 158 96 156 92 150 Z"/>
    <path fill="#9E2A1C" d="M136 126 C142 118 152 118 156 122 C156 126 152 132 146 132 Z"/>

    <!-- Điểm Nhấn Mỡ Hành Vàng Hổ Phách (Golden Scallion Oil) -->
    <circle cx="120" cy="138" r="4.5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

def create_concept_c():
    # Concept C: "Xửng Hấp Bánh Nhà Jun" (The Artisanal Steamer Pot)
    # A charming, iconic traditional bamboo steamer pot / basket:
    # 1. Round bamboo steamer body with woven texture slats.
    # 2. Steamer lid handle on top.
    # 3. Two gentle rising aromatic steam ribbons (#D9822B).
    # 4. On the front of the steamer: A crisp, proud letter "J" or red shrimp emblem.
    # Conveys fresh steaming hot specialty ("Có hấp chín ăn ngay"), family craft, 100% warm & safe.
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
    <rect x="36" y="118" width="184" height="12" rx="4" fill="#265C38"/>

    <!-- Thân Xửng Tre Hấp Bánh (Steamer Basket Body) -->
    <path fill="#1A4329" d="M44 134
      L212 134
      L202 208
      C200 216 192 222 184 222
      L72 222
      C64 222 56 216 54 208
      Z"/>
    <!-- Nan Nứa Đan Thân Xửng (Woven Bamboo Slats Accent) -->
    <line x1="52" y1="174" x2="204" y2="174" stroke="#265C38" stroke-width="4"/>

    <!-- Biểu Tượng Chữ J & Tôm Rim Đỏ Trên Thân Xửng (Embossed J & Red Shrimp on Pot) -->
    <path fill="#FAF7F2" d="M120 148
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
    <circle cx="151" cy="163" r="2.5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

with open('banh-loc-nha-jun/logo/concept-a.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_a())

with open('banh-loc-nha-jun/logo/concept-b.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_b())

with open('banh-loc-nha-jun/logo/concept-c.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_c())

print("Written updated concepts A, B, and C")
