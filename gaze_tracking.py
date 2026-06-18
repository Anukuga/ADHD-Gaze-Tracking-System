import cv2
import mediapipe as mp
import csv
import os
import time

# Open webcam
cap = cv2.VideoCapture(0)

# MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True
)

# Iris landmarks
LEFT_IRIS = [474, 475, 476, 477]
RIGHT_IRIS = [469, 470, 471, 472]

# CSV setup
csv_file = "gaze_data.csv"

if not os.path.exists(csv_file):

    with open(csv_file, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "timestamp",
            "frame_number",
            "left_eye_x",
            "left_eye_y",
            "right_eye_x",
            "right_eye_y",
            "gaze_direction"
        ])

frame_number = 0


while True:

    frame_number += 1

    success, frame = cap.read()

    if not success:
        break

    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    gaze_direction = "Center"

    left_eye_x = 0
    left_eye_y = 0

    right_eye_x = 0
    right_eye_y = 0

    if results.multi_face_landmarks:

        for face_landmarks in results.multi_face_landmarks:

            for idx in LEFT_IRIS:

                point = face_landmarks.landmark[idx]

                x = int(point.x * w)
                y = int(point.y * h)

                left_eye_x = x
                left_eye_y = y

                cv2.circle(frame, (x, y), 2, (0,255,0), -1)


            for idx in RIGHT_IRIS:

                point = face_landmarks.landmark[idx]

                x = int(point.x * w)
                y = int(point.y * h)

                right_eye_x = x
                right_eye_y = y

                cv2.circle(frame, (x, y), 2, (0,255,0), -1)


            iris = face_landmarks.landmark[468]

            x = iris.x

            if x < 0.45:

                gaze_direction = "Left"

            elif x > 0.55:

                gaze_direction = "Right"

            else:

                gaze_direction = "Center"


    timestamp = time.time()

    with open(csv_file, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            timestamp,
            frame_number,
            left_eye_x,
            left_eye_y,
            right_eye_x,
            right_eye_y,
            gaze_direction
        ])


    cv2.putText(
        frame,
        f"Gaze: {gaze_direction}",
        (30,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.imshow("ADHD Gaze Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):

        break


cap.release()

cv2.destroyAllWindows()