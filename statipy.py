import sys
import spotipy
import json
from json.decoder import JSONDecodeError
import spotipy.util as util

class Discogs:
    def __init__(self, album, artist):
        self.album = album
        self.artist = artist

class Statipyo:
    def __init__(self, song, artist, album):
        self.song = song
        self.artist = artist
        self.album = album

if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
        scope = "user-read-private user-read-email user-top-read user-library-read"
        print("|| Hello," + username + " STATIPY world! || ")
    else:
        print("ALERT - NOT AUTHORIZED")
        print("usage: python user_playlists.py [username]")
        sys.exit()

    token = util.prompt_for_user_token(username, scope)
    if token:
        # Creates Spotify obj
        stpy = spotipy.Spotify(auth=token)
        # Gets current users playlists
        playlists = stpy.user_playlists(username)

        song_ids = []
        artists_ids = []
        album_ids = []

        # Loops through playlists
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print(playlist['name'])
                print("   total tracks", playlist['tracks']['total'])
                results = stpy.user_playlist(username, playlist['id'],
                                    fields="tracks,next")
                tracks = results['tracks']
                print()
                print()
                print(json.dumps(tracks, sort_keys=True, indent=4))

    else:
        print("Token not cool. Auth Required.")


# Backpocket : JSON data
# print(json.dumps(VARIABLE, sort_keys=True, indent=4))
