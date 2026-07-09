import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import cv2
import av
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from detection.face_detection import detect_faces, get_landmarks
from detection.blink_detection import is_blinking
from detection.yawning_detection import is_yawning

st.title("Driver Drowsiness Detection â€” Live Demo")
st.write("Allow camera access below. Detects closed eyes and yawning in real time.")
st.info("Note: this web demo shows visual alerts only. The full local version (see GitHub) also plays an audio alarm.")

class DrowsinessProcessor(VideoProcessorBase):
    def __init__(self):
        self.sleep_counter = 0
        self.drowsy_counter = 0
        self.yawn_counter = 0

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        img = cv2.resize(img, (640, 480))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        status = ""
        color = (0, 255, 0)

        faces = detect_faces(gray)
        for face in faces:
            landmarks = get_landmarks(gray, face)
            left_blink, right_blink = is_blinking(landmarks)

            if left_blink == 0 and right_blink == 0:
                self.sleep_counter += 1
                self.drowsy_counter = 0
                if self.sleep_counter >= 6:
                    status = "SLEEPING !!!"
                    color = (0, 0, 255)
            elif left_blink == 1 and right_blink == 1:
                self.sleep_counter = 0
                self.drowsy_counter += 1
                if self.drowsy_counter >= 6:
                    status = "Drowsy..."
                    color = (0, 165, 255)
            else:
                status = "Active :)"
                color = (0, 255, 0)
                self.sleep_counter = 0
                self.drowsy_counter = 0

            if is_yawning(landmarks):
                self.yawn_counter += 1
                status = "Yawning!"
                color = (0, 255, 255)
            else:
                self.yawn_counter = 0

            cv2.putText(img, status, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

        return av.VideoFrame.from_ndarray(img, format="bgr24")

RTC_CONFIGURATION = {
    "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
}

webrtc_streamer(
    key="drowsiness-detection",
    video_processor_factory=DrowsinessProcessor,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False}, 
)
