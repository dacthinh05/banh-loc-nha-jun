import math
import subprocess

def create_concept_a_master():
    # Concept A: Monogram "Chữ J Tôm Quê" (The Shrimp-J Monogram)
    # The letter J is crafted from the organic, dynamic form of the cooked shrimp!
    # The top is crisp and architectural (x=150 to 176, y=56 to 140).
    # The bottom hook sweeps around (R_outer=58, R_inner=28) and terminates in a stylized 2-blade shrimp tail!
    # A warm amber dot #D9822B sits in the negative space as the golden spice/eye.
    # Framed in a crisp double circular bamboo ring.
    # 256x256, center (128, 128).
    # Zero unintended readings, iconic letterform J, 100% brand ownable.
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleA">
  <title id="titleA">Logo Bánh Lọc Nhà Jun — Concept A: Chữ J Tôm Quê</title>
  <g id="symbol">
    <!-- Vành Mẹt Tre Đôi Truyền Thống (Bamboo Steamer Rim) -->
    <path fill="#1A4329" fill-rule="evenodd" d="M128 14 A114 114 0 1 0 128 242 A114 114 0 1 0 128 14 Z M128 22 A106 106 0 1 1 128 234 A106 106 0 1 1 128 22 Z"/>
    <path fill="#1A4329" fill-rule="evenodd" d="M128 30 A98 98 0 1 0 128 226 A98 98 0 1 0 128 30 Z M128 34 A94 94 0 1 1 128 222 A94 94 0 1 1 128 34 Z"/>

    <!-- Thân Chữ J Vững Chãi Màu Xanh Lá Chuối (Green J Stem) -->
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

    <!-- Chú Tôm Rim Đỏ Son Lượn Dọc Lưng Chữ J (Crimson Braised Shrimp Arc) -->
    <!-- Uốn cong tự nhiên ôm lấy chữ J, tạo thành biểu tượng kép J + Tôm -->
    <path fill="#9E2A1C" d="M136 76
      C148 70 162 76 164 88
      C166 102 152 122 138 136
      C124 148 108 154 94 154
      C84 154 78 146 80 138
      C82 130 90 126 98 124
      C112 122 122 112 128 98
      C132 88 132 80 136 76 Z"/>
    <!-- Đuôi tôm sắc sảo (Tail fin) -->
    <path fill="#9E2A1C" d="M80 138 C72 142 64 138 64 130 C72 132 78 134 84 134 Z"/>
    <path fill="#9E2A1C" d="M80 146 C72 152 62 148 60 140 C68 142 76 143 82 141 Z"/>

    <!-- Hạt Ngọc Mỡ Hành Vàng Hổ Phách (Golden Spice Accent) -->
    <circle cx="112" cy="98" r="5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

def create_concept_b_master():
    # Concept B: "Chiếc Bánh Mẹt Tre & Nếp Gấp Gia Truyền" (Artisanal Dumpling in Bamboo Steamer)
    # A clear, top-down presentation:
    # A single, plump, folded Bánh Lọc sitting gracefully on a lush green banana leaf.
    # The dumpling has a smooth rounded belly and an arched back with 3 hand-folded pleats.
    # Inside the body: the unmistakable red shrimp filling is visible through the translucent dough.
    # Framed in the double bamboo rim.
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleB">
  <title id="titleB">Logo Bánh Lọc Nhà Jun — Concept B: Bánh Lọc Mẹt Tre Truyền Thống</title>
  <g id="symbol">
    <!-- Vòng Mẹt Tre Đôi Truyền Thống (Bamboo Steamer Rim) -->
    <path fill="#1A4329" fill-rule="evenodd" d="M128 14 A114 114 0 1 0 128 242 A114 114 0 1 0 128 14 Z M128 22 A106 106 0 1 1 128 234 A106 106 0 1 1 128 22 Z"/>
    <path fill="#1A4329" fill-rule="evenodd" d="M128 30 A98 98 0 1 0 128 226 A98 98 0 1 0 128 30 Z M128 34 A94 94 0 1 1 128 222 A94 94 0 1 1 128 34 Z"/>

    <!-- Phiến Lá Chuối Lót Mẹt (Banana Leaf Bed) -->
    <path fill="#1A4329" d="M42 168
      C76 198 134 204 186 186
      C212 176 220 164 222 154
      C200 168 162 182 124 182
      C78 182 50 170 42 168 Z"/>

    <!-- Chiếc Bánh Bột Lọc Bán Nguyệt Với Nếp Gấp Thủ Công (Pleated Dumpling) -->
    <!-- Dáng bán nguyệt nghiêng 15 độ, viền lưng có 3 nếp gấp gập tay -->
    <path fill="#1A4329" d="M54 150
      C58 116 86 86 122 76
      C132 74 142 80 138 90
      C134 96 126 100 122 104
      C138 104 148 112 144 122
      C142 128 134 132 126 136
      C142 138 152 148 146 158
      C142 164 132 166 120 166
      C88 166 64 158 54 150 Z"/>

    <!-- Khoảng Bột Trong Veo & Nhân Tôm Rim Đỏ Son (Translucent Window & Red Shrimp) -->
    <path fill="#9E2A1C" d="M78 142
      C84 122 104 112 120 116
      C128 118 132 126 128 132
      C124 138 116 138 108 136
      C98 134 90 142 86 148
      C84 150 80 148 78 142 Z"/>
    <path fill="#9E2A1C" d="M120 116 C126 108 134 108 138 112 C138 116 134 122 128 122 Z"/>

    <!-- Điểm Nhấn Mỡ Hành Vàng Hổ Phách (Golden Scallion Oil) -->
    <circle cx="106" cy="128" r="4.5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

