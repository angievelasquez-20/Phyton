from flask import Flask, render_template, request, jsonify
import numpy as np
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

def decision_tree(edad, ingreso, ubicacion):
    # Datos de ejemplo (deberías usar tus propios datos)
    X = np.array([[25, 5000, 1], [40, 10000, 0], [30, 7000, 1], [50, 15000, 0]])
    y = np.array([1, 0, 1, 0])  # 1: Compra, 0: No compra

    modelo = DecisionTreeClassifier()
    modelo.fit(X, y)

    # Datos de prueba
    datos_cliente = np.array([[edad, ingreso, ubicacion]])
    prediccion = modelo.predict(datos_cliente)[0]

    return "Compra" if prediccion == 1 else "No Compra"

