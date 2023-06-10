import cv2
import numpy as np

# Load the image
image = cv2.imread('C:/Users/Lenovo/Documents/vastuu/img.jpg')


# Convert the image to grayscale 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a threshold to the image to create a binary mask
ret, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Find the contours of the black pixels
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize variables to keep track of the biggest rectangle found
max_area = 0
max_x = 0
max_y = 0
max_w = 0
max_h = 0

# Iterate through each contour and find the biggest rectangle
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    area = w * h

    if area > max_area:
        max_area = area
        max_x = x
        max_y = y
        max_w = w
        max_h = h

# Draw a rectangle around the biggest rectangle
cv2.rectangle(image, (max_x, max_y), (max_x + max_w, max_y + max_h), (0, 255, 0), 2)

# Output the coordinates of the center of the rectangle in x, y, z format
center_x = max_x + max_w/2
center_y = max_y + max_h/2
center_z = 0
print(f"x: {center_x}, y: {center_y}, z: {center_z}")

# Crop the image to the biggest rectangle
crop_img = image[max_y:max_y+max_h, max_x:max_x+max_w]

# Save the cropped image
cv2.imwrite('output_image.png', crop_img)
