#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:48:55 2018

@author: johnyorangeseed
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import the datasets
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

print(X)


# taking care of the missing data
from sklearn.preprocessing import Imputer
# Specifying our strategy for imputing missing values
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
# Fitting this Imputer variable onto out matrix data X
imputer = imputer.fit(X[:, 1:3]) # Specify columns that contain the missing data
# Replace the missing data with the values
X[:, 1:3] = imputer.transform(X[:, 1:3])


# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# creating an object of the class we imported
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
# France is 0, Germany is 1, Spain is 2

# Machine learning models are based in equations, so it's good to
#encode categorical data into numerical values

# However, there is no relational order between the countries

# To prevent the ML model from interpreting order, use dummy 
#encoding table

# Fit the OneHotEncoder onto the first column of index 0
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

# Create the labelEncoder object for the dependent purchased column
labelEncoder_Y = LabelEncoder()
Y = labelEncoder_Y.fit_transform(Y)
# Yes is 1, no is 0


# Splitting the dataset into the training set and the test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42) 
# w/ test_size of 0.2 and 10 observations, 2 go to test & 8 go to training
# X corresponds to the feature variables,
# Y corresponds to the dependent variables
# random_state is the seed of random # generator, can be any int value












