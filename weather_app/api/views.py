from django.http import HttpResponse
from django.shortcuts import render
import requests


def index(request):
    api_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

    try:
        response = requests.get(api_url, timeout=2.50)
        if response.status_code == 200:
            api_data = response.json()
            return render(request, 'api/external_api_view.html', {'api_data': api_data})
        else:
            return render(request, 'api/error_template.html', {'error_message': f"API request failed with status code {response.status_code}"})
    except Exception as e:
        return render(request, 'api/error_template.html', {'error_message': f"An error occurred: {str(e)}"})   


def hourly_weather(request):
    api_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    try:
        response = requests.get(api_url, timeout=2.50)
        if response.status_code == 200:
            api_data = response.json()
            time = api_data['hourly']['time']
            temperature = api_data['hourly']['temperature_2m']
            humidity = api_data['hourly']['relative_humidity_2m']
            wind_speed = api_data['hourly']['wind_speed_10m']
            hourly_data = list(zip(time, temperature, humidity, wind_speed))
            return render(request, 'api/hourly_weather_view.html', {'hourly_data': hourly_data})
        else:
            return render(request, 'api/error_template.html', {'error_message': f"API request failed with status code {response.status_code}"})
    except Exception as e:
        return render(request, 'api/error_template.html', {'error_message': f"An error occurred: {str(e)}"})   
