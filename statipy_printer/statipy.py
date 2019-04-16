import sys
import spotipy
import json
from json.decoder import JSONDecodeError
import spotipy.util as util

t_results = []
a_results = []
ab_results = []



def show(tracks):
    for i, item in enumerate(tracks['items']):
        """ prints through playlist tracks with # and appends to global """
        track = item['track']
        track_key = track['id']
        track_results = stp.track(track_key)
        artist_info = track_results['artists']
        artist_key = artist_info[0]['id']
        album_key = track_results['album']['id']
        album_name = track_results['album']['name']
        # adds to global variable
        t_results = t_results.append(track_key)
        # Appened to global here
        track_ids.append(track_key)
        artist_ids.append(artist_key)
        album_ids.append(album_key)
        # print("\t {} \t {} || {}".format(i, track['name'], track['artists'][0]['name']))


def show_track_artist(track_key):
    for item in range(len(track_ids)):
        track_key = track_ids[item]
        track_results = stp.track(track_key)
        artist_info = track_results['artists']
        album_key = track_results['album']['id']
        album_name = track_results['album']['name']
        artist_name = artist_info[0]['name']
        artist_key = artist_info[0]['id']
        # adds to global variable
        a_results = a_results.append(artist_info)
        print()
        print("Song: {} Popularity: {}".format(track_results['name'], track_results['popularity']))
        print("Contains explicit content?: {} Artist: {}".format(track_results['explicit'], artist_name))
        # print("Song Id: {} | Artist Id: {} ".format(track_results['id'], artist_key))
        # print("Album: {} | Album Id: {}".format(album_name, album_key))
        if album_name is None:
            print("--")
        print()

def show_artist(artist_key):
    for item in range(len(artist_ids)):
        artist_key = artist_ids[item]
        artist_results = stp.artist(artist_key)
        # print(json.dumps(artist_results, sort_keys=True, indent=4))
        artist_name = artist_results['name']
        artist_pop = artist_results['popularity']
        artist_ff = artist_results['followers']['total']
        artist_genre = artist_results['genres']
        # adds to global variable
        ab_results = ab_results.append(artist_results)
        # New data set
        print()
        print("\t {}".format(artist_name))
        print("Artist Popularity: {} Followers: {}".format(artist_pop, artist_ff))
        # Genre error handling:
        if len(artist_genre) >= 0:
            print("Genre: ")
            for x in range(len(artist_genre)):
                print(" \t {}".format(artist_genre[x]))
        elif artist_genre is None:
            print("* Unclassifiable *")
        else:
            print("---")
        print()
    print("***********************")
    print()

def show_album(album_key):
    for key in range(len(album_ids)):
        album_key = album_ids[key]
        album_results = stp.album(album_key)
        album_name = album_results['name']
        album_rd = album_results['release_date']
        album_tracks = album_results['total_tracks']
        # album_img = album_results['images']['url']
        # print(album_img)
        print("Album: {} Total Tracks: {} Released: {} ".format(album_name, album_tracks, album_rd) )


if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
        scope = "user-read-private user-read-email user-library-read playlist-read-private playlist-read-collaborative"
        print()
        print()
        print()
        print("** || Hello, * " + username + " * Welcome to STATIPY world! || **")
        print()
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
        playlist_ids = []
        count = 0
        # Loops through playlists
        print("Calling Spotify Api for Data...")
        print()
        print("Gathering Playlists to Analyze:")
        print()
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print( " >>> "  + playlist['name'])
                playlist_key = playlist['id']
                results = stp.user_playlist(username, playlist_key, fields="tracks,next")
                tracks = results['tracks']
                playlist_ids.append(playlist_key)
                show(tracks)
                print("\t total tracks:", playlist['tracks']['total'])
                # while tracks >> next
                while tracks['next']:
                    tracks = stp.next(tracks)
                    show(tracks)
                print()
                # Gathers data from tracks in playlists
        show_track_artist(track_ids)
        print("***********************")
        show_artist(artist_ids)
        show_album(album_ids)
        print()
        print("***********************")
        print("Total Tracks : {}".format(len(track_ids)))
        print("Total Artists : {}".format(len(artist_ids)))
        print("Total Playlists Analyzed : {}".format(len(playlist_ids)))
    else:
        print("Token not cool. Auth Required.")


# Backpocket : JSON data
# print(json.dumps(VARIABLE, sort_keys=True, indent=4))
