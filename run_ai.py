from ultralytics import YOLO
import cv2

print("Initializing AI Brain...")

model = YOLO("yolov8n.pt")

print("Scanning image...")

results = model("sample.jpg")


for result in results:
    
    print("\n=============================================")
    print(f"[AI RESULT] Found {len(result.boxes)} object(s) in the image!")
    print("=============================================\n")
    
    
    result.save(filename="output_result.jpg")
    print("[SUCCESS] Saved labeled image as 'output_result.jpg'")
    
