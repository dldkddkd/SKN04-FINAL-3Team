from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('', views.home, name='home'),
    path('', index, name='index'),  # index 라우팅
    path('planner/', views.planner, name='planner'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('myplace/', views.myplace, name='myplace'),
]