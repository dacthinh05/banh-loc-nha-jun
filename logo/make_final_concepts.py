import math
import subprocess

def create_concept_a():
    # Concept A: Monogram Seal "Mẹt Tre & Chữ J Tinh Hoa"
    # A circular woven bamboo steamer seal.
    # The letter J is bold, fluid, descending from top right (x=156, y=52) to loop at bottom (y=196) and curve up to (x=76, y=144).
    # Inside the J bowl is an elegant, appetizing curved shrimp silhouette in crimson #9E2A1C.
    # Banana leaf contour on the left.
    # Exactly 3 colours: #1A4329 (Bamboo Green), #9E2A1C (Shrimp Red), #D9822B (Golden Amber).
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleA">
  <title id="titleA">Logo Bánh Lọc Nhà Jun — Concept A: Mẹt Tre &amp; Chữ J Tinh Hoa</title>
  <g id="symbol">
    <!-- Vành Mẹt Tre Đôi Làng Nghề (Concentric Bamboo Steamer Rim) -->
    <path fill="#1A4329" fill-rule="evenodd" d="M128 14 A114 114 0 1 0 128 242 A114 114 0 1 0 128 14 Z M128 24 A104 104 0 1 1 128 232 A104 104 0 1 1 128 24 Z"/>
    <path fill="#1A4329" fill-rule="evenodd" d="M128 30 A98 98 0 1 0 128 226 A98 98 0 1 0 128 30 Z M128 34 A94 94 0 1 1 128 222 A94 94 0 1 1 128 34 Z"/>

    <!-- Chữ J Cách Điệu Dáng Bánh Lọc Uốn Lượn (Stylized J Monogram) -->
    <!-- Thân chữ J thanh thoát, nét cong hoàn hảo ở đáy -->
    <path fill="#1A4329" d="M152 52
      L172 52
      L172 144
      C172 176 146 200 112 200
      C76 200 52 174 52 142
      C52 126 64 114 80 114
      C96 114 106 126 106 142
      C106 154 98 162 88 166
      C94 174 102 178 112 178
      C132 178 150 164 150 140
      L150 52 Z"/>

    <!-- Vạt Lá Chuối Nâng Đỡ Bên Lưng Chữ J (Banana leaf accent) -->
    <path fill="#1A4329" d="M172 96
      C186 102 196 114 196 130
      C196 148 184 164 172 172
      C172 152 172 124 172 96 Z"/>

    <!-- Chú Tôm Đồng Rim Đỏ Son Tuyệt Đẹp (Artisanal Braised Shrimp) -->
    <!-- Uốn lượn hình trăng khuyết trong lòng chữ J -->
    <path fill="#9E2A1C" d="M136 78
      C146 74 152 80 152 88
      C152 100 140 116 128 128
      C116 138 102 144 90 144
      C82 144 78 138 80 132
      C82 126 90 122 98 120
      C110 118 120 110 128 98
      C132 90 134 84 136 78 Z"/>
    <!-- Đuôi tôm (Shrimp tail fin) -->
    <path fill="#9E2A1C" d="M80 132 C74 134 68 130 68 124 C74 126 80 128 84 128 Z"/>
    <path fill="#9E2A1C" d="M80 138 C74 142 66 140 64 134 C70 135 76 135 82 134 Z"/>

    <!-- Hạt Ngọc Mỡ Hành / Tiêu Vàng Hổ Phách (Golden amber accent) -->
    <circle cx="116" cy="98" r="5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

def create_concept_b():
    # Concept B: Modern Pictorial Mark "Cánh Bánh Pha Lê & Tôm Rim Ánh Son"
    # The authentic crystal bánh lọc silhouette:
    # 1. Base: A lush, sweeping green banana leaf (Lá chuối xanh) cradling the dish.
    # 2. Dumpling body: A crystal leaf / boat silhouette (vỏ bột lọc dẻo trong veo hình cánh buồm/chiếc lá).
    # 3. Filling: The unmistakable curved red shrimp (tôm rim đỏ au) proudly visible through the crystal dough.
    # 4. Golden scallion oil accent.
    # Clean, modern, highly appetizing, unmistakable as Bánh Bột Lọc.
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleB">
  <title id="titleB">Logo Bánh Lọc Nhà Jun — Concept B: Cánh Bánh Pha Lê &amp; Tôm Rim Ánh Son</title>
  <g id="symbol">
    <!-- Phiến Lá Chuối Tươi Xanh Nâng Đỡ (Curving Banana Leaf Base) -->
    <path fill="#1A4329" d="M22 172
      C62 198 130 206 196 186
      C224 176 238 162 244 150
      C224 166 184 184 134 184
      C80 184 40 170 22 172 Z"/>

    <!-- Vỏ Bánh Lọc Pha Lê Trong Veo Hình Chiếc Lá (Crystal Dumpling Shell) -->
    <!-- Đường cong thanh thoát, hai đầu vuốt nhọn tựa cánh buồm trong suốt -->
    <path fill="#1A4329" fill-rule="evenodd" d="M34 158
      C44 116 82 66 138 66
      C182 66 218 106 226 152
      C186 178 120 184 62 170
      C48 166 38 162 34 158 Z
      M58 152
      C68 118 98 84 136 84
      C170 84 198 116 204 148
      C168 166 112 170 74 160
      C66 158 60 155 58 152 Z"/>

    <!-- Chú Tôm Rim Đỏ Son Nép Mình Giữa Bột Trong (Braised Shrimp Inside) -->
    <!-- Uốn lượn mềm mại, nhìn thấu qua lớp bột trong veo -->
    <path fill="#9E2A1C" d="M84 142
      C92 118 116 102 140 106
      C152 108 162 116 160 126
      C158 134 148 138 138 136
      C126 134 114 140 108 150
      C104 156 96 158 92 154
      C86 150 84 144 84 142 Z"/>
    <!-- Đuôi tôm sắc sảo (Shrimp tail) -->
    <path fill="#9E2A1C" d="M142 106
      C150 98 160 96 164 100
      C166 104 162 110 154 112 Z"/>

    <!-- Điểm Nhấn Hành Phi & Mỡ Hành Vàng Óng (Golden scallion oil accent) -->
    <circle cx="128" cy="120" r="5" fill="#D9822B"/>
    <circle cx="144" cy="132" r="3.5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

