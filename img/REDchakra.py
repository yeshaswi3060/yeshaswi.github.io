import cv2
import numpy as np

# Load the images
img = cv2.imread('output_image.png')
img_to_add = cv2.imread('C:/Users/Lenovo/Documents/vastuu/img/chakra.png', cv2.IMREAD_UNCHANGED)

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
mask = cv2.bitwise_or(mask1, mask2)

# Find the contours of the red bounded box
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw the bounding box around the contour with maximum area
if len(contours) > 0:
    max_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(max_contour)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Calculate the middle point of the bounding box
    middle_point = (int(x + w/2), int(y + h/2))

    # Get the input degree from the user
    degree = int(input("Enter degree to rotate the image (clockwise): "))

    # Rotate the image to the specified degree
    rows, cols = img_to_add.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2, rows/2), degree, 1)
    img_to_add = cv2.warpAffine(img_to_add, M, (cols, rows))

    # Calculate the maximum scaling factor based on width and height
    scale_factor = min(w / cols, h / rows)
    new_size = (int(cols * scale_factor), int(rows * scale_factor))
    img_to_add = cv2.resize(img_to_add, new_size, interpolation=cv2.INTER_LINEAR)

    # Overlay the img_to_add on top of the img at the middle point
    overlay_width, overlay_height = img_to_add.shape[:2]
    start_x = max(0, middle_point[0] - overlay_width // 2)
    start_y = max(0, middle_point[1] - overlay_height // 2)
    end_x = min(start_x + overlay_width, img.shape[1])
    end_y = min(start_y + overlay_height, img.shape[0])
    overlay = img_to_add[:end_y - start_y, :end_x - start_x, :]
    alpha_mask = overlay[:, :, 3] / 255.0
    overlay = alpha_mask[:, :, np.newaxis] * overlay[:, :, :3]
    img[start_y:end_y, start_x:end_x, :] = (1.0 - alpha_mask[:, :, np.newaxis]) * img[start_y:end_y, start_x:end_x, :] + overlay

cv2.imwrite('result.png', img)
