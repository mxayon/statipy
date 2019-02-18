import sys
import spotipy
import json
from json.decoder import JSONDecodeError
import spotipy.util as util

class Discogs:
    def __init__(self, album, artist):
        self.album = album
        self.artist = artist

def show(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        track_key = track['id']
        track_results = stp.track(track_key)
        track_ids.append(track_key)
        print( " {} {} {}".format(i, track['artists'][0]['name'], track['name']))


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
    stp = spotipy.Spotify(auth=token)


    track_ids = []
    artists_ids = []
    album_ids = []
    ready = 0


    if token:
        # Creates Spotify obj
        # Gets current users playlists
        playlists = stp.user_playlists(username)
        # Set.. Go!
        # Loops through playlists
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print(playlist['name'])
                print("   total tracks", playlist['tracks']['total'])
                results = stp.user_playlist(username, playlist['id'], fields="tracks,next")
                tracks = results['tracks']
                print()
                print()

                show(tracks)
    else:
        print("Token not cool. Auth Required.")


# Backpocket : JSON data
# print(json.dumps(VARIABLE, sort_keys=True, indent=4))
