from django.http import HttpResponse
from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import WeatherDataSerializer
from weather_app.settings import WEATHER_API_ENDPOINT


class WeatherView(APIView):
    def get(self, request):
        # Make a request to the API Endpoint, include a timeout argument so pylint won't shout at me
        response = requests.get(WEATHER_API_ENDPOINT, timeout=2.50)
        # Convert the response to Json
        data = response.json()
        # Create a serializer - since the data structure is slightly different from the API Endpoint, I need to specify each field manually
        serializer = WeatherDataSerializer(data={
            'latitude': data['latitude'],
            'longitude': data['longitude'],
            'utc_offset_seconds': data['utc_offset_seconds'],
            'timezone': data['timezone'],
            'timezone_abbreviation': data['timezone_abbreviation'],
            'current_time': data['current']['time'],
            'current_temperature_2m': data['current']['temperature_2m'],
            'current_humidity_2m': data['current']['relative_humidity_2m'],
            'current_weather_code': data['current']['weather_code'],
            'current_wind_speed_10m': data['current']['wind_speed_10m'],
            'daily_time': data['daily']['time'],
            'daily_weather_code': data['daily']['weather_code'],
            'daily_temperature_2m_max': data['daily']['temperature_2m_max'],
            'daily_temperature_2m_min': data['daily']['temperature_2m_min'],
            'daily_precipitation_sum': data['daily']['precipitation_sum'],
            'daily_precipitation_probability': data['daily']['precipitation_probability_max'],
            'daily_wind_speed_10m_max': data['daily']['wind_speed_10m_max']
        })
        # Check if the serializer is valid, then save and return the data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # Since we only want to display data, we don't need further methods
