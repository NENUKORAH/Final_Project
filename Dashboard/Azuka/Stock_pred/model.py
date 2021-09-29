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
from yfinance import ticker

#################################################
# Flask Setup
#################################################
#app = Flask(__name__)

#################################################
# Setup
#################################################


TODAY = datetime.date.today()


def train(ticker, days):
    #ticker= yf.Ticker(ticker)#, days=7)
    # data = yf.download("^GSPC", "2008-01-01", TODAY.strftime("%Y-%m-%d"))
    data = yf.download(ticker, start="2010-01-01", end=TODAY.strftime("%Y-%m-%d"))
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
    

    with open(f'models/{ticker}.json', 'w') as fout:
        # print(model_to_json(model))
        json.dump(model_to_json(model), fout)  # Save model
        


def predict(ticker, days):

    with open('serialized_modelT.json', 'r') as fin:
        model = model_from_json(json.load(fin))  # Load model
    

    future = TODAY + datetime.timedelta(days=days)

    dates = pd.date_range(start="2020-01-01", end=future.strftime("%m/%d/%Y"),)
    df = pd.DataFrame({"ds": dates})

    forecast = model.predict(df)
    print(f"++++++++++++++forecast++++++++++\n{forecast}")

    return forecast.tail(days).to_dict("records")
        

def convert(prediction_list):
    output = {}
    for data in prediction_list:
        date = data["ds"].strftime("%m/%d/%Y")
        output[date] = data["trend"]
    return output
    


if __name__ =="__main__":
    #ticker_name = "TSLA"

    ticker_names = ['TSLA', 'MSFT', 'AAPL']

    [train(name) for name in ticker_names]
    #predict(ticker_name, 7)