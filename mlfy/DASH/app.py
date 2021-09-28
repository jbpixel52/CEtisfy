# %%


import json

import dash
import dash_core_components as dcc
import dash_html_components as html
import matplotlib.pyplot as plt
import numpy as np
import pandas
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import spotipy
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

app = dash.Dash(__name__)


def make_pandas(dir):

    with open(dir) as f:
        songdata = json.load(f)
    df = pandas.DataFrame(songdata)
    return df


def fig_regression():
    df = make_pandas('../playlists/Top Songs - USA Sep-27-2021.json')
    dfy=make_pandas('../playlists/Top Songs - Mexico Sep-27-2021.json')
    X = df.valence.values.reshape(-1, 1)
    Y = dfy.valence.values.reshape(-1,1)
    model = LinearRegression()
    model.fit(X, Y)

    x_range = np.linspace(X.min(), X.max(), 100)
    y_range = model.predict(x_range.reshape(-1, 1))

    fig = px.scatter(df, x='valence', y='energy', opacity=1,hover_name='name')
    fig.add_traces(go.Scatter(x=x_range, y=y_range, name='Regression Fit'))
    fig.show()


fig_regression()


if __name__ == '__main__':
    app.run_server(debug=True)
