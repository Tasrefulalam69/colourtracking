import cv2
import numpy as np

# Open webcam
cap = cv2.VideoCapture(0)

print("Object Tracking chalu hocche... Bondho korte 'q' press korun.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip image horizontally
    frame = cv2.flip(frame, 1)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range for blue color object
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([140, 255, 255])

    # Threshold the HSV image
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Target Object", (x, y - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Show window
    cv2.imshow("Object Tracking - Project 1", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()