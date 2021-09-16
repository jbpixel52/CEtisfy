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

# SPOTIFY OBJECT  sp
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=scope))
pp=pprint.PrettyPrinter()
saved_songs=0
for batch in range(1):
    results = sp.current_user_saved_tracks(limit=20,offset=batch*50)
    for idx, item in enumerate(results['items']):
        track = item['track']
        #print(idx, track['artists'][0]['name'], " – ", track['name'])
    saved_songs =results

for idx, item in enumerate(saved_songs['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'],track['id'])
print('\n')       
analysed_song= sp.audio_features("6NVB6W7G3svCKe5zB7kY8q")
pp.pprint(analysed_song)

def song_analysis():
    data = []
    for idx, item in enumerate(saved_songs['items']):
        track = item['track']
        analysis = sp.audio_features(track['id'])
        data.append(analysis)
        stringdata = str(track["artists"][0]['name'],str(' - '),str(track['name']))
        metadata=[]
        metadata.append(stringdata)        
        
        return [data,metadata]
        
dataset = song_analysis()
df =pandas.DataFrame(dataset)
# %%
