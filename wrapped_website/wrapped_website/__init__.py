import os
import json

try:
    with open('../data/spotify_keys.json', 'r') as f:
              spotify_keys = json.load(f)
    os.environ["SPOTIPY_CLIENT_ID"] = spotify_keys["client_ID"]
    os.environ["SPOTIPY_CLIENT_SECRET"] = spotify_keys["client_secret"]
except FileNotFoundError:
    print("-----------------------------------------")
    print(os.getcwd())
    print("-----------------------------------------")