def create_concept_c_master():
    # Concept C: "Dải Lụa Ẩm Thực & Bếp Nhà Jun" (Modern Culinary S-Swirl)
    # An iconic, flowing Yin-Yang / S-curve harmony of Leaf Green #1A4329 and Shrimp Red #9E2A1C.
    # The green curve evokes the fresh banana leaf wrapping and the letter J.
    # The red curve evokes the tender, savory braised shrimp.
    # Together they rotate into a continuous, harmonious circle of flavor, care, and heritage.
    # Ultra-clean, timeless, scales to 16px perfectly, zero clutter.
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleC">
  <title id="titleC">Logo Bánh Lọc Nhà Jun — Concept C: Dải Lụa Ẩm Thực &amp; Bếp Nhà</title>
  <g id="symbol">
    <!-- Vòng Mẹt Tre Đôi Truyền Thống (Bamboo Steamer Rim) -->
    <path fill="#1A4329" fill-rule="evenodd" d="M128 14 A114 114 0 1 0 128 242 A114 114 0 1 0 128 14 Z M128 22 A106 106 0 1 1 128 234 A106 106 0 1 1 128 22 Z"/>
    <path fill="#1A4329" fill-rule="evenodd" d="M128 30 A98 98 0 1 0 128 226 A98 98 0 1 0 128 30 Z M128 34 A94 94 0 1 1 128 222 A94 94 0 1 1 128 34 Z"/>

    <!-- Dải Xanh Lá Chuối & Chữ J Cách Điệu (The Green Leaf & J Wave) -->
    <path fill="#1A4329" d="M128 42
      C168 42 196 74 196 114
      C196 150 172 174 140 174
      C116 174 98 158 98 138
      C98 122 110 110 126 110
      C138 110 146 118 146 128
      C146 134 142 140 136 142
      C132 144 128 142 126 140
      C124 146 130 152 138 152
      C154 152 172 136 172 112
      C172 84 150 62 124 62
      C92 62 66 90 66 128
      C66 170 96 200 138 200
      C150 200 162 196 172 190
      C160 204 144 212 126 212
      C78 212 44 174 44 128
      C44 80 80 42 128 42 Z"/>

    <!-- Dải Đỏ Son Tôm Rim Uốn Lượn Đối Xứng (The Crimson Shrimp Flame) -->
    <path fill="#9E2A1C" d="M136 78
      C152 82 164 96 164 114
      C164 136 146 156 126 156
      C112 156 104 146 104 136
      C104 128 110 122 116 122
      C122 122 126 126 126 130
      C124 132 120 132 118 130
      C118 134 122 138 128 138
      C138 138 148 126 148 112
      C148 98 138 88 128 86
      C118 84 108 88 100 94
      C108 84 122 76 136 78 Z"/>

    <!-- Hạt Ngọc Mỡ Hành Vàng Hổ Phách (Golden Center Dot) -->
    <circle cx="128" cy="128" r="6" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

with open('banh-loc-nha-jun/logo/concept-a.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_a_master())

with open('banh-loc-nha-jun/logo/concept-b.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_b_master())

with open('banh-loc-nha-jun/logo/concept-c.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_c_master())

print("Successfully written master concepts A, B, and C")
