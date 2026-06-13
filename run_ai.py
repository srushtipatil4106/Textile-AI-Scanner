from ultralytics import YOLO
import cv2

print("Initializing AI Brain...")
# Load a pre-trained YOLOv8 Nano model
model = YOLO("yolov8n.pt")

print("Scanning image...")
# Run the AI model on your sample image
results = model("sample.jpg")

# Look at the results
for result in results:
    # Print the boxes/objects found to the terminal
    print("\n=============================================")
    print(f"[AI RESULT] Found {len(result.boxes)} object(s) in the image!")
    print("=============================================\n")
    
    # Save a copy of the image with boxes drawn on it
    result.save(filename="output_result.jpg")
    print("[SUCCESS] Saved labeled image as 'output_result.jpg'")
    