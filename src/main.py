# ------------------------------------------------------------
# This script captures live video from the webcam using OpenCV.
# It displays the camera feed and allows the user to:
#   - Press 'c' to capture the current frame and run face
#     recognition using face_rec.verify_user().
#   - Press 'q' to quit the application.
#
# Currently, it performs only face recognition.
# In the final system, this script will act as the main
# orchestrator, coordinating both face recognition and
# liveness detection before granting access.
# # # # 
# TODO:
# 1. Add liveness detection to ensure the system recognizes a real person, 
#    not just a photo.
# 2. Replace the manual face/liveness check (currently pressing 'c') 
#    with automatic triggering based on PIR sensor input.
# ------------------------------------------------------------

import cv2
from vision import face_rec

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

print("Press 'c' to check face, 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)    

    cv2.imshow("Camera", frame)
    

    key = cv2.waitKey(30) & 0xFF
    if key == ord('c'):
        is_match, name = face_rec.verify_user(frame)
        print(is_match, name)
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
