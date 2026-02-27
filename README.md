# Blood Bank Demand Prediction System
Overview:

The Blood Bank Demand Prediction System uses Machine Learning to predict future blood demand based on historical monthly usage data.

This system helps blood banks:

Predict blood requirements

Manage inventory efficiently

Prevent shortages

Support emergency preparedness

# Features

Machine Learning based prediction using Linear Regression

Blood demand forecasting

Data visualization using Matplotlib

Inventory planning support

Easy to use and extend

# Technologies Used

Python

Pandas

NumPy

Matplotlib

Scikit-learn

# Machine Learning Model

Model Used: Linear Regression

Purpose: Predict future blood demand based on past monthly usage.

# Input Features

Blood Type

October usage

November usage

December usage

January usage

February usage

Output

Predicted blood requirement in Litres

Example:

O+  : 270 Litres
A+  : 206 Litres
B+  : 173 Litres
AB+ : 39 Litres
O-  : 16 Litres
A-  : 17 Litres
B-  : 15 Litres
AB- : 7 Litres
# Visualization

The system generates a bar chart showing predicted blood demand.

# Project Structure
Blood-Bank-Prediction/
│
├── Blood Bank Dataset.csv
├── blood_prediction.py
├── README.md
└── requirements.txt
# How to Run

Step 1:

pip install pandas numpy matplotlib scikit-learn

Step 2:

python blood_prediction.py
# Applications

Hospitals

Blood banks

Healthcare analytics

Emergency planning

Inventory management

# Future Improvements

Deep Learning prediction model

Real-time prediction system

Web dashboard

Database integration

AI-based demand forecasting
