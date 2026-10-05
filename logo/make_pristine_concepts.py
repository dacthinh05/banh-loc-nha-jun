import math
import subprocess

def create_concept_a_pristine():
    # Concept A: "Chữ J Nếp Bánh" (Folded J Monogram with Crimson Shrimp Dot)
    # The letter J (Jun) IS the folded dumpling!
    # - Stem is clean and architectural, x=136 to 168 (width 32), from y=80 down to y=156.
    # - At the bottom, the J sweeps in a smooth, majestic semicircle (outer radius 60, inner radius 28) up to x=48, y=140.
    # - Along the outer bottom-left curve of the J are 3 clean, crisp pleat scallops (nếp gấp gập mí thủ công):
    #   Scallop 1: arc from angle 180 to 225
    #   Scallop 2: arc from angle 225 to 270
    #   Scallop 3: arc from angle 270 to 315
    # - The "dot" of the J at (152, 48) is an elegant crimson circle r=16 (or curved shrimp droplet) in #9E2A1C!
    # Total canvas: 256x256. Center (128, 128).
    # Zero cliches, zero faces, 100% pure identity design.
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleA">
  <title id="titleA">Logo Bánh Lọc Nhà Jun — Concept A: Chữ J Nếp Bánh Gia Truyền</title>
  <g id="symbol">
    <!-- Dấu Chấm Chữ J: Hạt Ngọc Tôm Rim Đỏ Son (Crimson Shrimp Heart Dot) -->
    <circle cx="156" cy="46" r="18" fill="#9E2A1C"/>
    <!-- Điểm nhấn mỡ hành vàng óng (Golden spice accent) -->
    <circle cx="162" cy="40" r="4.5" fill="#D9822B"/>

    <!-- Thân Chữ J Bánh Lọc Xếp Nếp Gập Mí Thủ Công (Pleated J Dumpling Body) -->
    <path fill="#1A4329" d="M140 82
      L172 82
      L172 152
      C172 188 142 216 104 216
      C66 216 40 188 40 152
      C40 134 54 120 72 120
      C90 120 102 134 102 152
      C102 166 92 178 78 180
      C84 186 94 190 104 190
      C124 190 140 174 140 152
      Z"/>

    <!-- 3 Nếp Gấp Bánh Lọc Tinh Xảo Dọc Viền Cong Chữ J (Folded Pleat Scallops) -->
    <path fill="#265C38" d="M40 152
      C32 164 36 178 48 186
      C44 176 46 164 54 156
      Z"/>
    <path fill="#265C38" d="M56 188
      C52 198 62 210 76 214
      C70 206 70 196 76 188
      Z"/>
    <path fill="#265C38" d="M84 214
      C88 222 102 226 116 222
      C108 218 102 212 102 204
      Z"/>
  </g>
