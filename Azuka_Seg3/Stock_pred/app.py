# import necessary libraries
import os
import flask
import plotly
import plotly.express as px
import plotly.offline.offline 
import plotly.graph_objects as go
import io
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
# Setup
#################################################


#create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def get_prediction():
        
        

        ticker= flask.request.form["ticker"]
        days= flask.request.form["day"]
        days = int(days)

        #Open MSFT or TSLA model from the json file
        with open(f'models/{ticker}.json', 'r') as fin:
            model = model_from_json(json.load(fin))  # Load model
            
        TODAY = datetime.date.today()

        future = TODAY + datetime.timedelta(days=days)

        dates = pd.date_range(start=TODAY, end=future.strftime("%m/%d/%Y"),)
        df = pd.DataFrame({"ds": dates})

        forecast = model.predict(df)
  
        

        response_object = {"ticker": ticker, "forecast": forecast['yhat'].to_dict()}
        
        fig = px.line(x = forecast["ds"], y=forecast["yhat"], 
                labels={"x": "Date ", "y": "Closing stock price " }, 
                range_x =("Sep 28,2021",  future),
                title="Tesla Potential Future Stock Values")
        
        fig.show()
        # return redirect("/", code=302)
      
                                      
        return jsonify(response_object)


if __name__ == "__main__":
    
    app.run(debug=True)













