from ultralytics import YOLO

# Load a pre-trained YOLOv11 model
model = YOLO('yolov5n.pt')  # 'n' denotes the nano version; adjust as needed

# Train the model on your dataset
results = model.train(
    data='E:/railroad_crossing/crossing/Traintracks-4/data.yaml',
    epochs=10,
    batch=4,
    name='traintrack-fast',
    save_period=1,  # ← Save weights after every epoch
    project='railway_output',
    exist_ok=True
)

