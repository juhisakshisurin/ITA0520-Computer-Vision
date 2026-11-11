import cv2
import numpy as np

# Get image size from user
size = int(input("Enter image size: "))

# Create white image
image = np.ones((size, size, 3), dtype=np.uint8) * 255

# Box size = 1/10th of image size
box = size // 10

# Top-left = Black
image[0:box, 0:box] = [0, 0, 0]

# Top-right = Blue
image[0:box, size-box:size] = [255, 0, 0]

# Bottom-left = Green
image[size-box:size, 0:box] = [0, 255, 0]

# Bottom-right = Red
image[size-box:size, size-box:size] = [0, 0, 255]

# Display image
cv2.imshow("Four Colored Boxes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
