
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

### Day 3: Custom Defect Inspection & Tensor Filtering
Objective: Extract raw mathematical outputs from the YOLOv8 neural network and engineer industrial business logic to filter out low-confidence background noise.

Key Implementations:

Data Parsing: Wrote Python script mechanics to break down the AI's complex output objects into raw numbers: bounding box matrix coordinates (xyxy), object class IDs (cls), and certainty ratings (conf).

Confidence Thresholding: Implemented an optimization guardrail (if confidence < 0.50: continue) to immediately drop low-certainty predictions (filtering out shaky 30% and 47% ghost detections) to prevent false alarms on the factory line.

Industrial Mapping: Created a Python dictionary look-up table (defect_mapping) to translate generic COCO asset classes (like person or potted plant) into actionable textile manufacturing alerts (e.g., Weave Anomaly and Color Stain).

Outcome: The terminal successfully processed the pixel grid, ignored background noise, isolated exactly 2 critical defects, and automatically generated an industrial pass/fail evaluation: STATUS: ROLL REJECTED ❌.

 ### Day 4: Full-Stack Interface Engineering via StreamlitObjective
: Wrap the backend computer vision scripts into a visual, interactive web application framework suitable for non-technical production operators.
Key Implementations:Frontend Design: Engineered a web dashboard using the Streamlit framework, introducing UI/UX components like st.file_uploader() for seamless image drag-and-drop capability.

System Environment Alignment: Diagnosed and resolved standard Windows multi-Python path conflicts (ModuleNotFoundError) by enforcing local dependency updates explicitly using the py -m pip install execution package standard.

Dynamic Data Pipeline: Bound the frontend UI directly to the backend vision layer. Uploaded images are converted live into NumPy arrays ($H \times W \times C$), evaluated by the model, and processed by the Day 3 filter matrix in real-time.

Visual Warning States: integrated state-dependent UI alerts (st.warning, st.error, and st.success) to render clean, high-impact industrial report cards based on the inspection verdict.

Outcome: Successfully deployed a fully functional, responsive local web server at localhost:8501 that completely abstracts backend terminal code into a sleek, deployable enterprise prototype.

### DAY 5 :
Objective: Upgrade the static dashboard to visually overlay neural network predictions directly onto the web application's image frame.

Key Implementations:

Matrix Visual Processing: Integrated YOLO’s .plot() method to burn geometric box boundaries directly into the image array variables.

Color Space Alignment: Fixed inverted image color problems by using OpenCV (cv2.cvtColor) to translate BGR numpy arrays into RGB arrays so the web browser renders skin tones and clothing colors perfectly.

UI Noise Reduction: Discovered the difference between deep learning outputs and frontend filters. Used labels=False parameter logic to suppress generic pre-trained tags (person, potted plant), allowing custom code mappings to handle business analytics cleanly.

Outcome: Created an enterprise-ready dashboard that shows users exactly where anomalies are located without overwhelming them with chaotic raw data labels.

