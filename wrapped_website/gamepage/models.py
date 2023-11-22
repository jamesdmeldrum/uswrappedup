from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json, re
from django.urls import reverse
import random, os
from .settings import STATIC_ROOT

file_path = os.path.join(STATIC_ROOT, 'data/song-data.json')

def random_pwd():
    possible_chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890")

    pwd = ""

    while len(pwd) < 6:
        ind = random.randint(0, len(possible_chars)-1)
        char = possible_chars[ind]
        pwd += char

    return pwd


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    passcode = models.CharField(max_length=6, default=random_pwd())
    title = models.CharField(max_length=40)
    date_created = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    reveal = models.BooleanField(default=True)

    def toggle_reveal(self):
        if self.reveal:
            self.reveal = False
        else:
            self.reveal = True

    def get_reveal(self):
        return self.reveal

    def tracks(self):
        return [track for track in Track.objects.filter(game=self)]

    def tracks_alphabetical(self):
        tracks = [track for track in Track.objects.filter(game=self)]
        tracks2 = sorted(tracks, key=lambda x: str(x.person))
        return tracks2

    def num_tracks(self):
        return len(self.tracks())

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('game-invite', kwargs={'passcode': self.passcode})


class Track(models.Model):
    title = models.TextField(max_length=150)
    person = models.TextField(max_length=30)
    link = models.TextField(max_length=250)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def convert_to_uri(self):
        x = str(self.link)
        x = re.split('[ /:.?]', x)
        song_id = ""
        i = 0
        while i < 100 and i < len(x):
            segment = x[i]
            if segment == "track":
                song_id = x[i+1]
                break
            i += 1
        if i == 100 or i == len(x):
            self.link = "spotify:track:4PTG3Z6ehGkBFwjybzWkR8"
        else:
            self.link = "spotify:track:" + song_id
        print(self.link)
        self.save()

    def getsongdata(self):
        try:
            with open(file_path, 'r') as f:
                results = json.load(f)[self.link]
        except KeyError:
            self.convert_to_uri()
            results = spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
            results = spotify.track(self.link)
            output_dict = {self.link: results}
            with open(file_path, 'r') as f:
                song_data = json.load(f)
            song_data[str(self.link)] = results
            with open(file_path, 'w') as f:
                json.dump(song_data, f)
            if self.link != "spotify:track:4PTG3Z6ehGkBFwjybzWkR8":
                self.title = results['name']
            self.person = str(self.person).upper()
            self.save()

        return results

    def embedlink(self):
        results = self.getsongdata()
        try:
            return results['preview_url'].split("?")[0]
        except AttributeError:
            return results['preview_url']

    def getimage(self):
        results = self.getsongdata()
        imagelink = results['album']['images'][0]['url']
        return imagelink

    def getartist(self):
        results = self.getsongdata()
        return results['album']['artists'][0]['name']

    def __str__(self):
        return self.title
