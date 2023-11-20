from django import forms
from .models import Game, Track


class PlayForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['passcode']


class AddTrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ["person", "link"]