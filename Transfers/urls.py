"""
URL configuration for Transfers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
1. Add an import:  from other_app.views import Home
2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from mainAPP.views import *

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index),
    path('clubs/', clubs, name='clubs'),
    path('players/', players, name='players'),
    path('<str:country_name>/clubs/', country),
    path('u_20_players/', u_20_players, name='u-20'),
    path('seasons/', seasons, name='seasons'),
    path('<str:club_name>/players/', clubs_players, name='clubs_players'),
    path('transfers_record/', transfers_record),
    path('stats/', stats, name='stats'),
    path('latest_transfers/', latest_transfers, name='latest_transfers'),
    path('<str:mavsum>/mavsumlar/', mavsumlar, name='mavsumlar'),
    path('top_50_clubs/', top_50_clubs ),
    path('about/', about , name='about'),
    path('tryouts/', tryouts , name='tryouts'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



