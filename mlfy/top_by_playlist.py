# %%
import json
from datetime import date
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import id_getters

CLIENT_ID = '66da3fd147fb4433bf1a67a444f5d57e'
CLIENT_SECRET = '1ca107b9f0114b00a43e7a81c44630e9'
REDIRECT_URI = 'http://localhost:8080'
TODAY = date.today()

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI))


def request_playlist(id, _limit, loops):
    songdata = []

    for batch in range(loops):
        results = sp.playlist_tracks(id, limit=50)

        for i in range(_limit):
            song_id = results['items'][i]['track']['id']
            feats = sp.audio_features(song_id)
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


def make_countries_json():
    with open('./playlists/links.json', "r") as file:
        links = json.load(file)
    for key in links['weeklies']:
        value=links['weeklies'][key]
        print(key," -> ",value)
        playlist_id = id_getters.get_playlists_id(value)
        songdata_json(playlist_id, request_playlist(playlist_id, 50, 1))

def songdata_json(id, data):
    filename = './playlists/'+str(get_playlist_name(id))+" "+TODAY.strftime("%b-%d-%Y")+'.json'
    print(filename)
    with open(filename, "w") as file:
        json.dump(data, file)


def main():
    make_countries_json()


main()
# %%
