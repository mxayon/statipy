# statipy
python app using spotipy wrapper for gathering data from the spotify api to perform some exploratory data analysis &amp; visualizations of current users tracks and artists

# get auth
sign up to get credentials:
<br>
https://developer.spotify.com/

sign in through CLI:
<br>
<br>
export SPOTIPY_CLIENT_ID='xxxxxxxx'
<br>
export SPOTIPY_CLIENT_SECRET='xxxxxxxxx'
<br>
export SPOTIPY_REDIRECT_URI='https://mxnkpl.com/'
<br>
* IMPORTANT: SPOTIPY_REDIRECT_URI='can be taco /'
  - just dont forget the " / " after; where spotify is going to redirect api request.

# import SPOTIPY
https://spotipy.readthedocs.io

# Spotify object

#Playlist, Artists & Albums


# Take Aways

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

save to a class?
