
import cv2

# Open input video
cap = cv2.VideoCapture("reverse_slow_input.mp4")

if not cap.isOpened():
    print("Video not found. Keep the video in the same folder as this Python file.")

else:
    frames = []

    # Read all frames
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()

    if len(frames) == 0 or fps <= 0:
        print("No valid video frames found.")

    else:
        # Reverse frame order
        frames.reverse()

        height, width = frames[0].shape[:2]

        # Half FPS = slow motion
        slow_fps = fps / 2

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        output = cv2.VideoWriter(
            "reverse_slow_motion.mp4",
            fourcc,
            slow_fps,
            (width, height)
        )

        for frame in frames:
            output.write(frame)

        output.release()

        print("Reverse slow-motion video created successfully.")
        print("Output file: reverse_slow_motion.mp4")
