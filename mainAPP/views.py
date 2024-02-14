import datetime

from django.shortcuts import render
from .models import *

from datetime import  date

def index(request):
    return render(request, 'index.html')

def clubs(request):
    context={
        'clubs': Club.objects.order_by('-kapital').all()
    }
    return render(request, 'clubs.html', context)


def players(request):
    context={
        'players': Player.objects.order_by('-narx').all()
    }
    return render(request, 'players.html', context)

def country(request, country_name):
    context={
        'clubs': Club.objects.filter(davlat__nom__contains=country_name)
    }
    return render(request, 'country_clubs.html', context)


def u_20_players(request):
    hozirgi_sana = str(date.today())
    yil = int(hozirgi_sana[:4]) - 20
    yangi_sana=hozirgi_sana.replace(hozirgi_sana[:4], str(yil))
    context={
        'players': Player.objects.order_by('-narx').filter(t_yil__gt=yangi_sana)
    }
    return render(request, 'U-20 players.html' , context)


def seasons(request):
    mavsumlar = Transfer.objects.all().values_list('mavsum', flat=True)
    context = {
        'mavsumlar': sorted(mavsumlar)
    }
    return render(request, 'transfer-archive.html', context)


def clubs_players(request, club_name):
    context={
        'clubs': Club.objects.filter(nom=club_name),
        'players': Player.objects.order_by('-narx').filter(club__nom=club_name)
    }

    return render(request, 'clubs-players.html', context)


def transfers_record(request):
    context={
        'players': Transfer.objects.order_by('-narx').filter(narx__gte=50)[:100]
    }
    return render(request, 'transfer-records.html', context)

def stats(request):
    return render(request, 'stats.html')

def latest_transfers(request):
    hozirgi_sana = str(date.today())
    yil = hozirgi_sana[:4]
    context={
        'transfers': Transfer.objects.order_by('-narx').filter(mavsum__contains=yil)
    }
    return render(request, 'latest-transfers.html', context)



