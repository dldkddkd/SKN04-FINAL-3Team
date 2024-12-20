from django.urls import path
from . import views
from .views import map_view

urlpatterns = [
    path('', views.home, name='home'),
    path('', map_view, name='map_view'),  # map_view로 라우팅
    path('planner/', views.planner, name='planner'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('myplace/', views.myplace, name='myplace'),
]