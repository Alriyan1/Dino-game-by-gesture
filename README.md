# Dino Game by Gesture 🦖

**Dino Game by Gesture** is a lightweight Python project that lets you play the classic side-scrolling dinosaur game (or any application that accepts keyboard input) using body gestures detected from your webcam. It uses MediaPipe for pose detection, OpenCV for camera capture/display, and PyAutoGUI to send keyboard events.

---

## 🔧 Features

- Real-time pose detection using MediaPipe
- Gesture-to-key mappings: Jump/Duck/Start
- No game modification required — works by sending keyboard events to the active window
- Simple, easy-to-read code for customizing gestures and thresholds

---

## 🧩 How it works

1. The webcam feed is processed by `PoseModule.py`, which returns pose landmarks (key body points).
2. `main.py` computes distances between key points (shoulders, index finger, center line) and uses simple thresholds to decide which keystroke to send.
3. `pyautogui` issues the keyboard events (`up`, `down`, `enter`) to the currently focused window.

---

## ✅ Gesture Controls

- **Jump** — Raise your torso/shoulders to bring the mid-point closer to the top of the frame (detected by `upper_distance < 200`) → `Up` key
- **Duck** — Bend/bring shoulders closer to bottom of the frame (detected by `lower_distance < 200`) → `Down` key
- **Start / Restart** — Bring your right index near your left shoulder (detected by `RindexToLshoulder < 100`) → `Enter` key

> Tip: These thresholds are defined in `main.py`. Tweak the numeric values to fit your camera distance, resolution and lighting.

---

## 🛠️ Requirements

- Python 3.8+ (Windows recommended)
- Packages (install via pip):

```bash
pip install opencv-python mediapipe pyautogui
```

If you prefer to pin versions, use something like:

```bash
pip install "opencv-python>=4.5" "mediapipe>=0.8" pyautogui
```

---

## ▶️ Running the project

1. Make sure a game (e.g., Chrome Dino offline or another app that listens to keypresses) is open and the game window is focused.
2. Open a terminal in this folder and run:

```bash
python main.py
```

3. Position yourself so your shoulders and upper body are visible in the webcam. Follow printed debug distances in the terminal to fine-tune gestures.

4. Press `Esc` in the OpenCV window to exit.

---

## ⚙️ Calibration & Tips

- If keystrokes trigger too easily or not reliably, adjust the thresholds in `main.py`:
  - `upper_distance < 200` (jump)
  - `lower_distance < 200` (duck)
  - `RindexToLshoulder < 100` (start)
- Make sure the game window has focus; `pyautogui` will send events to whatever window is active.
- Ensure consistent lighting and a clean background for best pose detection.

---

## ✨ Improvements & Ideas

- Add a configuration file or command-line args for thresholds and camera index
- Add a small calibration mode to auto-compute thresholds for a user
- Add a GUI overlay with button to “activate” sending keystrokes
- Support for multiple games and custom key mappings

---

## Contributing

Contributions are welcome! Open an issue or submit a pull request with improvements or bug fixes.

---

If you want, I can add a `requirements.txt`, or implement a simple calibration flow to tune thresholds automatically. 🔧
