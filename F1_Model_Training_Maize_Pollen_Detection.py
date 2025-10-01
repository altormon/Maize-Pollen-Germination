# pip install ultralytics
# pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
import os
import torch
from ultralytics import YOLO
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
model = YOLO("yolov9c.pt")
model.train(
    data="C:/Users/atorr/Documents/doctorado_biotecnologia/resultados/Germinacion/Maize_Pollen_Germination_v2plus2/datav2plus2.yaml",
    epochs=150,
    imgsz=640,
    batch=8,
    device="cuda" if torch.cuda.is_available() else "cpu",
    augment=True,
    hsv_h=0.015,
    hsv_s=0.7,
    hsv_v=0.4,
    translate=0.1,
    scale=0.5,
    degrees=0,
    flipud=0.5,
    fliplr=0.5,
    mosaic=1.0,
    mixup=0.1,
    copy_paste=0.1,
    workers=4,
    patience=20,
    optimizer="AdamW",
    lr0=0.001,
    project="PollenYOLO",
    name="YOLOv9_Maize_Pollen",
    exist_ok=True,
    single_cls=False)