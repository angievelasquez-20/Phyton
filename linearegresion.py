from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from sklearn.linear_model import LinearRegression


app = Flask(__name__)

data = {
    "Study Hours": [10, 15, 12, 8, 14, 5, 16, 7, 11, 13, 9, 4, 18, 3, 17, 6, 14, 2, 20, 1],
    "Final Grade": [3.8, 4.2, 3.6, 3, 4.5, 2.5, 4.8, 2.8, 3.7, 4, 3.2, 2.2, 5, 1.8, 4.9, 2.7, 4.4, 1.5, 5, 1]
}

df = pd.DataFrame(data)
x = df[["Study Hours"]]
y = df["Final Grade"]  # Corregir a serie en lugar de DataFrame

model = LinearRegression()
model.fit(x, y)

def generate_plot():
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='blue', label='Datos reales')
    plt.plot(x, model.predict(x), color='red', label='Regresión lineal')
    plt.title('Horas de estudio vs Calificación Final')
    plt.xlabel('Horas de estudio')
    plt.ylabel('Calificación')
    plt.legend()
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_data = base64.b64encode(buf.getvalue()).decode('utf-8')
    plt.close()
    return img_data



