from django.urls import path
from .views import inbox_view  # nebo co máš jako výchozí pohled

urlpatterns = [
    path('', inbox_view, name='inbox'),