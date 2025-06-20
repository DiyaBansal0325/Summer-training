# -*- coding: utf-8 -*-
"""ML Models.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/197Ow8SNDEYKN2-BxrZIbf74VppT7obqh
"""

#ML MOdels --->
#Data --- we will train the model ---> we pass input data to out model and this model will return prediction of that input data.

#Types of ML Models:
#1) Supervised ML Model ---> When we have labelled data , then we will use this model.
#2) Unsupervised ML Model ---> When we have only values not included column names

"""#1) Supervised ML Models"""

# 1). Linear Regression ---> When we have targeted data as numerical(continuous).

import numpy as np
import pandas as pd

df = pd.read_csv("insurance.csv")

df.head(2)

df.isnull().sum()

df = pd.get_dummies(df , columns= ['sex','smoker','region'])

df = df.astype(int)

df.head(3)

x = df.drop(columns = ['charges'])   ###Input features
y = df['charges']     ##Target feature

from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()            ###this is a model and we use when we have numerical target data

lr.fit(x_train , y_train)

y_pred = lr.predict(x_test)
#y_pred

#y_test

from sklearn.metrics import r2_score

r2_score(y_test , y_pred)

df = pd.read_csv("covid_toy.csv")

df = df.dropna()

# df.head(3)

df = pd.get_dummies(df , columns = ['gender','cough','city'])

# df.head(2)

from sklearn.preprocessing import LabelEncoder

lb = LabelEncoder()

df['has_covid'] = lb.fit_transform(df['has_covid'])

x = df.drop(columns= ['has_covid'])
y = df['has_covid']

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()

lr.fit(x_train , y_train)

y_pred = lr.predict(x_test)

from sklearn.metrics import accuracy_score

accuracy_score(y_test , y_pred)

