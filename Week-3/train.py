from ultralytics import YOLO

# Load model
model = YOLO("yolov8n.pt")

# Train on small dataset (built-in)
model.train(data="coco8.yaml", epochs=10)
