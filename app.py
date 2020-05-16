import pickle
with open('model.pickle','rb') as f:
    model=pickle.load(f)
# model.predict()

from flask import Flask, render_template, request
import numpy as np
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check")
def check():
    return render_template("check.html")
@app.route("/putmarks",methods=['POST'])
def putmarks():
    features=[float(value) for value in request.form.values()]
    print(features)
    features=[features]
    marks=model.predict(features)[0]*5
    return render_template("check.html",percentage=marks)

if __name__=="__main__":
    app.run(debug=True)