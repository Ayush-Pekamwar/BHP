# Bangalore House Price Prediction

A machine learning regression project to predict house prices in Bangalore. The project includes data preprocessing, feature engineering, model selection, and deployment with a user-friendly web interface hosted on AWS.
<br>
Working Real-Time Website : http://ec2-13-48-30-156.eu-north-1.compute.amazonaws.com/
<br>
DataSet used : https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data

## Features

- Predict house prices based on area, location, number of bedrooms, and bathrooms.
- Clean and functional UI for user interaction.
- Hosted on AWS for easy access.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Steps Involved](#steps-involved)
4. [Setup and Installation](#setup-and-installation)
5. [Usage](#usage)
6. [Results](#results)
7. [Contributing](#contributing)
8. [License](#license)

---

## Project Overview

The Bangalore House Price Prediction project is designed to analyze and predict real estate prices in Bangalore using machine learning. The workflow involved:

- Data collection and preprocessing.
- Developing a regression model to estimate prices.
- Deploying the model as a web application.

---

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask
- **Machine Learning:** Python (NumPy, Pandas, Scikit-learn, Matplotlib)
- **Deployment:** AWS, Nginx

---

## Steps Involved

1. **Data Preprocessing**:
   - Data cleaning.
   - Handling missing values.
   - Removing outliers using standard deviation and domain knowledge.

2. **Feature Engineering**:
   - Dimensionality reduction for locations.
   - One-hot encoding for categorical features.

3. **Model Selection**:
   - K-fold cross-validation.
   - Hyperparameter tuning using GridSearchCV.
   - Selecting the best-performing model.

4. **Deployment**:
   - Exported the model using Pickle.
   - Built a user interface with HTML, CSS, and JavaScript.
   - Hosted the application on AWS with Nginx for reverse proxying.

---

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/bangalore-house-price-prediction.git
   ```

2. Navigate to the project directory:
   ```bash
   cd bangalore-house-price-prediction
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask server:
   ```bash
   python app.py
   ```

5. Access the application at `http://127.0.0.1:5000`.

---

## Usage

1. Enter the area in square feet, the number of BHKs, bathrooms, and select a location.
2. Click on **Estimate Price** to view the predicted house price.
3. Results are displayed interactively with animations.

---

## Results

The project achieved robust predictions using Linear regression, with optimized performance validated by K-fold cross-validation. The UI provides an intuitive user experience.
Working Website : http://ec2-13-48-30-156.eu-north-1.compute.amazonaws.com/
---
