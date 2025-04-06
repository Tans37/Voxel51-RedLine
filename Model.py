from ultralytics import YOLO

model = YOLO("yolov8s-seg.pt") 

model.train(
    data="/content/Railway-tracks-1/data.yaml", 
    epochs=100,                
    lr0=0.0005,
    freeze=10,                
    name="track_only_finetune",
    pretrained=True
)