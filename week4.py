import cv2
import numpy as np

# Load the image
image = cv2.imread("Image-detection/demo/Resources/Photos/trees.jpeg")

blank = np.zeros(image.shape, dtype='uint8')


image_blur = cv2.medianBlur(image,25)

image_blur_gray = cv2.cvtColor(image_blur, cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(image_blur_gray, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,3,2)

cv2.imshow("threshold Image", thresh)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Initialize variables to count objects and total area
num_objects = 0
total_area = 0

areas = [cv2.contourArea(contour) for contour in contours]

sorted_areas = sorted(areas, reverse=True)

max_area = sorted_areas[1]

window = sorted_areas[0]

min_area_threshold = 0.5*max_area# Adjust this threshold according to your requirements

cv2.drawContours(blank, contours, -1, (255,255,255), 1)
cv2.imshow('Contours Drawn', blank)

# Loop through each contour
for contour in contours:
    # Calculate the area of the contour
    area = cv2.contourArea(contour)

    if area > min_area_threshold and area<window:
        num_objects += 1
        total_area += area

        # Find the bounding rectangle for the contour
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the number of objects and total area
cv2.putText(image, f"Number of objects: {num_objects}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
cv2.putText(image, f"Total area: {total_area}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

# Display the image with bounding boxes and information
cv2.imshow('final' , image)
cv2.waitKey(0)
cv2.destroyAllWindows()
