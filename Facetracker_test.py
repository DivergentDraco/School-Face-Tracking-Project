import cv2
import mediapipe as mp
import pyautogui
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
        
        #Assign sensitivity
            sensitivity_x = 3  
            sensitivity_y = 9
        #
            if id == 1:
                screen_x = max(1, min(screen_w - 2, int(screen_w * (landmark.x * sensitivity_x - (sensitivity_x - 1) / 2))))
                screen_y = max(1, min(screen_h - 2, int(screen_h * (landmark.y * sensitivity_y - (sensitivity_y - 1) / 2))))
        #Makes the cursor move in regards to screen_x and screen_y
                pyautogui.moveTo(screen_x, screen_y, duration=0.02)

        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))

        if (left[0].y - left[1].y) < 0.004:
            pyautogui.click()
            cv2.waitKey(500)  # More stable than sleep()
    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)
    #Print status of position and landmark
    
    print(f"Raw landmark: {landmark.x}, {landmark.y}")
    print(f"Screen Position: {screen_x}, {screen_y}")
    
    # Exit when Esc (27) is pressed
    key = cv2.waitKey(1) & 0xFF
    '''
    if key == 27:  # ESC key
        print("Esc pressed, exiting...")
        break
    else:
        print(f"Key pressed: {key}")  # Debugging line
    print(f"Pressed key code: {key}")
    '''
# Release camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()