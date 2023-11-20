import os
import json
import settings

file_path = os.path.join(settings.STATIC_ROOT, 'data/spotify_keys.json')

with open(file_path, 'r') as f:
    spotify_keys = json.load(f)
os.environ["SPOTIPY_CLIENT_ID"] = spotify_keys["client_ID"]
os.environ["SPOTIPY_CLIENT_SECRET"] = spotify_keys["client_secret"]