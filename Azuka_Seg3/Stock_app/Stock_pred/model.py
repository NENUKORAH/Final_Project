# import necessary libraries
import os
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

#################################################
# Flask Setup
#################################################
#app = Flask(__name__)

#################################################
# Database Setup
#################################################

# from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

# # Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# from .models import Pet


#BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
msft = yf.Ticker("TSLA")
TODAY = datetime.date.today()


def train(ticker="TSLA"):
    # data = yf.download("^GSPC", "2008-01-01", TODAY.strftime("%Y-%m-%d"))
    data = yf.download(ticker, "2010-01-01", TODAY.strftime("%Y-%m-%d"))
    data.head()
    data["Adj Close"].plot(title=f"{ticker} Stock Adjusted Closing Price")

    df_forecast = data.copy()
    df_forecast.reset_index(inplace=True)
    df_forecast["ds"] = df_forecast["Date"]
    df_forecast["y"] = df_forecast["Adj Close"]
    df_forecast = df_forecast[["ds", "y"]]
    #df_forecast

    model = Prophet(interval_width=0.95, daily_seasonality=True)
    model.fit(df_forecast)

    #joblib.dump(model, "Msft.joblib")
    

    with open('serialized_modelT.json', 'w') as fout:
        # print(model_to_json(model))
        json.dump(model_to_json(model), fout)  # Save model
        


def predict(ticker, days):

#     model_file = ("Msft.joblib")
#     if not model_file.exists():
#         return False

#     model = joblib.load(model_file)
    with open('serialized_modelT.json', 'r') as fin:
        model = model_from_json(json.load(fin))  # Load model
    

    future = TODAY + datetime.timedelta(days=days)

    dates = pd.date_range(start="2020-01-01", end=future.strftime("%m/%d/%Y"),)
    df = pd.DataFrame({"ds": dates})

    forecast = model.predict(df)
    print(f"++++++++++++++forecast++++++++++\n{forecast}")

    #model.plot(forecast).savefig(f"{ticker}_plot.png")
    #model.plot_components(forecast).savefig(f"{ticker}_plot_components.png")

    return forecast.tail(days).to_dict("records")
        

def convert(prediction_list):
    output = {}
    for data in prediction_list:
        date = data["ds"].strftime("%m/%d/%Y")
        output[date] = data["trend"]
    return output
    


if __name__ =="__main__":
    predict("TSLA", 7)