</svg>'''
    return svg

def create_concept_b_pristine():
    # Concept B: "Cánh Bánh Pha Lê & Tôm Rim" (The Pure Crystal Crescent Dumpling)
    # A standalone, gorgeous, minimalist crescent dumpling.
    # An arched back (top) with 4 rhythmic folded pleats.
    # A sweeping curved banana leaf cradling the bottom.
    # Inside: the glowing curved red shrimp.
    # Balanced on 256x256, center (128, 128).
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleB">
  <title id="titleB">Logo Bánh Lọc Nhà Jun — Concept B: Cánh Bánh Pha Lê &amp; Tôm Rim</title>
  <g id="symbol">
    <!-- Dải Lá Chuối Xanh Nâng Đỡ Đáy Bánh (Banana Leaf Base) -->
    <path fill="#1A4329" d="M24 166
      C66 198 134 206 196 184
      C224 174 238 160 244 148
      C222 164 182 182 132 182
      C78 182 42 168 24 166 Z"/>

    <!-- Thân Bánh Lọc Bán Nguyệt Dẻo Trong Veo (The Crescent Tapioca Dumpling) -->
    <!-- 4 Nếp Gấp Mí Thủ Công Dọc Sống Lưng Bánh -->
    <path fill="#265C38" fill-rule="evenodd" d="M36 154
      C44 112 80 68 132 68
      C144 68 152 74 150 84
      C148 90 142 94 136 98
      C152 98 162 106 160 116
      C158 122 152 126 146 130
      C162 132 172 142 168 152
      C166 158 158 162 152 164
      C166 166 174 176 170 184
      C166 188 156 190 146 188
      C106 188 64 176 36 154 Z
      M60 148
      C72 118 98 94 130 94
      C142 94 148 104 144 114
      C138 120 130 124 124 126
      C142 130 148 142 142 152
      C136 156 126 158 116 158
      C88 158 72 154 60 148 Z"/>

    <!-- Nhân Tôm Đồng Rim Đỏ Son Tuyệt Đẹp (Crimson Shrimp Filling) -->
    <path fill="#9E2A1C" d="M82 142
      C90 122 112 110 130 114
      C138 116 144 124 140 132
      C136 138 126 140 118 138
      C108 136 100 142 96 150
      C92 154 86 154 84 150
      C80 146 82 142 82 142 Z"/>
    <path fill="#9E2A1C" d="M130 114 C136 106 146 106 150 110 C150 114 146 120 140 120 Z"/>

    <!-- Điểm Nhấn Mỡ Hành Vàng Hổ Phách (Golden Scallion Oil) -->
    <circle cx="114" cy="126" r="4.5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

def create_concept_c_pristine():
    # Concept C: "Con Dấu Mẹt Tre & Bánh Lọc Gia Truyền" (Artisanal Heritage Steamer Seal)
    # A classic Vietnamese heritage culinary badge:
    # A clean woven bamboo circular frame.
    # Inside: A perfectly balanced, horizontal pleated Bánh Lọc resting on a banana leaf.
    # Center: The glowing red shrimp.
    # Above: 2 gentle rising aroma ribbons.
    # Balanced, warm, authentic, evoking traditional family kitchen ("Nhà làm").
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleC">
  <title id="titleC">Logo Bánh Lọc Nhà Jun — Concept C: Con Dấu Mẹt Tre Gia Truyền</title>
  <g id="symbol">
    <!-- Vòng Mẹt Tre Đôi Truyền Thống (Concentric Steamer Rim) -->
    <path fill="#1A4329" fill-rule="evenodd" d="M128 14 A114 114 0 1 0 128 242 A114 114 0 1 0 128 14 Z M128 22 A106 106 0 1 1 128 234 A106 106 0 1 1 128 22 Z"/>
    <path fill="#1A4329" fill-rule="evenodd" d="M128 30 A98 98 0 1 0 128 226 A98 98 0 1 0 128 30 Z M128 34 A94 94 0 1 1 128 222 A94 94 0 1 1 128 34 Z"/>

    <!-- Làn Khói Thơm Thanh Thoát Bốc Lên Từ Bếp Hấp (Rising aromatic steam ribbons) -->
    <path fill="#D9822B" d="M118 56
      C115 66 121 72 118 82
      C117 84 115 84 114 82
      C112 72 118 66 115 56
      C116 54 118 54 118 56 Z"/>
    <path fill="#D9822B" d="M138 56
      C141 66 135 72 138 82
      C139 84 141 84 142 82
      C144 72 138 66 141 56
      C140 54 138 54 138 56 Z"/>

    <!-- Phiến Lá Chuối Lót Mẹt (Banana Leaf Base) -->
    <path fill="#1A4329" d="M48 168
      C78 194 130 198 178 182
      C200 174 208 164 212 156
      C194 168 160 178 126 178
      C84 178 56 168 48 168 Z"/>

    <!-- Chiếc Bánh Lọc Bán Nguyệt Nằm Ngang Tuyệt Đẹp (Horizontal Pleated Dumpling) -->
    <path fill="#265C38" d="M56 152
      C62 118 92 92 128 92
      C164 92 194 118 200 152
      C176 146 152 142 128 142
      C104 142 80 146 56 152 Z"/>

    <!-- Nhân Tôm Rim Đỏ Son Đậm Đà (Braised Shrimp Filling) -->
    <path fill="#9E2A1C" d="M106 122
      C116 114 136 114 146 122
      C142 130 134 128 126 128
      C118 128 110 130 106 122 Z"/>

    <!-- Điểm Nhấn Mỡ Hành Vàng Hổ Phách (Golden Spice Dot) -->
    <circle cx="126" cy="134" r="4" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

with open('banh-loc-nha-jun/logo/concept-a.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_a_pristine())

with open('banh-loc-nha-jun/logo/concept-b.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_b_pristine())

with open('banh-loc-nha-jun/logo/concept-c.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_c_pristine())

print("Written pristine concepts A, B, and C")
