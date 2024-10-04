![Demo](https://raw.githubusercontent.com/ISmokeData/Mediapipe_Tracker_GUI/f97cc53304386ed76bae2d8f6e3feba700e270cb/tempelate/zuuzuz.gif)

# Camera Feed Detection App with Kivy, OpenCV, and MediaPipe

This project is a live camera feed application built using Kivy, OpenCV, and MediaPipe. It detects and tracks facial landmarks, hand landmarks, and body pose landmarks in real-time. The app is designed to visualize these landmarks using circles and connecting lines, making it easy to see key points on the face, hands, and body.

## Features

- **Real-time Camera Feed**: Accesses the webcam to display a live camera feed within a Kivy interface.
- **Face Detection**: Detects facial landmarks and visualizes them using light purple circles and connecting lines.
- **Hand Detection**: Detects hand landmarks and draws light purple circles at key points, with connecting lines between them.
- **Pose Detection**: Detects full body pose landmarks, including the shoulders, elbows, wrists, hips, knees, and ankles, and visualizes connections between them using light pink lines and circles.
- **Customizable FPS**: Runs at 30 FPS but can be adjusted as needed.

## Technology Stack

- **Kivy**: Used to create the graphical user interface and handle the live camera feed.
- **OpenCV**: For capturing the camera feed and converting the image format.
- **MediaPipe**: For detecting and processing face, hand, and pose landmarks.
- **Python**: The primary language for writing the application logic.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/CameraApp.git
    cd CameraApp
    ```

2. Install the required dependencies:
    ```bash
    pip install kivy opencv-python mediapipe
    ```

3. Run the app:
    ```bash
    python main.py
    ```

## How It Works

1. **Face Detection**: 
   - Uses MediaPipe's FaceMesh to detect multiple facial landmarks and draws light purple circles on detected points.
   
2. **Hand Detection**: 
   - Detects key points on the hand and connects them with lines using MediaPipe’s Hand solution.

3. **Pose Detection**: 
   - Tracks body pose landmarks such as shoulders, elbows, wrists, hips, and knees, drawing light pink connections between these points.


## Future Enhancements

- Add support for gesture recognition using hand landmarks.
- Implement better performance optimization for low-end devices.
- Extend to track multiple people in the camera feed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
