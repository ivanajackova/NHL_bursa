from django.shortcuts import render

from django.shortcuts import render

def inbox_view(request):
    return render(request, 'messaging/inbox.html')

#Tato funkce inbox_view je Django view – obsluhuje požadavek na stránku s doručenými zprávami.