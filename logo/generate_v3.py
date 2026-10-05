import math
import subprocess

def create_concept_a_v3():
    # Concept A: Monogram Seal "Mẹt Tre & Chữ J Bánh Lọc"
    # An elegant artisanal food seal:
    # Outer double ring representing the layered bamboo rim of traditional steamers (vành đôi mây tre).
    # Ring 1 (outer): R=116, thickness 8 -> outer 116, inner 108
    # Ring 2 (inner): R=100, thickness 4 -> outer 100, inner 96
    # Inside: A strong, fluid J monogram.
    # The J stem descends on the right (x=160), loops smoothly at bottom (y=190) and hooks up to (x=80, y=140).
    # Cradled in the J is a beautifully stylized cooked shrimp (tôm rim) in crimson #9E2A1C.
    # The shrimp has a distinct curved body, head segment with eye/rostrum, and a notched tail.
    # On the outer spine of J, 3 crisp geometric pleats (nếp gấp bánh) harmonize with the letterform.
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleA">
  <title id="titleA">Logo Bánh Lọc Nhà Jun — Concept A: Mẹt Tre &amp; Chữ J Xứ Quảng</title>
  <g id="symbol">
    <!-- Vành Mẹt Tre Lớp Ngoài (Outer Steamer Rim) -->
    <path fill="#1A4329" fill-rule="evenodd" d="M128 12 A116 116 0 1 0 128 244 A116 116 0 1 0 128 12 Z M128 20 A108 108 0 1 1 128 236 A108 108 0 1 1 128 20 Z"/>
    
    <!-- Vành Mẹt Tre Lớp Trong (Inner Accent Rim) -->
    <path fill="#1A4329" fill-rule="evenodd" d="M128 28 A100 100 0 1 0 128 228 A100 100 0 1 0 128 28 Z M128 34 A94 94 0 1 1 128 222 A94 94 0 1 1 128 34 Z"/>

    <!-- Chữ J Cách Điệu Khối Bánh Lọc (The Pleated J Monogram) -->
    <path fill="#1A4329" d="M152 54
      L174 54
      L174 140
      C174 172 148 196 114 196
      C78 196 54 172 54 142
      C54 126 66 114 82 114
      C98 114 108 126 108 142
      C108 152 102 160 92 164
      C98 172 106 176 114 176
      C134 176 152 162 152 138
      Z"/>

    <!-- 3 Nếp Gấp Bánh Lọc Gập Mí Dọc Lưng Chữ J (Folded Dumpling Pleats) -->
    <path fill="#265C38" d="M174 80
      C184 82 192 90 192 100
      C192 108 186 114 180 118
      C188 122 194 130 194 140
      C194 150 186 158 178 162
      C184 166 188 174 186 182
      C184 188 176 192 168 190
      C174 180 174 156 174 140
      Z"/>

    <!-- Chú Tôm Rim Đỏ Son Tuyệt Đẹp (Artisanal Braised Shrimp) -->
    <!-- Thân tôm uốn cong hình trăng khuyết, đầu tôm hướng lên, đuôi xòe 2 nhánh -->
    <path fill="#9E2A1C" d="M136 78
      C144 74 152 78 152 86
      C152 98 142 112 132 124
      C122 134 110 142 96 144
      C88 144 82 138 84 130
      C86 122 94 120 102 118
      C114 116 124 108 130 96
      C134 88 134 82 136 78 Z"/>
    <!-- Đuôi tôm (Shrimp tail fin) -->
    <path fill="#9E2A1C" d="M84 130
      C78 132 72 128 72 122
      C78 124 84 126 88 126 Z"/>
    <path fill="#9E2A1C" d="M84 136
      C78 140 70 138 68 132
      C74 133 80 133 86 132 Z"/>

    <!-- Điểm Nhấn Hạt Tiêu / Mỡ Hành Vàng Hổ Phách (Amber golden accent) -->
    <circle cx="116" cy="98" r="5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

