from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html')

def clubs(request):
    context={
        'clubs': Club.objects.all()
    }
    return render(request, 'clubs.html', context)


def players(request):
    context={
        'players': Player.objects.all()
    }
    return render(request, 'players.html', context)

# def countries(request, pk):
#     context={
#         'country':
#     }






