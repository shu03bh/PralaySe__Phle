# PralaySePhle - Natural Disaster Prediction Web App

[![GitHub License](https://img.shields.io/github/license/shu03bh/PralaySePhle)](https://github.com/shu03bh/PralaySe__Phle/blob/main/LICENSE)

## Overview

**PralaySePhle** is a web app that predicts the chances of natural disasters like floods, earthquakes, storms, and droughts. By entering data such as rainfall, location, and other factors, the app uses machine learning models to help predict these disasters, allowing for better preparation and early warnings.

## Key Features

- **Disaster Predictions**: The app predicts:
  - **Floods** based on rainfall, water levels, and geography.
  - **Earthquakes** using seismic activity and location data.
  - **Storms** by analyzing weather conditions like wind speed and temperature.
  - **Droughts** based on rainfall, soil moisture, and temperature.
- **Simple Interface**: Easy to use, just enter your data and get predictions.
- **Accurate Models**: The app uses machine learning models trained to provide reliable disaster forecasts.
- **Responsive Design**: The app works on mobile, tablet, and desktop devices.
- **Video Guides**: Videos to help users navigate and understand the predictions.

## How the Machine Learning Models Work

We've trained four different models, each for a specific disaster. Here’s a breakdown:

### 1. **Flood Prediction**

- **Model Type**: Random Forest Classifier
- **Looks At**:
  - Rainfall (mm)
  - Water level (m)
  - Elevation (m)
  - Past flood history
- **Accuracy**: 85% on test data

### 2. **Earthquake Prediction**

- **Model Type**: Gradient Boosting Classifier
- **Looks At**:
  - Seismic activity (Richter scale)
  - Depth of the earthquake (km)
  - Tectonic plate locations
  - Latitude and longitude
- **Accuracy**: 82% on test data

### 3. **Storm Prediction**

- **Model Type**: XGBoost Classifier
- **Looks At**:
  - Wind speed (km/h)
  - Air pressure (hPa)
  - Temperature (°C)
  - Humidity (%)
- **Accuracy**: 88% on test data

### 4. **Drought Prediction**

- **Model Type**: Logistic Regression
- **Looks At**:
  - Rainfall (mm)
  - Temperature (°C)
  - Soil moisture (%)
  - Drought history
- **Accuracy**: 80% on test data

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, pandas, numpy

## Project Structure

```plaintext
├── static/
│   ├── css/             # Styling files
│   ├── js/              # JavaScript for app functionality
│   ├── images/          # Images used in the app
│   ├── videos/          # Video guides
├── templates/
│   ├── index.html       # Main homepage
│   ├── flood.html       # Flood prediction form
│   ├── earthquake.html  # Earthquake prediction form
│   ├── storm.html       # Storm prediction form
│   └── drought.html     # Drought prediction form
├── models/
│   ├── flood_model.pkl  # Flood prediction model
│   ├── earthquake_model.pkl  # Earthquake prediction model
│   ├── storm_model.pkl  # Storm prediction model
│   └── drought_model.pkl  # Drought prediction model
├── screenshots/         # Screenshots of the website
├── app.py               # Flask app backend
├── requirements.txt     # Python package dependencies
└── README.md            # This documentation file
```

## Screenshots

### Homepage
*Add a screenshot here*

### Flood Prediction Page
*Add a screenshot of the flood prediction page*

*Add more screenshots for the other disasters.*

## Installation

### Prerequisites

- Python 3.8 or higher
- Flask, scikit-learn, numpy, pandas

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/shu03bh/PralaySePhle.git
   cd PralaySePhle
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## How to Use

- Go to the homepage and choose a disaster to predict.
- Enter the required data (e.g., rainfall, location, temperature).
- Click on "Predict" to get the results.

## Contributing

We welcome contributions to improve the app. To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push the branch (`git push origin feature-name`).
5. Open a pull request.


This version is designed to be more user-friendly and easier to understand.
