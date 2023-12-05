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
        # Make a request to the API Endpoint with a timeout argument so pylint won't hate me
        response = requests.get(WEATHER_API_ENDPOINT, timeout=2.50)
        # Convert the response to Json
        data = response.json()
        # Create a serializer - since the data structure is slightly different from the API Endpoint, I need to specify each field manually
        serializer = WeatherDataSerializer(data={
            'latitude': data['latitude'],
            'longitude': data['longitude'],
            'generationtime_ms': data['generationtime_ms'],
            'utc_offset_seconds': data['utc_offset_seconds'],
            'timezone': data['timezone'],
            'timezone_abbreviation': data['timezone_abbreviation'],
            'elevation': data['elevation'],
            'current_time': data['current']['time'],
            'current_interval': data['current']['interval'],
            'current_temperature_2m': data['current']['temperature_2m'],
            'current_wind_speed_10m': data['current']['wind_speed_10m'],
            'hourly_time': data['hourly']['time'],
            'hourly_temperature_2m': data['hourly']['temperature_2m'],
            'hourly_relative_humidity_2m': data['hourly']['relative_humidity_2m'],
            'hourly_wind_speed_10m': data['hourly']['wind_speed_10m'],
        })
        # Check if the serializer is valid, then save and return the data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # Since we only want to display data, we don't need further methods
