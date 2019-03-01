# STATIPY
Python app using Spotipy wrapper for gathering data from the Spotify api to perform some exploratory data analysis &amp; visualizations of current users tracks and artists through their playlists.

The [SPOTIFY API](https://developer.spotify.com/documentation/web-api/) has some really good documentation on how to access their API, which uses node.js for their examples. This project uses the Spotipy wrapper, making all calls purely through python!

1. Sign in to SPOTIFY (if you download the desktop app, theres more automagic things to perform - like grabbing device id and playing music remotely through command line)
2. Make a [spotify developer account](https://developer.spotify.com/)
3. Make an app and register to get key
4. Spotify api has a limit of 50, Ive reached my cap a couple of times, specifically when I needed to present this. It just means you need to wait another day. (hopefully this is clean enough that you wont have to.)
5. Sign in with your developer credentials on the command line (more below...)
6. When you run statipy, it saves your developer credentials in a username variable, and the scope variable is defined when it runs this part of the code:

```
#Asking for permission to get current users playlists:

scope = "user-read-private user-read-email user-library-read playlist-read-private playlist-read-collaborative"
```

```
#Spotipy function that keeps you authorized saved into token variable:

token = util.prompt_for_user_token(username, scope)
```


7. Command line should now retrieve current users data.
> * Playlists - Name and Total tracks
> * Tracks - Song Info from each playlist
> * Artist - Artist Info from each track
> * Album - Album Info from each track




Purpose of this project is to run some Exploratory Data Analysis on your very own spotify playlist. So far I have managed to extract data on 870+ songs in one run and only reaches its limit if ran too many times.



## import SPOTIPY

```
pip install spotipy

```

Incase any errors occur after pip install - try forcing the upgrade from the github repo -

```
pip install git+https://github.com/plamere/spotipy.git --upgrade
```

Check out:
[spotipy on github](https://github.com/plamere/spotipy)

or

https://spotipy.readthedocs.io


## ... Get auth

Sign up to get credentials:
<br>
https://developer.spotify.com/

You need to set your Spotify API credentials. You can do this by
setting environment variables like so:
<br>

```
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
```

> IMPORTANT: SPOTIPY_REDIRECT_URI='https://mxnkpl.com/'
  - just dont forget the " / " after; where spotify is going to redirect api request.

Once you have the environment variables set, run the Statipy app from your command line..

```
python statipy.py
```

> (Be careful not to push out keys or publish them up on github!)

# Spotify object

#Playlist, Artists & Albums


# Takeaways

Indents matter -
  fixing functions and scope!

digging in to nested data -

```
  [0]['followers']['total']
```

naming convention -
  plural S and singular
  " " vs ' '
  key vs id
