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


def make_pandas():
    
    with open('./songdata.json') as f:
        songdata = json.load(f)
    df = pandas.DataFrame(songdata)
    #pp.pprint(df)
    dfcopy = df.squeeze()
    #pp.pprint(dfcopy)
    return df

def fig_regression():
    # df = px.data.tips()
    # X = df.total_bill.values.reshape(-1, 1)
    df = make_pandas()
    X = df.valence.values.reshape(-1,1)

    model = LinearRegression()
    model.fit(X, df.energy)

    x_range = np.linspace(X.min(), X.max(), 100)
    y_range = model.predict(x_range.reshape(-1, 1))

    fig = px.scatter(df, x='valence', y='energy', opacity=0.65)
    fig.add_traces(go.Scatter(x=x_range, y=y_range, name='Regression Fit'))
    fig.show()



fig = px.scatter(make_pandas(), x="valence", y="energy",
                    hover_name="name",
                    log_x=True)
fig_regression()
app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
    
])
if __name__ == '__main__':
    app.run_server(debug=True)
