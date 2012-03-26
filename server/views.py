from django.shortcuts import render
from server.models import server
from django.contrib.auth.decorators import login_required

def home(request):
    s = server.objects.all()[:30]
    sorted(s, key=lambda a: a.today_sessions)
    return render(request, 'server_list.html', {'servers': s})

@login_required
def create(request):
    return render(request, 'server_create.html')
    
def view(request, server_id):
    try:
        s = server.objects.get(pk=server_id)
    except server.DoesNotExist:
        return 
    return render(request, 'server_view.html', {'server': s})