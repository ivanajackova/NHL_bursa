<<<<<<< HEAD
import os
=======
"""
ASGI config for nhl_bursa project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

>>>>>>> d164f05 (akouška save)
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nhl_bursa.settings')

application = get_asgi_application()
<<<<<<< HEAD

=======
>>>>>>> d164f05 (akouška save)
