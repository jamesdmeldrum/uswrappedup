from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gamepage-home'),
    path('create/', views.CreateGame.as_view(), name='gamepage-create'),
    path('play/', views.GameList, name='gamepage-play'),
    path('play/<passcode>', views.GamePlay, name='game-detail'),
    path('add/<passcode>', views.AddTrack, name='add-track'),
    path('add/', views.add, name='add-unknown'),
    path('invite/', views.invite, name='gamepage-invite'),
    path('invite/<passcode>', views.invite_game, name='game-invite'),
]

