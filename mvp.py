import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output



app = dash.Dash()
df = pd.read_csv(
    'https://raw.githubusercontent.com/M0chim0nster/MVP/master/data.csv')
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div([
 html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    })





    ])
if __name__ == '__main__':
    app.run_server()