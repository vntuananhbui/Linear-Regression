# Linear Regression Salary Predictor**

## Introduction
This Python script performs linear regression analysis on salary data to predict future salaries based on years of experience. It uses the gradient descent algorithm to find the best-fit linear regression line for the given data. Additionally, the script allows users to make salary predictions for a specific year or visualize the linear regression line using matplotlib.

## Requirements
To run this script, you'll need the following:

Python 3.x installed on your machine.

Required Python packages: numpy, matplotlib, pandas, and scikit-learn. You can install them using pip:

### Copy code
```bash
# pip install numpy matplotlib pandas scikit-learn
```
## Usage
### Data Preparation:

Ensure you have a CSV file named 'salary_dataset.csv' containing two columns: 'year' and 'salary'.
Each row in the CSV file should represent a year-salary pair.
Run the Script:

Execute the script by running it in a Python environment (e.g., using a code editor or command line).
## Select an Option:

The script will prompt you to choose between two options:
Type '1' to predict future salary for a specific year.
Type '2' to plot the linear regression line alongside the data points.
## Option 1: Predict Future Salary
If you choose option '1,' the script will ask you to input a year for which you want to predict the salary.
After entering the year, the script will display the predicted salary for that year based on the linear regression model.
## Option 2: Plot Linear Regression Line
If you choose option '2,' the script will generate a plot showing the data points (years vs. salaries) and the linear regression line.
This visualization helps you visualize the relationship between years of experience and salary, showcasing how the linear regression model fits the data.
## Explain Code
The code is structured as follows:

It starts by importing necessary libraries, including numpy, matplotlib, pandas, and scikit-learn.

Data is loaded from a CSV file into a pandas DataFrame, separating years and salaries as input features.

Several functions are defined for gradient descent and linear regression:

get_gradient_b and get_gradient_m calculate the gradients for the intercept and slope of the linear regression line.

update_gradient updates the intercept and slope using the calculated gradients.

gradient_descent performs the gradient descent algorithm to optimize the intercept and slope.

predict_function predicts salaries based on the learned model.

The main part of the code uses gradient descent to fit a linear regression model to the data, and it prints the resulting intercept and slope.

Depending on the user's choice, the script either predicts a future salary or plots the linear regression line.

## Author
This mini project made by TomBui with learning resource from DLLT
