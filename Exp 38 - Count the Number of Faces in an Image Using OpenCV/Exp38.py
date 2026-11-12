import cv2
from mtcnn import MTCNN

# Read input image
image = cv2.imread("face_count_input_3faces.jpg.jpeg")

if image is None:
    print("Image not found. Keep the image in the same folder as this Python file.")

else:
    # OpenCV reads BGR; MTCNN expects RGB
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Create face detector
    detector = MTCNN()

    # Detect faces
    faces = detector.detect_faces(rgb)

    result = image.copy()

    # Draw a rectangle around every detected face
    for face in faces:
        x, y, w, h = face["box"]
        x = max(0, x)
        y = max(0, y)
        cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Count faces
    face_count = len(faces)
    print("Number of faces detected:", face_count)

    # Display
    cv2.imshow("Original Image", image)
    cv2.imshow("Faces Detected", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
