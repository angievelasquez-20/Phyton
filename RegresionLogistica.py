"""regresion logistica para transporte de paquetes"""
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from flask import Flask, render_template, request
from datetime import datetime

clima_map = {
    "soleado": 0,
    "lluvioso": 1,
    "nublado": 2,
    "tormenta": 3
}

trafico_map = {
    "bajo": 0,
    "medio": 1,
    "alto": 2
}


def predict_transport(distancia, peso, clima, trafico):
    """
    Predice si el paquete se podrá transportar en funcion de distancia, peso, clima, trafico
    """
    X = np.array([
        [10, 5, 0, 0],
        [12, 4, 1, 1],
        [15, 6, 2, 1],
        [14, 5, 0, 2],
        [18, 7, 1, 0],
        [16, 6, 2, 0],
        [20, 8, 3, 1],
        [13, 4, 0, 1],
        [19, 9, 2, 1],
        [17, 6, 1, 2],
        [25, 12, 0, 1],
        [22, 9, 2, 0],
        [11, 3, 1, 0],
        [23, 10, 3, 0],
        [21, 7, 2, 2],
        [26, 14, 3, 2],
        [28, 15, 2, 2],
        [30, 16, 3, 1],
        [24, 11, 2, 2],
        [27, 13, 3, 2],
        [29, 14, 2, 1],
        [31, 17, 1, 2],
        [33, 18, 3, 1],
        [35, 20, 0, 2],
        [32, 16, 2, 2],
        [34, 19, 3, 0],
        [36, 21, 1, 2],
        [38, 22, 0, 2],
        [40, 25, 3, 2],
        [39, 24, 2, 2],
    ])

    y = [
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0
    ]

    model = LogisticRegression(max_iter=200)
    model.fit(X, y)

    # Codificar clima y trafico
    clima_code = clima_map.get(clima.lower(), 0)
    trafico_code = trafico_map.get(trafico.lower(), 0)

    x_new = np.array([[distancia, peso, clima_code, trafico_code]])
    pred = model.predict(x_new)
    return int(pred[0])

if __name__ == '__main__':
    print(predict_transport(15, 5, "soleado", "bajo"))