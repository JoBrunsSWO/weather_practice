from rest_framework import serializers
from api.models import WeatherData

class WeatherDataSerializer(serializers.ModelSerializer):
    # Create a serializer for Weather Data with all fields from the model plus id, slightly differing from the data structure in the API Endpoint
    class Meta: 
        model = WeatherData
        fields = ['id', 'latitude', 'longitude', 'generationtime_ms',
                  'utc_offset_seconds', 'timezone', 'timezone_abbreviation',
                  'elevation', 'current_time', 'current_interval', 'current_temperature_2m',
                  'current_wind_speed_10m', 'hourly_time', 'hourly_temperature_2m',
                  'hourly_relative_humidity_2m', 'hourly_wind_speed_10m']
        
