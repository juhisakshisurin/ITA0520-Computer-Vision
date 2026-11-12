import cv2
import pytesseract

# Tesseract installation path in Windows
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Open video
cap = cv2.VideoCapture("text_video_input.mp4")

if not cap.isOpened():
    print("Video not found. Keep the video in the same folder as this Python file.")

else:
    frame_number = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Read text from one frame every 20 frames
        if frame_number % 20 == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            text = pytesseract.image_to_string(gray).strip()

            if text:
                print("Detected Text:", text)

        frame_number += 1

    cap.release()
    print("Text extraction completed.")
