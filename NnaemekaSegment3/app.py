import os
import dash
import pandas as pd
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv("Tesla.csv")

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([

    html.H1("Tesla Stock Price Prediction Dashboard", style={'text-align': 'center'}),
    
    dcc.Dropdown(
        id="ticker",
        options=[{"label": x, "value": x} 
                 for x in df.columns[1:]],
        value=df.columns[8],
        clearable=False,
    ),
    dcc.Graph(id="time-series-chart"),
])

@app.callback(
    Output("time-series-chart", "figure"), 
    [Input("ticker", "value")])
def display_time_series(ticker):
    fig = px.line(df, x='date', y=ticker, title='Tesla Financial Information Trend')
    fig.update_xaxes(rangeslider_visible=True)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
    
