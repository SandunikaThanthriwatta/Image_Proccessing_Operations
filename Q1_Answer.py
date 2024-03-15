#Thanthriwatta T.P.S.
#EG/2019/3757

import cv2

# Function to reduce the number of intensity levels in the image
def intensity_levels_reduction(img, levels):
    # Calculate the factor to reduce intensity levels
    factorNum = 256 // levels
    # Apply intensity reduction formula
    image = (img // factorNum) * factorNum
    return image

# Path to the input image
ImagePath = "ImagePath/Image.jpeg"
# Read the input image in grayscale
img = cv2.imread(ImagePath, cv2.IMREAD_GRAYSCALE)

# Prompt the user to input the number of intensity levels
LevelsNumber = int(input("Enter the number of intensity levels: "))

# Checking whether the user-given number of intensity levels is a power of 2 or not
if LevelsNumber <= 0 or not (LevelsNumber & (LevelsNumber - 1) == 0):
    print("Number should be a power of 2!")
    exit()

# Reduce the number of intensity levels using the function
resultImage = intensity_levels_reduction(img, LevelsNumber)

# Save the result image and display it
cv2.imwrite('ResultsPath/Q1/Img_{}.jpg'.format(LevelsNumber), resultImage)
cv2.imshow('Reduced Image', resultImage)

# Wait for any key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
