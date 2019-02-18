import sys
import spotipy
import json
from json.decoder import JSONDecodeError
import spotipy.util as util

class Discogs:
    def __init__(self, album, artist):
        self.album = album
        self.artist = artist


if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
        scope = "user-read-private user-read-email user-top-read user-library-read"
