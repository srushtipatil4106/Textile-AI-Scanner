
# Textile AI Scanner 🧵🤖

A computer vision application built to automate quality control in manufacturing by identifying defects in fabric structures. This project is being constructed via an accelerated 7-day sprint.

## 📅 Progress Log

### Day 1: Environment Setup & Core Matrix Parsing
* **Milestone:** Built a clean environment architecture utilizing Python 3.14, OpenCV 4.13, and YOLOv8.
* **Technical Deep-Dive:** Implemented an image parsing script (`test_vision.py`) to read and convert static images into structured multi-dimensional numerical matrices (NumPy arrays).
* **Results:** Successfully isolated a sample matrix with grid shape dimensions matching the source asset’s spatial resolution.

### Day 2: Core Object Recognition & AI Inference
* **Milestone:** Integrated the Ultralytics YOLOv8 computer vision engine.
* **Technical Deep-Dive:** Developed an automated AI pipeline (`run_ai.py`) that initializes a pre-trained neural network framework, processes the raw BGR image array, extracts bounding-box tensor coordinates, and renders an annotated classification overlay.
* **Results:** Successfully predicted and mapped elements within the custom environment, generating `output_result.jpg`.
