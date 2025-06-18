from django.shortcuts import render
from .models import Card  # pokud máš model Card v marketplace, jinak uprav


def marketplace_list(request):
    cards = Card.objects.filter(is_for_sale=True)
    return render(request, 'marketplace/marketplace_list.html', {'cards': cards})


# Create your views here.
