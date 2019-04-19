# STATIPY
Python app using Spotipy wrapper for gathering data from the Spotify api to perform some exploratory data analysis &amp; visualizations of current users tracks and artists through their playlists.

The [SPOTIFY API](https://developer.spotify.com/documentation/web-api/) has some really good documentation on how to access their API, which uses node.js for their examples. This project uses the Spotipy wrapper, making all calls purely through python!

********

Purpose of this project is to run some Exploratory Data Analysis on your very own spotify playlist. So far I have managed to extract data on 991 songs added to the statipy_playlist database. Statipy saves it as a CSV file so each iteration of the statipy_analyzer.py code, it will create a new document, just dont forget to rename the document unless you want it to override previous data.

There is alot of data readily available in the spotify api, as well as other 'juicier' numerical data types although I prefer to study the playlist usage and see if I can make inferences about the music that has been saved.

Lucily me and my partner through commuting on bart and various occasions have amounted 991 tracks to analyze. For my purposes, I will factor in the repeated tracks as a measure of how much the tracks is liked and saved between both parties.

Future features may include usage of device ID endpoint, implementing album art covers through webbrowser, diving deeper with current date by pulling all popularities and all genres, and mapping out how artists are connected, specifically Nirvana and RuPaul.

*********

Visualizing the data gathered by Spotify user, allows us to make inferences on what user can do to improve Spotify experience based on data saved.

i. Installation:
##### import SPOTIPY
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


Once you have the environment variables set, run the Statipy app from your command line..
```
python Statipy.py [username]
```
> (Be careful not to push out keys or publish them up on github!)



1. Sign in to SPOTIFY (if you download the desktop app, theres more automagic things to perform - like grabbing device id and playing music remotely through  command line)

  Sign up to get credentials:
  <br>
  https://developer.spotify.com/


2. Make a Spotify developer account on the developer dashboard.
  If you dont have a Spotify account yet, make one. If Spotify is logged in on your Spotify desktop app it uses that sign in info.
3. Make an app and register to get key
  Give a brief description on Spotify, the developer dashboard gives you your app usage and traffic.

  *** IMPORTANT ***
  save your client id key and secret key on your computer to a file that will not be exposed on github or in the interwebs

4. Spotify api has a limit of 50, Ive reached my cap a couple of times, but resets the next day.

  A good thing to keep in mind, if you reach your daily limit, you get a connection error that the token has expired. You can check back on the developer page to see if you have reached the limit - in which case you can try the next day, or if you just need to update your permissions list it would be a quick way to find out.

5. Sign in with your developer credentials on the command line or add it to a file and import it to your .py file, (in this example, the statipy_analyzer.py - already imports from config.py). If you save it to a file, make sure you don't include this in any uploads or on Github pushes otherwise you would be exposing your keys.

#HideYourKeysHideYourWifi

## ... Get auth


You need to set your Spotify API credentials. You can do this by
setting environment variables like so:
<br>

```
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
```

> IMPORTANT: SPOTIPY_REDIRECT_URI='https://mxnkpl.com/'
  - just dont forget the " / " after url, allows spotify to redirect api request.


6. When you run Statipy, it saves your developer credentials entered in CLI into a username variable,

(if you run statipy_analyzer.py [username] by pulling this project on github, it will use username configuration that you have set up in config.py)

and the scope variable is defined when it runs this part of the code:

```
# Asks for permission to get current users playlists:

scope = "user-read-private user-read-email user-library-read playlist-read-private playlist-read-collaborative"
```

```
#Spotipy function that keeps you authorized saved into token variable:

token = util.prompt_for_user_token(username, scope)
```


7. Command line / IDE should now retrieve current users data.
> * Playlists - Name and Total tracks
> * Tracks - Song Info from each playlist
> * Artist - Artist Info from each track
> * Album - Album Info from each track




## Running statipy_analyzer.py

```
python statipy_analyzer.py [username]
```

Statipy analyzer will run in any package that contains:

```
__init__.py
and
config.py
```



in its folder.

* As step 5 states: you must create your own config.py file to run locally with same export syntax for CLI.


# Spotify object
Data available on spotify api:

Track   popularity   explicit       followers
Album   popularity   release_date   album_art
Artist  popularity   followers      genre
Audio Analysis

of current users saved, public, private and followed playlists.

The objective is to analyze the frequency of objects and find patterns in the saved data that could be used to improve playlist content and Spotify user experience.

#Playlist, Artists & Albums
**update**
As of 4/10 there are a total of 991 tracks.

Total Tracks : 971
Total Artists : 971
Total Playlists Analyzed : 19


#### Takeaways for statipy_analyzer

Indents matter -
  fixing functions and scope!


naming convention -
  plural S and singular
  " " vs ' '
  key vs id

#### Takeaways for Exploratory Data Analyis

Save time: Plan ahead, ask questions,
clean data frame and prepare data types early.

Have a clear divide and conquer plan before trying new things.
