# Prueba Resumen de Texto

Este proyecto cuenta con un frontend desarrollado con React, que proporciona una interfaz de usuario para ingresar el texto a resumir. Este frontend se conecta al backend implementado en Flask, encargado de realizar resúmenes de texto en español mediante el uso del módulo NLTK; para procesar y analizar el texto, eliminando palabras de parada y puntuación, calculando la frecuencia de las palabras y generando un resumen ordenado basado en la puntuación de las oraciones.

# Backend
Requisitos: 
- Python 3.11.5
- Flask 3.0 
- Flask-cors 4.0 
- Nltk 3.8.1

(Se necesita tener instalado python https://www.python.org/downloads/release/python-3115/)
Para instalar estos requisitos usar: 
pip install Flask flask-cors nltk

Se cuenta con dos archivos .py : 
- main.py : inicia flask y API
- modelo.py: modelo para resumen de texto

Ejecucion:
python main.py

# Frontend
Requisitos:
- node js 20.10.0 LTS
- axios 1.6.2
- react 18.2.0
- react-dom 18.2.0
- react-scripts 5.0.1
- web-vitals 2.1.4

(Se necesita tener instalado node.js https://nodejs.org/en)
Instalar dependencias:
npm install

En App.js se encuentra la logica para consumir la API usando axios y contiene la interfaz grafica.

Ejecucion:
npm start
