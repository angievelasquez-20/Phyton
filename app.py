from multiprocessing import reduction
from pyexpat import model
from turtle import towards
from flask import Flask, render_template, request, jsonify
import datetime
import re
from matplotlib import dates
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from flask import Flask, render_template
import RL


app = Flask(__name__)

@app.route("/hello")
def home():
  return"hello, flask"

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime ("%A, %d %B, %Y at %X")
    match_object =re.fullmatch ("[a-zA-Z]+", name)
    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "friend"
    content  = f"hello there, {clean_name} hour: {now}"
    return content

@app.route("/RegresionLineal")
def RegresionLineal():
    return render_template("RegresionLineal.html")

    
@app.route('/calculategrades', methods=["GET", "POST"])
def calculategrades():
    def generate_plot():
        result = None
        img_data = generate_plot()
        
        if request.method == 'POST':
            hours = float(request.form['hours'])
            prediction = model.predict([[hours]])[0]
            result = round(prediction, 2)
        
        return render_template('calculategrades.html', result=result, img_data=img_data)


@app.route("/decision_tree/")
def decision_tree():
    return render_template('DecisionTree.html', datos=dates, resultado=reduction)

@app.route("/RL/")
def RL():
    return render_template('RL.html', datos=dates, resultado=reduction)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/RegresionLogistica", methods=["GET", "POST"])
def RegresionLogistica():
    predicted_result = None
    if request.method == 'POST':
        try:
            distancia = float(request.form['distancia'])
            peso = float(request.form['peso'])
            clima = request.form['clima']
            trafico = request.form['trafico']

            predicted_result = RegresionLogistica.predict_transport(distancia, peso, clima, trafico)

        except (ValueError, TypeError):
            predicted_result ="Entrada no valida"

    return render_template("RegresionLogistica.html", predicted_result=predicted_result)


@app.route("/DefMachine")
def DefMachine():
    return render_template("DefMachine.html") 

@app.route("/DefInteligencia")
def DefInteligencia():
    return render_template("DefInteligencia.html")

@app.route("/Diferencia")
def Diferencia():
    return render_template("Diferencia.html")

@app.route("/modelosML")
def modelosML():
    return render_template("modelosML.html")

if __name__ == '__main__':
    app.run(debug=True)



