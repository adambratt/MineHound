from django.shortcuts import render
from server.models import server
from django.contrib.auth.decorators import login_required


def dashboard(request):
    servers = server.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'servers': servers})