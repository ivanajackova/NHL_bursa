from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.inbox_view, name='inbox'),
]

#Když uživatel přejde na /inbox/, spustí se funkce inbox_view,Funkce (view), která zpracuje zobrazení doručené pošty,Jméno této cesty – lze ji použít v šabloně nebo v přesměrování