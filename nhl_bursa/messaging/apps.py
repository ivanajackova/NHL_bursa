from django.apps import AppConfig

class MessagingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nhl_bursa.messaging'

#Definuje se vlastní konfigurační třída s názvem MessagingConfig