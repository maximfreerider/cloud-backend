from rest_framework import serializers
from .models import Flight, History


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ('id', 'name', 'come_from', 'come_to', 'avia_company', 'speed', 'registration_info', 'flight_distance')


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('id', 'flight_id', 'start', 'finish')