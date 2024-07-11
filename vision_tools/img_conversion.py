from PIL import Image
from pathlib import Path
import os

def convert_images(img_folder, from_ext, to_ext, remove_original=True):
    """
    Convert images from one format to another.

    Parameters:
    img_folder (str): The folder containing the images to convert.
    from_ext (str): The current extension of the images (e.g., 'jpeg', 'png').
    to_ext (str): The desired extension for the converted images (e.g., 'jpg', 'bmp').
    remove_original (bool): Whether to remove the original images after conversion. Default is True.
    
    Returns:
    None
    """
    img_folder = Path(img_folder)
    img_file_list = img_folder.glob(f"*.{from_ext}")
    
    for img_file in img_file_list:
        with Image.open(img_file) as img:
            output_file = img_file.with_suffix(f".{to_ext}")
            img.save(output_file, to_ext.upper())
            print(f"Converted {img_file} to {output_file}")

        if remove_original:
            os.remove(img_file)
    
    print("Conversion complete!")

def jpeg_to_jpg(img_folder):
    """Convert JPEG images to JPG."""
    convert_images(img_folder, "jpeg", "jpg")

def jpeg_to_png(img_folder):
    """Convert JPEG images to PNG."""
    convert_images(img_folder, "jpeg", "png")

def jpeg_to_bmp(img_folder):
    """Convert JPEG images to BMP."""
    convert_images(img_folder, "jpeg", "bmp")

def jpeg_to_webp(img_folder):
    """Convert JPEG images to WEBP."""
    convert_images(img_folder, "jpeg", "webp")

def jpeg_to_gif(img_folder):
    """Convert JPEG images to GIF."""
    convert_images(img_folder, "jpeg", "gif")

def jpeg_to_avif(img_folder):
    """Convert JPEG images to AVIF."""
    convert_images(img_folder, "jpeg", "avif")

def jpeg_to_svg(img_folder):
    """Convert JPEG images to SVG."""
    convert_images(img_folder, "jpeg", "svg")

def jpeg_to_pjp(img_folder):
    """Convert JPEG images to PJP."""
    convert_images(img_folder, "jpeg", "pjp")

def jpg_to_jpeg(img_folder):
    """Convert JPG images to JPEG."""
    convert_images(img_folder, "jpg", "jpeg")

def jpg_to_png(img_folder):
    """Convert JPG images to PNG."""
    convert_images(img_folder, "jpg", "png")

def jpg_to_bmp(img_folder):
    """Convert JPG images to BMP."""
    convert_images(img_folder, "jpg", "bmp")

def jpg_to_webp(img_folder):
    """Convert JPG images to WEBP."""
    convert_images(img_folder, "jpg", "webp")

def jpg_to_gif(img_folder):
    """Convert JPG images to GIF."""
    convert_images(img_folder, "jpg", "gif")

def jpg_to_avif(img_folder):
    """Convert JPG images to AVIF."""
    convert_images(img_folder, "jpg", "avif")

def jpg_to_svg(img_folder):
    """Convert JPG images to SVG."""
    convert_images(img_folder, "jpg", "svg")

def jpg_to_pjp(img_folder):
    """Convert JPG images to PJP."""
    convert_images(img_folder, "jpg", "pjp")

def png_to_jpeg(img_folder):
    """Convert PNG images to JPEG."""
    convert_images(img_folder, "png", "jpeg")

def png_to_jpg(img_folder):
    """Convert PNG images to JPG."""
    convert_images(img_folder, "png", "jpg")

def png_to_bmp(img_folder):
    """Convert PNG images to BMP."""
    convert_images(img_folder, "png", "bmp")

def png_to_webp(img_folder):
    """Convert PNG images to WEBP."""
    convert_images(img_folder, "png", "webp")

def png_to_gif(img_folder):
    """Convert PNG images to GIF."""
    convert_images(img_folder, "png", "gif")

def png_to_avif(img_folder):
    """Convert PNG images to AVIF."""
    convert_images(img_folder, "png", "avif")

def png_to_svg(img_folder):
    """Convert PNG images to SVG."""
    convert_images(img_folder, "png", "svg")

def png_to_pjp(img_folder):
    """Convert PNG images to PJP."""
    convert_images(img_folder, "png", "pjp")

def bmp_to_jpeg(img_folder):
    """Convert BMP images to JPEG."""
    convert_images(img_folder, "bmp", "jpeg")

def bmp_to_jpg(img_folder):
    """Convert BMP images to JPG."""
    convert_images(img_folder, "bmp", "jpg")

def bmp_to_png(img_folder):
    """Convert BMP images to PNG."""
    convert_images(img_folder, "bmp", "png")

def bmp_to_webp(img_folder):
    """Convert BMP images to WEBP."""
    convert_images(img_folder, "bmp", "webp")

def bmp_to_gif(img_folder):
    """Convert BMP images to GIF."""
    convert_images(img_folder, "bmp", "gif")

def bmp_to_avif(img_folder):
    """Convert BMP images to AVIF."""
    convert_images(img_folder, "bmp", "avif")

def bmp_to_svg(img_folder):
    """Convert BMP images to SVG."""
    convert_images(img_folder, "bmp", "svg")

def bmp_to_pjp(img_folder):
    """Convert BMP images to PJP."""
    convert_images(img_folder, "bmp", "pjp")

