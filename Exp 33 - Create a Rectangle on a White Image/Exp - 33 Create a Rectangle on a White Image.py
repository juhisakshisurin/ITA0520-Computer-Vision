import cv2
import numpy as np

# Get image size from user
size = int(input("Enter image size: "))

# Create white image
image = np.ones((size, size, 3), dtype=np.uint8) * 255

# Draw rectangle
cv2.rectangle(
    image,
    (100, 100),
    (size-100, size-150),
    (0, 0, 255),
    5
)

# Display image
cv2.imshow("Rectangle Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
