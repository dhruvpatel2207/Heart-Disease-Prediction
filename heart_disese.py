import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data Collection and Processing """

#Loading the csv data to a Pandas DataFrame
heart_data = pd.read_csv('/content/data.csv')

# Printing the first five rows in the data
heart_data.head()

# Printing the last five rows in the data 
heart_data.tail()

# Print the number of rows and columns 
heart_data.shape

# Getting some information about the data 
heart_data.info()

# Checking the null values in the data 
heart_data.isnull().sum()

# Getting some statistical measures about the data 
heart_data.describe()

# Checking the Distribution of the Target Values 
heart_data['target'].value_counts()

"""1 --> Defective Heart

2 --> Healthy Heart

Spliting the Features and Targets
"""

X = heart_data.drop(columns='target',axis=1)
Y = heart_data['target']

print(X)

print(Y)

"""Spliting the data into Training data and Testing data"""

X_train , X_test , Y_train , Y_test = train_test_split(X , Y , test_size=0.2, stratify=Y, random_state=2)

print(X.shape , X_test.shape , X_train.shape)

"""Model Training

Logistics Regression
"""

model = LogisticRegression()

# Traing LogisticsRegression Model with Training data 
model.fit(X_train, Y_train)

"""Model Evaluation

Accuracy Score
"""

# accuracy on training data 
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction , Y_train)

print('Accuracy of training data : ',training_data_accuracy)

# accuracy on test data 
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction , Y_test)

print('Accuracy of test data :',test_data_accuracy)

"""Building the predective system """

input_data = (53,1,0,140,203,1,0,155,1,3.1,0,0,3)

# Change the input data to numpy array 
input_data_as_numpy_array = np.asarray(input_data)

# Reshape the numpy array as we are prediciting for oly one instance 
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)

print(prediction)

if(prediction[0]==0 ):
  print('The Person does not have Heart Disease')
else:
  print('The Person is suffering from Heart Disease')

import pickle
with open('heart_disease.sav','wb') as file:
  pickle.dump(model ,file)

