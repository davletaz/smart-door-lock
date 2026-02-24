# ------------------------------------------------------------
# This script captures live video from the webcam using OpenCV.
# It displays the camera feed and allows the user to:
#   - Press 'c' to capture the current frame and run face
#     recognition using face_rec.verify_user().
#   - Press 'q' to quit the application.
#
# Currently, liveness detection + face recognition
# # # # 
# TODO:
# Replace the manual face/liveness check (currently pressing 'c') 
# with automatic triggering based on PIR sensor input.
# ------------------------------------------------------------

import cv2
from vision import face_rec
from vision import liveness 

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height

print("Press 'c' to check face, 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip horizontally for mirror effect
    cv2.imshow("Camera", frame)

    key = cv2.waitKey(30) & 0xFF

    if key == ord('c'):
        # Face detection
        if not liveness.has_face(frame):
            print("No face detected")
            continue

        # Liveness check
        is_real = liveness.check_liveness(frame)
        if not is_real:
            print("Spoof detected - Access denied")
            continue

        print("Real face detected")

        # Face recognition
        is_match, name = face_rec.verify_user(frame)
        if is_match:
            print(f"ACCESS GRANTED: Welcome {name}!")
            # TODO: trigger door open mechanism via MQTT/Arduino
        else:
            print("ACCESS DENIED: Unknown face")
            # TODO: log the attempt, trigger alert

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()