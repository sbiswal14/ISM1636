import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

import pickle

# Uncomment the following snippet of code to debug problems with finding the .pkl file path
# This snippet of code will exit the program and print the current working directory.
# import os
# exit(os.getcwd())

mowers_model = pickle.load(open('./data/lawn_riding_mowers.pkl', "rb"))

print("\n*****************************************************")
print("* Riding mowers ownership Prediction Model *")
print("*****************************************************\n")
income = float(input("Enter the Income: "))
lotsize = float(input("Enter the lot size: "))
df = pd.DataFrame({'Income': [income], 'Lot_Size': [lotsize]})
print(df)
result = mowers_model.predict(df)
probability = mowers_model.predict_proba(df)
ownership = ('Nonowner', 'Owner')
print(probability)
print(f"\nThe riding mowers model indicates probability of ownership at {probability[0][1]:.4f}, therefore it's indicated that the person is {ownership[result[0]]}.\n")
