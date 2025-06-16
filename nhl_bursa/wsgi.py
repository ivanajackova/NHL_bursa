"""
WSGI config for nhl_bursa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nhl_bursa.settings')

application = get_wsgi_application()

#Tento kód je součástí souboru wsgi.py, který Django používá při nasazení aplikace na produkční server Render.