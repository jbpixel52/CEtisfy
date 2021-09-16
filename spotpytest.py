# %%
from json.decoder import JSONDecodeError
import spotipy.util as util
import webbrowser
import json
import sys
import os
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint
import pandas
import matplotlib.pyplot as plt
CLIENT_ID = '66da3fd147fb4433bf1a67a444f5d57e'
CLIENT_SECRET = '1ca107b9f0114b00a43e7a81c44630e9'
REDIRECT_URI = 'http://localhost:8080'


scope = "user-library-read"

# USER ID: 12151542744

#pretty printer
pp = pprint.PrettyPrinter()
# SPOTIFY OBJECT  sp
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scope))

saved_songs = 0

def request_songs(loops,_offset):
    for batch in range(1):
        results = sp.current_user_saved_tracks(limit=10, offset=_offset*loops)
        for idx, item in enumerate(results['items']):
            track = item['track']
            print(idx, track['artists'][0]['name'], " – ", track['name'])
        saved_songs = results


def song_analysis(songs):
    data = []
    for item in dict(saved_songs['items']):
        track = item['track']
        analysis = sp.audio_features(track['id'])
        data.append()

    return data


def make_pandas():
    df = pandas.DataFrame(song_analysis(request_songs(1,100)))
    pp.pprint(df)

make_pandas()
# %%
