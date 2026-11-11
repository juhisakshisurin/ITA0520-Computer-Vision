import cv2
import numpy as np

# Get image size from user
size = int(input("Enter image size: "))

# Create white image
image = np.ones((size, size, 3), dtype=np.uint8) * 255

# Find center and radius
center = (size // 2, size // 2)
radius = size // 4

# Draw circle
cv2.circle(
    image,
    center,
    radius,
    (255, 0, 0),
    5
)

# Display image
cv2.imshow("Circle Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
