import kivy
from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
import mediapipe as mp

class CameraApp(App):
    def build(self):
        # Initialize OpenCV camera and MediaPipe solutions
        self.capture = cv2.VideoCapture(1)  # Access webcam
        self.face_mesh = mp.solutions.face_mesh.FaceMesh()
        self.hands = mp.solutions.hands.Hands()
        self.pose = mp.solutions.pose.Pose()

        self.img = Image()  # Kivy widget to display the camera feed
        Clock.schedule_interval(self.update, 1.0/30.0)  # 30 FPS
        return self.img

    def update(self, dt):
    # Read frame from OpenCV
        ret, frame = self.capture.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
            h, w, c = frame.shape
    
            # Face detection with light purple-colored circles and connecting lines
            face_results = self.face_mesh.process(frame_rgb)
        if face_results.multi_face_landmarks:
            for face_landmarks in face_results.multi_face_landmarks:
                for id, lm in enumerate(face_landmarks.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    # Cyan color: (255, 255, 0) in OpenCV BGR format
                    cv2.circle(frame, (cx, cy), 2, (255, 255, 0), -1)
    
            # Hand detection with light purple-colored circles and connecting lines
            hand_results = self.hands.process(frame_rgb)
            if hand_results.multi_hand_landmarks:
                for hand_landmarks in hand_results.multi_hand_landmarks:
                    prev_point = None  # Keep track of the previous point to draw lines
                    for id, lm in enumerate(hand_landmarks.landmark):
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        # Light purple color: (200, 162, 200) for hands as well
                        cv2.circle(frame, (cx, cy), 5, (255, 255, 0), -1)
    
                        if prev_point:
                            cv2.line(frame, prev_point, (cx, cy), (255, 255, 0), 2)
                        prev_point = (cx, cy)
    
            # Pose detection with light pink-colored connections and circles
            pose_results = self.pose.process(frame_rgb)
            if pose_results.pose_landmarks:
                landmarks = pose_results.pose_landmarks.landmark
    
                # Define connections between landmarks
                body_connections = [
                    (mp.solutions.pose.PoseLandmark.LEFT_SHOULDER, mp.solutions.pose.PoseLandmark.LEFT_ELBOW),
                    (mp.solutions.pose.PoseLandmark.LEFT_ELBOW, mp.solutions.pose.PoseLandmark.LEFT_WRIST),
                    (mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER, mp.solutions.pose.PoseLandmark.RIGHT_ELBOW),
                    (mp.solutions.pose.PoseLandmark.RIGHT_ELBOW, mp.solutions.pose.PoseLandmark.RIGHT_WRIST),
                    (mp.solutions.pose.PoseLandmark.LEFT_SHOULDER, mp.solutions.pose.PoseLandmark.LEFT_HIP),
                    (mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER, mp.solutions.pose.PoseLandmark.RIGHT_HIP),
                    (mp.solutions.pose.PoseLandmark.LEFT_HIP, mp.solutions.pose.PoseLandmark.LEFT_KNEE),
                    (mp.solutions.pose.PoseLandmark.LEFT_KNEE, mp.solutions.pose.PoseLandmark.LEFT_ANKLE),
                    (mp.solutions.pose.PoseLandmark.RIGHT_HIP, mp.solutions.pose.PoseLandmark.RIGHT_KNEE),
                    (mp.solutions.pose.PoseLandmark.RIGHT_KNEE, mp.solutions.pose.PoseLandmark.RIGHT_ANKLE),
                    (mp.solutions.pose.PoseLandmark.LEFT_SHOULDER, mp.solutions.pose.PoseLandmark.RIGHT_SHOULDER),
                    (mp.solutions.pose.PoseLandmark.LEFT_HIP, mp.solutions.pose.PoseLandmark.RIGHT_HIP)
                ]
    
                # Draw circles at landmarks and lines between connected landmarks (Light Pink)
                for connection in body_connections:
                    start_idx, end_idx = connection
                    start_landmark = landmarks[start_idx.value]
                    end_landmark = landmarks[end_idx.value]
    
                    start_point = (int(start_landmark.x * w), int(start_landmark.y * h))
                    end_point = (int(end_landmark.x * w), int(end_landmark.y * h))
    
                    # Light pink color for body landmarks and connections
                    cv2.circle(frame, start_point, 5, (255, 255, 0), -1)
                    cv2.circle(frame, end_point, 5, (255, 255, 0), -1)
    
                    # Draw lines between key points (light pink color)
                    cv2.line(frame, start_point, end_point, (255, 255, 0), 2)
    
            # Convert back to BGR for Kivy and display
            buf = cv2.flip(frame, 0).tobytes()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.img.texture = texture

    def on_stop(self):
        self.capture.release()

if __name__ == '__main__':
    CameraApp().run()
