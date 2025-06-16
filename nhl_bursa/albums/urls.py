from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
]

#Vytváří ,seznam URL pravidel, které Django použije,Prázdná cesta – tedy základní URL (např. /albums/),Funkce ve views.py, která zpracuje požadavek,Název této cesty – lze použít v šablonách pro url 'album_list'