import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials 
import pandas as pd 
import spotipy.util as util

# https://github.com/NikLinnane/Spotify-API/blob/main/Spotipy%20API%20Data%20Pull.ipynb
# https://towardsdatascience.com/extracting-song-data-from-the-spotify-api-using-python-b1e79388d50
# get personal data - https://medium.com/@rafaelnduarte/how-to-retrieve-data-from-spotify-110c859ab304


# auth 
cid = ""
secret = ""
username = ""
scope = "user-library-read"
authorization_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"
redirect_uri = "https://localhost.com/callback/"

token = util.prompt_for_user_token(username,scope,client_id='client_id_number',client_secret='client_secret',redirect_uri='https://localhost.com/callback/')
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

client_credentials_manager = SpotifyClientCredentials(client_id = cid, client_secret=secret)

sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

token = client_credentials_manager.get_access_token()
spotify = spotipy.Spotify(auth=token)
print(token)
print(spotify)

def get_personalData(range, type, artist_name, track_name):

def get_audio_feature():


def get_playlist(creator_id, playlist_url, limit, offset):
	# create an empty list and an empty df
    playlist_features_list = ['artist', 'album', 'track_name', 'track_id', 'danceability', 'energy', 'key', 'loudness', 'mode', 
                              'speechiness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms', 'time_signature', 'acousticness']
    playlist_df = pd.DataFrame(columns = playlist_features_list)

# loop through the specified playlist and extract wanted features
    playlist = sp.user_playlist_tracks(creator_id, playlist_url, limit=limit, offset=offset)["items"]
    for track in playlist:

        # create empty dict
        playlist_features = {}

 
	playlist_features['artist'] = track['track']['album']['artists'][0]['name']
	playlist_features['album'] = track['track']['album']['name']
	playlist_features['track_name'] = track['track']['name']
	playlist_features['track_id'] = track['track']['id']
	playlist_features["explicit"] = track["track"]["explicit"]
        playlist_features["popularity"] = track["track"]["popularity"]
        playlist_features["album_release_date"] = track["track"]["album"]["release_date"]
        playlist_features["duration_ms"] = track["track"]["duration_ms"]
        playlist_features['added_by'] = track["added_by"]["id"]
        playlist_features['added_at'] = track["added_at"]
	
	# get audio features 
	audio_features = sp.audio_features(playlist_features["track_id"])[0]
        for feature in playlist_features_list[4:]:
            playlist_features[feature] = audio_features[feature]
        
        # concat dfs
        track_df = pd.DataFrame(playlist_features, index = [0])
        playlist_df = pd.concat([playlist_df, track_df], ignore_index = True)

    # return df
    return playlist_df

