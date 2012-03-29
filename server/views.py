from django.shortcuts import render
from server.models import server
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.utils import simplejson

def home(request):
    s = server.objects.filter(status=1)[:30]
    sorted(s, key=lambda a: a.today_sessions())
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
    
    
def stats(request, stat, server_id):
    try:
        s = server.objects.get(pk=server_id)
    except server.DoesNotExist:
        return Http404
    
    if stat == 'hourly_users':
        return json(s.hourly_sessions())
    elif stat == 'weekly_users':
        return json(s.weekly_sessions())
    
    return Http404
        
        
def json(data):
    return HttpResponse(simplejson.dumps(data))
        
    
