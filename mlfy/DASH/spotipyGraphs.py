#%%
from numpy.core.fromnumeric import mean, size
import spotipy
import pandas
import numpy as np
import seaborn as sns
import  json
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

def make_pandas(dir):
    
    with open(dir) as f:
        songdata = json.load(f)
    df = pandas.DataFrame(songdata)
    return df

def regression():
    df = make_pandas('../playlists/Top Songs - USA Sep-27-2021.json')
    dfy=make_pandas('../playlists/Top Songs - Mexico Sep-27-2021.json')
    sns.lmplot(data=df, x="valence", y='energy',height=10,hue="artist")
        
def pairplot(df):
    plt.figure(dpi=300,facecolor='pink')
    sns.pairplot(df, hue="artist", palette='rainbow')

regression()
