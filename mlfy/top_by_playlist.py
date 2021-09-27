# %%
import json
from json.decoder import JSONDecodeError

import numpy as np
import spotipy
import spotipy.util as util
from sklearn.feature_extraction.text import CountVectorizer
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

import id_getters

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


def request_playlist(id, _limit, loops):
    songdata = []

    for batch in range(loops):
        results = sp.playlist_tracks(id, limit=50)
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


def get_playlist_name(id):
    return (sp.playlist(id)['name'])


def songdata_json(id, data):
    filename = './playlists/'+str(get_playlist_name(id))+'.json'
    print(filename)
    with open(filename, "w") as file:
        json.dump(data, file)


def main():
    playlist_id = id_getters.get_playlists_id()
    songdata_json(playlist_id, request_playlist(playlist_id, 50, 1))


main()
# %%
