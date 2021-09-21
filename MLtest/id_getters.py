# %%

"""GETTERS FOR THE IDs OF ALL OBJECTS by SPOTIFY LINK
    """
def get_playlists_id(url=input('Enter the spotify playlist link:')):
    return url.replace('https://open.spotify.com/playlist/', '').split('?')[0]

def get_album_id(url=input('Enter the spotify ALBUM link:')):
    return url.replace('https://open.spotify.com/album/', '').split('?')[0]


def get_track_id(url=input('Enter the spotify TRACK link:')):
    return url.replace('https://open.spotify.com/track/', '').split('?')[0]


def get_track_id(url=input('Enter the spotify ARTIST link:')):
    return url.replace('https://open.spotify.com/artist/', '').split('?')[0]


def get_user_id(url=input('Enter the spotify user ID link:')):
    return url.replace('https://open.spotify.com/user/', '').split('?')[0]

get_playlists_id()