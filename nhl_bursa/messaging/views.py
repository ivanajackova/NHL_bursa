from django.shortcuts import render


from django.shortcuts import render

def inbox_view(request):
    return render(request, 'messaging/inbox.html')
# Create your views here.
