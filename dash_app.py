# %%
import plotly.express as px
import dash
from dash import dcc
from dash import html
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output
from sklearn.cluster import KMeans

import k_means_analysis as kma

setpath = 'tf_mini.csv'
countrypath = 'playlists/Top Songs - Global Oct-26-2021.json'

#import plotly.graph_objects as go
# or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

K = kma.k_means_structure(setpath, countrypath)


all_dims = [
    'energy', 'valence', 'tempo', 'duration', 'danceability', 'key', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness']

# fig = px.scatter(data_frame=K.fullframe, x="duration",
#                  y='valence', color='cluster', size='set',trendline='ols', template="plotly_dark")
# fig2 = px.scatter(data_frame=K.fullframe, x="duration",
#                   y='energy', color='cluster', size='set',trendline='ols', template="plotly_dark")

app = dash.Dash()
app.layout = html.Div([
    dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x}
                 for x in all_dims],
        value=all_dims[:2],
        multi=True
    ),
    dcc.Graph(id="splom"),
])

@app.callback(
    Output("splom", "figure"), 
    [Input("dropdown", "value")])
def update_bar_chart(dims):
    fig = px.scatter_matrix(data_frame=K.fullframe,dimensions=dims , color='cluster', size='set',template="plotly_dark")
    return fig


# Turn off reloader if inside Jupyter
app.run_server(debug=True, use_reloader=True)
