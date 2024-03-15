# Thanthriwatta T.P.S.
# EG/2019/3757

from PIL import Image
import numpy as np
import cv2

# Path to the input image
ImagePath = "ImagePath/Image.jpeg"
# Open the image using PIL
image = Image.open(ImagePath)

# Rotate the image by 45 degrees (expanding to avoid cropping)
Image_45 = image.rotate(45, expand=True)
# Rotate the image by 90 degrees (expanding to avoid cropping)
Image_90 = image.rotate(90, expand=True)

# Convert PIL Image to NumPy array for OpenCV
image_45_np = np.array(Image_45)
image_90
