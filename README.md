# STATIPY
Python app using Spotipy wrapper for gathering data from the Spotify api to perform some exploratory data analysis &amp; visualizations of current users tracks and artists through their playlists

# Import Spotipy

# Get auth

sign up to get credentials:
<br>
https://developer.spotify.com/

You need to set your Spotify API credentials. You can do this by
setting environment variables like so:
<br>

'''
export SPOTIPY_CLIENT_ID='your-spotify-client-id'


export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'


export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
'''


* IMPORTANT: SPOTIPY_REDIRECT_URI='can be taco /'
  - just dont forget the " / " after; where spotify is going to redirect api request.

# import SPOTIPY
https://spotipy.readthedocs.io

# Spotify object

#Playlist, Artists & Albums


# Takeaways

Indents matter -
  fixing functions and scope!

digging in to nested data -
  [0]['followers']['total']

error handling -
  if data is not there ..

naming convention -
  plural S and singular
  " " vs ' '
  key vs id

use notes to break code into readable segments
  label where things are initialized but keep pattern clear

things I looked up / reviewed
  FOR LOOP - particulary range(len(x))
  enumerate


if __name__ == '__main__':
