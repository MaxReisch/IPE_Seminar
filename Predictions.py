import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#importing the data set

dataset = pd.read_csv('Verspaetung.csv', sep= ';', low_memory=False)

dataset['GA'] = dataset['GA'].astype('category')
dataset.dropna()



X = dataset.iloc[:, 0:12].values
y = dataset.iloc[:, 37].values


# Encoding categorical data

from sklearn.preprocessing import LabelEncoder, OneHotEncoder


labelencoder_X_2 = LabelEncoder()

X[:,2] = labelencoder_X_2.fit_transform(X[:,2])


