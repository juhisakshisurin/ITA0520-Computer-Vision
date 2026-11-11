import cv2

# Read image from Desktop
image = cv2.imread(r"C:\Users\ashis\OneDrive\Desktop\input\input.jpg")

# Check image
if image is None:
    print("Image not found. Please check the path and file name.")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply threshold segmentation
    ret, segmented = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Display output
    cv2.imshow("Original Image", image)
    cv2.imshow("Segmented Image", segmented)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
