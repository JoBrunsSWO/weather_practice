from rest_framework import serializers
from api.models import WeatherData
from utils import convert_date

class WeatherDataSerializer(serializers.ModelSerializer):
    # Create a serializer for Weather Data with all fields from the model plus id, slightly differing from the data structure in the API Endpoint
    class Meta: 
        model = WeatherData
        fields = '__all__'

    def to_representation(self, instance):
        # Convert the date field to a more readable format
        representation = super().to_representation(instance)
        representation['current_time'] = convert_date(representation['current_time'])
        representation['daily_time'] = [convert_date(day) for day in representation['daily_time']]
        return representation
        
