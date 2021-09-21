#%%
import spotipy
import pandas
import numpy as np
import seaborn as sns
import  json
import matplotlib.pyplot as plt


def make_pandas():
    
    with open('./songdata.json') as f:
        songdata = json.load(f)
        
    df = pandas.DataFrame(songdata)
    #pp.pprint(df)
    dfcopy = df.squeeze()
    #pp.pprint(dfcopy)
    return df


def pairplot(df):
    plt.figure(dpi=300,facecolor='pink')
    sns.pairplot(df, hue="artist", palette='rainbow')

