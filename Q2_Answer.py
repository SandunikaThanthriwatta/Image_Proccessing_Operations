# Thanthriwatta T.P.S.
# EG/2019/3757

import cv2
import numpy as np

# Function to apply an average filter to the image
def average_filter(img, Size):
    # Create a kernel with ones of size (Size x Size)
    kernel = np.ones((Size, Size), np.float32) / (Size * Size)
    # Apply the filter using convolution
    image = cv2.filter2D(img, -1, kernel)
    return image

# Path to the input image
ImagePath = "ImagePath/Image.jpeg"
# Read the input image in grayscale
image = cv2.imread(ImagePath, cv2.IMREAD_GRAYSCALE)

# Apply 3x3 filter
filter_3x3 = average_filter(image, 3)
# Apply 10x10 filter
filter_10x10 = average_filter(image, 10)
# Apply 20x20 filter
filter_20x20 = average_filter(image, 20)

# Saving the filtered images
cv2.imwrite('ResultsPath/Q2/Img_3x3.jpg', filter_3x3)
cv2.imwrite('ResultsPath/Q2/Img_10x10.jpg', filter_10x10)
cv2.imwrite('ResultsPath/Q2/Img_20x20.jpg', filter_20x20)

# Displaying the filtered images
cv2.imshow("3x3 Filter", filter_3x3)
cv2.imshow("10x10 Filter", filter_10x10)
cv2.imshow("20x20 Filter", filter_20x20)

# Wait for any key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
