
import cv2
from deepface import DeepFace

# Load the pre-trained face detector (Standard OpenCV)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def has_face(frame):
    """
    Returns TRUE if a face is detected in the frame.
    Returns FALSE if empty.
    """
    # 1. Convert to Grayscale (Faster detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 2. Detect Faces
    # scaleFactor=1.1, minNeighbors=5 are standard settings
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    # 3. Check if list is empty
    if len(faces) > 0:
        return True # Face found!
    
    return False # No face

def check_liveness(frame):
    """
    Returns:
    True: If a real face is detected
    False: If a face fake is detected
    None: If no face is detected + Error
    """
    try:
        # Extract face with anti fake enabled
        face_objs = DeepFace.extract_faces(
            img_path = frame,
            detector_backend = "opencv",
            enforce_detection = True,
            anti_fake = True
                )
        # Check results
        for face in face_objs:
            if face["is_real"] == True:
                return True
        return False 
    except ValueError:
        return None
    except Exception as e:
        print(f"Liveness Error")
        return None
