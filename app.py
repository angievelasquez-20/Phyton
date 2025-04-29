from pyexpat import model
from flask import Flask, render_template, request
import datetime
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

@app.route("/hello2")
def home():
  return"hello, flask"

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    #formatted_now = now.strftime ("%A, %d %B, %Y at %X")
    match_object =re.fullmatch ("[a-zA-Z]+", name)
    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "friend"
    content  = f"hello there, {clean_name} hour: {now}"
    return content

@app.route("/")
def RegresionLogistica():
    return render_template("RegresionLogistica.html")


@app.route('/calculategrades/', methods=["GET", "POST"])
def calculategrades():
    def generate_plot():
        result = None
        img_data = generate_plot()
        
        if request.method == 'POST':
            hours = float(request.form['hours'])
            prediction = model.predict([[hours]])[0]
            result = round(prediction, 2)
        
        return render_template('calculategrades.html', result=result, img_data=img_data)

@app.route('/menu')
def mostrar_menu():
    return render_template('menu.html')

@app.route('/decision_tree')
def decision_tree():
    # Datos de ejemplo
    X = np.array([[25, 5000, 1], [40, 10000, 0], [30, 7000, 1], [50, 15000, 0]])
    y = np.array([1, 0, 1, 0])  # 1: Compra, 0: No compra
    
    modelo = DecisionTreeClassifier()
    modelo.fit(X, y)

    # Datos de prueba (Ejemplo: [1, 0, 1])
    datos_cliente = np.array([[30, 6000, 1]])  # Edad: 30, Ingreso: 6000, Ubicación: 1
    prediccion = modelo.predict(datos_cliente)[0]

    datos = {'edad': 30, 'ingreso': 6000, 'ubicacion': 1}
    
    return render_template('DecisionTree.html', datos=datos, resultado=prediccion)


if __name__ == '__main__':
    app.run(debug=True)