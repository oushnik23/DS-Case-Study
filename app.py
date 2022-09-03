# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 14:49:42 2022

@author: Administrator
"""
import os
os.getcwd()
os.chdir(r"C:\Users\Administrator\Desktop\PYTHON\DS Case Study Eko")

import numpy as np
import pickle

from flask import Flask, render_template, request
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    feature=[float(x) for x in request.form.values()]
    f1=np.array(feature).reshape(1,10)
    prediction=model.predict(f1)
    if int(prediction)==1:
        prediction="Yes"
    else:
        prediction="No"
    return render_template("home.html",prediction_text="The employee is {}".format(prediction),**locals())
    #if int(prediction)==1:
        #output="Yes"
    #else:
        #output=="No"
    #return render_template("home.html",prediction=output)
    
if __name__=="__main__":
    app.run(debug=True)
