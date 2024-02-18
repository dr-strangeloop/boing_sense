import cv2 
import pyaudio

def get_cam_frame(cam_handle):
    """ Get a frame from the camera handle
    """
    pass


def get_aud_frame():
    """ Get a frame from the audio mic handle
    """
    pass

if __name__ == "__main__":
    # Step 1: Get a frame from the camera 
    frame_cam = get_cam_frame(cam_handle='')

    # Step 2: Get a frame from the audio mic
    frame_aud = get_aud_frame()

