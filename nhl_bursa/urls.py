
#Importní část souboru urls.py v Django projektech. Slouží ke správnému směrování URL adres a obsluze statických a mediálních souborů.
from django.contrib import admin #Django administrační rozhraní, Umožňuje spravovat databázové záznamy (uživatele, kartičky, zprávy...) přes webové rozhraní.
from django.urls import path, include #Funkce pro definování jednotlivých URL adres, umožňuje vložit URL adresy z jiných aplikací (např. albums, messaging, users...).
from django.conf import settings #Importuje Django nastavení (settings.py), což je nutné pro kontrolu proměnných jako DEBUG, MEDIA_URL, MEDIA_ROOT atd.
from django.conf.urls.static import static #Umožňuje v režimu vývoje (DEBUG = True) obsluhovat statické a mediální soubory přímo Django serverem


urlpatterns = [ #Je hlavní seznam URL cest
    path('admin/', admin.site.urls),
    path('', include('nhl_bursa.albums.urls')), #Kořenová adresa / přesměrovává na aplikaci albums.
    path('messaging/', include('nhl_bursa.messaging.urls')), #Cesty začínající na /messaging/ budou směrovány do messaging aplikace.
]

if settings.DEBUG: #Zajišťuje, že během vývoje (lokálně) bude Django umět obsluhovat mediální soubory (např. obrázky, fotky, soubory nahrané uživateli).
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



