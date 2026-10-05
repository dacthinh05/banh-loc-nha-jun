import math
import subprocess

def create_concept_a_clean():
    # Concept A: "Mẹt Tre & Chữ J Tinh Giản" (Monogram Seal)
    # A bold, geometric, pristine J monogram inside a double bamboo circle.
    # Canvas 256x256. Center (128, 128).
    # Double ring:
    # Outer circle: R=114, thickness 8 -> R_out=114, R_in=106
    # Inner circle: R=98, thickness 4 -> R_out=98, R_in=94
    # Monogram J:
    # Stem at x=154, width 28. Descends from y=60 down to y=152.
    # Turns in a smooth circular arc with outer radius 54, inner radius 26.
    # Hooks up to x=72, y=140.
    # Inside the bowl of the J:
    # A beautifully stylized crimson shrimp silhouette in #9E2A1C at (114, 128).
    # Colors: #1A4329 (Forest Green), #9E2A1C (Shrimp Crimson), #D9822B (Golden Amber).
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleA">
  <title id="titleA">Logo Bánh Lọc Nhà Jun — Concept A: Mẹt Tre &amp; Chữ J Tinh Giản</title>
  <g id="symbol">
    <!-- Vòng Mẹt Tre Đôi Truyền Thống (Concentric Steamer Rim) -->
    <path fill="#1A4329" fill-rule="evenodd" d="M128 14 A114 114 0 1 0 128 242 A114 114 0 1 0 128 14 Z M128 22 A106 106 0 1 1 128 234 A106 106 0 1 1 128 22 Z"/>
    <path fill="#1A4329" fill-rule="evenodd" d="M128 30 A98 98 0 1 0 128 226 A98 98 0 1 0 128 30 Z M128 34 A94 94 0 1 1 128 222 A94 94 0 1 1 128 34 Z"/>

    <!-- Chữ J Hình Học Tinh Tuyển (Geometric J Monogram) -->
    <path fill="#1A4329" d="M148 58
      L176 58
      L176 150
      C176 182 148 204 114 204
      C78 204 52 180 52 146
      C52 128 66 116 82 116
      C98 116 108 128 108 144
      C108 156 100 166 88 170
      C94 178 104 182 114 182
      C132 182 148 168 148 146
      Z"/>

    <!-- Nhân Tôm Rim Đỏ Son Tuyệt Sắc Ở Lòng Chữ J (Crimson Shrimp in J) -->
    <!-- Thân tôm uốn cong hình trăng khuyết, đầu tôm thon gọn, đuôi xòe cá tính -->
    <path fill="#9E2A1C" d="M138 86
      C144 80 150 84 150 92
      C150 104 140 120 128 132
      C116 142 102 146 92 146
      C86 146 82 140 84 134
      C86 128 92 126 98 124
      C110 122 118 114 126 104
      C132 96 134 90 138 86 Z"/>
    <path fill="#9E2A1C" d="M84 134 C78 136 72 132 72 126 C78 128 84 130 88 130 Z"/>
    <path fill="#9E2A1C" d="M84 140 C78 144 70 142 68 136 C74 137 80 137 86 136 Z"/>

    <!-- Điểm Nhấn Mỡ Hành Vàng Hổ Phách (Golden Scallion Oil Dot) -->
    <circle cx="116" cy="102" r="5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

def create_concept_b_clean():
    # Concept B: "Chiếc Bánh Mẹt Tre & Nếp Gấp Gia Truyền" (Artisanal Pictorial Steamer)
    # A top-down view of an authentic bamboo basket with a fresh banana leaf and a perfectly pleated Bánh Bột Lọc!
    # 1. Bamboo rim (vành mẹt tre tròn).
    # 2. Banana leaf texture underneath (phiến lá chuối xanh tươi).
    # 3. Authentic Bánh Bột Lọc crescent with 4 distinct, delicate hand-crimped pleats (nếp gấp viền bánh).
    # 4. Translucent center revealing the glowing red shrimp (tôm rim).
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleB">
  <title id="titleB">Logo Bánh Lọc Nhà Jun — Concept B: Mẹt Bánh Lọc Xếp Nếp Gia Truyền</title>
  <g id="symbol">
    <!-- Vành Mẹt Tre Đan Thủ Công (Woven Bamboo Steamer Rim) -->
    <circle cx="128" cy="128" r="114" fill="none" stroke="#1A4329" stroke-width="8"/>
    <circle cx="128" cy="128" r="98" fill="none" stroke="#1A4329" stroke-width="3"/>

    <!-- Phiến Lá Chuối Tươi Lót Dưới Mẹt (Banana Leaf Bed in Steamer) -->
    <path fill="#1A4329" d="M44 140
      C60 188 108 214 164 210
      C198 206 216 190 220 178
      C190 196 142 200 96 186
      C64 176 48 156 44 140 Z"/>

    <!-- Chiếc Bánh Lọc Bán Nguyệt Với 4 Nếp Gấp Mí Rõ Ràng (The 4-Pleated Dumpling) -->
    <!-- Cung vòm trên lượn 4 nếp gấp thủ công tinh xảo của thợ lành nghề -->
    <path fill="#1A4329" d="M52 144
      C54 116 76 84 104 74
      C114 70 124 74 122 84
      C120 90 114 94 110 98
      C124 96 136 102 134 112
      C132 118 126 122 120 126
      C136 126 148 134 144 144
      C142 150 134 154 126 158
      C140 160 148 168 144 176
      C140 182 130 184 120 182
      C88 178 62 164 52 144 Z"/>

    <!-- Lòng Bột Dẻo Trong Veo (Translucent dumpling body) -->
    <!-- Khoảng âm bản tinh gọn làm bật lên nhân tôm rim -->
    <path fill="#9E2A1C" d="M78 136
      C84 116 102 108 116 112
      C124 114 128 120 126 126
      C124 132 116 134 110 132
      C100 130 92 136 88 144
      C86 148 80 148 78 144
      C76 142 76 138 78 136 Z"/>
      
    <!-- Đuôi tôm rim (tail) -->
    <path fill="#9E2A1C" d="M116 112
      C122 106 128 106 132 110
      C132 114 128 118 122 118 Z"/>

    <!-- Hạt Tiêu & Mỡ Hành Vàng Hổ Phách (Golden Spice Accents) -->
    <circle cx="104" cy="124" r="4.5" fill="#D9822B"/>
    <circle cx="118" cy="136" r="3.5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

