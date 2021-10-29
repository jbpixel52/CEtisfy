# %%

import spotipy
from spotipy.oauth2 import SpotifyOAuth
CLIENT_ID = '66da3fd147fb4433bf1a67a444f5d57e'
CLIENT_SECRET = '1ca107b9f0114b00a43e7a81c44630e9'
REDIRECT_URI = 'http://localhost:8080'
scope = "user-library-read"
def get_track(id):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                    client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope='user-top-read'))
    return sp.track(id)['name']