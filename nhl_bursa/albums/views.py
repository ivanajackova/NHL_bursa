from django.shortcuts import render, redirect
from .models import Card
from .forms import CardForm

def album_list(request):
    cards = Card.objects.filter(owner=request.user) if request.user.is_authenticated else []
    return render(request, 'albums/album_list.html', {'cards': cards})

#Definuje funkci (view), která zpracovává HTTP požadavek.Django ji zavolá, když uživatel navštíví určitou URL, například /albums/.
#tady ukládám fungujívi verzi na it

def add_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            card = form.save(commit=False)
            card.owner = request.user
            card.save()
            return redirect('album_list')
    else:
        form = CardForm()
    return render(request, 'albums/add_card.html', {'form': form})