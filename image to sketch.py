# Install necessary libraries
!pip install opencv-python matplotlib

# Import required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

# Upload the image
uploaded = files.upload()

# Load the image (replace 'your_image_path_here.jpg' with the name of your uploaded image)
image_path = list(uploaded.keys())[0]
img = cv2.imread(image_path)

# Convert image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
invert_img = cv2.bitwise_not(gray_img)

# Apply Gaussian blur
blurred_img = cv2.GaussianBlur(invert_img, (111, 111), 0)

# Invert the blurred image
inverted_blurred_img = cv2.bitwise_not(blurred_img)

# Sketch image (blended)
sketch = cv2.divide(gray_img, inverted_blurred_img, scale=256.0)

# Save the sketch to a file
sketch_path = "/content/sketched_image.jpg"
cv2.imwrite(sketch_path, sketch)

# Display the image
plt.imshow(sketch, cmap='gray')
plt.axis('off')
plt.show()

# Provide the option to download the sketch image
files.download(sketch_path)