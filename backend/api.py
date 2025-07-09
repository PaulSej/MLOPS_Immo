from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin


import joblib
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd
import numpy as np
import json
import logging


app = Flask(__name__)
cors = CORS(app, resources={r"/predict": {"origins": "http://localhost"}}) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'



logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

linear_regression_model = joblib.load("linear_regression_apartments_paris.pkl")

@app.route('/')
@cross_origin()
def home():
    return jsonify({"welcome": "Welcome to Flask with Docker! Does hot reload features works?"})

@app.route('/predict', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content-Type'])
def predict():
    
    python_dict_predictor = request.get_json()
    #logger.debug(f'Received data: {python_dict_predictor}')
    python_dict_predictor = {k:[v] for k,v in python_dict_predictor.items()} 
    pandas_serie_predictor = pd.DataFrame(data=python_dict_predictor)

    price_prediction = linear_regression_model.predict(pandas_serie_predictor)
    #logger.debug(f'Received data: {price_prediction}')
    return jsonify(int(price_prediction[0]))




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)