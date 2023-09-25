import sys
import os
from PIL import Image

# Grab the first and the second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exist, if not then create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{filename}")
    clear_format = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clear_format}.png', 'png')




