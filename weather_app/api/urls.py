from django.urls import path
from . import views

urlpatterns = [
    # Define url path for the Weather View
    path('weather/', views.WeatherView.as_view(), name='weather-details'),

]