def create_concept_c():
    # Concept C: "Bếp Nhà Jun & Hương Vị Gia Truyền" (Warm Kitchen & Steamer Badge)
    # A warm, inviting circular kitchen badge:
    # Outer ring: Bamboo steamer tray (Mẹt tre hấp bánh).
    # Upper part: A clean, warm roofline ("Nhà") embracing the composition.
    # Center: The iconic freshly steamed Bánh Lọc resting on banana leaf with gentle aroma steam.
    # Conveys safety, home warmth ("Nhà làm"), traditional family recipe, 100% pure & clean.
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleC">
  <title id="titleC">Logo Bánh Lọc Nhà Jun — Concept C: Bếp Nhà &amp; Hương Vị Gia Truyền</title>
  <g id="symbol">
    <!-- Khung Mẹt Tre Tròn Làng Nghề (Bamboo Steamer Outer Ring) -->
    <path fill="#1A4329" fill-rule="evenodd" d="M128 16 A112 112 0 1 0 128 240 A112 112 0 1 0 128 16 Z M128 24 A104 104 0 1 1 128 232 A104 104 0 1 1 128 24 Z"/>

    <!-- Mái Nhà Gia Đình Ấm Cúng (Warm Sheltering Roofline / Nhà) -->
    <path fill="#1A4329" d="M128 42
      L202 94
      C205 96 205 101 202 103
      L194 109
      C191 111 187 110 184 108
      L128 68
      L72 108
      C69 110 65 111 62 109
      L54 103
      C51 101 51 96 54 94
      Z"/>

    <!-- Hai Làn Hơi Thơm Thanh Thoát Bốc Lên Từ Bếp Hấp (Rising aromatic steam ribbons) -->
    <path fill="#D9822B" d="M118 76
      C115 84 121 90 118 98
      C117 99 115 99 114 98
      C112 90 118 84 115 76
      C116 75 118 75 118 76 Z"/>
    <path fill="#D9822B" d="M138 76
      C141 84 135 90 138 98
      C139 99 141 99 142 98
      C144 90 138 84 141 76
      C140 75 138 75 138 76 Z"/>

    <!-- Chiếc Bánh Lọc Bán Nguyệt Dẻo Thơm (Artisanal Dumpling Silhouette) -->
    <path fill="#1A4329" fill-rule="evenodd" d="M68 162
      C68 116 94 98 128 98
      C162 98 188 116 188 162
      C168 156 148 152 128 152
      C108 152 88 156 68 162 Z
      M86 154
      C92 124 108 112 128 112
      C148 112 164 124 170 154
      C156 150 142 148 128 148
      C114 148 100 150 86 154 Z"/>

    <!-- Nhân Tôm Rim Đỏ Son Đậm Đà Tỏa Sáng Ở Lòng Bánh (Braised Shrimp Filling) -->
    <path fill="#9E2A1C" d="M106 130
      C116 122 136 122 146 130
      C142 138 134 136 126 136
      C118 136 110 138 106 130 Z"/>

    <!-- Điểm Nhấn Mỡ Hành Vàng Hổ Phách (Golden spice accent) -->
    <circle cx="126" cy="144" r="4" fill="#D9822B"/>

    <!-- Chiếc Lá Chuối Xanh Nâng Đỡ Đáy Bánh (Banana Leaf Base) -->
    <path fill="#1A4329" d="M48 178
      C78 166 108 168 128 178
      C148 168 178 166 208 178
      C180 206 144 212 128 212
      C112 212 76 206 48 178 Z"/>
  </g>
</svg>'''
    return svg

with open('banh-loc-nha-jun/logo/concept-a.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_a())

with open('banh-loc-nha-jun/logo/concept-b.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_b())

with open('banh-loc-nha-jun/logo/concept-c.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_c())

print("Successfully written final concept-a.svg, concept-b.svg, concept-c.svg")