def create_concept_b_v3():
    # Concept B: "Bánh Lọc Bán Nguyệt & Tôm Rim Xứ Quảng" (Authentic Horizontal Crescent Dumpling)
    # The quintessential Vietnamese Bánh Bột Lọc:
    # 1. Base: An elegant, wide green banana leaf (Lá chuối tươi) curving gently underneath.
    # 2. Body: A sleek, plump horizontal crescent dumpling.
    # 3. Top edge: 4 delicate, rhythmic handmade pleats (nếp gấp dập mí bánh lọc).
    # 4. Translucent window in center revealing a stylized braised shrimp (tôm rim) glowing in crimson #9E2A1C.
    # Center (128, 128). Perfectly balanced.
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleB">
  <title id="titleB">Logo Bánh Lọc Nhà Jun — Concept B: Cánh Bánh Bán Nguyệt &amp; Tôm Rim Ánh Son</title>
  <g id="symbol">
    <!-- Phiến Lá Chuối Tươi Xanh Nâng Đỡ Đáy Bánh (Banana Leaf Base) -->
    <path fill="#1A4329" d="M20 170
      C64 196 128 202 192 184
      C224 174 242 160 248 148
      C228 162 188 178 136 178
      C76 178 36 166 20 170 Z"/>

    <!-- Vành Bánh Lọc Bán Nguyệt Dẻo Trong với 4 Nếp Gấp Mí Thủ Công (Pleated Dumpling Arch) -->
    <path fill="#265C38" d="M32 152
      C40 102 78 64 128 64
      C140 64 150 70 148 80
      C146 86 140 90 136 94
      C152 94 162 102 160 112
      C158 118 152 122 146 126
      C162 128 174 136 170 148
      C168 154 160 158 154 162
      C170 164 180 172 176 182
      C172 188 162 190 150 188
      C106 188 60 176 32 152 Z"/>

    <!-- Khoảng Bột Trong Suốt Ở Tâm Bánh (Translucent negative-space dough) -->
    <!-- Real hole / negative space cutout using evenodd rule or clean shape -->
    <path fill="#FAF7F2" d="M52 146
      C66 116 94 92 124 94
      C136 112 142 136 138 164
      C108 170 76 164 52 146 Z"/>

    <!-- Chú Tôm Rim Đỏ Au Nằm Trọn Trong Bánh (Braised Shrimp Filling) -->
    <path fill="#9E2A1C" d="M72 140
      C78 120 98 108 118 112
      C128 114 134 122 130 130
      C126 136 118 138 110 136
      C100 134 92 140 88 148
      C86 152 80 154 76 150
      C72 146 70 142 72 140 Z"/>
    <!-- Đuôi tôm (tail) -->
    <path fill="#9E2A1C" d="M120 112
      C126 104 134 102 138 106
      C140 110 136 116 130 118 Z"/>

    <!-- Điểm Xuyết Vàng Hổ Phách Của Mỡ Hành & Tiêu (Golden spice dot) -->
    <circle cx="106" cy="124" r="4.5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

def create_concept_c_v3():
    # Concept C: "Bếp Nhà Jun — Tinh Hoa Mẹt Bánh Gia Truyền" (Artisanal Kitchen & Steamer Badge)
    # A timeless, warm artisanal Vietnamese culinary seal:
    # An octagon / soft diamond shape inspired by traditional Vietnamese wooden window lattice and kitchen hearth.
    # Inside:
    # 1. A clean, warm roofline ("Nhà") protecting the kitchen.
    # 2. A beautifully folded Bánh Lọc resting on twin banana leaves.
    # 3. Two gentle rising steam ribbons evoking fresh hot dumplings from the steamer.
    # Colors: Heritage Green #1A4329, Crimson #9E2A1C, Warm Amber #D9822B.
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleC">
  <title id="titleC">Logo Bánh Lọc Nhà Jun — Concept C: Bếp Nhà &amp; Hương Vị Gia Truyền</title>
  <g id="symbol">
    <!-- Khung Mẹt Bát Giác Làng Nghề (Artisanal Hearth Frame) -->
    <path fill="none" stroke="#1A4329" stroke-width="6" stroke-linejoin="round" d="M76 24
      L180 24
      L232 76
      L232 180
      L180 232
      L76 232
      L24 180
      L24 76
      Z"/>

    <!-- Mái Nhà Ấm Cúng Che Chở (Sheltering Home Roof / Nhà) -->
    <path fill="#1A4329" d="M128 44
      L196 92
      C199 94 199 98 196 100
      L188 106
      C185 108 181 107 178 105
      L128 70
      L78 105
      C75 107 71 108 68 106
      L60 100
      C57 98 57 94 60 92
      Z"/>

    <!-- Hai Làn Hơi Thơm Bốc Lên Từ Bếp Hấp (Aromatic Steam Ribbons) -->
    <path fill="#D9822B" d="M118 78
      C115 86 121 92 118 100
      C117 101 115 101 114 100
      C112 92 118 86 115 78
      C116 77 118 77 118 78 Z"/>
    <path fill="#D9822B" d="M138 78
      C141 86 135 92 138 100
      C139 101 141 101 142 100
      C144 92 138 86 141 78
      C140 77 138 77 138 78 Z"/>

    <!-- Chiếc Bánh Lọc Bán Nguyệt Dẻo Thơm (Artisanal Dumpling) -->
    <path fill="#265C38" d="M72 156
      C72 120 98 102 128 102
      C158 102 184 120 184 156
      C168 150 148 146 128 146
      C108 146 88 150 72 156 Z"/>

    <!-- Nhân Tôm Rim Đỏ Son Đậm Đà (Braised Shrimp Core) -->
    <path fill="#9E2A1C" d="M106 124
      C116 116 136 116 146 124
      C144 132 134 130 126 130
      C118 130 110 132 106 124 Z"/>
    <circle cx="126" cy="138" r="4" fill="#D9822B"/>

    <!-- Chiếc Lá Chuối Xanh Nâng Đỡ Đáy Bánh (Banana Leaf Base) -->
    <path fill="#1A4329" d="M52 174
      C80 162 110 164 128 174
      C146 164 176 162 204 174
      C176 200 142 204 128 204
      C114 204 80 200 52 174 Z"/>
  </g>
</svg>'''
    return svg

with open('banh-loc-nha-jun/logo/concept-a.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_a_v3())

with open('banh-loc-nha-jun/logo/concept-b.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_b_v3())

with open('banh-loc-nha-jun/logo/concept-c.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_c_v3())

print("Created v3 for all 3 concepts")
