import os
import json

with open('./data/spotify_keys.json', 'r') as f:
          spotify_keys = json.load(f)
os.environ["SPOTIPY_CLIENT_ID"] = spotify_keys["client_ID"]
os.environ["SPOTIPY_CLIENT_SECRET"] = spotify_keys["client_secret"]