#!/usr/bin/env python3
"""
Image Compression Script for HKU Urban Legend Tour
Compresses images to reduce file size while maintaining quality
"""

from PIL import Image
import os
import sys

def compress_image(input_path, output_path, quality=85, max_width=1920):
    """
    Compress an image with optional resizing
    
    Args:
        input_path: Path to input image
        output_path: Path to save compressed image
        quality: JPEG quality (1-100, default 85)
        max_width: Maximum width in pixels (maintains aspect ratio)
    """
    try:
        # Open image
        img = Image.open(input_path)
        
        # Convert RGBA to RGB if necessary (for PNG to JPEG conversion)
        if img.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
            img = background
        
        # Resize if image is too large
        if img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            print(f"  Resized to {max_width}x{new_height}")
        
        # Determine output format
        if output_path.lower().endswith('.png'):
            # For PNG, use optimize
            img.save(output_path, 'PNG', optimize=True)
        else:
            # For JPEG
            img.save(output_path, 'JPEG', quality=quality, optimize=True)
        
        # Get file sizes
        original_size = os.path.getsize(input_path)
        compressed_size = os.path.getsize(output_path)
        reduction = (1 - compressed_size / original_size) * 100
        
        print(f"  Original: {original_size / 1024 / 1024:.2f} MB")
        print(f"  Compressed: {compressed_size / 1024 / 1024:.2f} MB")
        print(f"  Reduction: {reduction:.1f}%")
        
        return True
    except Exception as e:
        print(f"  Error: {e}")
        return False

def main():
    img_dir = "img"
    
    # Create backup directory
    backup_dir = os.path.join(img_dir, "originals")
    os.makedirs(backup_dir, exist_ok=True)
    
    # Images to compress (you can modify this list)
    images_to_compress = [
        ("MB4.png", "MB4.jpg", 85, 1920),  # Convert PNG to JPEG
        ("Haking2.jpg", "Haking2.jpg", 85, 1920),
        ("kb2.jpg", "kb2.jpg", 85, 1920),
        ("Haking1.jpg", "Haking1.jpg", 85, 1920),
        ("lyh.jpg", "lyh.jpg", 85, 1920),
        ("eliothall.jpg", "eliothall.jpg", 85, 1920),
        ("kb1.jpg", "kb1.jpg", 85, 1920),
        ("MB3.jpg", "MB3.jpg", 85, 1920),
        ("RedWall.jpg", "RedWall.jpg", 85, 1920),
        ("knowles.JPG", "knowles.JPG", 85, 1920),
    ]
    
    print("Starting image compression...\n")
    
    for input_name, output_name, quality, max_width in images_to_compress:
        input_path = os.path.join(img_dir, input_name)
        
        if not os.path.exists(input_path):
            print(f"⚠️  {input_name} not found, skipping...")
            continue
        
        print(f"📸 Compressing {input_name}...")
        
        # Backup original
        backup_path = os.path.join(backup_dir, input_name)
        if not os.path.exists(backup_path):
            os.rename(input_path, backup_path)
            print(f"  Backed up to: {backup_path}")
        
        # Compress
        output_path = os.path.join(img_dir, output_name)
        success = compress_image(backup_path, output_path, quality, max_width)
        
        if success:
            print(f"✅ {output_name} compressed successfully!\n")
        else:
            print(f"❌ Failed to compress {input_name}\n")
    
    print("\n🎉 Compression complete!")
    print(f"Original files backed up in: {backup_dir}")
    
    # Calculate total space saved
    total_original = sum(os.path.getsize(os.path.join(backup_dir, f)) 
                         for f in os.listdir(backup_dir) if os.path.isfile(os.path.join(backup_dir, f)))
    total_compressed = sum(os.path.getsize(os.path.join(img_dir, f)) 
                           for f in os.listdir(img_dir) 
                           if os.path.isfile(os.path.join(img_dir, f)) and not f.startswith('.'))
    
    print(f"\nTotal original size: {total_original / 1024 / 1024:.2f} MB")
    print(f"Total compressed size: {total_compressed / 1024 / 1024:.2f} MB")
    print(f"Total space saved: {(total_original - total_compressed) / 1024 / 1024:.2f} MB")

if __name__ == "__main__":
    main()
