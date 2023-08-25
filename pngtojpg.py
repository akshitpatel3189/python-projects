import os
from PIL import Image

def convert_png_to_jpg(png_path, jpg_path):
    image = Image.open(png_path)
    image = image.convert("RGB")  # Convert RGBA image to RGB
    image.save(jpg_path, "JPEG")

# Directory containing the PNG images
png_directory = "E:/OneDrive - Marine Thinking/Work/Work 9/FishingBoat"

# Directory to save the converted JPG images
jpg_directory = "E:/OneDrive - Marine Thinking/Work/Work 9/video"

# Create the output directory if it doesn't exist
if not os.path.exists(jpg_directory):
    os.makedirs(jpg_directory)

# Convert each PNG image to JPG
for filename in os.listdir(png_directory):
    if filename.endswith(".png"):
        png_path = os.path.join(png_directory, filename)
        jpg_filename = os.path.splitext(filename)[0] + ".jpg"
        jpg_path = os.path.join(jpg_directory, jpg_filename)
        convert_png_to_jpg(png_path, jpg_path)
