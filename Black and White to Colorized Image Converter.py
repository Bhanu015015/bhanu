# Install required libraries
!pip install opencv-python matplotlib

# Import required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Directly specify the image name (replace 'your_image.jpg' with the actual name of your image)
image_path = '/content/your_image.jpg'  # Replace with your image file name

# Read the black-and-white image
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Convert grayscale to color by applying a simple colormap
colorized_image = cv2.applyColorMap(gray_image, cv2.COLORMAP_JET)

# Display the original black-and-white and colorized image side by side
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Original black-and-white image
axes[0].imshow(gray_image, cmap='gray')
axes[0].set_title('Original Black & White Image')
axes[0].axis('off')

# Colorized image
axes[1].imshow(colorized_image)
axes[1].set_title('Colorized Image')
axes[1].axis('off')

plt.show()