def webp_to_jpeg(img_folder):
    """Convert WEBP images to JPEG."""
    convert_images(img_folder, "webp", "jpeg")

def webp_to_jpg(img_folder):
    """Convert WEBP images to JPG."""
    convert_images(img_folder, "webp", "jpg")

def webp_to_png(img_folder):
    """Convert WEBP images to PNG."""
    convert_images(img_folder, "webp", "png")

def webp_to_bmp(img_folder):
    """Convert WEBP images to BMP."""
    convert_images(img_folder, "webp", "bmp")

def webp_to_gif(img_folder):
    """Convert WEBP images to GIF."""
    convert_images(img_folder, "webp", "gif")

def webp_to_avif(img_folder):
    """Convert WEBP images to AVIF."""
    convert_images(img_folder, "webp", "avif")

def webp_to_svg(img_folder):
    """Convert WEBP images to SVG."""
    convert_images(img_folder, "webp", "svg")

def webp_to_pjp(img_folder):
    """Convert WEBP images to PJP."""
    convert_images(img_folder, "webp", "pjp")

def gif_to_jpeg(img_folder):
    """Convert GIF images to JPEG."""
    convert_images(img_folder, "gif", "jpeg")

def gif_to_jpg(img_folder):
    """Convert GIF images to JPG."""
    convert_images(img_folder, "gif", "jpg")

def gif_to_png(img_folder):
    """Convert GIF images to PNG."""
    convert_images(img_folder, "gif", "png")

def gif_to_bmp(img_folder):
    """Convert GIF images to BMP."""
    convert_images(img_folder, "gif", "bmp")

def gif_to_webp(img_folder):
    """Convert GIF images to WEBP."""
    convert_images(img_folder, "gif", "webp")

def gif_to_avif(img_folder):
    """Convert GIF images to AVIF."""
    convert_images(img_folder, "gif", "avif")

def gif_to_svg(img_folder):
    """Convert GIF images to SVG."""
    convert_images(img_folder, "gif", "svg")

def gif_to_pjp(img_folder):
    """Convert GIF images to PJP."""
    convert_images(img_folder, "gif", "pjp")

def avif_to_jpeg(img_folder):
    """Convert AVIF images to JPEG."""
    convert_images(img_folder, "avif", "jpeg")

def avif_to_jpg(img_folder):
    """Convert AVIF images to JPG."""
    convert_images(img_folder, "avif", "jpg")

def avif_to_png(img_folder):
    """Convert AVIF images to PNG."""
    convert_images(img_folder, "avif", "png")

def avif_to_bmp(img_folder):
    """Convert AVIF images to BMP."""
    convert_images(img_folder, "avif", "bmp")

def avif_to_webp(img_folder):
    """Convert AVIF images to WEBP."""
    convert_images(img_folder, "avif", "webp")

def avif_to_gif(img_folder):
    """Convert AVIF images to GIF."""
    convert_images(img_folder, "avif", "gif")

def avif_to_svg(img_folder):
    """Convert AVIF images to SVG."""
    convert_images(img_folder, "avif", "svg")

def avif_to_pjp(img_folder):
    """Convert AVIF images to PJP."""
    convert_images(img_folder, "avif", "pjp")

def svg_to_jpeg(img_folder):
    """Convert SVG images to JPEG."""
    convert_images(img_folder, "svg", "jpeg")

def svg_to_jpg(img_folder):
    """Convert SVG images to JPG."""
    convert_images(img_folder, "svg", "jpg")

def svg_to_png(img_folder):
    """Convert SVG images to PNG."""
    convert_images(img_folder, "svg", "png")

def svg_to_bmp(img_folder):
    """Convert SVG images to BMP."""
    convert_images(img_folder, "svg", "bmp")

def svg_to_webp(img_folder):
    """Convert SVG images to WEBP."""
    convert_images(img_folder, "svg", "webp")

def svg_to_gif(img_folder):
    """Convert SVG images to GIF."""
    convert_images(img_folder, "svg", "gif")

def svg_to_avif(img_folder):
    """Convert SVG images to AVIF."""
    convert_images(img_folder, "svg", "avif")

def svg_to_pjp(img_folder):
    """Convert SVG images to PJP."""
    convert_images(img_folder, "svg", "pjp")

def pjp_to_jpeg(img_folder):
    """Convert PJP images to JPEG."""
    convert_images(img_folder, "pjp", "jpeg")

def pjp_to_jpg(img_folder):
    """Convert PJP images to JPG."""
    convert_images(img_folder, "pjp", "jpg")

def pjp_to_png(img_folder):
    """Convert PJP images to PNG."""
    convert_images(img_folder, "pjp", "png")

def pjp_to_bmp(img_folder):
    """Convert PJP images to BMP."""
    convert_images(img_folder, "pjp", "bmp")

def pjp_to_webp(img_folder):
    """Convert PJP images to WEBP."""
    convert_images(img_folder, "pjp", "webp")

def pjp_to_gif(img_folder):
    """Convert PJP images to GIF."""
    convert_images(img_folder, "pjp", "gif")

def pjp_to_avif(img_folder):
    """Convert PJP images to AVIF."""
    convert_images(img_folder, "pjp", "avif")

def pjp_to_svg(img_folder):
    """Convert PJP images to SVG."""
    convert_images(img_folder, "pjp", "svg")


