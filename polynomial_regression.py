### Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


### Import Dataset
dataset = pd.read_csv('amd_daily.csv')    # Feel free to use your own dataset to experiment.
# Add Day as index column to serve as independent variable
dataset['Day'] = range(1,len(dataset['Close'])+1)


# Data Preprocessing
# Extracting independent (X) and dependent (y) columns/fields/variables. You can experiment with different independent variables.
X = dataset.iloc[:,7:].values      # Independent variables (Date)
y = dataset.iloc[:,4:5].values       # Dependent variable (close)
# Reference for iloc: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html


# NOTE: This time we won't split the dataset into training and test set as we want to utilize whole dataset to train the model.


### Model Training
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Training the Linear Regression model (named linear_regressor here) on the dataset
linear_regressor = LinearRegression()      # Define regressor as regression instance. The linear regression class works for multiple regression as well.
linear_regressor.fit(X, y)     # Train the model on training data of both independent and dependent data.

poly_regressor = PolynomialFeatures(degree=25)   # You can try different degrees to best fit the model to the data.

# We generate a matrix of features to train our polynomial regressor on. As per the polynomial equation of the polynomial regression model, we need a feature for each degree.
X_poly = poly_regressor.fit_transform(X)
final_regressor = LinearRegression()
# Train final regression model with the polynomial matrix we created above.
final_regressor.fit(X_poly, y)
# Don't worry if you don't understand it. Go through the explanation to understand the concept in depth: https://github.com/meetofleaf/ML-Journal-ep3_Polynomial_Regression/blob/main/polynomial_regression_explanation.md


### Prediction
# Function to predict profit based on input using our models (final_regressor and poly_regressor)
def prediction(day):
    return final_regressor.predict(poly_regressor.fit_transform([[day]]))

print(prediction(295))  # The input is the day, which means the model predicts what will be the price of the stock on given number of day. Feel free to experiment.


### If you were able to run till here successfully, then machine learning part is complete. Let's visualize the model.


### Model Visualization
# Visualizing the linear regression model
plt.scatter(X,y, color="red")
plt.plot(X, linear_regressor.predict(X), color="blue")
plt.title("AMD Stock Polynomial Regression Analysis")
plt.xlabel("Day")
plt.ylabel("Price")
plt.show()

# Visualizing the polynomial regression model
plt.scatter(X,y, color="red")
plt.plot(X, final_regressor.predict(poly_regressor.fit_transform(X)), color="blue")
plt.title("AMD Stock Polynomial Regression Analysis")
plt.xlabel("Day")
plt.ylabel("Price")
plt.show()

