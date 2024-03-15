# Thanthriwatta T.P.S.
# EG/2019/3757

import cv2
import numpy as np

# Function to perform block averaging on the image
def block_average_func(img, size):
    # Get the height and width of the image
    height, width = img.shape[:2]
    # Calculate the number of blocks in width and height based on the given size
    WidthBlocks = width // size
    HeightBlocks = height // size

    # Reshape the image into blocks
    blocks = img[:HeightBlocks * size, :WidthBlocks * size].reshape(HeightBlocks, size, WidthBlocks, size, -1)

    # Calculate the average value of each block
    averagValue = np.mean(blocks, axis=(1, 3)).astype(np.uint8)

    # Repeat the average values to reconstruct the image
    result = np.repeat(np.repeat(averagValue, size, axis=0), size, axis=1)
    return result

# Path to the input image
ImagePath = "ImagePath/Image.jpeg"
# Read the input image in grayscale
image = cv2.imread(ImagePath, cv2.IMREAD_GRAYSCALE)

# Apply block averaging with different block sizes
image_3x3 = block_average_func(image, 3)
image_5x5 = block_average_func(image, 5)
image_7x7 = block_average_func(image, 7)

# Saving the resulting images
cv2.imwrite('ResultsPath/Q4/Img_3x3.jpg', image_3x3)
cv2.imwrite('ResultsPath/Q4/Img_5x5.jpg', image_5x5)
cv2.imwrite('ResultsPath/Q4/Img_7x7.jpg', image_7x7)

# Displaying the resulting images
cv2.imshow('3x3 image.jpg', image_3x3)
cv2.imshow('5x5 image.jpg', image_5x5)
cv2.imshow('7x7 image.jpg', image_7x7)

# Wait for any key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
