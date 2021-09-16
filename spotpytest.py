# %%
import collections
import json
import os
import pprint
import sys
import webbrowser
from json.decoder import JSONDecodeError

import matplotlib.pyplot as plt
import pandas
import simplejson
import spotipy
import spotipy.util as util
import yaml
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

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


def request_songs(loops, _offset):
    for batch in range(1):
        results = splibrary.current_user_saved_tracks(
            limit=10, offset=_offset*loops)
        for idx, item in enumerate(results['items']):
            track = item['track']
            #print(idx, track['artists'][0]['name'], " – ", track['name'])

        songs = results['items']

        return songs


def user_top_artists():
    scope = 'user-top-read'
    results = sptop.current_user_top_tracks(limit=10, time_range="medium_term")

    with open('top_artists.txt', 'w') as outfile:
        json.dump(results, outfile)


def make_pandas(arg):
    df = pandas.DataFrame(arg)
    pp.pprint(df)


type(request_songs(2, 500))
user_top_artists()

# %%
