import math
import subprocess

def create_concept_a():
    # Concept A: Monogram J & Bánh Lọc Scallop in Bamboo Steamer Rim
    # Clean geometry, R_outer=112, R_inner=98.
    # J is constructed with clean geometric curves:
    # Outer scalloped pleats: 3 elegant rhythmic arc pleats along the back.
    # Inner curve cradling an elegant curved shrimp.
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleA">
  <title id="titleA">Logo Bánh Lọc Nhà Jun — Concept A: Mẹt Tre &amp; Chữ J Xếp Nếp</title>
  <g id="symbol">
    <!-- Vành Mẹt Tre tối giản & vững chãi -->
    <path fill="#1A4329" fill-rule="evenodd" d="M128 16 C189.856 16 240 66.144 240 128 C240 189.856 189.856 240 128 240 C66.144 240 16 189.856 16 128 C16 66.144 66.144 16 128 16 Z M128 28 C72.772 28 28 72.772 28 128 C28 183.228 72.772 228 128 228 C183.228 228 228 183.228 228 128 C228 72.772 183.228 28 128 28 Z"/>
    
    <!-- Chữ J Bánh Lọc với nếp gấp thủ công thanh thoát -->
    <path fill="#1A4329" d="M142 50
      C154 50 166 56 166 70
      C166 76 162 82 158 86
      C168 90 172 98 172 108
      C172 116 166 122 162 126
      C170 132 174 142 174 152
      C174 186 146 206 112 206
      C78 206 58 186 58 162
      C58 148 68 138 82 138
      C96 138 106 148 106 162
      C106 172 98 180 88 182
      C95 186 103 188 112 188
      C132 188 152 174 152 150
      C152 138 148 130 144 122
      L144 72
      C144 58 142 50 142 50 Z"/>

    <!-- Tôm rim đỏ au uốn lượn sắc sảo (Artisanal Braised Shrimp) -->
    <path fill="#9E2A1C" d="M106 88
      C124 78 142 86 144 104
      C145 116 138 128 126 134
      C116 139 104 138 96 130
      C88 122 88 112 94 102
      C98 96 102 91 106 88 Z
      M116 100
      C110 104 106 110 107 116
      C108 121 112 123 118 121
      C124 119 128 114 127 109
      C126 104 122 100 116 100 Z" fill-rule="evenodd"/>

    <!-- Nốt vàng hổ phách (Măng tre / Hạt ngọc gia vị) -->
    <circle cx="124" cy="74" r="6" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

def create_concept_b():
    # Concept B: The Pure Translucent Dumpling & Crimson Shrimp (Pictorial / Minimalist Modern)
    # Silhouette of the crescent dumpling, delicate pleats, leaf base, glowing shrimp heart.
    # Center (128, 128)
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleB">
  <title id="titleB">Logo Bánh Lọc Nhà Jun — Concept B: Cánh Bánh Trong Veo &amp; Tôm Rim Ánh Son</title>
  <g id="symbol">
    <!-- Dải lá chuối xanh nâng đỡ đáy bánh (Banana Leaf Base) -->
    <path fill="#1A4329" d="M28 168 
      C64 198 132 208 196 186 
      C224 176 238 162 242 152 
      C224 168 184 186 136 186 
      C82 186 46 172 28 168 Z"/>

    <!-- Vỏ bánh lọc dẻo trong với 4 nếp gấp gập tay tinh tế (Translucent pleated dumpling) -->
    <path fill="#265C38" fill-rule="evenodd" d="M34 162
      C42 126 72 74 128 62
      C138 60 148 64 148 72
      C148 78 143 83 140 87
      C154 87 166 94 166 104
      C166 110 160 115 156 118
      C172 120 184 128 184 140
      C184 146 179 151 174 154
      C190 156 204 165 204 176
      C204 178 202 182 198 184
      C142 200 78 192 34 162 Z
      M58 156
      C88 174 140 178 178 162
      C174 150 160 140 144 138
      C130 118 116 102 96 92
      C70 106 58 132 58 156 Z"/>

    <!-- Nhân tôm rim đỏ tươi mướt mắt ở trung tâm (Glowing Crimson Shrimp Heart) -->
    <path fill="#9E2A1C" d="M92 114
      C112 102 138 108 144 126
      C148 138 140 150 126 156
      C112 162 98 158 90 148
      C84 140 84 130 90 122
      C88 126 90 134 96 138
      C104 144 116 142 122 134
      C128 126 124 118 114 116
      C104 114 96 118 92 114 Z"/>
      
    <!-- Đốm vàng óng ánh của tiêu măng rim (Golden spice accent) -->
    <circle cx="108" cy="110" r="5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

def create_concept_c():
    # Concept C: Mái Nhà & Chiếc Bánh Ấm Nồng (Heritage & Family / Combination Mark)
    # A warm sheltering roofline ("Nhà") protecting the artisanal bánh bột lọc on banana leaf with steam
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleC">
  <title id="titleC">Logo Bánh Lọc Nhà Jun — Concept C: Mái Nhà &amp; Bánh Lọc Xứ Quảng</title>
  <g id="symbol">
    <!-- Mái nhà vững chãi ấm cúng che chở (The sheltering home roof / Nhà) -->
    <path fill="#1A4329" d="M128 26
      L224 88
      C228 91 228 97 224 100
      L214 106
      C210 109 205 108 202 104
      L128 56
      L54 104
      C51 108 46 109 42 106
      L32 100
      C28 97 28 91 32 88
      Z"/>

    <!-- Làn khói thơm nghi ngút từ xửng hấp mẹt tre (Rising aromatic steam) -->
    <path fill="#D9822B" d="M112 70 C108 80 114 86 112 94 C111 96 109 96 108 94 C106 86 112 80 108 72 C107 70 111 68 112 70 Z"/>
    <path fill="#D9822B" d="M128 64 C124 76 130 84 128 94 C127 96 125 96 124 94 C122 84 128 76 124 66 C123 64 127 62 128 64 Z"/>
    <path fill="#D9822B" d="M144 70 C140 80 146 86 144 94 C143 96 141 96 140 94 C138 86 144 80 140 72 C139 70 143 68 144 70 Z"/>

    <!-- Chiếc bánh lọc tròn đầy viên mãn ở trung tâm (Plump folded bánh bột lọc) -->
    <path fill="#265C38" d="M64 166
      C64 124 94 106 128 106
      C162 106 192 124 192 166
      C176 160 156 156 128 156
      C100 156 80 160 64 166 Z"/>

    <!-- Nhân tôm rim đỏ au tỏa sáng ở lòng bánh (Red shrimp heart) -->
    <path fill="#9E2A1C" d="M108 126
      C120 118 136 118 148 126
      C152 130 148 136 142 134
      C134 130 122 130 114 134
      C108 136 104 130 108 126 Z"/>

    <!-- Đôi lá chuối xanh mướt nâng đỡ phía dưới (Banana leaves foundation) -->
    <path fill="#1A4329" d="M40 186
      C74 172 108 174 128 184
      C148 174 182 172 216 186
      C186 214 144 218 128 218
      C112 218 70 214 40 186 Z"/>
  </g>
</svg>'''
    return svg

with open('banh-loc-nha-jun/logo/concept-a.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_a())

with open('banh-loc-nha-jun/logo/concept-b.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_b())

with open('banh-loc-nha-jun/logo/concept-c.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_c())

print("Created concept-a.svg, concept-b.svg, concept-c.svg")
