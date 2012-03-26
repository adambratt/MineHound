from django.shortcuts import render
from server.models import server
from django.contrib.auth.decorators import login_required

def home(request):
    s = server.objects.all()[:30]
    return render(request, 'server_list.html', {'servers': s})

@login_required
def create(request):
    return render(request, 'server_create.html')