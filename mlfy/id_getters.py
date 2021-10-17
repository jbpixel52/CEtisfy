# %%

"""GETTERS FOR THE IDs OF ALL OBJECTS by SPOTIFY LINK
    """
def get_playlists_id(url):
    return url.replace('https://open.spotify.com/playlist/', '').split('?')[0]


def get_album_id(url):
    return url.replace('https://open.spotify.com/album/', '').split('?')[0]


def get_track_id(url):
    return url.replace('https://open.spotify.com/track/', '').split('?')[0]


def get_artist_id(url):
    return url.replace('https://open.spotify.com/artist/', '').split('?')[0]


def get_user_id(url):
    return url.replace('https://open.spotify.com/user/', '').split('?')[0]

