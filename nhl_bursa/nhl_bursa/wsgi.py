"""
WSGI config for nhl_bursa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
>>>>>>> d164f05 (akouška save)
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nhl_bursa.settings')

application = get_wsgi_application()
