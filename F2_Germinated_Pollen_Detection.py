# pip install pandas openpyxl
# pip install ultralytics
import os
import pandas as pd
import argparse
from ultralytics import YOLO

def main(threshold):
    model = YOLO("./runs/detect/weights/best.pt")
    input_folder = "./Input"
    output_folder = "./Results/Images"
    os.makedirs(output_folder, exist_ok=True)
    input_images = [f for f in os.listdir(input_folder) if f.endswith(('.jpg', '.png', '.jpeg', '.JPG', '.PNG', '.JPEG'))]
    results_list = []

    for image in input_images:
        full_input = os.path.join(input_folder, image)
        results = model(full_input, conf=threshold, save=True, project="./Results", name="Images", exist_ok=True)
        count_germinated = 0
        count_non_germinated = 0
        for result in results:
            for box in result.boxes:
                class_id = int(box.cls[0])
                confidence = box.conf[0].item()
                if confidence >= threshold:
                    class_name = model.names[class_id]
                    if class_name == "Germinated":
                        count_germinated += 1
                    elif class_name == "Not germinated":
                        count_non_germinated += 1
        results_list.append([image, count_germinated, count_non_germinated])

    df = pd.DataFrame(results_list, columns=["Image", "Germinated", "Not germinated"])
    os.makedirs("./Results", exist_ok=True)
    df.to_excel("./Results/results_classification.xlsx", index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.25,
        help="Confidence threshold (default=0.25)"
    )
    args = parser.parse_args()
    main(args.threshold)