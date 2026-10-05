import math
import subprocess

def create_concept_a_definitive():
    # Concept A: Monogram Emblem "Mẹt Tre & Chữ J Tôm Quê"
    # Double bamboo steamer ring: R_out=114, R_in=106 and R_out=98, R_in=94
    # Monogram J:
    # Stem: x=148 to 176, y=56 to 142.
    # Arc turns down to y=200, sweeps up to x=76, y=144.
    # Shrimp:
    # A sleek, anatomically stylized braised shrimp:
    # Head at (142, 84), tapering body along arc, dorsal curve to (96, 144),
    # terminating in a graceful pointed tail fan at (76, 134).
    # Accent amber dot at (114, 102).
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleA">
  <title id="titleA">Logo Bánh Lọc Nhà Jun — Concept A: Mẹt Tre &amp; Chữ J Tôm Quê</title>
  <g id="symbol">
    <!-- Vành Mẹt Tre Đôi Truyền Thống (Concentric Steamer Rim) -->
    <path fill="#1A4329" fill-rule="evenodd" d="M128 14 A114 114 0 1 0 128 242 A114 114 0 1 0 128 14 Z M128 22 A106 106 0 1 1 128 234 A106 106 0 1 1 128 22 Z"/>
    <path fill="#1A4329" fill-rule="evenodd" d="M128 30 A98 98 0 1 0 128 226 A98 98 0 1 0 128 30 Z M128 34 A94 94 0 1 1 128 222 A94 94 0 1 1 128 34 Z"/>

    <!-- Chữ J Vững Chãi Màu Xanh Lá Chuối (Solid J Monogram) -->
    <path fill="#1A4329" d="M148 56
      L176 56
      L176 142
      C176 178 146 202 110 202
      C74 202 52 178 52 144
      C52 128 66 116 82 116
      C98 116 108 128 108 144
      C108 156 100 166 88 170
      C94 176 102 180 110 180
      C132 180 148 166 148 140
      Z"/>

    <!-- Chú Tôm Rim Đỏ Son Uốn Cong Tuyệt Mỹ (Sleek Braised Shrimp) -->
    <!-- Thân tôm vuốt cong thanh thoát, đầu nhọn, lưng cong, đuôi xòe cá tính -->
    <path fill="#9E2A1C" d="M144 80
      C148 76 156 80 156 88
      C156 102 146 122 134 136
      C120 148 102 154 88 150
      C82 148 80 142 84 136
      C88 132 96 130 106 128
      C118 124 128 114 132 100
      C134 90 136 82 144 80 Z"/>
    <!-- Đuôi tôm (Shrimp Tail) -->
    <path fill="#9E2A1C" d="M84 136 C74 138 68 132 70 124 C76 128 82 130 86 132 Z"/>
    <path fill="#9E2A1C" d="M86 142 C76 148 68 144 68 136 C76 138 82 139 88 138 Z"/>

    <!-- Điểm Nhấn Mỡ Hành Vàng Hổ Phách (Golden Scallion Oil Dot) -->
    <circle cx="114" cy="98" r="5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

def create_concept_b_definitive():
    # Concept B: "Cánh Bánh Pha Lê & Tôm Rim" (Pictorial Crescent Dumpling)
    # The quintessential crescent shape of Bánh Bột Lọc:
    # Double bamboo steamer rim.
    # Underneath: sweeping fresh green banana leaf curve.
    # The Dumpling: an authentic, crisp crescent dumpling (bán nguyệt):
    # Top ridge: smooth arc with 3 subtle, delicate hand-crimped pleat notches.
    # Bottom curve: gentle concave curve resting on the leaf.
    # Center: The iconic curved red shrimp shining through the crystal dough.
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleB">
  <title id="titleB">Logo Bánh Lọc Nhà Jun — Concept B: Cánh Bánh Pha Lê &amp; Tôm Rim Ánh Son</title>
  <g id="symbol">
    <!-- Vòng Mẹt Tre Đôi Truyền Thống (Concentric Steamer Rim) -->
    <path fill="#1A4329" fill-rule="evenodd" d="M128 14 A114 114 0 1 0 128 242 A114 114 0 1 0 128 14 Z M128 22 A106 106 0 1 1 128 234 A106 106 0 1 1 128 22 Z"/>
    <path fill="#1A4329" fill-rule="evenodd" d="M128 30 A98 98 0 1 0 128 226 A98 98 0 1 0 128 30 Z M128 34 A94 94 0 1 1 128 222 A94 94 0 1 1 128 34 Z"/>

    <!-- Phiến Lá Chuối Tươi Lót Dưới Đáy Bánh (Banana Leaf Base) -->
    <path fill="#1A4329" d="M36 162
      C70 194 132 202 190 182
      C214 172 222 160 226 150
      C206 164 166 178 126 178
      C76 178 46 166 36 162 Z"/>

    <!-- Thân Bánh Lọc Bán Nguyệt Dẻo Trong Veo (The Crescent Tapioca Dumpling) -->
    <!-- Đường cong bán nguyệt dập mí 3 nếp gấp gập tay tinh tế -->
    <path fill="#1A4329" fill-rule="evenodd" d="M46 148
      C54 106 86 78 128 78
      C140 78 146 84 144 92
      C142 96 138 100 134 104
      C150 102 160 110 156 120
      C154 126 148 130 142 134
      C160 136 170 146 164 158
      C160 166 148 170 136 170
      C96 170 62 160 46 148 Z
      M64 144
      C72 118 96 98 126 98
      C136 98 142 108 138 116
      C132 122 126 126 120 128
      C140 132 148 144 142 154
      C136 158 124 160 112 160
      C88 160 72 152 64 144 Z"/>

    <!-- Chú Tôm Rim Đỏ Son Uốn Cong Trong Lòng Bánh (Braised Shrimp Inside) -->
    <path fill="#9E2A1C" d="M84 140
      C92 120 112 110 128 114
      C136 116 142 124 138 132
      C134 138 126 140 118 138
      C108 136 100 142 96 150
      C92 154 86 154 84 150
      C80 146 82 142 84 140 Z"/>
    <path fill="#9E2A1C" d="M128 114 C134 106 144 106 148 110 C148 114 144 120 138 120 Z"/>

    <!-- Điểm Nhấn Mỡ Hành Vàng Hổ Phách (Golden Scallion Oil) -->
    <circle cx="112" cy="126" r="4.5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

