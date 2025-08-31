from ultralytics import YOLO

# Load a pretrained YOLOv8 model (you can choose nano/small/medium)
model = YOLO("yolov8n.pt")  # nano is lightweight

# Train the model on your dataset
results = model.train(
    data=r"C:\Users\Lathika\OneDrive\Desktop\E_Waste_Project\underwater_plastics\data.yaml",

    epochs=10,
    imgsz=640
)


# Evaluate on validation set
metrics = model.val()

# Run inference on a test image
results = model.predict(source="ewaste/underwater pollution/test", save=True)
