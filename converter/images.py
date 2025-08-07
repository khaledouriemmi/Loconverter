from PIL import Image
import os

def convert_image(input_path: str, output_path: str, target_format: str) -> None:
    """Convert images between different formats using Pillow.

    Args:
        input_path: Path to the input image
        output_path: Path where the converted image will be saved
        target_format: Desired output format (e.g., 'jpg', 'png', 'webp')

    Raises:
        Exception: If conversion fails
    
    Supports: PNG, JPG/JPEG, TIFF, BMP, WebP
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Convert RGBA to RGB if saving as JPEG
            if target_format.lower() in ['jpg', 'jpeg'] and img.mode == 'RGBA':
                # Create white background
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[3])  # Use alpha channel as mask
                img = background
            
            # Save with the target format
            target_format = target_format.upper()
            if target_format == 'JPG':
                target_format = 'JPEG'
            
            # Save with maximum quality for JPEG
            if target_format == 'JPEG':
                img.save(output_path, format=target_format, quality=95)
            else:
                img.save(output_path, format=target_format)
    except Exception as e:
        raise Exception(f"Error converting image: {str(e)}")
