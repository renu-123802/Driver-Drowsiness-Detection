# Driver Drowsiness Detection System 🚗💤

An AI-powered safety application that monitors driver alertness in real-time to prevent accidents caused by fatigue and distraction.

## 📌 Project Overview
Drowsiness is one of the leading causes of road accidents worldwide. This project uses **Computer Vision** and **Deep Learning** landmarks to detect signs of sleepiness (closed eyes) or fatigue (yawning) and triggers an immediate audio alarm to alert the driver.

## ✨ Key Features
* **Real-time Face Tracking:** Uses Dlib's 68-point facial landmark predictor.
* **Eye Aspect Ratio (EAR):** Detects if eyes are closed for a specific duration.
* **Mouth Aspect Ratio (MAR):** Detects yawning patterns through mouth opening.
* **Instant Audio Alerts:** High-frequency alarm triggered via Pygame.
* **Visual HUD:** Real-time bounding boxes and landmark overlays on the video feed.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Computer Vision:** OpenCV, Dlib
* **Audio Handling:** Pygame
* **Mathematics:** NumPy (for Euclidean distance calculations)

## 📐 How it Works (Technical Logic)
The system calculates the **Eye Aspect Ratio (EAR)** to determine if the eyes are blinking or closed.

The EAR formula is:
$$EAR = \frac{||p_2 - p_6|| + ||p_3 - p_5||}{2||p_1 - p_4||}$$

If the EAR stays below a threshold (e.g., 0.25) for more than 20 consecutive frames, the alarm is triggered. A similar logic is applied to the **Mouth Aspect Ratio (MAR)** to detect yawning.

## 🚀 Getting Started

### 1. Clone the Repository
git clone https://github.com/renu-123802/Driver-Drowsiness-Detection.git
cd Driver-Drowsiness-Detection
---

### 3. Check your `alarm.py` (First Image)
I noticed in your first screenshot that you are still using the **hardcoded absolute path** on line 11:
`r'C:\Users\Renu\OneDrive\Desktop\project...'`

Since you've moved everything into a clean GitHub structure, **this code will crash** for anyone else (or even for you if you rename the folder). 

**Update line 11 to use a relative path:**
```python
import os
# ... inside your function
base_path = os.path.dirname(__file__)
alarm_file = os.path.join(base_path, "..", "data", "alarm.wav")