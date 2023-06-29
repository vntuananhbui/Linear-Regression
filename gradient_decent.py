from hashlib import new
import numpy as np
import matplotlib.pyplot as plt
from numpy import gradient
import pandas as pd
from sklearn.linear_model import LinearRegression

#get CSV file
dataFrame = pd.read_csv('salary_dataset.csv')

year = dataFrame['year'].values.reshape(-1,1)
salary = dataFrame['salary'].values.reshape(-1,1)
#define function


def get_gradient_b(x,y,m,b):
    N = len(x)
    sum_gradient_b = 0
    for i in range(N):
        sum_gradient_b += (y[i] - ((m*x[i]) + b))
    gradient_b = -(2/N) * sum_gradient_b
    return gradient_b

def get_gradient_m(x,y,m,b):
    N = len(x)
    sum_gradient_m = 0
    for i in range(N):
        sum_gradient_m += (x[i] * (y[i] - ((m * x[i]) + b)))
    gradient_m = -(2/N) * sum_gradient_m
    return gradient_m

def update_gradient(x,y,m_current,b_current,learning_rate):
    gradient_m = get_gradient_m(x,y,m_current,b_current)
    gradient_b = get_gradient_b(x,y,m_current,b_current)
    b = b_current - (learning_rate * gradient_b)
    m = m_current - (learning_rate * gradient_m)
    return b,m

def gradient_descent(x,y,learning_rate,iteration):
    b= 0
    m= 0
    for i in range(iteration):
        b,m = update_gradient(x,y,m,b,learning_rate)
    return b,m

def predict_function(x,m,b):
    predict = m*x + b
    print('In',x,'years, your salary is: ',predict)
#main funtion

b,m = gradient_descent(year,salary,0.01,1000)
# print('Intercept: ',b)
# print('Coeff: ',m)
y = [m*x + b for x in year]

predict_function(8,m,b)
#User input
user_input = input("Please type '1' : Predict the future Value | Please type '2' : Plot the Linear Regression Line")

if user_input == '1':
    input1 = int(input("Please type year you will work"))
    print(input1)
    predict_function(input1,m,b)
elif user_input == '2':
    plt.plot(year,salary,'o')
    plt.plot(year,y)
    plt.show()



