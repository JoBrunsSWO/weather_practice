from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hourly-weather', views.hourly_weather, name='hourly_weather'),
]