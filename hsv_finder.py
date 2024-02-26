import cv2
import numpy as np

def nothing(x):
    pass

# Create a window named 'image'
cv2.namedWindow('image')

# Create a VideoCapture object to capture video from the default camera (index 0)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Read a single frame from the camera
ret, img = cap.read()

# Check if the frame was successfully read
if not ret:
    print("Error: Could not read frame.")
    exit()

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Create trackbars for adjusting HSV values
# Rest of the script remains the same...


# Create trackbars for adjusting HSV values
cv2.createTrackbar('Hue Low','image',0,179,nothing)
cv2.createTrackbar('Hue High','image',0,179,nothing)
cv2.createTrackbar('Saturation Low','image',0,255,nothing)
cv2.createTrackbar('Saturation High','image',0,255,nothing)
cv2.createTrackbar('Value Low','image',0,255,nothing)
cv2.createTrackbar('Value High','image',0,255,nothing)

# Set initial trackbar positions
cv2.setTrackbarPos('Hue Low','image',0)
cv2.setTrackbarPos('Hue High','image',179)
cv2.setTrackbarPos('Saturation Low','image',0)
cv2.setTrackbarPos('Saturation High','image',255)
cv2.setTrackbarPos('Value Low','image',0)
cv2.setTrackbarPos('Value High','image',255)

while True:
    # Get current positions of all trackbars
    h_low = cv2.getTrackbarPos('Hue Low','image')
    h_high = cv2.getTrackbarPos('Hue High','image')
    s_low = cv2.getTrackbarPos('Saturation Low','image')
    s_high = cv2.getTrackbarPos('Saturation High','image')
    v_low = cv2.getTrackbarPos('Value Low','image')
    v_high = cv2.getTrackbarPos('Value High','image')

    # Threshold the HSV image to get only orange colors
    mask = cv2.inRange(hsv, (h_low, s_low, v_low), (h_high, s_high, v_high))
    res = cv2.bitwise_and(img, img, mask=mask)

    # Display the original image and the masked image
    cv2.imshow('image', np.hstack([img, res]))

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
