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



