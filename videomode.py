import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui

# Hand decetor
detector = HandDetector(detectionCon=0.9, maxHands=1)


# Capture video from camera
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # Detect hands
    hands, img = detector.findHands(frame)

    # Hand detection
    if hands:
        info = hands[0]
        # Number of fingers up
        fingersUp = detector.fingersUp(info)
        # Jump if index finger is up
        if fingersUp[1] == 1:
            print("Jump")
            cv2.putText(img, "Command: Jump", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            pyautogui.press('space')
        else:
            print("No command")
            cv2.putText(img, "Command: No command", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    cv2.imshow('frame', frame)
    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
