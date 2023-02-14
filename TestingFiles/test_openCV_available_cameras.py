import cv2

def get_available_camera(number_of_cameras):
    for i in range(number_of_cameras):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"Camera {i}: available")
            cap.release()
            return i
        else:
            print(f"Camera {i}: not available")
            cap.release()
    return -1

camera_index = 0
number_of_cameras = 10  # set a maximum number of cameras to check
camera_index = get_available_camera(number_of_cameras)

if camera_index != -1:
    cap = cv2.VideoCapture(camera_index)
    while True:
        ret, frame = cap.read()
        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
else:
    print("No available cameras.")
