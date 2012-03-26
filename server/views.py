from django.shortcuts import render
from server.models import server

def home(request):
    s = Server.objects.all()[:30]
    return render(request, 'server_list.html', {'servers': s})
