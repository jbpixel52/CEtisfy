# %%
import json
from json.decoder import JSONDecodeError

import numpy as np
import spotipy
import spotipy.util as util
from sklearn.feature_extraction.text import CountVectorizer
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

CLIENT_ID = '66da3fd147fb4433bf1a67a444f5d57e'
CLIENT_SECRET = '1ca107b9f0114b00a43e7a81c44630e9'
REDIRECT_URI = 'http://localhost:8080'
scope = "user-library-read"

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

def songdata_json(data):
    with open("songdata.json", "w") as write_file:
     json.dump(data, write_file)

songdata_json(request_songs(50,120))

# %%
