#!/usr/bin/env python3
"""
Generate placeholder product images for Plated by Benny website.
Requires: pip install pillow
"""

from PIL import Image, ImageDraw, ImageFont
import os

def generate_placeholder_image(filename, product_name, color_hex):
    """Generate a placeholder image for a product."""
    width, height = 400, 400

    # Convert hex to RGB
    color = tuple(int(color_hex[i:i+2], 16) for i in (0, 2, 4))

    # Create image with gradient-like effect
    img = Image.new('RGB', (width, height), color='#FAF8F3')
    draw = ImageDraw.Draw(img)

    # Draw a jar shape
    jar_color = color
    # Jar lid
    draw.rectangle([150, 80, 250, 100], fill=jar_color)
    draw.rectangle([140, 100, 260, 110], fill=color, outline='#D4AF37', width=2)

    # Jar body
    draw.polygon([(150, 110), (250, 110), (240, 380), (160, 380)],
                 fill='#FAF8F3', outline=jar_color, width=3)

    # Jar content (colored inside)
    draw.polygon([(155, 140), (245, 140), (240, 375), (165, 375)],
                 fill=jar_color, outline=None)

    # Add some texture/pattern
    for i in range(155, 245, 15):
        draw.ellipse([i, 150, i+10, 160], fill='#D4AF37', outline=None)
        draw.ellipse([i+8, 170, i+18, 180], fill='#D4AF37', outline=None)

    # Add product name
    try:
        # Try to use a nice font, fall back to default
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
    except:
        font = ImageFont.load_default()

    # Draw product name at bottom
    bbox = draw.textbbox((0, 0), product_name, font=font)
    text_width = bbox[2] - bbox[0]
    text_x = (width - text_width) // 2
    draw.text((text_x, 320), product_name, fill='#C41E3A', font=font)

    # Save image
    img.save(filename)
    print(f"✓ Generated {filename}")

def main():
    """Generate all product placeholder images."""
    os.makedirs('assets', exist_ok=True)

    products = [
        ('assets/malabar-carrot.jpg', 'Malabar Spiced\nCarrot', '#FFD700'),
        ('assets/labneh-pearls.jpg', 'Labneh\nPearls', '#F5DEB3'),
        ('assets/honey-butter-blaze.jpg', 'Honey Butter\nBlaze', '#DAA520'),
        ('assets/midnight-hummus.jpg', 'Midnight\nHummus', '#2F4F4F'),
        ('assets/red-beret-salsa.jpg', 'Red Beret\nSalsa', '#DC143C'),
    ]

    print("Generating placeholder product images...\n")
    for filename, product_name, color in products:
        generate_placeholder_image(filename, product_name, color)

    print("\n✓ All images generated successfully!")
    print("Place these in the assets folder for the website to display properly.")

if __name__ == '__main__':
    main()
