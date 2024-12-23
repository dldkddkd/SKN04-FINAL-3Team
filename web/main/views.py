from django.conf import settings
from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'ncp_client_id': settings.NCP_CLIENT_ID})

def home(request):
    return render(request, 'index.html')

def planner(request):
    return render(request, 'planner.html')

def profile(request):
    return render(request, 'profile.html')

def settings(request):
    return render(request, 'settings.html')

def myplace(request):
    return render(request, 'myplace.html')