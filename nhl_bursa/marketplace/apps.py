from django.apps import AppConfig

class MarketplaceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nhl_bursa.marketplace'

#Nastavuje výchozí typ primárního klíče (ID) pro modely v této aplikaci,Určuje plnou cestu k aplikaci jako Python modul.