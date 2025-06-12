from django.db import models
from nhl_bursa.albums.models import Card

class Listing(models.Model):
    card = models.OneToOneField(Card, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date_listed = models.DateTimeField(auto_now_add=True)

