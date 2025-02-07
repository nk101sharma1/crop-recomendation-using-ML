# LNCT-Smart-Agriculture-Crop-Recommendation
This platform leverages machine learning to provide crop recommendations based on environmental and soil parameters. By inputting data such as nitrogen, phosphorus, potassium levels, temperature, humidity, and rainfall, the application predicts the best crops suited for the given conditions.
Here's the updated README file with the addition of the **crop_recommendation.csv** file in the file structure:

---

# LNCT Smart Agriculture Crop Recommendation Platform 1.0

## Overview

The **LNCT Smart Agriculture Crop Recommendation Platform** is a machine learning-powered web application built to recommend the most suitable crop for a given set of agricultural parameters. The platform takes in parameters such as soil nitrogen, phosphorus, potassium, temperature, humidity, soil pH, and rainfall, then uses a pre-trained machine learning model to predict the optimal crop to grow in the given environment.

## Features

- **Machine Learning-Powered Predictions**: The platform uses a machine learning model to predict the best crop based on input parameters.
- **User-Friendly Interface**: The application offers an intuitive web interface for users to enter agricultural data easily.
- **Documentation Modal**: Provides a detailed explanation of the parameters and their valid ranges for users.
- **Web-Based**: The platform is a web-based application, accessible through any browser.

## Installation Guide

### Prerequisites

To run this application locally, you will need:

- **Python 3.x** installed on your system.
- **Flask** for the backend.
- **Pickle** for loading the pre-trained machine learning model.
- **Numpy** for handling numerical operations.
- **pandas** for analyzing, cleaning, exploring, and manipulating data.
- **scit-learn** for learning, pre-processing, cross-validation, and visualization algorithms using.





### Steps

1. **Clone the Repository**:  
   If you have not already, clone the repository to your local machine.
   
   ```bash
   git clone https://github.com/Birendra7/LNCT-Smart-Agriculture-Crop-Recommendation
   cd LNCT-Smart-Agriculture-Crop-Recommendatio
   ```

2. **Create a Virtual Environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```

3. **Install Dependencies**:

   Install the required libraries via `pip`:

   ```bash
   pip install flask numpy scikit-learn
   ```

4. **Add the Model**:

   Ensure that you have a pre-trained machine learning model saved as `model.pkl`. This model should be in the same directory as the `app.py` file.

5. **Add the Dataset**:

   You also need to ensure that the `crop_recommendation.csv` dataset is in the same directory as `app.py`. This file contains the historical crop data used for training the model.

6. **Run the Flask Application**:

   After setting everything up, you can start the Flask server by running:

   ```bash
   python app.py
   ```

   The application will be available at `http://127.0.0.1:5000/`.

7. **Access the Platform**:

   Open a web browser and navigate to `http://127.0.0.1:5000/`. The platform will load, allowing you to input soil and environmental parameters to receive crop recommendations.

## Application Structure

Here’s the folder structure of the application:

```
LNCT-Smart-Agriculture/
│
├── app.py                         # Flask backend application
├── model.pkl                      # Pre-trained machine learning model
├── crop_recommendation.csv        # Dataset containing agricultural data
├── static/
│   ├── styles.css                 # CSS styling for the platform
│   └── style.js                   # JavaScript file for handling interactivity
├── templates/
│   └── index.html                 # HTML template for the web interface
├── README.md                      # Documentation for the application
└── LICENSE                        # License information (MIT)
└── database/
    └── crop_recommendation.csv     #  recommendations nse information (MIT)
```

### Folder Breakdown

- **app.py**: This is the main Python file that runs the Flask web application, handles form submissions, and serves the machine learning predictions.
- **model.pkl**: The trained machine learning model (pickle file) that is used to make predictions based on the input parameters.
- **crop_recommendation.csv**: The dataset that contains agricultural data used to train the machine learning model.
- **static/styles.css**: Contains the CSS styling for the application, including layout, colors, and font styles.
- **static/style.js**: Contains JavaScript code to handle user interactions such as opening the documentation modal and handling form submission.
- **templates/index.html**: The HTML structure for the user interface, where users input agricultural parameters.
- **README.md**: Provides an overview of the project and the steps to set it up.
- **LICENSE**: A file containing the MIT License for this project.

## Usage

### Input Parameters:
To get a crop recommendation, enter the following parameters into the form on the web interface:

- **Nitrogen (N)**: Ratio of Nitrogen content in soil (1-500 PPM)
- **Phosphorus (P)**: Ratio of Phosphorous content in soil (1-500 PPM)
- **Potassium (K)**: Ratio of Potassium content in soil (1-500 PPM)
- **Temperature**: Expected temperature in °C (-50 to 50)
- **Humidity**: Relative humidity in percentage (0-100%)
- **Soil pH**: Soil pH value (0-14)
- **Rainfall**: Expected rainfall in mm (max 1000 mm)

After entering the data, click the **Recommend** button, and the system will return a prediction with the recommended crop.

### Documentation Modal:

You can view the documentation by clicking the **Click here for the Documentation** button. The modal describes each input parameter and its valid range.

## Example Use Case

1. User enters the following parameters:
    - **Nitrogen (N)**: 180
    - **Phosphorus (P)**: 50
    - **Potassium (K)**: 120
    - **Temperature**: 25°C
    - **Humidity**: 60%
    - **Soil pH**: 6.5
    - **Rainfall**: 400 mm
    
2. After submitting the form, the platform predicts and recommends the best crop for these conditions, such as "Rice" or "Wheat" based on the pre-trained model's prediction.

## Screenshots

Here are some example screenshots of the platform:

1. **Home Page with Form Input:**

![image](https://github.com/user-attachments/assets/569799fb-22c6-4630-bc5b-5e7813c852c9)

2. **Documentation Modal:**

![image](https://github.com/user-attachments/assets/d901d546-6d8c-4b00-96e2-126353be7f73)

3. **Crop Recommendation Result:**

![image](https://github.com/user-attachments/assets/1f388cf8-26c6-4bfd-ae9d-7cda6811156a)

   

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The machine learning model used for crop prediction can be any suitable model trained with relevant agricultural data. Make sure to train and pickle your own model or replace `model.pkl` with a model that fits your needs.
- The dataset `crop_recommendation.csv` is used to train the model. You can modify it or add more data to improve the model's accuracy.

--- 

### Additional Notes:

1. You can store screenshots in a `![image](https://github.com/user-attachments/assets/27fe4f28-41d9-498c-bd4b-5862bad8b1d5)
 folder in your project and link them in the README.
2. If the machine learning model isn't included in the repo, users should be instructed on how to generate or obtain the `model.pkl` file.


# live link :- https://lnct-smart-agriculture-crop-u467.onrender.com/
