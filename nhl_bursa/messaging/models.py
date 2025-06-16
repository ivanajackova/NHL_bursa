from django.db import models
from django.db import models
from django.conf import settings

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

#Tato třída Message definuje Django model pro zprávy mezi uživateli v aplikaci messaging. V databázi bude reprezentovat jednu zprávu, kterou uživatel poslal jinému uživateli.