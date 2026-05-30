# Predictive Analytics Using Historical Data

## Project Overview

This project uses Machine Learning techniques to analyze historical sales data and predict future sales trends using Linear Regression.

The system performs:

* Data cleaning
* Data preprocessing
* Model training
* Future prediction
* Accuracy evaluation
* Visualization generation

---

## Features

* Historical data analysis
* Data cleaning and preprocessing
* Missing value handling
* Duplicate removal
* Linear Regression model
* Future sales prediction
* Prediction accuracy evaluation
* Automated report generation
* Visualization of predicted trends

---

## Technologies Used

* Python
* Pandas
* Matplotlib
* Scikit-learn

---

## Machine Learning Algorithm

### Linear Regression

The project uses Linear Regression to predict sales based on historical quantity ordered data.

Where:

* x = Quantity Ordered
* y = Predicted Sales

---

## Dataset

The dataset contains historical sales records including:

* Quantity Ordered
* Sales
* Product Information
* Customer Information

---

## Project Workflow

```text id="rd1"
Historical Dataset
        ↓
Data Cleaning
        ↓
Preprocessing
        ↓
Train Regression Model
        ↓
Predict Future Sales
        ↓
Evaluate Accuracy
        ↓
Generate Reports & Charts
```

---

## Outputs Generated

### 1. Prediction Report

```text id="rd2"
prediction_report.csv
```

Contains:

* Actual Sales
* Predicted Sales

### 2. Prediction Visualization

```text id="rd3"
sales_prediction.png
```

Displays:

* Actual sales points
* Predicted regression trend

---

## How to Run the Project

### Install Required Libraries

```bash id="rd4"
pip install pandas matplotlib scikit-learn
```

### Run the Program

```bash id="rd5"
python main.py
```

---

## Model Evaluation

The model performance is evaluated using:

### R² Score

R^2

This measures prediction accuracy.

---

## Future Enhancements

* Time-series forecasting
* Multiple feature prediction
* Interactive dashboard
* Streamlit web application
* Advanced forecasting models

---

## Conclusion

This project demonstrates how Machine Learning and Predictive Analytics can be used to analyze historical data and forecast future trends efficiently.

It provides a beginner-friendly implementation of:

* Regression modeling
* Forecasting
* Data preprocessing
* Visualization
* Automated reporting
