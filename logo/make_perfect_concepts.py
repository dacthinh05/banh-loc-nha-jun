import math
import subprocess

def create_concept_a():
    # Concept A: Monogram Emblem "Mẹt Tre & Chữ J Tinh Giản"
    # A bold, geometric, pristine J monogram inside a double bamboo circle.
    # Canvas 256x256. Center (128, 128).
    # Double ring:
    # Outer circle: R_out=114, R_in=106
    # Inner circle: R_out=98, R_in=94
    # Monogram J:
    # Stem at x=148, width 28. Descends from y=60 down to y=152.
    # Turns in a smooth circular arc with outer radius 54, inner radius 26.
    # Hooks up to x=72, y=140.
    # Inside the bowl of the J:
    # A beautifully stylized crimson shrimp silhouette in #9E2A1C at (112, 130).
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
    <path fill="#9E2A1C" d="M136 88
      C142 82 148 86 148 94
      C148 106 138 122 126 134
      C114 144 100 148 90 148
      C84 148 80 142 82 136
      C84 130 90 128 96 126
      C108 124 116 116 124 106
      C130 98 132 92 136 88 Z"/>
    <path fill="#9E2A1C" d="M82 136 C76 138 70 134 70 128 C76 130 82 132 86 132 Z"/>
    <path fill="#9E2A1C" d="M82 142 C76 146 68 144 66 138 C72 139 78 139 84 138 Z"/>

    <!-- Điểm Nhấn Mỡ Hành Vàng Hổ Phách (Golden Scallion Oil Dot) -->
    <circle cx="114" cy="104" r="5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

def create_concept_b():
    # Concept B: "Cánh Bánh Pha Lê & Tôm Rim" (Crystal Leaf Dumpling)
    # Inside the double bamboo circle:
    # A beautiful, graceful horizontal crystal leaf / canoe dumpling silhouette (vỏ bột pha lê trong veo).
    # Symmetrical horizontal geometry:
    # Outer leaf: tips at x=42 and x=214, swollen middle at y=128 (width 172, height 88).
    # Underneath: sweeping fresh banana leaf curve.
    # Inside: unmistakable curved crimson shrimp in the center.
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleB">
  <title id="titleB">Logo Bánh Lọc Nhà Jun — Concept B: Cánh Bánh Pha Lê &amp; Tôm Rim Ánh Son</title>
  <g id="symbol">
    <!-- Vòng Mẹt Tre Đôi Truyền Thống (Concentric Steamer Rim) -->
    <path fill="#1A4329" fill-rule="evenodd" d="M128 14 A114 114 0 1 0 128 242 A114 114 0 1 0 128 14 Z M128 22 A106 106 0 1 1 128 234 A106 106 0 1 1 128 22 Z"/>
    <path fill="#1A4329" fill-rule="evenodd" d="M128 30 A98 98 0 1 0 128 226 A98 98 0 1 0 128 30 Z M128 34 A94 94 0 1 1 128 222 A94 94 0 1 1 128 34 Z"/>

    <!-- Phiến Lá Chuối Nâng Đỡ Đáy Bánh (Banana Leaf Base) -->
    <path fill="#1A4329" d="M38 152
      C72 184 130 192 188 174
      C210 166 218 156 222 148
      C202 160 164 174 126 174
      C78 174 48 160 38 152 Z"/>

    <!-- Cánh Bánh Pha Lê Trong Veo (The Crystal Tapioca Leaf Silhouette) -->
    <!-- Đường cong hình chiếc lá hai đầu vuốt nhọn tự nhiên của bánh lọc -->
    <path fill="#1A4329" fill-rule="evenodd" d="M42 134
      C72 90 128 80 184 96
      C206 102 216 114 216 122
      C196 156 142 168 88 154
      C60 146 48 138 42 134 Z
      M64 132
      C88 104 132 98 174 110
      C188 114 194 122 192 126
      C176 146 136 154 98 144
      C78 138 68 134 64 132 Z"/>

    <!-- Chú Tôm Rim Đỏ Son Tuyệt Đẹp Ở Tâm Bánh (Artisanal Braised Shrimp Core) -->
    <path fill="#9E2A1C" d="M96 138
      C104 118 126 110 144 114
      C152 116 158 122 154 130
      C150 136 142 138 134 136
      C122 134 114 138 110 146
      C106 150 100 152 96 148
      C92 144 92 140 96 138 Z"/>
    <path fill="#9E2A1C" d="M144 114 C150 106 158 104 162 108 C164 112 160 118 154 120 Z"/>

    <!-- Điểm Xuyết Mỡ Hành & Hạt Tiêu (Scallion oil & pepper accent) -->
    <circle cx="128" cy="126" r="4.5" fill="#D9822B"/>
    <circle cx="140" cy="134" r="3.5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

