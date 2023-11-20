from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Game, Track
from .forms import PlayForm, AddTrackForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import spotipy


# Create your views here.
def home(request):
    return render(request, 'gamepage/home.html')


def create(request):
    return render(request, 'gamepage/create.html')


class GameListView(ListView):
    model = Game
    template_name = 'gamepage/play.html'
    context_object_name = 'games'
    ordering = ['-date_created']


def GameList(request):
    context = {}
    form = PlayForm()
    games = Game.objects.all()
    context["games"] = games
    context["form"] = form

    if request.method == "POST":
            print(request)
            # create a form instance and populate it with data from the request:
            form = PlayForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                game = Game.objects.filter(passcode=form.data.get('passcode')).first()
                if game:
                    return HttpResponseRedirect("/play/%s" % str(game.passcode))

    return render(request, 'gamepage/play.html', context)


def GamePlay(request, passcode):
    context = {}
    game = Game.objects.filter(passcode=passcode).first()
    context["object"] = game
    return render(request, 'gamepage/game_play.html', context)


class GameDetailView(DetailView):
    model = Game
    template_name = 'gamepage/game_play.html'


def AddTrack(request, passcode):
    context = {}
    form = AddTrackForm()
    game = Game.objects.filter(passcode=passcode).first()
    if not game:
        return render(request, 'gamepage/home.html')

    context["form"] = form

    if request.method == "POST":
            print(request)
            # create a form instance and populate it with data from the request:
            form = AddTrackForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                print(form)
                form.instance.game = game
                form.instance.title = "Pending"
                form.save()

    elif request.method == "GET":
        return render(request, 'gamepage/add_track.html', context)

    context = {}
    form = PlayForm()
    games = Game.objects.all()
    context["games"] = games
    context["form"] = form
    return render(request, 'gamepage/play.html', context)


def add(request):
    context = {}
    form = PlayForm()
    context["form"] = form

    if request.method == "POST":
        form = PlayForm(request.POST)
        # check whether it's valid:
        game = Game.objects.filter(passcode=form.data.get('passcode')).first()
        if game:
            return HttpResponseRedirect("/add/%s" % str(game.passcode))

    return render(request, 'gamepage/add.html', context)


def invite(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'gamepage/invite.html', context)


class CreateGame(CreateView):
    model = Game
    template_name = 'gamepage/create.html'
    fields = ['title', 'passcode']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


def invite_game(request, passcode):
    context = {}
    form = AddTrackForm()
    game = Game.objects.filter(passcode=passcode).first()
    if not game:
        return render(request, 'gamepage/home.html')

    context['object'] = game
    return render(request, 'gamepage/invite_links.html', context)