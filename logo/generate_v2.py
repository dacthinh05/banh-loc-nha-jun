import math
import subprocess

def create_concept_a_v2():
    # Concept A: Monogram Emblem "Mẹt Tre & Chữ J Xứ Quảng"
    # Outer circle: Bamboo steamer rim R_out=112, R_in=96 (clean concentric geometry with 4 neat bamboo joint accents)
    # Inside: A majestic, fluid Letter "J" where the stem descends from top-right and sweeps into a graceful crescent hook.
    # The hook of the J represents the folded dumpling, with 3 delicate scalloped crimps along the outer bottom curve.
    # Cradled in the bowl of the J is an unmistakable silhouette of an artisanal braised shrimp (tôm rim) in vibrant red #9E2A1C.
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleA">
  <title id="titleA">Logo Bánh Lọc Nhà Jun — Concept A: Mẹt Tre &amp; Chữ J Xứ Quảng</title>
  <g id="symbol">
    <!-- Vành Mẹt Tre Gia Truyền (Concentric Bamboo Steamer Rim) -->
    <path fill="#1A4329" fill-rule="evenodd" d="M128 16 C189.856 16 240 66.144 240 128 C240 189.856 189.856 240 128 240 C66.144 240 16 189.856 16 128 C16 66.144 66.144 16 128 16 Z M128 30 C73.876 30 30 73.876 30 128 C30 182.124 73.876 226 128 226 C182.124 226 226 182.124 226 128 C226 73.876 182.124 30 128 30 Z"/>

    <!-- 4 Khía Mây Nẹp Vành Tre Đối Xứng Tinh Tế (Bamboo rim ties) -->
    <rect x="125" y="16" width="6" height="14" rx="2" fill="#FAF7F2"/>
    <rect x="125" y="226" width="6" height="14" rx="2" fill="#FAF7F2"/>
    <rect x="16" y="125" width="14" height="6" rx="2" fill="#FAF7F2"/>
    <rect x="226" y="125" width="14" height="6" rx="2" fill="#FAF7F2"/>

    <!-- Chữ J Cách Điệu từ Cánh Bánh Lọc (Letter J Monogram with Folded Pleats) -->
    <!-- Thân chữ J dứt khoát từ trên xuống, uốn lượn hình trăng khuyết nâng đỡ -->
    <path fill="#1A4329" d="M148 52 
      L172 52 
      C172 52 172 136 172 146 
      C172 178 144 204 108 204 
      C70 204 48 178 48 148 
      C48 132 60 120 76 120 
      C92 120 102 132 102 148 
      C102 160 94 168 84 170 
      C90 178 100 182 110 182 
      C132 182 148 166 148 142 
      Z"/>

    <!-- Chiếc Bánh Lọc Xếp Nếp Gập Mí (Scalloped dumpling wing on the J's back) -->
    <path fill="#265C38" d="M172 90
      C182 92 190 100 190 110
      C190 118 184 124 178 128
      C186 132 192 140 192 150
      C192 160 184 170 174 174
      C180 180 184 188 180 196
      C176 202 166 204 156 200
      C164 190 170 176 170 160
      C170 134 172 106 172 90 Z"/>

    <!-- Tôm Rim Đỏ Son Tuyệt Mỹ Ở Lòng Chữ J (Artisanal Braised Shrimp Silhouette) -->
    <!-- Uốn cong tự nhiên: Thân tôm dày, đuôi cong vuốt nhọn, râu khẽ uốn -->
    <path fill="#9E2A1C" d="M136 84
      C142 80 148 82 150 88
      C152 96 146 106 138 116
      C128 128 118 136 104 140
      C96 142 88 140 86 134
      C84 128 90 124 96 122
      C106 120 116 114 124 104
      C130 96 132 88 136 84 Z"/>

    <!-- Hạt Tiêu & Mỡ Hành Gia Truyền (Golden spice accent) -->
    <circle cx="116" cy="100" r="5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

def create_concept_b_v2():
    # Concept B: "Cánh Bánh Bán Nguyệt & Tôm Rim Ánh Son" (Authentic Bánh Bột Lọc Silhouette)
    # The quintessential crescent shape of Bánh Bột Lọc:
    # Top edge: Beautiful arched back with 4 delicate hand-crimped scallops (nếp gấp viền bánh).
    # Inside: Translucent body showing the iconic curved red shrimp with tail.
    # Bottom: Fresh green banana leaf curve cradling the dumpling.
    # Clean, balanced, appetizing, 100% recognizable as Vietnamese Bánh Bột Lọc.
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleB">
  <title id="titleB">Logo Bánh Lọc Nhà Jun — Concept B: Cánh Bánh Bán Nguyệt &amp; Tôm Rim Ánh Son</title>
  <g id="symbol">
    <!-- Dải Lá Chuối Xanh Mướt Nâng Đỡ (Fresh Banana Leaf Foundation) -->
    <path fill="#1A4329" d="M24 164
      C62 198 132 208 198 186
      C226 176 238 162 244 150
      C224 168 182 186 132 186
      C78 186 42 170 24 164 Z"/>

    <!-- Thân Bánh Lọc Bán Nguyệt Dẻo Trong (The Translucent Tapioca Dumpling Body) -->
    <!-- Viền trên lượn 4 nếp gấp gập mí thủ công mềm mại, chuẩn nét ẩm thực xứ Quảng -->
    <path fill="#265C38" d="M38 154
      C44 116 78 72 132 64
      C142 62 152 68 150 76
      C148 82 142 86 138 90
      C152 90 164 98 162 108
      C160 114 154 118 148 122
      C162 124 174 132 172 142
      C170 148 164 152 158 156
      C172 158 182 168 180 176
      C178 180 172 182 166 182
      C118 192 68 184 38 154 Z"/>

    <!-- Vùng Bột Trong Suốt Ở Tâm Bánh (Translucent negative space revealing the filling) -->
    <path fill="#FAF7F2" d="M58 150
      C76 118 108 92 138 94
      C148 114 154 140 152 168
      C116 174 80 168 58 150 Z"/>

    <!-- Tôm Rim Đỏ Au Đậm Đà Nép Giữa Bánh (Signature Braised Shrimp Filling) -->
    <path fill="#9E2A1C" d="M82 144
      C88 122 108 108 128 112
      C136 114 142 120 140 128
      C138 136 130 140 122 138
      C112 136 102 142 98 152
      C96 156 90 158 86 156
      C82 154 80 148 82 144 Z"/>

    <!-- Đuôi tôm rim uốn lượn sắc sảo (Shrimp tail detail) -->
    <path fill="#9E2A1C" d="M128 112
      C134 104 142 100 146 104
      C148 108 144 114 138 118
      Z"/>

    <!-- Hạt Màng Tiêu/Mỡ Hành Thơm Lừng (Aromatic scallion oil / pepper accent) -->
    <circle cx="118" cy="126" r="4.5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

def create_concept_c_v2():
    # Concept C: "Bếp Nhà Jun & Mẹt Bánh Xứ Quảng" (Artisanal Heritage Cartouche / Seal)
    # A sophisticated artisanal food seal:
    # Hexagonal / Rounded Diamond Steamer Cartouche with bamboo woven corners.
    # Inside: A pair of fresh banana leaves cradling a plump Bánh Bột Lọc with 2 rising aromatic steam ribbons.
    # At top: A classic roof crest ("Nhà") protecting the kitchen's craft.
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleC">
  <title id="titleC">Logo Bánh Lọc Nhà Jun — Concept C: Bếp Nhà &amp; Hương Vị Gia Truyền</title>
  <g id="symbol">
    <!-- Khung Mái Nhà Gia Đình Ấm Cúng (Warm Sheltering Roofline) -->
    <!-- Góc nghiêng 45 độ chuẩn xác tuyệt đối (exact 45-degree angles) -->
    <path fill="#1A4329" d="M128 28
      L214 114
      C217 117 217 123 214 126
      L204 136
      C201 139 195 139 192 136
      L128 72
      L64 136
      C61 139 55 139 52 136
      L42 126
      C39 123 39 117 42 114
      Z"/>

    <!-- Hai làn hương khói bánh nóng hổi bốc lên (Rising aromatic steam ribbons) -->
    <path fill="#D9822B" d="M118 78
      C114 88 122 96 118 106
      C117 108 114 108 113 106
      C111 96 119 88 115 78
      C116 76 119 76 118 78 Z"/>
    <path fill="#D9822B" d="M138 78
      C142 88 134 96 138 106
      C139 108 142 108 143 106
      C145 96 137 88 141 78
      C140 76 137 76 138 78 Z"/>

    <!-- Chiếc Bánh Lọc Bán Nguyệt Căng Mọng (Plump artisanal dumpling) -->
    <path fill="#265C38" d="M68 160
      C68 122 96 102 128 102
      C160 102 188 122 188 160
      C170 154 150 150 128 150
      C106 150 86 154 68 160 Z"/>

    <!-- Tôm Rim Đỏ Ánh Son Ở Trung Tâm Bánh (Red Shrimp Heart) -->
    <path fill="#9E2A1C" d="M106 126
      C118 116 138 116 150 126
      C146 134 138 132 128 132
      C118 132 110 134 106 126 Z"/>

    <!-- Đôi Lá Chuối Xanh Nâng Đỡ Tựa Đôi Bàn Tay Gìn Giữ (Banana Leaf Base) -->
    <path fill="#1A4329" d="M42 182
      C76 168 108 170 128 182
      C148 170 180 168 214 182
      C184 212 144 218 128 218
      C112 218 72 212 42 182 Z"/>
      
    <!-- Nốt vàng tiêu măng (Golden spice dot) -->
    <circle cx="128" cy="142" r="4.5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

with open('banh-loc-nha-jun/logo/concept-a.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_a_v2())

with open('banh-loc-nha-jun/logo/concept-b.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_b_v2())

with open('banh-loc-nha-jun/logo/concept-c.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_c_v2())

print("Updated concept-a.svg, concept-b.svg, concept-c.svg to v2")
