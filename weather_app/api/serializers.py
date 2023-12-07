from rest_framework import serializers
from api.models import WeatherData

class WeatherDataSerializer(serializers.ModelSerializer):
    # Create a serializer for Weather Data with all fields from the model plus id, slightly differing from the data structure in the API Endpoint
    class Meta: 
        model = WeatherData
        fields = ['id', 'latitude', 'longitude','utc_offset_seconds', 'timezone',
                  'timezone_abbreviation', 'current_time', 'current_temperature_2m',
                  'current_humidity_2m', 'current_weather_code', 'current_wind_speed_10m',
                  'daily_time', 'daily_weather_code', 'daily_temperature_2m_max',
                  'daily_temperature_2m_min', 'daily_precipitation_sum', 
                  'daily_precipitation_probability', 'daily_wind_speed_10m_max'
        ]
        
