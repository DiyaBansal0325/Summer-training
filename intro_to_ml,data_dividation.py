# -*- coding: utf-8 -*-
"""Intro to ML,Data Dividation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ld6T_EuX-le1FzSIREkaXFak97goqvXa
"""

# Introduction to Machine Learning ---->

# Data ----> divide (Input , target) ----> trained by ML Model ---> ML Model data Predction --->
# Model Accuracy .

# Normal Distribution --->
# -3 -2 -1 0 1 2 3

# here 0 ---> Central tendancy(mean , median)
# gap(standard deviation) equal

# Why we convert our data into Normal Distribution?
# (1). Calculation easy
# (2). take less time for training and executing .

# ML ---> Feature Engineering(Create Aprropriatre data) + ML Models ---> Solution .

# Feature Engineering

# (1). Data Dividation

import pandas as pd

df = pd.read_csv("covid_toy.csv")
# df.head(3)

df.isnull().sum()    ### return total missing values in a dataframe

from sklearn.impute import SimpleImputer

si = SimpleImputer()  ### It will fill missing values  .

# if data
# Numerical ---> fill data mean .
# Categorical ----> fill data most_frequent value .

df['fever'] = si.fit_transform(df[['fever']])

# df.isnull().sum()

# df.head(3)

df['has_covid'].value_counts()   ### it will return total frequency of each sub-category in a column

df['gender'] = df['gender'].map({"Female":0 , "Male":1})

df['cough'] = df['cough'].map({"Mild":0 , "Strong":1})

df['city'] = df['city'].map({
    "Kolkata":0,
    "Bangalore":1,
    "Delhi":2,
    "Mumbai":3
})

df['has_covid'] = df['has_covid'].map({"No":0 , "Yes":1})

df.sample(3)

x = df.drop(columns = ['has_covid'])   ###Independent data
# x

y = df['has_covid']  #### Target/dependent data
# y

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42)

print("Total Data Shape:" , df.shape)
print("-------------------------------")
print("Input data Shape:" , x.shape)
print("x_train data Shape:" , x_train.shape)
print("x_test data Shape:" , x_test.shape)
print("-------------------------------")

print("Target data Shape:" , y.shape)
print("y_train data Shape:" , y_train.shape)
print("y_test data Shape:" , y_test.shape)
print("-------------------------------")

# df(100,6) = x(100,5) + y(100,1)
# x(100,5) = x_train(80,5) + x_test(20,5)
# y(100,1) = y_train(80,1) + y_test(20,1)

# How can we convert our data into mean centroud (Normal distribution) ???

import numpy as np

np.round(x_train.describe() , 2)

from sklearn.preprocessing import StandardScaler

sc= StandardScaler()   ####  it will convert our data into mean centroid(mean=0,std=1)

x_train_sc = sc.fit_transform(x_train)  #### fit means learn the parameters and transform means apply on
# that data.

x_train_new = pd.DataFrame(x_train_sc , columns = x_train.columns)

np.round(x_train_new.describe() , 2)

# data ---> min = 0 , max = 1

np.round(x_train.describe() , 2)

from sklearn.preprocessing import MinMaxScaler

mn = MinMaxScaler()

x_train_mn = mn.fit_transform(x_train)

x_train_new = pd.DataFrame(x_train_mn , columns = x_train.columns)

np.round(x_train_new.describe() , 2)