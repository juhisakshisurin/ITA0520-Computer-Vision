import cv2
import numpy as np

# Get text from user
text = input("Enter the text: ")

# Create white image
image = np.ones((400, 700, 3), dtype=np.uint8) * 255

# Put text on image
cv2.putText(
    image,
    text,
    (50, 200),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.5,
    (0, 0, 255),
    3
)

# Display image
cv2.imshow("Text Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
