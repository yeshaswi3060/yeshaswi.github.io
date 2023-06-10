import cv2
import numpy as np

# Load the image
img = cv2.imread('output_image.png')

# Convert the image to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds of the red color
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)

lower_red = np.array([170, 50, 50])
upper_red = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv, lower_red, upper_red)

# Combine the two masks
mask = mask1 + mask2

# Find the contours of the red bounded box
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw the bounding box around the contour with maximum area
if len(contours) > 0:
    max_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(max_contour)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Calculate the middle point of the bounding box
    middle_point = (int(x + w/2), int(y + h/2))

    # Draw a green dot on the middle point
    cv2.circle(img, middle_point, 5, (0, 255, 0), -1)

cv2.imwrite('output_image.png', img)
