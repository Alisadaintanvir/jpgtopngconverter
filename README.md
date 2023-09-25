# Image Converter Script
This is a simple Python script for converting images from one format to another in bulk. It takes a folder containing input images and an output folder as command-line arguments and converts all the images in the input folder to PNG format, saving them in the output folder.

## Prerequisites
- Python 3.x
- Pillow (PIL) library (pip install Pillow)
  
## Usage
1. Clone the repository to your local machine:
`git clone https://github.com/Alisadaintanvir/image-converter.git`

2. Navigate to the project directory:
`cd image-converter`

3. Run the script by providing the input folder and output folder as arguments:
`python image_converter.py input_folder output_folder`

Replace image_converter.py with the name of your script, input_folder with the path to the folder containing input images, and output_folder with the path to the folder where the converted images will be saved.

#### For example:
`python image_converter.py input_images/ output_images/`

4. The script will convert all the images in the input_folder to PNG format and save them in the output_folder.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Pillow (PIL) - The Python Imaging Library used for image processing.
Feel free to modify and enhance the script as needed for your specific use case.
