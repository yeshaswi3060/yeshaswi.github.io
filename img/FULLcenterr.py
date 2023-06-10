from PIL import Image
import math

# Load the two images
background = Image.open('output_image.png')
foreground = Image.open('C:/Users/Lenovo/Documents/vastuu/img/chakra.png').convert('RGBA')


# Get the dimensions of the images
background_width, background_height = background.size
foreground_width, foreground_height = foreground.size

foreground_width = int(foreground_width * 2.5)
foreground_height = int(foreground_height * 2.5)
foreground = foreground.resize((foreground_width, foreground_height))


# Calculate the center coordinates of the background image
center_x = int(background_width / 2)
center_y = int(background_height / 2)

# Calculate the top-left corner coordinates of the foreground image
top_left_x = center_x - int(foreground_width / 2)
top_left_y = center_y - int(foreground_height / 2)

# Ask user for the angle of rotation in degrees
angle_degrees = int(input("Enter the digree how much you want to rotate: "))

# Convert the angle from degrees to radians
angle_radians = math.radians(angle_degrees)

# Rotate the foreground image by the specified angle
foreground_rotated = foreground.rotate(angle_degrees, resample=Image.BICUBIC, expand=True)

# Get the dimensions of the rotated foreground image
foreground_rotated_width, foreground_rotated_height = foreground_rotated.size

# Calculate the top-left corner coordinates of the rotated foreground image
top_left_x_rotated = center_x - int(foreground_rotated_width / 2)
top_left_y_rotated = center_y - int(foreground_rotated_height / 2)

# Create a new image with the same size as the background image and a transparent background
new_image = Image.new('RGBA', (background_width, background_height), (0, 0, 0, 0))

# Paste the background and rotated foreground images onto the new image
new_image.paste(background, (0, 0))
new_image.paste(foreground_rotated, (top_left_x_rotated, top_left_y_rotated), foreground_rotated)

# Save the result
new_image.save('result.png')
