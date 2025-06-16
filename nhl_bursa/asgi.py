import os #Import modul os, který umožňuje práci s prostředím
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nhl_bursa.settings')

application = get_asgi_application()  #vytvoří objekt application, který pak  server  použije k běhu  aplikace.

