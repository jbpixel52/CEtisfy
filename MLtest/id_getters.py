# %%

"""GETTERS FOR THE IDs OF ALL OBJECTS by SPOTIFY LINK
    """
def get_playlists_id(url=input('Enter the spotify playlist link:')):
    link = url.replace('https://open.spotify.com/playlist/', '')
    return link.split('?')[0]


def get_album_id(url=input('Enter the spotify playlist link:')):
    link = url.replace('https://open.spotify.com/album/', '')
    return link.split('?')[0]


def get_track_id(url=input('Enter the spotify playlist link:')):
    link = url.replace('https://open.spotify.com/track/', '')
    return link.split('?')[0]


def get_track_id(url=input('Enter the spotify playlist link:')):
    link = url.replace('https://open.spotify.com/artist/', '')
    return link.split('?')[0]


def get_user_id(url=input('Enter the spotify playlist link:')):
    link = url.replace('https://open.spotify.com/user/', '')
    return link.split('?')[0]
