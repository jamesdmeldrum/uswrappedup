import os
import json
from .settings import STATIC_ROOT

file_path = os.path.join(STATIC_ROOT, 'data/spotify_keys.json')

with open(file_path, 'r') as f:
    spotify_keys = json.load(f)
os.environ["SPOTIPY_CLIENT_ID"] = spotify_keys["client_ID"]
os.environ["SPOTIPY_CLIENT_SECRET"] = spotify_keys["client_secret"]