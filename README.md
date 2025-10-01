# Maize-Pollen-Germination

Maize-Pollen-Germination is a simple program based on artificial intelligence designed to detect germinated and not germinated maize pollen from stereomicroscopy images.


Requirements (first use only)

The use of Anaconda is recommended (a Python distribution with all necessary tools included).

Download and install Anaconda from: https://www.anaconda.com/download
During installation, choose: Python version: 3.9 or later. Default installation settings
After installation, open the Anaconda Prompt (Windows) or a terminal (Linux).


Installation (first use only)

Download this repository from GitHub: Click on Code → Download ZIP. Extract the folder to a location of your choice (e.g. Documents/ASAP).
Extract the folders "train" and "valid".
Download the model (https://github.com/altormon/Maize-Pollen-Germination/releases/download/v1.0/weights.zip). Extract the folder and insert it in the "detect" folder (Maize-Pollen-Germination/runs/detect).
Create a new environment in Anaconda and install the required libraries:

cd %USERPROFILE%\Documents\Maize-Pollen-Germination

conda create -n mpg python=3.9

conda activate mpg

pip install -r requirements.txt


Usage

Inside the ASAP folder, place all the images you want to analyze inside the Input folder.
Run the script (F2) using the pre-trained model (best.pt is already included):

cd %USERPROFILE%\Documents\Maize-Pollen-Germination

conda activate mpg

python F2_Germinated_Pollen_Detection.py

The program will automatically process all images inside the Input folder. Results will be saved in a new folder called Results, including a Excel file with germination measurements, and processed images with detected pollen highlighted.


Notes

Only F2_Germinated_Pollen_Detection.py is needed to analyze new images. The other script (F1) is used for model training and is not necessary unless you want to retrain the AI model. Make sure all input images are clear and properly focused for best results.
