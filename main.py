import cv2 
import pyaudio

def get_cam_frame():
    """ Get a frame from the camera handle
    """
    cap = cv2.VideoCapture(0) # Create an interace to VideoCapture
    flag, data = cap.read() # Read an image from the interface
    return data

def get_aud_frame():
    """ Get a frame from the audio mic handle
    """
    sample_format = pyaudio.paInt16 # 16 bits per sample
    channels = 1 # Number of audio channels
    fs = 44100 # Sampling frequency 
    chunk = 1024 # Record in chunks of 1024 samples
    cap = pyaudio.PyAudio() # Create an interface to PortAudio
    stream = cap.open(format=sample_format, channels=channels, rate=fs, frames_per_buffer=chunk, input=True) # Read an audio frame from the interface
    data = stream.read(chunk)
    return data

if __name__ == "__main__":
    
    # Step 1: Get a frame from the camera 
    frame_cam = get_cam_frame()
    
    # Step 2: Get a frame from the audio mic
    frame_aud = get_aud_frame()
    

