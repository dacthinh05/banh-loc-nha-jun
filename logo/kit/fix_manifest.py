import os
import shutil
import json

KIT_DIR = "banh-loc-nha-jun/logo/kit"
VARIANTS_DIR = os.path.join(KIT_DIR, "variants")

# 1. Update site.webmanifest with clean relative icon paths
manifest_data = {
  "name": "Bánh Lọc Nhà Jun",
  "short_name": "Nhà Jun",
  "icons": [
    {
      "src": "icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "icon-512.png",
      "sizes": "512x512",
      "type": "image/png"
    },
    {
      "src": "maskable-512.png",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "maskable"
    }
  ],
  "theme_color": "#1A4329",
  "background_color": "#FAF7F2",
  "display": "standalone",
  "start_url": "./index.html"
}

with open(os.path.join(VARIANTS_DIR, "site.webmanifest"), "w", encoding="utf-8") as f:
    json.dump(manifest_data, f, indent=2, ensure_ascii=False)

# 2. Destinations to sync
dest_dirs = [
    "banh-loc-nha-jun/assets",
    "public/showcase/banh-loc-nha-jun/assets",
    "public/images/banh-loc"
]

files_to_sync = [
    "favicon.ico",
    "favicon.svg",
    "apple-touch-icon.png",
    "icon-192.png",
    "icon-512.png",
    "maskable-512.png",
    "site.webmanifest"
]

for d in dest_dirs:
    os.makedirs(d, exist_ok=True)
    for fname in files_to_sync:
        src = os.path.join(VARIANTS_DIR, fname)
        if os.path.exists(src):
            dst = os.path.join(d, fname)
            shutil.copy2(src, dst)
            print(f"Synced {fname} -> {d}")

print("Manifest and icon sync finished successfully!")
