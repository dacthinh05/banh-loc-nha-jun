# Script to construct Concept A, B, and C with exact vector geometry
import math
import os
import subprocess

def create_concept_a_symbol():
    # Concept A: Monogram J + Bamboo Basket Rim + Shrimp filling
    # 256x256 canvas
    # Colors: Green #1A4329, Red #9E2A1C
    
    # Outer ring: Bamboo tray / mẹt tre rim
    # Radius outer: 114, Radius inner: 100. Center (128, 128)
    # With 4 subtle diagonal binding accents (mây quấn vành tre)
    # Ring path with evenodd rule:
    # Outer circle: M 128 14 A 114 114 0 1 0 128 242 A 114 114 0 1 0 128 14 Z
    # Inner circle: M 128 28 A 100 100 0 1 1 128 228 A 100 100 0 1 1 128 28 Z
    
    # Let's construct the stylized "J" Bánh Lọc:
    # Stem top at x=148, y=52.
    # The right outer edge has 3 gentle scalloped ripples (nếp gấp bánh lọc):
    # Ripple 1: y=52 to 92
    # Ripple 2: y=92 to 132
    # Ripple 3: curve around the bend to y=172, x=136
    # Then sweeping arc up to the tip of J at x=78, y=148.
    # Inner contour curves smoothly back.
    # Shrimp shape: centered around (114, 134), stylized crescent/comma.
    
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256" role="img" aria-labelledby="titleA">
  <title id="titleA">Logo Bánh Lọc Nhà Jun — Concept A: Mẹt Tre &amp; Chữ J Xếp Nếp</title>
  <g id="symbol">
    <!-- Vành mẹt tre truyền thống (Bamboo tray ring) -->
    <path fill="#1A4329" fill-rule="evenodd" d="M128 16 C189.856 16 240 66.144 240 128 C240 189.856 189.856 240 128 240 C66.144 240 16 189.856 16 128 C16 66.144 66.144 16 128 16 Z M128 28 C72.772 28 28 72.772 28 128 C28 183.228 72.772 228 128 228 C183.228 228 228 183.228 228 128 C228 72.772 183.228 28 128 28 Z"/>
    
    <!-- 4 Khía mây buộc mẹt tre (Tradition bamboo basket lashings) -->
    <path fill="#FAF7F2" d="M46 52 L52 46 L58 52 L52 58 Z M204 52 L210 46 L216 52 L210 58 Z M46 204 L52 198 L58 204 L52 210 Z M204 204 L210 198 L216 204 L210 210 Z"/>

    <!-- Thân chữ J Bánh Lọc với viền xếp nếp thủ công -->
    <!-- Bắt đầu từ đỉnh phải chữ J, lượn 3 nếp gấp bánh, cong qua đáy và vuốt lên mỏm J -->
    <path fill="#1A4329" d="M140 48 
      C152 48 164 54 164 68 
      C164 74 161 78 157 82 
      C166 86 170 94 170 104 
      C170 112 165 118 160 122 
      C168 128 172 138 172 150 
      C172 186 142 208 106 208 
      C72 208 52 186 52 160 
      C52 144 64 134 78 134 
      C92 134 102 144 102 158 
      C102 168 98 174 92 178 
      C98 184 106 186 114 186 
      C134 186 148 172 148 146 
      L148 70 
      C148 58 144 48 140 48 Z"/>
      
    <!-- Nhân tôm rim đỏ ánh son nép trong lòng chữ J (Shrimp filling heart) -->
    <path fill="#9E2A1C" d="M108 92 
      C126 84 142 94 144 112 
      C145 124 139 135 128 142 
      C117 149 104 149 96 141 
      C88 133 88 121 94 110 
      C98 103 103 97 108 92 Z 
      M116 104 
      C111 108 107 114 108 122 
      C109 127 114 130 120 128 
      C126 126 130 120 129 114 
      C128 108 123 104 116 104 Z" fill-rule="evenodd"/>
      
    <!-- Hạt mè/tiêu điểm xuyết nhỏ tinh tế (Subtle spice accent) -->
    <circle cx="120" cy="80" r="5" fill="#D9822B"/>
  </g>
</svg>'''
    return svg

with open('banh-loc-nha-jun/logo/concept-a-v1.svg', 'w', encoding='utf-8') as f:
    f.write(create_concept_a_symbol())
print("Created concept-a-v1.svg")
