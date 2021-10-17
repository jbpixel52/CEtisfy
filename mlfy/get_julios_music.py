# %%
import collections
import json
import os
import pprint
import sys
import webbrowser
from json.decoder import JSONDecodeError
import seaborn as sns
import matplotlib.pyplot as plt
import pandas
import simplejson
import spotipy
import spotipy.util as util
import yaml
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import random
randomint= (random.randint(0,10000))
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


for batch in range(loops):
    results = splibrary.current_user_saved_tracks(limit=_limit, offset=_offset)
    data.append(results['items'])
    
    
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)