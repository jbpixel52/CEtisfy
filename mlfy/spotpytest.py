# %%
import pprint
import random
from json.decoder import JSONDecodeError

import matplotlib.pyplot as plt
import numpy as np
import pandas
import seaborn as sns
import sklearn as sk
import sklearn.compose
import sklearn.decomposition
import sklearn.linear_model
import sklearn.metrics
import sklearn.pipeline
import sklearn.preprocessing
import spotipy
import spotipy.util as util
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from sklearn_pandas import DataFrameMapper
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

randomint = (random.randint(0, 10000))
CLIENT_ID = '66da3fd147fb4433bf1a67a444f5d57e'
CLIENT_SECRET = '1ca107b9f0114b00a43e7a81c44630e9'
REDIRECT_URI = 'http://localhost:8080'


scope = "user-library-read"

# USER ID: 12151542744

# pretty printer
pp = pprint.PrettyPrinter()
# SPOTIFY OBJECT  sp
splibrary = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                      client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scope))

sptop = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                  client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope='user-top-read'))


def request_songs(_limit, loops):
    songdata = []

    for batch in range(loops):
        results = splibrary.current_user_saved_tracks(
            limit=_limit, offset=batch*_limit)
        for i in range(_limit):
            song_id = results['items'][i]['track']['id']
            feats = splibrary.audio_features(song_id)
            energy = feats[0]['energy']
            valence = feats[0]['valence']
            tempo = feats[0]['tempo']
            lenght = feats[0]['duration_ms']

            songdata.append({'name': results['items'][i]['track']['name'], 'artist': results['items']
                            [i]['track']['artists'][0]['name'], 'id': results['items'][i]['track']['id'], 'energy': energy, 'valence': valence, 'tempo': tempo, 'lenght': lenght})
        print('## LOOP:', batch)

    return songdata


def user_top_artists():
    scope = 'user-top-read'
    results = sptop.current_user_top_tracks(limit=10, time_range="medium_term")


def make_pandas(arg):
    df = pandas.DataFrame(arg)
    pp.pprint(df)

    dfcopy = df.squeeze()

    return df


def make_dataframe(df):
    plt.figure(figsize=(10, 10))
    ax = sns.scatterplot(data=df, x='tempo', y='energy', hue='artist',
                         palette='rainbow', size='lenght', sizes=(50, 1000), alpha=0.6)
    h, labs = ax.get_legend_handles_labels()
    ax.legend(h[1:20], labs[1:20], loc='best', title='artists')


def pairplot(df):
    plt.figure(figsize=(10, 10))
    sns.pairplot(df, hue="artist", palette='rainbow')


def regplot(df):
    plt.figure(figsize=(10, 10))
    sns.regplot(data=df, x='valence', y='tempo')


def main():
    loops = input('loops to do:')
    make_dataframe(make_pandas(request_songs(50, int(loops))))
    pairplot(make_pandas(request_songs(50, int(loops))))
    regplot(make_pandas(request_songs(50, int(loops))))


main()
# %%
