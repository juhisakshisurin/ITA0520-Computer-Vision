import cv2
import numpy as np

# Read input image
image = cv2.imread(r"C:\Users\ashis\OneDrive\Desktop\Experiment36\background_subtraction_input.png.jpeg")

if image is None:
    print("Image not found. Keep the image in the same folder as this Python file.")

else:
    # Convert BGR image to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Green background range
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])

    # Detect green background
    background_mask = cv2.inRange(
        hsv, lower_green, upper_green
    )

    # Keep everything except green background
    foreground_mask = cv2.bitwise_not(background_mask)

    result = cv2.bitwise_and(
        image, image, mask=foreground_mask
    )

    # Display original and processed images
    cv2.imshow("Original Image", image)
    cv2.imshow("Background Removed", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
