from ultralytics import YOLO

if __name__ == '__main__':
    # Load a baseline YOLO architecture model
    model = YOLO("yolov8n.pt")

    # Train for 3 quick rounds (epochs) to test your machine
    model.train(data="dataset.yaml", epochs=3, imgsz=640)