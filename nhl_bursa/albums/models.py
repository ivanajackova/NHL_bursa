from django.db import models
from django.conf import settings

class Card(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cards/')
    description = models.TextField()
    is_for_sale = models.BooleanField(default=False)

    #Tato třída Card definuje databázový model v Django – konkrétně model pro hokejovou kartičku