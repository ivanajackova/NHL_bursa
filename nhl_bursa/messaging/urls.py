from django.urls import path
from . import views  # musí být tento řádek

urlpatterns = [
    path('inbox/', views.inbox_view, name='inbox'),
]
