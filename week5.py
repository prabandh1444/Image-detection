# import packages
import cv2
import numpy as np

# threshold values
threshold = 14

# Read image in grayscale

image = cv2.imread('Image-detection/demo/Resources/Photos/Sample Image.jpg', cv2.IMREAD_GRAYSCALE)

#  Convert into black and white image 
_, binary_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY_INV)

# find total pixels in the image
total_pixels = image.shape[0] * image.shape[1]

# find number of black pixels
pore_pixels = cv2.countNonZero(binary_image)

# Calculate porosity_percentage = (black pixels)/(total pixels)* 100
porosity_percentage = (pore_pixels / total_pixels) * 100

# print porosity upto 2 decimals
print(f"Porosity Percentage: {porosity_percentage:.2f}%")

# wait and destroy all windows upon keyboard input
cv2.waitKey(0)
cv2.destroyAllWindows()