def create_concept_c_clean():
    # Concept C: "Bánh Lọc Gói Lá & Bếp Nhà Jun" (Artisanal Folded Leaf & Hearth)
    # Visual: A clean, elegant diamond/leaf badge showing the traditional wrapped Bánh Lọc Lá Quảng Bình!
    # In Quang Binh, Bánh Lọc Lá is wrapped in banana leaves into a neat, folded rectangle/pillow.
    # Here, two folded banana leaf folds cross gracefully to form a clean, warm emblem.
    # An open fold reveals the translucent crystal dumpling and braised red shrimp.
    # Above: 2 delicate warm steam wisps evoking the hot steamer.
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleC">
  <title id="titleC">Logo Bánh Lọc Nhà Jun — Concept C: Bánh Lọc Gói Lá &amp; Bếp Nhà</title>
  <g id="symbol">
    <!-- Khung Mẹt Tre Tròn Gia Truyền (Round Steamer Frame) -->
    <circle cx="128" cy="128" r="114" fill="none" stroke="#1A4329" stroke-width="8"/>
    <circle cx="128" cy="128" r="98" fill="none" stroke="#1A4329" stroke-width="3"/>

    <!-- Làn Khói Thơm Từ Xửng Hấp Nghi Ngút (Two graceful steam ribbons) -->
    <path fill="#D9822B" d="M120 48
      C116 58 122 66 118 76
      C117 78 114 78 113 76
      C111 66 119 58 115 48
      C116 46 119 46 120 48 Z"/>
    <path fill="#D9822B" d="M136 48
      C140 58 134 66 138 76
      C139 78 142 78 143 76
      C145 66 137 58 141 48
      C140 46 137 46 136 48 Z"/>

    <!-- Chiếc Lá Chuối Gói Bánh Xứ Quảng (Folded Banana Leaf Wrapper) -->
    <!-- Hai vạt lá chuối gập chéo tạo hình khối gối bánh truyền thống -->
    <path fill="#1A4329" d="M56 160
      C56 120 90 92 136 92
      C182 92 200 126 200 160
      C168 184 128 190 88 184
      C70 180 56 170 56 160 Z"/>

    <!-- Vạt Bánh Pha Lê Trong Suốt Hé Lộ (Translucent Dumpling Window) -->
    <path fill="#FAF7F2" d="M76 156
      C76 128 100 108 134 108
      C166 108 180 130 180 156
      C154 170 120 174 94 168
      C82 164 76 160 76 156 Z"/>

    <!-- Tôm Rim Đỏ Son Đậm Đà (Braised Shrimp Core) -->
    <!-- Uốn cong tự nhiên trong vạt bánh hé mở -->
    <path fill="#9E2A1C" d="M102 152
      C108 132 128 122 146 126
      C154 128 158 134 156 142
      C154 148 146 150 138 148
      C126 146 118 152 114 160
      C112 164 106 164 102 160
      C100 156 100 154 102 152 Z"/>

    <!-- Hạt Ngọc Mỡ Hành Vàng Óng (Golden amber accent) -->
    <circle cx="132" cy="138" r="4.5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

with open('banh-loc-nha-jun/logo/concept-a.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_a_clean())

with open('banh-loc-nha-jun/logo/concept-b.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_b_clean())

with open('banh-loc-nha-jun/logo/concept-c.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_c_clean())

print("Created 3 clean, solid concepts")
