from django.shortcuts import render
import os


def map_view(request):
    context = {
        'ncp_client_id': os.getenv('NCP_CLIENT_ID')  # .env 파일에서 가져온 값
    }
    return render(request, 'index.html', context)

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