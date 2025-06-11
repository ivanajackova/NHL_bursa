"""
URL configuration for nhl_bursa project.

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
=======
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
>>>>>>> d164f05 (akouška save)
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

<<<<<<< HEAD
=======
urlpatterns = [
    path('admin/', admin.site.urls),
]

>>>>>>> d164f05 (akouška save)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('albums.urls')),
<<<<<<< HEAD
    path('messaging/', include('messaging.urls')),
    # TOTO PŘIDEJ
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




>>>>>>> d164f05 (akouška save)
