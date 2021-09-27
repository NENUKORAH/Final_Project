# import necessary libraries
import os
import flask
import plotly
from flask import (Flask, render_template,
    jsonify,
    request,
    redirect)
import numpy as np
import pandas as pd
import json
import datetime 
from pathlib import Path

import joblib
import yfinance as yf

import seaborn as sns
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sklearn.metrics import mean_squared_error, mean_absolute_error
import math
from fbprophet import Prophet
from fbprophet.serialize import model_to_json, model_from_json
from yfinance import ticker
from pydantic import BaseModel

from model import convert, predict

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# # Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# from .models import Pet

#
with open('serialized_modelT.json', 'r') as fin:
    model = model_from_json(json.load(fin))  # Load model

#create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
#@app.post("/predict")
def get_prediction():
        
        ticker= yf.Ticker("ticker")
        day= yf.Ticker("days")
        print(f"ticker++++++++++++++\n{ticker}")

        ticker= flask.request.form["ticker"]
        days= flask.request.form["day"]
        days = int(days)

        print(f"ticker++++++++++++++\n{ticker}")
        prediction_list = predict(ticker,days)
        print(f"prediction_list++++++++++++++\n{prediction_list}")
        #return ticker
        

        if not prediction_list:
            raise HTTPException(status_code=400, detail="Model not found.")

        response_object = {"ticker": ticker, "forecast": convert(prediction_list)}
              
        return response_object




if __name__ == "__main__":
    app.run(debug=True)













