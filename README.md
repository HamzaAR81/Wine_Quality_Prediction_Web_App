# Wine Quality Prediction App

![Wine Bottles](wine_bottles.jpg)

## Overview

The Wine Quality Prediction App is a web-based application that utilizes an Artificial Neural Network (ANN) to predict the quality of wine based on its chemical properties. The ANN model is trained on a dataset of various wines and their respective quality ratings. Users can input the wine's chemical characteristics into the app, and it will provide an estimate of the wine's quality.

## Features

- User-friendly web interface for inputting wine properties.
- Prediction of wine quality using an Artificial Neural Network.
- Insightful visualizations of the prediction results.
- Option to explore the dataset used for training the ANN model.
- Continuous improvement through updates and feedback.

## Installation

To use the Wine Quality Prediction App, follow these steps:

1. Clone this repository to your local machine using `git clone`.
2. Navigate to the project directory: `cd wine-quality-prediction-app`.
3. Install the required Python packages: `pip install -r requirements.txt`.
4. Launch the app: `python app.py`.
5. Open your web browser and go to `http://localhost:8000` to access the app.

## Usage

1. Input the wine's chemical properties:
   - Fixed Acidity
   - Volatile Acidity
   - Citric Acid
   - Residual Sugar
   - Chlorides
   - Free Sulfur Dioxide
   - Total Sulfur Dioxide
   - Density
   - pH
   - Sulphates
   - Alcohol

2. Click the "Predict" button to see the estimated quality of the wine.

3. Observe the visualizations to gain insights into the predictions.


**The dataset** The goal is to predict `Quality of Red Wine` using Artificial Nueral Network.

There are 11 independent variables :

   * `Fixed Acidity`
   * `Volatile Acidity`
   * `Citric Acid`
   * `Residual Sugar`
   * `Chlorides`
   * `Free Sulfur Dioxide`
   * `Total Sulfur Dioxide`
   * `Density`
   * `pH`
   * `Sulphates`
   * `Alcohol`

Target variable:
* `Quality`: The quality of wine that on scale from 1 to 6, how best the quality of wine is.

# How to Use This Project

Follow following steps:
1. Go to  **Command Prompt**

![Command Prompt Page](https://github.com/HamzaAR81/Earth_Quake_Prediction_web_app/blob/29d0e64578d5fb3c7628aa243421d020d429bbf2/Templete/cmd.png.png)

2. Write in command prompt
    ```python
    pip install -r requirements.txt

3. Also Write in cmd 
    ```python
    pip install streamlit

4. For Verification write:
    ```python
    streamlit hello

5. Then type
    ```python
    streamlit run <path of the Web_App.py>

6. This will appear:
 ![Home Page](https://github.com/HamzaAR81/Earth_Quake_Prediction_web_app/blob/29d0e64578d5fb3c7628aa243421d020d429bbf2/Templete/Web_App.png.png)

8. Now, fill the options and click result.


## Feedback and Contributions

We welcome feedback, suggestions, and contributions to improve the Wine Quality Prediction App. If you encounter any issues or have ideas to enhance the app, please open an issue or submit a pull request on this repository.

## Disclaimer

The predictions made by the Wine Quality Prediction App are based on the Artificial Neural Network model trained on historical data. The accuracy of predictions may vary, and the app should not be used as the sole determinant of wine quality. Always rely on the expertise of wine professionals and personal tasting experiences for accurate assessments.

---

# Thank You!

