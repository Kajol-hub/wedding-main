"""
Downloads placeholder images for the wedding website.
Run this once to populate the static/images folder.
Replace with real images later.
"""
import os
import urllib.request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "static", "images")
MUSIC_DIR = os.path.join(BASE_DIR, "static", "music")

os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(MUSIC_DIR, exist_ok=True)

# Placeholder images from picsum.photos (free, no API key needed)
placeholders = {
    "hero.jpg": "https://picsum.photos/id/1024/1920/1080",        # Wedding/couple vibe
    "bride1.jpg": "https://picsum.photos/id/64/600/800",           # Gallery 1
    "bride2.jpg": "https://picsum.photos/id/65/600/800",           # Gallery 2
    "bride3.jpg": "https://picsum.photos/id/91/600/800",           # Gallery 3
    "venue.jpg": "https://picsum.photos/id/164/1200/600",          # Venue
    "parents1.jpg": "https://picsum.photos/id/177/400/500",        # Parents 1
    "parents2.jpg": "https://picsum.photos/id/203/400/500",        # Parents 2
    "parents3.jpg": "https://picsum.photos/id/219/400/500",        # Parents 3
    "parents4.jpg": "https://picsum.photos/id/256/400/500",        # Parents 4
}

print("🎉 Wedding Website - Downloading placeholder images...\n")

for filename, url in placeholders.items():
    filepath = os.path.join(IMAGES_DIR, filename)
    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
        print(f"  ✓ {filename} (already exists)")
        continue
    try:
        print(f"  ⬇ Downloading {filename}...")
        urllib.request.urlretrieve(url, filepath)
        print(f"  ✓ Saved {filename}")
    except Exception as e:
        print(f"  ✗ Failed {filename}: {e}")

# Create a placeholder music file (silent - replace with real song later)
music_path = os.path.join(MUSIC_DIR, "wedding-song.mp3")
if not os.path.exists(music_path) or os.path.getsize(music_path) == 0:
    # Minimal valid MP3 file (silent frame)
    mp3_header = bytes([
        0xFF, 0xFB, 0x90, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    ]) * 100
    with open(music_path, "wb") as f:
        f.write(mp3_header)
    print(f"\n  ✓ Created placeholder music file (replace with real .mp3 later)")

print("\n✅ Setup complete! Run: python app.py")
print("   Then open: http://127.0.0.1:5000")