def create_concept_c_definitive():
    # Concept C: "Bếp Nhà Jun & Hương Vị Gia Truyền" (Artisanal Heritage Steamer & Hearth)
    # A timeless seal combining:
    # 1. Double bamboo steamer circle.
    # 2. A warm sheltering roofline ("Mái Nhà") at top.
    # 3. Two rising aromatic steam ribbons (#D9822B).
    # 4. A plump, folded Bánh Lọc resting on twin banana leaves.
    # 5. Core braised shrimp filling.
    # Balanced, warm, authentic, evoking traditional family kitchen ("Nhà làm").
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleC">
  <title id="titleC">Logo Bánh Lọc Nhà Jun — Concept C: Bếp Nhà &amp; Hương Vị Gia Truyền</title>
  <g id="symbol">
    <!-- Vòng Mẹt Tre Đôi Truyền Thống (Concentric Steamer Rim) -->
    <path fill="#1A4329" fill-rule="evenodd" d="M128 14 A114 114 0 1 0 128 242 A114 114 0 1 0 128 14 Z M128 22 A106 106 0 1 1 128 234 A106 106 0 1 1 128 22 Z"/>
    <path fill="#1A4329" fill-rule="evenodd" d="M128 30 A98 98 0 1 0 128 226 A98 98 0 1 0 128 30 Z M128 34 A94 94 0 1 1 128 222 A94 94 0 1 1 128 34 Z"/>

    <!-- Mái Nhà Gia Đình Ấm Cúng (Warm Sheltering Roofline / Nhà) -->
    <path fill="#1A4329" d="M128 42
      L194 90
      C197 92 197 96 194 98
      L186 104
      C183 106 179 105 176 103
      L128 68
      L80 103
      C77 105 73 106 70 104
      L62 98
      C59 96 59 92 62 90
      Z"/>

    <!-- Hai Làn Hơi Thơm Thanh Thoát Bốc Lên Từ Bếp Hấp (Rising aromatic steam ribbons) -->
    <path fill="#D9822B" d="M118 74
      C115 82 121 88 118 96
      C117 97 115 97 114 96
      C112 88 118 82 115 74
      C116 73 118 73 118 74 Z"/>
    <path fill="#D9822B" d="M138 74
      C141 82 135 88 138 96
      C139 97 141 97 142 96
      C144 88 138 82 141 74
      C140 73 138 73 138 74 Z"/>

    <!-- Chiếc Bánh Lọc Bán Nguyệt Dẻo Thơm (Artisanal Dumpling) -->
    <path fill="#1A4329" fill-rule="evenodd" d="M68 158
      C68 118 96 100 128 100
      C160 100 188 118 188 158
      C168 152 148 148 128 148
      C108 148 88 152 68 158 Z
      M86 150
      C92 124 108 114 128 114
      C148 114 164 124 170 150
      C156 146 142 144 128 144
      C114 144 100 146 86 150 Z"/>

    <!-- Nhân Tôm Rim Đỏ Son Đậm Đà (Braised Shrimp Filling) -->
    <path fill="#9E2A1C" d="M106 128
      C116 120 136 120 146 128
      C142 136 134 134 126 134
      C118 134 110 136 106 128 Z"/>

    <!-- Điểm Nhấn Mỡ Hành Vàng Hổ Phách (Golden Spice Dot) -->
    <circle cx="126" cy="140" r="4" fill="#D9822B"/>

    <!-- Đôi Lá Chuối Xanh Nâng Đỡ Đáy Bánh (Banana Leaf Base) -->
    <path fill="#1A4329" d="M48 174
      C78 162 108 164 128 174
      C148 164 178 162 208 174
      C180 202 144 208 128 208
      C112 208 76 202 48 174 Z"/>
  </g>
</svg>'''
    return svg

with open('banh-loc-nha-jun/logo/concept-a.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_a_definitive())

with open('banh-loc-nha-jun/logo/concept-b.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_b_definitive())

with open('banh-loc-nha-jun/logo/concept-c.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_c_definitive())

print("Written definitive concepts A, B, and C")
