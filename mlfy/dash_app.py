import dash
from dash import dcc
from dash import html
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output
from sklearn.cluster import KMeans

import k_means_analysis as kma


#import plotly.graph_objects as go
import plotly.express as px
 # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

K =kma.k_means_structure()

fig = px.scatter(data_frame=K.df_k_means.head(-1000),x="energy", y="us_popularity_estimate", color="cluster",
                size='us_popularity_estimate')
fig.show()

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=True)  # Turn off reloader if inside Jupyter

