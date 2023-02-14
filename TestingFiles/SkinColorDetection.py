import cv2
import numpy as np

def detect_skin(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define a range of skin color in HSV
    lower = np.array([0, 20, 70], dtype=np.uint8)
    upper = np.array([20, 255, 255], dtype=np.uint8)

    # Threshold the HSV image to get only skin colors
    mask = cv2.inRange(hsv, lower, upper)

    # Blur the mask to remove noise
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    return mask

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("Webcam", frame)

    mask = detect_skin(frame)
    cv2.imshow("Skin color mask", mask)

    # Add your hand or head detection code here

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
