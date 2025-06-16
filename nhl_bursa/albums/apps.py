from django.apps import AppConfig  #Importuje základní třídu AppConfig, kterou Django používá pro konfiguraci každé aplikace.

class AlbumsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' #Výchozí typ primárního klíče pro nové modely
    name = 'nhl_bursa.albums'

#Definuje vlastní konfigurační třídu pro aplikaci albums.
