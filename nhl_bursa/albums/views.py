from django.shortcuts import render
from .models import Card

def album_list(request):
    cards = Card.objects.filter(owner=request.user) if request.user.is_authenticated else []
    return render(request, 'albums/album_list.html', {'cards': cards})

#Definuje funkci (view), která zpracovává HTTP požadavek.Django ji zavolá, když uživatel navštíví určitou URL, například /albums/.
#tady ukládám fungujívi verzi na it