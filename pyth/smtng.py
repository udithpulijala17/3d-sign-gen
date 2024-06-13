import cv2
import mediapipe as mp
import numpy as np
import time

start_time = time.time()

mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=1
)

def main():
    draw = mp.solutions.drawing_utils
    cap = cv2.VideoCapture(0)
    
    try:
        while cap.isOpened():
            curr_time = time.time() - start_time
            
            if int(curr_time) % 1.0 == 0:  # Check if a second has elapsed
                print("Time elapsed:", round(curr_time, 2), "seconds")

            success, img = cap.read()
            if not success:
                break
            img = cv2.flip(img, 1)
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(imgRGB)

            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    draw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            cv2.imshow("Image", img)
            if cv2.waitKey(1) & 0xFF == ord('q') or curr_time > 10:
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
        
main()