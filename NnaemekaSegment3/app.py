import dash
import pandas as pd
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as bdc

df = pd.read_csv("Tesla.csv")

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("Tesla Stock Price Prediction Dashboard", style={'text-align': 'center'}),
    
    dcc.Dropdown(
        id="ticker",
        options=[{"label": x, "value": x} 
                 for x in df.columns[1:]],
        value=df.columns[1],
        clearable=False,
    ),
    dcc.Graph(id="time-series-chart"),
])

@app.callback(
    Output("time-series-chart", "figure"), 
    [Input("ticker", "value")])
def display_time_series(ticker):
    fig = px.line(df, x='date', y=ticker, title='Tesla Financial Information Trend')
    return fig

app.run_server(debug=True)
