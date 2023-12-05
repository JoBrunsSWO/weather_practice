from django.db import models
from django.utils import timezone as django_timezone

class WeatherData(models.Model): 
    # Create a model for Weather Data, slightly differing from the data structure in the API Endpoint
    
    # Metadata. These fields are the same as the API Endpoint
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    generationtime_ms = models.FloatField(default=0)
    utc_offset_seconds = models.IntegerField(default=0)
    timezone = models.CharField(max_length=50, default="GMT")
    timezone_abbreviation = models.CharField(max_length=10, default="GMT")
    elevation = models.IntegerField(default=0)

    # Current weather data. In the API Endpoint, they are nested under the "current" key
    current_time = models.DateTimeField(default=django_timezone.now)
    current_interval = models.IntegerField(default=0)
    current_temperature_2m = models.FloatField(default=0)
    current_wind_speed_10m = models.FloatField(default=0)

    # Hourly weather data. In the API Endpoint, they are nested under the "hourly" key
    hourly_time = models.JSONField(default=list)
    hourly_temperature_2m = models.JSONField(default=list)
    hourly_relative_humidity_2m = models.JSONField(default=list)
    hourly_wind_speed_10m = models.JSONField(default=list)

    # String representation of the model
    def __str__(self):
        return f"Weather at ({self.latitude}, {self.longitude})"