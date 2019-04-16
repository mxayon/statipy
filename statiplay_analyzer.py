import sys
import spotipy
import config
import json
import spotipy.util as util
import pandas as pd


def show(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        track_key = track['id']
        track_results = stp.track(track_key)
        album_key = track_results['album']['id']
        artist_feat = track_results['artists'][0]['name']
        artist_key = track_results['artists'][0]['id']
        track_name = track_results['name']
        explicit_bool = track_results['explicit']
        is_explicit = str(explicit_bool).lower()
        track_pop = track_results['popularity']
        album_name = track_results['album']['name']
        album_img = track_results['album']['images']
        album_date = track_results['album']['release_date']
        track_ids.append(track_key)
        album_ids.append(album_key)
        track_titles.append(track_name)
        artist_names.append(artist_feat)
        album_titles.append(album_name)
        track_popularity.append(track_pop)
        album_release.append(album_date)
        explicit_content.append(is_explicit)
    return


username = config.username
cid = config.client_id
cs = config.client_secret
uri = config.redirect_uri
scope = "user-library-read playlist-read-private playlist-read-collaborative"
token = util.prompt_for_user_token(username, scope, client_id=cid, client_secret=cs, redirect_uri=uri)

if __name__ == '__main__':
    playlist_ids = []
    track_ids = []
    album_ids = []
    artist_ids = []
    track_titles = []
    explicit_content = []
    track_popularity = []
    album_release = []
    artist_names = []
    album_titles = []
    if token:
        stp = spotipy.Spotify(auth=token)
        playlist = stp.user_playlists(username)
        print("Calling Spotify api...")
        print("Checking {}'s playlists".format(username))
        for playlist in playlist['items']:
            if playlist['owner']['id'] == username:
                playlist_key = playlist['id']
                results = stp.user_playlist(username, playlist_key, fields="tracks,next")
                tracks = results['tracks']
                show(tracks)
                print(playlist['name'])
                print("\t total tracks: ", playlist['tracks']['total'])
                while tracks['next']:
                    tracks = stp.next(tracks)
                    show(tracks)
                playlist_ids.append(playlist_key)
                print()
        print("Total Playlists Analyzed : {}".format(len(playlist_ids)))
        print("Total Songs Analyzed : {}".format(len(track_ids)))
        print("Released in {} different Albums".format(len(album_ids)))
        print()
        track_dict = {
        'Track': track_titles,
        'Explicit': explicit_content,
        'Tpopularity': track_popularity,
        'Artist': artist_names,
        'Album': album_titles,
        'Rdate': album_release
        }
        results_df = pd.DataFrame(track_dict, columns=['Track','Explicit', 'Tpopularity', 'Artist', 'Album', 'Rdate'])
        results_df.to_csv('statipy_results.csv')
        with open('track_ids.json', 'w') as outfile:
            json.dump(track_ids, outfile)
        with open('album_ids.json', 'w') as outfile:
            json.dump(album_ids, outfile)
        with open('artist_ids.json', 'w') as outfile:
            json.dump(artist_ids, outfile)
    else:
        print ("Can't get token for ", username)
