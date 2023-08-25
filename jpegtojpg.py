import os
from PIL import Image

def convert_jpeg_to_jpg(jpeg_path, jpg_path):
    image = Image.open(jpeg_path)
    image.save(jpg_path, "JPEG")

# Directory containing the JPEG images
jpeg_directory = "E:/OneDrive - Marine Thinking/Work/Work 8/Researchshipraw"

# Directory to save the converted JPG images
jpg_directory = "E:/OneDrive - Marine Thinking/Work/Work 8/video"

# Create the output directory if it doesn't exist
if not os.path.exists(jpg_directory):
    os.makedirs(jpg_directory)

# Convert each JPEG image to JPG
for filename in os.listdir(jpeg_directory):
    if filename.endswith(".jpeg"):
        jpeg_path = os.path.join(jpeg_directory, filename)
        jpg_filename = os.path.splitext(filename)[0] + ".jpg"
        jpg_path = os.path.join(jpg_directory, jpg_filename)
        convert_jpeg_to_jpg(jpeg_path, jpg_path)
