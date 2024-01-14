from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import redirect 

def index(request):
    games = Games.objects.all()
    return render(request, "index.html", {"games": games})

def gamepage(request,id):
    developers = Developers.objects.get(pk = int(id))
    games = Games.objects.get(pk = int(id))
    steam_games = Steam_games.objects.get(pk = int(id))
    egs_games = Egs_games.objects.get(pk = int(id))
    return render(request, "gamepage.html", {"developers": developers, "games": games, "steam_games": steam_games,"egs_games": egs_games})
 
def redirect_view(request): 
    response = redirect('/menu/') 
    return response
 


