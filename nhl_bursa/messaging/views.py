from django.shortcuts import render


def inbox_view(request):
    return render(request, 'messaging/inbox.html')


from django.shortcuts import render

# Create your views here.
