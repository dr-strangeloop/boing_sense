import cv2
import pyaudio
import imutils
import time
def get_cam_frame(cap):
        """Get a frame from the camera handle"""
        flag, data = cap.read()  # Read an image from the interface
        return data
# otherwise, grab a reference to the video file


def get_aud_frame(cap):
        """Get a frame from the audio mic handle"""
        sample_format = pyaudio.paInt16  # 16 bits per sample
        channels = 1  # Number of audio channels
        fs = 44100  # Sampling frequency
        chunk = 1024  # Record in chunks of 1024 samples
        stream = cap.open(
            format=sample_format,
            channels=channels,
            rate=fs,
            frames_per_buffer=chunk,
            input=True,
        )  # Read an audio frame from the interface
        data = stream.read(chunk)
        return data

def detect_ball_coordinates(frame, color):
        """Detect yellow rubber basketballs in the frame"""
        # Step 1: perform blur and change it to hsv color space
        frame_blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        frame_hsv = cv2.cvtColor(frame_blurred, cv2.COLOR_BGR2HSV)

        # Step 2: construct a mask for the color
        mask = cv2.inRange(frame_hsv, color["lower"], color["upper"])

        # Step 3: perform math operations to remove small blobs.
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        
        # Step 4: find ball contours and its center. Find contours in the mask and initialize the current (x, y) center of the ball
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        center = None
        
        # only proceed if at least one contour was found
        if len(cnts) > 0:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            ball_coords = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            # only proceed if the radius meets a minimum size
            if radius > 10:
                # draw the circle and centroid on the frame,
                # then update the list of tracked points
                cv2.circle(frame, (int(x), int(y)), int(radius),
                    (0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)

        # show the frame to our screen
            cv2.imshow("Frame", frame)
            cv2.waitKey(1000)
            
            
        return ball_coords


if __name__ == "__main__":

    # Step 1: Get a frame from the camera
    frame_counter = 0
    cap = cv2.VideoCapture(0)  # Create an interace to VideoCapture
    frame_cam = get_cam_frame(cap)

        # Step 2: Get a frame from the audio mic
    cap = pyaudio.PyAudio()  # Create an interface to PortAudio
    frame_aud = get_aud_frame(cap)

        # Step 3: Ball Detection and Tracking with CV2
    color = {}
    color["lower"] = (0, 78, 104)
    color["upper"] = (17, 230, 255)

    basketballs = detect_ball_coordinates(
        frame_cam, color
        )  # Detects balls in the camera frame
    
        # Step 4: Motion Analysis: Analyze the ball's motion specificallyfocusing on vertical movement, to identify bounces

        # Step 5: Audio Processing: Process audio signals to identify distinct sounds associated with ball bounces

    # Step 6: Synchronization: Sync the info from the camera and audio processing to correlate visual and auditory cues

    # Step 7: Bounce Detection: Develop an algorithm that detects when the ball makes contact with the surface based on both visual and audio cues

    # Step 8: counting Mechanism: Implement a counter that increments each time a bounce is successfully detected
    # import cv2
