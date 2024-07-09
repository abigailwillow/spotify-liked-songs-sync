import spotipy
import dotenv
import os

from spotipy.oauth2 import SpotifyOAuth

dotenv.load_dotenv()

auth = SpotifyOAuth(scope='user-library-read playlist-modify-private playlist-modify-public')

print(f'Authorization URL: {auth.get_authorize_url()}')

spotify = spotipy.Spotify(auth_manager=auth)

playlist = spotify.playlist(os.getenv('PLAYLIST_ID'))

spotify.playlist_replace_items(playlist['id'], [])

saved_tracks = spotify.current_user_saved_tracks(limit=50)

while True:
    track_ids = [track['track']['id'] for track in saved_tracks['items']]
    spotify.playlist_add_items(playlist['id'], track_ids)
    print(f'Added {saved_tracks["offset"] + len(saved_tracks["items"])} liked songs to \'{playlist["name"]}\'')

    if saved_tracks['next']:
        saved_tracks = spotify.next(saved_tracks)
    else:
        break
