# Maize-Pollen-Germination

Maize-Pollen-Germination is a simple program based on artificial intelligence designed to detect germinated and not germinated maize pollen from stereomicroscopy images.


Requirements (first use only)

The use of Anaconda is recommended (a Python distribution with all necessary tools included).

1. Download and install Anaconda from: https://www.anaconda.com/download.
2. During installation, choose: Python version: 3.9 or later. Default installation settings.
3. After installation, open the Anaconda Prompt (Windows) or a terminal (Linux).


Installation (first use only)

1. Download this repository from GitHub: Click on Code → Download ZIP. Extract the folder to a location of your choice (e.g. Documents/ASAP).
2. Extract the folders "train" and "valid".
3. Download the model (https://github.com/altormon/Maize-Pollen-Germination/releases/download/v1.0/weights.zip). Extract the folder and insert it in the "detect" folder (Maize-Pollen-Germination/runs/detect).
4. Create a new environment in Anaconda (open "Anaconda Prompt") and install the required libraries:

cd %USERPROFILE%\Documents\Maize-Pollen-Germination

conda create -n mpg python=3.9

conda activate mpg

pip install -r requirements.txt


Usage

1. Inside the ASAP folder, place all the images you want to analyze inside the Input folder.
2. Run the script (F2) using the pre-trained model (best.pt is already included):

cd %USERPROFILE%\Documents\Maize-Pollen-Germination

conda activate mpg

python F2_Germinated_Pollen_Detection.py

3. The program will automatically process all images inside the Input folder. Results will be saved in a new folder called Results, including a Excel file with germination measurements, and processed images with detected pollen highlighted.


Notes

Only F2_Germinated_Pollen_Detection.py is needed to analyze new images. The other script (F1) is used for model training and is not necessary unless you want to retrain the AI model. Make sure all input images are clear and properly focused for best results.
