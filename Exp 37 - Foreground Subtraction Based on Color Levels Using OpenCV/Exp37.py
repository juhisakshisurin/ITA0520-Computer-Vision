import cv2
import numpy as np

# Read input image
image = cv2.imread("foreground_subtraction_input.png.jpeg")
if image is None:
    print("Image not found. Keep the image in the same folder as this Python file.")

else:
    # Convert BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Red color has two HSV ranges
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    red_mask = cv2.bitwise_or(mask1, mask2)

    # Remove the selected red foreground
    keep_mask = cv2.bitwise_not(red_mask)

    result = cv2.bitwise_and(
        image, image, mask=keep_mask
    )

    # Display original and processed images
    cv2.imshow("Original Image", image)
    cv2.imshow("Foreground Removed", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
