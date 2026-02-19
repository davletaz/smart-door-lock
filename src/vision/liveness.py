
import cv2
from deepface import DeepFace

def check_liveness(frame):
    """
    Returns:
    True: If a real face is detected
    False: If a face fake is detected
    None: If no face is detected + Error
    """
    try:
        # Extract face with anti spoofing enabled
        face_result = DeepFace.extract_faces(
            img_path = frame,
            detector_backend = "opencv",
            enforce_detection = False,
            anti_spoofing = True
                )
        # Check Results
        if not face_result:
            return "No Face Detected"

        is_real = results[0].get("is_real", False)
        return is_real
        
    except Exception as e:
        print(f"Liveness Error: {e}")
        return None

