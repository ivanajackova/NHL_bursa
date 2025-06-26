from django.db import models
from django.conf import settings  # správný import pro AUTH_USER_MODEL

class Card(models.Model):
    NHL_TEAMS = [
        ('BOS', 'Boston Bruins'),
        ('TOR', 'Toronto Maple Leafs'),
        ('MTL', 'Montreal Canadiens'),
        ('CHI', 'Chicago Blackhawks'),
        ('NYR', 'New York Rangers'),
        ('LAK', 'Los Angeles Kings'),
        ('TBL', 'Tampa Bay Lightning'),
        ('EDM', 'Edmonton Oilers'),
        ('COL', 'Colorado Avalanche'),
        ('VGK', 'Vegas Golden Knights'),
        ('VNC', 'Vancouver Canucks'),
        # přidej další týmy podle potřeby
    ]

    name = models.CharField(max_length=100)
    team = models.CharField(max_length=3, choices=NHL_TEAMS)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='cards/')
    is_for_sale = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # klíčová oprava

    def __str__(self):
        return self.name

    #Tato třída Card definuje databázový model v Django – konkrétně model pro hokejovou kartičku