## Subash Chandra Biswal (U77884251)  ##


from flask import *
from urllib import response
from flask import render_template
from flask import *
from flask import Flask, request, flash

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import os

import pickle

# Uncomment the following snippet of code to debug problems with finding the .pkl file path
# This snippet of code will exit the program and print the current working directory.
# import os
# exit(os.getcwd())

mowers_model = pickle.load(open('../Assignment/data/lawn_riding_mowers.pkl', "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/postmessage", methods=['GET', 'POST'])
def postmessage():
    if request.method == "POST":
        income = float(request.form["income"])
        lotsize = float(request.form["lotsize"])
        df = pd.DataFrame({'Income': [income], 'Lot_Size':[lotsize]})
        result = mowers_model.predict(df)
        probability = mowers_model.predict_proba(df)
        ownership = ('Nonowner', 'Owner')
        return_str = f"\n\n\nThe riding mowers model indicates that the person is {ownership[result[0]]} with ownership probability at {probability[0][1]:.4f}.\n"
        return_str += "<br><a href='/'>Back</a>"
        return return_str
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

