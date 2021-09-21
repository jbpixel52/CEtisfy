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
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI))
sp.playlist_tracks
'https://open.spotify.com/playlist/37i9dQZF1DXb67OkZ6150Z?si=eab738d5c8664fe6'
'https://open.spotify.com/playlist/37i9dQZF1E39FY3NZiWu6C?si=9655e338661d4644'
def get_id(link):
    url = str(link)
    url.find('?si')
    url.find('playlist/')
    url.replace('https://open.spotify.com/playlist/','')
def request_songs(_limit, loops):
    songdata = []

    for batch in range(loops):
        results = sp.playlist_tracks(id)
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

    with open("topxplaylist.json", "w") as write_file:
        json.dump(data, write_file)


songdata_json(request_songs(50, 1))

# %%