def create_concept_c():
    # Concept C: "Bánh Lọc Tam Vị Mẹt Tre" (The Signature Trio Steamer - Radial Harmony)
    # Representing the signature Combo 3 Vị: Tôm Thịt Măng, Măng Thịt Nấm, Bánh Chay!
    # Inside the bamboo steamer, 3 stylized crystal dumplings curve in dynamic radial harmony (120 degrees apart),
    # forming an organic triquetra / triskelion that symbolizes heritage, family, and culinary abundance.
    # Center: A glowing red shrimp triskelion core.
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleC">
  <title id="titleC">Logo Bánh Lọc Nhà Jun — Concept C: Mẹt Bánh Tam Vị Gia Truyền</title>
  <g id="symbol">
    <!-- Vòng Mẹt Tre Đôi Truyền Thống (Concentric Steamer Rim) -->
    <path fill="#1A4329" fill-rule="evenodd" d="M128 14 A114 114 0 1 0 128 242 A114 114 0 1 0 128 14 Z M128 22 A106 106 0 1 1 128 234 A106 106 0 1 1 128 22 Z"/>
    <path fill="#1A4329" fill-rule="evenodd" d="M128 30 A98 98 0 1 0 128 226 A98 98 0 1 0 128 30 Z M128 34 A94 94 0 1 1 128 222 A94 94 0 1 1 128 34 Z"/>

    <!-- 3 Cánh Bánh Lọc Tam Vị Xoay Tròn Hòa Hợp (Three Dumplings in Radial Harmony) -->
    <!-- Bánh 1 (Đỉnh 12h) -->
    <g transform="translate(128, 128)">
      <!-- Dumpling 1 at 0 deg -->
      <path fill="#1A4329" d="M-14 -72 C-2 -92 28 -88 44 -74 C34 -58 14 -50 -2 -50 C-10 -50 -16 -60 -14 -72 Z" transform="rotate(0)"/>
      <path fill="#9E2A1C" d="M6 -72 C14 -80 26 -78 30 -70 C24 -64 12 -62 6 -72 Z" transform="rotate(0)"/>
      <circle cx="16" cy="-64" r="3.5" fill="#D9822B" transform="rotate(0)"/>

      <!-- Dumpling 2 at 120 deg -->
      <path fill="#1A4329" d="M-14 -72 C-2 -92 28 -88 44 -74 C34 -58 14 -50 -2 -50 C-10 -50 -16 -60 -14 -72 Z" transform="rotate(120)"/>
      <path fill="#9E2A1C" d="M6 -72 C14 -80 26 -78 30 -70 C24 -64 12 -62 6 -72 Z" transform="rotate(120)"/>
      <circle cx="16" cy="-64" r="3.5" fill="#D9822B" transform="rotate(120)"/>

      <!-- Dumpling 3 at 240 deg -->
      <path fill="#1A4329" d="M-14 -72 C-2 -92 28 -88 44 -74 C34 -58 14 -50 -2 -50 C-10 -50 -16 -60 -14 -72 Z" transform="rotate(240)"/>
      <path fill="#9E2A1C" d="M6 -72 C14 -80 26 -78 30 -70 C24 -64 12 -62 6 -72 Z" transform="rotate(240)"/>
      <circle cx="16" cy="-64" r="3.5" fill="#D9822B" transform="rotate(240)"/>

      <!-- Tâm Điểm: Tôm Rim Đỏ Son Tam Hợp (Central Red Shrimp Crest) -->
      <path fill="#9E2A1C" d="M-4 -20 C18 -26 26 -6 20 14 C12 32 -10 24 -16 6 C-18 -4 -12 -16 -4 -20 Z M2 -8 C-4 -6 -6 0 -4 6 C-2 10 4 10 8 6 C10 2 8 -4 2 -8 Z" fill-rule="evenodd"/>
      <circle cx="0" cy="0" r="4.5" fill="#D9822B"/>
    </g>
  </g>
</svg>'''
    return svg

with open('banh-loc-nha-jun/logo/concept-a.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_a())

with open('banh-loc-nha-jun/logo/concept-b.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_b())

with open('banh-loc-nha-jun/logo/concept-c.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_c())

print("Created perfect concepts A, B, and C")
