import sys
import spotipy
import json
from json.decoder import JSONDecodeError
import spotipy.util as util

def show(tracks):
    for i, item in enumerate(tracks['items']):
        """ prints through playlist tracks with # and appends to global """
        track = item['track']
        track_key = track['id']
        track_results = stp.track(track_key)
        artist_info = track_results['artists']
        artist_key = artist_info[0]['id']
        track_ids.append(track_key)
        artist_ids.append(artist_key)
        print("\t {} \t {} || {}".format(i, track['name'], track['artists'][0]['name']))
    print()

def show_track_artist():
    for item in range(len(track_ids)):
        track_key = track_ids[item]
        track_results = stp.track(track_key)
        print("Song: {} | {}  |".format(track_results['name'], track_results['id']))
        print("Song popularity: {} Contains explicit content? {}".format(track_results['popularity'], track_results['explicit']))
        artist_info = track_results['artists']
        artist_name = artist_info[0]['name']
        artist_key = artist_info[0]['id']
        print("Artist: {} | {}  |".format(artist_name, artist_key))
        artist_results = stp.artist(artist_key)
        # print(json.dumps(artist_results, sort_keys=True, indent=4))
        artist_pop = artist_results['popularity']
        artist_ff = artist_results['followers']['total']
        print("Artist Popularity: {} | Followers: {} |".format(artist_pop, artist_ff))
        print()
    print("***********************")
    print()
if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
        scope = "user-read-private user-read-email user-library-read playlist-read-private playlist-read-collaborative"
        print()
        print()
        print("** || Hello, * " + username + " * Welcome to STATIPY world! || **")
        print()
        print()
    else:
        print("ALERT - NOT AUTHORIZED")
        print("usage: python user_playlists.py [username]")
        sys.exit()

    # Statipy object call | auth
    token = util.prompt_for_user_token(username, scope)

    if token:
        # Creates Spotify obj
        stp = spotipy.Spotify(auth=token)
        # Gets current users playlists
        playlists = stp.user_playlists(username)
        # Ready Set.. Global Variablles!
        track_ids = []
        artist_ids = []
        album_ids = []
        # Loops through playlists
        print("Playlists to Analyze:")
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print( " >> "  + playlist['name'])
                print("\t total tracks", playlist['tracks']['total'])
                results = stp.user_playlist(username, playlist['id'], fields="tracks,next")
                tracks = results['tracks']
                show(tracks)

            # while tracks >> next
                while tracks['next']:
                    tracks = stp.next(tracks)
                    show(tracks)
        # gathers data from tracks in playlists
                show_track_artist()

        print("***********************")
        print("Total Tracks : {}".format(len(track_ids)))
        print("Total Artists : {}".format(len(artist_ids)))
        print("Total Playlists Analyzed : {}".format(len(playlists)))
    else:
        print("Token not cool. Auth Required.")


# Backpocket : JSON data
# print(json.dumps(VARIABLE, sort_keys=True, indent=4))
