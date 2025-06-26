from django.shortcuts import render, redirect, get_object_or_404
from .models import Card
from .forms import CardForm

def album_list(request):
    cards = Card.objects.filter(owner=request.user) if request.user.is_authenticated else []
    return render(request, 'albums/album_list.html', {'cards': cards})

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

def edit_card(request, card_id):
    card = get_object_or_404(Card, id=card_id, owner=request.user)
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES, instance=card)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = CardForm(instance=card)
    return render(request, 'albums/add_card.html', {'form': form})

def delete_card(request, card_id):
    card = get_object_or_404(Card, id=card_id, owner=request.user)
    card.delete()
    return redirect('album_list')

def toggle_sale(request, card_id):
    card = get_object_or_404(Card, id=card_id, owner=request.user)
    card.is_for_sale = not card.is_for_sale
    card.save()
    return redirect('album_list')
