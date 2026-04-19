from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")

# Correct path (go one folder back)
results = model("../frames", save=True)

print("Segmentation completed!")