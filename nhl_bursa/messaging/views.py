from django.shortcuts import render

def inbox_view(request):
    return render(request,'messaging/inbox.html')
# Create your views here.
def message_inbox_view():
    return None