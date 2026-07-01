import os
import cv2
import numpy as np

# Create clean folders inside your project
paths = [
    "datasets/images/train",
    "datasets/images/val",
    "datasets/labels/train",
    "datasets/labels/val"
]
for p in paths:
    os.makedirs(p, exist_ok=True)

def create_mock_images(img_dir, label_dir, count):
    for i in range(count):
        
        img = np.ones((640, 640, 3), dtype=np.uint8) * 180
        
        cv2.rectangle(img, (200, 200), (400, 400), (30, 30, 30), -1)
        
        cv2.imwrite(os.path.join(img_dir, f"fabric_{i}.jpg"), img)
        
        
        with open(os.path.join(label_dir, f"fabric_{i}.txt"), "w") as f:
            f.write("0 0.5 0.5 0.3 0.3\n")

print("🧵 Generating your mock fabric dataset...")
create_mock_images("datasets/images/train", "datasets/labels/train", 4)
create_mock_images("datasets/images/val", "datasets/labels/val", 2)
print("✅ Done! Folders are ready.")